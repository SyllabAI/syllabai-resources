# T-C42 R19+R20 — Join Re-Run + Substrate Re-Build over the Unchanged C42-R14-Amended Resolution (Consuming the R18 Override Map)

| | |
|---|---|
| **Task ID** | T-C42 R19 (join lane re-run) + R20 (substrate lane re-build) — the operator directive "fire R19+R20" (2026-10-04, zai-web), naming exactly the R18 record's next-decision gates: "R19+R20 (join re-run + substrate re-build consuming the R18 map, the DEMOTE and the extension rows)" |
| **Date** | 2026-10-04 |
| **Baseline** | `c10553d` (the R18 post-commit audit commit; local == remote at round start) |
| **Kind** | agent-deterministic re-runs; every gate fail-closed; zero promotion (the substrate stays `SUGGESTED`; the C41-promoted 73 HUMAN_VALIDATED edges byte-untouched) |
| **Verification** | `scripts/c42_r19_r20_join_substrate_check.py` → `graph/reports/C42_R19_R20_CHECK.json` (W1–W7 ALL PASS, exit 0; deterministic re-run byte-stable) |

## R19 — join re-run

`scripts/c32_notes_maths_a_join.py` under a dated **T-C42 R19 amendment** (P5: the
generator is re-pinned, landed records never edited):
`Official-Specifications/parsed/_derived/notes-join/igcse-maths-a-18-higher.json`
refreshed = **198 joined / 5 unresolved / 203 anchors / 0 foreign codes — census
UNCHANGED** (the R18 round re-pointed 0 note-level joins — BOTH adjudicated
STANDING — and cleared 0 anchors; the resolution file is BYTE-UNTOUCHED, counts
stay 222/214/8, last writer remains R14; the R19 round adds no resolution
writes of its own); **120/188 distinct codes**; anchors by tier **81 Foundation /
117 Higher** (unchanged); wording census **EXACT 173 / LEDGER_EXPLAINABLE 25**
(unchanged); the exact unresolved id set pinned (the C31 §3 residual + the 2
R1-cleared + the 2 R6-cleared anchors, fail-closed). **NEW at R19: the
generator itself pins the two R18 STANDING joins** —
`converting-between-fdp` → 4MA1-1.2G on `spcpt_8MpvS5pnYkf9QswF` and
`basic-angle-properties` → 4MA1-4.1B on `spcpt_5FMXZMjqSZ3GK53q`, each
verified against the R18 map's own `note_level_adjudications` (ruling text +
anchor id + landed code together, fail-closed; the R12/R16 in-generator pin
convention, now carried on the join side too) — plus the standing R10/R14
pins (`expanding-triple-brackets` → 4MA1-2.2A, `algebraic-fractions` →
4MA1-2.2C, `related-calculations` → 4MA1-1.8D STANDING,
`composite-functions` → 4MA1-3.2D, the R14 re-point); the unresolved anchors
keep their PROPOSAL-ONLY candidates that bind nothing.

## R20 — substrate re-build

`scripts/c40_maths_a_chunk_sp_substrate.py@2.4.0` under a dated **T-C42 R20
amendment**: G2 re-pinned to the unchanged 198+5 exact id set; **the FIVE
operator override maps consumed FAIL-CLOSED** — the R1 map (16 entries), the
R6 map (7 entries incl. the 2-key subsumption registry), the R10 map (8
verdicted entries: 7 REATTRIBUTE + the loop's first DEMOTE), the R14 map (5
verdicted entries: 4 REATTRIBUTE + the loop's second DEMOTE_TO_WORKLIST) AND
the R18 map `scripts/c42_section_overrides_r18.yaml` (4 entries: 1 verdicted
REATTRIBUTE — converting-between-fdp ord 3, 1.2G → 1.3D, the R9/R10
inverse-direction repair shape — + 2 labeled extension REATTRIBUTEs, ords 2/4
of the same note → 1.3D / 1.6C, the R6 transparently-labeled precedent, zero
silent repair + 1 DEMOTE_TO_WORKLIST, basic-angle-properties ord 1 — the
labeling primer, no canonical 188 row teaches it, the loop's third DEMOTE,
recorded never forced); **BOTH R18 note-level STANDING pins verified
in-generator** (the rulings read verbatim from the R18 map's
`note_level_adjudications`); the R10 STANDING pin (related-calculations →
1.8D) and the R14 RE-POINT pin (composite-functions → 3.2D) re-verified;
coverage + worklist recomputed; chunker and `c40-chunk-convention-1`
untouched.

**R20 detail — the R18 projections land HERE, computed never assumed:** the
R18 record projected "1.3D gains chunk coverage at the next re-build (the
R12/R16 coverage-gain precedent) — coverage 128 → 129 codes projected (129/188,
59 uncovered)" and "the unresolved-span class grows 22 → 23"; the re-build
computes exactly that arithmetic (W5: gained `4MA1-1.3D` COMPUTED, lost none —
the ord-3 verdicted + ord-2 extension rows are the anchoring rows; the 1.3D
uncovered-SP DEFER row on the R17 worklist resolves into anchored rows), and
the R18 map's gate arithmetic stays recorded-not-claimed: every re-gate
re-seeds (the R13 → R17 falsification precedent), so the 90% gate outcome is
whatever the R21 re-gate actually computes — R21 is NOT fired by this
directive.

