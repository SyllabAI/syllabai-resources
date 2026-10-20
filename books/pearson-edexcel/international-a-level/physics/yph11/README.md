# Pearson Edexcel International A-Level Physics (2018), YPH11 — Student Book Intake (2026-10-21)

**Status:** SOURCE (wave-2 intake, T-MIG-141) — parse lane NOT started.
Scaffold per `books/README.md` §5 (copy of `physics/4ph1/`).

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
- **Provenance:** https://www.taleem360.com/edexcel-international-a-level-physics-student-book-1-in-pdf-syq (direct download link f=34f2fa1f, 97.36 MiB listing)

### Pearson Edexcel International A2 Level Physics Student Book 2

- **Title:** Pearson Edexcel International A2 Level Physics Student Book 2
- **Authors:** Miles Hudson
- **ISBN:** 978-1292244478
- **Coverage:** IAL Units 4 & 5 (Unit 6 is the practical unit, no SB)
- **File:** **PENDING**
- **Pages:** —
- **Bytes:** —
- **sha256:** —
- **Quality:** NOT SOURCED this wave — taleem360 bot-walled (reCAPTCHA), scribd login-gated
- **Provenance:** candidates: taleem360.com/edexcel-international-a-level-physics-book-2-vyu; pdfcoffee.com/edexcel-ial-physics-book-2-pdf-free.html (32MB); scribd.com/document/890242837

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
