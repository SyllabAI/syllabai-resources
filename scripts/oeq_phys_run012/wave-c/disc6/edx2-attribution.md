# run-012 DISC-6 — the EDX-2 stack attribution + the census-guard hand-off (T-OEQ-PHYS-FORMAT-1)

Date: 2026-11-03. Closes the DISC-6 discovery filed by the wave-C dossier:
the platform-lane follow-up "which sub-step of the T-CONSUME-EDX-2 post-build
stack collapsed the per-part md fields, and a standing guard so no future bank
rebuild can ship the same corruption silently."

Verdicts in one line each:

- **Attributed step: the clean-segment grafts, v1 pass** (the 23a residual
  chain's third stage: dictionary patch → fix_tail → **clean-segment grafts
  321 (v1) + 36 (v2 gate-exact pairing)** → 0).
- **Mis-pairing mechanism: the v1 graft's clean-source pool was keyed per
  QUESTION (and field kind), not per part** — last write wins — so every
  residual target field received its own question's LAST part's content.
- **Intro commit: v2 `c2388bca` (T-CONSUME-EDX-2 run-001, 2026-10-21) for every
  confirmed corruption group**, including three banks outside igcse-physics-19
  that the wave-C census did not scan.
- **Standing guard delivered: `apps/hub/scripts/import_corpus/census_guard.py`
  + `CENSUS-GUARD.md` (v2)** — mandatory exit-0 gate before any future bank
  rebuild ships; baseline receipt committed alongside.

## 1. The attributed step, by elimination and by fit

The EDX-2 run's post-build stack, as of record in the run receipt
(`v2 .syllabai/receipts/T-CONSUME-EDX-2/run-001-edexcel-bundle-refresh.json`,
verification block) and the executor's worklog block (worklog @ `c2388bca`,
line ~10996):

```
math dictionaries 1020/1020 refetched 0-failed
-> patch_corpus_math (21,592 seen / 22,104 fixed)   <- span-internal replacements
-> fix_tail (6 files)                               <- tail fixes, 6 files
-> clean-segment grafts (321 v1 + 36 v2 gate-exact)  <- WHOLE-FIELD writes from a pairing table
-> 23c relink 16 -> 0                               <- link graph only
-> 23d 12-lane gap annotations                      <- manifests only
-> registry restored byte-exact                     <- courses.json only
```

Only one step writes wholesale md content from a pairing table: the
clean-segment grafts. The span patch rewrites spans INSIDE existing fields and
never moves content across fields; fix_tail touched 6 files; 23c/23d/registry
do not write question md. The receipt itself splits the graft pass into a
non-gate-exact variant and a corrective one — **"321 (v1) + 36 (v2 gate-exact
pairing)"** — the v2 pass exists precisely because v1's parallel-tree pairing
was not field-exact.

EDX-1 counterfactual: the same stack's graft stage at EDX-1 was a handful of
**"path-aligned"** grafts (33 isotope fields via the 23b convention + named
families: density `\bcancel`, sin(50)=A/7, vector moduli, |z1/z2|,
lambda_alpha/lambda_e, `\boxed{\times}`, f'' primes — EDX-1 receipt, changes
block) — per-field path pairing, no question-level pool — and the physics bank
was verified clean after EDX-1 (`2ece53bf`) by the wave-C mechanism table.

Implementation note of record: no file matching `graft`/`clean-seg` exists in
any v2 tree (`git ls-tree -r` greps at `c2388bca` and at HEAD are empty), and
the worklog narrates counts only — the v1/v2 graft passes were ad-hoc lane
worktree scripts, never committed. Step-level attribution above is therefore
receipt+worklog+data-based and HIGH confidence; the exact defective source
line is not recoverable. That gap is itself a finding (§6, P1).

## 2. Target selection: the residual defect list, quantified

