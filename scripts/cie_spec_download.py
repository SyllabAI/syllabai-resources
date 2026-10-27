#!/usr/bin/env python3
"""T-SPECS-CIE-1 — Download + register official CIE syllabus PDFs.

Input : .cache/sme_spec/cie_course_specs.json (from cie_spec_discover.py)
        + MANUAL entries for the 3 lanes whose SME card is null
          (the Edexcel Science-Double-Award precedent; newest published
          edition from the Cambridge qualification page).
Output: Official-Specifications/<cie-qual-slug>/<original-filename>.pdf
        Official-Specifications/<cie-qual-slug>/spec.json
        Official-Specifications/manifest.json  (Edexcel entries untouched,
        CIE entries appended; totals updated)
        scripts/cie_spec_edexcel_snapshot.json (pre-change entry hashes,
        for the verify lane's byte-stability guard)

Validation per PDF: %PDF magic, pypdf page count, sha1, cover_code
detection from the cover text (years 1990-2035 excluded from the 4-digit
code candidates). Resumable: skips a group whose spec.json validates.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
import time
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import pypdf

REPO = Path("/home/z/my-project/syllabai-resources")
OUT = REPO / "Official-Specifications"
CACHE = Path("/home/z/my-project/.cache/sme_spec/cie_course_specs.json")
SNAP = REPO / "scripts" / "cie_spec_edexcel_snapshot.json"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

MANUAL = {
    # SME leaves courseExamSpecificationPdfLink null on the three "-25" IGCSE
    # lanes (same class as the Edexcel 4SD0 double-award case). URLs taken
    # from the official Cambridge qualification pages (newest published
    # edition — the same convention SME itself uses on cie-igcse-business-25
    # and cie-igcse-economics-25):
    "cie-igcse-accounting-25": {
        "url": "https://www.cambridgeinternational.org/Images/718141-2027-2029-syllabus.pdf",
        "sme_source_url": None,
        "discovered_via": "manual:cambridge-qualification-page (SME card null)",
    },
    "cie-igcse-english-language-25": {
        "url": "https://www.cambridgeinternational.org/Images/718783-2027-2029-syllabus.pdf",
        "sme_source_url": None,
        "discovered_via": "manual:cambridge-qualification-page (SME card null)",
    },
    "cie-igcse-environmental-management-25": {
        "url": "https://www.cambridgeinternational.org/Images/718156-2027-2029-syllabus.pdf",
        "sme_source_url": None,
        "discovered_via": "manual:cambridge-qualification-page (SME card null)",
    },
    # SME's card points at the retired 2022-2024 edition (HTTP 404 at
    # cambridgeinternational.org). Substituted with the newest published
    # edition from the official 8021 qualification page; the stale SME link
    # is preserved as sme_source_url (the Edexcel stale-business-link
    # precedent):
    "cie-as-english-general-paper-21": {
        "url": "https://www.cambridgeinternational.org/Images/743333-2028-2030-syllabus.pdf",
        "sme_source_url": "https://www.cambridgeinternational.org/Images/557265-2022-2024-syllabus.pdf",
        "discovered_via": "manual:cambridge-qualification-page (SME card stale — retired edition 404)",
    },
}

VARIANT_TOKENS = {"core", "extended", "biology", "chemistry", "physics"}


def fetch(url: str, tries: int = 3) -> bytes:
    last: Exception | None = None
    for i in range(tries):
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent": UA, "Accept": "application/pdf,*/*"})
            with urllib.request.urlopen(req, timeout=120) as resp:
                return resp.read()
        except Exception as exc:  # noqa: BLE001
            last = exc
            time.sleep(2 + 3 * i)
    raise RuntimeError(f"fetch failed after {tries} tries: {url}: {last!r}")


def subject_slug(slugs: list[str]) -> str:
    base = [s[len("cie-"):] if s.startswith("cie-") else s for s in slugs]
    multi = len(base) > 1
    if multi:
        pref = os_common(base)
        cand = pref  # os_common already truncates at the last dash
        if not cand or cand in ("cie", "cie-"):
            cand = base[0]
    else:
        cand = base[0]
    changed = True
    while changed:
        changed = False
        cand = cand.rstrip("-")
        toks = cand.split("-")
        if toks and re.fullmatch(r"\d{2}", toks[-1]):
            toks = toks[:-1]
            changed = True
        elif multi and toks and toks[-1] in VARIANT_TOKENS:
            toks = toks[:-1]
            changed = True
        cand = "-".join(toks)
    return "cie-" + cand


def os_common(items: list[str]) -> str:
    pref = ""
    for ch_idx in range(min(len(s) for s in items)):
        ch = items[0][ch_idx]
        if all(s[ch_idx] == ch for s in items):
            pref += ch
        else:
            break
    return pref[:pref.rfind("-")] if "-" in pref else pref


def window_of(url_or_name: str) -> str:
    m = re.search(r"(\d{4}-\d{4}|\d{4})-syllabus", url_or_name)
    return m.group(1) if m else "unknown"


def codes_from_pdf(pdf_path: Path, pages: int) -> tuple[str, list[str], str, str]:
    reader = pypdf.PdfReader(str(pdf_path))
    cover_text = ""
    all_front = ""
    for i in range(min(5, len(reader.pages))):
        try:
            t = reader.pages[i].extract_text() or ""
        except Exception:  # noqa: BLE001
            t = ""
        all_front += t + "\n"
        if i < 2:
            cover_text += t + "\n"
    tokens = Counter(re.findall(r"\b(\d{4})\b", all_front))
    cands = {t: n for t, n in tokens.items()
             if not (1990 <= int(t) <= 2035) and n >= 2}
    cover_code = None
    m = re.search(r"Cambridge (?:IGCSE|International AS & A Level|Advanced[^\n]*)"
                  r"[^\n]{0,120}?(\d{4})", cover_text)
    if m and not (1990 <= int(m.group(1)) <= 2035):
        cover_code = m.group(1)
    if cover_code is None and cands:
        cover_code = max(cands, key=lambda k: (cands[k], k))
    title = (reader.metadata or {}).get("/Title") or None
    author = (reader.metadata or {}).get("/Author") or None
    if title:
        title = str(title).strip()[:200]
    if author:
        author = str(author).strip()[:80]
    spec_codes = sorted(cands) if cands else ([cover_code] if cover_code else [])
    return cover_code or "?", spec_codes, title or "?", author or "?"


def main() -> int:
    disc = json.loads(CACHE.read_text())
    lanes = disc["lanes"]
    effective: dict[str, dict] = {}
    for slug, e in lanes.items():
        m = MANUAL.get(slug)
        if m:
            effective[slug] = {"url": m["url"], "sme_source_url": m["sme_source_url"],
                               "discovered_via": m["discovered_via"]}
            continue
        effective[slug] = {"url": e.get("spec_link"),
                           "sme_source_url": None,
                           "discovered_via": "sme:courseExamSpecificationPdfLink"}
    missing = [s for s, v in effective.items() if not v["url"]]
    if missing:
        print("UNRESOLVED LANES (no SME link, no MANUAL):", missing)
        return 1

    groups: dict[str, list[str]] = {}
    for slug, v in effective.items():
        groups.setdefault(v["url"], []).append(slug)
    print(f"groups: {len(groups)} unique PDFs for {len(effective)} lanes")

    manifest_path = OUT / "manifest.json"
    manifest = json.loads(manifest_path.read_text())
    if not SNAP.exists():
        SNAP.write_text(json.dumps(
            {e["slug"]: hashlib.sha256(json.dumps(e, sort_keys=True).encode())
             .hexdigest() for e in manifest["qualifications"]}, indent=1))
        print(f"edexcel snapshot written: {len(manifest['qualifications'])} entries")

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    added, skipped, failed = 0, 0, []
    for url in sorted(groups):
        slugs = sorted(groups[url])
        fname = url.rstrip("/").rsplit("/", 1)[-1]
        win = window_of(url)
        qual = f"{subject_slug(slugs)}-{win}"
        qdir = OUT / qual
        spec_json = qdir / "spec.json"
        pdf_path = qdir / fname
        if spec_json.exists():
            try:
                rec = json.loads(spec_json.read_text())
                if hashlib.sha1(pdf_path.read_bytes()).hexdigest() == rec["sha1"]:
                    skipped += 1
                    continue
            except Exception:  # noqa: BLE001
                pass
        qdir.mkdir(parents=True, exist_ok=True)
        try:
            blob = fetch(url)
            if not blob.startswith(b"%PDF"):
                raise RuntimeError(f"not a PDF ({blob[:20]!r})")
        except Exception as exc:  # noqa: BLE001
            failed.append({"url": url, "lanes": slugs, "error": repr(exc)[:160]})
            print(f"  FAIL {url} lanes={slugs}: {exc!r}")
            continue
        pdf_path.write_bytes(blob)
        sha1 = hashlib.sha1(blob).hexdigest()
        reader = pypdf.PdfReader(str(pdf_path))
        pages = len(reader.pages)
        cover_code, spec_codes, title, author = codes_from_pdf(pdf_path, pages)
        rec = {
            "slug": qual,
            "board": "cambridge-cie",
            "pdf": fname,
            "source_url": url,
            "sme_source_url": effective[slugs[0]]["sme_source_url"],
            "http_content_type": "application/pdf",
            "sha1": sha1,
            "bytes": len(blob),
            "pages": pages,
            "edition_window": win,
            "spec_codes": spec_codes,
            "cover_code": cover_code,
            "pdf_title": title,
            "pdf_author": author,
            "sme_courses": slugs,
            "discovered_via": effective[slugs[0]]["discovered_via"],
            "fetched_utc": now,
        }
        spec_json.write_text(json.dumps(rec, indent=1) + "\n")
        added += 1
        print(f"  OK {qual}: {fname} sha1={sha1[:10]} pages={pages} cover={cover_code} lanes={len(slugs)}")
        time.sleep(1.0)

    have = {e["slug"] for e in manifest["qualifications"]}
    merged = 0
    for url in sorted(groups):
        slugs = sorted(groups[url])
        fname = url.rstrip("/").rsplit("/", 1)[-1]
        win = window_of(url)
        qual = f"{subject_slug(slugs)}-{win}"
        if qual in have:
            continue
        rec = json.loads((OUT / qual / "spec.json").read_text())
        manifest["qualifications"].append(rec)
        have.add(qual)
        merged += 1
    manifest["generated_utc"] = now
    src = manifest["source"]
    src["cie_provider"] = "Cambridge International Education (cambridgeinternational.org)"
    if "manual" not in src["discovered_via"]:
        src["discovered_via"] += ("; CIE syllabuses via SME course cards, 3 newest-edition "
                                  "manuals from the Cambridge qualification pages where the SME card is null")
    cie_lanes_covered = sum(len(e["sme_courses"]) for e in manifest["qualifications"]
                            if e.get("board") == "cambridge-cie")
    manifest["totals"] = {
        "qualifications": len(manifest["qualifications"]),
        "sme_courses_covered": 49 + cie_lanes_covered,
        "sme_courses_total": 93,
        "missing_courses": [],
    }
    manifest_path.write_text(json.dumps(manifest, indent=1) + "\n")
    if failed:
        (OUT / "_cie_failed_downloads.json").write_text(json.dumps(failed, indent=1) + "\n")
    print(f"\ndownloaded={added} skipped(resume)={skipped} failed={len(failed)} manifest_merged={merged} "
          f"quals_total={manifest['totals']['qualifications']} cie_lanes_covered={cie_lanes_covered}")
    return 0 if not failed else 2


if __name__ == "__main__":
    sys.exit(main())
