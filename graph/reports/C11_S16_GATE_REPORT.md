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

> **Session-45 update (2026-09-12):** the session-44 verdict round has since
> recorded the operator's full decision set (28 edge CONFIRM / 3 HOLD @
> E-08/E-26/E-29 / 0 REJECT; 29 node CONFIRM; OD-1/OD-2 RATIFIED —
> `scripts/c11_review_verdicts.yaml`), and the authorized application round
> promoted the 28 CONFIRM edges through the §18 pathway
> (`c11_diff_review.py approve --all` → one `c11_promote.py` invocation →
> gated G13 re-run; `scripts/c11_promotions.yaml` now carries 28 entries,
> `operator`, 2026-09-12). The verdict counts and state rows below are the
> session-41 snapshot they were decided against, annotated where they moved.
> **§16 remains NOT ready / NOT authorized** — the explicit authorization is
> still a separate operator action.

> **Session-46 update (2026-09-12): §16 IS NOW AUTHORIZED.** The operator gave
> the explicit authorization this report was awaiting — verbatim: "Okay, I
> authorize" — answering item 4 below (the sole remaining blocker at the close
> of session 45). It is recorded in the operator-owned
> `scripts/c11_s16_authorization.yaml` and validated fail-closed by
> `scripts/c11_s16_authorization_check.py` (schema / authorization-only
> payload / cross-file consistency / frozen-pilot-disposition invariants).
> The answer above ("NO — §16 is NOT ready") is the session-41 readiness
> verdict, listing exactly the operator review actions that are now all
> complete: gate list 14/14 DONE, blockers 4/4 settled. The authorization adopts
> item 14's batching proposal as the sanctioned execution shape — every batch
> still passes its own operator gate before any promotion. The authorization
> itself commands no generation: batch execution is separately commissioned,
> and nothing outside the operator's decision set changes.

