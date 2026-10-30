#!/usr/bin/env python3
"""Phase 6 validation gate for the YCH12 SB2 corpus v1 (books/README.md §5).
Exit non-zero unless ALL CHECKS PASSED. Checks:
  1. unique chunk IDs, ych1_v1_ grammar
  2. 15-key grammar (13 base + optional text_original/llm_repaired)
  3. topic coverage 10/10, chapter coverage 35/35 (+ back matter present:
     maths_skills, preparing_for_exams, command_words, glossary;
     periodic_table/index/graph_paper page-coverage check — index parses as
     TableFormer tables -> table_data, the documented IAL precedent)
  4. dual page numbering per chunk; front matter book_pages null
  5. offset law: book_page = pdf_page - 13 on every chunk
  6. chapter_questions chunks anchored inside the 10 probed EXAM PRACTICE ranges
  7. reading order: pdf_pages non-decreasing within each (unit, chapter) group
  8. char_count consistency (recomputed from text)
  9. size bounds 20..2500; 0 LaTeX remnants
 10. content types from the documented vocabulary
 11. front-matter guard: no question/divider/thinking_bigger typing on roman pages
"""
import json, re, sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from book_structure_ych12 import (CHAPTERS, EXTRA_SECTIONS, TOPIC_DIVIDERS,
                                  THINKING_BIGGER, EXAM_PRACTICE, N_PAGES, OFFSET)

CORPUS = os.environ.get("YCH12_CORPUS",
                        "/home/z/my-project/data/ych12_sb2/out/edexcel_ial_chemistry_ych12_sb2_chunks_v1.jsonl")

BASE_KEYS = ["id", "book_title", "author", "unit_no", "unit_name", "chapter_no",
             "chapter_title", "section", "content_type", "book_pages", "pdf_pages",
             "char_count", "text"]
KNOWN_TYPES = {"body", "front_matter", "skills", "topic_divider", "divider",
               "chapter_questions", "unit_questions", "learning_objectives",
               "worked_example", "exam_hint", "key_point", "activity", "practical",
               "did_you_know", "thinking_bigger", "checkpoint", "subject_vocabulary",
               "glossary", "index", "table_data", "maths_skills", "preparing_for_exams",
               "command_words", "periodic_table", "graph_paper", "appendix", "safety"}
EP_RANGES = sorted((b + OFFSET, e + OFFSET) for b, e in EXAM_PRACTICE.values())  # book pages -> pdf pages
FIRST_ARABIC_PDF = OFFSET + 2  # 15; book 1 does not exist

errors = []
chunks = [json.loads(l) for l in open(CORPUS)]
print(f"loaded {len(chunks)} chunks")

# v2 fresh-parse lane: YCH12_VERSION=v2 asserts the ych2_v2_ grammar (default
# v1). (VER interpolates DIRECTLY into the id regex and the report filename —
# the value must be "v2", not "2": E-005 in books/README.md.)
VER = os.environ.get("YCH12_VERSION", "v1")
ID_RE = re.compile(rf"ych2_{VER}_u\d+_c\d+_pdf\d{{3}}_\d{{4}}")

# 1. unique IDs + grammar
ids = [c["id"] for c in chunks]
if len(set(ids)) != len(ids):
    errors.append("duplicate chunk ids")
for cid in ids:
    if not ID_RE.fullmatch(cid):
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
for i, (unit, label, title, b, e) in enumerate(CHAPTERS):
    cno = i + 1
    got = by_chapter.get(cno)
    if not got:
        errors.append(f"chapter {cno} ({label} {title}) has no chunks")
    elif got != {unit}:
        errors.append(f"chapter {cno} unit mismatch: {got} != {unit}")
units_seen = {c["unit_no"] for c in chunks if c["unit_no"]}
if units_seen != set(range(11, 21)):
    errors.append(f"topic coverage {sorted(units_seen)} != 11-20")
for need in ("maths_skills", "preparing_for_exams", "command_words", "glossary"):
    if not any(c["content_type"] == need for c in chunks):
        errors.append(f"back matter {need} missing")
# periodic table (book 298 = pdf 310) and graph-paper end leaves (books 305-308 =
# pdf 317-320) are image-only end-matter pages: they are recorded as by-design
# gaps in the parse report, not chunked (no text exists to chunk). Index pages
# (pdf 311-316) parse as TableFormer tables -> table_data chunks (documented IAL
# precedent).
def covered(pdf_lo, pdf_hi):
    return any(c["pdf_pages"][0] <= pdf_hi and c["pdf_pages"][1] >= pdf_lo for c in chunks)
