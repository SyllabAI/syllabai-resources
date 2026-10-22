#!/usr/bin/env python3
"""Phase 6 validation gate for the YPH11 SB1 corpus v1 (books/README.md §5).
Exit non-zero unless ALL CHECKS PASSED. Checks:
  1. unique chunk IDs, yph1_v1_ grammar
  2. 15-key grammar (13 base + optional text_original/llm_repaired)
  3. topic coverage 4/4, chapter coverage 11/11 (+ WaaP + back matter present)
  4. dual page numbering per chunk; front matter book_pages null
  5. offset law: book_page = pdf_page - 11 on every chunk
  6. chapter_questions chunks anchored inside the 11 probed EXAM PRACTICE ranges
  7. body reading order: pdf_pages non-decreasing within each (unit, chapter)
  8. char_count consistency (recomputed from text)
  9. size bounds 20..2400; 0 LaTeX remnants
 10. content types from the documented vocabulary
"""
import json, re, sys

sys.path.insert(0, "/home/z/my-project/scripts")
from book_structure_yph11 import CHAPTERS, EXTRA_SECTIONS, TOPIC_NAMES, N_PAGES, OFFSET

CORPUS = "/home/z/my-project/download/rag_yph11/edexcel_ial_physics_yph11_sb1_chunks_v1.jsonl"

BASE_KEYS = ["id", "book_title", "author", "unit_no", "unit_name", "chapter_no",
             "chapter_title", "section", "content_type", "book_pages", "pdf_pages",
             "char_count", "text"]
KNOWN_TYPES = {"body", "front_matter", "skills", "divider", "chapter_questions",
               "unit_questions", "learning_objectives", "worked_example", "exam_hint",
               "key_point", "activity", "practical", "extension_work", "did_you_know",
               "thinking_bigger", "checkpoint", "subject_vocabulary", "glossary",
               "appendix", "index", "table_data", "safety", "reminder"}
EP_RANGES = [(s, e) for k, s, e, u, lab, ct in EXTRA_SECTIONS if ct == "chapter_questions"]

errors = []
warnings = []
chunks = [json.loads(l) for l in open(CORPUS)]
print(f"loaded {len(chunks)} chunks")

# 1. unique IDs + grammar
ids = [c["id"] for c in chunks]
if len(set(ids)) != len(ids):
    errors.append("duplicate chunk ids")
for cid in ids:
    if not re.fullmatch(r"yph1_v1_u\d+_c\d+_pdf\d{3}_\d{4}", cid):
        errors.append(f"bad id grammar: {cid}")

# 2. 15-key grammar
for c in chunks:
    missing = [k for k in BASE_KEYS if k not in c]
    extra = [k for k in c if k not in BASE_KEYS + ["text_original", "llm_repaired"]]
    if missing:
        errors.append(f"{c['id']}: missing keys {missing}")
    if extra:
        errors.append(f"{c['id']}: unexpected keys {extra}")

# 3. coverage
by_chapter = {}
for c in chunks:
    if c["chapter_no"]:
        by_chapter.setdefault(c["chapter_no"], set()).add(c["unit_no"])
for cno, unit, title, bpage in CHAPTERS:
    got = by_chapter.get(cno)
    if not got:
        errors.append(f"chapter {cno} ({title}) has no chunks")
    elif got != {unit}:
        errors.append(f"chapter {cno} unit mismatch: {got} != {unit}")
units_seen = {c["unit_no"] for c in chunks if c["unit_no"]}
if units_seen != {1, 2, 3, 4}:
    errors.append(f"topic coverage {units_seen} != 1-4")
if not any(c["content_type"] == "skills" and c["chapter_no"] is None and (c["book_pages"] or [99])[0] <= 7 for c in chunks):
    errors.append("Working as a Physicist section (book 2-7) missing")
for need in ("glossary", "appendix"):
    if not any(c["content_type"] == need for c in chunks):
        errors.append(f"back matter {need} missing")
