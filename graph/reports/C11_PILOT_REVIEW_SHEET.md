# T-C11 Pilot Review Sheet — Concept / Prerequisite / Misconception Graph

Slice 4CH1-1.25–1.36 · generated 2026-09-11 · decision record `scripts/c11_pilot_decisions.yaml` (pass 1: `c11-pilot-pass-1`) · adversarial pass 2: `scripts/c11_pilot_review_pass2.yaml`

**NOTHING in the graph is authoritative.** All 29 nodes / 66 edges are AI_SUGGESTED (SUGGESTED or REVIEW_REQUIRED). HUMAN_VALIDATED is reachable only by your promotion command — the promotion pathway will be built in the next round (c10_promote-style, decisions-side) after this review.

How to review: for each row check the quoted evidence actually appears in the cited file and actually says what the record claims; then rule on the relation CLASS and direction, not just existence. Verdict vocabulary: CONFIRM / REJECT / HOLD / MERGE (identity) / SPLIT (identity). Machine state: `graph_check.py` groups 10–11 + `c11_negative_test.py` are green; every quote is machine-verified byte-for-byte against its source file.

## 1. Totals & second-pass agreement

| | nodes | authored edges | |
|---|---|---|
| pass-1 (extraction) | 29 | 33 (+33 derived PART_OF) |
| pass-2 verdicts | 29 CONFIRM(+note) | 31 CONFIRM(+note) · 1 HOLD · 1 REJECT |

Raw agreement (NOT κ — single human rater, architecture §12): nodes 29/29 = 100.0%; edges — of the 31 edges pass-1 asserted (SUGGESTED), pass-2 confirmed 31 (100.0%); the 2 edges pass-1 emitted as REVIEW_REQUIRED were concordantly NOT asserted by pass 2 (HOLD/REJECT) — keep-vs-drop is left to you (§3.1). No pass-2 verdict contradicts a pass-1 assertion.

## 2. Concept & misconception nodes (29)

