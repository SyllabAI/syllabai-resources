# Cambridge IGCSE Physics (0625) — Student Book Intake (2026-10-21)

**Status:** PARSED (v1 corpus, W-F9 2026-11-20 — trace 1a1f4951330253b5; validator ALL CHECKS PASSED; LLM polish NOT STARTED, quota-walled).
Scaffold per `books/README.md` §5 (copy of `physics/4ph1/`).

## Books of this lane

### Cambridge IGCSE Physics (3rd edition, Hodder) — Tom Duncan & Heather Kennett

- **Title:** Cambridge IGCSE Physics (3rd edition, Hodder) — Tom Duncan & Heather Kennett
- **Authors:** Tom Duncan, Heather Kennett (Hodder Education; Cambridge-endorsed)
- **ISBN:** 9781444176421 (Hodder 3rd ed)
- **Coverage:** Full IGCSE Physics syllabus (0625)
- **File:** `source/student-book.pdf`
- **Pages:** 328
- **Bytes:** 13,646,813
- **sha256:** `32a3771a26b2c47b9eaffb747dbb5c2f0faeb67d5e0daf77e5fb11255d13551b`
- **Quality:** Native text layer, clean on sampled pages. NOTE: this is the Hodder endorsed book, not the CUP Sang Coursebook named in the catalog plan — full and clean was the pick; CUP Sang 3rd ed (ISBN 9781108744593) stays an upgrade candidate. papacambridge's 'CUP 3rd ed' uploads turned out to be 67-69-page PREVIEWS (public-20% files), not full books
- **Provenance:** https://ebooks.papacambridge.com/directories/CAIE/CAIE-ebooks/upload/cambridge%20igcse%20physics%20(3rd%20edition)%20by%20tom%20duncan%20and%20heather%20kennett.pdf

## Course binding (planned)

v2 hub course cie-igcse-physics-23 · specKey cambridge-international/igcse/physics/0625

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

## Parse of record (W-F9, 2026-11-20 — trace 1a1f4951330253b5)

**Status: PARSED (v1).** Corpus `parsed/cie_igcse_physics_0625_chunks_v1.jsonl` — **896
chunks** (`c0625_v1_u{unit}_c{n}_pdf{p}_{i}`), 13-key v1 grammar. Text-layer lane, no
OCR: PyMuPDF span-pool assembly, **fixed-gutter x=307** column law (the PDFium render has
an irregular two-band grid — text right band, figures/margins left; per-page gap votes
are unreliable; 258/328 pages two-column). Page law `book = pdf - 13` (verified 5 ways).
**Unit law:** the 5 printed section dividers become units (unit_no/unit_name on chapter
chunks). 50 chapters; opener phase law (head → at-a-glance box → body; box bullet glyphs
render as 'l' or single '●'); '●● Worked example(s)' → worked_example, '●● Practical …'
→ practical; back banks forced types (revision/exam/practical-test/alt-practical banks +
Answers + Index). Checklists anchored 50/50; openers 50/50. **DAMAGE CLASS D-2 of
record:** fi/fl ligature loss in the render ('Specifi c', 'classifi cation', ' elds'; 488
glue occurrences) — NOT repaired in v1 body text (transcription-only polish pending,
quota-walled). In-chapter revision-question sets print no heading — typed body honestly
(routed limitation; the banks carry the serving anchors). Validator
`pipeline/scripts/validate_0625.py` **ALL CHECKS PASSED** (2026-11-20); determinism
sha256 byte-identical re-run. See `parsed/parse_report_v1.json` (decisions D-1…D-7).
