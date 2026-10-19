# Phase 1 (T-C09) — Completeness Report

Generated 2026-09-10 by `scripts/c09_spec_graph_extract.py` (zero-LLM, deterministic).

Source: `international-gcse-chemistry-2017-specification-2026-09-10_12-18-50.md` (raw OCR) cross-checked statement-by-statement against the official `international-gcse-chemistry-2017-specification.pdf` (Issue 3).

## 1. Extraction results vs acceptance gates

| Gate | Target | Actual | Status |
|---|---|---|---|
| Unique spec-point codes | 182 | 182 | PASS |
| C-points | 52 | 52 | PASS |
| Sections (topics) | 4 | 4 | PASS |
| Subsections (subtopics) | 28 | 28 | PASS |
| Practical statements | 12 | 12 | PASS |
| Command-word entries | 25 | 25 | PASS |
| HTML tables classified | 45 | 45 | PASS |
| Spec-statement tables | 31 | 31 | PASS |
| PART_OF edges | 210 | 210 | PASS |

Per-section counts: S1: 60 (target 60) · S2: 50 (target 50) · S3: 22 (target 22) · S4: 50 (target 50)

## 2. Ground-truth baseline amendment (supersedes the plan's §5 numbers)

The build plan (`KNOWLEDGE_GRAPH_BUILD_PLAN.md` §5, Session 27) recorded a baseline of **167 codes / 40 C-points / 29 subsections**. The full PDF cross-check run during this extraction shows the official Issue-3 PDF contains **182 unique codes / 52 C-points / 28 subsections** (S1: 60, S2: 50, S3: 22, S4: 50). The plan's numbers predated the statement-level PDF reconciliation and are superseded by:

| Measure | Plan §5 (superseded) | PDF-verified (this run) | Evidence |
|---|---|---|---|
| Unique codes | 167 | **182** | line-anchored PDF scan, pages 16–32; set-equality with md parse |
| C-points | 40 | **52** | 14 (S1) + 12 (S2) + 8 (S3) + 18 (S4) |
| Subsections | 29 | **28** | real-header scan (two-line + 'Students should:' signature): S1 (a–i), S2 (a–h), S3 (a–c), S4 (a–h) |
| Two-col / colspan row split | 128 / 39 | **132 / 49 + 1 orphan pair** | row-shape census below; the md's (h) Synthetic polymers table loses two rows to the outside-the-table orphan emission |

The md itself contains all 182 statements, but **two of them (4.49C, 4.50C) were emitted by the OCR as plain text lines outside the HTML table** — a table-only row count under-reports the true total (181 in-table + 1 duplicate-truncated row). The 167 figure was produced by an earlier count that missed the S2/S4 totals and the orphan pair.

## 3. PDF cross-check (all 182 statements)

| Match level | Count | Meaning |
|---|---|---|
| exact | 119 | md text identical to PDF text |
| normalized | 52 | equal after space/punctuation/unicode-notation normalisation |
| fuzzy | 11 | similarity ≥ 0.90 after normalisation (residual OCR damage) |
| mismatch | 0 | below 0.90 — REVIEW REQUIRED |

Statement order md vs PDF: identical
Codes only in md: none
Codes only in PDF: none

## 4. Structural damage inventory (md OCR; documented, never fixed)

- **statement-continuation-row** — 3.22C: T24 r8: 'References to Le Chatelier's principle are not required' merged into 3.22C
- **statement-continuation-row** — 4.34C: T31 r3: 'C=O -CH2OH' merged into 4.34C
- **statement-continuation-row** — 4.38C: T32 r3: 'C - C - O -' merged into 4.38C
- **equation-block-attached** — 4.49C: md lines 587-589 attached to 4.49C
- **truncated-table-row-superseded** — 4.49C: 4.49C in-table row (T33 r7) truncated: 'understand how to write the structural and displayed formula of a polyester, showing the r...' — superseded by orphan line 585
- **subsection-reassigned-from-pdf** — 4.23: 4.23: md-walk said (c), PDF boundary map says (d) 'Alkenes'
- **subsection-reassigned-from-pdf** — 4.24: 4.24: md-walk said (c), PDF boundary map says (d) 'Alkenes'
- **subsection-reassigned-from-pdf** — 4.25: 4.25: md-walk said (c), PDF boundary map says (d) 'Alkenes'
- **subsection-reassigned-from-pdf** — 4.26: 4.26: md-walk said (c), PDF boundary map says (d) 'Alkenes'
- **subsection-reassigned-from-pdf** — 4.27: 4.27: md-walk said (c), PDF boundary map says (d) 'Alkenes'
- **subsection-reassigned-from-pdf** — 4.28: 4.28: md-walk said (c), PDF boundary map says (d) 'Alkenes'

