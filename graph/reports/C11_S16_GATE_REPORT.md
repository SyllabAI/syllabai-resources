# T-C11 §16 Readiness Report — FINAL (Session 41, 2026-09-11)

**Question:** is §16 (full 4CH1 T-C11 expansion) ready for explicit
authorization?

**Answer: NO — §16 is NOT ready. This report does not self-authorize
anything.** The machine side is fully green and the operator's two
REVIEW_REQUIRED decisions are executed and recorded; what remains are
operator review actions (the two PENDING medium-confidence judgments, the
per-row verdicts on the 31 SUGGESTED edges and 29 nodes, and the explicit
§16 authorization itself), which by design cannot be performed by the
generation/review pipeline.

Ratification/promotion state at the close of this round: **0 promoted, 0
ratified identities** (the two RR decisions are REJECT and HOLD; the two
medium-confidence judgments are presented-pending; nothing else is confirmed).

## The 14 required readiness items

### 1. Final pilot node count

**29** (27 CONCEPT + 2 MISCONCEPTION). Unchanged by this round: the operator
REJECT removed an edge, not a node. All 29 remain AI_SUGGESTED; node
promotion (via PART_OF authority) is deferred to the expansion round per §18
scope limits.

### 2. Final edge count by relation type

**65 total** = 33 derived PART_OF + 32 authored semantic:

| relation | count | note |
|---|---|---|
| PART_OF | 33 | derived from node attachments (c11.7 machine-verified) |
| REQUIRES_PREREQUISITE | 25 | was 26 — the operator-REJECTED `4CH1-PR-03 → 4CH1-CON-MOLE` removed |
| EXPLAINED_BY | 3 | 1 of them (MOLAR-GAS-VOL ← AVOGADRO-LAW) is PENDING-gated |
| MISCONCEPTION_OF | 1 | |
| REMEDIATED_BY | 2 | 1 of them (MIS-EQ-SUBSCRIPT ← CONSERVATION-MASS) is PENDING-gated |
| WRONG_ANSWER_PATTERN | 1 | |
| RELATED_TO / COMMONLY_CONFUSED_WITH | 0 / 0 | honest abstention (residual classes kept empty) |

### 3. Accepted / rejected / held counts

| category | count |
|---|---|
| operator ACCEPT verdicts | **0** (no identity ratified) |
| operator REJECT verdicts | **1** — `PR-03 REQUIRES_PREREQUISITE CON-MOLE`, executed (HELD-13, permanent) |
| operator HOLD verdicts | **1** — `GAS-VOL-CALC REQUIRES_PREREQUISITE AVOGADRO-LAW`, stays REVIEW_REQUIRED |
| operator PENDING (presented, undecided) | **2** — the medium-confidence judgments (§5 below) |
| held candidates (abstention record) | **11 held + 2 rejected = 13** (HELD-01…12 + HELD-13; HELD-09 was already rejected as the negative control; HELD-13 is the operator rejection) |
| graph edges by state | 64 SUGGESTED + 1 REVIEW_REQUIRED + 0 HUMAN_VALIDATED |
| authored SUGGESTED edges awaiting per-row confirmation | 31 (29 unmarked + 2 PENDING-gated) |

### 4. Promoted count

**0.** No promotion was commanded: "promote ONLY explicitly ratified edge
identities" — no identity is ratified (see 3). The promotion record
(`scripts/c11_promotions.yaml`) has zero entries; the complete promotion
audit ran at zero with every guard exercised
(C11_OPERATOR_DECISIONS.md §4): 27/27 promote tests including the two new
permanence guards (T19: tool-level refusal of the rejected identity; T20:
generator-level G13 refusal of a forged promotion for it).

### 5. All remaining REVIEW_REQUIRED edges

1. `4CH1-CON-GAS-VOL-CALC REQUIRES_PREREQUISITE 4CH1-CON-AVOGADRO-LAW` —
   **operator HOLD** (2026-09-11; reasons recorded verbatim; not eligible for
   promotion; not to be converted to ACCEPT/REJECT merely to complete the
   pilot).
