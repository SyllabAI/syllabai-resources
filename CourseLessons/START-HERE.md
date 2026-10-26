# START-HERE — for every agent working on CourseLessons

You are here to build or improve **Lessons**: the best learning resource for a
course on the internet. Read this file top to bottom, then follow the flow.
Total reading time: ~10 minutes. Do not skip the hard laws.

## 0. Reading order

1. This file (entry point, laws, flow).
2. `FEATURE-SPEC.md` — what a complete Lesson carries (your target state).
3. `BUILD-PLAYBOOK.md` — how work flows stage by stage (S0–S4) and how to
   **resume a partially built lesson** or **start one from scratch**.
4. `VALIDATION.md` — the exact checks your output must pass.
5. `SELF-IMPROVEMENT.md` — how to report mistakes/findings (mandatory).
6. Your course folder, e.g.
   `lessons/pearson-edexcel/international-gcse/chemistry-4ch1/` — start with
   `course.yaml`, then `findings.jsonl` (learn from predecessors' mistakes
   BEFORE writing), then `TRACKER.md`.

## 1. The 10 hard laws

1. **Fetch-first.** L1 corpus assets (book PDF, parse of record, past papers,
   mark schemes) are fetched from their repos of record via one-shot
   credentialed inline URLs. Never persist the token: not in files, not in
   remotes, not in logs. Scrub after every use.
2. **Provenance law.** Every prose section carries `chunkRefs` (ids in the
   parse of record) and a `bookPage` anchor. If you write a sentence that is
   not derived from the parse of record or an explicitly allowed authored
   block type, it must not exist — or it must arrive as a finding first.
3. **Spec-subset law.** `specRefs` of any section ⊆ the chapter's join set
   (`book_chapters.specCodes`). Never invent a spec code; never widen.
4. **Derived-links law.** Links to revision notes / flashcards / exam
   questions / past papers are computed by the renderer from spec codes.
   You NEVER author a link by hand. If you believe a mapping is missing,
   file a finding.
5. **MS-language law.** Glossary entries and exam-hint boxes carry
   `ms_accepts` / `ms_avoids` lines taken from real mark schemes. Banned
   phrases (per-subject list in `VALIDATION.md`) fail lint.
6. **Honest-absent law.** A missing mapping renders nothing — no placeholder
   panels, no invented content, no "coming soon" promises.
7. **SUGGESTED law.** Everything you produce lands as `status: draft`. The
   flip to review/published is an explicit operator command, recorded in the
   tracker with a receipt. You never self-publish.
8. **Receipt law.** Every stage you complete leaves `qa/receipt.yaml` in the
   lesson folder: stage, date, agent id, prompt version, lint result,
   trace id. No receipt → the stage never happened.
9. **Findings law.** Every mistake you notice — yours or a predecessor's —
   goes to the course `findings.jsonl` (append-only, schema in
   `SELF-IMPROVEMENT.md`). A finding that recurs twice forces a system change
   (prompt edit, lint rule, or spec fix), not a third silent fix.
10. **Tracker law.** No status change without a `tracker` transaction (see
    `scripts/`). The tracker is the single source of truth for "what exists
    and what state it is in". If it is not in the tracker, it does not exist.
    The transaction includes the **phase rollup**: when a flip publishes the
    last unpublished pack of a phase, the SAME commit flips
    `phases.<unit>.status` to `complete` in `tracker.yaml` AND closes the
    phase row (headline + tail) in `TRACKER.md`. Close every flip/tx with
    `python3 scripts/tracker_check.py` — a non-zero exit means the tracker is
    drifting; fix it in the same commit before pushing (V10, f-0035).

## 2. Your first 5 commands

```bash
cd CourseLessons
python3 scripts/lessonctl.py report --course chemistry-4ch1   # what exists, what state
python3 scripts/lessonctl.py resume lessons/pearson-edexcel/international-gcse/chemistry-4ch1/lessons/u1-c01-states-of-matter
# ^ prints a WORK-ORDER: exactly what to do next for a partially built lesson
python3 scripts/lessonctl.py scaffold --course chemistry-4ch1 --chapter u1:c02
# ^ start-from-scratch: emits the lesson skeleton (sections, boxes, glossary seeds)
python3 scripts/lessonctl.py lint lessons/pearson-edexcel/international-gcse/chemistry-4ch1/lessons/u1-c01-states-of-matter
```

## 3. Resume vs. start-from-scratch (the golden rule)

- **Resume wins.** Before starting anything, run `report` + `resume`. A
  partially built lesson is continued, never restarted over. `lesson.yaml`
  records `stage`, `section_spine`, and per-section completion; the work
  order tells you the next smallest useful unit of work (usually one section
  or one box set).
- **Start from scratch only if** the tracker shows no lesson folder for the
  chapter. Then `scaffold`, fill sections one at a time, lint after each.

## 4. Writing quality bar (non-negotiable)

- Clarity first: short sentences, define every technical term at first use,
  one idea per paragraph.
- Every section: prose (from provenance) + at least one additive box (see
  `FEATURE-SPEC.md` §2) + a knowledge check.
- Examiner-true: command words, mark allocations, and accept/avoid phrasing
  come from mark schemes, not memory. If unsure, write the content and flag
  `qa-note: ms-verify` in the section front-matter.
- No fluff, no "In this section we will...", no artificial endings.

## 5. When you finish a unit of work

1. `lint` until clean.
2. Write `qa/receipt.yaml` (stage S1–S4 per `BUILD-PLAYBOOK.md`).
3. Append any findings to `findings.jsonl`.
4. `tracker` transaction to record progress — including the phase rollup
   (law 10) — and run `python3 scripts/tracker_check.py` until it exits 0.
5. Hand back with a one-paragraph summary: what changed, what lint says,
   what the next agent should pick up.
