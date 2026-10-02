# T-C42 R11+R12 — Join Re-Run + Substrate Re-Build over the C42-R10-Amended Resolution

| | |
|---|---|
| **Task ID** | T-C42 R11 (join lane re-run) + R12 (substrate lane re-build) — the operator directive's "then R7/R8/R9 again" |
| **Date** | 2026-10-03 |
| **Baseline** | `a26f3aa` (the R10 verdict-round commit) |
| **Kind** | agent-deterministic re-runs; every gate fail-closed; zero promotion (the substrate stays `SUGGESTED`; the C41-promoted 73 HUMAN_VALIDATED edges byte-untouched) |
| **Verification** | `scripts/c42_r11_r12_join_substrate_check.py` → `graph/reports/C42_R11_R12_CHECK.json` (W1–W7 ALL PASS, exit 0; deterministic re-run byte-stable) |

## R11 — join re-run

`scripts/c32_notes_maths_a_join.py` under a dated **T-C42 R11 amendment** (P5: the
generator is re-pinned, landed records never edited):
`Official-Specifications/parsed/_derived/notes-join/igcse-maths-a-18-higher.json`
refreshed = **198 joined / 5 unresolved / 203 anchors / 0 foreign codes — census
UNCHANGED** (the R10 round corrected 2 codes and cleared 0 anchors); **120/188
distinct codes** (2.2A already covered via substitution.json; 1.8D keeps its
anchor — the R10 STANDING adjudication); anchors by tier 82 Foundation / 116
Higher (the 2 re-points moved both anchors to Higher-store codes); wording census
**EXACT 173 / LEDGER_EXPLAINABLE 25** (unchanged — both re-pointed rows were
EXACT before and after); the exact unresolved id set pinned (the C31 §3 residual
+ the 2 R1-cleared + the 2 R6-cleared anchors, fail-closed); **NEW at R11: the
generator itself pins the exact codes the two re-pointed joins must carry**
(`expanding-triple-brackets` → 4MA1-2.2A, `algebraic-fractions` → 4MA1-2.2C,
`related-calculations` → 4MA1-1.8D STANDING) — any drift fails closed; the
unresolved anchors keep their PROPOSAL-ONLY candidates that bind nothing.

## R12 — substrate re-build

`scripts/c40_maths_a_chunk_sp_substrate.py@2.2.0` under a dated **T-C42 R12
amendment**: G2 re-pinned to the unchanged 198+5 exact id set; **the THREE
operator override maps consumed FAIL-CLOSED** — the R1 map (16 entries), the R6
map (7 entries incl. the 2-key subsumption registry) **and the R10 map (8
verdicted entries: 7 REATTRIBUTE + 1 DEMOTE_TO_WORKLIST — the loop's first
DEMOTE)**; the R10 map's **note-level STANDING pin verified in-generator**
(related-calculations must still join 1.8D on `spcpt_crKbmb6wVjM4yPJh`);
coverage + worklist recomputed; chunker and `c40-chunk-convention-1` untouched.
Result: `graph/igcse-maths-a/spec_chunk_mappings.yaml` regenerated = **923 rows
= 841 anchored + 21 unresolved-span worklist (incl. the DEMOTE row, chunk
identity intact) + 61 uncovered-SP worklist** (was 925 = 842 + 20 + 63);
**COVERAGE 125 → 127 of 188** (gained `1.6A` and `1.6C` — both via the R10
REATTRIBUTE rows; lost none); **CHUNK IDENTITY INVARIANT HOLDS** (W3: the
(note_path, ordinal, heading, sha256_16) multiset of all 862 chunk rows
IDENTICAL to the pre-R12 blob `80c883dcde552485` — only code attribution moved);
all 7 R10 REATTRIBUTE rows land verbatim with `provenance.override`
(provenance_class verdicted); the DEMOTE row (related-calculations ord 2)
carries `provenance.override` (action DEMOTE_TO_WORKLIST) + its recorded
worklist reason + disposition — RECORDED never forced; the 5 rows of the 2
re-pointed anchors ride the R10 codes; the meta counters now count from the
FINAL rows (post-override), not emission-time counters.

## Verification (scripts/c42_r11_r12_join_substrate_check.py)

- **W1** join refresh (census unchanged, 0 foreign, exact unresolved set,
  resolution pin, 2/2 verbatim codes, the STANDING pin)
- **W2** substrate shape (923 = 841 + 21 + 61; covered 127; all
  SUGGESTED/RULE_DERIVED; exactly 1 DEMOTE row, on the right chunk)
- **W3** chunk identity invariant (862-row multiset identical)
- **W4** re-attribution audit (all 862 pre-R12 chunk rows replayed: 5 re-pointed
  on the R10 CORRECT anchors, 24 REATTRIBUTE rows (R1 10 + R6 7 + R10 7),
  4 RETAIN, 2 subsumed riding the join, 1 DEMOTE, 18 cleared-span rows, 808
  non-surface rows zero-drift incl. the 3 STANDING rows)
- **W5** coverage/worklist recompute (gained 1.6A + 1.6C, lost none; worklist
  complete; mapping_ids unique)
- **W6** protected surfaces (dirty set == the R11/R12 footprint; Lane C stores,
  chemistry, the R10-amended resolution, the C42 scope/R0–R10 records
  byte-identical to `a26f3aa`)
- **W7** determinism (substrate re-run byte-identical; join re-run
  content-identical modulo generated_utc)

**ALL PASS 7/7, exit 0.**

## Staleness after

Join + substrate + coverage/worklist **FRESH**; the R9-era fill verdict record
and review sheet are superseded — **R13 renders a FRESH re-stratified sheet over
the rebuilt surface and re-fills under the C12/C13 convention with the R1
standing instruction (BOTH tier wordings) and `c42-heading-only-convention-1`
in force** (the convention's H1/H2/H3 ladder resolves the heading-only class
mechanically, per-row provenance); spec-links refresh remains a separate
follow-up armed by the R0 census; the `sme_spcpt_verify` legacy BASE pointer
stays on the operator queue.

## Scope guards

Chemistry, parsed canonical bundles, Lane C stores (concepts 82 /
concept_edges 157 = 84 PART_OF + 73 semantic / kinds 72), `spec-links/**`, the
C25–C41 records and the C42 scope/R0–R10 records byte-untouched (W6).

## Footprint

The refreshed join + the rebuilt substrate + `scripts/c32_notes_maths_a_join.py`
(R11 amendment) + `scripts/c40_maths_a_chunk_sp_substrate.py@2.2.0` (R12
amendment) + `scripts/c42_r11_r12_join_substrate_check.py` (new battery) +
`graph/reports/C42_R11_R12_CHECK.json` +
`graph/reports/C42_R11_R12_JOIN_SUBSTRATE_RECORD.{md,json}`.

**Next natural gate:** R13 re-gate (OPERATOR EVIDENCE, gate 2 re-run — fresh
re-stratified review sheet, both-tier-wording fill, the heading-only convention
enforced, ≥90% per-class required, Part B re-decided), then R5 §18 substrate
apply (operator gate 3) — the operator's choice to fire.
