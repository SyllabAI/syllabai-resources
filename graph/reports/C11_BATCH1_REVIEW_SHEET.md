# T-C11 §16 Batch 1 Review Sheet — Concept / Prerequisite / Misconception Graph

Slice 4CH1-1.1–1.12 (S1 remainder, first 12 SPs) · generated 2026-09-12 · decision record `scripts/c11_batch1_decisions.yaml` (pass 1: `c11-s16-batch-1`) · adversarial pass 2: `scripts/c11_batch1_review_pass2.yaml` · authorization: `scripts/c11_s16_authorization.yaml` (§16 authorized 2026-09-12; batch 1 commissioned by the operator, session 47)

**NOTHING in this batch is authoritative.** All 24 nodes / 53 batch edges are AI_SUGGESTED (SUGGESTED or REVIEW_REQUIRED). HUMAN_VALIDATED is reachable only by your promotion command via the §18 pathway (`scripts/c11_promote.py` → `scripts/c11_promotions.yaml` → gated generator re-run). **Zero batch-1 promotions exist.** This sheet is the batch's operator gate: record verdicts in `scripts/c11_batch1_verdicts_template.yaml` (fill + rename to `c11_batch1_verdicts.yaml`); a later session encodes and applies them.

How to review: for each row check the quoted evidence actually appears in the cited file and actually says what the record claims; then rule on the relation CLASS and direction, not just existence. Machine state: the full gate suite is green at the merged 53-node / 118-edge store; every quote is machine-verified byte-for-byte against its source file (G03/c11.4); the 4.15 negative control is uncovered.

## 1. Totals & second-pass agreement

| | nodes | authored edges | held | |
|---|---|---|---|
| pass-1 (extraction) | 24 | 29 (+24 derived PART_OF) | 12 |
| pass-2 verdicts | 24 CONFIRM(+note) | 28 CONFIRM(+note) · 1 HOLD · 0 REJECT | all 12 AGREE |

Raw agreement (NOT κ — single human rater, architecture §12): nodes 24/24 = 100.0%; edges — of the 28 edges pass-1 asserted (SUGGESTED), pass-2 confirmed 28 (100.0%); pass-1 quarantined 1 edge as REVIEW_REQUIRED, concordantly HOLD by pass 2. **Zero pass-2 demotions** — the abstention happened at authoring (12 held + 1 self-quarantine) rather than as pass-2 attack fallout; the adversarial findings land as CONFIRM_WITH_NOTE flags (§5).

Forecast calibration (C11_BATCH_FORECAST.json future_batch_records): predicted 28.8 nodes / 33 edges / 12 held vs actual 24 / 29 / 12 — nodes −16.7%, edges −12.1%, held 0.0% (terminology-heavy slice, lighter on procedures than the calculation-heavy pilot).

## 2. Concept & misconception nodes (24)

