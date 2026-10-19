# T-C42 R7+R8 — Join Re-Run + Substrate Re-Build over the C42-R6-Amended Resolution

| | |
|---|---|
| **Task** | T-C42 (K2-B rework, the scope §7 loop's deterministic re-run lanes — R7 = the R2 lane, R8 = the R3 lane) |
| **Operator directive** | "R1-shaped verdict round over this inventory (then R2/R3/R4 re-run)" (2026-10-02, zai-web) — the R2/R3/R4 re-runs were fired in the same directive as the R6 round |
| **Baseline** | syllabai-resources `e48a434` (the amended R6 commit); resolution blob `466250eaa21fada2` (the R6-amended file) |
| **Nature** | agent-deterministic, every gate fail-closed, zero promotion (the substrate stays SUGGESTED; the C41-promoted 73 HUMAN_VALIDATED edges byte-untouched) |
| **Verification** | `scripts/c42_r7_r8_join_substrate_check.py` W1–W7 ALL PASS, exit 0 (deterministic re-runs byte-identical) |

---

## 1. R7 — the T-C32 join re-run

`scripts/c32_notes_maths_a_join.py` under a dated T-C42 R7 amendment (P5: the
generator is re-pinned, landed records never edited). The 2026-10-02 join is
regenerated 1:1 from the R6-amended resolution with the verbatim-preservation
rule unchanged and the foreign-code hard-fail in force:

| Measure | R2-era (post-R1) | **R7 (post-R6)** |
|---|---|---|
| joined / unresolved / anchors | 200 / 3 / 203 | **198 / 5 / 203** |
| distinct official codes | 119 | **120** (gained 2.4A, 2.8C, 3.4A; lost 2.8D, 4.4C) |
| foreign codes | 0 | **0** |
| wording census | 175 EXACT / 25 LEDGER_EXPLAINABLE | **173 EXACT / 25 LEDGER_EXPLAINABLE** |

Unresolved id set pinned EXACT (fail-closed): the C31 §3 residual
(`spcpt_QWXhzVp2S3VYZdZc`) + the 2 R1-cleared anchors (Mathematical Symbols,
Problem Solving with Areas) + the 2 R6-cleared anchors (Problem Solving with
Volumes, Geometrical Proof). All 8 R6 CORRECT codes landed verbatim and read
EXACT against their (Foundation-bare or Higher-H-) store ids — e.g. Compound
Measures → 4.4G "use compound measure such as speed, density and pressure",
Finding Gradients of Tangents → 4MA1-3.4A(H) "understand the concept of a
variable rate of change". The newly unresolved anchors carry PROPOSAL-ONLY
candidates that bind nothing (the standing residual rule).

## 2. R8 — the substrate re-build

`scripts/c40_maths_a_chunk_sp_substrate.py`@**2.1.0** under a dated T-C42 R8
amendment: G2 re-pinned to the 198+5 exact id set; **BOTH** operator override
maps consumed fail-closed — the R1 map (16 entries) AND the R6 map
(`scripts/c42_section_overrides_r6.yaml`: 4 verdicted + 3 labeled extension
entries); the R6 **subsumption registry** verified 2 R1 entries
(solving-linear-inequalities ord 3 → 2.8C, basic-fractions ord 6 → 1.2A) whose
correction now rides the join — recorded as `provenance.override_subsumed`,
NOT re-applied as no-ops; coverage + worklist recomputed; the chunker and
`c40-chunk-convention-1` untouched.

| Measure | R3-era (post-R1) | **R8 (post-R6)** |
|---|---|---|
| store rows | 928 = 854 + 8 + 66 | **925 = 842 anchored + 20 unresolved-span + 63 uncovered-SP** |
| covered codes | 122 / 188 | **125 / 188** (gained 1.2D, 2.4A, 3.4A, 3.4D, 4.9D; lost 2.8D, 4.4C) |
| chunk rows (anchored + unresolved-span) | 862 | **862 — identity invariant holds** |
| override consumption | 16 R1 entries (12 REATTR + 4 RETAIN) | R1: 10 REATTR + 4 RETAIN + 2 subsumed; R6: 7 REATTR (4 verdicted + 3 extension) |

The 12 rows of the 2 newly-cleared spans (Problem Solving with Volumes ords
0–3, Geometrical Proof ords 0–7) demoted to the unresolved-span worklist with
per-row R6 reasons — RECORDED, never forced. Applied override rows carry
`provenance.override` with the map sha and, for the R6 extension entries, the
`provenance_class: extension` label verbatim — the R9 re-fill can distinguish
verdicted from extension rulings.

## 3. Verification (W1–W7 ALL PASS)

| Gate | Asserts |
|---|---|
| W1 | join 198/5/203, 0 foreign, exact post-R6 unresolved set, resolution pin == amended disk file, 8/8 CORRECT codes landed, 2 cleared anchors absent from joins |
| W2 | 925 = 842 + 20 + 63; covered 125; every row SUGGESTED + RULE_DERIVED; upstream tier verbatim |
| W3 | the (note_path, ordinal, heading, sha256_16) multiset of all 862 chunk rows IDENTICAL to the pre-R8 blob `4ebb095ec73c850b` — only code attribution moved |
| W4 | all 862 pre-R8 chunk rows replayed: 40 rows on the 8 R6 CORRECT anchors re-pointed; 17 REATTRIBUTE (R1 10 + R6 7) + 4 RETAIN with provenance; 2 subsumed entries ride the join with `override_subsumed` provenance; 12+8 cleared-span rows demoted; all other rows zero-drift (spec_code AND upstream fields) |
| W5 | covered == recomputed; worklist complete; mapping_ids unique |
| W6 | dirty set == the R7/R8 footprint exactly; Lane C stores, chemistry substrate, the R6-amended resolution, the C42 scope/R0–R6 records byte-identical to `e48a434` |
| W7 | substrate re-run byte-identical; join re-run content-identical modulo `generated_utc` |

## 4. Staleness after and scope guards

FRESH: the join, the substrate, coverage/worklist. SUPERSEDED: the R4-era fill
verdict record and review sheet — **R9 renders a FRESH re-stratified sheet over
the rebuilt surface and re-fills under the C12/C13 convention with the R1
standing instruction (both tier wordings) in force**. spec-links refresh
remains a separate follow-up armed by the R0 census; the sme_spcpt_verify
legacy BASE pointer stays on the operator queue.

Chemistry, the parsed canonical bundles, the Lane C stores (concepts 82 /
concept_edges 157 = 84 PART_OF + 73 semantic / kinds 72), `spec-links/**`, the
C25–C41 records and the C42 scope/R0–R6 records byte-untouched (W6).
