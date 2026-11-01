#!/usr/bin/env python3
"""Fetch Pearson international grade-boundary PDFs (slug-matrix probe).

Pearson has never kept one stable URL slug per session — the June 2025 doc
lives at `grade-boundaries-june-2025-int-gcse.pdf` while June 2026 is
`grade-boundaries-june-2026-international-gcse.pdf`. The fetcher therefore
probes a small slug matrix per session and family and keeps the first hit
that verifies as a real PDF (%PDF magic + a final URL that is not Pearson's
/campaigns/404.html). Every miss is recorded — absence is data (covid
sessions, not-yet-published series).

Families:
  pearson-int-gcse-linear   International-GCSE/  (4CH1, 4MA1, ... linear 9-1/A*-G)
  pearson-int-gcse-modular  International-GCSE/  (4XCH1, 4XMA1, ... modular units + UMS)
  pearson-ial               International-A-level/  (WCH11.., X/Y cash-ins, UMS)
"""
from __future__ import annotations

import argparse
import json
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from gb_common import (MANIFEST, RAW, http_get, manifest_append,
                       manifest_lookup, now_utc, pdf_ok, session_list,
                       session_slug, sha256_bytes)

BASE = "https://qualifications.pearson.com/content/dam/pdf/Support/Grade-boundaries"

# Pearson has never kept one stable slug: 2024+ docs use
# `grade-boundaries-<month>-<year>-<family>.pdf`; older docs used a YYMM
# prefix (`1906-ig-9-1-subject-grade-boundaries.pdf`,
# `2201_intGCSE_(9-1)_Subject_Grade_Boundaries_V1.pdf`,
# `2001-ial-grade-boundaries.pdf`, ...). The fetcher probes the full
# discovered matrix per session and keeps the first variant that verifies
# as a real PDF (%PDF magic + a final URL that is not Pearson's
# /campaigns/404.html).

FAMILY_SLUGS: dict[str, tuple[str, list[str]]] = {
    "pearson-int-gcse-linear": (
        "International-GCSE",
        ["grade-boundaries-{s}-int-gcse.pdf",
         "grade-boundaries-{s}-international-gcse.pdf",
         "{ym}-ig-9-1-subject-grade-boundaries.pdf",
         "{ym}-int-gcse-grade-boundaries.pdf",
         "{ym}_intGCSE_(9-1)_Subject_Grade_Boundaries_V1.pdf",
         "{ym}-intgcse-9-1-subject-grade-boundaries.pdf",
         "{ym}-international-gcse-subject-grade-boundaries.pdf",
         "{ym}-int-gcse-subject-grade-boundaries.pdf"],
    ),
    "pearson-int-gcse-modular": (
        "International-GCSE",
        ["grade-boundaries-{s}-international-gcse-modular.pdf",
         "grade-boundaries-{s}-int-gcse-modular.pdf"],
    ),
    "pearson-ial": (
        "International-A-level",
        ["grade-boundaries-{s}-international-advanced-level.pdf",
         "grade-boundaries-{s}-ial.pdf",
         "{ym}-ial-grade-boundaries.pdf",
         "{ym}-int-a-level-grade-boundaries.pdf"],
    ),
}


def probe(family: str, session: str, force: bool) -> dict:
    """Download the first slug variant that verifies; return a report row."""
    out: dict = {"family": family, "session": session, "status": "missing"}
    if not force:
        prior = manifest_lookup(family, session)
        if prior:
            f = RAW / family / f"{session}.pdf"
            if f.exists() and pdf_ok(f.read_bytes()[:8]):
                return {**out, "status": "cached",
                        "sha256": prior["sha256"], "url": prior["url"]}
    folder, slugs = FAMILY_SLUGS[family]
    s = session_slug(session)
    month_num = {"january": "01", "february": "02", "june": "06",
                 "october": "10", "november": "11"}[s.split("-")[0]]
    ym = s.split("-")[1][2:] + month_num               # 'January 2023' -> '2301'
    for slug in slugs:
        url = f"{BASE}/{folder}/{slug.format(s=s, ym=ym)}"
        code, body, final = http_get(url)
        if code == 200 and pdf_ok(body) and "404" not in final:
            dest = RAW / family
            dest.mkdir(parents=True, exist_ok=True)
            (dest / f"{session}.pdf").write_bytes(body)
            sha = sha256_bytes(body)
            manifest_append(family, session, url, final, sha, len(body))
            return {**out, "status": "fetched", "sha256": sha[:16],
                    "bytes": len(body), "url": url}
        if code == 200 and "404" in final:
            continue          # Pearson's soft-404 page
        if code != 200:
            continue
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--sessions", nargs="*", help="subset, e.g. 'June 2026'")
    args = ap.parse_args()

    sessions = args.sessions or session_list()
    jobs = [(fam, s) for fam in FAMILY_SLUGS for s in sessions]
    report: list[dict] = []
    with ThreadPoolExecutor(max_workers=6) as ex:
        futs = {ex.submit(probe, fam, s, args.force): (fam, s)
                for fam, s in jobs}
        for f in as_completed(futs):
            report.append(f.result())

    by: dict[str, list[dict]] = {}
    for r in report:
        by.setdefault(r["family"], []).append(r)
    for fam, rows in sorted(by.items()):
        got = [r["session"] for r in rows if r["status"] in ("fetched", "cached")]
        print(f"{fam}: {len(got)} docs -> {', '.join(sorted(got)) or 'NONE'}")
    total = sum(1 for r in report if r["status"] in ("fetched", "cached"))
    print(f"TOTAL {total}/{len(jobs)} docs (manifest: {MANIFEST})")
    missing = sorted((r["family"], r["session"]) for r in report
                     if r["status"] == "missing")
    if missing:
        (RAW / "fetch-missing.json").write_text(json.dumps(
            {"generated": now_utc(), "missing": missing}, indent=2))
        print(f"absent sessions recorded: {len(missing)} "
              f"(raw/fetch-missing.json)")
    # A lane with ZERO documents is a hard failure (source outage?), a
    # partial set is normal (sessions genuinely do not exist).
    sys.exit(0 if total > 0 else 2)


if __name__ == "__main__":
    main()