| # | code | family | title | attaches to (role) | conf | evidence (anchor → quote) | pass-2 | operator |
|---|---|---|---|---|---|---|---|---|
| 1 | `4CH1-CON-STATES-THREE` | CONCE | The three states of matter (solid, liquid, gas) | 4CH1-1.1 (core) | high | NOTE: “The three states of matter are solids, liquids and gases” | CONFIRM_WITH_NOTE | ☐ |
| 2 | `4CH1-CON-STATE-PARTICLE-MODEL` | CONCE | Particle arrangement, movement and energy in the three states | 4CH1-1.1 (core); 4CH1-1.3 (supp) | high | NOTE: “In this model, the particles are represented by small solid spheres” | CONFIRM_WITH_NOTE | ☐ |
| 3 | `4CH1-CON-STATE-CHANGES` | CONCE | Interconversions between the three states (melting, freezing, boiling, condensation, sublimation) | 4CH1-1.2 (core) | high | NOTE: “State changes occur at the melting point (solid to liquid, liquid to solid) and at the boiling point” | CONFIRM | ☐ |
| 4 | `4CH1-CON-EVAPORATION-BOILING` | CONCE | Evaporation and its distinction from boiling | 4CH1-1.2 (enri) | high | NOTE: “Evaporation occurs over a range of temperatures” | CONFIRM_WITH_NOTE | ☐ |
| 5 | `4CH1-CON-DIFFUSION` | CONCE | Diffusion in gases and liquids | 4CH1-1.3 (core) | high | NOTE: “Diffusion occurs in gases and liquids, due to the random motion of their particles” | CONFIRM | ☐ |
| 6 | `4CH1-CON-DILUTION` | CONCE | Dilution of coloured solutions | 4CH1-1.3 (core) | high | NOTE: “Dilution is the process of adding more solvent (usually water) to a solution” | CONFIRM | ☐ |
| 7 | `4CH1-CON-SOLUTION` | CONCE | Solution, solute and solvent | 4CH1-1.4 (core) | high | NOTE: “The liquid in which a solute dissolves” | CONFIRM_WITH_NOTE | ☐ |
| 8 | `4CH1-CON-SATURATED-SOLUTION` | CONCE | Saturated solution | 4CH1-1.4 (core); 4CH1-1.10 (supp) | high | NOTE: “A solution with the maximum concentration of solute dissolved in the solvent” | CONFIRM | ☐ |
| 9 | `4CH1-CON-SOLUBILITY` | CONCE | Solubility (g per 100 g of solvent) | 4CH1-1.5C (core) | high | NOTE: “Solubility is a measurement of how much of a substance will dissolve in a given volume of a liquid” | CONFIRM | ☐ |
| 10 | `4CH1-CON-SOLUBILITY-CURVE` | CONCE | Solubility curves (plotting and interpreting) | 4CH1-1.6C (core) | high | NOTE: “Solubility graphs or curves represent solubility in g per 100 g of water plotted against temperature” | CONFIRM | ☐ |
| 11 | `4CH1-CON-HEATING-CONSTANT-MASS` | CONCE | Heating to constant mass | 4CH1-1.7C (enri) | high | NOTE: “Repeat this process until the mass remains constant” | CONFIRM_WITH_NOTE | ☐ |
| 12 | `4CH1-CON-ELEMENT` | CONCE | Element | 4CH1-1.8 (core) | high | NOTE: “A substance made of atoms that all contain the same number of protons and cannot be split into anyth” | CONFIRM | ☐ |
| 13 | `4CH1-CON-COMPOUND` | CONCE | Compound | 4CH1-1.8 (core) | high | NOTE: “A pure substance made up of two or more different elements chemically combined” | CONFIRM | ☐ |
| 14 | `4CH1-CON-MIXTURE` | CONCE | Mixture | 4CH1-1.8 (core) | high | NOTE: “A combination of two or more substances (elements and/or compounds) that are not chemically combined” | CONFIRM | ☐ |
| 15 | `4CH1-CON-PURE-SUBSTANCE` | CONCE | Pure substance (chemical sense) and fixed melting/boiling points | 4CH1-1.9 (core) | high | NOTE: “In chemistry, a pure substance may consist of a single element or compound which contains no other s” | CONFIRM_WITH_NOTE | ☐ |
| 16 | `4CH1-CON-SIMPLE-DISTILLATION` | CONCE | Simple distillation | 4CH1-1.10 (core) | high | NOTE: “Simple distillation is used to separate a liquid and soluble solid from a solution” | CONFIRM | ☐ |
| 17 | `4CH1-CON-FRACTIONAL-DISTILLATION` | CONCE | Fractional distillation | 4CH1-1.10 (core) | high | NOTE: “Fractional distillation is used to separate two or more liquids that are miscible with one another” | CONFIRM | ☐ |
| 18 | `4CH1-CON-FILTRATION` | CONCE | Filtration | 4CH1-1.10 (core) | high | NOTE: “Filtration is used to separate an undissolved solid from a mixture of the solid and a liquid / solut” | CONFIRM | ☐ |
| 19 | `4CH1-CON-CRYSTALLISATION` | CONCE | Crystallisation | 4CH1-1.10 (core) | high | NOTE: “Crystallisation is used to separate a dissolved solid from a solution, when the solid is much more s” | CONFIRM | ☐ |
| 20 | `4CH1-CON-CHROMATOGRAPHY` | CONCE | Paper chromatography (separation by differential solubility) | 4CH1-1.10 (core) | high | NOTE: “Paper chromatography is used to separate substances that have different solubilities in a given solv” | CONFIRM | ☐ |
| 21 | `4CH1-CON-CHROMATOGRAM-INTERPRETATION` | CONCE | Interpreting chromatograms | 4CH1-1.11 (core) | high | NOTE: “We can use a chromatogram to compare the substances present in a mixture to known substances and mak” | CONFIRM | ☐ |
| 22 | `4CH1-CON-RF-VALUE` | CONCE | Retention factor (Rf) | 4CH1-1.12 (core) | high | NOTE: “The retention factor, Rf, is calculated by the equation:” | CONFIRM | ☐ |
| 23 | `4CH1-MIS-GAS-PARTICLES-TOUCH` | MISCO | Drawing gas particles touching each other or joined by bonds | — | high | MARK_SCHEME: “Reject any touching circles”<br>remediation: “the particles in a gas are far apart and moving quickly and randomly” | CONFIRM | ☐ |
| 24 | `4CH1-MIS-CRYSTALLISATION-DRYNESS` | MISCO | Obtaining crystals by evaporating to dryness | — | high | MARK_SCHEME: “If evaporated to dryness then award no marks for whole question”<br>remediation: “The solution is heated, allowing the solvent to evaporate, leaving a saturated s” | CONFIRM | ☐ |

