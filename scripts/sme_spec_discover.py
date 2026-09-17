#!/usr/bin/env python3
"""Discover official exam-specification PDF links for all SME courses.

For each course directory under SME-ExamQuestion/:
  1. read manifest.json -> source.landing_url (a .../topic-questions/ URL)
  2. derive the course root URL (strip trailing 'topic-questions/' segment)
  3. fetch the root page, read props.pageProps.courseExamSpecificationPdfLink
  4. record course title + card title if present

Cache: .cache/sme_spec/course_specs.json  (resumable; --force refetches)
Output summary: courses with/without links, unique-PDF dedupe groups.
"""
from __future__ import annotations

import json
import re
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

REPO = Path("/home/z/my-project/download/syllabai-resources")
CACHE = Path("/home/z/my-project/.cache/sme_spec/course_specs.json")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

FIELD = "courseExamSpecificationPdfLink"


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
    return json.loads(m.group(1)) if m else {}


def course_root(landing: str) -> str:
    # landing_url points at a leaf type segment: .../<mid>/topic-questions/
    # or .../<mid>/pure-1/topic-questions/ or .../double-award/17/chemistry/topic-questions/
    return re.sub(r"(topic-questions|revision-notes|past-papers)/?$", "",
                  landing.rstrip("/")).rstrip("/") + "/"


def main() -> int:
    force = "--force" in sys.argv
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    done: dict = {}
    if CACHE.exists() and not force:
        done = json.loads(CACHE.read_text())

    course_dirs = sorted(p.name for p in (REPO / "SME-ExamQuestion").iterdir()
                         if p.is_dir())
    print(f"{len(course_dirs)} course dirs")

    for slug in course_dirs:
        if slug in done and not force:
            continue
        mpath = REPO / "SME-ExamQuestion" / slug / "manifest.json"
        manifest = json.loads(mpath.read_text())
        landing = manifest["source"]["landing_url"]
        root = course_root(landing)
        rec: dict = {"landing": landing, "root": root}
        try:
            html = fetch(root).decode("utf-8", errors="replace")
            pp = next_data(html).get("props", {}).get("pageProps", {})
            rec["spec_pdf"] = pp.get(FIELD)
            # nearby metadata for provenance
            rec["page_title"] = re.sub(r"\s+", " ", (re.search(
                r"<title>(.*?)</title>", html, re.S).group(1)
                if re.search(r"<title>(.*?)</title>", html, re.S) else ""))[:200]
            # learning-hub spec link (relatedLinks)
            m = re.search(r'href="(/learning-hub/exam-specifications/[^"]+)"',
                          html)
            rec["learning_hub"] = ("https://www.savemyexams.com" + m.group(1)
                                   ) if m else None
            rec["ok"] = True
            print(f"[ok] {slug}: {rec['spec_pdf']}")
        except Exception as exc:  # noqa: BLE001
            rec["ok"] = False
            rec["error"] = repr(exc)
            print(f"[ERR] {slug}: {exc!r}")
        done[slug] = rec
        CACHE.write_text(json.dumps(done, indent=1))
        time.sleep(0.8)

    # summary
    linked = {s: r["spec_pdf"] for s, r in done.items() if r.get("spec_pdf")}
    missing = [s for s, r in done.items() if not r.get("spec_pdf")]
    uniq = sorted(set(linked.values()))
    print(f"\ncourses with spec link : {len(linked)}/{len(done)}")
    print(f"courses WITHOUT link   : {len(missing)}")
    for s in missing:
        print(f"   - {s}")
    print(f"unique spec PDFs       : {len(uniq)}")
    by_pdf: dict[str, list[str]] = {}
    for s, u in linked.items():
        by_pdf.setdefault(u, []).append(s)
    for u in uniq:
        print(f"  [{len(by_pdf[u])} courses] {u}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
