#!/usr/bin/env python3
"""Validation for the 4PH1 physics chunks (8-point standard core checks)."""
import json, re, collections, sys

F = "/home/z/my-project/download/rag_physics/edexcel_igcse_physics_chunks_v1.jsonl"
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
    # standard point 1: dual numbering on every chunk
    if c.get("book_pages") is None and c["pdf_pages"][0] >= 11:
        errs.append(f"missing book_pages on body-range chunk: {c['id']}")
    if not isinstance(c.get("pdf_pages"), list) or len(c["pdf_pages"]) != 2:
        errs.append(f"bad pdf_pages: {c['id']}")

# chapter coverage: 28 chapters
chap = {c["chapter_no"] for c in chunks if c.get("chapter_no")}
missing = [n for n in range(1, 29) if n not in chap]
if missing:
    errs.append(f"chapters missing: {missing}")

# unit coverage: 8 units
units_seen = {c["unit_no"] for c in chunks if c.get("unit_no")}
missing_u = [n for n in range(1, 9) if n not in units_seen]
if missing_u:
    errs.append(f"units missing: {missing_u}")

# page monotonicity: body-range chunks must never go backwards. Non-body
# back-matter types (index/glossary/appendix/front_matter/divider/skills) are
# exempt: table interruptions in multi-column index pages can reorder them.
NON_BODY = {"index", "glossary", "appendix", "front_matter", "divider", "skills"}
last_start = 0
order_breaks = 0
for c in chunks:
    s = c["pdf_pages"][0]
    if c["content_type"] not in NON_BODY:
        if s < last_start - 1:
            order_breaks += 1
        last_start = max(last_start, s)
if order_breaks:
    errs.append(f"page order breaks: {order_breaks}")

# quality proxies
latex = sum(1 for c in chunks if re.search(r"\\|\{|\}", c["text"]))
subs = sum(1 for c in chunks if re.search(r"[₀-₉]", c["text"]))
sups = sum(1 for c in chunks if re.search(r"[⁰¹²³⁴-⁹⁺⁻]", c["text"]))
sizes = sorted(c["char_count"] for c in chunks)
types = collections.Counter(c["content_type"] for c in chunks)
unit_counts = collections.Counter(c["unit_no"] for c in chunks if c["unit_no"])

# serving-critical: question types present and page-anchored
qchunks = [c for c in chunks if c["content_type"] in ("chapter_questions", "unit_questions")]
qpages = sorted({p for c in qchunks for p in c["pdf_pages"]})
print(f"question-typed chunks: {len(qchunks)} on pdf pages {qpages}")

print(f"chunks: {len(chunks)}  unique ids: {len(set(ids))}")
print(f"chapters covered: {len(chap)}/28   units covered: {len(units_seen)}/8   order breaks: {order_breaks}")
print(f"size min/median/max: {sizes[0]}/{sizes[len(sizes)//2]}/{sizes[-1]}  total: {sum(sizes)/1e6:.2f} MB chars")
print(f"subscript chunks: {subs}   superscript chunks: {sups}   latex remnants: {latex}")
print("per unit:", dict(sorted(unit_counts.items())))
print("types:", dict(types.most_common(20)))
print()
print("ERRORS:" if errs else "ALL CHECKS PASSED")
for e in errs[:20]:
    print(" -", e)
sys.exit(1 if errs else 0)
