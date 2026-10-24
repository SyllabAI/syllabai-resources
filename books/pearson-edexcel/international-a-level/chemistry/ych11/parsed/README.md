# YCH11 SB1 parsed corpus — RAG deliverables (v1)

**Book:** Pearson Edexcel International AS/A Level Chemistry Student Book 1
(Curtis, Murgatroyd & Scott, Pearson 2018; IAS Units 1–2 = Topics 1–10).
**Corpus of record:** `edexcel_ial_chemistry_ych11_sb1_chunks_v1.jsonl` —
**1571 chunks**, ID prefix `ych1_v1_`, validator ALL CHECKS PASSED
(`../pipeline/scripts/validate_ych11.py`). Parse: docling 2.33.0 +
rapidocr-onnxruntime 1.4.4 OCR route; 291 blank display-equation regions
recovered by verbatim manual transcription before chunking; LLM polish R1
partial (48/800, quota-walled, resumable — see polish section).
**Pristine snapshot:** `edexcel_ial_chemistry_ych11_sb1_chunks_v1.pristine`
(pre-polish corpus; the merge's anchor diff runs against this file).

## Files

| File | What it is |
|---|---|
| `edexcel_ial_chemistry_ych11_sb1_chunks_v1.jsonl` | the RAG corpus (flat 15-key grammar, one JSON object per line) |
| `edexcel_ial_chemistry_ych11_sb1_chunks_v1.pristine` | pre-polish snapshot (do not serve; diff/audit input) |
| `parse_report_v1.json` | counts, content types, size stats, stack versions, sha256, by-design gaps |
| `full_book_docling.md` | whole book as markdown (reading-order rendering of the corpus) |

## Schema (15-key v3 grammar)

```json
{"id": "ych1_v1_u3_c10_pdf083_0342", "book_title": "...", "author": "...",
 "unit_no": 3, "unit_name": "Unit 1: Structure, Bonding and Introduction to Organic Chemistry",
 "chapter_no": 10, "chapter_title": "3B Covalent bonding", "section": "Electronegativity",
 "content_type": "body", "book_pages": [70, 71], "pdf_pages": [83, 84],
 "char_count": 911, "text": "…",
 "text_original": "…(only on polished chunks)", "llm_repaired": true}
```

- `unit_no` = the book's TOPIC (1–10). IAL mapping: Unit 1 exams Topics 1–5,
  Unit 2 exams Topics 6–10 (the book's own assessment tables).
- `chapter_no` = 1–35 sequential over the lettered chapters 1A…10D.
- `book_pages` = citation numbering (`book = pdf − 13`); `null` for front
  matter (roman i–xiii = PDF 2–14; book page 1 does not exist in the PDF).
- Chunk ID grammar: `ych1_v1_u<unit|0>_c<chapter|0>_pdf<pdfpage:03d>_<block:04d>`
  (SB2 will use `ych2_v1_` — the two-book law, YPH11 D-8).

## Content types (16) and RAG advice

| type | n | advice |
|---|---|---|
| body | 614 | main prose; the default retrieval surface |
| table_data | 206 | TableFormer tables incl. the 7-page index (309–315); keep, but expect pipe rows |
| learning_objectives | 96 | spec-mapped objectives (SPEC REFERENCE chips); high-value for "what must I know" queries |
| exam_hint | 143 | EXAM HINT + LEARNING TIP boxes; exam-technique gold |
| checkpoint | 92 | end-of-section self-check questions with answers-in-context |
| chapter_questions | 59 | the 10 per-topic EXAM PRACTICE banks (serving-critical anchors — pages 38/62/96/126/146/166/182/232/256/288 book) |
| thinking_bigger | 69 | per-topic real-world context + SCIENCE COMMUNICATION activities |
| subject_vocabulary | 74 | glossary-style definition boxes |
| worked_example | 58 | step-by-step calculations |
| did_you_know | 29 | enrichment snippets |
| front_matter | 46 | course structure / assessment overview (book_pages null) |
| skills | 17 | MATHS SKILLS section (290–295) |
| preparing_for_exams | 21 | sample answers + exam technique (296–301) |
| topic_divider | 35 | the 10 topic opener pages (2 pp each) |
| command_words | 1 | command-word glossary (302–303) |
| glossary | 11 | back-matter glossary (304–307) |

Not present (structurally): `practical` — the Core Practicals live in the
companion Lab Book; this book carries only CP chips. `index`/`graph_paper`/
`periodic_table` types — the index parses as `table_data` (IAL precedent);
the periodic-table page (book 308) and graph-paper end leaf (book 316) are
image-only, recorded in `parse_report_v1.json → by_design_gaps`.

## Polish provenance

LLM fidelity polish R1: 800/1571 selected (worst-first glue scoring; all 59
question chunks force-included); **48 applied** across two quota windows
before the account-level 429 wall re-closed (PM-3 disposition, resumable).
Polished chunks carry `text_original` + `llm_repaired: true`; guards:
0.97 whitespace-stripped LCS wording fidelity, line-strict retry, table pipe
discipline, Unicode non-decrease. Anchor diff vs pristine: 0 drift on all
serving-critical fields. Audit: glue runs 459→5 on changed chunks (survivors
are real long chemistry words); 0 Unicode regressions.
**Resume:** `node ../pipeline/scripts/llm_repair_ych11.js` →
`python3 ../pipeline/scripts/merge_llm_ych11.py` →
`python3 ../pipeline/scripts/audit_polish_ych11.py` →
`python3 ../pipeline/scripts/validate_ych11.py`.

## Recommended filters

- Retrieval over `body` + `worked_example` + `learning_objectives` for
  teaching content; `exam_hint`/`checkpoint` for exam-technique retrieval.
- Prefer chunks with `llm_repaired: true` when a polished/unpolished tie
  exists (de-glued text; the unpolished residue carries scan-wide
  dropped-space damage — 752 of 800 selected chunks still await R1).
- `chapter_questions` chunks are the serving split anchors — do not merge
  across them downstream.
- Equations inside this corpus are Unicode text (→, ⇌, sub/superscripts,
  (s)/(l)/(g)/(aq) state symbols) — tokenizers handle them natively; do not
  strip the sub/superscript code points.
