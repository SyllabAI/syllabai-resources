# Pearson Edexcel International A-Level Chemistry (2018), YCH11 — Student Book 1

**Status:** SB1 **PARSED** (T-PARSE-YCH11-1, 2026-10-24: corpus v1 1571 chunks,
validator ALL CHECKS PASSED; 291 blank display-equation regions recovered by
verbatim manual transcription before chunking; LLM polish R1–R4 partial at
130/800, quota-walled, resumable). SB2 = parsed in the sibling `ych12` lane
(T-PARSE-YCH12-1, 2026-10-25; `ych2_v1_` law) — the NOT-SOURCED note above was
drift from before that lane landed, repaired here.
Scaffold per `books/README.md` §5 (copy of the `physics/yph11/` IAL lane).

## Books of this lane

### Pearson Edexcel International AS Level Chemistry Student Book 1

- **Title:** Pearson Edexcel International AS / A Level Chemistry Student Book 1
- **Authors:** Cliff Curtis, Jason Murgatroyd, with David Scott (verified from the landed copy's cover, per E-001 discipline)
- **ISBN:** 978-1292244860 (Pearson 2018; dokumen.pub listing cross-check)
- **Coverage:** IAS Units 1 & 2 = Topics 1–10 (Unit 1: Structure, Bonding and Introduction to Organic Chemistry = Topics 1–5; Unit 2: Energetics, Group Chemistry, Halogenoalkanes and Alcohols = Topics 6–10). Unit 3 is the practical unit — no SB.
- **File:** `source/student-book-1.pdf` (ARCHIVE COPY — derivation note below)
- **Pages:** 329 PDF pages (front matter roman i–xiii = PDF 2–14; arabic book 2–316 = PDF 15–329; book page 1 does not exist in the PDF — print blank omitted, same law class as YPH11)
- **Bytes:** 148,791,436
- **sha256 (original of record):** `3d5348894f011e3fb8351f6c8badd691e1bbb2ea54d64eb306524dd0b20372eb`
- **Quality:** Image-only print replica (one full-page image per page, ~150 DPI; zero text layer — 20/20 sampled pages 0 chars) → OCR route (the proven 4CH1/4PH1/YCH11-stack). Producer Skia/PDF m75, Chromium creator; fake per-page ActiveLearn OPS outline. Cover is CLEAN (no third-party "PDF COMPILED BY" mark — unlike the YPH11 siblings).
- **Derivation note (disclosed):** the original exceeds GitHub's 100 MiB hard file limit, so the archive copy is a ghostscript `pdfwrite` derivative (color images resampled to 145 dpi Bicubic, DCTEncode, `-dPassThroughJPEGImages=false` per books/README.md L-022 — the flag without which /ebook is a no-op on JPEG pass-through). Pages unchanged (329); contents-page pixel MAE 1.17/255 vs the original; original retained at the provenance URL.
- **Parse of record (T-PARSE-YCH11-1, 2026-10-24):** docling 2.33.0 + rapidocr-onnxruntime 1.4.4 OCR route (formula enrichment OFF — 2.33 emits empty formula text either way, YPH11 D-7/L-020), 329/329 pages checkpointed; page law `book = pdf − 13` confirmed 3 ways (roman = pdf−1 i–xiii; TOC openers; printed digits "27"/"309"/"311"); 2 units / 10 topics / 35 chapters (1A–10D), per-topic THINKING BIGGER + EXAM PRACTICE banks (10/10 anchored); corpus v1 = **1571 chunks** (`ych1_v1_`), validator ALL CHECKS PASSED; 291 empty formula regions + 4 fraction-mangled items recovered by verbatim manual transcription from 150 dpi renders (evidence `pipeline/evidence/manual_formulas_ych11.jsonl`, 295 records, 8 adjudicated slivers); LLM polish R1–R4 partial (130/800 — 152 records: 130 ok / 14 rejected /
8 error-cum-429 — across six quota windows, quota-walled, resumable; anchor
diff 0 drift; 0 Unicode regressions)
- **Provenance:** https://www.taleem360.com/edexcel-international-a-level-chemistry-student-book-1-in-pdf-gfv (direct download link `?f=062fc8b2`, served 148,791,436 bytes to a Googlebot UA — the method of record from the YPH11 lane; this title was not reCAPTCHA-walled)

## Structure (probed 2026-10-24, production-confirmed at parse)

- **Page law:** `book = pdf − 13`, confirmed 3 ways: (1) roman headers PDF 5=iv … PDF 14=xiii (`roman = pdf − 1`); (2) TOC cross-checks (TOPIC 1 = book 2 → PDF 15; 1A = book 4 → PDF 17); (3) printed header digits (PDF 40 prints "27"; INDEX header prints "309" on PDF 322 and "311" on PDF 324 — the file's TOC promises INDEX 309, so the copy is COMPLETE, books/README.md L-021 discipline).
- **Units/topics/chapters:** 2 units, 10 topics, 35 lettered chapters (1A–1E, 2A–2B, 3A–3E, 4A–4B, 5A–5B, 6A–6G, 7A–7B, 8A–8D, 9A–9B, 10A–10D). Unit 1 = Topics 1–5 (book 2–147), Unit 2 = Topics 6–10 (book 148–289). Per-topic THINKING BIGGER + EXAM PRACTICE banks end each topic (10 EP banks).
- **Back matter:** MATHS SKILLS 290, PREPARING FOR YOUR EXAMS 296, COMMAND WORDS 302, GLOSSARY 304, PERIODIC TABLE 308, INDEX 309–315, graph-paper end leaf (book 316). NO answers section (Pearson publishes answers separately — same as the YPH11 books).
- **Front matter:** cover, i–xiii (course structure ×3, about this book, assessment overview ×2 incl. AOs/weightings tables) — `book_pages: null`.

## Course binding (planned)

v2 hub course ial-chemistry-17 (matches the SME-ExamQuestion lane name) · specKey
`pearson-edexcel/international-a-level/chemistry/ych11` — hub wiring lands at the serving lane.


## SERVING (T-BOOK-SERVE, 2026-10-31 — operator order trace 1a18fe1f9cace659)

- **r0 serving package LANDED**: `manifest.json` (book-slices-manifest-v2; unit =
  TOPIC 1–10) + `chapters/u{t}_c{n}.pdf` (35 lesson slices, 1A–10D) +
  `units/u{t}_practice.pdf` (10 per-topic EXAM PRACTICE banks as `unit_exam`,
  incl. T9's 4pp) + root `student-book-1.pdf` (blob-reuse of source/).
  THINKING BIGGER pages honestly unsliced (no mount — the EP bank is the
  question surface). Receipt: `pipeline/slices-gen-receipt.json`.
- documentId `5fe299af-08a7-53e1-85fc-c914e997062d` (derived ibm-docling@v3 of the archived bytes,
  sha256 `b17ea91f…7927`).
- Remaining: hub multi-book law (v2 PR) → DB apply + T-C20 flip (operator-gated,
  Neon MAIN paused).

## Next steps

1. Parse lane per `books/README.md` §5 phases 0–10 (quality gate: `../../PARSE_STANDARD.md` 8 points).
3. Serving lane — ARCHIVE-SIDE r0 LANDED 2026-10-31 (T-BOOK-SERVE, trace 1a18fe1f9cace659; see the SERVING section below); remaining: hub multi-book wiring (v2 PR) + DB apply + T-C20 flip.
3. Update `books/CATALOG.md` tracker in the same commit as each state change.
