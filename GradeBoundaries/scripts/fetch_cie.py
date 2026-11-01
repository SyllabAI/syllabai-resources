#!/usr/bin/env python3
"""Fetch Cambridge International grade-threshold PDFs (session-listing crawl).

The hub listing pages under /grade-threshold-tables/<session>/ ARE
server-rendered and link every syllabus threshold PDF as
/Images/<id>-<subject>-<code>-<season>-<year>-grade-threshold-table.pdf —
so the needed document ids are mechanically harvestable (the earlier
"JS-rendered, not crawlable" conclusion only held for the syllabus pages).
This fetcher crawls WANTED_SESSIONS for both programme levels, keeps every
link whose syllabus code is in WANTED_CODES (the course-map syllabi), and
records the listing page as provenance. CIE_IDS stays as the verified
known-ID fallback seed; missing wanted combos land in fetch-missing.json —
absence is data too, never invented.
"""
from __future__ import annotations

import argparse
import html
import json
import re
from concurrent.futures import ThreadPoolExecutor

from gb_common import (RAW, http_get, manifest_append, manifest_lookup,
                       now_utc, pdf_ok, session_slug, sha256_bytes)

BASE = "https://www.cambridgeinternational.org"

# server-rendered listing pages, per programme level
SESSION_PAGES = {
    "igcse": (BASE
              + "/programmes-and-qualifications/cambridge-upper-secondary"
                "/cambridge-igcse/grade-threshold-tables/{slug}/"),
    "alevel": (BASE
               + "/programmes-and-qualifications/cambridge-advanced"
                 "/cambridge-international-as-and-a-levels"
                 "/grade-threshold-tables/{slug}/"),
}

# Syllabus codes the hub course map needs (mapping/course-map.yaml). 0xxx =
# Cambridge IGCSE; 8xxx/9xxx = Cambridge International AS & A Level.
WANTED_CODES = {
    # IGCSE
    "0264", "0417", "0450", "0452", "0455", "0460", "0470", "0475", "0478",
    "0490", "0500", "0580", "0606", "0607", "0610", "0620", "0625", "0653",
    "0680", "0973",
    # AS & A Level
    "8021", "8291", "9609", "9618", "9696", "9700", "9701", "9702", "9706",
    "9708", "9709",
}

# Sessions to crawl, newest first. June is the full international series;
# November is the broad second series (March is the India-only subset and
# is deliberately out of scope for this wave).
WANTED_SESSIONS = ["June 2026", "June 2025", "November 2025", "November 2024"]

LINK_RE = re.compile(
    r"/Images/(\d+)-([a-z0-9-]+)-(\d{4})"
    r"-(june|march|november)-(\d{4})-grade-threshold-table\.pdf")

# syllabus -> session -> (document id, url filename). Verified known-ID
# seed kept as a fallback for anything the listing crawl cannot see yet.
CIE_IDS: dict[str, dict[str, tuple[int, str]]] = {
    "0620": {  # Chemistry IGCSE
        "June 2025": (741360, "741360-chemistry-0620-june-2025-grade-threshold-table.pdf"),
        "June 2026": (762856, "762856-chemistry-0620-june-2026-grade-threshold-table.pdf"),
    },
    "0625": {  # Physics IGCSE
        "June 2024": (716106, "716106-physics-0625-june-2024-grade-threshold-table.pdf"),
        "June 2026": (762857, "762857-physics-0625-june-2026-grade-threshold-table.pdf"),
    },
    "0580": {  # Mathematics (without coursework) IGCSE
        "June 2025": (741420, "741420-mathematics-without-coursework-0580-june-2025-grade-threshold-table.pdf"),
        "June 2026": (762852, "762852-mathematics-without-coursework-0580-june-2026-grade-threshold-table.pdf"),
    },
    "9609": {  # Business IAL
        "June 2026": (761507, "761507-business-9609-june-2026-grade-threshold-table.pdf"),
    },
    "9700": {  # Biology IAL
        "June 2026": (761524, "761524-biology-9700-june-2026-grade-threshold-table.pdf"),
    },
    "9701": {  # Chemistry IAL
        "June 2026": (761525, "761525-chemistry-9701-june-2026-grade-threshold-table.pdf"),
    },
}


