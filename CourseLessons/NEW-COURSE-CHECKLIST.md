# NEW-COURSE-CHECKLIST — onboarding a new board/qualification/subject

Path pattern: `lessons/<board>/<qualification>/<subject>-<code>/`
(e.g. `pearson-edexcel/international-gcse/chemistry-4ch1` — mirrors the
past-papers corpus grammar so paper linking stays mechanical).

## Phase A — assets (fetch-first; one-shot credentialed URLs, scrub after)

1. Spec of record: PDF + machine spine (sections → sub-sections → spec points).
2. Book of record: PDF (L1) + parse of record (`parsed/*_chunks_v3.jsonl`)
   with census. No parse yet → run the OCR runbook first (books doctrine).
3. Past papers + mark schemes: confirm coverage in the past-papers index
   (board/qual/subject path must resolve).
4. Question bank: confirm spec-coded coverage density per spec point.

## Phase B — config

5. Write `course.yaml`: qual, board, course_slug (hub), spec_of_record,
   book/parse of record (paths + sha256 pins), spine (chapter list with
   `chem_only`/route flags + join-set sizes), block_allowlist, lint_pack,
   doctrine_refs. Copy the shape from chemistry-4ch1.
6. Seed `findings.jsonl` (empty) + `qa/` + `lessons/` dirs.
7. Register the course in the root `tracker.yaml` + `TRACKER.md`.

## Phase C — pilot loop

8. Scaffold ONE lesson (usually the first chapter), run it S0→S4 end to end
   with full receipts. This calibrates prompts + lint for the subject.
9. Add the subject banned-phrase list (`scripts/lint_rules/<subject>.yaml`).
10. Retro, adjust, then batch the remaining chapters in unit-sized phases.

## Phase D — platform join-up

11. lessonPackV1 JSON emit lands via PR in syllabai-v2 (contracts law).
12. Renderer route + shelf entry verified against the hub.
13. Cross-link bridges confirmed (notes/flashcards/exam-questions joins).