| # | code | family | title | attaches to (role) | conf | evidence (anchor → quote) | pass-2 | operator |
|---|---|---|---|---|---|---|---|---|
| 1 | `4CH1-CON-EQ-WORD` | CONCE | Word equation | 4CH1-1.25 (core) | high | NOTE: “Word equations show the reactants and products of a chemical reaction using their full chemical name” | CONFIRM | ☐ |
| 2 | `4CH1-CON-EQ-SYMBOL` | CONCE | Balanced symbol (chemical) equation | 4CH1-1.25 (core) | high | NOTE: “A symbol equation must be balanced to give the correct ratio of reactants and products” | CONFIRM | ☐ |
| 3 | `4CH1-CON-EQ-STATE-SYM` | CONCE | State symbols (s), (l), (g), (aq) | 4CH1-1.25 (core) | high | NOTE: “You need to be confident using the state symbols (s), (l), (g) and (aq)” | CONFIRM | ☐ |
| 4 | `4CH1-CON-CONSERVATION-MASS` | CONCE | Law of Conservation of Mass | 4CH1-1.25 (core); 4CH1-1.26 (supp) | high | NOTE: “Atoms cannot be created or destroyed, so if they exist in the reactants then they absolutely must be” | CONFIRM | ☐ |
| 5 | `4CH1-CON-AR` | CONCE | Relative atomic mass (Ar) | 4CH1-1.26 (core); 4CH1-1.28 (core) | high | NOTE: “The relative atomic mass of every element is given on the Periodic Table. It is the larger of the tw” | CONFIRM | ☐ |
| 6 | `4CH1-CON-MR` | CONCE | Relative formula mass (Mr) | 4CH1-1.26 (core); 4CH1-1.28 (core) | high | NOTE: “To calculate the Mr of a substance, you have to add up the relative atomic masses of all the atoms p” | CONFIRM | ☐ |
| 7 | `4CH1-CON-MOLE` | CONCE | The mole (unit of amount of substance) | 4CH1-1.27 (core) | high | SPEC: “know that the mole(mol) is the unit for the amount of a substance” | CONFIRM | ☐ |
| 8 | `4CH1-CON-AVOGADRO-CONST` | CONCE | Avogadro constant | 4CH1-1.27 (enri) | high | NOTE: “The number of atoms, molecules or ions in a mole (1 mol) of a given substance is the Avogadro consta” | CONFIRM_WITH_NOTE | ☐ |
| 9 | `4CH1-CON-MOLAR-MASS` | CONCE | Molar mass | 4CH1-1.28 (core) | high | NOTE: “The mass of 1 mole of a substance is known as the molar mass” | CONFIRM | ☐ |
| 10 | `4CH1-CON-MOLE-MASS-CONV` | CONCE | Mole-mass conversion | 4CH1-1.28 (core) | high | NOTE: “Therefore we have to be able to convert between moles and grams” | CONFIRM | ☐ |
| 11 | `4CH1-CON-MOLAR-RATIO` | CONCE | Molar ratio from balanced equations | 4CH1-1.29 (core) | high | NOTE: “Remember the molar ratio of a balanced equation gives you the ratio of the amounts of each substance” | CONFIRM_WITH_NOTE | ☐ |
| 12 | `4CH1-CON-REACTING-MASS` | CONCE | Reacting mass calculation | 4CH1-1.29 (core) | high | SPEC: “calculate reacting masses using experimental data and chemical equations” | CONFIRM | ☐ |
| 13 | `4CH1-CON-YIELD` | CONCE | Yield (actual yield) | 4CH1-1.30 (core) | high | NOTE: “The actual yield is the recorded amount of product obtained” | CONFIRM_WITH_NOTE | ☐ |
| 14 | `4CH1-CON-THEOR-YIELD` | CONCE | Theoretical yield | 4CH1-1.30 (core) | high | NOTE: “The theoretical yield is the amount of product that would be obtained under perfect practical and ch” | CONFIRM_WITH_NOTE | ☐ |
| 15 | `4CH1-CON-PERCENT-YIELD` | CONCE | Percentage yield | 4CH1-1.30 (core) | high | SPEC: “calculate percentage yield” | CONFIRM | ☐ |
| 16 | `4CH1-CON-YIELD-FACTORS` | CONCE | Factors reducing yield | 4CH1-1.30 (enri) | high | NOTE: “In practice, you never get 100% yield in a chemical process for several reasons” | CONFIRM_WITH_NOTE | ☐ |
| 17 | `4CH1-CON-EMPIRICAL-FORMULA` | CONCE | Empirical formula | 4CH1-1.32 (core); 4CH1-1.33 (core) | high | SPEC: “know what is meant by the terms empirical formula and molecular formula” | CONFIRM | ☐ |
| 18 | `4CH1-CON-MOLECULAR-FORMULA` | CONCE | Molecular formula | 4CH1-1.32 (core); 4CH1-1.33 (core) | high | NOTE: “The molecular formula is the formula that shows the number and type of each atom in a molecule” | CONFIRM | ☐ |
| 19 | `4CH1-CON-EMP-MOL-CALC` | CONCE | Empirical and molecular formula calculation | 4CH1-1.33 (core) | high | NOTE: “Empirical formula calculations are very methodical” | CONFIRM | ☐ |
| 20 | `4CH1-CON-EXP-FORMULA-DEDUCTION` | CONCE | Experimental formula deduction (mass-difference method) | 4CH1-1.31 (core); 4CH1-1.36 (core) | high | NOTE: “The principle is to use mass measurements before and after a reaction and then convert masses into m” | CONFIRM | ☐ |
| 21 | `4CH1-CON-WATER-CRYST` | CONCE | Water of crystallisation and hydrated salts | 4CH1-1.31 (core) | high | SPEC: “salts containing water of crystallisation” | CONFIRM | ☐ |
| 22 | `4CH1-CON-CONCENTRATION` | CONCE | Concentration of a solution | 4CH1-1.34C (core) | high | NOTE: “Concentration refers to the amount of solute there is in a specific volume of the solvent” | CONFIRM | ☐ |
| 23 | `4CH1-CON-CONC-CALC` | CONCE | Concentration calculation (mol/dm3) | 4CH1-1.34C (core) | high | NOTE: “Calculate the concentration of a solution of sodium hydroxide, NaOH, in mol / dm3” | CONFIRM | ☐ |
| 24 | `4CH1-CON-VOL-CONVERSION` | CONCE | Volume unit conversion (cm3/dm3) | 4CH1-1.34C (core) | high | NOTE: “To convert cm3 to dm3, divide by 1000” | CONFIRM_WITH_NOTE | ☐ |
| 25 | `4CH1-CON-MOLAR-GAS-VOL` | CONCE | Molar gas volume at RTP (24 dm3) | 4CH1-1.35C (core) | high | SPEC: “the molar volume of a gas(24dm3and24000cm3at room temperature and pressure(rtp))” | CONFIRM | ☐ |
| 26 | `4CH1-CON-GAS-VOL-CALC` | CONCE | Gas volume calculation | 4CH1-1.35C (core) | high | NOTE: “The formula can be used to calculate the number of moles of gases from a given volume or vice versa” | CONFIRM | ☐ |
| 27 | `4CH1-CON-AVOGADRO-LAW` | CONCE | Avogadro's Law | 4CH1-1.35C (enri) | high | NOTE: “Avogadro’s Law states that at the same conditions of temperature and pressure, equal amounts of gase” | CONFIRM_WITH_NOTE | ☐ |
| 28 | `4CH1-MIS-EQ-SUBSCRIPT` | MISCO | Balancing equations by altering subscripts | — | high | NOTE: “A common mistake when balancing symbol equations is to add, change or remove small numbers in the ch”<br>remediation: “You cannot do this because it changes what the substance is” | CONFIRM | ☐ |
| 29 | `4CH1-MIS-CONC-UNIT` | MISCO | Failing to convert cm3 to dm3 in concentration calculations | — | high | MARK_SCHEME: “an answer of 10(.0) for 1 mark (i.e. failing to divide by 1000)”<br>remediation: “Don't forget your unit conversions” | CONFIRM | ☐ |

