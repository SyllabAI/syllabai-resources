#!/usr/bin/env python3
"""Validation for v3 Docling-based chunks."""
import json, re, collections, sys

F = "/home/z/my-project/download/rag_chemistry/edexcel_igcse_chemistry_chunks_v3.jsonl"
chunks = [json.loads(l) for l in open(F)]
errs = []

ids = [c["id"] for c in chunks]
if len(set(ids)) != len(ids):
    errs.append(f"duplicate ids: {len(ids) - len(set(ids))}")

for c in chunks:
    if not c.get("text") or not c["text"].strip():
        errs.append(f"empty text: {c['id']}")
    for k in ("unit_no", "chapter_no", "content_type", "pdf_pages", "book_pages", "section"):
        if k not in c:
            errs.append(f"missing field {k}: {c['id']}")

# chapter coverage
chap = {c["chapter_no"] for c in chunks if c.get("chapter_no")}
missing = [n for n in range(1, 30) if n not in chap]
if missing:
    errs.append(f"chapters missing: {missing}")

# page monotonicity (by pdf start page, stable within chapter)
last_start = 0
order_breaks = 0
for c in chunks:
    s = c["pdf_pages"][0]
    if s < last_start - 1:
        order_breaks += 1
    last_start = max(last_start, s)
if order_breaks:
    errs.append(f"page order breaks: {order_breaks}")

# quality proxies
latex = sum(1 for c in chunks if re.search(r"\\|\{|\}", c["text"]))
notdecoded = sum(1 for c in chunks if "formula-not-decoded" in c["text"])
subs = sum(1 for c in chunks if re.search(r"[₀-₉]", c["text"]))
arrows = sum(1 for c in chunks if "→" in c["text"] or "⇌" in c["text"])

sizes = sorted(c["char_count"] for c in chunks)
types = collections.Counter(c["content_type"] for c in chunks)
units = collections.Counter(c["unit_no"] for c in chunks if c["unit_no"])

print(f"chunks: {len(chunks)}  unique ids: {len(set(ids))}")
print(f"chapters covered: {len(chap)}/29   order breaks: {order_breaks}")
print(f"size min/median/max: {sizes[0]}/{sizes[len(sizes)//2]}/{sizes[-1]}  total: {sum(sizes)/1e6:.2f} MB chars")
print(f"subscript chunks: {subs}   arrow chunks: {arrows}   latex remnants: {latex}   not-decoded: {notdecoded}")
print("per unit:", dict(units))
print("top types:", dict(types.most_common(10)))
print()
print("ERRORS:" if errs else "ALL CHECKS PASSED")
for e in errs[:20]:
    print(" -", e)
sys.exit(1 if errs else 0)
