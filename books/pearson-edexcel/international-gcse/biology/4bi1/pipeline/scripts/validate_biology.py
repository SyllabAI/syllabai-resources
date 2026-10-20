#!/usr/bin/env python3
"""Validation gate for the 4BI1 biology chunks (8-point standard core checks).

Adapted from validate_physics.py with biology-specific additions:
- 2-up law coherence: book_pages must lie within [2*spread-10, 2*spread-9]
  for the chunk's pdf_pages (spread mapping is this book's dual-numbering law)
- serving-critical question anchoring: every probed chapter-question spread
  and unit-question spread must be covered by chunks of the right type
- answers section: book 329-348 must be covered by answers chunks
- char_count recomputation (== len(text))
"""
import json, re, sys, collections

sys.path.insert(0, "/home/z/my-project/syllabai-resources/books/pearson-edexcel/"
                   "international-gcse/biology/4bi1/pipeline/scripts")
from book_structure_biology import (
    CHAPTERS, QUESTION_RANGES, EXTRA_SECTIONS, N_SPREADS,
    book_page_of, spread_side_of,
)

F = "/home/z/my-project/download/rag_biology/edexcel_igcse_biology_chunks_v1.jsonl"
chunks = [json.loads(l) for l in open(F)]
errs = []

# --- unique ids -----------------------------------------------------------
ids = [c["id"] for c in chunks]
if len(set(ids)) != len(ids):
    errs.append(f"duplicate ids: {len(ids) - len(set(ids))}")

# --- 15-key grammar -------------------------------------------------------
KEYS = {"id", "book_title", "author", "unit_no", "unit_name", "chapter_no",
        "chapter_title", "section", "content_type", "book_pages", "pdf_pages",
        "char_count", "text"}
POLISH_KEYS = {"text_original", "llm_repaired"}   # 15-key grammar additions
for c in chunks:
    missing = KEYS - set(c)
    extra = set(c) - KEYS
    if missing:
        errs.append(f"missing keys {missing}: {c['id']}")
    if extra - POLISH_KEYS:
        errs.append(f"extra keys {extra - POLISH_KEYS}: {c['id']}")
    if ("text_original" in c) != ("llm_repaired" in c):
        errs.append(f"polish keys must co-occur: {c['id']}")
    if not c.get("text") or not c["text"].strip():
        errs.append(f"empty text: {c['id']}")
    if c.get("char_count") != len(c["text"]):
        errs.append(f"char_count mismatch ({c.get('char_count')} != {len(c['text'])}): {c['id']}")
    if not isinstance(c.get("pdf_pages"), list) or len(c["pdf_pages"]) != 2 \
            or c["pdf_pages"][0] > c["pdf_pages"][1]:
        errs.append(f"bad pdf_pages: {c['id']}")
    # 2-up law: book page must lie inside the covered spreads' book range
    if c.get("book_pages") is not None:
        lo = 2 * c["pdf_pages"][0] - 10
        hi = 2 * c["pdf_pages"][1] - 9
        if not (lo <= c["book_pages"][0] <= c["book_pages"][1] <= hi):
            errs.append(f"book_pages {c['book_pages']} outside spread range "
                        f"{c['pdf_pages']} ({lo}..{hi}): {c['id']}")
        if c["book_pages"][0] > c["book_pages"][1]:
            errs.append(f"book_pages inverted: {c['id']}")
    elif c["pdf_pages"][0] >= 6:
        # front matter pdf 1-5 may be null; body-range chunks may not
        errs.append(f"missing book_pages on body-range chunk: {c['id']}")
    if c["pdf_pages"][0] < 1 or c["pdf_pages"][1] > N_SPREADS:
        errs.append(f"pdf_pages out of range: {c['id']}")

# --- chapter / unit coverage ----------------------------------------------
chap = {c["chapter_no"] for c in chunks if c.get("chapter_no")}
missing = [n for n in range(1, 23) if n not in chap]
if missing:
    errs.append(f"chapters missing: {missing}")
units_seen = {c["unit_no"] for c in chunks if c.get("unit_no")}
missing_u = [n for n in range(1, 7) if n not in units_seen]
if missing_u:
    errs.append(f"units missing: {missing_u}")

# --- page monotonicity for body chunks -------------------------------------
NON_BODY = {"index", "glossary", "appendix", "front_matter", "divider",
            "skills", "back_cover", "answers", "unit_questions",
            "chapter_questions"}
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

