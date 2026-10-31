# Pearson Edexcel International A-Level Physics (2018), YPH11 — Student Books (2026-10-21 intake)

**Status:** SB1 **PARSED** (T-PARSE-YPH11-1, 2026-10-22: corpus v1 881 chunks,
validator ALL CHECKS PASSED; LLM polish R1 COMPLETE 2026-10-25 — 404/404,
audit green). SB2 **PARSED** (delta lane, 2026-10-22: corpus v1 826 chunks,
validator ALL CHECKS PASSED; LLM polish R1 COMPLETE 2026-10-30 — 794/794,
audit green). Scaffold per `books/README.md` §5
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
- **Parse of record (T-PARSE-YPH11-1, 2026-10-22):** Docling 2.33.0 + rapidocr-onnxruntime 1.4.4 OCR route, 225/225 pages checkpointed; page law `book = pdf - 11` confirmed 5 ways (roman front matter = pdf-1; TOC cross-checks x3 incl. 1 MOMENTUM b48=PDF59; INDEX header prints "211" on PDF 222; book page 1 does not exist in the PDF — print blank omitted); 4 topics / 11 chapters (1A-4B), per-chapter 2-page EXAM PRACTICE banks as chapter_questions anchors (11/11); corpus v1 = **881 chunks** (`yph1_v1_`), validator ALL CHECKS PASSED; docling 2.33 formula-region bug blanked 267/272 formula items — all recovered by verbatim manual transcription from rendered pages (evidence `pipeline/evidence/manual_formulas.jsonl`); LLM polish R1 COMPLETE (2026-10-25: 404/404 — 394 applied, 7 guard-rejected
evidence kept; audit space-glue 1759→4 on repaired chunks, 0 Unicode-unit
regressions — see `parsed/README.md` polish section)
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

---

## SB2 PARSE (delta lane, 2026-10-22 — same T-PARSE-YPH11-1 task, parallel session)

Student Book 2 was parsed by a second session running the operator's
"Retry YPH11 polish" directive, on top of this lane's SB1 work (L-008
parallel-lane protocol; blob-compare before push, genuine delta only).

- **Corpus:** `parsed/edexcel_ial_physics_yph11_sb2_chunks_v1.jsonl` — **826
  chunks** (`yph2_v1_` prefix per this lane's two-book law), Topics 5–11 /
  13 chapter blocks (5A…11B), offset `book = pdf − 10` (probed 3 ways;
  roman i–xi = PDF 1–11, arabic starts at book 2 = PDF 12 — same no-page-1
  law as SB1). Validator `pipeline/scripts/validate_ial_physics_sb2.py`:
  ALL CHECKS PASSED (13/13 chapters, 7/7 topics, 0 order breaks, strict
  offset law, 13/13 EXAM PRACTICE pairs page-anchored, 0 LaTeX remnants).
- **SOURCE INTEGRITY FIX (books/README.md E-004):** the SB2 archive copy
  landed at intake (41,870,983 B, sha256 `449dc3f3…73d0c`) was TRUNCATED at
  225pp — its own contents page promises COMMAND WORDS 218 / GLOSSARY 220 /
  INDEX 224 but the file ended mid-sample-answers (book 215). The original
  was re-downloaded via the documented taleem360 Googlebot-UA route and
  verified byte-identical to the original-of-record (120,888,486 B, sha256
  `28eabe40…8f`, 237pp), then a fresh complete 145dpi derivative was landed
  (48,278,974 B, sha256 `f8f3fc62…ce82d`, OCR parity 1.0000 vs original on
  the contents page; ghostscript `-dPassThroughJPEGImages=false` required —
  books/README.md L-022). **`source/student-book-2.pdf` is REPLACED in the
  delta commit.**
- **Structure findings:** per-chapter THINKING BIGGER (2pp, second page often
  a SCIENCE COMMUNICATION activity) + EXAM PRACTICE (2pp) pairs for all 13
  chapters; back matter = Maths Skills 204–209, Preparing 210–211, Sample
  Exam Answers 212–217, Command Words 218–219, Glossary 220–223, Index
  224–227 (no picture-credits page). 7 additive IAL content types as in SB1.
- **Formula orphans:** the docling 2.33 blank-formula bug (this lane's
  formula-provenance note above) affects SB2 identically — 278 empty formula
  regions exported to `pipeline/evidence/formula_orphans_sb2.json` for a
  future verbatim manual-transcription rescue (SB1's manual_formula law;
  display equations survive as plain OCR text in the meantime).
- **Polish R1:** glue census 90% of chunks (12+ char runs); 794/826 selected
  (67 chapter_questions forced); **R1 COMPLETE 2026-10-30 — 794/794
  terminal** (774 applied, all text-changed; 20 guard-rejected evidence
  kept) after five quota openings of the account-level 429 wall (2026-10-25
  through 2026-10-30). Post-merge anchor diff vs pristine 0 drift; audit
  space-run 4610 → 15 on repaired chunks, 0 Unicode-unit regressions (7
  residual long-run chunks verified as genuine source content);
  validator ALL CHECKS PASSED post-polish — full record in
  `parsed/README.md` polish section. Chain scripts of record replaced in
  the completion commit (`books/README.md` E-006).
## SERVING (T-BOOK-SERVE, 2026-10-31 — operator order trace 1a18fe1f9cace659)

- **r0 serving packages LANDED** (no-parse shelf law — "we dont need parsing for
  book pdf in book shelf"): per-book manifests `manifest-sb1.json` +
  `manifest-sb2.json` (book-slices-manifest-v2; the MULTI-BOOK MANIFEST LAW — one
  manifest file per book inside the 2-book lane; unit = TOPIC per the book's own
  structure) + chapter slices under per-book scope dirs `sb1/chapters/u{t}_c{n}.pdf`
  (11) and `sb2/chapters/u{t}_c{n}.pdf` (13) + root `student-book-1.pdf` /
  `student-book-2.pdf` (blob-reuse of source/). Receipt:
  `pipeline/slices-gen-receipt.json`.
- documentIds (derivedDocumentId law, checksum|ibm-docling|v3, over the ARCHIVED
  bytes): SB1 `7e6891e1-e41c-5eaf-8aa4-003baffc3907` (sha256 `aa1aed60…015d0`), SB2
  `a767d89e-d678-5b75-9513-1b325915c189` (sha256 **`faf4c467…f988`** — see `books/README.md` E-008;
  differs from the `f8f3fc62…ce82d` pin at equal byte size).
- Anchors: SB1 11/11 + SB2 13/13 EXAM PRACTICE `questionsStartPage` (per-chapter
  EP banks ride the 133g in-chapter jump). `unit_exam`: none (both books anchor
  EP per chapter).
- Remaining: hub multi-book law (v2 PR: registry map + per-book manifest
  resolution + Topic labels) → DB apply + T-C20 flip (operator-gated, Neon MAIN
  paused).

- Pipeline evidence: `pipeline/METHOD_AND_FINDINGS_SB2.md`,
  `pipeline/worklog_sb2.md`, `pipeline/evidence/parse_sb2.log`,
  `pipeline/evidence/llm_repair_ids_sb2.json`, `pipeline/docling_pages_sb2/`
  (237 per-page checkpoints).