Identity-policy notes (split-first; merges are operator-only): pass-2 flags the yield triple (CON-YIELD / CON-THEOR-YIELD / CON-PERCENT-YIELD) and reminds that all aliases are merge inputs. No pass-2 merge recommendations beyond §3.1 notes.

## 3. Authored semantic edges (33)

Direction conventions: REQUIRES_PREREQUISITE source=dependent → target=prerequisite; EXPLAINED_BY explained → explainer; REMEDIATED_BY misconception → concept.

### 3.1 REVIEW_REQUIRED (operator must settle these two first)

| edge | conf | evidence | ambiguity (pass-1) | pass-2 | operator |
|---|---|---|---|---|---|
| `4CH1-PR-03` **REQUIRES_PREREQUISITE** `4CH1-CON-MOLE` | medium | “| moles | a / Ar | a / Ar |” | Implicit concept use only (table row label). Genuine prerequisite on CON-MOLE, or transitively subsumed via PR-03 -> CON-EXP-FORMULA-DEDUCTION -> CON-MOLE? Semantic judgment reserved for review. | REJECT: Subsumed transitively via PR-03 -> EXP-FORMULA-DEDUCTION -> MOLE; the "moles" table-row label is implicit use only. Pass-1 emitted as REVIEW_REQUIRED; pass 2 would not emit at all. Left in the graph a | ☐ |
| `4CH1-CON-GAS-VOL-CALC` **REQUIRES_PREREQUISITE** `4CH1-CON-AVOGADRO-LAW` | medium | “Therefore, the volume of oxygen needed would be = 5 moles x 150 cm3” | The worked example relies on volume-ratios-track-mole-ratios without naming Avogadro's Law. Genuine dependency on CON-AVOGADRO-LAW, or merely an application of CON-MOLAR-RATIO (which has no node-to-node edge here)? Seman | HOLD: The worked example applies volume-ratios-track-mole-ratios without naming the law; the dependency may be on CON-MOLAR-RATIO instead (which has no direct edge here). Pass-1 already emitted as REVIEW_RE | ☐ |

