#!/usr/bin/env python3
"""Probe: does SME link official specifications anywhere?

Targets:
1. Course landing page (igcse/chemistry/edexcel/19/)
2. One revision-note page (cached probes said specPoint attrs = id/name/definition/video)
3. Topic-questions page
4. SME sitemap for pages containing 'specification' in URL
Scan raw HTML (not just __NEXT_DATA__) for:
- 'specification' mentions with hrefs
- pearson / qualifications / edexcel.com / aqa / ocr / cambridge links
- any .pdf hrefs
"""
from __future__ import annotations

import json
import re
import urllib.request
from pathlib import Path

CACHE = Path("/home/z/my-project/.cache/sme_spec_probe.json")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

PAGES = {
    "course_landing": "https://www.savemyexams.com/igcse/chemistry/edexcel/19/",
    "revision_note": ("https://www.savemyexams.com/igcse/chemistry/edexcel/19/revision-notes/"
                      "1-principles-of-chemistry/1-5-chemical-formulae-equations-calculations/"
                      "1-5-3-moles-mass-and-rfm/"),
    "topic_questions": ("https://www.savemyexams.com/igcse/chemistry/edexcel/19/topic-questions/"
                        "1-principles-of-chemistry/1-1-states-of-matter/exam-questions/"),
}

# probe sitemap too
SITEMAPS = [
    "https://www.savemyexams.com/sitemap.xml",
    "https://www.savemyexams.com/sitemap_index.xml",
]


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA,
                                               "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=45) as resp:
        return resp.read()


HREF_RE = re.compile(r'href="([^"]+)"', re.I)
SPEC_WORDS = re.compile(r'specification|syllabus', re.I)
BOARD_RE = re.compile(
    r'qualifications\.pearson\.com|pearsonschools|edexcel\.com|aqa\.org\.uk|'
    r'ocr\.org\.uk|cambridgeinternational\.org|wjec|eduqas|\.pdf', re.I)


def scan(name: str, html: str, out: dict) -> None:
    hrefs = HREF_RE.findall(html)
    board_links = sorted({h for h in hrefs if BOARD_RE.search(h)})
    # any text near 'specification'
    spec_hrefs = sorted({h for h in hrefs if SPEC_WORDS.search(h)})
    # also scan raw text mentions around 'specification' (first 5 contexts)
    ctx = []
    for m in list(SPEC_WORDS.finditer(html))[:8]:
        s = max(0, m.start() - 120)
        e = min(len(html), m.end() + 120)
        ctx.append(re.sub(r'\s+', ' ', html[s:e]))
    out[name] = {
        "bytes": len(html),
        "board_links": board_links[:40],
        "spec_word_hrefs": spec_hrefs[:40],
        "spec_contexts": ctx,
        "n_hrefs": len(hrefs),
    }


def main() -> int:
    out: dict = {}
    for name, url in PAGES.items():
        try:
            html = fetch(url).decode("utf-8", errors="replace")
            scan(name, html, out)
            print(f"[ok] {name}: {len(html)} bytes")
        except Exception as exc:  # noqa: BLE001
            out[name] = {"error": repr(exc)}
            print(f"[err] {name}: {exc!r}")

    # sitemap discovery (may 404 or be index)
    sm: dict = {}
    for url in SITEMAPS:
        try:
            body = fetch(url).decode("utf-8", errors="replace")
            urls = re.findall(r"<loc>([^<]+)</loc>", body)
            spec_urls = [u for u in urls if SPEC_WORDS.search(u)]
            sm[url] = {"n_loc": len(urls), "spec_urls": spec_urls[:50],
                       "is_index": "sitemapindex" in body,
                       "child_locs": [u for u in urls if u.endswith(".xml")][:20]}
            print(f"[ok] {url}: {len(urls)} locs")
        except Exception as exc:  # noqa: BLE001
            sm[url] = {"error": repr(exc)}
            print(f"[err] {url}: {exc!r}")
    out["sitemaps"] = sm

    CACHE.write_text(json.dumps(out, indent=1))
    print(f"saved -> {CACHE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
