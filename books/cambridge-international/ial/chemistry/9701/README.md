# Cambridge International AS & A Level Chemistry (9701) — Student Book Intake (2026-10-21)

**Status:** SOURCE (wave-2 intake, T-MIG-141) — parse lane NOT started.
Scaffold per `books/README.md` §5 (copy of `physics/4ph1/`).

## Books of this lane

### Cambridge International AS & A Level Chemistry Coursebook (3rd edition)

- **Title:** Cambridge International AS & A Level Chemistry Coursebook (3rd edition)
- **Authors:** Lawrie Ryan, Roger Norris
- **ISBN:** 9781108859037 (family)
- **Coverage:** Full A Level (AS + A2) in one volume, syllabus for examination from 2022
- **File:** `source/student-book.pdf`
- **Pages:** 889
- **Bytes:** 38,227,604
- **sha256:** `1fa8afa3b3a3dc7dd4b981041e7bd9e2019c19095a0f59d75858e5c12c3e4928`
- **Quality:** Native text layer, clean on sampled pages; DISCLOSED DEFECT: 2 of 889 pages carry a third-party advertising watermark (WeChat CLASS0608 overlay, p31 + 1 more) — parse lane must quarantine/strip those pages' overlay text
- **Provenance:** https://www.exampaperspractice.co.uk/wp-content/uploads/CambridgeInternationalASALevelChemistryCoursebook.pdf

## Course binding (planned)

v2 hub course cie-a-level-chemistry-25 · specKey cambridge-international/ial/chemistry/9701 (pastpapers-corpus.ts grammar)

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
