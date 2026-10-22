# FEATURE-SPEC — what a Lesson carries

Target state for every lesson. The per-lesson Definition of Done is §5.
Features marked **[P2+]** are post-pilot: document intent, do not build yet.

## 1. Lesson anatomy (top of every lesson page)

| # | Feature | Source |
|---|---|---|
| 1 | **Learning objectives** — verbatim spec wording for the chapter's join set | `book_chapters.learning_objective` + specCodes |
| 2 | **Spec-point map** — which spec points this lesson teaches; Paper-1/Paper-2 route badges | spec join + `paper_route` |
| 3 | **Prior knowledge box** — what the learner must already know, with drill-in links to the exact earlier lesson/section | authored (allowed block: `prior-knowledge`), verified against spine order |
| 4 | **Cross-curricular links box** — Maths (e.g. ratios, standard form), Physics, Biology, Economics/industry, History of science | authored (`cross-curricular`), must name the concrete skill/topic, never vague |
| 5 | **Lesson TOC** — section list with progress rings | renderer |
| 6 | **"Where this appears in the exam"** — paper breakdown for the chapter's spec points (e.g. "1C JUN23 Q4(b), 2 marks") | past-paper anchor index |

## 2. Section anatomy (the repeating unit — ~17 sections per chapter)

Prose from the parse of record (`chunkRefs` provenance + `bookPage` anchor),
plus additive boxes, plus interactivity:

| # | Feature | Source / rule |
|---|---|---|
| 1 | **Prose body** — page-true reading text | parse of record; OCR lint law |
| 2 | **`:::key-point`** strips | census `key_point` chunks (140 available, 4CH1) |
| 3 | **`:::exam-hint`** with MS accept/avoid lines | census `exam_hint` chunks (113) + mark schemes |
| 4 | **`:::misconception`** — the wrong idea, why it's wrong, the right phrasing | authored; examiner-true |
| 5 | **`:::safety`** / practical boxes | census `safety` chunks (44) + `practicals.yaml` |
| 6 | **`:::did-you-know`** engagement cards | census `did_you_know` chunks (17) |
| 7 | **`:::maths-skills`** — the quantitative skill in this section, worked in exam style | authored (chem: sig figs, ratios, unit conversions) |
| 8 | **Glossary chips** inline — hover card: definition + `ms_accepts`/`ms_avoids` + "hear it" [P2+ TTS] | `glossary.yaml` per lesson |
| 9 | **Figures page-true** — bbox-anchored to the PDF of record | figure sidecar at ingest |
| 10 | **Interactive blocks** interleaved by page: MCQ, sort-match, table-fill, eq-builder, drag-label, num-stepper, sim-embed (PhET) | VALIDATED blocks (`book_blocks`) — reused, not rewritten |
| 11 | **Worked example** — stepwise, with the mark-scheme mark lines shown as an examiner would award them | `num-stepper` blocks + MS corpus |
| 12 | **Quick check** — 2–5 bank questions filtered by the section's specRefs | question bank (derived) |
| 13 | **Section summary** — "In one page" recall card | authored ≤120 words |
| 14 | **"Can you…?"** self-assessment checklist — each item keyed to a spec point | authored |
| 15 | **Page anchor** — "see p.42 in the student book" → PDF slice drill-in | bookPage |

## 3. Lesson-closing layer

| # | Feature | Source |
|---|---|---|
| 1 | **Timed chapter check** (live on the platform) | bank via specCodes |
| 2 | **Past-paper anchor cards** — spec point → real paper questions with QP + MS links | pastpapers corpus |
| 3 | **Flashcard deck** for the lesson, decay-aware due badge | flashcard bridge (ADR-031) |
| 4 | **Revision-notes panel** — exact spineCode join, honest-absent when 0 | `books-notes.ts` |
| 5 | **TutorCard** — AI tutor anchored to this lesson's spec codes, page-true citations | tutor book-arm |
| 6 | **Unit/Strength checks** — end-of-unit synthesis | `strength-u*` packs |

## 4. Platform features (the reader; renderer-owned)

| # | Feature | Notes |
|---|---|---|
| 1 | **Highlighting** — multi-colour, per-user, persisted; select text → highlight/note/flashcard [P2+ for flashcard-from-highlight] | local-first, syncs when signed in |
| 2 | **Saved notes** — per section, linked to highlights; exportable | same store as progress |
| 3 | **Glossary search** across the course | from lesson `glossary.yaml` union |
| 4 | **In-course search** — sections, boxes, glossary | tsvector (already in DB for chunks) |
| 5 | **Progress + resume** — per-section completion, "continue where you left off" | `chapter_progress` law |
| 6 | **Spaced review ("look back")** — interleaved retrieval quiz from earlier lessons, decay-driven | learner model |
| 7 | **Read-aloud (TTS)** [P2+] and translation-ready i18n [P2+] | `speech-math` groundwork |
| 8 | **Bookmarks/favourites**, dark mode, WCAG AA, mobile-first | reader baseline |
| 9 | **One-page revision sheet** — auto-generated printable PDF per lesson | renderer export [P2+] |
| 10 | **Paper-route awareness** — Paper-2-only content badged everywhere it appears | spine `chem_only` flags |

## 5. Per-lesson Definition of Done (lint-enforced where possible)

- [ ] `lesson.yaml` complete: spine, statuses, receipts, feature checklist.
- [ ] Every section: provenance (`chunkRefs` + `bookPage`) + ≥1 additive box + a quick check.
- [ ] Boxes coverage: ≥1 `misconception` and ≥1 `exam-hint` per section; `prior-knowledge` on the lesson's first section; `cross-curricular` ≥1 per lesson.
- [ ] Glossary: every technical term at first use is a chip; entries carry `ms_accepts`/`ms_avoids`.
- [ ] specRefs subset law + page-anchor monotonicity hold.
- [ ] Lint clean (`scripts/lessonctl.py lint`), receipt written, tracker updated.
- [ ] Honest-absent audit: any missing mapping omitted, not faked.

## 6. Feature additions — how to propose

New feature → `findings.jsonl` entry `type: feature-gap` with evidence
(learner need, comparable-platform precedent, cost). The operator accepts →
FEATURE-SPEC updated in the same PR → only then build. Self-improvement flow:
see `SELF-IMPROVEMENT.md`.
