# C11 Projection-Review Verdict — the operator's gate on the 2026-09-30 promotion sheet

**Date:** 2026-10-01 (Asia/Dhaka session) · **Operator trace:** `1a0f3c31c0cc39b1` · **Reviewed artifact:** the T-C11 promotion review sheet delivered 2026-09-30 (chat artifact, trace `1a0f296108678439`; companion to syllabai-core PR #37 `87e4869`/`0522b08` + syllabai-hub PR #12 `3cb07b4`/`b14af50` — the "12 skipped required-practical edges" drawability fix). This document is that sheet's durable successor: the sandbox lost the original file, so the verdict below was re-grounded against the store before recording.

**Verification pins:** syllabai-core deployed store `src/main/resources/concept-graph/` at origin/main `0522b08` (stage `pilot+s16-batch-1..4`, 275 edges: 153 HUMAN_VALIDATED incl. 112 REQUIRES_PREREQUISITE); syllabai-resources canonical store at origin/main `451d6c4` (stage `pilot+s16-batch-1..11`, 488 edges: 389 HUMAN_VALIDATED incl. 206 REQUIRES_PREREQUISITE + 117 PART_OF). Reconstruction scripts: session workspace `scripts/kg_state_compare.py`, `scripts/kg_projection_verify.py`, `scripts/kg_anchor_evidence.py`, `scripts/kg_practical_evidence.py`.

---

## 1. The operator's verdict (recorded verbatim, per-pair)

### §5.4 — the 8 order anomalies

| # | Pair | Decision | Operator reason (verbatim intent preserved) |
|---|---|---|---|
| 1 | **1.3 → 1.2** | **GO — keep** | Likely spiral dependency: diffusion/dilution feeding states-of-matter vocabulary. Not an evidence failure; the anomaly is ordering, not absence of the underlying concept relation. |
| 2 | **1.10 → 1.5C** | **GO — keep** | Likely intentional spiral: formal solubility/saturation treatment occurs later than the earlier solubility surface. |
| 3 | **1.10 → PR-01** | **GO — keep** | Classic **pre-lab/post-lab spiral**: the practical occurs before the formal saturation treatment. Not to be "corrected" merely to make numeric order monotonic. |
| 4 | **1.28 → 1.26** | **NO-GO for promotion as currently anchored** | Needs evidence inspection around the anchor. Exactly the case where an anchor could be misplaced; if evidence belongs to another SP, fix the `PART_OF` anchor rather than minting/promoting a new prerequisite edge. |
| 5 | **1.33 → 1.32** | **NO-GO for promotion as currently anchored** | Same gas-test-family issue. Numeric inversion alone isn't fatal, but evidence-level inspection is called for. |
| 6 | **1.33 → 1.31** | **NO-GO for promotion as currently anchored** | Strongest of the 1.31–1.33 cluster candidates for an anchor-placement problem; inspect the underlying concept evidence before settling it. |
| 7 | **3.14C → 3.12** | **NO-GO for promotion as currently anchored** | Energy-change/bond-energy calculation ordering needs evidence inspection. Do not encode the inversion as a new authoritative relationship merely because the projection produces it. |
| 8 | **3.14C → 3.13** | **NO-GO for promotion as currently anchored** | Same family and same concern as #7. Verify the concept→SP anchor before accepting the structural interpretation. |

**Gate summary per the verdict table: 3 KEEP AS DERIVED (#1–#3) · 5 HOLD — NO-GO for any promotion until anchor evidence is checked (#4–#8).** Deliberately conservative.

### §5.5 — the five no-basis practicals

**PR-05: NO-GO · PR-06: NO-GO · PR-07: NO-GO · PR-08: NO-GO · PR-12: NO-GO** — from this review sheet. The sheet does not contain the evidence needed to promote them. This is not a ruling that these practicals should never receive prerequisite edges.

**Reason:** do not invent prerequisite edges from practical proximity, curriculum order, or semantic similarity. `REQUIRES_PREREQUISITE` is an educational relation requiring governed evidence; the canonical architecture distinguishes authoritative educational relations from retrieval-derived relationships.

**Authorized next step:** **Batch-5 prerequisite authoring: GO. Batch-5 promotion itself: NO-GO until that authoring/evidence pass is reviewed.**

### The 132 concept-backed pairs

**The 132 projected SP pairs remain read-model projections with `derived` provenance** — not duplicate T-C11 records. The read-model projection proceeds (it is live: core PR #37 + hub PR #12).

**Bottom line (operator, verbatim):** "I would **not promote any new settled T-C11 edge from this review**. The read-model projection can proceed; the five practical gaps should proceed to **Batch-5 authoring**, not straight to promotion."

---

## 2. Verification — every sheet figure re-derives from the deployed store

The projection was reconstructed independently (concept-level HUMAN_VALIDATED REQUIRES_PREREQUISITE edges projected onto Specification Points via the concepts' attachment anchors; practicals project to their `practicals.yaml` spec point; self-pairs collapse; pair notation prerequisite → dependent):

| Sheet figure | Re-derivation | Status |
|---|---|---|
| **132** projected SP pairs | exactly 132 | ✅ exact |
| **13** practical-dependent pairs (validated concept-level bases; "can safely be projected") | exactly 13 (12 store edges; PR-04's two edges converge on one pair, 1.58C → 1.60C) | ✅ exact |
| **8** order anomalies | exactly the 8 inverted-order pairs of the projection | ✅ exact |
| **22** inferred-only pairs | the three weak-basis classes counted per-row: 13 practical-dependent + 8 inverted + 1 non-CORE-anchored = **22 row-reviews** (20 distinct pairs — `1.10 → 1.7C` carries all three flags) | ✅ reconciled |
| the other **110** pairs | order-respecting, CORE-anchored, concept-only → the "remain derived" body | ✅ 132 − 22 = 110 |

The 8 anomalies decompose by cause (facts from the store; dispositions remain the operator's):

- **#1, #2, #3 (KEEP)** — each traces to a SUPPORTING-role secondary anchor: CON-STATE-PARTICLE-MODEL at 1.3 [SUPPORTING] (its CORE anchor is 1.1); CON-SATURATED-SOLUTION at 1.10 [SUPPORTING] (CORE 1.4). The spirals the operator confirmed are real features of the anchor set, not projection bugs.
- **#4 (1.28 → 1.26), #5 (1.33 → 1.32)** — **dual-CORE shadow artifacts**: both endpoint concepts carry CORE attachments at BOTH SPs (CON-MR {1.26,1.28}, CON-AR {1.26,1.28}; CON-MOLECULAR-FORMULA {1.32,1.33}, CON-EMPIRICAL-FORMULA {1.32,1.33}), so the projection necessarily emits both the order-respecting twin (1.26→1.28, 1.32→1.33) and the inverted shadow. The concept-level edges themselves are pedagogically sound (Mr requires Ar; molecular requires empirical). The store fact supersedes the sheet's prose guess ("ionic equations vs halide testing") — the 1.26/1.28 pair is Mr/Ar.
- **#6 (1.33 → 1.31)** — the **genuine single-chain inversion**: CON-WATER-CRYST anchored only at 1.31 (CORE), CON-EMP-MOL-CALC only at 1.33 (CORE), and the settled edge runs WATER-CRYST REQUIRES EMP-MOL-CALC, making the later SP the prerequisite of the earlier one. This is the strongest anchor-placement candidate, exactly as the operator flagged; its resolution (edge direction vs. re-anchoring vs. accept-as-post-hoc-dependency) belongs to the next evidence pass.
- **#7, #8 (3.14C → 3.12 / 3.13)** — **edge-direction inversions at SP level**: CON-ACTIVATION-ENERGY is CORE-anchored only at 3.14C; CON-CATALYST at 3.12+3.13; the settled edge runs CATALYST REQUIRES ACTIVATION-ENERGY. The concept edge is HUMAN_VALIDATED and sound (catalyst mechanism presupposes activation energy); the SP-level inversion exists because the spec formalizes activation energy (3.14C) after catalyst knowledge (3.12/3.13). HOLD stands: never encode the inversion as a new authoritative SP relation.

**Consequence of #4–#8 HOLD:** none of the 8 inverted pairs may enter any settled store from this review. For the 4 artifact/shadow pairs the future fix, if any, is anchor-role refinement (a dual-CORE secondary attachment demoted to ENRICHMENT/SUPPORTING) — never a new prerequisite edge. No anchor was modified in this round (that is evidence-pass work, operator-gated).

---

## 3. §5.5 ground-truth reconciliation — the "no-basis" practicals DO have an authored, promoted basis in this repo

The sheet's §5.5 premise ("no existing prerequisite basis") was **true of the DEPLOYED core store only**. In THIS repo (the T-C11 pipeline home) the authoring the operator just authorized already exists — batches 5/6/7/11 covered exactly those five practicals, and the edges went through the §18 diff-review + promotion pathway:

| Edge | Batch | Derivation | Evidence (NOTE quotes) | Promoted |
|---|---|---|---|---|
| PR-05 REQUIRES CON-O2-PERCENT-DETERMINATION | 5 | USED_WITHOUT_RETEACHING | "To determine the percentage of oxygen in air using the oxidation of iron"; "percentage of oxygen =" | 2026-09-22, `C11_DIFF_REVIEW_B5_2026-09-22.md` |
| PR-06 REQUIRES CON-REACT-ARRANGE | 6 | USED_WITHOUT_RETEACHING | "To investigate the reactions between dilute hydrochloric and sulfuric acids with the metals magnesium, iron and zinc"; "The metals can be ranked in reactivity order Mg > Zn > Fe" | 2026-09-22, `C11_DIFF_REVIEW_B6_2026-09-22.md` |
| PR-07 REQUIRES CON-SALT-INSOLUBLE-REACTANT | 7 | USED_WITHOUT_RETEACHING | "To prepare a pure, dry sample of hydrated copper(II) sulfate crystals"; "Add the copper(II) oxide slowly to the hot dilute acid and stir until the base is in excess…" | 2026-09-23, `C11_DIFF_REVIEW_B7_2026-09-23.md` |
| PR-08 REQUIRES CON-SALT-PRECIPITATION | 7 | USED_WITHOUT_RETEACHING | "The solid salt obtained is the precipitate…"; "Filter to remove precipitate from mixture" | 2026-09-23, `C11_DIFF_REVIEW_B7_2026-09-23.md` |
| PR-12 REQUIRES CON-ESTERS | 11 | EXPLICIT_TEACH_SEQUENCE | "To prepare a small sample of ethyl ethanoate" | 2026-09-25, `C11_DIFF_REVIEW_B11_2026-09-25.md` |
| PR-12 REQUIRES CON-SIMPLE-DISTILLATION | 11 | USED_WITHOUT_RETEACHING | "The ester is then distilled off as soon as it is formed and collected in a separate beaker by condensation" (sanctioned boundary edge, session-66 ruling TARGET-5) | 2026-09-25, `C11_DIFF_REVIEW_B11_2026-09-25.md` |
| PR-12 REQUIRES CON-ACID-REACTIONS | 11 | USED_WITHOUT_RETEACHING | "To remove acidic impurities, sodium carbonate solution can be added, until the mixture stops fizzing…" (sanctioned boundary edge, session-66 ruling TARGET-6) | 2026-09-25, `C11_DIFF_REVIEW_B11_2026-09-25.md` |

Each carries its upstream T-C10 HUMAN_VALIDATED anchors (2.14/2.10, 2.21/2.15, 2.42/2.39, 2.43C/2.41C, 4.43C/4.39C) and follows the established practical-edge patterns (PR-01→CON-SATURATED-SOLUTION / PR-04→CON-ELECTROLYSIS shapes). Full evidence blocks: session workspace `tc17-work/c11-probe/practical_batch5_evidence.json` (extracted from `scripts/c11_batch{5,6,7,11}_decisions.yaml`).

**Naming collision recorded honestly:** the sheet's "Batch-5 pass" was numbered against the DEPLOYED store's stage line (`pilot+batch-1..4` → next = 5). This repo's batch 5 is the Section-2 slice (which is itself where PR-05's edge was authored). The material content the sheet proposed — authored, evidence-backed concept-level prerequisite edges for PR-05/06/07/08/12 — is complete: **7 edges across batches 5/6/7/11.** Re-authoring them would create duplicate records, which the operator's own ruling forbids ("rather than becoming duplicate T-C11 records").

**Coverage observation for the review round (not fixed here):** PR-05/06/07/08 carry exactly one edge each (the "investigation-of" basis) and PR-12 three, whereas the deployed practicals carry 1–2 each including method-ground edges. Whether the five deserve additional USED_WITHOUT_RETEACHING edges (e.g. PR-07 → CON-CRYSTALLISATION-class method concepts) is a scope decision for the authoring review — to be decided on evidence, never on proximity or similarity.

---

## 4. Gate consequences as executed this round

1. **NO promotion executed anywhere.** `scripts/c11_promotions.yaml` untouched; no verdict encode; no generator re-run; no core sync.
2. **The deployed core store stays at batch-4.** The 119 HUMAN_VALIDATED edges that exist here but are not deployed (7 practical-origin + 112 concept→concept from batches 5–11) remain undeployed. The core sync (regenerate `concept_edges.yaml` from `graph/igcse-chemistry/` → core PR → seed) is now THE operator gate through which the "Batch-5 promotion NO-GO" is enforced: it happens only after the operator reviews the §3 authoring package.
3. **The 132 projections stay derived** in the live read model (core PR #37 / hub PR #12), flagged `derived=true` with `derivedViaConceptCodes` — teachers and the operator can always distinguish projected pairs from settled ones.
4. **#1–#3 remain derived** — no action, recorded as confirmed intentional spirals.
5. **#4–#8 remain HOLD** — the anchor-evidence facts are in §2; the resolution pass (anchor-role refinement for the 4 shadows; the #6 direction/anchor decision) is the next operator-gated evidence work.
6. **Batch-5 authoring = materially complete** (§3); the review of that authoring evidence is the pending operator action. The evidence package is §3 of this document plus the JSON extract; nothing further was authored this round.

## 5. Appendix A — the 22 weak-basis rows (flags: P=practical-dependent, I=inverted, N=non-CORE-anchored)

```text
#  pair (prereq -> dep)    flags  via store edge(s)
1  4CH1-1.10 -> 4CH1-1.13  P      PR-02 => CON-CHROMATOGRAPHY
2  4CH1-1.10 -> 4CH1-1.7C  P,I,N  PR-01 => CON-SATURATED-SOLUTION   [the #3 KEEP spiral]
3  4CH1-1.12 -> 4CH1-1.13  P      PR-02 => CON-RF-VALUE
4  4CH1-1.31 -> 4CH1-1.36  P      PR-03 => CON-EXP-FORMULA-DEDUCTION
5  4CH1-1.4  -> 4CH1-1.7C  P      PR-01 => CON-SATURATED-SOLUTION
6  4CH1-1.58C-> 4CH1-1.60C P      PR-04 => CON-AQUEOUS-DISCHARGE; PR-04 => CON-ELECTROLYSIS
7  4CH1-1.5C -> 4CH1-1.7C  P      PR-01 => CON-SOLUBILITY
8  4CH1-3.10 -> 4CH1-3.15  P      PR-10 => CON-RATE-FACTORS
9  4CH1-3.12 -> 4CH1-3.16  P      PR-11 => CON-CATALYST
10 4CH1-3.13 -> 4CH1-3.16  P      PR-11 => CON-CATALYST
11 4CH1-3.2  -> 4CH1-3.8   P      PR-09 => CON-CALORIMETRY
12 4CH1-3.9  -> 4CH1-3.15  P      PR-10 => CON-RATE-EXPERIMENTS
13 4CH1-3.9  -> 4CH1-3.16  P      PR-11 => CON-RATE-EXPERIMENTS
14 4CH1-1.3  -> 4CH1-1.2   I      CON-STATE-CHANGES => CON-STATE-PARTICLE-MODEL   [#1 KEEP spiral]
15 4CH1-1.10 -> 4CH1-1.5C  I      CON-SOLUBILITY => CON-SATURATED-SOLUTION         [#2 KEEP spiral]
16 4CH1-1.28 -> 4CH1-1.26  I      CON-MR => CON-AR          [#4 HOLD — dual-CORE shadow]
17 4CH1-1.33 -> 4CH1-1.32  I      CON-MOLECULAR-FORMULA => CON-EMPIRICAL-FORMULA   [#5 HOLD — dual-CORE shadow]
18 4CH1-1.33 -> 4CH1-1.31  I      CON-WATER-CRYST => CON-EMP-MOL-CALC              [#6 HOLD — genuine single-chain inversion]
19 4CH1-3.14C-> 4CH1-3.12  I      CON-CATALYST => CON-ACTIVATION-ENERGY            [#7 HOLD — edge-direction inversion]
20 4CH1-3.14C-> 4CH1-3.13  I      CON-CATALYST => CON-ACTIVATION-ENERGY            [#8 HOLD — edge-direction inversion]
(21–22: rows 2 and 16–20 re-flagged across classes — 22 row-reviews, 20 distinct pairs)
```

The full 132-pair table regenerates deterministically: `python3 scripts/kg_projection_verify.py` (session workspace; inputs = the deployed store YAMLs at the pinned revisions).
