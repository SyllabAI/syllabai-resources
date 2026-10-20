# Cambridge International AS & A Level Biology (9700) — Student Book Intake (2026-10-21)

**Status:** SOURCE (wave-2 intake, T-MIG-141) — parse lane NOT started.
Scaffold per `books/README.md` §5 (copy of `physics/4ph1/`).

## Books of this lane

### Cambridge International AS and A Level Biology Coursebook (4th edition)

- **Title:** Cambridge International AS and A Level Biology Coursebook (4th edition)
- **Authors:** Mary Jones, Richard Fosbery, Jennifer Gregory, Dennis Taylor
- **ISBN:** 9781107636828 (4th ed family)
- **Coverage:** Full A Level in one volume (4th ed, 2014 printing)
- **File:** `source/student-book.pdf`
- **Pages:** 696
- **Bytes:** 51,263,078
- **sha256:** `fa4954c88855a587a63deeb2725f6abb22aed8b3551ed02462dfbf53c036bfe7`
- **Quality:** Native text layer, clean on sampled pages. UPGRADE CANDIDATE: 5th edition (ISBN 9781108859028) for the 2025 lane when a clean full copy is sourced
- **Provenance:** https://ebooks.papacambridge.com/directories/CAIE/CAIE-ebooks/upload/cambridge%20international%20as%20and%20a%20level%20biology%20coursebook.pdf

## Course binding (planned)

v2 hub course cie-a-level-biology-25 · specKey cambridge-international/ial/biology/9700

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
