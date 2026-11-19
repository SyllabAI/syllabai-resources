#!/usr/bin/env python3
"""validate_9702.py — 8-point gate for the CIE 9702 corpus v1."""
import json, re, sys, collections, os

CORPUS = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      "out/cie_a_level_physics_9702_chunks_v1.jsonl")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from book_structure_9702 import (chapter_ranges, CHAPTER_OPENERS, PDF_PAGES_TOTAL,
                                 OFFSET, FRONT_MATTER_END)

recs = [json.loads(l) for l in open(CORPUS, encoding="utf-8")]
fail = []
ok = lambda name: print(f"  PASS {name}")


def check(name, cond, detail=""):
    if cond:
        ok(name)
    else:
        fail.append(name)
        print(f"  FAIL {name} {detail}")


print(f"corpus: {len(recs)} chunks")

# 1. unique ids + grammar
ids = [r["id"] for r in recs]
check("unique ids", len(set(ids)) == len(ids))
gram = re.compile(r"^c9702_v1_u0_c(\d+)_pdf(\d{3})_(\d{4})$")
check("id grammar", all(gram.match(i) for i in ids))

# 2. schema keys exact (13-key v1 grammar)
KEYS = {"id", "book_title", "author", "unit_no", "unit_name", "chapter_no",
        "chapter_title", "section", "content_type", "book_pages", "pdf_pages",
        "text", "char_count"}
check("schema keys", all(set(r.keys()) == KEYS for r in recs))

# 3. chapter coverage
chaps = {r["chapter_no"] for r in recs if r["chapter_no"]}
check("32/32 chapters", chaps == set(range(1, 33)), f"got {sorted(chaps)[:40]}")
titles = {r["chapter_title"] for r in recs}
for t in ["P1 Practical skills at AS level", "P2 Planning, analysis and evaluation",
          "Glossary", "Index", "Answers to SAQs", "Answers to EOC questions",
          "Recommended resources"]:
    check(f"cover: {t[:30]}", any(t == x or x.startswith(t) for x in titles))
check("cover: Appendices", any(x.startswith("Appendix") for x in titles))
check("cover: Front matter", any(x.startswith("Front matter") for x in titles))

# 4. page-order integrity
prev = None
breaks = 0
for r in recs:
    cur = (r["pdf_pages"][0], r["pdf_pages"][1])
    if prev and cur[0] < prev[1]:
        if cur[0] < prev[0]:
            breaks += 1
    prev = cur
check("0 page-order breaks", breaks == 0, f"{breaks}")
check("page bounds", all(1 <= r["pdf_pages"][0] <= r["pdf_pages"][1] <= PDF_PAGES_TOTAL for r in recs))

# 5. chapter-range coherence
rng = {}
for s, e, m in chapter_ranges():
    rng[(m["chapter_no"], m["chapter_title"])] = (s, e)
bad = 0
for r in recs:
    key = (r["chapter_no"], r["chapter_title"])
    s, e = rng.get(key, (None, None))
    if s is None or not (s <= r["pdf_pages"][0] and r["pdf_pages"][1] <= e):
        bad += 1
check("chapter-range coherence", bad == 0, f"{bad} outliers")

# 6. dual page numbering + offset law
badbp = 0
for r in recs:
    p0, p1 = r["pdf_pages"]
    if p0 <= FRONT_MATTER_END:
        if r["book_pages"] is not None:
            badbp += 1
    else:
        if r["book_pages"] is None or r["book_pages"][0] != p0 - OFFSET \
                or r["book_pages"][1] != p1 - OFFSET:
            badbp += 1
check("dual page numbering (offset law)", badbp == 0, f"{badbp}")

# 7. serving-critical: EOC anchoring per chapter
cq = [r for r in recs if r["content_type"] == "chapter_questions"]
cq_chaps = {r["chapter_no"] for r in cq if r["chapter_no"]}
check("EOC sets anchored 32/32 chapters", cq_chaps == set(range(1, 33)),
      f"covered {len(cq_chaps)}/32: missing {sorted(set(range(1,33)) - cq_chaps)}")
check("EOC header text present", sum(1 for r in cq if "End-of-chapter questions" in r["text"][:60]) >= 30)

# 8. junk/watermark classes
cjk = lambda t: sum(1 for c in t if 0x2E80 <= ord(c) <= 0x9FFF)
check("0 CJK/watermark", all(cjk(r["text"]) == 0 and "CLASS0608" not in r["text"] for r in recs))
check("0 'images' junk", all(r["text"].strip() != "images" for r in recs))
check("0 replacement chars", all("\ufffd" not in r["text"] for r in recs))
check("0 running-header leakage",
      all(not r["text"].startswith("Cambridge International AS Level Physics")
          and not r["text"].startswith("Cambridge International A Level Physics")
          for r in recs))

# 9. sizes + char_count integrity
sizes = [r["char_count"] for r in recs]
check("char_count == len(text)", all(r["char_count"] == len(r["text"]) for r in recs))
check("size bounds", min(sizes) >= 1 and max(sizes) <= 2400,
      f"min={min(sizes)} max={max(sizes)}")
tiny = sum(1 for s in sizes if s < 30)
print(f"  INFO tiny (<30 char) chunks: {tiny} (figure-label debris class, honest)")

# unicode formula sanity (informational)
sub = sum(1 for r in recs if "₀" in r["text"] or "₂" in r["text"] or "₃" in r["text"])
sup = sum(1 for r in recs if "⁻" in r["text"] or "²" in r["text"] or "³" in r["text"])
print(f"  INFO chunks with Unicode subscripts: {sub}, superscripts: {sup}")

types = collections.Counter(r["content_type"] for r in recs)
print(f"  INFO content types: {dict(types.most_common())}")

print()
if fail:
    print(f"VALIDATION FAILED: {len(fail)} checks: {fail}")
    sys.exit(1)
print("ALL CHECKS PASSED")