Hypothesis: the grafts only touched fields that were still failing the 23a
gates after the dictionary patch + fix_tail — i.e. the fields whose pollution
the span machinery could NOT repair (speech text sitting in PROSE rather than
inside code spans/`$..$` segments, and multiline spans the aria whole-match
could not convert). Test at the EDX-2 build pin, resources main@`aa0b4de1`
(the graft's input state), with the 23a gate's own MARK regex quoted verbatim
from `patch_corpus_math_23a.ts` @ `c2388bca`
(`graft-target-pollution-census.json`, this directory):

- **22/22 of the wave-C collapse targets' true (corpus) contents carry
  23a-class pollution at the pin** — 18 prose-form (`mark_raw` only, outside
  any span the dictionary can reach) + 4 multiline-span form.
- The polluted NON-last fields that were NOT collapsed number 139 — and **all
  139 are span-form or multiline-span form (0 prose-only)**: exactly the class
  the dictionary + multiline converter repairs. None of them reached the graft.
- Bank-wide context: 280/2,270 md fields polluted (12.33%); 119 of 978
  last-part fields polluted — a last-part residual target would have been
  grafted with its own pool value (correct-by-accident), which is consistent
  with zero last-part collapses found.
- Per-question pool audit (17 affected questions, same artifact): polluted
  parts are exactly the collapsed set; each question's last part clean at the
  pin.
- Cross-bank confirmation: the corruption holders of §4's three other banks
  are all MARK-polluted at the pin (holder lengths 498/981, 499/976, 784
  chars) while their last parts are clean (126/525, 126/521, 225) — the same
  target-selection law held there.

## 3. The mis-pairing mechanism

Every corrupted field equals its own question's LAST part's content:

- igcse-physics-19 (wave-C census): 18 solution_md + 2 problem+solution
  middle-part pairs, all raw-exact copies of the last sibling; `qstn_K6yxfXjpJXp5sSyG`
  parts 0–3 all carry part 4's solution.
- A pool built by iterating parts and assigning `pool[(question, kind)] = content`
  (last write wins), then applied to every residual (part, kind) target,
  produces exactly this signature — including the "correct-by-accident" case
  for last-part targets and the single-part-question case.
- Source identity (pre-rebuild committed bank vs fresh corpus) is immaterial:
  both carried the same clean per-part content for these fields at the moment
  of the run (bank clean through EDX-1; corpus stable).
- The 36 v2 "gate-exact pairing" grafts re-paired field-exactly and did not
  corrupt (no collapsed field resolves to a non-last sibling).

## 4. Bank-wide sweep: the census-guard baseline (new corruption found)

The delivered guard ran over ALL 106 content banks at v2 main
`fa8059d7e0b1` (2026-11-03): **106 banks / 44,502 questions / 148,978 md
fields, 39 findings in 27 groups** (`disc6-guard-baseline.json` on the v2
side; classification in `guard-baseline-corpus-classification.json` here;
intro-commit walks in `intro-walk.json`).

- **igcse-physics-19: 0 findings** — the wave-C repair holds under the
  bank-wide scan.
- **5 further EDX-2-corrupted fields confirmed across 3 banks** — all
  flip CLEAN/OTHER → COLLAPSED at exactly `c2388bca` in their bank-file
  histories (§4.1), all holders MARK-polluted at the pin (§2), all raw-exact
  (or, for 4.1c, post-patch-pool-exact) copies of their question's last part:

  - a. `igcse-physics-modular-24-unit-2` — `qstn_StT48QqJHnmfWTDr`, part
    `qstnprt_TQjyXfgvNtgD897N` (#1 of 3): problemMd + solutionMd collapse to
    part #2 (`qstnprt_KN2bJvcVTDdGZP2p`); corpus topic
    `radioactivity-particles/properties-of-radiation` (the same 7-1 radiation
    family as the physics-19 ZTrm case).
  - b. `igcse-science-double-award-17-physics` — `qstn_j4MgKD5BjMHMxFzG`,
    part `qstnprt_6z5wkKsZtQZhbvgH` (#1 of 3): problemMd + solutionMd collapse
    to part #2 (`qstnprt_jKF8MTv8DDYvvXMW`); corpus topic
    `radioactivity-and-particles/properties-of-radiation`.
  - c. `ial-maths-20-decision-1` — `qstn_hjMZz7469DDbGmkD`, part
    `qstnprt_GcDFjgD9bRKWkGjC`: problemMd carries a 226-char copy of part
    `qstnprt_YVdMxVrV4VyYp5Rx`'s problem — the pool value here is the
    POST-PATCH last-part text (the pin corpus's raw last-part problem is 225
    chars; the plane copy is its 23a-patched form), i.e. the same collapse
    executed over the patched tree. Corpus holder content (755 chars, distinct)
    is intact of record.

  These 5 fields are the **wave-D candidate**: same L4 repair shape as wave-C
  (plane := corpus of record verbatim, hotlink at the current cut, gates
  T1/G1–G6, guard green pre+post). Operator ruling requested.

### 4.1 Intro-commit walks

For each confirmed group, the bank file's full commit history was walked and
the holder field classified per rev against the corpus of record
(`intro-walk.json`): igcse-physics-modular-24-unit-2 (10 revs), igcse-science-double-award-17-physics
(13 revs), ial-maths-20-decision-1 (6 revs) — **exactly one state transition
each, `OTHER -> COLLAPSED`/`TWIN-COPY` at `c2388bca`, 2026-10-21**. The
intervening waves that touched these banks (EQFC-CONSUME-1 `1f520457`,
RN-DEBRIS-5/6/7/9, selector-2fix `e13bc8b1`) did NOT alter the collapsed
state — the collapse was introduced once, by EDX-2, and never repaired.

### 4.2 Benign and out-of-scope groups

- `cie-as-chemistry-25` `qstn_62k9kSPCBGRt34yy` (2 findings, 1,407-char
  solutions on parts #1/#2): the CORPUS ITSELF carries the identical pair —
  BENIGN-OF-RECORD. (CIE packs were never rebuilt by the EDX lanes; the guard
  flag is the allowlist's first legitimate customer.)
- `ial-maths-20-statistics-2` `qstn_VC4gHySgcd2xYVyf`: the corpus of record
  carries a 23-char identical twin solution pair; the plane twin-copy predates
  EDX-2 (no transition in the file's 6-rev history) and its 222-char text
  drift is the ordinary corpus<->plane field-drift class. Not corruption.
- `igcse-maths-b-16` (20 groups / 31 findings): the past-papers fetch-bank
  plane (T-MIG-136 axis, 22-char id space) has NO SME topic-question corpus
  counterpart by the no_topic_questions ruling — unclassifiable by corpus, and
  EDX-2 never rebuilt that pack (restored byte-exact per the receipt's scope
  guards; the file is owned by the MATHSB/RN-DEBRIS-10 lanes). NOT EDX-2
  class. Owned by the fetch-bank lane: its value-length profile (18 findings
  <= 63 chars — likely attested mark-scheme boilerplate; 13 findings 118–548
  chars — whole-solution copies needing review) is in the classification
  artifact for that lane's own census.

## 5. The standing guard (the deliverable)

- `apps/hub/scripts/import_corpus/census_guard.py` (v2): self-contained
  stdlib scan of every `questions.json` bank (worktree or `--git-rev` mode,
  course filter, JSON receipt, allowlist) detecting any part whose
  problemMd/solutionMd is identical to a sibling part's within the same
  question; `collapse_signature` subclass when the value is the question's
  LAST part's content (the EDX-2 fingerprint). Fail-closed exit 1 on any
  finding not allowlisted. Optional `--serialization-check` surveys the T1
  serialization law per bank (informational: 10/106 banks T1-conformant at
  baseline, including igcse-physics-19; the other 96 are earlier builder-era
  conventions, e.g. maths-b's single-line compact law — unification is
  optional platform work, NOT part of this mandate).
- `apps/hub/scripts/import_corpus/CENSUS-GUARD.md` (v2): the mandate — run
  and land exit-0 BEFORE any rebuilt bank is committed and again AFTER any
  post-build stack, receipt pasted into the run receipt's verification block.
- Baseline receipt: `v2 .syllabai/lane-artifacts/T-OEQ-PHYS-FORMAT-1/disc6-guard-baseline.json`
  (+ the classification artifact on the resources side).

## 6. Process findings (for the platform lane)

- **P1 — ad-hoc stack steps are unauditable.** The v1/v2 graft passes were
  never committed; the receipts narrate counts only. Every post-build stack
  step must live as a committed, re-runnable script with its own receipt, or
  the "documented reproducible path" is not reproducible.
- **P2 — replay hazard.** The EDX-2 receipt documents the stack as "the
  reproducible path" — including the defective v1 graft pass. Any future
  rebuild that replays it verbatim re-introduces the collapse. The path must
  not be replayed until the graft stage is replaced by the gate-exact pairing
  (or dropped in favor of exporter-side repair).
- **P3 — the corruption was gate-invisible.** After the grafts, every 23a gate
  read ZERO: the grafts made the gates green while destroying the id→content
  mapping. Per-field gates cannot see a cross-field class; the census guard is
  the missing gate and should be wired as a hard pre-ship step (R2).
- **P4 — learner impact of the remaining 5 fields.** Two radiation questions
  (modular-24 unit 2; science-double-award physics) serve a wrong part-(b)
  problem+solution, and the ial decision-1 LP question serves a wrong problem
  statement — since 2026-10-21, same as the physics-19 22 were.

## 7. Artifact index

- `graft-target-pollution-census.json` — §2 census (bank @ pin `aa0b4de1`,
  23a MARK quoted from the run-time script, per-target flags, per-question
  pool audit, baseline partition).
- `guard-baseline-corpus-classification.json` — §4 classification of all 39
  baseline findings (27 groups) against the corpus of record.
- `intro-walk.json` — §4.1 per-field commit-history walks.
- v2 side: `apps/hub/scripts/import_corpus/census_guard.py`,
  `apps/hub/scripts/import_corpus/CENSUS-GUARD.md`,
  `.syllabai/receipts/T-CONSUME-EDX-2/DISC-6-handoff.md`,
  `.syllabai/lane-artifacts/T-OEQ-PHYS-FORMAT-1/disc6-guard-baseline.json`.