## 5. Notation-damage census (heuristic; the pipeline lint owns fixes)

54 of 182 statements carry at least one damage flag. Counts by class:

| Damage flag | Statements |
|---|---|
| lost-space | 17 |
| latex-fragment | 13 |
| unknown-leading-verb | 9 |
| subsection-reassigned-from-pdf | 6 |
| full-width-punct | 4 |
| cjk-leak | 3 |
| lost-subscript | 3 |
| statement-continuation-row | 3 |
| orphaned-outside-table | 2 |
| code-space-damage | 2 |
| equation-rendered-as-latex-block | 1 |
| superseded-truncated-table-row | 1 |

These detectors are a census heuristic (regex classes from `CORPUS_REVIEW_2026-09-10.md` §3.1), not authoritative classification. Statement text in `specification_points.yaml` is verbatim-damaged.

## 6. 45-table classification census

| Index | Class | md line | Rows |
|---|---|---|---|
| T0 | changes_summary | 62 | 4 |
| T1 | paper_overview | 333 | 4 |
| T2 | paper_overview | 347 | 4 |
| T3 | spec_statement | 397 | 9 |
| T4 | spec_statement | 406 | 8 |
| T5 | spec_statement | 413 | 6 |
| T6 | spec_statement | 415 | 7 |
| T7 | spec_statement | 419 | 3 |
| T8 | spec_statement | 421 | 14 |
| T9 | spec_statement | 423 | 9 |
| T10 | spec_statement | 429 | 10 |
| T11 | spec_statement | 435 | 5 |
| T12 | spec_statement | 437 | 8 |
| T13 | spec_statement | 459 | 6 |
| T14 | spec_statement | 461 | 6 |
| T15 | spec_statement | 463 | 8 |
| T16 | spec_statement | 465 | 8 |
| T17 | spec_statement | 480 | 2 |
| T18 | spec_statement | 482 | 8 |
| T19 | spec_statement | 486 | 8 |
| T20 | spec_statement | 488 | 12 |
| T21 | spec_statement | 496 | 9 |
| T22 | spec_statement | 523 | 10 |
| T23 | spec_statement | 529 | 10 |
| T24 | spec_statement | 531 | 9 |
| T25 | spec_statement | 557 | 8 |
| T26 | spec_statement | 561 | 8 |
| T27 | spec_statement | 563 | 7 |
| T28 | spec_statement | 568 | 5 |
| T29 | spec_statement | 571 | 7 |
| T30 | spec_statement | 573 | 7 |
| T31 | spec_statement | 575 | 7 |
| T32 | spec_statement | 578 | 9 |
| T33 | spec_statement | 581 | 8 |
| T34 | assessment_info | 597 | 3 |
| T35 | ao_weightings | 641 | 5 |
| T36 | ao_by_unit | 645 | 5 |
| T37 | codes_appendix | 803 | 3 |
| T38 | cognitive_skills | 901 | 7 |
| T39 | maths_skills | 932 | 29 |
| T40 | maths_skills | 934 | 5 |
| T41 | command_words | 940 | 17 |
| T42 | command_words | 944 | 12 |
| T43 | periodic_table | 1008 | 6 |
| T44 | glossary | 1171 | 5 |

## 7. Subsection inventory (28)

