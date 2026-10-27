# Receipts & batteries — the operating-culture import (F63)

> Provenance: Task-13 cross-review of the sibling maths-B lane (4MB1, lanes
> T-MIG-136 / 4MB1-QUALITY / MB4-MS-RATTACH / UIUX-*; trace `1a16cfed6208f175`,
> operator order trace `1a16d05526c8019d` "import their receipts/batteries culture
> into your docs"). The maths-B lane's *platform* discipline is genuinely ahead of
> ours — receipts on every claim, leg-structured probe batteries, honest-verdict
> culture — while its *learner-facing* output shipped defect classes our gates
> already refuse (550/2,412 digit-soup parts, 96 lost-answer solutions, 423
> in-part mark-sum mismatches, 1,435 control chars). This file imports what they
> do better, maps each practice onto machinery we already have, and states the
> two things we deliberately do NOT import.

## The eight laws

1. **Receipts: evidence or it didn't happen.** Every run that asserts a state
   (corpus green, canaries hold, export matched) leaves a machine-readable
   artifact: what ran, per-leg exit codes and durations, the head it ran on,
   and an honest pass bit. `run_all.sh` now writes one:
   `receipts/battery-<UTCSTAMP>-<pid>.json` (schema `syllabai.examq-battery-receipt/0.1`).
   Receipts are LOCAL evidence — gitignored, cited from PR descriptions and
   LEDGER entries, never committed as routine noise. Preserve one under a wave
   name only when a wave's evidence must outlive the session.
2. **Batteries: one command, numbered legs, honest summary.** A battery is not
   "some checks passed somewhere"; it is one invocation whose every stage is a
   named leg with its own exit code and seconds, ending in an `N/M PASS` summary
   and a single pass bit. `run_all.sh` is the corpus battery: legs =
   `bootstrap-series-index` → `convert-corpus` → `cross-diff` → `aggregate-report`
   → `canaries`. If a leg fails, the receipt still records every completed leg —
   a battery that dies at leg 3 does not get to claim legs 4-5.
3. **Re-execution, not receipt-trust.** A receipt proves what RAN, not what is
   TRUE. Cross-checks (reviews, landings, disputes) re-run the gates fresh; the
   maths-B lane's own rule, adopted verbatim: "re-executed every gate
   independently (fresh runs, not receipt-trust)". The wave-22 pre-ship
   re-verification (2,607/2,607 re-run, 0 problems) is the house precedent.
4. **Pre-registration and honest verdicts.** BLOCKED is a verdict, not a failure
   to mention (wave-21's "1,332 queued honestly" is the model; the maths-B lane
   records benchmarks as BLOCKED with skip counts rather than soft passes).
   Decisions do not self-ratify: human queues (MCQ keys, crop verdicts,
   no-spec-point) stay human, per the review-queue taxonomy. Incidents and
   self-inflicted defects are disclosed verbatim, not paraphrased away (the
   2020-01 2CR self-contradicting MS, the wave-22 harness dead-code finding).
5. **Census before ship.** A defect class is measured corpus-wide before it is
   declared fixed. The maths-B lane's anti-pattern is the cautionary tale:
   remediation by eyeball lists (~250 parts) against a 550-part defect class.
   House form: the disclosure census (per-wave `{new/gone/changed}` files) and
   G-E1's exact match against it. No wave ships on a sample.
6. **Claims exist once pushed.** Local-only work does not exist for peers (the
   maths-B lane learned this when a dead PAT made a completed task invisible and
   a peer duplicated it). House form: PR-first; ephemeral staging is assumed to
   die with the session (wave-21's withheld drafts did), so anything that must
   survive a session is on main or in a ledger file before the session ends.
7. **Rollback anchors.** Every serving change names the state it replaces. House
   form: the G-E5 data-cut law (F51) pins the exact source cut in the manifest;
   exporter sync PRs name the previous serving manifest; the battery receipt
   records `git_head` it ran on. Reverting is a lookup, not an archaeology.
8. **Gates measure the learner surface.** Marks-exact parse correctness is not
   UX correctness — that is the one-sentence root cause of every defect class in
   the maths-B census. Our import of their failure is already built: char
   hygiene and PUA exclusion (V3), answer-presence and numeric fidelity (V4/V6),
   mark-point coverage (V7), per-part mark-sum law (C13), figure-coverage
   eyeball verdicts (CROP-REVIEW). When a new surface is added, its gate class
   comes with it — never "the parse is right, ship it".

## What we deliberately do NOT import

- **The per-claim yaml task board** (`.syllabai/tasks/*.yaml` + receipts dirs
  per task id). We have LEDGER (findings), CANARIES (regressions), disclosure
  files (serving deltas) and the AGENTS.md open-work list. A second board would
  drift against the first; two sources of "what is open" is how drift starts.
- **Live-prod probe batteries.** This lane has no prod plane of its own; the
  serving plane is the v2 hub, covered by the exporter gates (G-E1..E5) and the
  sync PRs' CI. If a prod-probe need ever appears, it gets its own lane with
  its own credentials discipline — not a borrowed one.

## Battery receipt schema (`syllabai.examq-battery-receipt/0.1`)

```json
{
  "battery": "Official-ExamQuestion run_all battery (ADR-037 corpus)",
  "receipt_schema": "syllabai.examq-battery-receipt/0.1",
  "started_utc": "2026-10-24T09:00:00Z",
  "finished_utc": "2026-10-24T09:41:12Z",
  "git_head": "ac59f031",
  "papers": "1C 2C",
  "series_count": 16,
  "env": {"SKIP_FETCH": "0", "EXAMQ_UPLOAD_DIR": "/home/z/my-project/upload"},
  "legs": [
    {"name": "bootstrap-series-index", "exit": 0, "seconds": 1},
    {"name": "convert-corpus",         "exit": 0, "seconds": 2103},
    {"name": "cross-diff",             "exit": 0, "seconds": 4},
    {"name": "aggregate-report",       "exit": 0, "seconds": 2},
    {"name": "canaries",               "exit": 0, "seconds": 6}
  ],
  "summary": "5/5 PASS",
  "pass": true
}
```

`git_dirty` is recorded as a boolean when the checkout has uncommitted
Official-ExamQuestion changes (a dirty-tree battery pass is advisory, never
citable as the state of main).

## Shape batteries (added 2026-10-27, the deep-audit wave)

The furniture battery (C77/C94) guards the footer/watermark UNIVERSE. The deep-audit wave
added the SHAPE universe as standing battery legs, all convertable to one command each:

1. **Shape sweep** (offline): the battery-v3 walker over all 54 topic.json — furniture
   families, atom-run/bond-fragment drawing garbage, MCQ-candidate shapes, MP fragment
   shapes, mojibake slots, consistency re-checks (MP sums, empty fields). Session receipt
   `da-sweep.json` is the head census; re-run it after any converter emission change.
2. **Gate censuses** (every conversion): G3 drawing-option MCQ candidates (F94), G4
   drawing-linearization gaps (F96), G7 mp_answer_gap (F95) — report-only arms + review-queue
   entries so a shape class can never again pass vacuously.
3. **Canaries**: C96 tick-glyph canonical, C97 bare-answer-solution law, C98 the pinned
   drawing-linearization open census (15). A pinned census moves only with its disclosure in
   the same commit (law 8's fix-and-disclose applied to counts, not just diffs).
4. **The self-check pair** (standing rules 1 + 4): battery + canaries fresh AND one live page
   per affected family read end-to-end as a user sees it. The 2026-06 2C wave verified both.
