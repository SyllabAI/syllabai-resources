#!/usr/bin/env python3
"""Validation for YPH11 SB2 chunks (8-point standard core checks, IAL lane).

Extra checks vs the 4PH1 reference:
- strict offset law: book_pages == pdf_pages - 11 on every numbered chunk
- question anchoring: all 13 chapter EXAM PRACTICE ranges (PDF) covered by
  chapter_questions-typed chunks exactly on their pages
- front matter (PDF 1-11) must have book_pages null;
  arabic chunks (PDF >= 12) must have book_pages (no printed page 1 in book)
"""
import json, re, collections, sys

F = "/home/z/my-project/download/rag_yph11/edexcel_ial_physics_yph11_sb2_chunks_v1.jsonl"
chunks = [json.loads(l) for l in open(F)]
errs = []

BASE_KEYS = {"id", "book_title", "author", "unit_no", "unit_name", "chapter_no",
             "chapter_title", "section", "content_type", "book_pages", "pdf_pages",
             "char_count", "text"}
ALLOWED = BASE_KEYS | {"text_original", "llm_repaired"}

ids = [c["id"] for c in chunks]
if len(set(ids)) != len(ids):
    errs.append(f"duplicate ids: {len(ids) - len(set(ids))}")
if not all(i.startswith("yph2_v1_") for i in ids):
    errs.append("id prefix violation (expected yph2_v1_)")

for c in chunks:
    if not c.get("text") or not c["text"].strip():
        errs.append(f"empty text: {c['id']}")
    if not set(c.keys()) <= ALLOWED:
        errs.append(f"schema key violation: {c['id']} extra={set(c.keys()) - ALLOWED}")
    for k in ("unit_no", "chapter_no", "content_type", "pdf_pages", "book_pages", "section"):
        if k not in c:
            errs.append(f"missing field {k}: {c['id']}")
    if not isinstance(c.get("pdf_pages"), list) or len(c["pdf_pages"]) != 2:
        errs.append(f"bad pdf_pages: {c['id']}")
        continue
    # dual numbering + strict offset law
    p0, p1 = c["pdf_pages"]
    if c.get("book_pages") is None:
        if p0 >= 12:
            errs.append(f"missing book_pages on body-range chunk: {c['id']}")
    else:
        if c["book_pages"] != [p0 - 10, p1 - 10]:
            errs.append(f"offset law violated: {c['id']} book={c['book_pages']} pdf={c['pdf_pages']}")

# chapter coverage: 13 chapters (5A..11B)
chap = {c["chapter_no"] for c in chunks if c.get("chapter_no")}
missing = [n for n in range(1, 14) if n not in chap]
if missing:
    errs.append(f"chapters missing: {missing}")

# unit coverage: 4 topics
units_seen = {c["unit_no"] for c in chunks if c.get("unit_no")}
missing_u = [n for n in range(5, 12) if n not in units_seen]
if missing_u:
    errs.append(f"units missing: {missing_u}")

# page monotonicity (body-range chunks never go backwards; back matter exempt:
# multi-column index/commentary pages can reorder internally)
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

# serving-critical: all 11 exam-practice ranges page-anchored to chapter_questions
EXPECTED_Q = {1: (22, 23), 2: (34, 35), 3: (50, 51), 4: (64, 65), 5: (80, 81),
              6: (92, 93), 7: (108, 109), 8: (124, 125), 9: (140, 141),
              10: (158, 159), 11: (176, 177), 12: (186, 187), 13: (212, 213)}
qchunks = [c for c in chunks if c["content_type"] == "chapter_questions"]
qpages = {p for c in qchunks for p in c["pdf_pages"]}
for cno, (a, b) in sorted(EXPECTED_Q.items()):
    missing_p = [p for p in (a, b) if p not in qpages]
    if missing_p:
        errs.append(f"chapter {cno} exam-practice pages not question-typed: {missing_p}")
# no question-typed chunks OUTSIDE the expected ranges
stray = sorted(p for p in qpages if not any(a <= p <= b for a, b in EXPECTED_Q.values()))
if stray:
    errs.append(f"question-typed chunks on unexpected pages: {stray}")

# quality proxies
latex = sum(1 for c in chunks if re.search(r"\\|\{|\}", c["text"]))
sups = sum(1 for c in chunks if re.search(r"[⁰¹²³⁴-⁹⁺⁻]", c["text"]))
sizes = sorted(c["char_count"] for c in chunks)
types = collections.Counter(c["content_type"] for c in chunks)
unit_counts = collections.Counter(c["unit_no"] for c in chunks if c["unit_no"])
print(f"chunks: {len(chunks)}  unique ids: {len(set(ids))}")
print(f"chapters covered: {len(chap)}/13   units covered: {len(units_seen)}/7   order breaks: {order_breaks}")
print(f"question-typed chunks: {len(qchunks)} on {len(qpages)} pdf pages (expected 26)")
print(f"size min/median/max: {sizes[0]}/{sizes[len(sizes)//2]}/{sizes[-1]}  total: {sum(sizes)/1e6:.2f} MB chars")
print(f"superscript chunks: {sups}   latex remnants: {latex}")
print("per unit:", dict(sorted(unit_counts.items(), key=lambda kv: (kv[0] is None, kv[0]))))
print("types:", dict(types.most_common(22)))
print()
print("ERRORS:" if errs else "ALL CHECKS PASSED")
for e in errs[:25]:
    print(" -", e)
sys.exit(1 if errs else 0)