Identity-policy notes (split-first; merges are operator-only, OD-1 operand rule): pass-2 flags the CON-STATES-THREE / CON-STATE-PARTICLE-MODEL pair (merge candidate), the CON-SOLUTION triple-node (split option) and CON-PURE-SUBSTANCE (definition + criterion in one node). All are operator identity decisions (template §identity_decisions).

## 3. Authored semantic edges (29)

Direction conventions: REQUIRES_PREREQUISITE source=dependent → target=prerequisite; EXPLAINED_BY explained → explainer; REMEDIATED_BY misconception → concept.

### 3.1 REVIEW_REQUIRED (open operator decision)

| edge | conf | evidence | ambiguity (pass-1 self-review) | pass-2 | operator |
|---|---|---|---|---|---|
| `4CH1-CON-CRYSTALLISATION` **REQUIRES_PREREQUISITE** `4CH1-CON-SOLUTION` | medium | “Crystallisation is used to separate a dissolved solid from a solution, when the solid is much more s” | Transitively subsumed via CRYSTALLISATION -> SATURATED-SOLUTION -> SOLUTION; the load-bearing prerequisite (saturation) is already emitted — this vocabulary-level edge adds density without new reviewable information unle | HOLD: Pass-1 already quarantined this to REVIEW_REQUIRED at authoring (subsumption class: CRYSTALLISATION -> SATURATED-SOLUTION -> SOLUTION). Pass 2 agrees with the doubt and would not emit it as SUGGESTED: | ☐ |

### 3.2 SUGGESTED edges (28) — the §18- promotable surface after verdicts

Flagged rows (pre-triage FLAGGED in the verdict template): the relation-class choice on DIFFUSION EXPLAINED_BY (B1-H-04), the symmetric-operand options (B1-H-01/B1-H-10), the vocabulary-level technique→solution class (FP-B1-4), and the MIS-GAS remediation-target pattern.

