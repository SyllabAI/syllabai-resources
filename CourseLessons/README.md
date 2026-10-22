# CourseLessons — the authoring home for SyllabAI Lessons

> **Mission:** for every course we cover, this folder produces **the single best
> learning resource for that course on the internet** — a complete, exam-true,
> self-improving lesson library built on top of the licensed book of record,
> the parse of record, real past papers, mark schemes, and a spec-coded question
> bank. Any agent (or human) must be able to arrive here cold, read
> [`START-HERE.md`](START-HERE.md), and productively continue an existing lesson
> or start a new one.

## What lives here

| Path | Purpose |
|---|---|
| `START-HERE.md` | **Agent entry point.** Reading order, the 10 hard laws, how to resume vs. start. |
| `FEATURE-SPEC.md` | Every feature a Lesson carries (reading core, additive boxes, platform features) + per-lesson Definition of Done. |
| `BUILD-PLAYBOOK.md` | The stage flow S0–S4, gates G1–G4, receipts, and the resume protocol. |
| `VALIDATION.md` | The lint law: what every lesson must pass before review. |
| `SELF-IMPROVEMENT.md` | How agents report mistakes and findings so other agents learn (findings ledger, root-cause-twice law, retros). |
| `NEW-COURSE-CHECKLIST.md` | Onboarding a new board/qualification/subject. |
| `TRACKER.md` + `tracker.yaml` | **The tracking doc of record** — one place that tracks every course, every lesson, every status. `TRACKER.md` is human-readable; `tracker.yaml` is its machine twin (scripts consume this). |
| `prompts/` | Versioned prompt registry. Every receipt records which prompt version produced the content. |
| `scripts/` | The pipeline tooling (`lessonctl.py` CLI + `section_map.py`). Stdlib-only, no deps beyond PyYAML. |
| `lessons/<board>/<qualification>/<subject>-<code>/` | The lessons themselves, organized by **board → qualification → subject**, mirroring the past-papers corpus grammar. |

## The substrate (what a Lesson is built ON — never duplicated)

A Lesson is an interactive HTML rendering of a course, assembled from:

1. **The book of record** (L1 PDF, page-true) and its **parse of record**
   (`parsed/*_chunks_v3.jsonl`) — prose, key points, exam hints, safety,
   figures, glossary seeds. Content lives here, referenced by provenance —
   never copy-pasted into syllabai-v2.
2. **The spec of record** (182 spec points for 4CH1) — every section declares
   which spec points it teaches.
3. **Real past papers + mark schemes** (56 papers for 4CH1, QP *and* MS) —
   the accept/avoid vocabulary layer and the past-paper anchor cards.
4. **The question bank** — spec-coded, difficulty-banded checks.
5. **The platform** (syllabai-v2) — renderer, tutor, flashcards, notes bridge,
   learner model. Contracts: `packages/contracts/src/books-lesson.ts`.

The full pipeline picture (L0–L4, corpus-side vs platform-side) is in
`BUILD-PLAYBOOK.md` §1.

## Status

- **First course:** Pearson Edexcel International GCSE Chemistry (**4CH1**) —
  `lessons/pearson-edexcel/international-gcse/chemistry-4ch1/`.
- Companion doctrine in syllabai-v2: `docs/books/` (BOOKS-START-HERE,
  BOOK-BUILD-PLAYBOOK, BOOK-PACK-SPEC, BOOK-SELF-IMPROVEMENT) and
  `docs/books/LESSON-PLAN-4CH1-v1.md`.
- The interactive book ships as **two renderers over one substrate**: the rail
  (page-true PDF companion — live) and **Lesson** (this folder's output — the
  primary year-round learning surface). The PDF of record is never altered.