| Code | Title (PDF) | Title (md) | Header source | Points | First–last code | PDF page |
|---|---|---|---|---|---|---|
| 4CH1-S1-a | States of matter | States of matter | md-table | 7 | 1.1 – 1.7C | 17 |
| 4CH1-S1-b | Elements, compounds and mixtures | Elements,compounds and mixtures | md-table | 6 | 1.8 – 1.13 | 18 |
| 4CH1-S1-c | Atomic structure | Atomic structure | md-table | 4 | 1.14 – 1.17 | 18 |
| 4CH1-S1-d | The Periodic Table | The Periodic Table | md-table | 7 | 1.18 – 1.24 | 18 |
| 4CH1-S1-e | Chemical formulae, equations and calculations | Chemical formulae, equations and calculations | md-table | 12 | 1.25 – 1.36 | 19 |
| 4CH1-S1-f | Ionic bonding | Ionic bonding | md-table | 7 | 1.37 – 1.43 | 20 |
| 4CH1-S1-g | Covalent bonding | Covalent bonding | md-table | 8 | 1.44 – 1.51 | 20 |
| 4CH1-S1-h | Metallic bonding | Metallic bonding | md-table | 3 | 1.52C – 1.54C | 21 |
| 4CH1-S1-i | Electrolysis | Electrolysis | md-table | 6 | 1.55C – 1.60C | 21 |
| 4CH1-S2-a | Group 1 (alkali metals) – lithium, sodium and potassium | Group1(alkali metals)-lithium,sodium and potassium | md-table | 4 | 2.1 – 2.4C | 22 |
| 4CH1-S2-b | Group 7 (halogens) – chlorine, bromine and iodine | Group 7(halogens)-chlorine,bromine and iodine | md-table | 4 | 2.5 – 2.8C | 22 |
| 4CH1-S2-c | Gases in the atmosphere | Gases in the atmosphere | md-table | 6 | 2.9 – 2.14 | 23 |
| 4CH1-S2-d | Reactivity series | Reactivity series | md-table | 7 | 2.15 – 2.21 | 23 |
| 4CH1-S2-e | Extraction and uses of metals | Extraction and uses of metals | md-table | 6 | 2.22C – 2.27C | 24 |
| 4CH1-S2-f | Acids, alkalis and titrations | Acids, alkalis and titrations | md-table | 6 | 2.28 – 2.33C | 24 |
| 4CH1-S2-g | Acids, bases and salt preparations | Acids, bases and salt preparations | md-table | 10 | 2.34 – 2.43C | 25 |
| 4CH1-S2-h | Chemical tests | Chemical tests | md-table | 7 | 2.44 – 2.50 | 26 |
| 4CH1-S3-a | Energetics | Energetics | md-table | 8 | 3.1 – 3.8 | 27 |
| 4CH1-S3-b | Rates of reaction | Rates of reaction | md-table | 8 | 3.9 – 3.16 | 28 |
| 4CH1-S3-c | Reversible reactions and equilibria | Reversible reactions and equilibria | md-table | 6 | 3.17 – 3.22C | 28 |
| 4CH1-S4-a | Introduction | Introduction | md-table | 6 | 4.1 – 4.6 | 29 |
| 4CH1-S4-b | Crude oil | Crude oil | md-table | 12 | 4.7 – 4.18 | 29 |
| 4CH1-S4-c | Alkanes | Alkanes | md-table | 4 | 4.19 – 4.22 | 30 |
| 4CH1-S4-d | Alkenes | None | pdf-recovered | 6 | 4.23 – 4.28 | 30 |
| 4CH1-S4-e | Alcohols | Alcohols | md-table | 5 | 4.29C – 4.33C | 31 |
| 4CH1-S4-f | Carboxylic acids | Carboxylic acids | md-table | 4 | 4.34C – 4.37C | 31 |
| 4CH1-S4-g | Esters | Esters | md-table | 6 | 4.38C – 4.43C | 32 |
| 4CH1-S4-h | Synthetic polymers | Synthetic polymers | md-table | 7 | 4.44 – 4.50C | 32 |

## 8. Practical inventory (12)