if not covered(311, 316):
    errors.append("index pages (pdf 311-316) not covered by any chunk")
report_path = os.path.join(os.path.dirname(CORPUS), f"parse_report_{VER}.json")
gaps = {g["pdf_page"]: g for g in json.load(open(report_path)).get("by_design_gaps", [])}
for pdf_page, kind in ((310, "periodic_table"), (317, "graph_paper"),
                       (318, "graph_paper"), (319, "graph_paper"), (320, "graph_paper")):
    if pdf_page not in gaps or gaps[pdf_page].get("kind") != kind:
        errors.append(f"image-only end-matter page pdf {pdf_page} ({kind}) not registered "
                      f"in parse_report by_design_gaps")

# 4/5. dual numbering + offset law
for c in chunks:
    bp, pp = c["book_pages"], c["pdf_pages"]
    if not (isinstance(pp, list) and len(pp) == 2 and 1 <= pp[0] <= pp[1] <= N_PAGES):
        errors.append(f"{c['id']}: bad pdf_pages {pp}")
        continue
    if pp[0] < FIRST_ARABIC_PDF:  # front matter roman region
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
ep_touched = set()
for c in chunks:
    if c["content_type"] == "chapter_questions":
        n_q += 1
        s, e = c["pdf_pages"]
        hit = any(s >= a and e <= b for a, b in EP_RANGES)
        if not hit:
            errors.append(f"{c['id']}: chapter_questions outside EXAM PRACTICE ranges pp={s}-{e}")
        for i, (a, b) in enumerate(EP_RANGES):
            if s >= a and e <= b:
                ep_touched.add(i)
if len(ep_touched) != 10:
    errors.append(f"EP banks covered: {len(ep_touched)}/10")

# 7. reading order within (unit, chapter) group
ORDERED_TYPES = {"body", "learning_objectives", "worked_example", "exam_hint",
                 "checkpoint", "subject_vocabulary", "key_point", "practical",
                 "did_you_know", "thinking_bigger", "table_data", "activity",
                 "chapter_questions", "topic_divider"}
per_group = {}
for c in chunks:
    if c["content_type"] in ORDERED_TYPES:
        per_group.setdefault((c["unit_no"], c["chapter_no"], c["content_type"]), []).append(c)
for key, cs in per_group.items():
    seq = [c["pdf_pages"][0] for c in cs]
    breaks = [(i, seq[i - 1], seq[i]) for i in range(1, len(seq)) if seq[i] < seq[i - 1] - 1]
    if breaks:
        errors.append(f"order breaks in {key}: {breaks[:3]}")

# 8. char_count
for c in chunks:
    if c["char_count"] != len(c["text"]):
        errors.append(f"{c['id']}: char_count {c['char_count']} != len(text) {len(c['text'])}")

# 9. size bounds + latex remnants
for c in chunks:
    if len(c["text"]) < 20:
        errors.append(f"{c['id']}: chunk too small ({len(c['text'])})")
    # hard max 2400->2500 (E-007, CONT-V2-5): polish de-glue repairs restore
    # dropped spaces and legitimately grow text — first offender
    # u15_c11_pdf154_0756 2367->2430 (wording-identical, LCS guard passed);
    # pristine max 2367, so 2500 leaves bounded headroom without re-opening
    # the parse-era runaway class the bound exists for.
    if len(c["text"]) > 2500:
        errors.append(f"{c['id']}: chunk over hard max ({len(c['text'])})")
    if re.search(r"\\[a-zA-Z]+|\{\\\w", c["text"]):
        errors.append(f"{c['id']}: LaTeX remnant")

# 10. types
for c in chunks:
    if c["content_type"] not in KNOWN_TYPES:
        errors.append(f"{c['id']}: unknown content_type {c['content_type']}")

# 11. front-matter guard
FM_TYPE_GUARD = {"chapter_questions", "unit_questions", "thinking_bigger", "topic_divider"}
for c in chunks:
    if c["pdf_pages"][0] < FIRST_ARABIC_PDF and c["content_type"] in FM_TYPE_GUARD:
        errors.append(f"{c['id']}: phantom {c['content_type']} on front-matter pages")

print(f"chapter_questions chunks: {n_q}; EP banks covered: {len(ep_touched)}/10")
if errors:
    print(f"\nFAIL: {len(errors)} errors")
    for e in errors[:40]:
        print("  -", e)
    sys.exit(1)
print("\nALL CHECKS PASSED")
