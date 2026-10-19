# C11 Diff Review Bundle — pending §18 edge promotions (generated 2026-09-12)

- baseline commit: `5715396`
- state fingerprint: `3cefbe260722` (promo_count=0)
- actionable: 28 edges (clean 28 / pending-flagged 0); not-actionable: 4; nodes awaiting a pathway: 29
- preview fidelity: simulator re-emits graph/concept_edges.yaml under the generator's own serialization contract with a byte-identity guard — what you read is what G13 will write.

## Batch approval

```bash
cd work/syllabai-resources && python3 scripts/c11_diff_review.py approve \
  '4CH1-CON-CONC-CALC REQUIRES_PREREQUISITE 4CH1-CON-MOLE' \
  '4CH1-CON-CONC-CALC REQUIRES_PREREQUISITE 4CH1-CON-VOL-CONVERSION' \
  '4CH1-CON-EMP-MOL-CALC REQUIRES_PREREQUISITE 4CH1-CON-AR' \
  '4CH1-CON-EMP-MOL-CALC REQUIRES_PREREQUISITE 4CH1-CON-EMPIRICAL-FORMULA' \
  '4CH1-CON-EMP-MOL-CALC REQUIRES_PREREQUISITE 4CH1-CON-MOLE' \
  '4CH1-CON-EQ-SYMBOL EXPLAINED_BY 4CH1-CON-CONSERVATION-MASS' \
  '4CH1-CON-EXP-FORMULA-DEDUCTION REQUIRES_PREREQUISITE 4CH1-CON-MOLE' \
  '4CH1-CON-GAS-VOL-CALC REQUIRES_PREREQUISITE 4CH1-CON-MOLAR-GAS-VOL' \
  '4CH1-CON-GAS-VOL-CALC REQUIRES_PREREQUISITE 4CH1-CON-MOLE-MASS-CONV' \
  '4CH1-CON-MOLAR-GAS-VOL REQUIRES_PREREQUISITE 4CH1-CON-MOLE' \
  '4CH1-CON-MOLAR-MASS REQUIRES_PREREQUISITE 4CH1-CON-AR' \
  '4CH1-CON-MOLAR-MASS REQUIRES_PREREQUISITE 4CH1-CON-MOLE' \
  '4CH1-CON-MOLAR-MASS REQUIRES_PREREQUISITE 4CH1-CON-MR' \
  '4CH1-CON-MOLE-MASS-CONV REQUIRES_PREREQUISITE 4CH1-CON-MOLAR-MASS' \
  '4CH1-CON-MOLECULAR-FORMULA REQUIRES_PREREQUISITE 4CH1-CON-EMPIRICAL-FORMULA' \
  '4CH1-CON-MOLECULAR-FORMULA REQUIRES_PREREQUISITE 4CH1-CON-MR' \
  '4CH1-CON-MR REQUIRES_PREREQUISITE 4CH1-CON-AR' \
  '4CH1-CON-PERCENT-YIELD REQUIRES_PREREQUISITE 4CH1-CON-THEOR-YIELD' \
  '4CH1-CON-PERCENT-YIELD REQUIRES_PREREQUISITE 4CH1-CON-YIELD' \
  '4CH1-CON-REACTING-MASS REQUIRES_PREREQUISITE 4CH1-CON-MOLAR-RATIO' \
  '4CH1-CON-REACTING-MASS REQUIRES_PREREQUISITE 4CH1-CON-MOLE-MASS-CONV' \
  '4CH1-CON-THEOR-YIELD REQUIRES_PREREQUISITE 4CH1-CON-REACTING-MASS' \
  '4CH1-CON-WATER-CRYST REQUIRES_PREREQUISITE 4CH1-CON-EMP-MOL-CALC' \
  '4CH1-CON-YIELD EXPLAINED_BY 4CH1-CON-YIELD-FACTORS' \
  '4CH1-MIS-CONC-UNIT REMEDIATED_BY 4CH1-CON-VOL-CONVERSION' \
  '4CH1-MIS-CONC-UNIT WRONG_ANSWER_PATTERN 4CH1-CON-CONC-CALC' \
  '4CH1-MIS-EQ-SUBSCRIPT MISCONCEPTION_OF 4CH1-CON-EQ-SYMBOL' \
  '4CH1-PR-03 REQUIRES_PREREQUISITE 4CH1-CON-EXP-FORMULA-DEDUCTION' \
  --by <operator> --date 2026-09-12 --review-ref graph/reports/C11_DIFF_REVIEW_2026-09-12.md
```

Pending-flagged (PENDING operator_decision) edges are excluded from the command above; approving them additionally requires `--include-pending` — that flag records the explicit decision this bundle presents.

## Index