- `4CH1-1.7C` (a): practical: investigate the solubility of a solid in water at a specific temperature
- `4CH1-1.13` (b): practical: investigate paper chromatography using inks/food colourings
- `4CH1-1.36` (e): practical:know how to determine the formula of a metal oxide by combustion(e.g.magnesium oxide)or by reduction(e.g.copper(II)oxide)
- `4CH1-1.60C` (i): practical: investigate the electrolysis of aqueous solutions
- `4CH1-2.14` (c): practical:determine the approximate percentage by volume of oxygen in air using a metal or a non-metal
- `4CH1-2.21` (d): practical: investigate reactions between dilute hydrochloric and sulfuric acids and metals(e.g. magnesium, zinc and iron)
- `4CH1-2.42` (g): practical:prepare a sample of pure,dry hydrated copper(II)sulfate crystals starting from copper(II)oxide
- `4CH1-2.43C` (g): practical:prepare a sample of pure,dry lead(II)sulfate
- `4CH1-3.8` (a): practical: investigate temperature changes accompanying some of the following types of change: • salts dissolving in water • neutralisation reactions 
- `4CH1-3.15` (b): practical: investigate the effect of changing the surface area of marble chips and of changing the concentration of hydrochloric acid on the rate of r
- `4CH1-3.16` (b): practical: investigate the effect of different solids on the catalytic decomposition of hydrogen peroxide solution
- `4CH1-4.43C` (g): practical: prepare a sample of an ester such as ethyl ethanoate

## 9. Command-word inventory (25 = 23 main + 2 categorised)

- **Add/Label** (main)
- **Calculate** (main)
- **Comment on** (main)
- **Complete** (main)
- **Deduce** (main)
- **Describe** (main)
- **Determine** (main)
- **Design** (main)
- **Discuss** (main)
- **Draw** (main)
- **Estimate** (main)
- **Evaluate** (main)
- **Explain** (main)
- **Give/State/Name** (main)
- **Give a reason/reasons** (main)
- **Identify** (main)
- **Justify** (main)
- **Plot** (main)
- **Predict** (main)
- **Show that** (main)
- **Sketch** (main)
- **State what is meant by** (main)
- **Suggest** (main)
- **Analyse the data/graph to explain** (verb-preceding-command-word)
- **What,Why,Which** (multiple-choice-questions)

## 10. C-point applicability rule (grounded)

From the PDF (p. 7): 'specification statements that are in bold with a 'C' reference relate to content that is only in the International GCSE in Chemistry and is not found in the International GCSE in Science (Double Award)'. Paper 1C (shared with 4SD0/1C) 'assesses core content that is not in bold and does not have a 'C' reference'; Paper 2C 'assesses all the content, including content that is in bold and has a 'C' reference' (pp. 13–14). Therefore: non-C points → papers 1C+2C, shared with Double Award; C points → Paper 2C only, Chemistry-only.

## 11. Skill-tag census (leading verbs → draft SKILL tags)

| Verb | Statements | Mapped skill tag |
|---|---|---|
| know | 56 | 4CH1-SK-KNOW |
| understand | 54 | 4CH1-SK-UNDERSTAND |
| describe | 27 | 4CH1-SK-DESCRIBE |
| explain | 16 | 4CH1-SK-EXPLAIN |
| investigate | 7 | 4CH1-SK-INVESTIGATE |
| calculate | 6 | 4CH1-SK-CALCULATE |
| write | 3 | 4CH1-SK-WRITE |
| draw | 3 | 4CH1-SK-DRAW |
| use | 3 | UNMAPPED — flagged `unknown-leading-verb` |
| prepare | 3 | UNMAPPED — flagged `unknown-leading-verb` |
| be | 2 | UNMAPPED — flagged `unknown-leading-verb` |
| identify | 1 | UNMAPPED — flagged `unknown-leading-verb` |
| determine | 1 | 4CH1-SK-DETERMINE |

Practical statements additionally carry `4CH1-SK-PRACTICAL`.

## 12. Operator review actions

1. **Spot-check**: open `SPOT_CHECK_SHEET.md`, compare the 20 sampled statements against the PDF (semantic match; notation damage is expected and acceptable, wording differences beyond notation are not).
2. **PR review**: the `graph/*.yaml` files are the Phase-1 deliverable — git PR is the HUMAN_VALIDATED gate (promotion happens at review, not here).
3. Known-open items: the REVIEW list in §3 (if non-empty) and any `unknown-leading-verb` entries in §11.
