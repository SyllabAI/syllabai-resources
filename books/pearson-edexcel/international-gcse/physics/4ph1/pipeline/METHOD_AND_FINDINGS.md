# Physics 4PH1 Parse — Method, Findings & Decisions

**Date:** 2026-10-19 · **Parse agent:** Super Z lane · **Task IDs:** T-PARSE-4PH1-1/2/3
**Standard:** `books/pearson-edexcel/international-gcse/PARSE_STANDARD.md` (8-point, from the chemistry audit) + operator serving-critical directive on question typing and per-chunk dual page numbering.

## 1. Source

- 308-page image-only scan (RICOH MP C4503 producer, zero text layer on all
  sampled pages) → OCR route mandatory, same as chemistry.
- sha256 `9b0783d9…313a` pinned in README + parse report.
- Received via operator tmpfiles link after direct GitHub upload failed
  (trace 1a1539ed1a5c074d); pushed to repo by the parse lane.

## 2. Structure reverse-engineering (finding #1)

- 8 units / 28 chapters (chemistry had 4/29) — TOC at PDF 5–7.
- **Offset book = PDF − 10**, confirmed three ways: PDF 144's running header
  prints "134"; ch1 opener PDF 13 = book 3; index 289 → PDF 299 (plausible vs
  308 pages).
- TOC OCR digit garbles resolved by LEARNING OBJECTIVES page scan of the
  parsed corpus: ch8 = 75 (not "15"), ch16 = 150 (opener PDF 160), ch17 = 158
  (opener PDF 168 — objectives on the facing page), ch22 = 221 (opener PDF
  231). Ch11's opener regex initially missed because OCR rendered
  "LEARNING.OBJECTIVES" with a period.
- Book page 1 = PDF 11 = Experimental Skills page (typed `skills`, like
  chemistry's skills pages); front matter = PDF 1–10.
- **This book has NO answers section** (unlike chemistry) — verified by
  corpus-wide marker scan.
- Unit-question ranges (8 units) located by merged-OCR-aware scan
  (`UNIT\s*QUESTIONS` catches `UNITQUESTIONS`); 47 question-typed chunks land
  exactly on those pages (serving-critical requirement met).

## 3. Parser-stack saga (finding #2 — the big one)

The workspace reset wiped all packages; the reinstall exposed version mines:

| Attempt | Result |
|---|---|
| docling 2.140 (fresh default) | Formulas decoded BUT ~140–230 s/page on graph-heavy pages; root cause: CodeFormulaV2 VLM engine `max_new_tokens` defaults to **4096** — graph regions decoded as formulas burn thousands of tokens on 2 CPU cores |
| docling 2.33.0 (mistaken "2.133") | Fast (~9–13 s/page) BUT CodeFormula v1 integration returns **empty** formula text in this env; also crashed (`list index out of range`) on 4+ pages |
| docling 2.133.0 (chemistry's actual version) | Formulas decode (verified PDF 16: `s p e e = gradient = distance/time = 30m/2.5s = 12 m/s` → converted to Unicode) BUT erratic multi-minute hangs on ordinary pages (PDF 20 > 9 min) and required rapidocr 3.9.2 (3.10.0 removed `PP_OCRV6_LANGS`) + artifacts-path reshuffle (heron repo copy, tableformer `accurate/`+`fast/` symlinks, CodeFormulaV2 re-download) |

**Decision (bounded time, checkpointed durability): page-level hybrid.**
Keep the fast 2.33 corpus as the base (305 pages), splice in the two verified
2.133 formula-decoded pages (PDF 16–17), and use a Tesseract fallback for the
pages docling could not process at all (PDF 14, 20, 21; PDF 307 is genuinely
blank — pixel-verified). The retry ladder in `docling_full_physics.py`
(formula ON → formula OFF → record error) plus per-page JSON checkpointing
made every failure recoverable without losing the grind.

**Finding #3:** 33 pages were re-parsed with formula enrichment OFF (CodeFormula
crash); their display equations survive as plain RapidOCR text (e.g.
"v2 = u2 + (2 x a x s)") rather than LaTeX-decoded Unicode. Display equations
in this book are ALSO almost always present in body text, so content loss is
marginal — documented rather than risked hours of re-grind.

## 4. Chunking & validation

- `book_structure_physics.py` + `parse_docling_physics.py` — same architecture
  as the audited chemistry pipeline (LaTeX→Unicode physics incl. `∝, λ, ρ, Ω`,
  state symbols, fractions; sidebar double-OCR dedup; heading dedup incl.
  merged-OCR forms `KEYPOINT`, `PHYSICSONLY`, `ACTIVITY1`; 350–1600 char
  packing; `phys_v1_` ID prefix).
- Fix vs chemistry: `split_long` falls back to line/word splitting — index and
  glossary entries have no sentence punctuation, which previously produced
  35k-char chunks (7 over hard max); after fix: max 2299, 0 over hard max.
- New physics content type: `extension_work` (additive; EXTENSION WORK boxes,
  not examinable). `EXAMPLE n` boxes map to `worked_example`; `REMINDER` maps
  to `exam_hint`.
- Validation (`validate_physics.py`): **ALL CHECKS PASSED** — 736 chunks,
  unique IDs, 28/28 chapters, 8/8 units, 0 body order breaks (multi-column
  index internal ordering exempted), dual numbering everywhere, question
  chunks page-anchored, 33 chunks with Unicode superscripts, 0 LaTeX remnants.
- One order-break investigation: index tables (PDF 304–306) reorder chunks
  inside the index type — benign, RAG-filtered, exempted with justification.

## 5. Decision log

| # | Decision | Rationale |
|---|----------|-----------|
| 1 | OCR route (image-only scan) | zero text layer |
| 2 | Page-level hybrid parser stack | 2.133 formula fidelity only on 2 pages; fast 2.33 base; bounded session time; checkpointed resume |
| 3 | Retry ladder per page (formula ON→OFF→error) | CodeFormula crash bug on ~37 pages; layout+tables preserved on retry |
| 4 | Tesseract fallback for 4 pages | docling-unprocessable; schema-compatible records |
| 5 | Blank page 307 accepted | pixel-verified 0.7% ink |
| 6 | `extension_work` as additive content type | truthful typing; additive per standard point 6 |
| 7 | Index ordering exemption in validator | multi-column artifact, RAG-filtered type |
| 8 | No LLM polish in v1 | time-boxed; RapidOCR word-merge noise documented; chemistry v2/v3 polish pattern is the ready remedy |
| 9 | Line/word fallback in split_long | index/glossary have no sentence punctuation |
| 10 | Learning-objectives newline trim applied (3/53 residual) | audit action item for future parses |

## 6. Deliverables

- `parsed/`: `edexcel_igcse_physics_chunks_v1.jsonl` (736 chunks) +
  `full_book_docling.md` + `parse_report_v1.json` + `load_rag.py` + README.
- `pipeline/`: this doc, worklog, scripts (`docling_full_physics.py`,
  `parse_docling_physics.py`, `book_structure_physics.py`, `validate_physics.py`,
  `scan_physics_markers.py`, probe scripts, `tess_fallback.py`).
- `docling_pages/`: 308 per-page JSON checkpoints (raw parser output).