| # | identity | confidence | flag |
|---|----------|------------|------|
| 1 | `4CH1-CON-CONC-CALC REQUIRES_PREREQUISITE 4CH1-CON-MOLE` | high |  |
| 2 | `4CH1-CON-CONC-CALC REQUIRES_PREREQUISITE 4CH1-CON-VOL-CONVERSION` | high |  |
| 3 | `4CH1-CON-EMP-MOL-CALC REQUIRES_PREREQUISITE 4CH1-CON-AR` | high |  |
| 4 | `4CH1-CON-EMP-MOL-CALC REQUIRES_PREREQUISITE 4CH1-CON-EMPIRICAL-FORMULA` | high |  |
| 5 | `4CH1-CON-EMP-MOL-CALC REQUIRES_PREREQUISITE 4CH1-CON-MOLE` | high |  |
| 6 | `4CH1-CON-EQ-SYMBOL EXPLAINED_BY 4CH1-CON-CONSERVATION-MASS` | high |  |
| 7 | `4CH1-CON-EXP-FORMULA-DEDUCTION REQUIRES_PREREQUISITE 4CH1-CON-MOLE` | high |  |
| 8 | `4CH1-CON-GAS-VOL-CALC REQUIRES_PREREQUISITE 4CH1-CON-MOLAR-GAS-VOL` | high |  |
| 9 | `4CH1-CON-GAS-VOL-CALC REQUIRES_PREREQUISITE 4CH1-CON-MOLE-MASS-CONV` | high |  |
| 10 | `4CH1-CON-MOLAR-GAS-VOL REQUIRES_PREREQUISITE 4CH1-CON-MOLE` | high |  |
| 11 | `4CH1-CON-MOLAR-MASS REQUIRES_PREREQUISITE 4CH1-CON-AR` | high |  |
| 12 | `4CH1-CON-MOLAR-MASS REQUIRES_PREREQUISITE 4CH1-CON-MOLE` | high |  |
| 13 | `4CH1-CON-MOLAR-MASS REQUIRES_PREREQUISITE 4CH1-CON-MR` | high |  |
| 14 | `4CH1-CON-MOLE-MASS-CONV REQUIRES_PREREQUISITE 4CH1-CON-MOLAR-MASS` | high |  |
| 15 | `4CH1-CON-MOLECULAR-FORMULA REQUIRES_PREREQUISITE 4CH1-CON-EMPIRICAL-FORMULA` | high |  |
| 16 | `4CH1-CON-MOLECULAR-FORMULA REQUIRES_PREREQUISITE 4CH1-CON-MR` | high |  |
| 17 | `4CH1-CON-MR REQUIRES_PREREQUISITE 4CH1-CON-AR` | high |  |
| 18 | `4CH1-CON-PERCENT-YIELD REQUIRES_PREREQUISITE 4CH1-CON-THEOR-YIELD` | high |  |
| 19 | `4CH1-CON-PERCENT-YIELD REQUIRES_PREREQUISITE 4CH1-CON-YIELD` | high |  |
| 20 | `4CH1-CON-REACTING-MASS REQUIRES_PREREQUISITE 4CH1-CON-MOLAR-RATIO` | high |  |
| 21 | `4CH1-CON-REACTING-MASS REQUIRES_PREREQUISITE 4CH1-CON-MOLE-MASS-CONV` | high |  |
| 22 | `4CH1-CON-THEOR-YIELD REQUIRES_PREREQUISITE 4CH1-CON-REACTING-MASS` | high |  |
| 23 | `4CH1-CON-WATER-CRYST REQUIRES_PREREQUISITE 4CH1-CON-EMP-MOL-CALC` | high |  |
| 24 | `4CH1-CON-YIELD EXPLAINED_BY 4CH1-CON-YIELD-FACTORS` | high |  |
| 25 | `4CH1-MIS-CONC-UNIT REMEDIATED_BY 4CH1-CON-VOL-CONVERSION` | high |  |
| 26 | `4CH1-MIS-CONC-UNIT WRONG_ANSWER_PATTERN 4CH1-CON-CONC-CALC` | high |  |
| 27 | `4CH1-MIS-EQ-SUBSCRIPT MISCONCEPTION_OF 4CH1-CON-EQ-SYMBOL` | high |  |
| 28 | `4CH1-PR-03 REQUIRES_PREREQUISITE 4CH1-CON-EXP-FORMULA-DEDUCTION` | high |  |

## Pending items — the exact diff each approval applies

### 1. `4CH1-CON-CONC-CALC REQUIRES_PREREQUISITE 4CH1-CON-MOLE` [high]