**R20 amendment detail — the third DEMOTE's round tag derived, not hard-coded:**
the R16 amendment derives the DEMOTE disposition tag from the consuming map's
`operator_round` (deterministic regex, fail-closed on an unparsable round);
the R20 consumption reuses that mechanics — the R18 DEMOTE row records
`(C42 R18 surface 3 demote)` under its own round, reproducing the R10/R14
strings byte-for-byte in form.

Result: `graph/igcse-maths-a/spec_chunk_mappings.yaml` regenerated = **921
rows = 839 anchored + 23 unresolved-span worklist (incl. ALL THREE DEMOTE rows
— related-calculations ord 2 [R10], unit-conversions ord 2 [R14],
basic-angle-properties ord 1 [R18] — chunk identity intact) + 60 → 59
uncovered-SP worklist** (was 922 = 840 + 22 + 60); **COVERAGE 128 → 129 of
188** (gained `4MA1-1.3D` — the R18 REATTRIBUTE target; lost none); **CHUNK
IDENTITY INVARIANT HOLDS** (W3: the (note_path, ordinal, heading, sha256_16)
multiset of all 862 chunk rows IDENTICAL to the pre-R20 blob
`63f879617a591c33` — only code attribution moved); all 3 R18 REATTRIBUTE rows
land verbatim with `provenance.override` — the ord-3 row carries
`provenance_class verdicted`, the ord-2/ord-4 rows carry
`provenance_class extension` (the R6 precedent, recorded zero-silent-repair);
the R18 DEMOTE row carries `provenance.override` (action
DEMOTE_TO_WORKLIST) + its recorded worklist reason + derived disposition —
RECORDED never forced; the meta counters count from the emitted rows.

## W4 — re-attribution census (all 862 pre-R20 chunk rows replayed)

| Class | Rows | Note |
|---|---|---|
| wholesale re-point (R14 CORRECT anchor) | 5 | composite-functions 3.3I → 3.2D |
| REATTRIBUTE override rows | 31 | R1 10 + R6 7 + R10 7 + R14 4 + R18 3 (1 verdicted + 2 labeled extension) |
| RETAIN rows | 4 | R1 rulings, provenance.override recorded |
| R1 entries riding the join | 2 | the R6 subsumption registry |
| DEMOTE rows | 3 | related-calculations ord 2 (R10) + unit-conversions ord 2 (R14) + basic-angle-properties ord 1 (R18) |
| cleared-span rows | 18 | the 4 cleared spans (2 R1 + 2 R6) stay worklist |
| zero-drift non-surface rows | 799 | incl. the related-calculations STANDING rows and the converting-between-fdp ords 0/5/6 + basic-angle-properties ords 0/2/3 (the joins the R18 rulings held STANDING) |

## Scope guards

Chemistry, parsed canonical bundles, the Lane C stores (concepts 82 /
concept_edges 157 = 84 PART_OF + 73 semantic / kinds 72), `spec-links/**`,
the C25–C41 records, the C42 scope/R0–R18 records, the C30 ledger, the R18
override map and the R18 verdicts byte-untouched. The resolution substrate is
byte-untouched (its sha pin `b4539ab904c9a319` equals the R15/R16 record's —
no writer since R14). The diff surface of this round is exactly: the two
amended generators + the refreshed join + the regenerated store + this
round's check/record artifacts.

**Stale by design after R19/R20:** none within the loop — the R21 re-gate
re-renders the review surface over this substrate (fired only by explicit
operator instruction; menu options (b) heading-only convention amendment,
(c) fire R5 on confirmed rows, (d) accept and re-scope remain open, the
operator's call); spec-links refresh remains a separate follow-up armed by
the R0 census; the `sme_spcpt_verify` legacy BASE pointer and the
accounting-sidecar G1/G2 census (the R18 environment finding, 53
pre-existing failures predating every C42 round) stay on the operator queue.

## What this round does not do

Nothing self-repairs beyond the deterministic re-runs. Zero promotion: all
921 rows re-verified `SUGGESTED` / `RULE_DERIVED`; the store's SUGGESTED →
HUMAN_VALIDATED apply is R5 (operator gate 3), armed only by a GREEN R21
re-gate and fired only by the operator's explicit instruction. The R21
re-gate itself is NOT fired by this directive — the operator named R19+R20
alone.
