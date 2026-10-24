# YCH12 SB2 — parsed corpus v1

| Field | Value |
| --- | --- |
| Book | Pearson Edexcel International AS/A Level Chemistry Student Book 2 (Curtis, Murgatroyd & Scott), ISBN 978-1-292-24472-3, 320 pp image-only print replica |
| Corpus | `edexcel_ial_chemistry_ych12_sb2_chunks_v1.jsonl` — **1400 chunks**, id law `ych2_v1_u<unit|0>_c<chapter|0>_pdf<ppp>_<bbbb>` (unit = TOPIC 11–20; chapter = sequential c1–c19 over lettered chapters 11A–20A) |
| Grammar | 13 base keys; `text_original` + `llm_repaired` reserved for the polish merge (none applied yet — R1 staged, quota-walled) |
| Page law | `book = pdf − 12` (4-way confirmed); front matter roman ii–xiii = PDF 2–13 with `book_pages: null`; book page 1 does not exist |
| Content types | 17 (body 549, table_data 197, exam_hint 128, chapter_questions 84, learning_objectives 76, thinking_bigger 69, checkpoint 68, subject_vocabulary 48, front_matter 45, topic_divider 32, worked_example 30, did_you_know 30, …) |
| Sizes | 41–2367 chars, avg 628, 0 over the 2400 hard max |
| Validation | `validate_ych12.py` ALL CHECKS PASSED; chunker byte-identity double-run sha256 `06864a80…` twice |
| Formula rescue | 315 empty formula regions exported; 133 verbatim-transcribed (127 fills + 6 adjudicated); **182 orphans on 71 pages remain — resumable** (evidence: `../pipeline/evidence/formula_orphans.json` + `manual_formulas_ych12.jsonl`) |
| LLM polish | R1 **staged, not started**: 800/1400 ids selected (`../pipeline/evidence/llm_repair_ids_ych12.json`), account-level 429 wall (probe-verified 2026-10-25) |
| By-design gaps | periodic-table page (book 298) + FOUR graph-paper end leaves (books 305–308) — image-only, registered in `parse_report_v1.json → by_design_gaps`, asserted by the validator |

## Files

- `edexcel_ial_chemistry_ych12_sb2_chunks_v1.jsonl` — the corpus (serving input)
- `edexcel_ial_chemistry_ych12_sb2_chunks_v1.pristine` — pre-polish byte-identity baseline (sha256 `06864a80…`); never edit
- `full_book_docling.md` — human-readable whole-book markdown regenerated from the corpus
- `parse_report_v1.json` — parse metadata, content-type census, page law, rescue + polish provenance, by-design gaps

## Resume recipes

```bash
# formula rescue continuation (182 orphans on 71 pages)
python3 ../pipeline/scripts/render_orphan_pages_ych12.py     # renders formula_png/
# ... transcribe remaining orphans verbatim into manual_batch_N.jsonl ...
cat manual_batch_*.jsonl > manual_formulas_ych12.jsonl
python3 ../pipeline/scripts/manual_formula_ws_ych12.py       # idempotent, bbox-verified
python3 ../pipeline/scripts/parse_docling_ych12.py           # re-chunk
YCH12_CORPUS=<out>/edexcel_ial_chemistry_ych12_sb2_chunks_v1.jsonl \
  python3 ../pipeline/scripts/validate_ych12.py              # must stay ALL CHECKS PASSED

# LLM polish R1 (when quota clears) — clone the YCH11 llm_repair_ych11.js pattern
# onto data/ych12_sb2/ with llm_repair_ids_ych12.json, then merge + audit + re-validate
```