| edge | method | conf | evidence (quote) | upstream | pass-2 | operator |
|---|---|---|---|---|---|---|
| `4CH1-CON-CHROMATOGRAM-INTERPRETATION` **REQUIRES_PREREQUISITE** `4CH1-CON-CHROMATOGRAPHY` | EXAMINER_TIP_EXPLICIT | high | “Paper chromatography is the name given to the overall separation technique while a chromatogram is t” | T-C10 HUMAN_VALIDATED 4CH1-1.10 @ Separation techniques (2026-09-11); 1.11 note | CONFIRM | ☐ |
| `4CH1-CON-CHROMATOGRAM-INTERPRETATION` **REQUIRES_PREREQUISITE** `4CH1-CON-PURE-SUBSTANCE` | USED_WITHOUT_RETEACHING | high | “Pure substances will produce only one spot on the chromatogram” | T-C10 HUMAN_VALIDATED 4CH1-1.11 @ Interpreting chromatograms (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-CHROMATOGRAPHY` **REQUIRES_PREREQUISITE** `4CH1-CON-SOLUBILITY` | USED_WITHOUT_RETEACHING | high | “Those substances with higher solubility will travel further than the others” | T-C10 HUMAN_VALIDATED 4CH1-1.10 @ Separation techniques (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-COMPOUND` **REQUIRES_PREREQUISITE** `4CH1-CON-ELEMENT` | DEFINITIONAL_DEPENDENCY | high | “A pure substance made up of two or more different elements chemically combined” | T-C10 HUMAN_VALIDATED 4CH1-1.8 @ Element, Compound or Mixture (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-CRYSTALLISATION` **EXPLAINED_BY** `4CH1-CON-SOLUBILITY` | SINGLE_SOURCE_CAUSAL_TEACHING | high | “Crystals begin to grow as solids will come out of solution due to decreasing solubility” | T-C10 HUMAN_VALIDATED 4CH1-1.10 @ Separation techniques (2026-09-11); 1.5C relation fro... | CONFIRM | ☐ |
| `4CH1-CON-CRYSTALLISATION` **REQUIRES_PREREQUISITE** `4CH1-CON-SATURATED-SOLUTION` | USED_WITHOUT_RETEACHING | high | “The solution is heated, allowing the solvent to evaporate, leaving a saturated solution behind” | T-C10 HUMAN_VALIDATED 4CH1-1.10 @ Separation techniques (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-DIFFUSION` **EXPLAINED_BY** `4CH1-CON-STATE-PARTICLE-MODEL` ⚑ | SINGLE_SOURCE_CAUSAL_TEACHING | high | “Diffusion occurs in gases and liquids, due to the random motion of their particles” | T-C10 HUMAN_VALIDATED 4CH1-1.3 @ Diffusion (2026-09-11) | CONFIRM_WITH_NOTE | ☐ |
| `4CH1-CON-DILUTION` **EXPLAINED_BY** `4CH1-CON-STATE-PARTICLE-MODEL` | SINGLE_SOURCE_CAUSAL_TEACHING | high | “This indicates that there are a lot of particles in a small amount of potassium manganate (VII) and ” | T-C10 HUMAN_VALIDATED 4CH1-1.3 @ Diffusion (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-EVAPORATION-BOILING` **REQUIRES_PREREQUISITE** `4CH1-CON-STATE-CHANGES` | DEFINITIONAL_DEPENDENCY | high | “It can happen at temperatures below the boiling point of the liquid” | T-C10 HUMAN_VALIDATED 4CH1-1.2 @ Changing states of matter (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-FILTRATION` **REQUIRES_PREREQUISITE** `4CH1-CON-SOLUTION` ⚑ | USED_WITHOUT_RETEACHING | high | “Filtration is used to separate an undissolved solid from a mixture of the solid and a liquid / solut” | T-C10 HUMAN_VALIDATED 4CH1-1.10 @ Separation techniques (2026-09-11) | CONFIRM_WITH_NOTE | ☐ |
| `4CH1-CON-FRACTIONAL-DISTILLATION` **REQUIRES_PREREQUISITE** `4CH1-CON-SIMPLE-DISTILLATION` | EXPLICIT_TEACH_SEQUENCE | high | “All of the substance is evaporated and collected, leaving behind the other components(s) of the mixt” | T-C10 HUMAN_VALIDATED 4CH1-1.10 @ Separation techniques (2026-09-11) | CONFIRM_WITH_NOTE | ☐ |
| `4CH1-CON-MIXTURE` **REQUIRES_PREREQUISITE** `4CH1-CON-COMPOUND` ⚑ | DEFINITIONAL_DEPENDENCY | high | “A combination of two or more substances (elements and/or compounds) that are not chemically combined” | T-C10 HUMAN_VALIDATED 4CH1-1.8 @ Element, Compound or Mixture (2026-09-11) | CONFIRM_WITH_NOTE | ☐ |
| `4CH1-CON-PURE-SUBSTANCE` **REQUIRES_PREREQUISITE** `4CH1-CON-COMPOUND` ⚑ | DEFINITIONAL_DEPENDENCY | high | “In chemistry, a pure substance may consist of a single element or compound which contains no other s” | T-C10 HUMAN_VALIDATED 4CH1-1.9 @ Pure substances (2026-09-11) | CONFIRM_WITH_NOTE | ☐ |
| `4CH1-CON-PURE-SUBSTANCE` **REQUIRES_PREREQUISITE** `4CH1-CON-STATE-CHANGES` | USED_WITHOUT_RETEACHING | high | “Pure substances melt and boil at specific and sharp temperatures” | T-C10 HUMAN_VALIDATED 4CH1-1.9 @ Pure substances (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-RF-VALUE` **REQUIRES_PREREQUISITE** `4CH1-CON-CHROMATOGRAM-INTERPRETATION` | USED_WITHOUT_RETEACHING | high | “For both measurements, the distance should be measured from the baseline to the centre of the dot.” | T-C10 HUMAN_VALIDATED 4CH1-1.12 @ Interpreting chromatograms (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-SATURATED-SOLUTION` **REQUIRES_PREREQUISITE** `4CH1-CON-SOLUTION` | DEFINITIONAL_DEPENDENCY | high | “A solution with the maximum concentration of solute dissolved in the solvent” | T-C10 HUMAN_VALIDATED 4CH1-1.4 @ Solutions (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-SIMPLE-DISTILLATION` **REQUIRES_PREREQUISITE** `4CH1-CON-SOLUTION` ⚑ | USED_WITHOUT_RETEACHING | high | “Simple distillation is used to separate a liquid and soluble solid from a solution” | T-C10 HUMAN_VALIDATED 4CH1-1.10 @ Separation techniques (2026-09-11) | CONFIRM_WITH_NOTE | ☐ |
| `4CH1-CON-SIMPLE-DISTILLATION` **REQUIRES_PREREQUISITE** `4CH1-CON-STATE-CHANGES` | USED_WITHOUT_RETEACHING | high | “The vapour passes through the condenser, where it cools and condenses, turning into the pure liquid ” | T-C10 HUMAN_VALIDATED 4CH1-1.10 @ Separation techniques (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-SOLUBILITY` **REQUIRES_PREREQUISITE** `4CH1-CON-SATURATED-SOLUTION` | DEFINITIONAL_DEPENDENCY | high | “the maximum mass of solute that can be dissolved in 100 g of water before a saturated solution is fo” | T-C10 HUMAN_VALIDATED 4CH1-1.5C @ Solubility (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-SOLUBILITY-CURVE` **REQUIRES_PREREQUISITE** `4CH1-CON-SOLUBILITY` | DEFINITIONAL_DEPENDENCY | high | “Solubility graphs or curves represent solubility in g per 100 g of water plotted against temperature” | T-C10 HUMAN_VALIDATED 4CH1-1.6C @ Solubility (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-STATE-CHANGES` **REQUIRES_PREREQUISITE** `4CH1-CON-STATE-PARTICLE-MODEL` | USED_WITHOUT_RETEACHING | high | “State changes require a change in the energy of the particles” | T-C10 HUMAN_VALIDATED 4CH1-1.2 @ Changing states of matter (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-STATE-PARTICLE-MODEL` **REQUIRES_PREREQUISITE** `4CH1-CON-STATES-THREE` ⚑ | DEFINITIONAL_DEPENDENCY | high | “The three states of matter can be represented by a simple model” | T-C10 HUMAN_VALIDATED 4CH1-1.1 @ Changing states of matter (2026-09-11) | CONFIRM_WITH_NOTE | ☐ |
| `4CH1-MIS-CRYSTALLISATION-DRYNESS` **REMEDIATED_BY** `4CH1-CON-SATURATED-SOLUTION` | EXPLICIT_TEACH_SEQUENCE | high | “The solution is heated, allowing the solvent to evaporate, leaving a saturated solution behind” | T-C10 HUMAN_VALIDATED 4CH1-1.10 @ Separation techniques (2026-09-11) | CONFIRM | ☐ |
| `4CH1-MIS-CRYSTALLISATION-DRYNESS` **WRONG_ANSWER_PATTERN** `4CH1-CON-CRYSTALLISATION` | ASSESSMENT_DOCUMENTED | high | “If evaporated to dryness then award no marks for whole question” | PMT Unit-1 Paper-1 MS "Elements, Compounds, Mixtures 2" Q1(d) (pinned scripts/c11_evide... | CONFIRM | ☐ |
| `4CH1-MIS-GAS-PARTICLES-TOUCH` **REMEDIATED_BY** `4CH1-CON-STATE-PARTICLE-MODEL` ⚑ | EXPLICIT_TEACH_SEQUENCE | high | “the particles in a gas are far apart and moving quickly and randomly” | T-C10 HUMAN_VALIDATED 4CH1-1.1 @ Changing states of matter (2026-09-11) | CONFIRM_WITH_NOTE | ☐ |
| `4CH1-MIS-GAS-PARTICLES-TOUCH` **WRONG_ANSWER_PATTERN** `4CH1-CON-STATE-PARTICLE-MODEL` | ASSESSMENT_DOCUMENTED | high | “Reject any touching circles” | PMT Unit-1 Paper-1 MS "States of Matter" Q3(a)(i)/Q4(a) (pinned scripts/c11_evidence/SO... | CONFIRM | ☐ |
| `4CH1-PR-01` **REQUIRES_PREREQUISITE** `4CH1-CON-SATURATED-SOLUTION` | USED_WITHOUT_RETEACHING | high | “This ensures that the solution is saturated” | T-C10 HUMAN_VALIDATED 4CH1-1.7C @ Investigating solubility (2026-09-11) | CONFIRM | ☐ |
| `4CH1-PR-01` **REQUIRES_PREREQUISITE** `4CH1-CON-SOLUBILITY` | USED_WITHOUT_RETEACHING | high | “Calculate the solubility of copper(II) sulfate in water at 30°C using the masses recorded” | T-C10 HUMAN_VALIDATED 4CH1-1.7C + 4CH1-1.5C @ Investigating solubility (2026-09-11) | CONFIRM | ☐ |

### 3.3 Derived PART_OF edges (24)

Derived deterministically from node attachments (concepts.yaml); each carries the attachment's evidence anchors and the node's provenance. Not re-listed here — review them via the §2 node rows. Machine-verified: the PART_OF set must exactly equal the declared attachments (c11.7).

## 4. Held / rejected candidates (12) — the abstention record

These were considered and NOT drawn. Review that each hold reason is right (pass-2 already did — column below). Overriding a hold = re-authoring the decision record, never hand-editing the graph. B1-H-06 and B1-H-07 record documented misconception evidence deferred for later passes — the operator may direct their minting.

| id | status | candidate | failing rule | pass-2 | operator |
|---|---|---|---|---|---|
| B1-H-01 | held | REQUIRES_PREREQUISITE(CON-MIXTURE, CON-ELEMENT) | TRANSITIVELY_SUBSUMED | AGREE_HOLD | ☐ |
| B1-H-02 | held | REQUIRES_PREREQUISITE(CON-SOLUBILITY-CURVE, CON-SATURATED-SOLUTION) | TRANSITIVELY_SUBSUMED | AGREE_HOLD | ☐ |
| B1-H-03 | held | REQUIRES_PREREQUISITE(CON-RF-VALUE, CON-CHROMATOGRAPHY) | TRANSITIVELY_SUBSUMED | AGREE_HOLD | ☐ |
| B1-H-04 | held | REQUIRES_PREREQUISITE(CON-DIFFUSION, CON-STATE-PARTICLE-MODEL) — "understanding diffusion presupposes the particle mo... | RELATION_CLASS_PAIR_CONFLICT | AGREE_HOLD | ☐ |
| B1-H-05 | held | COMMONLY_CONFUSED_WITH(CON-PURE-SUBSTANCE, "everyday meaning of pure") | NO_TARGET_NODE_PLUS_WEAK_CLASS | AGREE_HOLD | ☐ |
| B1-H-06 | held | MISCONCEPTION node "crystals form on cooling because particles freeze / join an ionic lattice" MISCONCEPTION_OF CON-C... | TARGET_ALREADY_MINTED | AGREE_HOLD | ☐ |
| B1-H-07 | held | MISCONCEPTION node "condensation explained as particles becoming denser / density change" MISCONCEPTION_OF CON-STATE-... | EVIDENCE_CLASS_WEAK | AGREE_HOLD | ☐ |
| B1-H-08 | held | EXPLAINED_BY(CON-SOLUBILITY, CON-STATE-PARTICLE-MODEL) — "why solids dissolve more at higher temperature" | INSUFFICIENT_EVIDENCE | AGREE_HOLD | ☐ |
| B1-H-09 | held | REQUIRES_PREREQUISITE(PR-01, CON-SOLUBILITY-CURVE) — "plot the results as a solubility curve" | EXCERPT_ONLY_EVIDENCE | AGREE_HOLD | ☐ |
| B1-H-10 | held | REQUIRES_PREREQUISITE(CON-PURE-SUBSTANCE, CON-ELEMENT) | TRANSITIVELY_SUBSUMED | AGREE_HOLD | ☐ |
| B1-H-11 | held | REQUIRES_PREREQUISITE(CON-SIMPLE-DISTILLATION, CON-EVAPORATION-BOILING) — "distillation uses evaporation" | ENRICHMENT_TARGET | AGREE_HOLD | ☐ |
| B1-H-12 | held | REQUIRES_PREREQUISITE(CON-CHROMATOGRAPHY, CON-SOLUTION) — "chromatography uses solvent/solution vocabulary" | TRANSITIVELY_SUBSUMED | AGREE_HOLD | ☐ |

## 5. Findings (pass-2, for the batch record)

- **FP-B1-1 (split-artifact)** — The CON-STATES-THREE / CON-STATE-PARTICLE-MODEL pair (both CORE @ 1.1) and the CON-SOLUTION triple-node are operator merge/split decisions — the same FP-2 class as the pilot yield triple. All flagged with merge notes; no defect.
- **FP-B1-2 (relation-class-choice)** — CON-DIFFUSION EXPLAINED_BY CON-STATE-PARTICLE-MODEL: causal evidence ("due to the random motion") chosen over the equally-real prerequisite reading (B1-H-04). One relation per pair forced the choice; the operator may rule differently (an OD-class decision).
- **FP-B1-3 (granularity)** — CON-PURE-SUBSTANCE carries definition + fixed-point criterion in one node; the 1.1 "energy" operand straddles the particle-model/state-changes boundary. Operator granularity notes, FP-3 class.
- **FP-B1-4 (density (vocabulary-level prereqs))** — Three 1.10 technique -> CON-SOLUTION edges (distillation, filtration, crystallisation): the first two are each their technique's only solution link (kept SUGGESTED), the third is subsumed (quarantined REVIEW_REQUIRED at authoring). Operator may prune the class further at the gate.
- **FN-B1-1 (false-negative-concern)** — Mark-scheme mining covered 2 of the 4 slice-relevant Unit-1 Paper-1 MS files (States of Matter, ECM2; ECM1/ECM3 unpinned) and no Paper-2 variants — the wrong-answer-pattern inventory for this slice is incomplete. Mirrors the pilot FN-3; batch 2 should pin the remainder.
- **FN-B1-2 (boundary)** — PR-02 (4CH1-1.13, paper-chromatography practical) is batch-2 scope: its edges to CON-CHROMATOGRAPHY / CON-RF-VALUE will be authored in batch 2 — cross-batch boundary edges to EXISTING nodes are sanctioned (no boundary minting needed).
- **FN-B1-3 (vocabulary-coverage)** — "Miscible" (fractional distillation) and "filtrate/residue" are taught inline without concepts — deliberate non-minting at pilot granularity; recorded so the coverage gap is explicit, not silent.

## 6. Command-kind tags (guide §8) — batch-1 SPs

| SP | verb | guide class | demanded substance | operator |
|---|---|---|---|---|
| 4CH1-1.1 | understand | UNDERSTAND_RELATION | particle-level description of the three states (arrangement, movement, closeness and energy of particles) with the simple sphere model | ☐ |
| 4CH1-1.10 | describe | DESCRIBE_EXPERIMENT | the experimental separation techniques (simple distillation, fractional distillation, filtration, crystallisation, paper chromatography) and what each separates | ☐ |
| 4CH1-1.11 | understand | UNDERSTAND_RELATION | reading a chromatogram (number and position of spots, reference spots) to infer the composition and purity of a mixture | ☐ |
| 4CH1-1.12 | understand | CALCULATE | calculation of Rf values from chromatogram distances and their use to identify components of a mixture | ☐ |
| 4CH1-1.2 | understand | UNDERSTAND_RELATION | names of the interconversion processes (melting, freezing, boiling, condensation, sublimation) and how each is achieved (energy changes at the melting/boiling point) | ☐ |
| 4CH1-1.3 | understand | UNDERSTAND_RELATION | interpreting diffusion and dilution-of-coloured-solution experiment results as evidence for the particle model (tiny, moving particles) | ☐ |
| 4CH1-1.4 | know | KNOW_TERM | definitions of the terms solvent, solute, solution and saturated solution | ☐ |
| 4CH1-1.5C | know | KNOW_TERM | solubility in the units g per 100 g of solvent and its dependence on temperature (solids, gases) and pressure (gases) | ☐ |
| 4CH1-1.6C | understand | REPRESENT_DIAGRAM | plotting and interpreting solubility curves (g per 100 g of water against temperature, reading and scaling values) | ☐ |
| 4CH1-1.7C | investigate | DESCRIBE_EXPERIMENT | the practical method for finding the solubility of a solid at a specific temperature (saturate, evaporate, heat to constant mass, calculate) | ☐ |
| 4CH1-1.8 | understand | UNDERSTAND_RELATION | classifying a substance as an element, compound or mixture (including from particle diagrams) | ☐ |
| 4CH1-1.9 | understand | UNDERSTAND_RELATION | fixed and sharp melting/boiling points of pure substances vs ranges for mixtures, and using melting/boiling data to distinguish them | ☐ |

## 7. Negative control (4CH1-4.15) — carried forward, still uncovered

Zero concepts, zero edges, zero coverage for 4.15 across the whole merged store (machine-tested: graph_check + negative test class 10/11 + the s16-authorization check D5). The batch adds nothing in S4 territory. Operator: acknowledge ☐

## 8. Batch-1 evidence set (pinned)

- 10 T-C10 HUMAN_VALIDATED-mapped notes (read in full at extraction): a. States of Matter ×5 (Changing states, Diffusion, Solutions, Solubility, Investigating solubility) + b. Elements, Compounds and Mixtures ×5 (Element/Compound or Mixture, Pure substances, Separation techniques, Interpreting chromatograms, Paper chromatography).
- 2 pinned mark-scheme extractions (misconception-class evidence only): SOM_MS_P1.txt (sha1_12 e41e67f27cd5) + ECM2_MS_P1.txt (sha1_12 3c31a1a0e154) — per-batch mark-scheme mining per the §16 scope; ECM1/ECM3 and the Paper-2 variants remain unpinned (FN-B1-1).

## 9. After review (the batch gate)

1. Fill `scripts/c11_batch1_verdicts_template.yaml` (rename to `c11_batch1_verdicts.yaml`): per-row verdicts, the RR settlement, the identity decisions, the held acknowledgment.
2. The next session encodes your verdicts (fail-closed) and applies them: CONFIRM edges through the §18 pathway (`c11_diff_review.py approve` → one `c11_promote.py` invocation → gated G13 re-run); REJECT rows re-authored out like HELD-13; MERGE/SPLIT as §7 re-authoring; the RR settlement per its vocabulary.
3. Only after the batch-1 gate settles does batch 2 (S1 remainder 1.13–1.24) get commissioned — the consolidated cross-slice boundary ruling comes before phase 2 (S3).

---
Machine artifacts: `graph/concepts.yaml`, `graph/concept_edges.yaml`, `graph/spec_command_kinds.yaml` (generated, gated, merged store) · `C11_BATCH1_REVIEW.json` (this sheet's machine record) · `scripts/c11_batch1_verdicts_template.yaml` (the verdict template) · contract: `C11_ARCHITECTURE.md`
