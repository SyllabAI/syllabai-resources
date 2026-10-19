# T-C11 §16 Batch 5 Review Sheet — Concept / Prerequisite / Misconception Graph

Slice 4CH1-2.1–2.14 (Section 2 — Inorganic Chemistry, FIRST slice: a Group 1 (Alkali Metals) / b Group 7 (Halogens) / c Gases in the Atmosphere, 14 SPs) + practical PR-05 · generated 2026-09-22 · decision record `scripts/c11_batch5_decisions.yaml` (pass 1: `c11-s16-batch-5`) · adversarial pass 2: `scripts/c11_batch5_review_pass2.yaml` · authorization: `scripts/c11_s16_authorization.yaml` (§16 authorized 2026-09-12; batch 5 commissioned by the operator's 'run batch 5' directive) · boundary ruling: `scripts/c11_batch5_boundary_ruling.yaml` (session 55, machine-checked — the 3 sanctioned boundary edges below)

**NOTHING in this batch is authoritative.** All 16 nodes / 31 batch edges are AI_SUGGESTED (SUGGESTED). HUMAN_VALIDATED is reachable only by your promotion command via the §18 pathway (`scripts/c11_promote.py` → `scripts/c11_promotions.yaml` → regeneration). **Zero batch-5 promotions exist.** This sheet is the batch's operator gate: record verdicts in `scripts/c11_batch5_verdicts_template.yaml` (fill + rename to `c11_batch5_verdicts.yaml`); a later session encodes and applies them.

How to review: for each row check the quoted evidence actually appears in the cited file and actually says what the record claims; then rule on the relation CLASS and direction, not just existence. Machine state: the full gate suite is green at the merged 129-node / 306-edge store; every quote is machine-verified byte-for-byte against its source file (G03/c11.4; 105 quote probes + 89 record anchors pre-verified BEFORE the registry grew, then re-verified by the generator); the 4.15 negative control is uncovered. THREE edges are cross-section boundary edges into the ruled owners (CON-ELECTRONIC-CONFIGURATION x2 — batch 2; CON-EXO-ENDO — batch 4 — sanctioned per the session-55 cross-slice ruling; no duplicate concept was minted). The GROUP1 pdftotext pin splits the Q1d IGNORE line across a column break and the GROUP7 pin interleaves the Q1bii Reject entries; the misconception attributions are recorded in the nodes' derivation_notes.

## 1. Totals & second-pass agreement

| | nodes | authored edges | held | |
|---|---|---|---|
| pass-1 (extraction) | 16 | 18 (+13 derived PART_OF) | 14 |
| pass-2 verdicts | 16 CONFIRM(+note) | 18 CONFIRM(+note) · 0 HOLD · 0 REJECT | all 14 AGREE |

Raw agreement (NOT κ — single human rater, architecture §12): nodes 16/16 = 100.0%; edges — of the 18 edges pass-1 asserted (SUGGESTED), pass-2 confirmed 18 (100.0%); pass-1 quarantined 0 edges as REVIEW_REQUIRED (this batch authored NONE — every doubt was held or resolved on explicit evidence). **One pass-2 finding (FP-B5-5, a mistargeted dependency surface) was re-authored BEFORE the gate; zero demotions at the re-authored state.**

Forecast calibration (C11_BATCH_FORECAST.json future_batch_records): predicted 33.6 nodes / 38.5 edges / 14.0 held vs actual 16 / 18 / 14 — the batch-5 record is appended by the forecast instrument at this gate (see the regenerated C11_BATCH_FORECAST.json). The descriptive-heavy S2 families run the lightest yield band so far (nodes/SP 1.14, edges/SP 1.29) — the item-14 plan's own S2 anticipation, with the inline-re-teach abstentions (B5-H-02/03) accounting for the gap, not thin coverage: no S1/S3 identity was re-minted (the 2 ruled targets reached via 3 sanctioned boundary edges); 2.14 attaches no concept node (PR-05 owns it — the 1.13/1.60C precedent) with the practical->concept edge authored.

## 2. Concept & misconception nodes (16)

| # | code | family | title | attaches to (role) | conf | evidence (anchor → quote) | pass-2 | operator |
|---|---|---|---|---|---|---|---|---|
| 1 | `4CH1-CON-G1-FAMILY-EVIDENCE` | CONCE | Group 1 water-reaction similarities as family evidence (alkali metals) | 4CH1-2.1 (core) | high | NOTE: “The reaction of the Group 1 metals with water provides evidence for categorising these elements into” | CONFIRM | ☐ |
| 2 | `4CH1-CON-G1-TREND` | CONCE | Group 1 reactivity trend from air/water reaction differences | 4CH1-2.2 (core) | high | NOTE: “The differences between the reactions of the group 1 metals with water and oxygen provide evidence o” | CONFIRM | ☐ |
| 3 | `4CH1-CON-G1-PREDICTION` | CONCE | Predicting alkali-metal properties from Group 1 trends | 4CH1-2.3 (core) | high | NOTE: “Following these trends, we can say that:” | CONFIRM | ☐ |
| 4 | `4CH1-CON-G1-REACTIVITY-ECONFIG` | CONCE | Group 1 reactivity trend explained by electronic configurations | 4CH1-2.4C (core) | high | NOTE: “As you go down Group 1, the number of shells of electrons increases by 1” | CONFIRM_WITH_NOTE | ☐ |
| 5 | `4CH1-CON-G7-PROPERTIES` | CONCE | Halogen colours, states and physical-property trends (Group 7) | 4CH1-2.5 (core) | high | NOTE: “At room temperature, the halogens exist in different states and colours, with different characterist” | CONFIRM | ☐ |
| 6 | `4CH1-CON-G7-PREDICTION` | CONCE | Predicting halogen properties from Group 7 trends (metal and non-metal halides) | 4CH1-2.6 (core) | high | NOTE: “The halogens react with some metals to form ionic compounds which are metal halide salts” | CONFIRM | ☐ |
| 7 | `4CH1-CON-G7-DISPLACEMENT` | CONCE | Halogen displacement reactions (evidence for the Group 7 reactivity trend) | 4CH1-2.7 (core) | high | NOTE: “A halogen displacement reaction occurs when a more reactive halogen displaces a less reactive haloge” | CONFIRM | ☐ |
| 8 | `4CH1-CON-G7-REACTIVITY-ECONFIG` | CONCE | Group 7 reactivity trend explained by electronic configurations | 4CH1-2.8C (core) | high | NOTE: “We can use electronic configuration to explain the trends in chemical reactivity down Group 7” | CONFIRM_WITH_NOTE | ☐ |
| 9 | `4CH1-CON-AIR-COMPOSITION` | CONCE | Composition of dry air (approximate percentages of the four most abundant gases) | 4CH1-2.9 (core) | high | NOTE: “About four-fifths (approximately 80%) nitrogen” | CONFIRM | ☐ |
| 10 | `4CH1-CON-O2-PERCENT-DETERMINATION` | CONCE | Determining the percentage of oxygen in air (metal and non-metal routes) | 4CH1-2.10 (core) | high | NOTE: “The percentage of oxygen in air can be found by reacting a metal or non-metal with the oxygen in a f” | CONFIRM | ☐ |
| 11 | `4CH1-CON-COMBUSTION-O2` | CONCE | Combustion of elements in oxygen (magnesium, hydrogen, sulfur) | 4CH1-2.11 (core) | high | NOTE: “All combustion reactions involve a chemical change in which oxygen reacts with elements or compounds” | CONFIRM | ☐ |
| 12 | `4CH1-CON-CO2-FROM-CARBONATES` | CONCE | Carbon dioxide from thermal decomposition of metal carbonates | 4CH1-2.12 (core) | high | NOTE: “Carbonates of metals from the lower half of the reactivity series tend to decompose on heating to pr” | CONFIRM | ☐ |
| 13 | `4CH1-CON-CO2-GREENHOUSE` | CONCE | Carbon dioxide as a greenhouse gas and the climate-change link | 4CH1-2.13 (core) | high | NOTE: “Greenhouse gases maintain the temperatures on Earth high enough to support life” | CONFIRM | ☐ |
| 14 | `4CH1-MIS-G1-SHELL-EXPLANATION` | MISCO | Explaining Group 1 reactivity via more shells / larger radius / shielding instead of outer-electron distance and weaker attraction | — | high | MARK_SCHEME: “IGNORE references to more shells / larger atomic radius / more”<br>remediation: “This means that the outermost electron gets further away from the nucleus, so th” | CONFIRM | ☐ |
| 15 | `4CH1-MIS-HALOGEN-HALIDE` | MISCO | Treating a halogen and its halide ion as having the same (or different) reactivity in displacement reasoning | — | high | MARK_SCHEME: “Reject any references to a halogen”<br>remediation: “A halogen displacement reaction occurs when a more reactive halogen displaces a ” | CONFIRM_WITH_NOTE | ☐ |
| 16 | `4CH1-MIS-CUO-COLOUR` | MISCO | Stating a colour other than black for the copper(II) oxide decomposition product | — | high | MARK_SCHEME: “black”<br>remediation: “Copper(II) carbonate is a green powder and slowly darkens as black copper(II) ox” | CONFIRM_WITH_NOTE | ☐ |

Identity-policy notes (split-first; merges are operator-only, OD-1 operand rule): pass-2 flags the 2.4C/2.8C sibling split (opposite trend directions — B5-ID-01), the 2.9/2.10 know-vs-method pair (B5-ID-02), the 2.14 practical ownership (B5-ID-03), the 2.11 single-family node (B5-ID-04), the CO2 two-node split (B5-ID-05) and the 2.1/2.2 similarities/differences pair (B5-ID-06). All are operator identity decisions (template §identity_decisions). 2.14 attaches NO batch-5 concept node (PR-05 owns it — the 1.13/1.60C precedent).

## 3. Authored semantic edges (18)

| # | edge | conf | derivation | evidence (anchor → quote) | pass-2 | operator |
|---|---|---|---|---|---|---|
| 1 | `4CH1-CON-AIR-COMPOSITION EXPLAINED_BY 4CH1-CON-O2-PERCENT-DETERMINATION` | high | SINGLE_SOURCE_CAUSAL_TEACHING | NOTE: “percentage of oxygen = 19.7%” | CONFIRM_WITH_NOTE | ☐ |
| 2 | `4CH1-CON-COMBUSTION-O2 REQUIRES_PREREQUISITE 4CH1-CON-EXO-ENDO` | high | USED_WITHOUT_RETEACHING | NOTE: “Combustion reactions give out heat, so they will always be exothermic reactions” | CONFIRM | ☐ |
| 3 | `4CH1-CON-G1-PREDICTION REQUIRES_PREREQUISITE 4CH1-CON-G1-TREND` | high | USED_WITHOUT_RETEACHING | NOTE: “Following these trends, we can say that:” | CONFIRM | ☐ |
| 4 | `4CH1-CON-G1-REACTIVITY-ECONFIG REQUIRES_PREREQUISITE 4CH1-CON-ELECTRONIC-CONFIGURATION` | high | USED_WITHOUT_RETEACHING | NOTE: “As you go down Group 1, the number of shells of electrons increases by 1” | CONFIRM | ☐ |
| 5 | `4CH1-CON-G1-TREND EXPLAINED_BY 4CH1-CON-G1-REACTIVITY-ECONFIG` | high | SINGLE_SOURCE_CAUSAL_TEACHING | NOTE: “Less energy is required to overcome the force of attraction as it gets weaker, so the oute” | CONFIRM | ☐ |
| 6 | `4CH1-CON-G1-TREND REQUIRES_PREREQUISITE 4CH1-CON-G1-FAMILY-EVIDENCE` | high | DEFINITIONAL_DEPENDENCY | NOTE: “The differences between the reactions of the group 1 metals with water and oxygen provide ” | CONFIRM | ☐ |
| 7 | `4CH1-CON-G7-DISPLACEMENT REQUIRES_PREREQUISITE 4CH1-CON-G7-PROPERTIES` | high | USED_WITHOUT_RETEACHING | NOTE: “The solution becomes orange as bromine is formed or” | CONFIRM | ☐ |
| 8 | `4CH1-CON-G7-DISPLACEMENT REQUIRES_PREREQUISITE 4CH1-CON-G7-REACTIVITY-ECONFIG` | high | DEFINITIONAL_DEPENDENCY | NOTE: “A halogen displacement reaction occurs when a more reactive halogen displaces a less react” | CONFIRM | ☐ |
| 9 | `4CH1-CON-G7-PREDICTION REQUIRES_PREREQUISITE 4CH1-CON-G7-PROPERTIES` | high | USED_WITHOUT_RETEACHING | NOTE: “The melting and boiling points of the halogens increase as you go down the group” | CONFIRM | ☐ |
| 10 | `4CH1-CON-G7-PREDICTION REQUIRES_PREREQUISITE 4CH1-CON-G7-REACTIVITY-ECONFIG` | high | USED_WITHOUT_RETEACHING | NOTE: “The halogens decrease in reactivity moving down the group, but they still form halide salt” | CONFIRM | ☐ |
| 11 | `4CH1-CON-G7-REACTIVITY-ECONFIG REQUIRES_PREREQUISITE 4CH1-CON-ELECTRONIC-CONFIGURATION` | high | USED_WITHOUT_RETEACHING | NOTE: “We can use electronic configuration to explain the trends in chemical reactivity down Grou” | CONFIRM | ☐ |
| 12 | `4CH1-MIS-CUO-COLOUR REMEDIATED_BY 4CH1-CON-CO2-FROM-CARBONATES` | high | ASSESSMENT_DOCUMENTED | NOTE: “Copper(II) carbonate is a green powder and slowly darkens as black copper(II) oxide is pro” | CONFIRM | ☐ |
| 13 | `4CH1-MIS-CUO-COLOUR WRONG_ANSWER_PATTERN 4CH1-CON-CO2-FROM-CARBONATES` | high | ASSESSMENT_DOCUMENTED | MARK_SCHEME: “REJECT all other colours” | CONFIRM | ☐ |
| 14 | `4CH1-MIS-G1-SHELL-EXPLANATION REMEDIATED_BY 4CH1-CON-G1-REACTIVITY-ECONFIG` | high | ASSESSMENT_DOCUMENTED | NOTE: “Less energy is required to overcome the force of attraction as it gets weaker, so the oute” | CONFIRM | ☐ |
| 15 | `4CH1-MIS-G1-SHELL-EXPLANATION WRONG_ANSWER_PATTERN 4CH1-CON-G1-REACTIVITY-ECONFIG` | high | ASSESSMENT_DOCUMENTED | MARK_SCHEME: “IGNORE references to more shells / larger atomic radius / more” | CONFIRM | ☐ |
| 16 | `4CH1-MIS-HALOGEN-HALIDE REMEDIATED_BY 4CH1-CON-G7-DISPLACEMENT` | high | ASSESSMENT_DOCUMENTED | NOTE: “A halogen displacement reaction occurs when a more reactive halogen displaces a less react” | CONFIRM | ☐ |
| 17 | `4CH1-MIS-HALOGEN-HALIDE WRONG_ANSWER_PATTERN 4CH1-CON-G7-DISPLACEMENT` | high | ASSESSMENT_DOCUMENTED | MARK_SCHEME: “Reject any references to a halogen” | CONFIRM | ☐ |
| 18 | `4CH1-PR-05 REQUIRES_PREREQUISITE 4CH1-CON-O2-PERCENT-DETERMINATION` | high | USED_WITHOUT_RETEACHING | NOTE: “To determine the percentage of oxygen in air using the oxidation of iron” | CONFIRM | ☐ |

Three edges are CROSS-SECTION boundary edges into the ruled owners (sanctioned per the session-55 cross-slice ruling — no duplicate mint): the two 2.4C/2.8C electronic-configuration rows (batch-2 owner) and the 2.11 exothermic-classification row (batch-4 owner). The EXPLAINED_BY composition row is the one relation-class flag to eyeball (FP-B5-4: the grounding direction vs an independent-facts reading).

## 4. Held candidates (14) — the abstention record

| id | candidate | failure class / reason |
|---|---|---|
| B5-H-01 | REQUIRES_PREREQUISITE(CON-G1-FAMILY-EVIDENCE, CON-ELECTRONIC-CONFIGURATION) | ENRICHMENT_BEYOND_SPEC + boundary discipline |
| B5-H-02 | REQUIRES_PREREQUISITE(CON-G7-PROPERTIES, CON-COVALENT-BOND or CON-MOLECULE) | RE-TEACHED INLINE |
| B5-H-03 | REQUIRES_PREREQUISITE(CON-G7-PREDICTION, CON-ION or CON-IONIC-FORMULA or CON-ION-CHARGE-RULES) | RE-TEACHED INLINE |
| B5-H-04 | MISCONCEPTION "swapping the Group 1 and Group 7 trend directions (reactivity increasing down Group 7 / decreasing down Group 1)" | INSUFFICIENT_EVIDENCE (session-53 Step-3 rule) |
| B5-H-05 | MISCONCEPTION "over-ticking observation-selection answers (the deduct-a-mark list rule)" | EXAM TECHNIQUE, NOT A MISCONCEPTION (the pilot HELD-12 class |
| B5-H-06 | MISCONCEPTION "swapping the displacement product colours (red for the bromine-formed solution; yellow for the iodine-formed solution)" | INSUFFICIENT_EVIDENCE (FC-1, attribution) |
| B5-H-07 | RELATED_TO(CON-CO2-GREENHOUSE, CON-CO2-FROM-CARBONATES) | FC-3 DENSITY + OD-2 |
| B5-H-08 | REQUIRES_PREREQUISITE(CON-COMBUSTION-O2, CON-REDOX-ELECTRONS) — the "classified as oxidation" boundary direction | OD-2 INCIDENTAL USAGE + G07 ANCHOR CLASS |
| B5-H-09 | REQUIRES_PREREQUISITE(CON-CO2-FROM-CARBONATES, a chemical-tests/limewater owner) | RE-TEACHED INLINE + NO OWNER |
| B5-H-10 | REQUIRES_PREREQUISITE(CON-CO2-FROM-CARBONATES, a reactivity-series owner) | FUTURE BOUNDARY + NO OWNER |
| B5-H-11 | CONCEPT node "oxidation as oxygen addition" (standalone) | ENRICHMENT_BEYOND_SPEC + IDENTITY RISK |
| B5-H-12 | REQUIRES_PREREQUISITE(CON-G7-PREDICTION, CON-G7-DISPLACEMENT) — or the reverse | NO_DIRECTIONAL_EVIDENCE (the B4-H-03 class) |
| B5-H-13 | COMMONLY_CONFUSED_WITH(halogen, halide ion) | NO CONFUSION STATEMENT + DOUBLE-COUNTING (the B3-H-13 rule) |
| B5-H-14 | REQUIRES_PREREQUISITE(CON-AIR-COMPOSITION, CON-NOBLE-GAS-INERTNESS) | OD-2 INCIDENTAL + UNAUDITED BOUNDARY |

Every held candidate cites its §19 failure class; the four CLASSIC wrong-answer patterns without pinned documentation are refused (the session-53 Step-3 rule). A held record is a valid outcome — the abstention is the system's honest output.

## 5. Operator verdict surface

- **18 SUGGESTED edges** (B5-E-01..18) — the §18 promotion surface
- **16 nodes** (13 CONCEPT B5-N-01..13 + 3 MISCONCEPTION B5-M-01..03) — node authority stays SUGGESTED; nodes have no §18 pathway (node promotion is a separate identity decision, deferred)
- **6 identity decisions** (B5-ID-01..06) — MERGE/SPLIT/KEEP_AS_IS
- **14 held candidates** — acknowledge the quarantine (no reopening)
- **0 REVIEW_REQUIRED edges** — zero RR settlements needed

Pathway: fill `scripts/c11_batch5_verdicts_template.yaml` → rename to `c11_batch5_verdicts.yaml` → a later session encodes + applies via `c11_verdict_encode_batch5`-style reconciliation + `c11_promote.py` (§18) + the gated generator re-run. NOTHING is promoted at this gate.

