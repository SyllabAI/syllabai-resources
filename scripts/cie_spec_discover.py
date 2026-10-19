#!/usr/bin/env python3
"""T-SPECS-CIE-1 — Discover official CIE syllabus PDF links for all CIE lanes.

For every `cie-*` course in SME-ExamQuestion/manifest.json (read via
`git show` — the SME-* dirs are outside the sparse checkout):
  1. take manifest landing_url (.../topic-questions/)
  2. derive the course root URL (strip leaf-type segment)
  3. fetch the root page, read props.pageProps.courseExamSpecificationPdfLink
     (JSON parse of __NEXT_DATA__ with a raw-regex fallback)
  4. on null, retry the revision-notes URL variant once
  5. record course title + the raw link verbatim

Cache: /home/z/my-project/.cache/sme_spec/cie_course_specs.json (resumable,
--force refetches). Print-only script: writes NO repo files.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

REPO = Path("/home/z/my-project/syllabai-resources")
CACHE = Path("/home/z/my-project/.cache/sme_spec/cie_course_specs.json")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
FIELD = "courseExamSpecificationPdfLink"


def git_show(path: str) -> str:
    return subprocess.run(["git", "-C", str(REPO), "show", f"HEAD:{path}"],
                          capture_output=True, text=True, check=True).stdout


def fetch(url: str, tries: int = 3) -> bytes:
    last: Exception | None = None
    for i in range(tries):
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent": UA, "Accept": "text/html,*/*"})
            with urllib.request.urlopen(req, timeout=60) as resp:
                return resp.read()
        except Exception as exc:  # noqa: BLE001
            last = exc
            time.sleep(2 + 3 * i)
    raise RuntimeError(f"fetch failed after {tries} tries: {url}: {last!r}")


def next_data(html: str) -> dict:
    m = re.search(
        r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>',
        html, re.S)
    if not m:
        return {}
    try:
        return json.loads(m.group(1))
    except json.JSONDecodeError:
        return {}


def find_link(html: str) -> str | None:
    nd = next_data(html)
    props = (nd.get("props", {}).get("pageProps", {}) if nd else {})
    link = props.get(FIELD)
    if isinstance(link, str) and link:
        return link
    m = re.search(r'"' + FIELD + r'"\s*:\s*"([^"]+)"', html)
    if m and m.group(1):
        return m.group(1)
    m = re.search(r'"' + FIELD + r'"\s*:\s*null', html)
    if m:
        return None
    return None


def course_root(landing: str) -> str:
    return re.sub(r"(topic-questions|revision-notes|past-papers)/?$", "",
                  landing.rstrip("/")).rstrip("/") + "/"


def main() -> int:
    force = "--force" in sys.argv
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    cache: dict = {}
    if CACHE.exists() and not force:
        cache = json.loads(CACHE.read_text())

    courses = json.loads(git_show("SME-ExamQuestion/manifest.json"))["courses"]
    cie = [c for c in courses if c["slug"].startswith("cie-")]
    print(f"cie lanes in registry: {len(cie)}")

    results: dict = {}
    if cache:
        results = cache.get("lanes", {})
        print(f"cache: {len(results)} lanes already probed")

    for i, c in enumerate(cie):
        slug = c["slug"]
        if slug in results and not force:
            continue
        landing = c["landing_url"]
        root = course_root(landing)
        entry: dict = {"landing_url": landing, "course_root": root}
        try:
            link = find_link(fetch(root).decode("utf-8", "replace"))
            if link is None:
                alt = root.replace("topic-questions/", "revision-notes/")
                entry["alt_probe"] = alt
                link = find_link(fetch(alt).decode("utf-8", "replace"))
            entry["spec_link"] = link
        except Exception as exc:  # noqa: BLE001
            entry["error"] = repr(exc)[:200]
            entry["spec_link"] = None
        entry["probe_variant"] = entry.get("alt_probe", root) if link else entry.get("spec_link") or root
        results[slug] = entry
        CACHE.write_text(json.dumps({"lanes": results}, indent=1))
        got = (entry.get("spec_link") or "NULL")[:80]
        print(f"  [{i+1}/{len(cie)}] {slug} -> {got}")
        time.sleep(1.0)

    links = {}
    for slug, e in sorted(results.items()):
        (links.setdefault(e.get("spec_link") or "NULL", [])).append(slug)
    print("\n=== DEDUPE GROUPS (by PDF URL) ===")
    for url, slugs in sorted(links.items()):
        print(f"  {url}\n    -> {len(slugs)} lanes: {', '.join(slugs[:4])}{' ...' if len(slugs) > 4 else ''}")
    n_ok = sum(1 for e in results.values() if e.get("spec_link"))
    print(f"\nlanes with link: {n_ok}/{len(results)}; unique PDFs: {len([k for k in links if k != 'NULL'])}; null lanes: {len(links.get('NULL', []))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
