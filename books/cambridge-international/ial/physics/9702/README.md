# Cambridge International AS & A Level Physics (9702) — Student Book Intake (2026-10-21)

**Status:** SOURCE (wave-2 intake, T-MIG-141) — parse lane NOT started.
Scaffold per `books/README.md` §5 (copy of `physics/4ph1/`).

## Books of this lane

### Cambridge International AS and A Level Physics Coursebook (2nd edition)

- **Title:** Cambridge International AS and A Level Physics Coursebook (2nd edition)
- **Authors:** David Sang, Graham Jones, Gurinder Chadha, Richard Woodside
- **ISBN:** 9781107697690 (2nd ed family)
- **Coverage:** Full A Level in one volume (2nd ed targets the 2016 syllabus line)
- **File:** `source/student-book.pdf`
- **Pages:** 744
- **Bytes:** 28,365,057
- **sha256:** `fa3e5ed25da0c3c1217959d50144e8e7291d09851ad8298bda5df2839e097ae6`
- **Quality:** Native text layer, clean on sampled pages. UPGRADE CANDIDATE: 3rd edition (ISBN 9781108859035, 2022 syllabus) is preferred for the 2025 lane when a clean full copy is sourced — dokumen.pub hosts it but is bot-gated; this 2nd ed is the full endorsed book in the meantime
- **Provenance:** https://www.cienotes.com/wp-content/uploads/2018/07/Cambridge-International-AS-and-A-Level-Physics-Coursebook-by-David-Sang-Graham-Jones-Gurinder-Chadha-and-Richard-Woodside.pdf

## Course binding (planned)

v2 hub course cie-a-level-physics-25 · specKey cambridge-international/ial/physics/9702

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
