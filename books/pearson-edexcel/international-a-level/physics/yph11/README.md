# Pearson Edexcel International A-Level Physics (2018), YPH11 — Student Books (2026-10-21 intake)

**Status:** SB1 **PARSED** (T-PARSE-YPH11-1, 2026-10-22: corpus v1 881 chunks,
validator ALL CHECKS PASSED; LLM polish R1 quota-walled at 1/404, resumable).
SB2 = SOURCE (parse lane not started). Scaffold per `books/README.md` §5
(copy of `physics/4ph1/`).

## Books of this lane

### Pearson Edexcel International AS Level Physics Student Book 1

- **Title:** Pearson Edexcel International AS Level Physics Student Book 1
- **Authors:** Miles Hudson
- **ISBN:** 978-1292244877
- **Coverage:** IAS Units 1 & 2 (+ practical guidance; Units 3 is the practical unit, no SB)
- **File:** `source/student-book-1.pdf`
- **Pages:** 225
- **Bytes:** 102,092,995
- **sha256:** `aa1aed604d627fda8a46cf67bd562234b2934abe9d26690e1bf38c27f9c015d0`
- **Quality:** Image-only print replica (one full-page image per page, ~150 DPI; zero text layer) -> OCR route required (the proven 4CH1/4PH1 stack)
- **Disclosed mark:** the cover carries a third-party "PDF COMPILED BY SAAD" annotation (same mark previously disclosed on the SB2 archive copy); content pages are unmarked
- **Parse of record (T-PARSE-YPH11-1, 2026-10-22):** Docling 2.33.0 + rapidocr-onnxruntime 1.4.4 OCR route, 225/225 pages checkpointed; page law `book = pdf - 11` confirmed 5 ways (roman front matter = pdf-1; TOC cross-checks x3 incl. 1 MOMENTUM b48=PDF59; INDEX header prints "211" on PDF 222; book page 1 does not exist in the PDF — print blank omitted); 4 topics / 11 chapters (1A-4B), per-chapter 2-page EXAM PRACTICE banks as chapter_questions anchors (11/11); corpus v1 = **881 chunks** (`yph1_v1_`), validator ALL CHECKS PASSED; docling 2.33 formula-region bug blanked 267/272 formula items — all recovered by verbatim manual transcription from rendered pages (evidence `pipeline/evidence/manual_formulas.jsonl`); LLM polish R1 partial (1/404 — account-level 429 wall, runner resumable)
- **Provenance:** https://www.taleem360.com/edexcel-international-a-level-physics-student-book-1-in-pdf-syq (direct download link f=34f2fa1f, 97.36 MiB listing)

### Pearson Edexcel International A2 Level Physics Student Book 2

- **Title:** Pearson Edexcel International A2 Level Physics Student Book 2
- **Authors:** Miles Hudson
- **ISBN:** 978-1292244478
- **Coverage:** IAL Units 4 & 5, Topics 5–11 + Maths Skills (Unit 6 is the practical unit, no SB) — identity proven by OCR of the cover ("Pearson Edexcel International A Level Physics Student Book 2") and the contents page (Topics 5–11)
- **File:** `source/student-book-2.pdf` (ARCHIVE COPY — see derivation note)
- **Pages:** 237 (full copy; cross-checked 237/238pp scribd copies of the same title)
- **Bytes:** 41,870,983
- **sha256:** `449dc3f34a56d64790abba2b1f39d2a35fd42e98c60e2a7cc063dd1d77573d0c`
- **Original scan (provenance of record):** 120,888,486 bytes · sha256 `28eabe40458d064216f593b44ffa96670f0fef1f7362b39af3a85c4e02ed5f8f` · image-only print replica (one full-page JPEG per page, ~150dpi; zero text layer) → OCR route
- **Derivation note (disclosed):** the original exceeds GitHub's 100 MiB hard file limit, so the archive copy is a ghostscript `pdfwrite` derivative (color images resampled 150→145 dpi Bicubic, DCTEncode, duplicate-image detection on). Pages unchanged (237); OCR parity verified on the contents page (231/234 chars vs original). Original retained locally at `scratch/books_dl_retry/sb2_taleem360.pdf` and re-downloadable at the provenance URL.
- **Quality:** Image-only print replica → OCR route (the proven 4CH1/4PH1/SB1 stack). Disclosed third-party mark: cover carries "PDF COMPILED BY SAAD".
- **Provenance:** https://www.taleem360.com/download/edexcel-international-a-level-physics-book-2-vyu?f=8bab16ce (direct link; the page is reCAPTCHA-walled to normal browsers but serves `text/html`+file to a Googlebot UA — the wall-bypass method of record, 2026-10-21)

## Course binding (planned)

v2 hub course ial-physics-19 · specKey pearson-edexcel/international-a-level/physics/yph11 (pastpapers-corpus.ts COURSE_SPECS grammar; NOTE: no ial-physics spec row exists there yet — hub wiring lands at the serving lane)

## Serving-path note (for the future integration lane)

The v2 hub serves the book PDF at the lane ROOT (`books/<specKey>/student-book.pdf`,
`bookCorpusPathForCourse`); this intake keeps the sha256-pinned source under
`source/` per the scaffold. Integration must copy/promote the pinned file to
the serving path (or the hub per-book file law lands first for multi-book
courses — T-MIG-140 receipt, multibook_disclosure).

## Next steps

1. Parse lane per `books/README.md` §5 phases 0-10 (quality gate:
   `../../PARSE_STANDARD.md` where applicable, else the same 8 points).
2. Serving lane (TEXTBOOK doc + book_chapters + slices manifest + T-C20 flip).
3. Update `books/CATALOG.md` tracker in the same commit as each state change.
