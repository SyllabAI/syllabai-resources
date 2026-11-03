# Adoption law proposal — run-012 reconciliation wave (T-OEQ-PHYS-FORMAT-1)

Status: DRAFT for sign-off. No corpus or plane content was edited in run-012; this
document proposes the rules under which the 105 adoptable fields get adopted.

Precedents this law generalizes: R2-a table morph verdict (run-009-r2 / #280),
run-010-m2 (#282, corpus := serving KaTeX verbatim), run-011-m3 (#285, corpus :=
live aria-label verbatim), and the DISC-1 discovery recorded in the run-011 ledger.

## L1 — Direction of adoption

**corpus := plane verbatim.** The serving plane (`syllabai-v2`, `questions.json`)
is what students see; the corpus (`syllabai-resources`, `topic.json`) is the record.
For the glue-spacing and format-family buckets the plane carries the repaired,
target form — the record follows the served truth. Verbatim means byte-exact
substring replacement inside the pinned field; no paraphrase, no reflow, no
"improvements" beyond the adopting field's own diff.

## L2 — Content-identity gate (the DISC-1 law)

Before adopting plane content into corpus field (part, field), the pair must be
proven to be **the same question**. Accepted proofs, in order of strength:

1. **Normalized hunk census** (automatic): every differing hunk belongs to a
   known repair family (glue-spacing, m1-code-span, math-env, prescript,
   text-unwrap, leftright, unit-style, bold-markers, invisible-marks, layout).
2. **Cross-id counterpart confirmation** (automatic): the "other" content
   provably lives under a counterpart id in the same topic.
3. **Eyeball sign-off** (manual): side-by-side dump recorded in the run dossier.

If no proof form passes, the field quarantines to the cross-id queue — never
adopted blind. (Failure mode of record: DISC-1, plane stored a different question
under `ZTrm3d8Qwgth5z94`.)

## L3 — Benign-style bucket: closed

715 fields are the same content in different encodings (pinned raw-URLs vs
relative asset paths, layout whitespace, invisible LRM marks, table-separator
spacing). **No content edits on either side.** The URL pinning is a serving-layer
concern; the corpus of record keeps relative asset paths.

## L4 — Cross-id bucket: mapping-repair, not field adoption

22 fields / 20 parts where content matches a *different* part id on the other
side, all within the same topic. Two confirmed mechanisms:

- **Boilerplate reuse** (e.g. `PnYK8tkCjzCjtwG3` is the corpus home of a generic
  MCQ solution shared by 4 plane parts): document, no-op.
- **True mapping drift** (`ZTrm3d8Qwgth5z94 ↔ CZmG2HZmcGRntGDF` — the DISC-1
  case; `Vn36YRgjsBNv8BK2 ↔ hV5TvZxVQMwbwTf2` both fields): repair in a dedicated
  wave with per-part mechanism confirmation and explicit sign-off. Never fix by
  field-verbatim adoption.

## L5 — Wave sequence

- **Wave A — glue-spacing**: 62 fields / 61 parts (52 pure space-inserts, 10
  mixed). Smallest per-field blast radius; all ratios ≥ 0.94.
- **Wave B — format families**: 43 fields / 43 parts (m1-code-spans 3,
  math-env ~6, prescripts 6, text-unwrap 4, leftright 34 overlapping, unit style,
  bold-markers). May split further per family if the leftright tag dominates.
- Each wave: surgical edits + field-level pins (before/after sha256) + qmd regen
  rides where the topic carries a regen file + full gate battery + drift-delta
  proof (L6).

## L6 — Drift-delta gate (new)

After each adoption wave, the full re-scan must show `drift_fields` reduced by
exactly the wave's pin count and `drift_parts` reduced accordingly; no unrelated
field may move (deep-diff law, G5 discipline). The re-scan artifact accompanies
the PR.

## L7 — Re-baseline and ledger

This census supersedes the run-010-m2 disclosure (634/850 → 627/842 as of
2026-11-03 main×main; delta -7/-8 attributed to plane-side RN-DEBRIS waves and
corpus-side #280/#282/#285 after that snapshot). `ledger.json` gains a
re-baseline entry; RES-1 (camera-lens) stays owned by wave B's mapping-repair
follow-up; RES-2 (branch-era qmd pins) re-baselines with the first wave that
touches its two topics.
