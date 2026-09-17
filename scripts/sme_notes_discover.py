#!/usr/bin/env python3
"""Fetch SME sitemaps and classify the 39 Edexcel exam-question courses by
the URL shape of their revision-notes trees.

single-segment : notes at /{level}/{subject}/edexcel/{mid}/revision-notes/...
extra-segment  : notes need an extra path segment (unit / variant / science)

Writes /home/z/my-project/.cache/sme_notes_urls.json (course -> note urls).
stdlib-only; no secrets involved (public sitemaps).
"""
from __future__ import annotations

import json
import re
import sys
import time
import urllib.request
from pathlib import Path

CACHE = Path("/home/z/my-project/.cache")
REG = Path("/home/z/my-project/download/syllabai-resources/SME-ExamQuestion/manifest.json")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")


def fetch(url: str, timeout: int = 60) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def get(url: str) -> bytes:
    last = None
    for a in range(3):
        try:
            return fetch(url)
        except Exception as exc:  # noqa: BLE001
            last = exc
            time.sleep(2 * (a + 1))
    raise RuntimeError(f"fetch failed x3: {url} ({last})")


def sitemap_urls(xml: bytes) -> list[str]:
    return re.findall(r"<loc>\s*(.*?)\s*</loc>", xml.decode("utf-8", "replace"))


def main() -> int:
    index = sitemap_urls(get("https://www.savemyexams.com/sitemap.xml"))
    print(f"sitemap index entries: {len(index)}")
    level_maps = [u for u in index
                  if re.search(r"/(igcse|international-a-level)[-/]", u)
                  and u.endswith(".xml")]
    if not level_maps:
        level_maps = index
    print(f"level sitemaps: {len(level_maps)}")
    for u in level_maps[:20]:
        print("  ", u)

    urls: list[str] = []
    for sm in level_maps:
        us = sitemap_urls(get(sm))
        urls.extend(us)
        print(f"  {sm.rsplit('/', 1)[-1]}: {len(us)} urls")
    notes = [u for u in urls if "/revision-notes/" in u]
    print(f"total urls {len(urls)} | revision-notes urls {len(notes)}")

    reg = json.loads(REG.read_text())
    courses = reg["courses"]
    report = {}
    for c in courses:
        level, subject, mid = c["level"], c["subject"], c["mid"]
        base = f"https://www.savemyexams.com/{level}/{subject}/edexcel/{mid}/revision-notes/"
        direct = [u for u in notes if u.startswith(base)]
        # find what other prefixes exist for this subject/level
        subj_prefix = f"https://www.savemyexams.com/{level}/{subject}/edexcel/"
        alt = sorted({u[len(subj_prefix):].split("/revision-notes/")[0]
                      for u in notes if u.startswith(subj_prefix)})
        report[c["slug"]] = {
            "notes_base": base,
            "direct_pages": len(direct),
            "alt_variant_prefixes": alt,
            "kind": ("single-segment" if direct and
                     all(a == mid for a in alt) else "extra-segment"),
        }
        print(f"{c['slug']:55s} {report[c['slug']]['kind']:14s} "
              f"direct={len(direct):4d} alt={alt}")

    out = CACHE / "sme_notes_urls.json"
    out.write_text(json.dumps({"notes_urls_total": len(notes),
                               "notes_urls": sorted(notes),
                               "courses": report}, indent=1),
                   encoding="utf-8")
    print(f"saved {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
