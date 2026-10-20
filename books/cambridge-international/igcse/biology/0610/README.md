# Cambridge IGCSE Biology (0610) — Student Book Intake (2026-10-21)

**Status:** SOURCE (wave-2 intake, T-MIG-141) — parse lane NOT started.
Scaffold per `books/README.md` §5 (copy of `physics/4ph1/`).

## Books of this lane

### Cambridge IGCSE Biology Coursebook (3rd edition)

- **Title:** Cambridge IGCSE Biology Coursebook (3rd edition)
- **Authors:** Mary Jones, Geoff Jones
- **ISBN:** 9781107614796 (3rd ed)
- **Coverage:** Full IGCSE Biology syllabus (0610)
- **File:** `source/student-book.pdf`
- **Pages:** 350
- **Bytes:** 34,793,363
- **sha256:** `bf255b643448b209230a1b61e10af74dbbb5c4396a80a3480b15641beffdd0c9`
- **Quality:** Image-only scan (multi-image pages, zero text layer) -> OCR route required. UPGRADE CANDIDATE: 4th edition (ISBN 9781108744814, 2021) when a clean full copy is sourced; papacambridge's 3rd-ed upload is a 67-page preview, scribd is login-gated
- **Provenance:** https://turingsebook.com/sites/default/files/ebooks/Cambridge%20IGCSE%20Biology.pdf

## Course binding (planned)

v2 hub course cie-igcse-biology-23 · specKey cambridge-international/igcse/biology/0610

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