2. Review-gated beyond the formal state (SUGGESTED + operator_decision
   PENDING, presented session 41, full 10-field presentations in
   C11_OPERATOR_DECISIONS.md §2):
   - `4CH1-CON-MOLAR-GAS-VOL EXPLAINED_BY 4CH1-CON-AVOGADRO-LAW`
     (medium; FP-1: the anchor supports molar-volume→formula, not
     law→molar-volume; recommendation HOLD)
   - `4CH1-MIS-EQ-SUBSCRIPT REMEDIATED_BY 4CH1-CON-CONSERVATION-MASS`
     (medium; the tip's own corrective argument is substance-identity;
     recommendation HOLD pending exact-concept minting)

### 6. Failure-class distribution (architecture §19, now including the operator rejection)

| class | candidates | count |
|---|---|---|
| FC-1 evidence-sufficiency | HELD-01, HELD-11 | 2 |
| FC-2 relation-class misfit | HELD-02, HELD-03, HELD-10, HELD-12, **HELD-08 (residual-class discipline; added session 44, verdict unchanged)**; + the open RR edge (FC-2 with FC-1 evidence) | 5 (+1 quarantined) |
| FC-3 redundancy/normalization | HELD-04, HELD-05, HELD-06, HELD-07, **HELD-13 (operator-REJECTED)** | 5 |
| FC-4 negative-control enforcement | HELD-09 (rejected) | 1 |

