# VALIDATION — the lint law for Lessons

Every lesson passes `python3 scripts/lessonctl.py lint <lesson-dir>` before
review. The linter is the contract; this doc explains each rule and how to fix.

## 1. Rule families

**V1 Schema (`lesson.yaml`)**
- Required keys present (`lesson_id`, `chapter_key`, `course_id`, `title`,
  `stage`, `sections[]`, `features{}`); section ids match the
  `u<unit>:c<NN>:s<NN>` grammar; `bookPage` monotonic within the lesson;
  `specRefs` non-empty per section.

**V2 Provenance**
- Every section front-matter carries `chunkRefs` (≥1) resolving to the parse
  of record and a `bookPage` in the chapter's page range. Authored-only
  sections (summary/checklist) are exempt but must declare
  `authored: true`.

**V3 Spec-subset**
- `specRefs ⊆ chapter join set` (from `course.yaml` spine join / platform
  registry). A code that is not in the join set fails — file a finding if you
  believe the join set itself is wrong.

**V4 Language / banned phrases (per-subject)**
- Chemistry pilot list: "free electrons" (say *delocalised electrons*),
  unqualified "sea of electrons", "the rate of the forward reaction increased
  so the equilibrium shifted" (mechanism-speak banned at IGCSE),
  imprecise "salt melting/boiling" phrasing; OCR artifacts: `(l)` for `(I)`,
  lost subscripts (`Ar` vs `Aᵣ`), mojibake. The list lives in
  `scripts/lint_rules/chem.yaml` and only grows via findings.

**V5 Box coverage (FEATURE-SPEC DoD §5)**
- ≥1 `exam-hint` and ≥1 `misconception` per section; `prior-knowledge` on the
  first section; ≥1 `cross-curricular` per lesson; summary + "Can you…?"
  checklist present at lesson close.

**V6 Glossary**
- Every `[[term]]` chip resolves to `glossary.yaml`; every glossary entry has
  definition ≤40 words + ≥1 `ms_accepts`; `ms_avoids` encouraged.

**V7 Checks**
- Quick-check question ids resolve in the question bank (or are flagged
  `pending-bank` with a finding); no authored question text duplicates
  book-question text (licensing law: book questions = page jumps only).

**V8 Honest-absent**
- No TODO placeholders in published-facing text; no fabricated links; a
  section with no work must not exist as an empty file (scaffold marks
  sections `stage: S0` explicitly instead).

**V9 Receipts + tracker**
- `qa/receipt.yaml` present for every claimed stage; tracker state matches
  `lesson.yaml` (mismatch fails lint).

**V10 Tracker rollup (`scripts/tracker_check.py`)**
- The tracker's rollup layers agree with pack ground truth:
  (a) `phases.<unit>.status` equals the rollup of member `pack_status`
  (all published ⇒ `complete`; `complete` ⇒ all published);
  (b) every `pack_status` equals the `status` in the pack's
  `qa/lessonPackV1.json`;
  (c) `TRACKER.md` phase-row headlines (no `**open`, no stale
  `LANES n/m`) and per-lesson `pack PUBLISHED/DRAFT` cells agree with
  `tracker.yaml`.
- Run `python3 scripts/tracker_check.py` as the closing gate of every
  flip/tracker transaction — exit code = number of errors, must be 0 before
  push. Born from finding `f-0035` (three occurrences of phase-row drift:
  c25, c27-repair, c29).

## 2. Severity model

- `error` — blocks handoff (V1–V3, V8, V9, V10).
- `warn` — blocks S4, allowed at S1/S2 (V4 first-offence new phrase, V5 gaps,
  V6 missing `ms_avoids`).
- `info` — advisory (style, long paragraphs >120 words, passive-voice runs).

Exit code = number of errors. Warnings are listed in the receipt.

## 3. Extending the rules

A lint rule change is a normal PR + a findings entry explaining the failure it
catches (root-cause-twice law). Removing a banned phrase requires evidence in
the finding that the ban was wrong.