- node 4CH1-CON-CONC-CALC — Concentration calculation (mol/dm3) (CONCEPT)
-   spec 4CH1-1.34C [CORE]: understand how to carry out calculations involving amount of substance, volume and concentrat...
- node 4CH1-CON-MOLE — The mole (unit of amount of substance) (CONCEPT)
-   spec 4CH1-1.27 [CORE]: know that the mole(mol) is the unit for the amount of a substance
- derivation: USED_WITHOUT_RETEACHING — Every 1.34C formula instance computes an amount in moles; the mole is never defined in this note (the 1.27 note's job).
- `NOTE` Solution concentration - IGCSE Chemistry Revision Notes.md — "Calculate the amount of solute, in moles, present in 2.5 dm3 of a solution whose concentration is 0.2 mol /..."

```diff
@@ -909,7 +912,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.34C @ Solution concentration (2026-09-11)
     generated_date: '2026-09-11'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-11'
 - source: 4CH1-CON-CONC-CALC
```

### 2. `4CH1-CON-CONC-CALC REQUIRES_PREREQUISITE 4CH1-CON-VOL-CONVERSION` [high]

- node 4CH1-CON-CONC-CALC — Concentration calculation (mol/dm3) (CONCEPT)
-   spec 4CH1-1.34C [CORE]: understand how to carry out calculations involving amount of substance, volume and concentrat...
- node 4CH1-CON-VOL-CONVERSION — Volume unit conversion (cm3/dm3) (CONCEPT)
-   spec 4CH1-1.34C [CORE]: understand how to carry out calculations involving amount of substance, volume and concentrat...
- derivation: USED_WITHOUT_RETEACHING — The rule is stated once and then enforced as a Remember-warning in worked examples 2 and 3; the mark-scheme wrong-answer pattern (failing to divide by 1000) independently confirms this is the operative sub-skill where candidates fail.
- `NOTE` Solution concentration - IGCSE Chemistry Revision Notes.md — "Remember: The volume needs to be in dm3"

```diff
@@ -931,7 +934,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.34C @ Solution concentration (2026-09-11); PMT CFEC2 MS Q4(a)
     generated_date: '2026-09-11'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-11'
 - source: 4CH1-CON-EMP-MOL-CALC
```

### 3. `4CH1-CON-EMP-MOL-CALC REQUIRES_PREREQUISITE 4CH1-CON-AR` [high]

- node 4CH1-CON-EMP-MOL-CALC — Empirical and molecular formula calculation (CONCEPT)
-   spec 4CH1-1.33 [CORE]: calculate empirical and molecular formulae from experimental data
- node 4CH1-CON-AR — Relative atomic mass (Ar) (CONCEPT)
-   spec 4CH1-1.26 [CORE]: calculate relative formula masses(including relative molecular masses) $ (M_{r}) $ from relat...
-   spec 4CH1-1.28 [CORE]: understand how to carry out calculations involving amount of substance, relative atomic mass ...
- derivation: USED_WITHOUT_RETEACHING — Procedure step 3 uses Ar values as given inputs; where Ar values come from is never taught in this note (the 1.26/periodic-table territory).
- `NOTE` Empirical & Molecular Formulae  Edexcel IGCSE Chemistry Revision Notes 2017.md — "Write the relative atomic mass of each element"

```diff
@@ -952,7 +955,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.33 @ Empirical & Molecular Formulae (2026-09-11)
     generated_date: '2026-09-11'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-11'
 - source: 4CH1-CON-EMP-MOL-CALC
```

### 4. `4CH1-CON-EMP-MOL-CALC REQUIRES_PREREQUISITE 4CH1-CON-EMPIRICAL-FORMULA` [high]

- node 4CH1-CON-EMP-MOL-CALC — Empirical and molecular formula calculation (CONCEPT)
-   spec 4CH1-1.33 [CORE]: calculate empirical and molecular formulae from experimental data
- node 4CH1-CON-EMPIRICAL-FORMULA — Empirical formula (CONCEPT)
-   spec 4CH1-1.32 [CORE]: know what is meant by the terms empirical formula and molecular formula
-   spec 4CH1-1.33 [CORE]: calculate empirical and molecular formulae from experimental data
- derivation: DEFINITIONAL_DEPENDENCY — The procedure's step 6 outputs an empirical formula; steps 5-6 operate on the simplest-whole-number-ratio definition taught in the same note's definition section (and demanded by 1.32).
- `NOTE` Empirical & Molecular Formulae  Edexcel IGCSE Chemistry Revision Notes 2017.md — "Write the final empirical formula"

```diff
@@ -973,7 +976,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.32 + 4CH1-1.33 @ Empirical & Molecular Formulae (2026-09-11)
     generated_date: '2026-09-11'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-11'
 - source: 4CH1-CON-EMP-MOL-CALC
```

### 5. `4CH1-CON-EMP-MOL-CALC REQUIRES_PREREQUISITE 4CH1-CON-MOLE` [high]

- node 4CH1-CON-EMP-MOL-CALC — Empirical and molecular formula calculation (CONCEPT)
-   spec 4CH1-1.33 [CORE]: calculate empirical and molecular formulae from experimental data
- node 4CH1-CON-MOLE — The mole (unit of amount of substance) (CONCEPT)
-   spec 4CH1-1.27 [CORE]: know that the mole(mol) is the unit for the amount of a substance
- derivation: USED_WITHOUT_RETEACHING — Procedure step 4 instructs "Calculate the moles of each element" without the note ever defining the mole (the 1.27 note's job) — textbook use-without-reteaching.
- `NOTE` Empirical & Molecular Formulae  Edexcel IGCSE Chemistry Revision Notes 2017.md — "Calculate the moles of each element"

```diff
@@ -994,7 +997,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.33 @ Empirical & Molecular Formulae (2026-09-11)
     generated_date: '2026-09-11'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-11'
 - source: 4CH1-CON-EXP-FORMULA-DEDUCTION
```

### 6. `4CH1-CON-EQ-SYMBOL EXPLAINED_BY 4CH1-CON-CONSERVATION-MASS` [high]

- node 4CH1-CON-EQ-SYMBOL — Balanced symbol (chemical) equation (CONCEPT)
-   spec 4CH1-1.25 [CORE]: write word equations and balanced chemical equations(including state symbols):for reactions s...
- node 4CH1-CON-CONSERVATION-MASS — Law of Conservation of Mass (CONCEPT)
-   spec 4CH1-1.25 [CORE]: write word equations and balanced chemical equations(including state symbols):for reactions s...
-   spec 4CH1-1.26 [SUPPORTING]: calculate relative formula masses(including relative molecular masses) $ (M_{r}) $ from relat...
- derivation: SINGLE_SOURCE_CAUSAL_TEACHING — Single-anchor causal teaching: the one sentence teaches the explanatory link itself ("enables us to ... since ..."). This is the relation the 4.15 negative-control class forbids constructing from premise+consequence aggregation.
- `NOTE` Writing chemical equations - IGCSE Chemistry Revision Notes.md — "The Law of Conservation of Mass enables us to balance chemical equations, since no atoms can be lost or cre..."

```diff
@@ -1452,7 +1455,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.25 @ Writing chemical equations (2026-09-11)
     generated_date: '2026-09-11'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-11'
 - source: 4CH1-CON-MOLAR-GAS-VOL
```

### 7. `4CH1-CON-EXP-FORMULA-DEDUCTION REQUIRES_PREREQUISITE 4CH1-CON-MOLE` [high]

- node 4CH1-CON-EXP-FORMULA-DEDUCTION — Experimental formula deduction (mass-difference method) (CONCEPT)
-   spec 4CH1-1.31 [CORE]: understand how the formulae of simple compounds can be obtained experimentally, including met...
-   spec 4CH1-1.36 [CORE]: practical:know how to determine the formula of a metal oxide by combustion(e.g.magnesium oxid...
- node 4CH1-CON-MOLE — The mole (unit of amount of substance) (CONCEPT)
-   spec 4CH1-1.27 [CORE]: know that the mole(mol) is the unit for the amount of a substance
- derivation: USED_WITHOUT_RETEACHING — The deduction method's core move is mass -> moles; the note never defines the mole (the 1.27 note's job).
- `NOTE` Simple compound formulae - IGCSE Chemistry Revision Notes.md — "The principle is to use mass measurements before and after a reaction and then convert masses into moles"

```diff
@@ -1016,7 +1019,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.31 @ Simple compound formulae (2026-09-11)
     generated_date: '2026-09-11'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-11'
 - source: 4CH1-CON-GAS-VOL-CALC
```

### 8. `4CH1-CON-GAS-VOL-CALC REQUIRES_PREREQUISITE 4CH1-CON-MOLAR-GAS-VOL` [high]

- node 4CH1-CON-GAS-VOL-CALC — Gas volume calculation (CONCEPT)
-   spec 4CH1-1.35C [CORE]: understand how to carry out calculations involving gas volumes and the molar volume of a gas(...
- node 4CH1-CON-MOLAR-GAS-VOL — Molar gas volume at RTP (24 dm3) (CONCEPT)
-   spec 4CH1-1.35C [CORE]: understand how to carry out calculations involving gas volumes and the molar volume of a gas(...
- derivation: DEFINITIONAL_DEPENDENCY — The calculation formula is stated in terms of the molar volume (both the dm3 and cm3 forms with their respective constants).
- `NOTE` Calculate Gas Volumes - IGCSE Chemistry Revision Notes.md — "Volume = Moles x Molar Volume"

```diff
@@ -1062,7 +1065,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.35C @ Calculate Gas Volumes (2026-09-11)
     generated_date: '2026-09-11'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-11'
 - source: 4CH1-CON-GAS-VOL-CALC
```

### 9. `4CH1-CON-GAS-VOL-CALC REQUIRES_PREREQUISITE 4CH1-CON-MOLE-MASS-CONV` [high]

- node 4CH1-CON-GAS-VOL-CALC — Gas volume calculation (CONCEPT)
-   spec 4CH1-1.35C [CORE]: understand how to carry out calculations involving gas volumes and the molar volume of a gas(...
- node 4CH1-CON-MOLE-MASS-CONV — Mole-mass conversion (CONCEPT)
-   spec 4CH1-1.28 [CORE]: understand how to carry out calculations involving amount of substance, relative atomic mass ...
- derivation: USED_WITHOUT_RETEACHING — Cross-SP dependency 1.35C -> 1.28: the mass-route gas questions explicitly chain grams -> moles -> volume with the mole-mass conversion used as a given.
- `NOTE` Calculate Gas Volumes - IGCSE Chemistry Revision Notes.md — "To answer these type of questions you must first convert grams to moles and then calculate the volume."

```diff
@@ -1084,7 +1087,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.35C @ Calculate Gas Volumes (2026-09-11)
     generated_date: '2026-09-11'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-11'
 - source: 4CH1-CON-MOLAR-GAS-VOL
```

### 10. `4CH1-CON-MOLAR-GAS-VOL REQUIRES_PREREQUISITE 4CH1-CON-MOLE` [high]

- node 4CH1-CON-MOLAR-GAS-VOL — Molar gas volume at RTP (24 dm3) (CONCEPT)
-   spec 4CH1-1.35C [CORE]: understand how to carry out calculations involving gas volumes and the molar volume of a gas(...
- node 4CH1-CON-MOLE — The mole (unit of amount of substance) (CONCEPT)
-   spec 4CH1-1.27 [CORE]: know that the mole(mol) is the unit for the amount of a substance
- derivation: DEFINITIONAL_DEPENDENCY — The molar gas volume is defined per mole ("the volume occupied by one mole of any gas"); the definition presupposes the mole concept.
- `NOTE` Calculate Gas Volumes - IGCSE Chemistry Revision Notes.md — "At room temperature and pressure, the volume occupied by one mole of any gas was found to be 24 dm3 or 24,0..."

```diff
@@ -1106,7 +1109,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.35C @ Calculate Gas Volumes (2026-09-11)
     generated_date: '2026-09-11'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-11'
 - source: 4CH1-CON-MOLAR-MASS
```

### 11. `4CH1-CON-MOLAR-MASS REQUIRES_PREREQUISITE 4CH1-CON-AR` [high]

- node 4CH1-CON-MOLAR-MASS — Molar mass (CONCEPT)
-   spec 4CH1-1.28 [CORE]: understand how to carry out calculations involving amount of substance, relative atomic mass ...
- node 4CH1-CON-AR — Relative atomic mass (Ar) (CONCEPT)
-   spec 4CH1-1.26 [CORE]: calculate relative formula masses(including relative molecular masses) $ (M_{r}) $ from relat...
-   spec 4CH1-1.28 [CORE]: understand how to carry out calculations involving amount of substance, relative atomic mass ...
- derivation: DEFINITIONAL_DEPENDENCY — Molar mass of an element is defined as its Ar in grams; the mapped note links them explicitly (Na/He/Li examples).
- `NOTE` Calculating moles and mass - IGCSE Chemistry Revision Notes.md — "For an element, it is the same as the relative atomic mass written in grams"

```diff
@@ -1127,7 +1130,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.28 @ Calculating moles and mass (2026-09-11)
     generated_date: '2026-09-11'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-11'
 - source: 4CH1-CON-MOLAR-MASS
```

### 12. `4CH1-CON-MOLAR-MASS REQUIRES_PREREQUISITE 4CH1-CON-MOLE` [high]

- node 4CH1-CON-MOLAR-MASS — Molar mass (CONCEPT)
-   spec 4CH1-1.28 [CORE]: understand how to carry out calculations involving amount of substance, relative atomic mass ...
- node 4CH1-CON-MOLE — The mole (unit of amount of substance) (CONCEPT)
-   spec 4CH1-1.27 [CORE]: know that the mole(mol) is the unit for the amount of a substance
- derivation: DEFINITIONAL_DEPENDENCY — Molar mass is defined per mole ("the mass of 1 mole"); the definition presupposes the mole concept.
- `NOTE` Calculating moles and mass - IGCSE Chemistry Revision Notes.md — "The mass of 1 mole of a substance is known as the molar mass"

```diff
@@ -1148,7 +1151,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.28 @ Calculating moles and mass (2026-09-11)
     generated_date: '2026-09-11'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-11'
 - source: 4CH1-CON-MOLAR-MASS
```

### 13. `4CH1-CON-MOLAR-MASS REQUIRES_PREREQUISITE 4CH1-CON-MR` [high]

- node 4CH1-CON-MOLAR-MASS — Molar mass (CONCEPT)
-   spec 4CH1-1.28 [CORE]: understand how to carry out calculations involving amount of substance, relative atomic mass ...
- node 4CH1-CON-MR — Relative formula mass (Mr) (CONCEPT)
-   spec 4CH1-1.26 [CORE]: calculate relative formula masses(including relative molecular masses) $ (M_{r}) $ from relat...
-   spec 4CH1-1.28 [CORE]: understand how to carry out calculations involving amount of substance, relative atomic mass ...
- derivation: DEFINITIONAL_DEPENDENCY — Molar mass of a compound is defined numerically as its Mr in grams; the mapped note links them explicitly and uses Mr in every compound worked example.
- `NOTE` Calculating moles and mass - IGCSE Chemistry Revision Notes.md — "For a compound, it is the same as the relative molecular or formula mass in grams"

```diff
@@ -1169,7 +1172,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.28 @ Calculating moles and mass (2026-09-11)
     generated_date: '2026-09-11'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-11'
 - source: 4CH1-CON-MOLE-MASS-CONV
```

### 14. `4CH1-CON-MOLE-MASS-CONV REQUIRES_PREREQUISITE 4CH1-CON-MOLAR-MASS` [high]

- node 4CH1-CON-MOLE-MASS-CONV — Mole-mass conversion (CONCEPT)
-   spec 4CH1-1.28 [CORE]: understand how to carry out calculations involving amount of substance, relative atomic mass ...
- node 4CH1-CON-MOLAR-MASS — Molar mass (CONCEPT)
-   spec 4CH1-1.28 [CORE]: understand how to carry out calculations involving amount of substance, relative atomic mass ...
- derivation: DEFINITIONAL_DEPENDENCY — The conversion formula (mass = moles x molar mass and rearrangements) contains the molar mass; the mapped note teaches molar mass first, then the conversion.
- `NOTE` Calculating moles and mass - IGCSE Chemistry Revision Notes.md — "The mass is calculated by moles x molar mass"

```diff
@@ -1190,7 +1193,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.28 @ Calculating moles and mass (2026-09-11)
     generated_date: '2026-09-11'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-11'
 - source: 4CH1-CON-MOLECULAR-FORMULA
```

### 15. `4CH1-CON-MOLECULAR-FORMULA REQUIRES_PREREQUISITE 4CH1-CON-EMPIRICAL-FORMULA` [high]

- node 4CH1-CON-MOLECULAR-FORMULA — Molecular formula (CONCEPT)
-   spec 4CH1-1.32 [CORE]: know what is meant by the terms empirical formula and molecular formula
-   spec 4CH1-1.33 [CORE]: calculate empirical and molecular formulae from experimental data
- node 4CH1-CON-EMPIRICAL-FORMULA — Empirical formula (CONCEPT)
-   spec 4CH1-1.32 [CORE]: know what is meant by the terms empirical formula and molecular formula
-   spec 4CH1-1.33 [CORE]: calculate empirical and molecular formulae from experimental data
- derivation: USED_WITHOUT_RETEACHING — The molecular-formula derivation procedure (note step 1-3) takes the empirical formula as its input and scales it; the taught relationship table (methane/ethane/ethene/benzene) presupposes both concepts.
- `NOTE` Empirical & Molecular Formulae  Edexcel IGCSE Chemistry Revision Notes 2017.md — "Find the relative formula mass of the empirical formula"

```diff
@@ -1212,7 +1215,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.32 + 4CH1-1.33 @ Empirical & Molecular Formulae (2026-09-11)
     generated_date: '2026-09-11'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-11'
 - source: 4CH1-CON-MOLECULAR-FORMULA
```

### 16. `4CH1-CON-MOLECULAR-FORMULA REQUIRES_PREREQUISITE 4CH1-CON-MR` [high]

- node 4CH1-CON-MOLECULAR-FORMULA — Molecular formula (CONCEPT)
-   spec 4CH1-1.32 [CORE]: know what is meant by the terms empirical formula and molecular formula
-   spec 4CH1-1.33 [CORE]: calculate empirical and molecular formulae from experimental data
- node 4CH1-CON-MR — Relative formula mass (Mr) (CONCEPT)
-   spec 4CH1-1.26 [CORE]: calculate relative formula masses(including relative molecular masses) $ (M_{r}) $ from relat...
-   spec 4CH1-1.28 [CORE]: understand how to carry out calculations involving amount of substance, relative atomic mass ...
- derivation: USED_WITHOUT_RETEACHING — The scaling factor is Mr(molecular)/Mr(empirical); both Mr computations are used as given skills (the 1.26 note's job).
- `NOTE` Empirical & Molecular Formulae  Edexcel IGCSE Chemistry Revision Notes 2017.md — "Add the relative atomic masses of all the atoms in the empirical formula"

```diff
@@ -1233,7 +1236,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.33 @ Empirical & Molecular Formulae (2026-09-11)
     generated_date: '2026-09-11'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-11'
 - source: 4CH1-CON-MR
```

### 17. `4CH1-CON-MR REQUIRES_PREREQUISITE 4CH1-CON-AR` [high]

- node 4CH1-CON-MR — Relative formula mass (Mr) (CONCEPT)
-   spec 4CH1-1.26 [CORE]: calculate relative formula masses(including relative molecular masses) $ (M_{r}) $ from relat...
-   spec 4CH1-1.28 [CORE]: understand how to carry out calculations involving amount of substance, relative atomic mass ...
- node 4CH1-CON-AR — Relative atomic mass (Ar) (CONCEPT)
-   spec 4CH1-1.26 [CORE]: calculate relative formula masses(including relative molecular masses) $ (M_{r}) $ from relat...
-   spec 4CH1-1.28 [CORE]: understand how to carry out calculations involving amount of substance, relative atomic mass ...
- derivation: DEFINITIONAL_DEPENDENCY — Mr is computed BY summing Ar values (the 1.26 demand itself); every worked example in the mapped note takes Ar values as inputs without re-deriving them.
- `NOTE` Calculate Relative Mass  Edexcel IGCSE Chemistry Revision Notes 2017.md — "To calculate the Mr of a substance, you have to add up the relative atomic masses of all the atoms present ..."

```diff
@@ -1255,7 +1258,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.26 @ Calculate Relative Mass (2026-09-11)
     generated_date: '2026-09-11'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-11'
 - source: 4CH1-CON-PERCENT-YIELD
```

### 18. `4CH1-CON-PERCENT-YIELD REQUIRES_PREREQUISITE 4CH1-CON-THEOR-YIELD` [high]

- node 4CH1-CON-PERCENT-YIELD — Percentage yield (CONCEPT)
-   spec 4CH1-1.30 [CORE]: calculate percentage yield
- node 4CH1-CON-THEOR-YIELD — Theoretical yield (CONCEPT)
-   spec 4CH1-1.30 [CORE]: calculate percentage yield
- derivation: DEFINITIONAL_DEPENDENCY — The denominator object of the 1.30 formula; the comparison is meaningless without the theoretical-yield concept.
- `NOTE` Calculate percentage yield - IGCSE Chemistry Revision Notes.md — "The percentage yield compares the actual yield to the theoretical yield"

```diff
@@ -1276,7 +1279,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.30 @ Calculate percentage yield (2026-09-11)
     generated_date: '2026-09-11'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-11'
 - source: 4CH1-CON-PERCENT-YIELD
```

### 19. `4CH1-CON-PERCENT-YIELD REQUIRES_PREREQUISITE 4CH1-CON-YIELD` [high]

- node 4CH1-CON-PERCENT-YIELD — Percentage yield (CONCEPT)
-   spec 4CH1-1.30 [CORE]: calculate percentage yield
- node 4CH1-CON-YIELD — Yield (actual yield) (CONCEPT)
-   spec 4CH1-1.30 [CORE]: calculate percentage yield
- derivation: DEFINITIONAL_DEPENDENCY — The numerator object of the 1.30 formula. Same anchor quote as the THEOR-YIELD edge — both components of the one taught comparison; review may merge these two edges with the numerator/denominator pair if the split is judged too fine.
- `NOTE` Calculate percentage yield - IGCSE Chemistry Revision Notes.md — "The percentage yield compares the actual yield to the theoretical yield"

```diff
@@ -1298,7 +1301,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.30 @ Calculate percentage yield (2026-09-11)
     generated_date: '2026-09-11'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-11'
 - source: 4CH1-CON-REACTING-MASS
```

### 20. `4CH1-CON-REACTING-MASS REQUIRES_PREREQUISITE 4CH1-CON-MOLAR-RATIO` [high]

- node 4CH1-CON-REACTING-MASS — Reacting mass calculation (CONCEPT)
-   spec 4CH1-1.29 [CORE]: calculate reacting masses using experimental data and chemical equations
- node 4CH1-CON-MOLAR-RATIO — Molar ratio from balanced equations (CONCEPT)
-   spec 4CH1-1.29 [CORE]: calculate reacting masses using experimental data and chemical equations
- derivation: USED_WITHOUT_RETEACHING — Step 2 of the three-step procedure uses the molar ratio as a given; the ratio concept is exercised, not taught, here.
- `NOTE` Reacting mass calculations - IGCSE Chemistry Revision Notes.md — "Step 2 - use the molar ratio from the balanced symbol equation"

```diff
@@ -1340,7 +1343,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.29 @ Reacting mass calculations (2026-09-11)
     generated_date: '2026-09-11'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-11'
 - source: 4CH1-CON-REACTING-MASS
```

### 21. `4CH1-CON-REACTING-MASS REQUIRES_PREREQUISITE 4CH1-CON-MOLE-MASS-CONV` [high]

- node 4CH1-CON-REACTING-MASS — Reacting mass calculation (CONCEPT)
-   spec 4CH1-1.29 [CORE]: calculate reacting masses using experimental data and chemical equations
- node 4CH1-CON-MOLE-MASS-CONV — Mole-mass conversion (CONCEPT)
-   spec 4CH1-1.28 [CORE]: understand how to carry out calculations involving amount of substance, relative atomic mass ...
- derivation: USED_WITHOUT_RETEACHING — Every worked example opens with moles = mass/Mr as a given step; the mole-mass conversion is never re-taught in this note (it is the 1.28 note's job).
- `NOTE` Reacting mass calculations - IGCSE Chemistry Revision Notes.md — "Step 1 - calculate the moles of magnesium"

```diff
@@ -1361,7 +1364,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.29 @ Reacting mass calculations (2026-09-11)
     generated_date: '2026-09-11'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-11'
 - source: 4CH1-CON-THEOR-YIELD
```

### 22. `4CH1-CON-THEOR-YIELD REQUIRES_PREREQUISITE 4CH1-CON-REACTING-MASS` [high]

- node 4CH1-CON-THEOR-YIELD — Theoretical yield (CONCEPT)
-   spec 4CH1-1.30 [CORE]: calculate percentage yield
- node 4CH1-CON-REACTING-MASS — Reacting mass calculation (CONCEPT)
-   spec 4CH1-1.29 [CORE]: calculate reacting masses using experimental data and chemical equations
- derivation: USED_WITHOUT_RETEACHING — The note states the theoretical yield's derivation basis (balanced equation + reacting masses) as a given — cross-SP dependency 1.30 -> 1.29; the reacting-mass procedure is not re-taught here.
- `NOTE` Calculate percentage yield - IGCSE Chemistry Revision Notes.md — "It is calculated from the balanced equation and the reacting masses"

```diff
@@ -1383,7 +1386,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.30 @ Calculate percentage yield (2026-09-11)
     generated_date: '2026-09-11'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-11'
 - source: 4CH1-CON-WATER-CRYST
```

### 23. `4CH1-CON-WATER-CRYST REQUIRES_PREREQUISITE 4CH1-CON-EMP-MOL-CALC` [high]

- node 4CH1-CON-WATER-CRYST — Water of crystallisation and hydrated salts (CONCEPT)
-   spec 4CH1-1.31 [CORE]: understand how the formulae of simple compounds can be obtained experimentally, including met...
- node 4CH1-CON-EMP-MOL-CALC — Empirical and molecular formula calculation (CONCEPT)
-   spec 4CH1-1.33 [CORE]: calculate empirical and molecular formulae from experimental data
- derivation: EXPLICIT_TEACH_SEQUENCE — The note explicitly teaches the hydrated-salt determination as an ADAPTATION of the empirical-formula steps (same note, later section); the examiner tip reinforces: "it is an application of deducing empirical formulae".
- `NOTE` Empirical & Molecular Formulae  Edexcel IGCSE Chemistry Revision Notes 2017.md — "The steps for empirical formula can be adapted for hydrated salt / water of crystallisation calculations"

```diff
@@ -1406,7 +1409,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.31 @ Empirical & Molecular Formulae (2026-09-11)
     generated_date: '2026-09-11'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-11'
 - source: 4CH1-PR-03
```

### 24. `4CH1-CON-YIELD EXPLAINED_BY 4CH1-CON-YIELD-FACTORS` [high]

- node 4CH1-CON-YIELD — Yield (actual yield) (CONCEPT)
-   spec 4CH1-1.30 [CORE]: calculate percentage yield
- node 4CH1-CON-YIELD-FACTORS — Factors reducing yield (CONCEPT)
-   spec 4CH1-1.30 [ENRICHMENT]: calculate percentage yield
- derivation: SINGLE_SOURCE_CAUSAL_TEACHING — Single anchor teaches the explanation of the actual-yield shortfall (five enumerated causes: equipment residue, reversibility, separation/purification losses, side reactions, transfer losses) in the same section that defines the yields.
- `NOTE` Calculate percentage yield - IGCSE Chemistry Revision Notes.md — "In practice, you never get 100% yield in a chemical process for several reasons"

```diff
@@ -1498,7 +1501,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.30 @ Calculate percentage yield (2026-09-11)
     generated_date: '2026-09-11'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-11'
 - source: 4CH1-MIS-EQ-SUBSCRIPT
```

### 25. `4CH1-MIS-CONC-UNIT REMEDIATED_BY 4CH1-CON-VOL-CONVERSION` [high]

- node 4CH1-MIS-CONC-UNIT — Failing to convert cm3 to dm3 in concentration calculations (MISCONCEPTION)
- node 4CH1-CON-VOL-CONVERSION — Volume unit conversion (cm3/dm3) (CONCEPT)
-   spec 4CH1-1.34C [CORE]: understand how to carry out calculations involving amount of substance, volume and concentrat...
- derivation: EXAMINER_TIP_EXPLICIT — The Examiner-Tips block of the 1.34C-mapped note is precisely the corrective content for the documented wrong answer ("To go from cm3 to dm3 : divide by 1000").
- `NOTE` Solution concentration - IGCSE Chemistry Revision Notes.md — "Don't forget your unit conversions"

```diff
@@ -1564,7 +1567,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.34C @ Solution concentration (2026-09-11)
     generated_date: '2026-09-11'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-11'
 - source: 4CH1-MIS-EQ-SUBSCRIPT
```

### 26. `4CH1-MIS-CONC-UNIT WRONG_ANSWER_PATTERN 4CH1-CON-CONC-CALC` [high]

- node 4CH1-MIS-CONC-UNIT — Failing to convert cm3 to dm3 in concentration calculations (MISCONCEPTION)
- node 4CH1-CON-CONC-CALC — Concentration calculation (mol/dm3) (CONCEPT)
-   spec 4CH1-1.34C [CORE]: understand how to carry out calculations involving amount of substance, volume and concentrat...
- derivation: ASSESSMENT_DOCUMENTED — The pattern manifests in concentration-calculation question contexts (MS Q4: 0.096/24 with (25 x 0.4)/1000 — an amount-from-concentration question); kept distinct from MISCONCEPTION_OF (no belief is documented — only the wrong answer and its cause).
- `MARK_SCHEME` CFEC2_MS_P1.txt — "an answer of 10(.0) for 1 mark (i.e. failing to divide by 1000)"

```diff
@@ -1543,7 +1546,9 @@ edges:
       scripts/c11_evidence/CFEC2_MS_P1.txt sha1 6c63a9e02b71)
     generated_date: '2026-09-11'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-11'
 - source: 4CH1-MIS-CONC-UNIT
```

### 27. `4CH1-MIS-EQ-SUBSCRIPT MISCONCEPTION_OF 4CH1-CON-EQ-SYMBOL` [high]

- node 4CH1-MIS-EQ-SUBSCRIPT — Balancing equations by altering subscripts (MISCONCEPTION)
- node 4CH1-CON-EQ-SYMBOL — Balanced symbol (chemical) equation (CONCEPT)
-   spec 4CH1-1.25 [CORE]: write word equations and balanced chemical equations(including state symbols):for reactions s...
- derivation: EXAMINER_TIP_EXPLICIT — The misconception is ABOUT balancing symbol equations (the target concept); the tip names the mistake explicitly — evidence class per the frozen §8A.11 hierarchy ("explicit SME/examiner statements").
- `NOTE` Writing chemical equations - IGCSE Chemistry Revision Notes.md — "A common mistake when balancing symbol equations is to add, change or remove small numbers in the chemical ..."

```diff
@@ -1521,7 +1524,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.25 @ Writing chemical equations (2026-09-11)
     generated_date: '2026-09-11'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-11'
 - source: 4CH1-MIS-CONC-UNIT
```

### 28. `4CH1-PR-03 REQUIRES_PREREQUISITE 4CH1-CON-EXP-FORMULA-DEDUCTION` [high]

- node 4CH1-CON-EXP-FORMULA-DEDUCTION — Experimental formula deduction (mass-difference method) (CONCEPT)
-   spec 4CH1-1.31 [CORE]: understand how the formulae of simple compounds can be obtained experimentally, including met...
-   spec 4CH1-1.36 [CORE]: practical:know how to determine the formula of a metal oxide by combustion(e.g.magnesium oxid...
- derivation: USED_WITHOUT_RETEACHING — Practical->conceptual: both 1.36 practicals (MgO by combustion, CuO by reduction) perform exactly the mass-difference deduction method as their analysis step (Steps 1-3 of the Results sections), without re-teaching its principle.
- `NOTE` Investigating metal oxide formulas - IGCSE Revision Notes.md — "Divide each of the two masses by the relative atomic masses of the element"

```diff
@@ -1429,7 +1432,9 @@ edges:
       node 4CH1-PR-03 (T-C09 RULE_DERIVED)
     generated_date: '2026-09-11'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-11'
 - source: 4CH1-CON-EQ-SYMBOL
```

## File-level meta hunks (once, for the whole batch)

```diff
@@ -47,6 +47,9 @@ meta:
     requires_prerequisite_edges: 25
     wrong_answer_pattern_edges: 1
     review_required_edges: 1
+    promoted_edges: 28
+    human_validated_edges: 28
+  promotion_record: scripts/c11_promotions.yaml
 edges:
 - source: 4CH1-CON-AR
   relation: PART_OF
```

## Not actionable (decided or ineligible)

- `4CH1-CON-GAS-VOL-CALC REQUIRES_PREREQUISITE 4CH1-CON-AVOGADRO-LAW` [DECIDED] decided: operator HOLD (2026-09-11) — stays REVIEW_REQUIRED, not promotable (§18)
- `4CH1-CON-MOLAR-GAS-VOL EXPLAINED_BY 4CH1-CON-AVOGADRO-LAW` [DECIDED] operator HOLD (2026-09-12)
- `4CH1-CON-REACTING-MASS REQUIRES_PREREQUISITE 4CH1-CON-EQ-SYMBOL` [DECIDED] operator HOLD (2026-09-12)
- `4CH1-MIS-EQ-SUBSCRIPT REMEDIATED_BY 4CH1-CON-CONSERVATION-MASS` [DECIDED] operator HOLD (2026-09-12)

## Nodes awaiting verdicts — no §18 pathway yet (informational)

| node | title | family | spec points (role) | confidence |
|------|-------|--------|--------------------|------------|
| `4CH1-CON-AR` | Relative atomic mass (Ar) | CONCEPT | 4CH1-1.26 (CORE); 4CH1-1.28 (CORE) | high |
| `4CH1-CON-AVOGADRO-CONST` | Avogadro constant | CONCEPT | 4CH1-1.27 (ENRICHMENT) | high |
| `4CH1-CON-AVOGADRO-LAW` | Avogadro's Law | CONCEPT | 4CH1-1.35C (ENRICHMENT) | high |
| `4CH1-CON-CONC-CALC` | Concentration calculation (mol/dm3) | CONCEPT | 4CH1-1.34C (CORE) | high |
| `4CH1-CON-CONCENTRATION` | Concentration of a solution | CONCEPT | 4CH1-1.34C (CORE) | high |
| `4CH1-CON-CONSERVATION-MASS` | Law of Conservation of Mass | CONCEPT | 4CH1-1.25 (CORE); 4CH1-1.26 (SUPPORTING) | high |
| `4CH1-CON-EMP-MOL-CALC` | Empirical and molecular formula calculation | CONCEPT | 4CH1-1.33 (CORE) | high |
| `4CH1-CON-EMPIRICAL-FORMULA` | Empirical formula | CONCEPT | 4CH1-1.32 (CORE); 4CH1-1.33 (CORE) | high |
| `4CH1-CON-EQ-STATE-SYM` | State symbols (s), (l), (g), (aq) | CONCEPT | 4CH1-1.25 (CORE) | high |
| `4CH1-CON-EQ-SYMBOL` | Balanced symbol (chemical) equation | CONCEPT | 4CH1-1.25 (CORE) | high |
| `4CH1-CON-EQ-WORD` | Word equation | CONCEPT | 4CH1-1.25 (CORE) | high |
| `4CH1-CON-EXP-FORMULA-DEDUCTION` | Experimental formula deduction (mass-difference method) | CONCEPT | 4CH1-1.31 (CORE); 4CH1-1.36 (CORE) | high |
| `4CH1-CON-GAS-VOL-CALC` | Gas volume calculation | CONCEPT | 4CH1-1.35C (CORE) | high |
| `4CH1-CON-MOLAR-GAS-VOL` | Molar gas volume at RTP (24 dm3) | CONCEPT | 4CH1-1.35C (CORE) | high |
| `4CH1-CON-MOLAR-MASS` | Molar mass | CONCEPT | 4CH1-1.28 (CORE) | high |
| `4CH1-CON-MOLAR-RATIO` | Molar ratio from balanced equations | CONCEPT | 4CH1-1.29 (CORE) | high |
| `4CH1-CON-MOLE` | The mole (unit of amount of substance) | CONCEPT | 4CH1-1.27 (CORE) | high |
| `4CH1-CON-MOLE-MASS-CONV` | Mole-mass conversion | CONCEPT | 4CH1-1.28 (CORE) | high |
| `4CH1-CON-MOLECULAR-FORMULA` | Molecular formula | CONCEPT | 4CH1-1.32 (CORE); 4CH1-1.33 (CORE) | high |
| `4CH1-CON-MR` | Relative formula mass (Mr) | CONCEPT | 4CH1-1.26 (CORE); 4CH1-1.28 (CORE) | high |
| `4CH1-CON-PERCENT-YIELD` | Percentage yield | CONCEPT | 4CH1-1.30 (CORE) | high |
| `4CH1-CON-REACTING-MASS` | Reacting mass calculation | CONCEPT | 4CH1-1.29 (CORE) | high |
| `4CH1-CON-THEOR-YIELD` | Theoretical yield | CONCEPT | 4CH1-1.30 (CORE) | high |
| `4CH1-CON-VOL-CONVERSION` | Volume unit conversion (cm3/dm3) | CONCEPT | 4CH1-1.34C (CORE) | high |
| `4CH1-CON-WATER-CRYST` | Water of crystallisation and hydrated salts | CONCEPT | 4CH1-1.31 (CORE) | high |
| `4CH1-CON-YIELD` | Yield (actual yield) | CONCEPT | 4CH1-1.30 (CORE) | high |
| `4CH1-CON-YIELD-FACTORS` | Factors reducing yield | CONCEPT | 4CH1-1.30 (ENRICHMENT) | high |
| `4CH1-MIS-CONC-UNIT` | Failing to convert cm3 to dm3 in concentration calculations | MISCONCEPTION |  | high |
| `4CH1-MIS-EQ-SUBSCRIPT` | Balancing equations by altering subscripts | MISCONCEPTION |  | high |