*(Session-44 accounting completion, operator-directed, report-only: this
distribution previously counted 12 of 13 entries — HELD-08 was unassigned.
HELD-08 is now listed under FC-2 (residual-class discipline), matching the
session-43 review-package appendix assignment; architecture §19 carries the
same fix. The distribution now accounts for all 13 held/rejected entries;
HELD-08's verdict is unchanged (HELD).)*

The rejected RR edge is the first FC-3 instance carried to a permanent
operator rejection — the taxonomy now has one fully-executed precedent per
quarantine channel (abstain: HELD-09; emit-then-reject: HELD-13).

### 7. Provenance coverage

**100%** of all 29 nodes and 65 edges carry complete provenance blocks
(tier/model_version/extraction_pass/derivation_method/derivation_notes/
upstream/generated_date) — machine-checked (G01, c11.3). For promoted edges:
vacuously 100% at zero promotions; the mechanism preserves provenance
verbatim (T01c byte-preservation test) and will be re-audited per edge at
the first promotion.

### 8. Evidence coverage

**100%**: every node attachment, every misconception's evidence and
remediation, and every authored edge carries ≥1 evidence anchor whose quote
byte-verifies in its cited file under the T-C10 norm (G03/G04/G07,
c11.4/c11.6/c11.7). Zero unevidenced records.

### 9. Confidence distribution

| population | high | medium | low |
|---|---|---|---|
| nodes (29) | 29 | 0 | 0 |
| authored semantic edges (32) | 29 | 3 | 0 |
| all edges incl. PART_OF (65) | 62 | 3 | 0 |

The 3 medium: the open RR edge (operator HOLD) + the 2 PENDING-gated
judgments — exactly the review-gated set, i.e. no ungated record sits below
high confidence. All derivation-method caps respected (G09/c11.9).

### 10. Ontology decisions

- **OD-1 (yield triple — resolved as an ontology decision per the operator's
  item 6): NO MERGE; the three yield concepts stay split.** Grounds: §8
  minting rule (two definitions + one procedure are distinct concepts), the
  definition-vs-procedure split precedent (1.32 vs 1.33), independent
  assessability (merging corrupts mastery attribution), and the operand
  structure of the comparison formula. Generalized for §16: one procedure
  concept + one concept per distinctly-taught operand definition, one
  DEFINITIONAL_DEPENDENCY prerequisite per operand, same-anchor multiplicity
  expected. Recorded in C11_ARCHITECTURE.md §20; a future merge remains
  operator-only.
- **OD-2 (operator rule, verbatim): "Do not treat table labels or incidental
  terminology as instructional evidence."** Codified: IMPLICIT_USE evidence
  alone can never ground promotion; quarantine-or-abstain per FC-1.
  Recorded in §20 with the HELD-13 rejection.

### 11. Negative-control results (4CH1-4.15)

Zero manufactured coverage, machine-enforced and machine-tested at the new
65-edge state: frozen `c11_negative_test` **14/14** (incl. classes 10–11:
4.15 attachment via acid-rain note; EXPLAINED_BY from premise+consequence
notes), new-variant suite `c11_task4_variants` **3/3** (spec-wording SPEC
anchor, combustion-note topical similarity, remediation path from
byte-true uncovered quotes — all rejected). Live graph: 4.15 = 0 concepts,
0 edges, 0 coverage.

### 12. Deterministic regeneration result

**Byte-identical.** The generator re-run at the post-decision state
(29/65/13, zero promotions) leaves all three graph YAML files unchanged;
promotion state remains a pure function of (decision record, promotions
file). The graph diff vs the `e218259` pilot snapshot is exactly the
operator REJECT: the rejected edge block removed and meta counts updated;
all 65 remaining edges byte-identical with evidence/provenance/confidence
preserved verbatim.

### 13. Remaining corpus gaps

1. **4CH1-4.15** (sulfur impurities → sulfur dioxide → acid rain): the
   demanded causal mechanism is taught nowhere in the corpus (premise +
   stated consequence sit in different notes). Remediation is an operator
   content decision (new corpus note / student-book OCR) — never a
   graph-side inference.
2. **Boundary concepts** (FN-2): chemical-formulae interpretation (the exact
   remediation target for MIS-EQ-SUBSCRIPT), solute/solvent/solution,
   isotope abundance — real prerequisites living outside the pilot slice.
   The expansion MUST settle the boundary-minting policy or cross-slice
   prerequisites will be structurally missing.
3. **Assessment evidence** (FN-3): only 2 of ~17 Unit-1 mark schemes pinned;
   the wrong-answer-pattern inventory is deliberately minimal. Expansion
   should pin and mine all Unit-1/2 MS files per batch. HELD-01 and HELD-11
   both await better assessment-side evidence.
4. **Recorded defect (CORRECTED session 43, 2026-09-12 — report/data
   drift):** the previously reported "corrupted `aximum yield`" alias never
   existed in any data revision — the store has carried `maximum yield`
   byte-stably in both the decision record and `graph/concepts.yaml`. The
   genuine issue is that the alias is **unevidenced by the corpus** (the
   phrase appears nowhere in the pilot corpus — see the session-43 alias
   audit, `C11_REVIEW_PACKAGE.md` §7); disposition (drop / re-evidence /
   keep) is an operator decision. Report text corrected 2026-09-12; the
   concept alias itself was not modified.
5. **Review gap (not corpus, listed for completeness)**: 31 SUGGESTED
   authored edges + 29 nodes await operator per-row verdicts.

### 14. Proposed expansion scope and batching strategy (PROPOSAL — not executed)

**Scope**: the remaining 170 of 182 4CH1 spec points (the pilot's 12 are
done), over the 4 sections — S1 Principles (60 SPs total: 48 remaining after
the pilot), S2 Inorganic (50), S3 Physical (22), S4 Organic (50) — plus the
cross-slice boundary-concept layer and per-batch mark-scheme mining. The
T-C10 store already provides HUMAN_VALIDATED note mappings for 181/182
points (4.15 excepted), so every batch has validated attachment input; the
PMT Markdown++ batch (operator push `766dd23`) is a candidate additional
corpus source to evaluate before S2–S4.

**Batch order and size** (≈12 SPs per batch, the pilot's proven
reviewable scale; each batch = own extraction_pass id + decision record +
gated generation + pass-2 adversarial review + review sheet + operator
gate; §19 taxonomy and §20 rulings applied as generation rules):

| phase | batches | scope | rationale |
|---|---|---|---|
| 1 | 4 batches | S1 remainder (1.1–1.24, then 1.37+) | completes the mole/stoichiometry backbone the pilot started; highest prerequisite connectivity; pilot corpus already read |
| 2 | 2 batches | S3 Physical (22 SPs) | small, tightly coupled to S1 (rates/energy/equilibria reuse S1 concepts); fastest validation of cross-slice prerequisites |
| 3 | 4 batches | S2 Inorganic (50 SPs) | descriptive-heavy; validates the boundary-minting policy at scale |
| 4 | 4 batches | S4 Organic (50 SPs) | homologous-series structure stress-tests split-first identity + OD-1's operand rule |

Volume estimate (pilot ratios: 2.4 nodes + 2.75 authored edges + 1 held per
SP, with S2/S4 expected lighter on procedures): roughly **380–450 concept
nodes, 420–510 authored edges, ~170 held candidates** review workload total;
per batch ≈ 30 nodes / 33 edges / 12 held — one operator review sheet each
(the pilot sheet took one review round; plan one round per batch plus one
consolidated cross-slice boundary ruling before phase 2).

**Promotion shape**: per batch, after the operator records per-row verdicts,
a staged promotion batch command is derived mechanically from the confirms
(c10 §12/§13 pattern: exact identities, gated applier, pre/post audit);
REJECTED rows are re-authored out like HELD-13; PENDING/REVIEW_REQUIRED rows
stay quarantined. No promotion by node/relation/confidence/batch ever.

**Preconditions the expansion inherits** (already enforced): FC-4 negative
control per SP class; OD-2 evidence rule; OD-1 operand rule; the §16
authorization itself.

## Operator gate list (session-40 11 conditions, updated)

| # | condition | status |
|---|---|---|
| 1 | two REVIEW_REQUIRED edges resolved | **DONE** — REJECT executed (HELD-13, permanent, machine-guarded T19/T20); HOLD recorded with verbatim reasons |
| 2 | held-candidate taxonomy documented | **DONE** — §19; distribution in item 6 above |
| 3 | promotion mechanism tested | **DONE** — 27/27 |
| 4 | pilot promotion audited | **DONE at zero** — complete promotion audit run with 0 promotions; guards exercised; per-edge audit runs at first promotion |
| 5 | graph_check passes | **DONE** — 11/11 at the 65-edge state |
| 6 | all negative tests pass | **DONE** — 14/14 + 3/3 + 27/27 |
| 7 | deterministic regeneration byte-identical | **DONE** — at the post-decision state (item 12) |
| 8 | provenance coverage for promoted edges | **VACUOUS (0 promoted)**; mechanism preserves verbatim (T01c) |
| 9 | no 4.15 false coverage | **DONE** — machine-tested (item 11) |
| 10 | human review record committed | **PARTIAL** — the RR decisions, the medium-confidence presentations and the ontology rulings are committed; the operator's per-row verdicts on the 31 SUGGESTED edges + 29 nodes are still open, and the two PENDING judgments await decisions |
| 11 | T-C11 pilot snapshot frozen | **DONE (moved legitimately)** — the frozen 29/66/12 snapshot became 29/65/13 by the operator's own REJECT; reproducibility re-proven byte-identical |

## What still blocks §16 (operator actions, in order)

1. Rule on the two PENDING medium-confidence judgments (recommendations:
   HOLD both — C11_OPERATOR_DECISIONS.md §2).
2. Record per-row verdicts on the 31 SUGGESTED authored edges and 29 nodes
   (CONFIRM / REJECT / HOLD / MERGE / SPLIT; a batch-confirmation shape can
   be proposed on request), including the yield-triple ruling
   acknowledgment.
3. Ratify and command the first promotion identities (exact triples via
   `scripts/c11_promote.py`; a staged batch command derives mechanically
   from the confirms), then run the promotion audit.
4. Explicitly authorize §16 (or commission the full scoped expansion plan
   from the proposal in item 14).

Until then: no mass generation, no DB writes, no promotion — and no §16
authorization. This round did not self-authorize and did not expand the
graph.