# index pages 222-224 must be covered (type may be table_data — 4PH1 precedent)
if not any(c["pdf_pages"][0] >= 222 for c in chunks):
    errors.append("index pages (pdf 222-224) not covered by any chunk")

# 4/5. dual numbering + offset law
for c in chunks:
    bp, pp = c["book_pages"], c["pdf_pages"]
    if not (isinstance(pp, list) and len(pp) == 2 and 1 <= pp[0] <= pp[1] <= N_PAGES):
        errors.append(f"{c['id']}: bad pdf_pages {pp}")
        continue
    if pp[0] < OFFSET + 2:  # front matter roman region
        if bp is not None:
            errors.append(f"{c['id']}: front matter must have book_pages null, got {bp}")
    else:
        if not (isinstance(bp, list) and len(bp) == 2):
            errors.append(f"{c['id']}: missing book_pages")
            continue
        if bp[0] != pp[0] - OFFSET or bp[1] != pp[1] - OFFSET:
            errors.append(f"{c['id']}: offset law broken bp={bp} pp={pp}")

# 6. question anchoring
n_q = 0
for c in chunks:
    if c["content_type"] == "chapter_questions":
        n_q += 1
        s, e = c["pdf_pages"]
        if not any(s >= a and e <= b for a, b in EP_RANGES):
            errors.append(f"{c['id']}: chapter_questions outside EXAM PRACTICE ranges pp={s}-{e}")
if n_q < 11:
    errors.append(f"only {n_q} chapter_questions chunks (expect >= 11 EP banks)")
ep_touched = set()
for c in chunks:
    if c["content_type"] == "chapter_questions":
        for i, (a, b) in enumerate(EP_RANGES):
            if c["pdf_pages"][0] >= a and c["pdf_pages"][1] <= b:
                ep_touched.add(i)
if len(ep_touched) != 11:
    errors.append(f"EP banks covered: {len(ep_touched)}/11")

# 7. body order within chapter
per_ch = {}
for c in chunks:
    if c["content_type"] in ("body", "learning_objectives", "worked_example", "exam_hint",
                             "checkpoint", "subject_vocabulary", "key_point", "practical",
                             "did_you_know", "thinking_bigger", "table_data"):
        per_ch.setdefault((c["unit_no"], c["chapter_no"]), []).append(c)
for key, cs in per_ch.items():
    seq = [c["pdf_pages"][0] for c in cs]
    breaks = [(i, seq[i - 1], seq[i]) for i in range(1, len(seq)) if seq[i] < seq[i - 1] - 1]
    if breaks:
        # index-style multi-column reflow would be a benign exception, but body
        # chapters must be clean — report as error (playbook: fix data, not check)
        errors.append(f"order breaks in {key}: {breaks[:3]}")

# 8. char_count
for c in chunks:
    if c["char_count"] != len(c["text"]):
        errors.append(f"{c['id']}: char_count {c['char_count']} != len(text) {len(c['text'])}")

# 9. size bounds + latex remnants
for c in chunks:
    if len(c["text"]) < 20:
        errors.append(f"{c['id']}: chunk too small ({len(c['text'])})")
    if len(c["text"]) > 2400:
        errors.append(f"{c['id']}: chunk over hard max ({len(c['text'])})")
    if re.search(r"\\[a-zA-Z]+|\{\\\w", c["text"]):
        errors.append(f"{c['id']}: LaTeX remnant")

# 10. types
for c in chunks:
    if c["content_type"] not in KNOWN_TYPES:
        errors.append(f"{c['id']}: unknown content_type {c['content_type']}")

print(f"chapter_questions chunks: {n_q}; EP banks covered: {len(ep_touched)}/11")
if errors:
    print(f"\nFAIL: {len(errors)} errors")
    for e in errors[:40]:
        print("  -", e)
    sys.exit(1)
print("\nALL CHECKS PASSED")