def harvest_listing(level: str, session: str) -> dict[str, str]:
    """code -> pdf URL, harvested from one server-rendered session page."""
    url = SESSION_PAGES[level].format(slug=session_slug(session))
    code_, body, final = http_get(url)
    if code_ != 200 or not body:
        print(f"listing {level} {session}: HTTP {code_}")
        return {}
    found: dict[str, str] = {}
    text = html.unescape(body.decode("utf-8", "replace"))
    for m in LINK_RE.finditer(text):
        doc_id, _slug, syll, season, year = m.groups()
        code = syll
        if code not in WANTED_CODES:
            continue
        got_session = f"{season.capitalize()} {year}"
        if got_session != session:
            continue
        found.setdefault(code, f"{BASE}{m.group(0)}")
    print(f"listing {level} {session}: {len(found)} wanted codes")
    return found


def _download(job: tuple[str, str, str]):
    """(code, session, url) -> (code, session, ok, body) — network only."""
    code, session, url = job
    http_code, body, _ = http_get(url, timeout=45)
    return code, session, http_code == 200 and pdf_ok(body), body


def fetch_one(code: str, session: str, url: str, body: bytes | None = None) -> bool:
    out_dir = RAW / "cie" / code
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / f"{session}.pdf"
    if dest.exists() and manifest_lookup(f"cie-{code}", session):
        print(f"cie {code} {session}: cached")
        return True
    if body is None:
        http_code, body, final = http_get(url)
    else:
        http_code, final = 200, url
    if http_code == 200 and pdf_ok(body):
        dest.write_bytes(body)
        manifest_append(f"cie-{code}", session, url, final,
                        sha256_bytes(body), len(body))
        print(f"cie {code} {session}: fetched {len(body)} bytes")
        return True
    print(f"cie {code} {session}: MISSING (http {http_code}) {url}")
    return False


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    _ = args  # cached docs are always honoured; --force is a manual rm

    harvest: dict[str, dict[str, str]] = {}
    listings = [(level, s) for s in WANTED_SESSIONS
                for level in ("igcse", "alevel")]
    with ThreadPoolExecutor(max_workers=8) as pool:
        for (level, session), found in zip(
                listings, pool.map(
                    lambda ls: harvest_listing(*ls), listings)):
            for code, url in found.items():
                harvest.setdefault(code, {})[session] = url

    # known-ID seed fills anything the crawl missed (verified ids only)
    for code, sessions in CIE_IDS.items():
        for session, (_doc_id, fname) in sessions.items():
            if session in WANTED_SESSIONS:
                harvest.setdefault(code, {}).setdefault(
                    session, f"{BASE}/Images/{fname}")

    jobs: list[tuple[str, str, str]] = []
    for code in sorted(harvest):
        for session in WANTED_SESSIONS:
            url = harvest[code].get(session)
            if url is not None:
                jobs.append((code, session, url))
    ok = 0
    missing: list[dict] = []
    done: dict[tuple[str, str], bytes] = {}
    with ThreadPoolExecutor(max_workers=8) as pool:
        for code, session, okdl, body in pool.map(_download, jobs):
            done[(code, session)] = body if okdl else b""
            print(f"download cie {code} {session}: "
                  f"{len(body) if okdl else 'FAIL'}")
    for code in sorted(WANTED_CODES):
        for session in WANTED_SESSIONS:
            url = harvest.get(code, {}).get(session)
            if url is None:
                missing.append({"code": code, "session": session,
                                "reason": "not in listing"})
                continue
            body = done.get((code, session)) or None
            if fetch_one(code, session, url, body):
                ok += 1
            else:
                missing.append({"code": code, "session": session,
                                "reason": "download failed", "url": url})
    print(f"CIE TOTAL {ok} docs present, {len(missing)} wanted-but-absent")

    (RAW / "cie" / "ID-REGISTRY.json").write_text(json.dumps({
        "generated": now_utc(),
        "method": "session-listing crawl + verified known-ID seed",
        "listingPages": SESSION_PAGES,
        "sessions": WANTED_SESSIONS,
        "wantedCodes": sorted(WANTED_CODES),
        "ids": CIE_IDS,
    }, indent=2))
    miss_path = RAW / "fetch-missing.json"
    try:
        prev = json.loads(miss_path.read_text()) if miss_path.exists() else {}
    except json.JSONDecodeError:
        prev = {}
    prev["cie"] = {
        "generated": now_utc(),
        "wanted": sorted(WANTED_CODES),
        "sessions": WANTED_SESSIONS,
        "missing": missing,
    }
    miss_path.write_text(json.dumps(prev, indent=2))


if __name__ == "__main__":
    main()