> **Session-47 update (2026-09-12): batch 1 COMMISSIONED + AUTHORED — its
> operator gate PENDING.** The operator commissioned phase-1 batch 1 ("run
> batch 1"): extraction_pass `c11-s16-batch-1` over the first 12 S1-remainder
> SPs (4CH1-1.1–1.12 + practical PR-01; 10 T-C10-validated notes + 2 pinned
> mark schemes). Authored: 24 nodes / 29 authored edges (28 SUGGESTED + 1
> subsumption-class REVIEW_REQUIRED quarantine) / 12 held candidates — the
> merged store is 53 nodes / 118 edges with the 28 operator promotions and
> every frozen pilot disposition byte-intact. The batch ENDS at its operator
> gate: `graph/reports/C11_BATCH1_REVIEW_SHEET.md` + the verdict template
> `scripts/c11_batch1_verdicts_template.yaml`; NOTHING from batch 1 is
> promoted, promotable-before-verdicts, or HUMAN_VALIDATED. The §18 front-end
> now lists the 28 batch-1 SUGGESTED edges as the pending actionable surface.

> **Session-48 update (2026-09-12): batch 1 GATE SETTLED — verdicts recorded
> and applied.** The operator ruled on the batch-1 gate with the verbatim
> ruling **"CONFIRM all"**. Recorded in the operator-owned verdict record
> `scripts/c11_batch1_verdicts.yaml` (the template, filled + renamed per the
> gate pathway): 28 edge CONFIRM / 24 node CONFIRM (B1-N-08/B1-N-11 keep
> ENRICHMENT scoping) / 4 identity decisions KEEP_AS_IS / RR settlement
> HOLD_REVIEW_REQUIRED / held appendix acknowledged. Applied through the
> exact session-44/45 shape: §7 re-authoring (the RR settlement + the two
> enrichment-scoping operator_decision blocks in
> `scripts/c11_batch1_decisions.yaml`) then §18 (`c11_diff_review.py
> approve --all` over the B1 bundle → one `c11_promote.py` invocation →
> gated G13 re-run; 28 new promotion entries, all `operator`, 2026-09-12,
> review_reference the B1 diff-review bundle). **Store total: 56 HUMAN_VALIDATED
> (28 pilot + 28 batch-1); the RR quarantine stays REVIEW_REQUIRED
> (operator-settled); batch-1 nodes stay SUGGESTED (no node §18 pathway).**
> The standing checker `scripts/c11_batch1_verdict_check.py` (33 checks)
> validates the verdict layer + three-way set equality (verdict CONFIRM set
> == live batch-1 HUMAN_VALIDATED set == store batch-1 entries). Batch 2
> (S1 remainder 1.13–1.24) is commissionable; the cross-slice boundary
> ruling comes before phase 2 (S3).

> **Session-49 update (2026-09-12): batch 2 COMMISSIONED + AUTHORED — its
> operator gate PENDING.** The operator commissioned phase-1 batch 2 ("run
> batch 2"): extraction_pass `c11-s16-batch-2` over the second 12
> S1-remainder SPs (4CH1-1.13–1.24 + practical PR-02; 7 T-C10-validated
> notes + 6 pinned mark schemes — the ECM1/ECM3 pins close the batch-1
> FN-B1-1 remainder). Authored: 14 nodes (11 CONCEPT incl. 1 ENRICHMENT
> leaf [semi-metals] + 2 mark-scheme-documented WRONG_ANSWER_PATTERN
> misconceptions: isotopes-differ-in-protons, RAM-vs-mass-number — both
> REJECT-column layout-verified) / 23 authored edges (all SUGGESTED, ZERO
> RR authored — every doubt held or resolved on explicit evidence) incl.
> the store's FIRST COMMONLY_CONFUSED_WITH edge and 5 sanctioned
> cross-boundary edges (CON-AR ×2, CON-ELEMENT, CON-CHROMATOGRAPHY,
> CON-RF-VALUE — no duplicate mint: the Ar term stays with the pilot's
> CON-AR) / 10 held candidates — the merged store is 67 nodes / 156 edges
> with the 56 operator promotions and every frozen disposition byte-intact.
> The batch ENDS at its operator gate:
> `graph/reports/C11_BATCH2_REVIEW_SHEET.md` + the verdict template
> `scripts/c11_batch2_verdicts_template.yaml`; NOTHING from batch 2 is
> promoted, promotable-before-verdicts, or HUMAN_VALIDATED. The §18
> front-end lists the 23 batch-2 SUGGESTED edges as the pending actionable
> surface (23 / 5 not-actionable / promo_count=56).

> **Session-50 update (2026-09-12): batch 2 GATE SETTLED — verdicts recorded
> and APPLIED.** The operator ruled on the session-49 review sheet, verbatim:
> "CONFIRM all" — recorded in the operator-owned
> `scripts/c11_batch2_verdicts.yaml` (23 edge CONFIRM / 14 node CONFIRM
> [B2-N-08 keeps ENRICHMENT scoping] / 4 identity decisions KEEP_AS_IS /
> held appendix of 10 acknowledged; NO RR settlement row — batch 2 authored
> zero REVIEW_REQUIRED edge), encoded fail-closed by
> `scripts/c11_verdict_encode_batch2.py`, applied session 50: §7
> re-authoring (`scripts/c11_verdict_apply_batch2.py` — the B2-N-08
> enrichment-scoping operator_decision block + header note; generator re-run
> byte-identical, the blocks never reach graph/*.yaml) + §18 promotion
> (bundle `graph/reports/C11_DIFF_REVIEW_B2_2026-09-12.md` →
> `c11_diff_review.py approve --all --by operator` → ONE `c11_promote.py`
> invocation → 23 promotions, all operator) → **79 HUMAN_VALIDATED total
> (28 pilot + 28 batch-1 + 23 batch-2)**. The §18 surface is empty again
> (0 / 5 not-actionable / promo_count=79). New standing gate
> `scripts/c11_batch2_verdict_check.py` ALL PASS (three-way set equality:
> verdict CONFIRM set == live batch-2 HV set == store batch-2 entries;
> pilot + batch-1 slices intact; 4.15 uncovered).

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
| operator ACCEPT verdicts | session-45: **28 CONFIRM** ratified (session 44) and promoted via §18; session-41 snapshot: **0** (no identity ratified) |
| operator REJECT verdicts | **1** — `PR-03 REQUIRES_PREREQUISITE CON-MOLE`, executed (HELD-13, permanent) |
| operator HOLD verdicts | session-45: **4** — the RR edge (session 41, below) + E-08/E-26/E-29 (session 44, rationale verbatim); session-41 snapshot: **1** |
| operator PENDING (presented, undecided) | session-45: **0** — both settled HOLD (session 44); session-41 snapshot: **2** — the medium-confidence judgments (§5 below) |
| held candidates (abstention record) | **11 held + 2 rejected = 13** (HELD-01…12 + HELD-13; HELD-09 was already rejected as the negative control; HELD-13 is the operator rejection) |
| graph edges by state | session-52: **118 HUMAN_VALIDATED** (28 pilot §18 session-45 + 28 batch-1 §18 session-48 + 23 batch-2 §18 session-50 + 39 batch-3 §18 session-52, all operator) + 3 SUGGESTED semantic (the pilot operator HOLDs — the only SUGGESTED semantic edges left) + 33+24+15+25 PART_OF (SUGGESTED, derived) + 2 REVIEW_REQUIRED (frozen); session-51: **79 HUMAN_VALIDATED** (unchanged — batch-3 authoring promotes nothing) + 42 SUGGESTED semantic (3 pilot operator HOLDs + 39 batch-3 edges awaiting that batch's operator gate) + 33+24+15+25 PART_OF (SUGGESTED, derived) + 2 REVIEW_REQUIRED (frozen); session-50: **79 HUMAN_VALIDATED** (28 pilot §18 session-45 + 28 batch-1 §18 session-48 + 23 batch-2 §18 session-50, all operator) + 3 SUGGESTED semantic (the pilot operator HOLDs — the only SUGGESTED semantic edges left) + 33+24+15 PART_OF (SUGGESTED, derived) + 2 REVIEW_REQUIRED (the pilot RR operator-HOLD + the settled batch-1 RR quarantine; batch 2 authored no RR); session-49: 56 HUMAN_VALIDATED + 3 SUGGESTED + 23 batch-2 SUGGESTED + 57 PART_OF + 2 RR; session-48: 56 HUMAN_VALIDATED + 3 SUGGESTED + 57 PART_OF + 2 RR; session-45: 28 HUMAN_VALIDATED + 3 SUGGESTED + 33 PART_OF + 1 RR; session-41 snapshot: 64 SUGGESTED + 1 REVIEW_REQUIRED + 0 HUMAN_VALIDATED |
| authored SUGGESTED edges awaiting per-row confirmation | session-52: **0** (batch-3 verdicts applied — 39 promoted, 14 held untouched; no RR was authored, so nothing settled to a non-promotable state); session-51: **39** (the batch-3 gate — 39 clean SUGGESTED edges awaiting per-row verdicts; 14 held untouched; zero RR authored); session-50: **0** (batch-2 verdicts applied — 23 promoted, 10 held untouched; no RR was authored, so nothing settled to a non-promotable state); session-49: **23** (the batch-2 gate — 23 clean SUGGESTED edges awaiting per-row verdicts; 10 held untouched); session-48: **0** (batch-1 verdicts applied — 28 promoted, RR settled, 12 held untouched); session-45: **0** (28 promoted, 3 HOLD); session-41 snapshot: 31 (29 unmarked + 2 PENDING-gated) |

### 4. Promoted count

**0.** No promotion was commanded: "promote ONLY explicitly ratified edge
identities" — no identity is ratified (see 3). The promotion record
(`scripts/c11_promotions.yaml`) has zero entries; the complete promotion
audit ran at zero with every guard exercised
(C11_OPERATOR_DECISIONS.md §4): 27/27 promote tests including the two new
permanence guards (T19: tool-level refusal of the rejected identity; T20:
generator-level G13 refusal of a forged promotion for it).

**Session-45 update (2026-09-12): 28.** The operator commanded the batch
promotion of the 28 CONFIRM verdicts through the §18 pathway (the
pre-verified batch-approve front-end invoked `c11_promote.py` once — a
single gated G13 re-run). The per-edge audit ran for real: every promotion's
evidence byte-verified before any write, provenance preserved verbatim,
`scripts/c11_promotions.yaml` = 28 entries (`operator`, 2026-09-12,
review_reference = the regenerated diff-review bundle), graph_check
c11.10/c11.13 green at 28 promoted, deterministic regeneration re-proven
byte-identical WITH the promotions file present.

**Session-48 update (2026-09-12): 56.** The batch-1 operator gate settled
(ruling "CONFIRM all", `scripts/c11_batch1_verdicts.yaml`): the same §18
pathway applied 28 more operator promotions over operator-confirmed
identities (bundle `graph/reports/C11_DIFF_REVIEW_B1_2026-09-12.md`; the
session-45 bundle preserved byte-intact at its own path). The standing
`c11_batch1_verdict_check.py` (33 checks) proves the three-way set equality
(verdict CONFIRM set == live batch-1 HUMAN_VALIDATED set == store batch-1
entries); graph_check c11.10/c11.13 green at 56 promoted; deterministic
regeneration re-proven byte-identical with the 56-entry store.

**Session-50 update (2026-09-12): 79.** The batch-2 operator gate settled
(ruling "CONFIRM all", `scripts/c11_batch2_verdicts.yaml`): the same §18
pathway applied 23 more operator promotions over operator-confirmed
identities (bundle `graph/reports/C11_DIFF_REVIEW_B2_2026-09-12.md`; the
pilot and B1 bundles preserved byte-intact at their own paths; zero RR
authored in batch 2, so nothing was left un-promotable by settlement). The
standing `c11_batch2_verdict_check.py` (32 checks) proves the three-way set
equality (verdict CONFIRM set == live batch-2 HUMAN_VALIDATED set == store
batch-2 entries); graph_check c11.10/c11.13 green at 79 promoted;
deterministic regeneration re-proven byte-identical with the 79-entry
store.

**Session-52 update (2026-09-13): 118.** The batch-3 operator gate settled
(the practical-review policy, `scripts/c11_batch3_verdicts.yaml`: CONFIRM
where the evidence clearly supports the authored relationship;
HOLD/REJECT only for genuine evidence insufficiency or an
architectural/semantic problem; ordinary ontology imperfection, wording
preferences, enrichment opportunities and theoretical alternative
interpretations are NOT blockers): 39 edge CONFIRM / 24 node CONFIRM / 7
identity decisions KEEP_AS_IS / 14 held acknowledged (clean quarantine).
The same §18 pathway applied 39 more operator promotions over
operator-confirmed identities (bundle
`graph/reports/C11_DIFF_REVIEW_B3_2026-09-13.md`; the pilot, B1 and B2
bundles preserved byte-intact at their own paths; zero RR authored in
batch 3, so nothing was left un-promotable by settlement). The §7
application is the header note only (no RR settlement block, no
ENRICHMENT node, no MERGE/SPLIT — all identity decisions KEEP_AS_IS);
generator re-run byte-identical. The standing `c11_batch3_verdict_check.py`
(32 checks) proves the three-way set equality (verdict CONFIRM set ==
live batch-3 HUMAN_VALIDATED set == store batch-3 entries); graph_check
c11.10/c11.13 green at 118 promoted; deterministic regeneration re-proven
byte-identical with the 118-entry store.

### 5. All remaining REVIEW_REQUIRED edges

> Session-45 (2026-09-12): the two PENDING judgments under 2 below were
> settled HOLD by the operator in session 44 (verbatim rationale in
> `scripts/c11_review_verdicts.yaml` rows E-26/E-29; §7 operator_decision
> blocks in the decision record); they stay SUGGESTED and are not promotable.

> Session-48 (2026-09-12): the batch-1 RR quarantine edge
> `4CH1-CON-CRYSTALLISATION REQUIRES_PREREQUISITE 4CH1-CON-SOLUTION`
> (authored session 47, subsumption class) was settled by the operator:
> HOLD_REVIEW_REQUIRED (ruling "CONFIRM all" — `scripts/c11_batch1_verdicts.yaml`
> row B1-RR-01; §7 operator_decision block in the batch-1 decision record).
> It stays REVIEW_REQUIRED and is not promotable.
>
> Session-50 (2026-09-12): batch 2 authored ZERO REVIEW_REQUIRED edges
> (every doubt was held or resolved on explicit evidence), so no RR
> settlement arose; the two RR edges below are unchanged.

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
vacuously 100% at zero promotions (session-41 snapshot); session-45: **28
promoted, provenance preserved verbatim** — the §18 transformation adds only
the validation fields (machine-checked c11.10/c11.13 + the promote test's
byte-preservation guard T01c).

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
preserved verbatim. Session-45 re-proof: the re-run at the post-application
state (29/65/13 with 28 promotions) is again byte-identical — the graph
diff vs the session-41 snapshot is exactly the 28 §18 promotions (status +
validated_by/date + meta counts + promotion_record), all evidence /
provenance / confidence / ambiguity blocks byte-identical.

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
| 4 | pilot promotion audited | **DONE** — complete promotion audit at zero (session 41, every guard exercised); session-45: the per-edge audit ran for real at 28 promotions (evidence byte-verified pre-write, provenance preserved, c11.10/c11.13 green) |
| 5 | graph_check passes | **DONE** — 11/11 at the 65-edge state |
| 6 | all negative tests pass | **DONE** — 14/14 + 3/3 + 27/27 |
| 7 | deterministic regeneration byte-identical | **DONE** — post-decision state (session 41) and post-application state (session-45 re-proof, item 12) |
| 8 | provenance coverage for promoted edges | **DONE (28 promoted)** — provenance preserved verbatim by the §18 transformation (T01c + c11.10/c11.13); session-41 snapshot: VACUOUS (0 promoted) |
| 9 | no 4.15 false coverage | **DONE** — machine-tested (item 11) |
| 10 | human review record committed | **DONE** — session-44 verdict record (`scripts/c11_review_verdicts.yaml`: 28 CONFIRM / 3 HOLD / 29 nodes / OD-1+OD-2 RATIFIED) + session-45 §18 application (28 promotions) + §7 decision-record blocks; the two PENDING judgments are settled HOLD; session-41 snapshot: PARTIAL |
| 11 | T-C11 pilot snapshot frozen | **DONE (moved legitimately)** — the frozen 29/66/12 snapshot became 29/65/13 by the operator's own REJECT; reproducibility re-proven byte-identical |

## What still blocks §16 (operator actions, in order)

> **Session-45 update (2026-09-12): items 1-3 are DONE.** The two PENDING
> judgments are settled HOLD (session 44, rows E-26/E-29); the per-row
> verdicts are recorded in the operator-owned verdict record (session 44);
> the 28 CONFIRM identities are ratified and promoted through §18 with the
> per-edge promotion audit green (session 45). What remains is item 4 alone.

> **Session-46 update (2026-09-12): item 4 is DONE — all four items settled.**
> §16 AUTHORIZED by explicit operator action (see the header note); nothing
> blocks §16 any longer. The gate list above is 14/14 DONE.

1. Rule on the two PENDING medium-confidence judgments (recommendations:
   HOLD both — C11_OPERATOR_DECISIONS.md §2). *— DONE session 44 (HOLD both).*
2. Record per-row verdicts on the 31 SUGGESTED authored edges and 29 nodes
   (CONFIRM / REJECT / HOLD / MERGE / SPLIT; a batch-confirmation shape can
   be proposed on request), including the yield-triple ruling
   acknowledgment. *— DONE session 44 (`scripts/c11_review_verdicts.yaml`).*
3. Ratify and command the first promotion identities (exact triples via
   `scripts/c11_promote.py`; a staged batch command derives mechanically
   from the confirms), then run the promotion audit. *— DONE session 45
   (28 §18 promotions, audit green).*
4. Explicitly authorize §16 (or commission the full scoped expansion plan
   from the proposal in item 14). *— DONE session 46 (§16 AUTHORIZED by
   explicit operator action, verbatim "Okay, I authorize"; record:
   `scripts/c11_s16_authorization.yaml`, gate:
   `scripts/c11_s16_authorization_check.py`).*

Until then: no mass generation, no DB writes, no unratified promotion — and
no §16 authorization. (Session-45 note: the 28 §18 promotions were the
operator's own command over session-44-ratified identities — exactly the
sanctioned channel; nothing else was promoted and nothing outside the pilot
slice was touched.) This round did not self-authorize and did not expand the
graph.

(Session-46 note: the "no §16 authorization" condition is now satisfied —
the operator authorized §16 explicitly on 2026-09-12, recorded in
`scripts/c11_s16_authorization.yaml`. The operative disciplines continue
unchanged and are carried in the authorization record's invariants: every
batch passes its own operator gate before any promotion; no unratified
promotion, ever; no DB writes; AI attribution forbidden; OD-1/OD-2 and the
§19 failure classes applied as generation rules; the deterministic
regeneration contract and the full gate suite green at every batch boundary.
No batch has been generated by the authorization itself.)

(Session-47 note: batch 1 has now been COMMISSIONED and AUTHORED under that
sanctioned pathway — own extraction_pass, own decision record
(`scripts/c11_batch1_decisions.yaml`), gated generation through the
registry-aware generator, pass-2 adversarial review
(`scripts/c11_batch1_review_pass2.yaml`), review sheet + verdict template.
The batch stops at its operator gate: no batch-1 promotion, no unratified
identity, no DB writes. The batch-1 verdicts — when the operator records
them — flow through exactly the session-44/45 shape: verdict record → §18
approve → one `c11_promote.py` invocation → gated G13 re-run. The
forecast instrument carries the batch-1 predicted-vs-actual record
(`C11_BATCH_FORECAST.json` future_batch_records).)

(Session-48 note: the batch-1 verdicts ARE now recorded and applied — the
operator's ruling "CONFIRM all", encoded verbatim in
`scripts/c11_batch1_verdicts.yaml` and settled exactly through the
session-44/45 shape described above (§7 blocks + §18 approve → promote →
gated re-run; bundle `graph/reports/C11_DIFF_REVIEW_B1_2026-09-12.md`).
The 28 batch-1 CONFIRM edges are HUMAN_VALIDATED with operator
attribution; the RR quarantine is operator-settled HOLD_REVIEW_REQUIRED and
stays un-promoted; the frozen pilot dispositions are byte-intact; the
full gate suite is green at the 56-promotion state, including the new
standing checker `scripts/c11_batch1_verdict_check.py`. No unratified
promotion occurred: every promoted identity traces to an operator verdict
row.)

(Session-50 note: the batch-2 verdicts are likewise recorded and applied —
the operator's ruling "CONFIRM all", encoded verbatim in
`scripts/c11_batch2_verdicts.yaml` (23 edge CONFIRM / 14 node CONFIRM /
4 KEEP_AS_IS / held 10 acknowledged; zero RR authored, so no settlement
row) and settled through the same sanctioned shape: §7 re-authoring
(`c11_verdict_apply_batch2.py` — the B2-N-08 enrichment block; generator
re-run byte-identical) + §18 (bundle
`graph/reports/C11_DIFF_REVIEW_B2_2026-09-12.md` → approve --all → one
`c11_promote.py` invocation → 23 operator promotions). The store now
carries 79 HUMAN_VALIDATED, all operator; the only SUGGESTED semantic
edges left are the 3 pilot operator HOLDs; both RR edges keep their
operator settlements; the frozen pilot + batch-1 dispositions are
byte-intact; the full gate suite is green at the 79-promotion state,
including the new standing checker `scripts/c11_batch2_verdict_check.py`.
No unratified promotion occurred: every promoted identity traces to an
operator verdict row. Batch 3 (S1 remainder 4CH1-1.37–1.60C) is the next
commissionable batch; the consolidated cross-slice boundary ruling comes
before phase 2 (S3).)
> **Session-51 update (2026-09-12): batch 3 AUTHORED to its operator gate —
> the full S1 remainder.** Commissioned by the operator's move-forward
> directive (batch 3 = 4CH1-1.37–1.60C + the Paper-2 mark schemes; "Reuse
> the established Batch 1/Batch 2 machinery"): extraction_pass
> c11-s16-batch-3 (24 SPs + practical PR-04), decision record
> `scripts/c11_batch3_decisions.yaml` — 24 nodes (20 CONCEPT + 4
> misconception: 1 examiner-tip ERRONEOUS_BELIEF + 3 mark-scheme
> WRONG_ANSWER_PATTERN), 39 authored edges (all SUGGESTED, zero RR; 6
> cross-boundary edges into batch-2 nodes; the store's FIRST RELATED_TO +
> second COMMONLY_CONFUSED_WITH deployments), 14 held candidates; 3
> Paper-2 MS pinned (IONIC/COVALENT/CFEC — FN-B2-1 closed; PMT publishes no
> metallic-bonding/electrolysis MS, recorded not silent). Merged store:
> 91 nodes / 220 edges (97 PART_OF + 123 semantic) / 60 command kinds /
> 79 HUMAN_VALIDATED unchanged (authoring promotes nothing). The review
> gate: `graph/reports/C11_BATCH3_REVIEW_SHEET.md` + the verdict template
> `scripts/c11_batch3_verdicts_template.yaml`; NOTHING from batch 3 is
> promoted, promotable-before-verdicts, or HUMAN_VALIDATED. The §18
> front-end lists the 39 batch-3 SUGGESTED edges as the pending actionable
> surface (39 / 5 not-actionable / promo_count=79). Section 1 coverage is
> now COMPLETE (pilot + batches 1–3 = all 60 S1 SPs).
> **Session-52 update (2026-09-13): batch 3 GATE SETTLED — verdicts recorded
> and applied; store total 118.** The operator authorized moving forward
> rather than reopening another prolonged review cycle and applied the
> practical-review policy per row (verbatim policy fragments recorded in
> `scripts/c11_batch3_verdicts.yaml` meta.operator_ruling; "My verdict file
> is that operator authorization."): 39 edge CONFIRM / 24 node CONFIRM /
> 7 identity decisions KEEP_AS_IS / 14 held acknowledged (clean quarantine —
> "A clean quarantine is preferable to inventing evidence"). Encoded
> fail-closed (`scripts/c11_verdict_encode_batch3.py` — pre-state
> reconciliation: 39 SUGGESTED triples, zero RR, 24 node codes, 14 held,
> 79-HV frozen pre-verdict store, §16 AUTHORIZED, all-operator attribution),
> then applied through the exact session-48/50 sanctioned shape: §7
> re-authoring (header note only — no RR settlement, no ENRICHMENT node, no
> MERGE/SPLIT; generator re-run byte-identical) + §18 (bundle
> `graph/reports/C11_DIFF_REVIEW_B3_2026-09-13.md` → approve --all --by
> operator → ONE c11_promote.py invocation → 39 promotions, all operator,
> 2026-09-13). The store now carries 118 HUMAN_VALIDATED (28 pilot + 28
> batch-1 + 23 batch-2 + 39 batch-3), every promoted identity tracing to an
> operator verdict row; the only SUGGESTED semantic edges left are the 3
> pilot operator HOLDs; both RR edges keep their operator settlements; the
> frozen pilot + batch-1 + batch-2 dispositions are byte-intact; the full
> gate suite is green at the 118-promotion state, including the new standing
> checker `scripts/c11_batch3_verdict_check.py` (32 checks). No unratified
> promotion occurred. SECTION 1 IS FULLY SETTLED: coverage complete (60/60
> SPs) and all three expansion batches gated + applied. Next: batch 4 =
> Section 3 Physical Chemistry (22 SPs, 15 T-C10-validated notes; the
> cross-slice boundary ruling recorded before/alongside its authoring);
> T-C11 no longer gates the broader SyllabAI development — phase 2 /
> learner-facing KG behavior / misconception-aware recommendations / pilot
> readiness proceed per the operator's exit directive.)
> **Session-52 addendum (2026-09-13): batch 4 COMMISSIONED + STARTED — the
> cross-slice boundary ruling recorded.** Per the operator's directive
> ("Batch 4 = Section 3 — Physical Chemistry. Use the established
> machinery." + "Resolve only the boundary decisions necessary to prevent
> duplicate or conflicting concepts between the completed Section 1 graph
> and Section 3. Do not turn this into another large ontology exercise."):
> `scripts/c11_batch4_boundary_ruling.yaml` records the scoped ruling —
> the machine-verified conflict audit (the S3 candidate term vocabulary
> vs the whole merged S1 store: ZERO canonical conflicts), the mint
> discipline for S3's new families, the 5 sanctioned boundary-edge targets
> (CON-MOLE, CON-COVALENT-BOND, CON-CONCENTRATION, CON-EQ-SYMBOL,
> CON-WATER-CRYST — ownership exact, boundary MINTING forbidden), and the
> explicit non-goals (no ontology redesign, no re-scope, no promotion
> authority). Standing checker `scripts/c11_batch4_boundary_check.py` ALL
> PASS (the zero-conflict audit re-runs on the live store; targets exist
> with exact ownership; the ruling mints nothing). The S3 Paper-2 mark
> schemes are pinned (`scripts/c11_ms_pin_batch4.py` →
> ENERGETICS_MS_P2.txt 6 pp / RATES_MS_P2.txt 2 pp / RRE_MS_P2.txt 3 pp —
> all three S3 families have Paper-2 MS, so unlike batches 1-3 no family
> is left without MS coverage; the pins carry Reject/Ignore
> misconception-evidence classes). Evidence base inventoried: 15 T-C10
> HUMAN_VALIDATED-mapped notes covering all 22 S3 SPs (energetics 6,
> rates 6, equilibria 3). The batch-4 authoring (extraction_pass
> c11-s16-batch-4 → decision record → registry extension → pass-2 → the
> operator gate) is the NEXT session's commission, with this ruling as its
> standing boundary constraint.