# --- serving-critical: question anchoring ----------------------------------
def spreads_of(chunks_of_type, cno=None):
    sp = set()
    for c in chunks_of_type:
        if cno is None or c.get("chapter_no") == cno:
            sp.update(range(c["pdf_pages"][0], c["pdf_pages"][1] + 1))
    return sp

for cno, bp0, bp1 in QUESTION_RANGES:
    want = {spread_side_of(bp)[0] for bp in range(bp0, bp1 + 1)}
    got = spreads_of([c for c in chunks if c["content_type"] == "chapter_questions"], cno)
    uncovered = want - got
    if uncovered:
        errs.append(f"ch{cno} question spreads uncovered: {sorted(uncovered)}")

unit_q_chunks = [c for c in chunks if c["content_type"] == "unit_questions"]
for key, bp0, bp1, _u, _l, _t in [e for e in EXTRA_SECTIONS if e[5] == "unit_questions"]:
    want = {spread_side_of(bp)[0] for bp in range(bp0, bp1 + 1)}
    got = spreads_of(unit_q_chunks)
    uncovered = want - got
    if uncovered:
        errs.append(f"unit questions ({key}) spreads uncovered: {sorted(uncovered)}")

# --- answers section coverage ----------------------------------------------
ans = spreads_of([c for c in chunks if c["content_type"] == "answers"])
for bp in (329, 331, 340, 348):
    sp, _side = spread_side_of(bp)
    if sp not in ans:
        errs.append(f"answers section: spread {sp} (book {bp}) uncovered")

# --- question-typed chunks must sit inside their probed ranges -------------
qr_by_ch = {}
for cno, bp0, bp1 in QUESTION_RANGES:
    qr_by_ch[cno] = (bp0, bp1)
for c in chunks:
    if c["content_type"] == "chapter_questions":
        bp0, bp1 = qr_by_ch.get(c.get("chapter_no"), (None, None))
        if bp0 is None:
            errs.append(f"chapter_questions chunk for unknown chapter: {c['id']}")
            continue
        lo, hi = spread_side_of(bp0)[0], spread_side_of(bp1)[0]
        if not (lo <= c["pdf_pages"][0] and c["pdf_pages"][1] <= hi):
            errs.append(f"chapter_questions chunk outside probed range "
                        f"{c['pdf_pages']} vs {lo}..{hi}: {c['id']}")

# --- quality proxies --------------------------------------------------------
latex = sum(1 for c in chunks if re.search(r"\\|\{|\}", c["text"]))
subs = sum(1 for c in chunks if re.search(r"[₀-₉]", c["text"]))
sups = sum(1 for c in chunks if re.search(r"[⁰¹²³⁴-⁹⁺⁻]", c["text"]))
sizes = sorted(c["char_count"] for c in chunks)
types = collections.Counter(c["content_type"] for c in chunks)
unit_counts = collections.Counter(c["unit_no"] for c in chunks if c["unit_no"])
over = [c["id"] for c in chunks if c["char_count"] > 2400]
if over:
    errs.append(f"chunks over HARD_MAX 2400: {len(over)} e.g. {over[:3]}")
tiny = [c["id"] for c in chunks if c["char_count"] < 20]
if tiny:
    errs.append(f"chunks under 20 chars: {len(tiny)} e.g. {tiny[:3]}")

qchunks = [c for c in chunks if c["content_type"] in ("chapter_questions", "unit_questions")]
qpages = sorted({p for c in qchunks for p in c["pdf_pages"]})
print(f"question-typed chunks: {len(qchunks)} across {len(qpages)} spreads")

print(f"chunks: {len(chunks)}  unique ids: {len(set(ids))}")
print(f"chapters covered: {len(chap)}/22   units covered: {len(units_seen)}/6   "
      f"order breaks: {order_breaks}")
print(f"size min/median/max: {sizes[0]}/{sizes[len(sizes)//2]}/{sizes[-1]}  "
      f"total: {sum(sizes)/1e6:.2f} MB chars")
print(f"subscript chunks: {subs}   superscript chunks: {sups}   latex remnants: {latex} "
      f"(0 expected on this text-layer lane)")
print("per unit:", dict(sorted(unit_counts.items())))
print("types:", dict(types.most_common(20)))
print()
print("ERRORS:" if errs else "ALL CHECKS PASSED")
for e in errs[:25]:
    print(" -", e)
sys.exit(1 if errs else 0)
