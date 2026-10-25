# YPH11 SB1 — Parsed Deliverables (v1, 2026-10-22)

**Book:** Pearson Edexcel International AS Level Physics Student Book 1
(Miles Hudson, Pearson 2018, ISBN 978-1292244877) — IAS Units 1-2 = Topics 1-4.
**Source:** `../source/student-book-1.pdf` · sha256 `aa1aed60…c015d0` · 225 pp
image-only print replica (Skia/Chromium, ActiveLearn) → Docling 2.33.0 +
rapidocr-onnxruntime 1.4.4 OCR route.
**Corpus:** `edexcel_ial_physics_yph11_sb1_chunks_v1.jsonl` = **881 chunks**,
15-key grammar (`yph1_v1_` ids). Validator: ALL CHECKS PASSED
(`../pipeline/scripts/validate_yph11.py`).
**Page law:** `book_page = pdf_page − 11` (5-way confirmed); front matter
(roman i-xi = PDF 1-12) carries `book_pages: null`; book page 1 does not exist
in the PDF (print blank omitted — first arabic page is book 2 = PDF 13).

## Schema

15-key flat grammar, identical to chemistry/physics/biology lanes:

```json
{"id": "yph1_v1_u1_c1_pdf022_0120", "book_title": "...", "author": "Miles Hudson",
 "unit_no": 1, "unit_name": "Mechanics", "chapter_no": 1, "chapter_title": "Motion",
 "section": "VELOCITY AND ACCELERATION", "content_type": "body",
 "book_pages": [11, 11], "pdf_pages": [22, 22], "char_count": 613, "text": "..."}
```

`unit` = IAL TOPIC (1-4); `chapter` = the book's own A/B/C/D chapter (1-11:
1A Motion, 1B Energy, 1C Momentum, 2A Fluids, 2B Solid material properties,
3A Basic waves, 3B Behaviour of waves, 3C More wave properties of light,
3D Quantum physics, 4A Electrical quantities, 4B Complete electrical circuits).
WaaP + back matter use `unit_no: null` (→ `u0` in ids).

## Content types (16) and RAG advice

| type | n | advice |
|---|---|---|
| body | ~350 | core teaching content — include |
| table_data | ~99 | TableFormer tables incl. the 4-column index (pdf 222-224, filter-friendly but keep for completeness), spec/data tables (resistivity, densities, exam structure) |
| chapter_questions | 67 | **serving-critical** — the 11 per-chapter EXAM PRACTICE banks (2 pp each, 11/11 anchored); drive the serving split |
| exam_hint | ~89 | EXAM HINT / LEARNING TIP boxes — high value for exam-prep retrieval |
| learning_objectives | ~48 | lesson LO boxes — great chapter/lesson summaries |
| worked_example | ~39 | WORKED EXAMPLE boxes with full solutions — high value |
| subject_vocabulary | 42 | end-of-chapter glossary boxes — definitions |
| checkpoint | 28 | CHECKPOINT self-check questions (with answers inferable from content) |
| skills | ~38 | Working as a Physicist (book 2-7) + MATHS SKILLS reference (book 194-199) |
| thinking_bigger | 13 | context/history spread pages per chapter |
| front_matter | ~26 | contents/course structure/about/practical skills/assessment overview (roman pages) |
| did_you_know | 8 | sidebar fact boxes |
| practical | 6 | CORE PRACTICAL / PRACTICAL SKILLS method boxes |
| appendix | ~27 | Preparing for your exams + sample exam answers + command words + acknowledgements |
| glossary | 10 | book glossary (book 207-210) |

## LLM fidelity polish

Round 1 selected 404/881 (all 56 glue-hit question chunks force-included;
63% of chunks carry scan-wide dropped-space runs — same class as 4PH1).
**Status: R1 COMPLETE 2026-10-25 — 404/404 terminal** (394 applied, 390 with
text changes; 7 guard-rejected raws kept as evidence with original text
preserved). Guards: length drift 0.6-1.7×, refusals, Unicode-unit
non-decrease, per-line pipe counts on tables, wording fidelity via
whitespace-stripped char-LCS ≥ 0.97 (the space-drop calibration —
L-006/L-015). Post-merge: anchor diff vs pristine **0 drift**; validator
**ALL CHECKS PASSED** (881 chunks, 11/11 chapters, 4/4 units, 22/22
question pages). Audit: dominant damage class space-glue **1759 → 4** on
repaired chunks (4 residuals are real URLs in acknowledgements, correctly
untouched); camel-glue 121 → 4; caps-glue 100 → 22; 0 Unicode-unit
regressions; superscript-bearing chunks 73 → 103 (proper physics notation
restored). 5 regen-only glue-damage stragglers below the R1 selector cap
are logged as R2 candidates (selector reconciliation in
`pipeline/scripts/select_noisy_yph11.py`). Runner/merge/audit/validate
chain is idempotent and re-runnable.

## Formula-provenance note

docling 2.33.0 emits formula REGIONS with EMPTY text (known §4.3 bug): 267/272
formula items were blank in the base parse. All 253 orphaned equations were
recovered by **verbatim manual transcription** from rendered pages
(transcription-only discipline; per-crop VLM decoding was rejected for
hallucination risk). Every page-JSON formula item patched this way is flagged
`formula_rescued: true, rescue: "manual-transcription"`; the sidecar log is
`../pipeline/evidence/manual_formulas.jsonl`. 5 items carried parse-native
text; 5 empty regions were adjudicated decorative/region-split slivers (no
content loss — checked against rendered pages).

---

## SB2 deliverable (delta lane, 2026-10-22)

| File | Book | Chunks | ID prefix |
|---|---|---|---|
| `edexcel_ial_physics_yph11_sb2_chunks_v1.jsonl` | SB2 (IA2, Units 4–5, Topics 5–11) | 826 | `yph2_v1_` |

Plus `full_book_sb2_docling.md` + `parse_report_sb2_v1.json`. Schema identical
to SB1 (15-key flat grammar; additive IAL types). Offset law `book = pdf − 10`
(no printed page 1; arabic starts at book 2 = PDF 12). 18 content types; 13/13
EXAM PRACTICE pairs typed `chapter_questions` and page-anchored. Validator:
`../pipeline/scripts/validate_ial_physics_sb2.py` — ALL CHECKS PASSED.

**SB2 formula provenance:** docling 2.33 blank-formula bug applies (278 empty
regions — `../pipeline/evidence/formula_orphans_sb2.json`); display equations
survive as plain OCR text (e.g. `E_k = p²/2m` renders as plain-run text);
verbatim manual transcription rescue is PENDING for SB2 (SB1's
manual_formula_ws_yph11.py is the precedent of record). SB2 formula items that
did decode: 9 converted to Unicode, 1 failed (dropped, body text carries it).

**SB2 polish status:** selected 794/826 (all 67 chapter_questions forced +
glue-scored), 0 applied — the same account-level 429 wall as SB1 R1; resume
identical (`pipeline/scripts/llm_repair_ial_physics_sb2.js` →
`merge_llm_ial_physics_sb2.py` → `audit_polish_ial_physics_sb2.py` →
re-validate; pristine snapshot shipped at
`edexcel_ial_physics_yph11_sb2_chunks_v1.pristine`).
