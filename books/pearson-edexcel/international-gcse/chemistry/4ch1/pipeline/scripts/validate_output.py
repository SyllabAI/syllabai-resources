#!/usr/bin/env python3
"""Validate the JSONL deliverable: schema, coverage, sizes, OCR word-ratio quality."""
import json, re, sys
from collections import Counter

PATH = "/home/z/my-project/download/rag_chemistry/edexcel_igcse_chemistry_chunks.jsonl"

REQUIRED = ["book_title", "unit_name", "content_type", "pdf_page_start",
            "pdf_page_end", "page_start", "page_end", "source_url", "char_count"]
errors, ids = [], set()
sizes, ctypes, units, chapters = [], Counter(), Counter(), set()
word_ratios = []
prev_page = 0
page_order_breaks = 0

for i, line in enumerate(open(PATH, encoding="utf-8"), 1):
    try:
        c = json.loads(line)
    except Exception as e:
        errors.append(f"line {i}: JSON error {e}")
        continue
    if set(c.keys()) < {"id", "text", "metadata"}:
        errors.append(f"line {i}: missing top-level keys")
    if c["id"] in ids:
        errors.append(f"line {i}: duplicate id {c['id']}")
    ids.add(c["id"])
    md = c["metadata"]
    for k in REQUIRED:
        if k not in md:
            errors.append(f"line {i}: metadata missing {k}")
    if not c["text"] or len(c["text"]) < 40:
        errors.append(f"line {i}: text too short ({len(c.get('text',''))})")
    sizes.append(len(c["text"]))
    ctypes[md["content_type"]] += 1
    units[md["unit_name"]] += 1
    if md["chapter_no"]:
        chapters.add(md["chapter_no"])
    if md["pdf_page_start"] < prev_page - 2:   # allow small non-monotonicity
        page_order_breaks += 1
    prev_page = max(prev_page, md["pdf_page_end"])
    toks = re.findall(r"[A-Za-z][A-Za-z'-]*", c["text"])
    if toks:
        good = sum(1 for t in toks if len(t) >= 2)
        word_ratios.append(good / len(toks))

print(f"chunks: {len(sizes)}  unique ids: {len(ids)}")
print(f"chapters covered: {len(chapters)}/29  -> {sorted(chapters)}")
print(f"avg word-ratio: {sum(word_ratios)/len(word_ratios):.3f} (OCR quality proxy)")
print(f"page-order breaks: {page_order_breaks}")
print(f"size: min={min(sizes)} max={max(sizes)} avg={sum(sizes)//len(sizes)}")
print(f"content types: {dict(ctypes)}")
print(f"units: {dict(units)}")
print(f"ERRORS: {len(errors)}")
for e in errors[:10]:
    print("  ", e)
sys.exit(1 if errors or len(chapters) < 29 else 0)