### 3.2 SUGGESTED edges (31)

| edge | method | conf | evidence (quote) | upstream | pass-2 | operator |
|---|---|---|---|---|---|---|
| `4CH1-CON-MOLE-MASS-CONV` **REQUIRES_PREREQUISITE** `4CH1-CON-MOLAR-MASS` | DEFINITIONAL_DEPENDENCY | high | “The mass is calculated by moles x molar mass” | T-C10 HUMAN_VALIDATED 4CH1-1.28 @ Calculating moles and mass (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-MOLAR-MASS` **REQUIRES_PREREQUISITE** `4CH1-CON-MOLE` | DEFINITIONAL_DEPENDENCY | high | “The mass of 1 mole of a substance is known as the molar mass” | T-C10 HUMAN_VALIDATED 4CH1-1.28 @ Calculating moles and mass (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-MOLAR-MASS` **REQUIRES_PREREQUISITE** `4CH1-CON-MR` | DEFINITIONAL_DEPENDENCY | high | “For a compound, it is the same as the relative molecular or formula mass in grams” | T-C10 HUMAN_VALIDATED 4CH1-1.28 @ Calculating moles and mass (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-MOLAR-MASS` **REQUIRES_PREREQUISITE** `4CH1-CON-AR` | DEFINITIONAL_DEPENDENCY | high | “For an element, it is the same as the relative atomic mass written in grams” | T-C10 HUMAN_VALIDATED 4CH1-1.28 @ Calculating moles and mass (2026-09-11) | CONFIRM_WITH_NOTE | ☐ |
| `4CH1-CON-MR` **REQUIRES_PREREQUISITE** `4CH1-CON-AR` | DEFINITIONAL_DEPENDENCY | high | “To calculate the Mr of a substance, you have to add up the relative atomic masses of all the atoms p” | T-C10 HUMAN_VALIDATED 4CH1-1.26 @ Calculate Relative Mass (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-REACTING-MASS` **REQUIRES_PREREQUISITE** `4CH1-CON-MOLE-MASS-CONV` | USED_WITHOUT_RETEACHING | high | “Step 1 - calculate the moles of magnesium” | T-C10 HUMAN_VALIDATED 4CH1-1.29 @ Reacting mass calculations (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-REACTING-MASS` **REQUIRES_PREREQUISITE** `4CH1-CON-MOLAR-RATIO` | USED_WITHOUT_RETEACHING | high | “Step 2 - use the molar ratio from the balanced symbol equation” | T-C10 HUMAN_VALIDATED 4CH1-1.29 @ Reacting mass calculations (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-REACTING-MASS` **REQUIRES_PREREQUISITE** `4CH1-CON-EQ-SYMBOL` | USED_WITHOUT_RETEACHING | high | “Then, the ratio between the substances is identified using the balanced chemical equation” | T-C10 HUMAN_VALIDATED 4CH1-1.29 @ Reacting mass calculations (2026-09-11) | CONFIRM_WITH_NOTE | ☐ |
| `4CH1-CON-PERCENT-YIELD` **REQUIRES_PREREQUISITE** `4CH1-CON-THEOR-YIELD` | DEFINITIONAL_DEPENDENCY | high | “The percentage yield compares the actual yield to the theoretical yield” | T-C10 HUMAN_VALIDATED 4CH1-1.30 @ Calculate percentage yield (2026-09-11) | CONFIRM_WITH_NOTE | ☐ |
| `4CH1-CON-PERCENT-YIELD` **REQUIRES_PREREQUISITE** `4CH1-CON-YIELD` | DEFINITIONAL_DEPENDENCY | high | “The percentage yield compares the actual yield to the theoretical yield” | T-C10 HUMAN_VALIDATED 4CH1-1.30 @ Calculate percentage yield (2026-09-11) | CONFIRM_WITH_NOTE | ☐ |
| `4CH1-CON-THEOR-YIELD` **REQUIRES_PREREQUISITE** `4CH1-CON-REACTING-MASS` | USED_WITHOUT_RETEACHING | high | “It is calculated from the balanced equation and the reacting masses” | T-C10 HUMAN_VALIDATED 4CH1-1.30 @ Calculate percentage yield (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-EMP-MOL-CALC` **REQUIRES_PREREQUISITE** `4CH1-CON-EMPIRICAL-FORMULA` | DEFINITIONAL_DEPENDENCY | high | “Write the final empirical formula” | T-C10 HUMAN_VALIDATED 4CH1-1.32 + 4CH1-1.33 @ Empirical & Molecular Formulae (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-EMP-MOL-CALC` **REQUIRES_PREREQUISITE** `4CH1-CON-MOLE` | USED_WITHOUT_RETEACHING | high | “Calculate the moles of each element” | T-C10 HUMAN_VALIDATED 4CH1-1.33 @ Empirical & Molecular Formulae (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-EMP-MOL-CALC` **REQUIRES_PREREQUISITE** `4CH1-CON-AR` | USED_WITHOUT_RETEACHING | high | “Write the relative atomic mass of each element” | T-C10 HUMAN_VALIDATED 4CH1-1.33 @ Empirical & Molecular Formulae (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-MOLECULAR-FORMULA` **REQUIRES_PREREQUISITE** `4CH1-CON-EMPIRICAL-FORMULA` | USED_WITHOUT_RETEACHING | high | “Find the relative formula mass of the empirical formula” | T-C10 HUMAN_VALIDATED 4CH1-1.32 + 4CH1-1.33 @ Empirical & Molecular Formulae (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-MOLECULAR-FORMULA` **REQUIRES_PREREQUISITE** `4CH1-CON-MR` | USED_WITHOUT_RETEACHING | high | “Add the relative atomic masses of all the atoms in the empirical formula” | T-C10 HUMAN_VALIDATED 4CH1-1.33 @ Empirical & Molecular Formulae (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-WATER-CRYST` **REQUIRES_PREREQUISITE** `4CH1-CON-EMP-MOL-CALC` | EXPLICIT_TEACH_SEQUENCE | high | “The steps for empirical formula can be adapted for hydrated salt / water of crystallisation calculat” | T-C10 HUMAN_VALIDATED 4CH1-1.31 @ Empirical & Molecular Formulae (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-EXP-FORMULA-DEDUCTION` **REQUIRES_PREREQUISITE** `4CH1-CON-MOLE` | USED_WITHOUT_RETEACHING | high | “The principle is to use mass measurements before and after a reaction and then convert masses into m” | T-C10 HUMAN_VALIDATED 4CH1-1.31 @ Simple compound formulae (2026-09-11) | CONFIRM | ☐ |
| `4CH1-PR-03` **REQUIRES_PREREQUISITE** `4CH1-CON-EXP-FORMULA-DEDUCTION` | USED_WITHOUT_RETEACHING | high | “Divide each of the two masses by the relative atomic masses of the element” | T-C10 HUMAN_VALIDATED 4CH1-1.36 @ Investigating metal oxide formulas (2026-09-11); prac... | CONFIRM | ☐ |
| `4CH1-CON-CONC-CALC` **REQUIRES_PREREQUISITE** `4CH1-CON-MOLE` | USED_WITHOUT_RETEACHING | high | “Calculate the amount of solute, in moles, present in 2.5 dm3 of a solution whose concentration is 0.” | T-C10 HUMAN_VALIDATED 4CH1-1.34C @ Solution concentration (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-CONC-CALC` **REQUIRES_PREREQUISITE** `4CH1-CON-VOL-CONVERSION` | USED_WITHOUT_RETEACHING | high | “Remember: The volume needs to be in dm3” | T-C10 HUMAN_VALIDATED 4CH1-1.34C @ Solution concentration (2026-09-11); PMT CFEC2 MS Q4(a) | CONFIRM | ☐ |
| `4CH1-CON-MOLAR-GAS-VOL` **REQUIRES_PREREQUISITE** `4CH1-CON-MOLE` | DEFINITIONAL_DEPENDENCY | high | “At room temperature and pressure, the volume occupied by one mole of any gas was found to be 24 dm3 ” | T-C10 HUMAN_VALIDATED 4CH1-1.35C @ Calculate Gas Volumes (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-GAS-VOL-CALC` **REQUIRES_PREREQUISITE** `4CH1-CON-MOLAR-GAS-VOL` | DEFINITIONAL_DEPENDENCY | high | “Volume = Moles x Molar Volume” | T-C10 HUMAN_VALIDATED 4CH1-1.35C @ Calculate Gas Volumes (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-GAS-VOL-CALC` **REQUIRES_PREREQUISITE** `4CH1-CON-MOLE-MASS-CONV` | USED_WITHOUT_RETEACHING | high | “To answer these type of questions you must first convert grams to moles and then calculate the volum” | T-C10 HUMAN_VALIDATED 4CH1-1.35C @ Calculate Gas Volumes (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-EQ-SYMBOL` **EXPLAINED_BY** `4CH1-CON-CONSERVATION-MASS` | SINGLE_SOURCE_CAUSAL_TEACHING | high | “The Law of Conservation of Mass enables us to balance chemical equations, since no atoms can be lost” | T-C10 HUMAN_VALIDATED 4CH1-1.25 @ Writing chemical equations (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-MOLAR-GAS-VOL` **EXPLAINED_BY** `4CH1-CON-AVOGADRO-LAW` | SINGLE_SOURCE_CAUSAL_TEACHING | medium | “From the molar gas volume the following formula triangle can be derived” | T-C10 HUMAN_VALIDATED 4CH1-1.35C @ Calculate Gas Volumes (2026-09-11) | CONFIRM_WITH_NOTE | ☐ |
| `4CH1-CON-YIELD` **EXPLAINED_BY** `4CH1-CON-YIELD-FACTORS` | SINGLE_SOURCE_CAUSAL_TEACHING | high | “In practice, you never get 100% yield in a chemical process for several reasons” | T-C10 HUMAN_VALIDATED 4CH1-1.30 @ Calculate percentage yield (2026-09-11) | CONFIRM | ☐ |
| `4CH1-MIS-EQ-SUBSCRIPT` **MISCONCEPTION_OF** `4CH1-CON-EQ-SYMBOL` | EXAMINER_TIP_EXPLICIT | high | “A common mistake when balancing symbol equations is to add, change or remove small numbers in the ch” | T-C10 HUMAN_VALIDATED 4CH1-1.25 @ Writing chemical equations (2026-09-11) | CONFIRM | ☐ |
| `4CH1-MIS-EQ-SUBSCRIPT` **REMEDIATED_BY** `4CH1-CON-CONSERVATION-MASS` | EXAMINER_TIP_EXPLICIT | medium | “You cannot do this because it changes what the substance is” | T-C10 HUMAN_VALIDATED 4CH1-1.25 @ Writing chemical equations (2026-09-11) | CONFIRM_WITH_NOTE | ☐ |
| `4CH1-MIS-CONC-UNIT` **WRONG_ANSWER_PATTERN** `4CH1-CON-CONC-CALC` | ASSESSMENT_DOCUMENTED | high | “an answer of 10(.0) for 1 mark (i.e. failing to divide by 1000)” | PMT Unit-1 Paper-1 MS "Chemical Formulae, Equations, Calculations 2" Q4(a) (pinned extr... | CONFIRM | ☐ |
| `4CH1-MIS-CONC-UNIT` **REMEDIATED_BY** `4CH1-CON-VOL-CONVERSION` | EXAMINER_TIP_EXPLICIT | high | “Don't forget your unit conversions” | T-C10 HUMAN_VALIDATED 4CH1-1.34C @ Solution concentration (2026-09-11) | CONFIRM | ☐ |

### 3.3 Derived PART_OF edges (33)

Derived deterministically from node attachments (concepts.yaml); each carries the attachment's evidence anchors and the node's provenance. Not re-listed here — review them via the §2 node rows. Machine-verified: the PART_OF set must exactly equal the declared attachments (c11.7).

## 4. Held / rejected candidates (12) — the abstention record

These were considered and NOT drawn. The pilot's success criterion includes correct abstention; review that each hold reason is right (pass-2 already did — column below). Overriding a hold = re-authoring the decision record, never hand-editing the graph.

| id | status | candidate | failing rule | pass-2 | operator |
|---|---|---|---|---|---|
| HELD-01 | held | MISCONCEPTION node "rounding non-integer empirical ratios" (e.g. 1.5 -> 2) MISCONCEPTION_OF CON-EMP-MOL-CALC | INSUFFICIENT_EVIDENCE_MISCONCEPTION | AGREE_HOLD | ☐ |
| HELD-02 | held | COMMONLY_CONFUSED_WITH(CON-CONCENTRATION, "solution strength") | NO_TARGET_NODE_PLUS_WEAK_CLASS | AGREE_HOLD | ☐ |
| HELD-03 | held | EXPLAINED_BY(CON-MOLE, CON-AVOGADRO-CONST) — "the Avogadro constant quantifies the mole" | RELATION_CLASS_AMBIGUOUS | AGREE_HOLD | ☐ |
| HELD-04 | held | REQUIRES_PREREQUISITE(CON-GAS-VOL-CALC, CON-MOLE) | TRANSITIVELY_SUBSUMED | AGREE_HOLD | ☐ |
| HELD-05 | held | REQUIRES_PREREQUISITE(CON-MOLAR-RATIO, CON-EQ-SYMBOL) | TRANSITIVELY_SUBSUMED_PLUS_DEFENSIONAL | AGREE_HOLD | ☐ |
| HELD-06 | held | REQUIRES_PREREQUISITE(CON-EMP-MOL-CALC, CON-MOLE-MASS-CONV) | TAUGHT_INLINE | AGREE_HOLD | ☐ |
| HELD-07 | held | REQUIRES_PREREQUISITE(CON-CONCENTRATION, solute/solvent/solution concepts) | TAUGHT_INLINE_PLUS_BOUNDARY | AGREE_HOLD | ☐ |
| HELD-08 | held | RELATED_TO(CON-EMPIRICAL-FORMULA, CON-MOLECULAR-FORMULA) | RESIDUAL_CLASS_DISCIPLINE | AGREE_HOLD | ☐ |
| HELD-09 | rejected | EXPLAINED_BY("SO2 formation from fuel impurities" concept, "combustion of hydrocarbon fuels" concept) and REMEDIATED_... | NEGATIVE_CONTROL_4_15 | AGREE_REJECT | ☐ |
| HELD-10 | held | REQUIRES_PREREQUISITE(CON-EXP-FORMULA-DEDUCTION, CON-EMP-MOL-CALC) | RELATION_CLASS_AMBIGUOUS | AGREE_HOLD | ☐ |
| HELD-11 | held | WRONG_ANSWER_PATTERN node from CFEC1 MS Q4(a)(ii)-(iii) ("0.44 for 1 mark only" / "0.0004") | EVIDENCE_AMBIGUOUS_EXTRACTION | AGREE_HOLD | ☐ |
| HELD-12 | held | MISCONCEPTION node "products written first confuses word-equation construction" MISCONCEPTION_OF CON-EQ-WORD | EXAM_TECHNIQUE_NOT_MISCONCEPTION | AGREE_HOLD | ☐ |

## 5. Findings (pass-2, for the pilot report)

- **FP-1 (false-positive-concern)** — MOLAR-GAS-VOL EXPLAINED_BY AVOGADRO-LAW: the evidence anchor supports the molar-volume->formula link, not law->molar-volume; mitigated by confidence=medium and the derivation note. Kept; flagged.
- **FP-2 (split-artifact)** — The PERCENT-YIELD -> {YIELD, THEOR-YIELD} edge pair is an artifact of the three-way yield split; both vanish under an operator merge. Identity-policy decision, not a defect.
- **FP-3 (granularity)** — REACTING-MASS -> EQ-SYMBOL: operative dependency is on interpreting (not writing) equations; the slice has one concept covering both. Granularity note for the expansion round.
- **FN-1 (false-negative-concern)** — HELD-01 (non-integer ratio mishandling) is plausibly a real, high-frequency misconception; the corpus simply does not document it. Mitigation path: deeper mark-scheme mining (17 Unit-1 MS files exist; only 2 pinned) or question-distractor mining in Phase 4 (T-C06).
- **FN-2 (false-negative-concern)** — Boundary concepts (chemical-formulae interpretation for Mr; solute/solvent for concentration; isotope abundance for Ar) are real prerequisites outside the slice; deliberately not minted (pilot scope). The expansion MUST define the boundary-minting policy or cross-slice prerequisites will be structurally missing.
- **FN-3 (coverage)** — Mark-scheme evidence mining was deliberately minimal (2 of ~17 Unit-1 mark schemes pinned) — the wrong-answer-pattern inventory is certainly incomplete; expansion round should mine all Unit-1/2 MS files for the slice's SPs.

## 6. Command-kind tags (guide §8)

| SP | verb | guide class | demanded substance | operator |
|---|---|---|---|---|
| 4CH1-1.25 | write | PRODUCE_EQUATION | worked examples of writing word equations and balanced symbol equations (with state symbols) | ☐ |
| 4CH1-1.26 | calculate | CALCULATE | Mr calculation procedure and worked examples from relative atomic masses | ☐ |
| 4CH1-1.27 | know | KNOW_TERM | definition or meaningful instructional use of the mole as the unit of amount of substance | ☐ |
| 4CH1-1.28 | understand | CALCULATE | amount-of-substance calculation procedures and worked examples using Ar and Mr | ☐ |
| 4CH1-1.29 | calculate | CALCULATE | reacting-mass calculation procedure and worked examples from experimental data and equations | ☐ |
| 4CH1-1.30 | calculate | CALCULATE | percentage-yield calculation procedure and worked examples | ☐ |
| 4CH1-1.31 | understand | DESCRIBE_EXPERIMENT | experimental method/procedure for obtaining formulae of simple compounds | ☐ |
| 4CH1-1.32 | know | KNOW_TERM | definitions of the terms empirical formula and molecular formula | ☐ |
| 4CH1-1.33 | calculate | CALCULATE | calculation procedure and worked examples for empirical and molecular formulae from experimental data | ☐ |
| 4CH1-1.34C | understand | CALCULATE | calculation procedures and worked examples involving amount of substance, volume and concentration | ☐ |
| 4CH1-1.35C | understand | CALCULATE | calculation procedures and worked examples for gas volumes and molar volume at RTP | ☐ |
| 4CH1-1.36 | know | DESCRIBE_EXPERIMENT | practical method for determining the formula of a metal oxide by combustion or reduction | ☐ |

## 7. Negative control (4CH1-4.15)

Zero concepts, zero edges, zero coverage for 4.15. The premise (“All these fuels contain carbon, hydrogen and small quantities of sulfur”, Definition-of-combustion note, mapped 4.11–4.13) and the stated consequence (“The sulfur dioxide produced from the combustion of fossil fuels dissolves in rainwater”, Nitrogen-Oxides-&-Sulfur-Dioxide note, mapped 4.14/4.16) were both present — the machine rules (attachment rule §2 + anchor admissibility §11 + negative test class 11) make the premise+consequence edge structurally impossible. Remediation is a corpus decision (new note / student-book OCR), never a graph-side inference. Operator: acknowledge ☐

## 8. After review

1. Record verdicts above (CONFIRM/REJECT/HOLD/MERGE/SPLIT per row).
2. On request, a staged promotion batch command will be derived mechanically from your confirms (c10_promote pattern: decisions-side validation blocks, gated applier, pre/post audit).
3. Expansion to the full 4CH1 graph requires the §16 criteria (all gates green + this review recorded + scoped expansion plan).

---
Machine artifacts: `graph/concepts.yaml`, `graph/concept_edges.yaml`, `graph/spec_command_kinds.yaml` (generated, gated) · `C11_PILOT_REVIEW.json` (this sheet's machine record) · contract: `C11_ARCHITECTURE.md`
