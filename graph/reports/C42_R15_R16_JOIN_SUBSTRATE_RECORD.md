# T-C42 R15+R16 — Join Re-Run + Substrate Re-Build over the C42-R14-Amended Resolution

| | |
|---|---|
| **Task ID** | T-C42 R15 (join lane re-run) + R16 (substrate lane re-build) — the operator directive "R15 (connection rerun) + R16 (substrate reconstruction), then R17 re-gating" (2026-10-04, zai-web) |
| **Date** | 2026-10-04 |
| **Baseline** | `af3b80d6` (the R14 post-commit audit commit; local == remote at round start) |
| **Kind** | agent-deterministic re-runs; every gate fail-closed; zero promotion (the substrate stays `SUGGESTED`; the C41-promoted 73 HUMAN_VALIDATED edges byte-untouched) |
| **Verification** | `scripts/c42_r15_r16_join_substrate_check.py` → `graph/reports/C42_R15_R16_CHECK.json` (W1–W7 ALL PASS, exit 0; deterministic re-run byte-stable) |

## R15 — join re-run

`scripts/c32_notes_maths_a_join.py` under a dated **T-C42 R15 amendment** (P5: the
generator is re-pinned, landed records never edited):
`Official-Specifications/parsed/_derived/notes-join/igcse-maths-a-18-higher.json`
refreshed = **198 joined / 5 unresolved / 203 anchors / 0 foreign codes — census
UNCHANGED** (the R14 round re-pointed 1 code and cleared 0 anchors; the
resolution counts stay 222/214/8); **120/188 distinct codes** (3.2D was already
covered via the sibling inverse-functions note — the re-point adds a second
note to a covered code, the R10 2.2A shape); anchors by tier **82 Foundation /
116 Higher → 81 / 117** (the re-pointed composite-functions anchor crossed
Foundation 3.3I → Higher 3.2D); wording census **EXACT 173 /
LEDGER_EXPLAINABLE 25** (unchanged); the exact unresolved id set pinned (the
C31 §3 residual + the 2 R1-cleared + the 2 R6-cleared anchors, fail-closed);
**NEW at R15: the generator itself pins the exact code the re-pointed join must
carry** (`composite-functions` → 4MA1-3.2D on `spcpt_XWbj3PG2n8tdWF2w`, plus
the standing R10 pins: `expanding-triple-brackets` → 4MA1-2.2A,
`algebraic-fractions` → 4MA1-2.2C, `related-calculations` → 4MA1-1.8D
STANDING) — any drift fails closed; the unresolved anchors keep their
PROPOSAL-ONLY candidates that bind nothing.

## R16 — substrate re-build

`scripts/c40_maths_a_chunk_sp_substrate.py@2.3.0` under a dated **T-C42 R16
amendment**: G2 re-pinned to the unchanged 198+5 exact id set; **the FOUR
operator override maps consumed FAIL-CLOSED** — the R1 map (16 entries), the R6
map (7 entries incl. the 2-key subsumption registry), the R10 map (8 verdicted
entries: 7 REATTRIBUTE + the loop's first DEMOTE) **and the R14 map (5 verdicted
entries: 4 REATTRIBUTE + the loop's second DEMOTE_TO_WORKLIST —
unit-conversions ord 2, metric mass conversion, no canonical 188 row teaches it,
REATTRIBUTE has no target)**; **BOTH note-level pins verified in-generator**
(the R10 STANDING pin: related-calculations must still join 1.8D on
`spcpt_crKbmb6wVjM4yPJh`; the R14 RE-POINT pin: composite-functions must join
3.2D on `spcpt_XWbj3PG2n8tdWF2w`); coverage + worklist recomputed; chunker and
`c40-chunk-convention-1` untouched.

**R16 amendment detail — DEMOTE disposition tag derived, not hard-coded:** the
R12 build hard-coded the first DEMOTE's round tag into the disposition string;
the R16 amendment derives the tag from the consuming map's `operator_round`
(deterministic regex, fail-closed on an unparsable round), which reproduces the
R10 string byte-for-byte and records the R14 DEMOTE under its own round — the
R17 re-fill sees exactly which operator round demoted each row.

Result: `graph/igcse-maths-a/spec_chunk_mappings.yaml` regenerated = **922 rows
= 840 anchored + 22 unresolved-span worklist (incl. BOTH DEMOTE rows —
related-calculations ord 2 [R10] and unit-conversions ord 2 [R14] — chunk
identity intact) + 60 uncovered-SP worklist** (was 923 = 841 + 21 + 61);
**COVERAGE 127 → 128 of 188** (gained `4.1D` — the sole previously-uncovered
R14 REATTRIBUTE target, via the properties-of-2d-shapes ord-2 ruling; lost
none); **CHUNK IDENTITY INVARIANT HOLDS** (W3: the (note_path, ordinal,
heading, sha256_16) multiset of all 862 chunk rows IDENTICAL to the pre-R16
blob `fe9166e8f31e4110` — only code attribution moved); all 4 R14 REATTRIBUTE
rows land verbatim with `provenance.override` (provenance_class verdicted) —
`4.1D`, `4.6A` (the C30-ledger Foundation wording), `6.3E`, `1.7B`; the 5 rows
of the re-pointed anchor ride 3.2D wholesale (the R14 CORRECT verdict); the
R14 DEMOTE row (unit-conversions ord 2) carries `provenance.override` (action
DEMOTE_TO_WORKLIST) + its recorded worklist reason + disposition — RECORDED
never forced; the meta counters count from the emitted rows.

## W4 — re-attribution census (all 862 pre-R16 chunk rows replayed)

| Class | Rows | Note |
|---|---|---|
| wholesale re-point (R14 CORRECT anchor) | 5 | composite-functions 3.3I → 3.2D |
| REATTRIBUTE override rows | 28 | R1 10 + R6 7 + R10 7 + R14 4 |
| RETAIN rows | 4 | R1 rulings, provenance.override recorded |
| R1 entries riding the join | 2 | the R6 subsumption registry |
| DEMOTE rows | 2 | related-calculations ord 2 (R10) + unit-conversions ord 2 (R14) |
| cleared-span rows | 18 | the 4 cleared spans (2 R1 + 2 R6) stay worklist |
| zero-drift non-surface rows | 803 | incl. the related-calculations STANDING rows |

## Scope guards

Chemistry, parsed canonical bundles, the Lane C stores (concepts 82 /
concept_edges 157 = 84 PART_OF + 73 semantic / kinds 72), `spec-links/**`, the
C25–C41 records and the C42 scope/R0–R14 records byte-untouched. The diff
surface of this round is exactly: the two amended generators + the refreshed
join + the regenerated store + this round's check/record artifacts.

**Stale by design after R15/R16:** none within the loop — the R17 re-gate
re-renders the review surface over this substrate; spec-links refresh remains a
separate follow-up armed by the R0 census; the `sme_spcpt_verify` legacy BASE
pointer stays on the operator queue.

## What this round does not do

Nothing self-repairs beyond the deterministic re-runs. Zero promotion: all 922
rows re-verified `SUGGESTED` / `RULE_DERIVED`; the store's SUGGESTED →
HUMAN_VALIDATED apply is R5 (operator gate 3), armed only by a GREEN R17
re-gate and fired only by the operator's explicit instruction.
