#!/usr/bin/env python3
"""Scan OCR'd pages for structural heading patterns. Prints only counts + matched
structural lines (titles), never body text, for regex tuning."""
import os, re, json
from collections import Counter

OCR_DIR = "/home/z/my-project/data/ocr_pages"

pat_unit = re.compile(r"^\s*UNIT\s+(\d{1,2})\b[:. ]*(.{0,60})$", re.I)
pat_sec = re.compile(r"^\s*(\d{1,2})\.(\d{1,2})\s+([A-Za-z][^.]{2,70})$")
pat_chap = re.compile(r"^\s*(\d{1,2})\s+([A-Z][A-Za-z' ()/-]{3,60})$")
pat_marker = re.compile(
    r"^\s*(TEST YOURSELF|EXAM[- ]STYLE QUESTION[S]?|PRACTICAL|DID YOU KNOW|"
    r"ACTIVITY|KEY POINT[S]?|SUMMARY QUESTION[S]?|END OF UNIT QUESTION[S]?|"
    r"OBJECTIVES|LEARNING OBJECTIVES|CHAPTER [A-Z]+|MATHS SKILLS|"
    r"PROGRESS CHECK|EXAM TECHNIQUE|EXAM HINT)\b.{0,40}$"
)

units, sections, chapters, markers = [], [], [], []
marker_count = Counter()
empty_pages, low_pages = [], []
char_counts = {}

for fn in sorted(os.listdir(OCR_DIR)):
    if not fn.endswith(".txt"):
        continue
    pno = int(fn[5:8])
    with open(os.path.join(OCR_DIR, fn), encoding="utf-8") as f:
        txt = f.read()
    char_counts[pno] = len(txt)
    if len(txt) < 40:
        empty_pages.append(pno)
        continue
    if len(txt) < 400:
        low_pages.append(pno)
    lines = txt.splitlines()
    for ln in lines:
        m = pat_unit.match(ln)
        if m:
            units.append({"p": pno, "unit": int(m.group(1)), "title": m.group(2).strip()[:60]})
            continue
        m = pat_sec.match(ln)
        if m:
            sections.append({"p": pno, "num": f"{m.group(1)}.{m.group(2)}", "title": m.group(3).strip()[:60]})
            continue
        m = pat_marker.match(ln)
        if m:
            key = m.group(1).upper()[:30]
            markers.append({"p": pno, "marker": key, "line": ln.strip()[:50]})
            marker_count[key] += 1
            continue
        m = pat_chap.match(ln)
        if m and pno < 30:  # chapter lines only checked early to reduce noise
            chapters.append({"p": pno, "num": m.group(1), "title": m.group(2).strip()[:60]})

print("== UNITS found ==")
for u in units:
    print(u)
print("\n== SECTION headings (first 50 of", len(sections), ") ==")
for s in sections[:50]:
    print(s)
print("\n== MARKER counts ==")
print(json.dumps(marker_count, indent=1))
print("\n== MARKER first-seen sample ==")
seen = set()
for m in markers:
    if m["marker"] not in seen:
        seen.add(m["marker"])
        print(m)
print("\nempty pages (<40 chars):", empty_pages)
print("low pages (<400 chars):", low_pages)
print("\nchar stats: min", min(char_counts.values()), "max", max(char_counts.values()),
      "avg", sum(char_counts.values()) // len(char_counts))
