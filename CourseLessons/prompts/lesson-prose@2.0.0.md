# lesson-prose@2.0.0 — the STANDALONE-VOICE law

> Operator directive of record (trace 1a168b88e0391dfd): *"I don't want 'The
> book said...'. The lesson is going to 100% book replacement. Students can
> achieve top grades reading and studying from lesson."*
>
> The Lesson IS the textbook. Everything below serves that contract.

## The six rules

1. **Teach, never attribute.** State the chemistry in the lesson's own
   authoritative second-person voice. Banned in student prose: "the book
   says/opens/notes/hints/warns/lands/prints", "the book's KEY POINT / HINT /
   REMINDER / Figure 7.x / Table 7.y / Example 2", "the printed heading",
   "the parse of record", "chunk 0307".
2. **Zero QA leakage.** Provenance lives in the QA layer and ONLY there:
   front-matter `chunkRefs` (per-section), `qa/receipt.yaml` (ocr_notes,
   boxes mapping, spillover notes), `lesson.yaml notes`. Student prose never
   carries chunk ids, receipt talk, OCR-repair disclosure parentheticals,
   print-heading provenance, or section-map commentary.
3. **Zero PDF-deflection.** No "open the student book PDF", no narration of
   the print question bank ("Book p. 83 questions 1–2 → page jump only").
   Practice joins the PLATFORM question bank by specRefs (derived-links law).
   The reader's page-anchor UI is metadata, not prose content.
4. **The substance is unchanged.** The law changes the VOICE, never the
   chemistry: every fact, worked example, table, extension idea and census
   box the book carries, the lesson carries — restated as direct instruction.
   Worked examples are introduced as problems to solve ("Worked example:
   find the formula for barium nitrate"), not as things the book does.
5. **Exam-hints speak as the platform.** Exam technique is SyllabAI's own
   coaching voice ("In the exam, ...", "The mark scheme wants...").
   Quoting a mark-scheme expectation is fine; attributing it to the print
   book is not.
6. **Diagrams are described, not cited.** Where the print book carries a
   figure the lesson cannot embed, teach the content in words or with a
   plain described sketch ("a lattice fence is the everyday picture of a
   regular repeating array") — no figure numbers, no dangling citations.

## Layer map (what goes where)

| Layer | Carries | Never carries |
|---|---|---|
| sections/*.md body | teaching prose, boxes, chips, GFM tables | attribution voice, chunk ids, QA talk, PDF pushes |
| sections/*.md front-matter | id/title/bookPage/chunkRefs/specRefs/blocks/glossary | — |
| qa/receipt.yaml | ocr_notes, title_refinements, re-homings, boxes→chunks mapping, spillover provenance | — |
| lesson.yaml notes | authoring notes, census facts | — |

## Lint note

V4 banned-phrase growth ("the book", "book's", "student book", "licensing
law" in section bodies) is QUEUED as a lessonctl tooling lane with its own
receipt (VALIDATION.md §3) — not silently added. Until it lands, this prompt
file is the law of record and every retrofit/review enforces it by hand.
