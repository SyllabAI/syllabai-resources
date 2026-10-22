# YPH11 lane — pipeline worklog

---
Task ID: T-PARSE-YPH11-1
Agent: Super Z (main)
Task: Parse CATALOG tracker row 3 book 1 (YPH11 SB1) per books/README.md §5
phases 0-10; operator directive "start the next book from CATALOG queue".

Work Log:
- Phase 0: SB1 lazy-fetched from origin (blob 12e4d968 → data/yph11_sb1.pdf);
  sha256 verified against the pinned intake value. Workspace reset #3 found at
  session start (packages/caches wiped; biology polish still parked at 91/363
  from T-PARSE-4BI1-1). Env rebuild: CPU-torch first (L-016), docling 2.33.0,
  rapidocr-onnxruntime 1.4.4 (NOT rapidocr 3.x — docling 2.33 imports
  rapidocr_onnxruntime), onnxruntime, artifacts re-downloaded to data/models.
- Phase 1: inspect — 225 pp, 15/15 sampled pages 0 text chars, exactly 1
  full-page image per page, Skia/PDF m75 producer, fake outline (223
  ActiveLearn URL entries), uniform single pages (no 2-up). OCR route
  mandatory, as the intake README said.
- Phase 2: structure probed visually (rendered PNGs) + production-stack OCR.
  Page law book = pdf − 11 confirmed 5 ways (D-4); book page 1 absent from
  the PDF. 4 topics / 11 chapters; per-chapter EXAM PRACTICE banks; back
  matter incl. unlisted ACKNOWLEDGEMENTS (b214). Marker census: 223/225
  pages carry glue runs; Hudson marker families mapped. "PDF COMPILED BY
  SAAD" mark found on the SB1 cover (README previously disclosed it only
  for SB2) — disclosed here.
- Phase 3: book_structure_yph11.py (topics/chapters/EXTRA_SECTIONS/markers/
  TYPE_PRIORITY), boundary coherence asserted (EP banks end exactly at next
  chapter start).
- Phase 4: docling_full_yph11.py (2.33 API fix: AcceleratorOptions import;
  correct DOCLING_ARTIFACTS_PATH env name — the committed 4ph1 scripts carry
  a corrupted "n" placeholder, errata E-003). 225/225 pages in 9 foreground
  windows (~14-17 s/page; index pages 300+ s under no-formula retry; peak
  RSS 3.4 GB).
- Phase 5: parse_docling_yph11.py. Formula-region crisis + rescue per
  METHOD D-7: 267/272 formula items empty (docling 2.33 bug); VLM crop
  decoding rejected (slow + hallucination risk); 260 equations manually
  transcribed from rendered pages via manual_formula_ws_yph11.py
  (worksheets with bbox + context alignment, idempotent apply, evidence
  sidecar manual_formulas.jsonl). 5 empty regions adjudicated decorative.
- Phase 6: validate_yph11.py — ALL CHECKS PASSED after three validator-side
  fixes (offset-law direction, index coverage via table_data precedent,
  front-matter phantom question chunks fixed in the chunker, not the check).
  Corpus v1: 881 chunks, 67 chapter_questions, 11/11 EP banks, 0 over
  hard-max, 0 LaTeX remnants. Pristine snapshot taken for future merge diffs.
- Phase 7: census 63% glue-hit → selected 404 (56/67 question chunks
  force-included); llm_repair_yph11.js (4PH1 guards: 0.97 whitespace-LCS,
  line-strict retry, Unicode non-decrease, pipe discipline). Gateway opened
  briefly (1 chunk OK) then re-walled — run quota-stops cleanly, resumable.
  SHIPPED PARTIAL per PM-3 (same disposition as 4BI1 R1).

Stage Summary:
- Corpus v1 LIVE in parsed/ (881 chunks, yph1_v1_ ids) + parse_report_v1.json
  (formula_rescue provenance embedded) + full_book_docling.md + pristine
  snapshot. Polish R1 parked at 1/404 — resume: `node scripts/llm_repair_
  yph11.js` → merge_llm_yph11.py (to write; physics merge is the template) →
  audit → validate. SB2 parse lane untouched (follow-on task).
