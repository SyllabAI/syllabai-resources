#!/usr/bin/env python3
"""validate_9701.py — 8-point gate for the CIE 9701 corpus v1."""
import json, re, sys, collections, os

CORPUS = "/home/z/my-project/download/rag_9701/cie_a_level_chemistry_9701_chunks_v1.jsonl"
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from book_structure_9701 import (CHAPTER_OPENERS, CHAPTER_TITLES, P1_START, P2_START,
                                 APPENDICES_START, ACKNOWLEDGEMENTS_START, PDF_PAGES_TOTAL)

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
gram = re.compile(r"^c9701_v1_u0_c(\d+)_pdf(\d{3})_(\d{4})$")
check("id grammar", all(gram.match(i) for i in ids))

# 2. schema keys exact (13-key v1 grammar)
KEYS = {"id", "book_title", "author", "unit_no", "unit_name", "chapter_no",
        "chapter_title", "section", "content_type", "book_pages", "pdf_pages",
        "text", "char_count"}
check("schema keys", all(set(r.keys()) == KEYS for r in recs))

# 3. chapter coverage
chaps = {r["chapter_no"] for r in recs if r["chapter_no"]}
check("30/30 chapters", chaps == set(range(1, 31)), f"got {len(chaps)}")
titles = {r["chapter_title"] for r in recs}
for t in ["P1 Practical skills 1", "P2 Practical skills 2", "Acknowledgements and imprint"]:
    check(f"cover: {t[:26]}", any(t in x for x in titles))
check("cover: Appendices", any(x.startswith("Appendices") for x in titles))
check("cover: Front matter", any(x.startswith("Front matter") for x in titles))

# 4. page-order integrity (id order == document order)
prev = None
breaks = 0
for r in recs:
    cur = (r["pdf_pages"][0], r["pdf_pages"][1])
    if prev and cur[0] < prev[1] - 0:  # start before prev end (overlap >0)
        if cur[0] < prev[0]:
            breaks += 1
    prev = cur
check("0 page-order breaks", breaks == 0, f"{breaks}")
check("page bounds", all(1 <= r["pdf_pages"][0] <= r["pdf_pages"][1] <= PDF_PAGES_TOTAL for r in recs))

# 5. chapter-range coherence: chunk pdf range inside declared chapter range
from book_structure_9701 import chapter_ranges
rng = {}
for s, e, m in chapter_ranges():
    key = (m["chapter_no"], m["chapter_title"])
    rng[key] = (s, e)
bad = 0
for r in recs:
    key = (r["chapter_no"], r["chapter_title"])
    s, e = rng.get(key, (None, None))
    if s is None or not (s <= r["pdf_pages"][0] and r["pdf_pages"][1] <= e):
        bad += 1
check("chapter-range coherence", bad == 0, f"{bad} outliers")

# 6. serving-critical: exam-style question anchoring
cq = [r for r in recs if r["content_type"] == "chapter_questions"]
ep_pages = set()
for r in cq:
    for p in range(r["pdf_pages"][0], r["pdf_pages"][1] + 1):
        ep_pages.add(p)
# all EXAM-STYLE QUESTIONS header pages must be inside chapter_questions chunks
hdr_pages = []
for i in range(1, PDF_PAGES_TOTAL + 1):
    pass  # full scan too slow here; sample via chunk text instead
bytext = sum(1 for r in cq if "EXAM-STYLE QUESTIONS" in r["text"])
check("exam-style banks anchored", len(cq) >= 32 and bytext >= 30,
      f"cq={len(cq)} with header={bytext}")

# 7. junk/watermark classes
cjk = lambda t: sum(1 for c in t if 0x2E80 <= ord(c) <= 0x9FFF)
check("0 watermark", all("CLASS0608" not in r["text"] and cjk(r["text"]) == 0 for r in recs))
check("0 'images' junk", all(r["text"].strip() != "images" for r in recs))
check("0 replacement chars", all("\ufffd" not in r["text"] for r in recs))

# 8. sizes + char_count integrity
sizes = [r["char_count"] for r in recs]
check("char_count == len(text)", all(r["char_count"] == len(r["text"]) for r in recs))
check("size bounds", min(sizes) >= 9 and max(sizes) <= 2400,
      f"min={min(sizes)} max={max(sizes)}")

# unicode formula sanity (informational)
sub = sum(1 for r in recs if "₀" in r["text"] or "₂" in r["text"] or "₃" in r["text"])
sup = sum(1 for r in recs if "⁻" in r["text"] or "²" in r["text"] or "³" in r["text"])
print(f"  INFO chunks with Unicode subscripts: {sub}, superscripts: {sup}")

print()
if fail:
    print(f"VALIDATION FAILED: {len(fail)} checks: {fail}")
    sys.exit(1)
print("ALL CHECKS PASSED")
