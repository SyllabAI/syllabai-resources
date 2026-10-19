# C11 Diff Review Bundle — pending §18 edge promotions (generated 2026-09-12)

- baseline commit: `b884cfb`
- state fingerprint: `da629f00ba18` (promo_count=56)
- actionable: 23 edges (clean 23 / pending-flagged 0); not-actionable: 5; nodes awaiting a pathway: 67
- preview fidelity: simulator re-emits graph/concept_edges.yaml under the generator's own serialization contract with a byte-identity guard — what you read is what G13 will write.

## Batch approval

```bash
cd work/syllabai-resources && python3 scripts/c11_diff_review.py approve \
  '4CH1-CON-AR REQUIRES_PREREQUISITE 4CH1-CON-ISOTOPES' \
  '4CH1-CON-ATOMIC-NUMBER COMMONLY_CONFUSED_WITH 4CH1-CON-MASS-NUMBER' \
  '4CH1-CON-ATOMIC-NUMBER REQUIRES_PREREQUISITE 4CH1-CON-SUBATOMIC-PARTICLES' \
  '4CH1-CON-ELECTRONIC-CONFIGURATION REQUIRES_PREREQUISITE 4CH1-CON-PERIODIC-TABLE' \
  '4CH1-CON-ELECTRONIC-CONFIGURATION REQUIRES_PREREQUISITE 4CH1-CON-SUBATOMIC-PARTICLES' \
  '4CH1-CON-GROUP-SIMILARITY EXPLAINED_BY 4CH1-CON-ELECTRONIC-CONFIGURATION' \
  '4CH1-CON-GROUP-SIMILARITY REQUIRES_PREREQUISITE 4CH1-CON-PERIODIC-TABLE' \
  '4CH1-CON-ISOTOPES REQUIRES_PREREQUISITE 4CH1-CON-SUBATOMIC-PARTICLES' \
  '4CH1-CON-MASS-NUMBER REQUIRES_PREREQUISITE 4CH1-CON-ATOMIC-NUMBER' \
  '4CH1-CON-MASS-NUMBER REQUIRES_PREREQUISITE 4CH1-CON-SUBATOMIC-PARTICLES' \
  '4CH1-CON-METAL-NONMETAL REQUIRES_PREREQUISITE 4CH1-CON-PERIODIC-TABLE' \
  '4CH1-CON-MOLECULE REQUIRES_PREREQUISITE 4CH1-CON-ATOM' \
  '4CH1-CON-NOBLE-GAS-INERTNESS EXPLAINED_BY 4CH1-CON-ELECTRONIC-CONFIGURATION' \
  '4CH1-CON-NOBLE-GAS-INERTNESS REQUIRES_PREREQUISITE 4CH1-CON-PERIODIC-TABLE' \
  '4CH1-CON-PERIODIC-TABLE REQUIRES_PREREQUISITE 4CH1-CON-ATOMIC-NUMBER' \
  '4CH1-CON-PERIODIC-TABLE REQUIRES_PREREQUISITE 4CH1-CON-ELEMENT' \
  '4CH1-CON-SUBATOMIC-PARTICLES REQUIRES_PREREQUISITE 4CH1-CON-ATOM' \
  '4CH1-MIS-ISOTOPES-DIFFER-PROTONS REMEDIATED_BY 4CH1-CON-ISOTOPES' \
  '4CH1-MIS-ISOTOPES-DIFFER-PROTONS WRONG_ANSWER_PATTERN 4CH1-CON-ISOTOPES' \
  '4CH1-MIS-RAM-MASS-NUMBER REMEDIATED_BY 4CH1-CON-AR' \
  '4CH1-MIS-RAM-MASS-NUMBER WRONG_ANSWER_PATTERN 4CH1-CON-AR' \
  '4CH1-PR-02 REQUIRES_PREREQUISITE 4CH1-CON-CHROMATOGRAPHY' \
  '4CH1-PR-02 REQUIRES_PREREQUISITE 4CH1-CON-RF-VALUE' \
  --by <operator> --date 2026-09-12 --review-ref graph/reports/C11_DIFF_REVIEW_B2_2026-09-12.md
```

Pending-flagged (PENDING operator_decision) edges are excluded from the command above; approving them additionally requires `--include-pending` — that flag records the explicit decision this bundle presents.

## Index

| # | identity | confidence | flag |
|---|----------|------------|------|
| 1 | `4CH1-CON-AR REQUIRES_PREREQUISITE 4CH1-CON-ISOTOPES` | high |  |
| 2 | `4CH1-CON-ATOMIC-NUMBER COMMONLY_CONFUSED_WITH 4CH1-CON-MASS-NUMBER` | high |  |
| 3 | `4CH1-CON-ATOMIC-NUMBER REQUIRES_PREREQUISITE 4CH1-CON-SUBATOMIC-PARTICLES` | high |  |
| 4 | `4CH1-CON-ELECTRONIC-CONFIGURATION REQUIRES_PREREQUISITE 4CH1-CON-PERIODIC-TABLE` | high |  |
| 5 | `4CH1-CON-ELECTRONIC-CONFIGURATION REQUIRES_PREREQUISITE 4CH1-CON-SUBATOMIC-PARTICLES` | high |  |
| 6 | `4CH1-CON-GROUP-SIMILARITY EXPLAINED_BY 4CH1-CON-ELECTRONIC-CONFIGURATION` | high |  |
| 7 | `4CH1-CON-GROUP-SIMILARITY REQUIRES_PREREQUISITE 4CH1-CON-PERIODIC-TABLE` | high |  |
| 8 | `4CH1-CON-ISOTOPES REQUIRES_PREREQUISITE 4CH1-CON-SUBATOMIC-PARTICLES` | high |  |
| 9 | `4CH1-CON-MASS-NUMBER REQUIRES_PREREQUISITE 4CH1-CON-ATOMIC-NUMBER` | high |  |
| 10 | `4CH1-CON-MASS-NUMBER REQUIRES_PREREQUISITE 4CH1-CON-SUBATOMIC-PARTICLES` | high |  |
| 11 | `4CH1-CON-METAL-NONMETAL REQUIRES_PREREQUISITE 4CH1-CON-PERIODIC-TABLE` | high |  |
| 12 | `4CH1-CON-MOLECULE REQUIRES_PREREQUISITE 4CH1-CON-ATOM` | high |  |
| 13 | `4CH1-CON-NOBLE-GAS-INERTNESS EXPLAINED_BY 4CH1-CON-ELECTRONIC-CONFIGURATION` | high |  |
| 14 | `4CH1-CON-NOBLE-GAS-INERTNESS REQUIRES_PREREQUISITE 4CH1-CON-PERIODIC-TABLE` | high |  |
| 15 | `4CH1-CON-PERIODIC-TABLE REQUIRES_PREREQUISITE 4CH1-CON-ATOMIC-NUMBER` | high |  |
| 16 | `4CH1-CON-PERIODIC-TABLE REQUIRES_PREREQUISITE 4CH1-CON-ELEMENT` | high |  |
| 17 | `4CH1-CON-SUBATOMIC-PARTICLES REQUIRES_PREREQUISITE 4CH1-CON-ATOM` | high |  |
| 18 | `4CH1-MIS-ISOTOPES-DIFFER-PROTONS REMEDIATED_BY 4CH1-CON-ISOTOPES` | high |  |
| 19 | `4CH1-MIS-ISOTOPES-DIFFER-PROTONS WRONG_ANSWER_PATTERN 4CH1-CON-ISOTOPES` | high |  |
| 20 | `4CH1-MIS-RAM-MASS-NUMBER REMEDIATED_BY 4CH1-CON-AR` | high |  |
| 21 | `4CH1-MIS-RAM-MASS-NUMBER WRONG_ANSWER_PATTERN 4CH1-CON-AR` | high |  |
| 22 | `4CH1-PR-02 REQUIRES_PREREQUISITE 4CH1-CON-CHROMATOGRAPHY` | high |  |
| 23 | `4CH1-PR-02 REQUIRES_PREREQUISITE 4CH1-CON-RF-VALUE` | high |  |

## Pending items — the exact diff each approval applies

### 1. `4CH1-CON-AR REQUIRES_PREREQUISITE 4CH1-CON-ISOTOPES` [high]

- node 4CH1-CON-AR — Relative atomic mass (Ar) (CONCEPT)
-   spec 4CH1-1.26 [CORE]: calculate relative formula masses(including relative molecular masses) $ (M_{r}) $ from relat...
-   spec 4CH1-1.28 [CORE]: understand how to carry out calculations involving amount of substance, relative atomic mass ...
- node 4CH1-CON-ISOTOPES — Isotopes and relative atomic mass from isotopic abundances (CONCEPT)
-   spec 4CH1-1.16 [CORE]: know what is meant by the terms atomic number, mass number, isotopes and relative atomic mass...
-   spec 4CH1-1.17 [CORE]: be able to calculate the relative atomic mass of an element $ A_{r} $ from isotopic abundances
- derivation: USED_WITHOUT_RETEACHING — Cross-boundary edge (source = the pilot CON-AR node, sanctioned per FN-B1-2 — no duplicate Ar mint in this batch): the Mr-calculation context uses relative atomic masses whose ground is the isotope/abundance structure taught in the 1.16/1.17 notes; the Calculate-Relative-Mass context presupposes that ground without re-teaching it.
- `NOTE` Relative atomic mass - IGCSE Chemistry Revision Notes.md — "The relative atomic mass of each element is calculated from the mass number and relative abundances of all ..."

```diff
@@ -2157,7 +2157,9 @@ edges:
       the pilot record (4CH1-1.26/1.28)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-ATOMIC-NUMBER
```

### 2. `4CH1-CON-ATOMIC-NUMBER COMMONLY_CONFUSED_WITH 4CH1-CON-MASS-NUMBER` [high]

- node 4CH1-CON-ATOMIC-NUMBER — Atomic number (CONCEPT)
-   spec 4CH1-1.16 [CORE]: know what is meant by the terms atomic number, mass number, isotopes and relative atomic mass...
- node 4CH1-CON-MASS-NUMBER — Mass number (CONCEPT)
-   spec 4CH1-1.16 [CORE]: know what is meant by the terms atomic number, mass number, isotopes and relative atomic mass...
- derivation: EXAMINER_TIP_EXPLICIT — First COMMONLY_CONFUSED_WITH edge in the store: the corpus itself documents the term-pair confusability (the examiner tip states it outright and gives the MASS = MASSIVE mnemonic), and the pinned PT/ATOM MS document the confusion being assessed (the same family as MIS-RAM-MASS-NUMBER on the Ar side). Symmetric term-pair relation, distinct from wrong-answer patterns per the frozen §8A.11 triple distinction.
- `NOTE` Atoms Definitions & Structure  Edexcel IGCSE Chemistry Revision Notes 2017.md — "Both the atomic number and the mass number are given on the Periodic Table, but it can be easy to confuse them"

```diff
@@ -3853,7 +3853,9 @@ edges:
       context PT_MS_P1 Q1 (pinned fd6352a38077)'
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-MIS-EQ-SUBSCRIPT
```

### 3. `4CH1-CON-ATOMIC-NUMBER REQUIRES_PREREQUISITE 4CH1-CON-SUBATOMIC-PARTICLES` [high]

- node 4CH1-CON-ATOMIC-NUMBER — Atomic number (CONCEPT)
-   spec 4CH1-1.16 [CORE]: know what is meant by the terms atomic number, mass number, isotopes and relative atomic mass...
- node 4CH1-CON-SUBATOMIC-PARTICLES — Subatomic particles (proton, neutron, electron — positions, relative masses, relative charges) (CONCEPT)
-   spec 4CH1-1.15 [CORE]: know the structure of an atom in terms of the positions, relative masses and relative charges...
- derivation: DEFINITIONAL_DEPENDENCY — The atomic number is defined as the number of PROTONS — the proton is a subatomic particle, so the 1.16 term is stated in terms of the 1.15 particle set (definitional operand; the batch-1 DEFINITIONAL_DEPENDENCY pattern).
- `NOTE` Atoms Definitions & Structure  Edexcel IGCSE Chemistry Revision Notes 2017.md — "The number of protons in the nucleus of an atom"

```diff
@@ -2179,7 +2179,9 @@ edges:
     upstream: 'T-C10 HUMAN_VALIDATED 4CH1-1.16 @ Atoms: Definitions & Structure (2026-09-11)'
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-CHROMATOGRAM-INTERPRETATION
```

### 4. `4CH1-CON-ELECTRONIC-CONFIGURATION REQUIRES_PREREQUISITE 4CH1-CON-PERIODIC-TABLE` [high]

- node 4CH1-CON-ELECTRONIC-CONFIGURATION — Electronic configuration of the first 20 elements (shells 2, 8, 8; configuration and Periodic Table position) (CONCEPT)
-   spec 4CH1-1.19 [CORE]: understand how to deduce the electronic configurations of the first 20 elements from their po...
-   spec 4CH1-1.22 [CORE]: understand how the electronic configuration of a main group element is related to its positio...
- node 4CH1-CON-PERIODIC-TABLE — Periodic Table arrangement (atomic-number order, groups and periods) (CONCEPT)
-   spec 4CH1-1.18 [CORE]: understand how elements are arranged in the Periodic Table： •in order of atomic number •in gr...
- derivation: USED_WITHOUT_RETEACHING — The 1.19/1.22 skill (deduce configurations FROM Periodic Table positions) uses the period/group structure without re-teaching it — the notations-to-period and last-notation-to-group rules presuppose the 1.18 arrangement concept (the chlorine worked example reads position off the table).
- `NOTE` Electronic Configurations  Edexcel IGCSE Chemistry Revision Notes 2017.md — "The number of notations in the electronic configuration tells us the number of occupied shells"

```diff
@@ -2400,7 +2400,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.19/1.22 @ Electronic Configurations (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-ELECTRONIC-CONFIGURATION
```

### 5. `4CH1-CON-ELECTRONIC-CONFIGURATION REQUIRES_PREREQUISITE 4CH1-CON-SUBATOMIC-PARTICLES` [high]

- node 4CH1-CON-ELECTRONIC-CONFIGURATION — Electronic configuration of the first 20 elements (shells 2, 8, 8; configuration and Periodic Table position) (CONCEPT)
-   spec 4CH1-1.19 [CORE]: understand how to deduce the electronic configurations of the first 20 elements from their po...
-   spec 4CH1-1.22 [CORE]: understand how the electronic configuration of a main group element is related to its positio...
- node 4CH1-CON-SUBATOMIC-PARTICLES — Subatomic particles (proton, neutron, electron — positions, relative masses, relative charges) (CONCEPT)
-   spec 4CH1-1.15 [CORE]: know the structure of an atom in terms of the positions, relative masses and relative charges...
- derivation: DEFINITIONAL_DEPENDENCY — The electronic configuration is the arrangement OF ELECTRONS in shells — the electron (a subatomic particle, whose shells-around-the-nucleus position is the 1.15 ground taught in the Atoms note) is the definitional operand of the configuration concept.
- `NOTE` Electronic Configurations  Edexcel IGCSE Chemistry Revision Notes 2017.md — "Electrons orbit the nucleus in shells (or energy levels) and each shell has a different amount of energy as..."

```diff
@@ -2424,7 +2424,9 @@ edges:
       & Structure (2026-09-11)'
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-EMP-MOL-CALC
```

### 6. `4CH1-CON-GROUP-SIMILARITY EXPLAINED_BY 4CH1-CON-ELECTRONIC-CONFIGURATION` [high]

- node 4CH1-CON-GROUP-SIMILARITY — Why elements in the same group have similar chemical properties (CONCEPT)
-   spec 4CH1-1.23 [CORE]: understand why elements in the same group of the Periodic Table have similar chemical properties
- node 4CH1-CON-ELECTRONIC-CONFIGURATION — Electronic configuration of the first 20 elements (shells 2, 8, 8; configuration and Periodic Table position) (CONCEPT)
-   spec 4CH1-1.19 [CORE]: understand how to deduce the electronic configurations of the first 20 elements from their po...
-   spec 4CH1-1.22 [CORE]: understand how the electronic configuration of a main group element is related to its positio...
- derivation: SINGLE_SOURCE_CAUSAL_TEACHING — The 1.23 "understand WHY" demand with an explicit causal sentence ("This is because they have the same number of outer electrons so will react and bond similarly") — the outer-electron count is the taught mechanism. The prerequisite reading of the same pair is HELD (B2-H-05, one relation per pair, the batch-1 B1-H-04/DIFFUSION discipline).
- `NOTE` Electronic Configuration & Reactivity  Edexcel IGCSE Chemistry Revision Notes 2017.md — "This is because they have the same number of outer electrons so will react and bond similarly"

```diff
@@ -3752,7 +3752,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.23 @ Electronic Configuration & Reactivity (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-MOLAR-GAS-VOL
```

### 7. `4CH1-CON-GROUP-SIMILARITY REQUIRES_PREREQUISITE 4CH1-CON-PERIODIC-TABLE` [high]

- node 4CH1-CON-GROUP-SIMILARITY — Why elements in the same group have similar chemical properties (CONCEPT)
-   spec 4CH1-1.23 [CORE]: understand why elements in the same group of the Periodic Table have similar chemical properties
- node 4CH1-CON-PERIODIC-TABLE — Periodic Table arrangement (atomic-number order, groups and periods) (CONCEPT)
-   spec 4CH1-1.18 [CORE]: understand how elements are arranged in the Periodic Table： •in order of atomic number •in gr...
- derivation: USED_WITHOUT_RETEACHING — The same-group statement uses the group concept (the 1.18 arrangement) without re-teaching it — this is the group-similarity concept's only direct Periodic Table link (the electronic-configuration pair carries the explanatory relation instead; not transitively subsumed because the emitted CONFIG -> PT chain runs the other direction from this node's EB edge).
- `NOTE` Electronic Configuration & Reactivity  Edexcel IGCSE Chemistry Revision Notes 2017.md — "Elements in the same group in the Periodic Table will have similar chemical properties"

```diff
@@ -2686,7 +2686,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.23 @ Electronic Configuration & Reactivity (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-ISOTOPES
```

### 8. `4CH1-CON-ISOTOPES REQUIRES_PREREQUISITE 4CH1-CON-SUBATOMIC-PARTICLES` [high]

- node 4CH1-CON-ISOTOPES — Isotopes and relative atomic mass from isotopic abundances (CONCEPT)
-   spec 4CH1-1.16 [CORE]: know what is meant by the terms atomic number, mass number, isotopes and relative atomic mass...
-   spec 4CH1-1.17 [CORE]: be able to calculate the relative atomic mass of an element $ A_{r} $ from isotopic abundances
- node 4CH1-CON-SUBATOMIC-PARTICLES — Subatomic particles (proton, neutron, electron — positions, relative masses, relative charges) (CONCEPT)
-   spec 4CH1-1.15 [CORE]: know the structure of an atom in terms of the positions, relative masses and relative charges...
- derivation: DEFINITIONAL_DEPENDENCY — The isotope definition is stated IN TERMS OF protons and neutrons — the nucleon pair is the definitional operand set (same class as ATOMIC-NUMBER -> SUBATOMIC).
- `NOTE` Atoms Definitions & Structure  Edexcel IGCSE Chemistry Revision Notes 2017.md — "Atoms of the same element which have the same number of protons but a different number of neutrons"

```diff
@@ -2707,7 +2707,9 @@ edges:
     upstream: 'T-C10 HUMAN_VALIDATED 4CH1-1.16 @ Atoms: Definitions & Structure (2026-09-11)'
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-MASS-NUMBER
```

### 9. `4CH1-CON-MASS-NUMBER REQUIRES_PREREQUISITE 4CH1-CON-ATOMIC-NUMBER` [high]

- node 4CH1-CON-MASS-NUMBER — Mass number (CONCEPT)
-   spec 4CH1-1.16 [CORE]: know what is meant by the terms atomic number, mass number, isotopes and relative atomic mass...
- node 4CH1-CON-ATOMIC-NUMBER — Atomic number (CONCEPT)
-   spec 4CH1-1.16 [CORE]: know what is meant by the terms atomic number, mass number, isotopes and relative atomic mass...
- derivation: USED_WITHOUT_RETEACHING — Using the mass number (neutron calculations, lithium/X worked examples) presupposes the atomic number without re-teaching it — the subtraction rule and every worked example use both terms together. Not subsumed by the SUBATOMIC chain (no emitted path MASS-NUMBER -> SUBATOMIC -> ATOMIC-NUMBER; the subatomic edge points the same direction).
- `NOTE` Atoms Definitions & Structure  Edexcel IGCSE Chemistry Revision Notes 2017.md — "The number of neutrons can thus be calculated by subtracting the atomic number from the mass number"

```diff
@@ -2731,7 +2731,9 @@ edges:
     upstream: 'T-C10 HUMAN_VALIDATED 4CH1-1.16 @ Atoms: Definitions & Structure (2026-09-11)'
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-MASS-NUMBER
```

### 10. `4CH1-CON-MASS-NUMBER REQUIRES_PREREQUISITE 4CH1-CON-SUBATOMIC-PARTICLES` [high]

- node 4CH1-CON-MASS-NUMBER — Mass number (CONCEPT)
-   spec 4CH1-1.16 [CORE]: know what is meant by the terms atomic number, mass number, isotopes and relative atomic mass...
- node 4CH1-CON-SUBATOMIC-PARTICLES — Subatomic particles (proton, neutron, electron — positions, relative masses, relative charges) (CONCEPT)
-   spec 4CH1-1.15 [CORE]: know the structure of an atom in terms of the positions, relative masses and relative charges...
- derivation: DEFINITIONAL_DEPENDENCY — The mass number is defined as protons + neutrons — the two nucleons are the definitional operand set (the 1.16 term presupposes the 1.15 particle set).
- `NOTE` Atoms Definitions & Structure  Edexcel IGCSE Chemistry Revision Notes 2017.md — "The number of protons and neutrons in the nucleus of an atom"

```diff
@@ -2752,7 +2752,9 @@ edges:
     upstream: 'T-C10 HUMAN_VALIDATED 4CH1-1.16 @ Atoms: Definitions & Structure (2026-09-11)'
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-METAL-NONMETAL
```

### 11. `4CH1-CON-METAL-NONMETAL REQUIRES_PREREQUISITE 4CH1-CON-PERIODIC-TABLE` [high]

- node 4CH1-CON-METAL-NONMETAL — Classifying elements as metals or non-metals (by properties and by Periodic Table position) (CONCEPT)
-   spec 4CH1-1.20 [CORE]: understand how to use electrical conductivity and the acid-base character of oxides to classi...
-   spec 4CH1-1.21 [CORE]: identify an element as a metal or a non-metal according to its position in the Periodic Table
- node 4CH1-CON-PERIODIC-TABLE — Periodic Table arrangement (atomic-number order, groups and periods) (CONCEPT)
-   spec 4CH1-1.18 [CORE]: understand how elements are arranged in the Periodic Table： •in order of atomic number •in gr...
- derivation: USED_WITHOUT_RETEACHING — The 1.21 position-based identification reads the metals/non-metals regions off the Periodic Table without re-teaching the arrangement — the left/right and zig-zag-line rules presuppose the 1.18 concept.
- `NOTE` Metals & non-metals in the Periodic Table - IGCSE Chemistry.md — "Metals are on the left of the Periodic Table and non-metals on the right"

```diff
@@ -2774,7 +2774,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.20/1.21 @ Metals & non-metals in the Periodic Table (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-MIXTURE
```

### 12. `4CH1-CON-MOLECULE REQUIRES_PREREQUISITE 4CH1-CON-ATOM` [high]

- node 4CH1-CON-MOLECULE — Molecule (CONCEPT)
-   spec 4CH1-1.14 [CORE]: know what is meant by the terms atom and molecule
- node 4CH1-CON-ATOM — Atom (definition and subatomic composition) (CONCEPT)
-   spec 4CH1-1.14 [CORE]: know what is meant by the terms atom and molecule
- derivation: DEFINITIONAL_DEPENDENCY — The molecule definition is stated IN TERMS OF atoms ("a group of two or more atoms chemically combined") — the atom is the definitional operand (the batch-1 SATURATED-SOLUTION -> SOLUTION pattern).
- `NOTE` Atoms Definitions & Structure  Edexcel IGCSE Chemistry Revision Notes 2017.md — "A group of two or more atoms chemically combined to form an identifiable unit which retains the properties ..."

```diff
@@ -2986,7 +2986,9 @@ edges:
     upstream: 'T-C10 HUMAN_VALIDATED 4CH1-1.14 @ Atoms: Definitions & Structure (2026-09-11)'
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-MR
```

### 13. `4CH1-CON-NOBLE-GAS-INERTNESS EXPLAINED_BY 4CH1-CON-ELECTRONIC-CONFIGURATION` [high]

- node 4CH1-CON-NOBLE-GAS-INERTNESS — Why the noble gases (Group 0) do not readily react (CONCEPT)
-   spec 4CH1-1.24 [CORE]: understand why the noble gases(Group0)do not readily react
- node 4CH1-CON-ELECTRONIC-CONFIGURATION — Electronic configuration of the first 20 elements (shells 2, 8, 8; configuration and Periodic Table position) (CONCEPT)
-   spec 4CH1-1.19 [CORE]: understand how to deduce the electronic configurations of the first 20 elements from their po...
-   spec 4CH1-1.22 [CORE]: understand how the electronic configuration of a main group element is related to its positio...
- derivation: SINGLE_SOURCE_CAUSAL_TEACHING — The 1.24 "understand why" demand with an explicit causal sentence ("...because they have full outer shells of electrons") — the full-outer-shell structure is the taught mechanism. The prerequisite reading of the same pair is HELD (B2-H-06, one relation per pair).
- `NOTE` Electronic Configuration & Reactivity  Edexcel IGCSE Chemistry Revision Notes 2017.md — "Group 0 elements do not do this because they have full outer shells of electrons"

```diff
@@ -3798,7 +3798,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.24 @ Electronic Configuration & Reactivity (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-YIELD
```

### 14. `4CH1-CON-NOBLE-GAS-INERTNESS REQUIRES_PREREQUISITE 4CH1-CON-PERIODIC-TABLE` [high]

- node 4CH1-CON-NOBLE-GAS-INERTNESS — Why the noble gases (Group 0) do not readily react (CONCEPT)
-   spec 4CH1-1.24 [CORE]: understand why the noble gases(Group0)do not readily react
- node 4CH1-CON-PERIODIC-TABLE — Periodic Table arrangement (atomic-number order, groups and periods) (CONCEPT)
-   spec 4CH1-1.18 [CORE]: understand how elements are arranged in the Periodic Table： •in order of atomic number •in gr...
- derivation: USED_WITHOUT_RETEACHING — The Group 0 statement uses the group/arrangement concept without re-teaching it — the noble-gas concept's only direct Periodic Table link (the electronic-configuration pair carries the explanatory relation; not subsumed — same non-chain shape as the GROUP-SIMILARITY -> PT edge).
- `NOTE` Electronic Configuration & Reactivity  Edexcel IGCSE Chemistry Revision Notes 2017.md — "The elements in Group 0 of the Periodic Table are called the noble gases"

```diff
@@ -3032,7 +3032,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.24 @ Electronic Configuration & Reactivity (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-PERCENT-YIELD
```

### 15. `4CH1-CON-PERIODIC-TABLE REQUIRES_PREREQUISITE 4CH1-CON-ATOMIC-NUMBER` [high]

- node 4CH1-CON-PERIODIC-TABLE — Periodic Table arrangement (atomic-number order, groups and periods) (CONCEPT)
-   spec 4CH1-1.18 [CORE]: understand how elements are arranged in the Periodic Table： •in order of atomic number •in gr...
- node 4CH1-CON-ATOMIC-NUMBER — Atomic number (CONCEPT)
-   spec 4CH1-1.16 [CORE]: know what is meant by the terms atomic number, mass number, isotopes and relative atomic mass...
- derivation: DEFINITIONAL_DEPENDENCY — The arrangement is defined BY the atomic number (increasing order; each element has one proton more than the preceding one) — the atomic-number concept is the definitional operand of the arrangement.
- `NOTE` Periodic Table Basics  Edexcel IGCSE Chemistry Revision Notes 2017.md — "Elements are arranged on the Periodic table in order of increasing atomic number"

```diff
@@ -3101,7 +3101,9 @@ edges:
     upstream: 'T-C10 HUMAN_VALIDATED 4CH1-1.18 @ Periodic Table: Basics (2026-09-11)'
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-PERIODIC-TABLE
```

### 16. `4CH1-CON-PERIODIC-TABLE REQUIRES_PREREQUISITE 4CH1-CON-ELEMENT` [high]

- node 4CH1-CON-PERIODIC-TABLE — Periodic Table arrangement (atomic-number order, groups and periods) (CONCEPT)
-   spec 4CH1-1.18 [CORE]: understand how elements are arranged in the Periodic Table： •in order of atomic number •in gr...
- node 4CH1-CON-ELEMENT — Element (CONCEPT)
-   spec 4CH1-1.8 [CORE]: understand how to classify a substance as an element,compound or mixture
- derivation: USED_WITHOUT_RETEACHING — Cross-boundary edge (target = the batch-1 CON-ELEMENT node, sanctioned per FN-B1-2): the Periodic Table is a table of elements and the 1.18 note uses the element term throughout without re-teaching it (the 1.8 definitions are that term's ground). This is the Periodic Table concept's only element link — not subsumed by any emitted chain (the batch-1 HELD-02/12 vocabulary-level discipline notes this class).
- `NOTE` Periodic Table Basics  Edexcel IGCSE Chemistry Revision Notes 2017.md — "There are over 100 chemical elements which have been isolated and identified"

```diff
@@ -3126,7 +3126,9 @@ edges:
       by the batch-1 record (4CH1-1.8)'
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-PURE-SUBSTANCE
```

### 17. `4CH1-CON-SUBATOMIC-PARTICLES REQUIRES_PREREQUISITE 4CH1-CON-ATOM` [high]

- node 4CH1-CON-SUBATOMIC-PARTICLES — Subatomic particles (proton, neutron, electron — positions, relative masses, relative charges) (CONCEPT)
-   spec 4CH1-1.15 [CORE]: know the structure of an atom in terms of the positions, relative masses and relative charges...
- node 4CH1-CON-ATOM — Atom (definition and subatomic composition) (CONCEPT)
-   spec 4CH1-1.14 [CORE]: know what is meant by the terms atom and molecule
- derivation: DEFINITIONAL_DEPENDENCY — The subatomic-particle description is stated IN TERMS OF the atom ("each atom is made of...") — knowing what the particles are positions presupposes the atom term (definitional operand).
- `NOTE` Atoms Definitions & Structure  Edexcel IGCSE Chemistry Revision Notes 2017.md — "Each atom is made of subatomic particles called protons, neutrons, and electrons"

```diff
@@ -3459,7 +3459,9 @@ edges:
     upstream: 'T-C10 HUMAN_VALIDATED 4CH1-1.15 @ Atoms: Definitions & Structure (2026-09-11)'
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-THEOR-YIELD
```

### 18. `4CH1-MIS-ISOTOPES-DIFFER-PROTONS REMEDIATED_BY 4CH1-CON-ISOTOPES` [high]

- node 4CH1-MIS-ISOTOPES-DIFFER-PROTONS — Believing isotopes of an element differ in their number of protons (MISCONCEPTION)
- node 4CH1-CON-ISOTOPES — Isotopes and relative atomic mass from isotopic abundances (CONCEPT)
-   spec 4CH1-1.16 [CORE]: know what is meant by the terms atomic number, mass number, isotopes and relative atomic mass...
-   spec 4CH1-1.17 [CORE]: be able to calculate the relative atomic mass of an element $ A_{r} $ from isotopic abundances
- derivation: EXPLICIT_TEACH_SEQUENCE — Remediation = the isotope definition itself (same protons, different neutrons) — the corrective concept IS the WAP target (the batch-1 B1-E-25 pattern: no deeper in-slice concept exists below the isotope definition; the node's remediation_evidence also carries the proton/atomic-number identity). Operator may drop the edge and keep the node-level evidence.
- `NOTE` Atoms Definitions & Structure  Edexcel IGCSE Chemistry Revision Notes 2017.md — "Atoms of the same element which have the same number of protons but a different number of neutrons"

```diff
@@ -4116,7 +4116,9 @@ edges:
     upstream: 'T-C10 HUMAN_VALIDATED 4CH1-1.16 @ Atoms: Definitions & Structure (2026-09-11)'
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-MIS-RAM-MASS-NUMBER
```

### 19. `4CH1-MIS-ISOTOPES-DIFFER-PROTONS WRONG_ANSWER_PATTERN 4CH1-CON-ISOTOPES` [high]

- node 4CH1-MIS-ISOTOPES-DIFFER-PROTONS — Believing isotopes of an element differ in their number of protons (MISCONCEPTION)
- node 4CH1-CON-ISOTOPES — Isotopes and relative atomic mass from isotopic abundances (CONCEPT)
-   spec 4CH1-1.16 [CORE]: know what is meant by the terms atomic number, mass number, isotopes and relative atomic mass...
-   spec 4CH1-1.17 [CORE]: be able to calculate the relative atomic mass of an element $ A_{r} $ from isotopic abundances
- derivation: ASSESSMENT_DOCUMENTED — The wrong answer is documented against the isotope questions (ATOM2 MS Q1(b) REJECT column — "why the isotopes have the same chemical properties"; ATOM3 MS Q1(a) documents "different numbers of protons" as an incorrect answer class on the isotope tables); the concept being tested is the isotope structure.
- `MARK_SCHEME` ATOM2_MS_P1.txt — "different number of protons"

```diff
@@ -3973,7 +3973,9 @@ edges:
       sha1 6c60d4721ea0)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-MIS-RAM-MASS-NUMBER
```

### 20. `4CH1-MIS-RAM-MASS-NUMBER REMEDIATED_BY 4CH1-CON-AR` [high]

- node 4CH1-MIS-RAM-MASS-NUMBER — Calling the Periodic Table relative atomic mass the mass number (MISCONCEPTION)
- node 4CH1-CON-AR — Relative atomic mass (Ar) (CONCEPT)
-   spec 4CH1-1.26 [CORE]: calculate relative formula masses(including relative molecular masses) $ (M_{r}) $ from relat...
-   spec 4CH1-1.28 [CORE]: understand how to carry out calculations involving amount of substance, relative atomic mass ...
- derivation: EXPLICIT_TEACH_SEQUENCE — Remediation = the Ar-on-the-Periodic-Table rule (which of the two numbers it is), plus the node-level remediation_evidence carrying the full Ar definition (abundance-weighted average, 1/12 carbon-12) — the corrective concept is the WAP target (the batch-1 B1-E-25 pattern). Cross-boundary target: the pilot CON-AR node.
- `NOTE` Calculate Relative Mass  Edexcel IGCSE Chemistry Revision Notes 2017.md — "The relative atomic mass of every element is given on the Periodic Table. It is the larger of the two numbers."

```diff
@@ -4140,6 +4140,8 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.26 @ Calculate Relative Mass (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
```

### 21. `4CH1-MIS-RAM-MASS-NUMBER WRONG_ANSWER_PATTERN 4CH1-CON-AR` [high]

- node 4CH1-MIS-RAM-MASS-NUMBER — Calling the Periodic Table relative atomic mass the mass number (MISCONCEPTION)
- node 4CH1-CON-AR — Relative atomic mass (Ar) (CONCEPT)
-   spec 4CH1-1.26 [CORE]: calculate relative formula masses(including relative molecular masses) $ (M_{r}) $ from relat...
-   spec 4CH1-1.28 [CORE]: understand how to carry out calculations involving amount of substance, relative atomic mass ...
- derivation: ASSESSMENT_DOCUMENTED — The wrong answer is documented against the Periodic Table reading question (PT MS Q1(b): "which number increases from 9 to 226 in Group 2?" — expected "(relative) atomic mass", REJECT "mass number"); the concept being tested is what the Periodic Table value means, i.e. the relative atomic mass. Cross-boundary target: the pilot CON-AR node (sanctioned per FN-B1-2).
- `MARK_SCHEME` PT_MS_P1.txt — "Reject mass number"

```diff
@@ -3996,7 +3996,9 @@ edges:
       sha1 fd6352a38077)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-MIS-CONC-UNIT
```

### 22. `4CH1-PR-02 REQUIRES_PREREQUISITE 4CH1-CON-CHROMATOGRAPHY` [high]

- node 4CH1-CON-CHROMATOGRAPHY — Paper chromatography (separation by differential solubility) (CONCEPT)
-   spec 4CH1-1.10 [CORE]: describe these experimental techniques for the separation of mixtures: 简单 distillation fracti...
- derivation: USED_WITHOUT_RETEACHING — Cross-boundary edge (target = the batch-1 CON-CHROMATOGRAPHY node, sanctioned per FN-B1-2): the 1.13 practical runs the paper-chromatography technique (its aim IS the technique applied to food colourings) without re-teaching the technique's ground — the practical note assumes the 1.10 separation concept.
- `NOTE` Paper chromatography - IGCSE Chemistry Revision Notes.md — "Investigate how paper chromatography can be used to separate and identify a mixture of food colourings"

```diff
@@ -3581,7 +3581,9 @@ edges:
       the batch-1 record (4CH1-1.10)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-PR-02
```

### 23. `4CH1-PR-02 REQUIRES_PREREQUISITE 4CH1-CON-RF-VALUE` [high]

- node 4CH1-CON-RF-VALUE — Retention factor (Rf) (CONCEPT)
-   spec 4CH1-1.12 [CORE]: understand how to use the calculation of $ R_{f} $ values to identify the components of a mix...
- derivation: USED_WITHOUT_RETEACHING — Cross-boundary edge (target = the batch-1 CON-RF-VALUE node, named explicitly by FN-B1-2 for this batch): the practical's results section uses Rf values and the solvent-front/spot-distance measurements without re-teaching the Rf concept (the 1.12 ground).
- `NOTE` Paper chromatography - IGCSE Chemistry Revision Notes.md — "The Rf values of food colours A, B, C and D should be compared to that for the unknown sample as well as a ..."

```diff
@@ -3605,7 +3605,9 @@ edges:
       the batch-1 record (4CH1-1.12)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-PR-03
```

## File-level meta hunks (once, for the whole batch)

```diff
@@ -84,8 +84,10 @@ meta:
     remediated_by_edges: 6
     requires_prerequisite_edges: 63
     wrong_answer_pattern_edges: 5
-    promoted_edges: 56
-    human_validated_edges: 56
+    promoted_edges: 79
+    human_validated_edges: 79
   promotion_record: scripts/c11_promotions.yaml
 edges:
 - source: 4CH1-CON-AR
```

## Not actionable (decided or ineligible)

- `4CH1-CON-CRYSTALLISATION REQUIRES_PREREQUISITE 4CH1-CON-SOLUTION` [DECIDED] decided: operator HOLD_REVIEW_REQUIRED (2026-09-12) — stays REVIEW_REQUIRED, not promotable (§18)
- `4CH1-CON-GAS-VOL-CALC REQUIRES_PREREQUISITE 4CH1-CON-AVOGADRO-LAW` [DECIDED] decided: operator HOLD (2026-09-11) — stays REVIEW_REQUIRED, not promotable (§18)
- `4CH1-CON-MOLAR-GAS-VOL EXPLAINED_BY 4CH1-CON-AVOGADRO-LAW` [DECIDED] operator HOLD (2026-09-12)
- `4CH1-CON-REACTING-MASS REQUIRES_PREREQUISITE 4CH1-CON-EQ-SYMBOL` [DECIDED] operator HOLD (2026-09-12)
- `4CH1-MIS-EQ-SUBSCRIPT REMEDIATED_BY 4CH1-CON-CONSERVATION-MASS` [DECIDED] operator HOLD (2026-09-12)

## Nodes awaiting verdicts — no §18 pathway yet (informational)

| node | title | family | spec points (role) | confidence |
|------|-------|--------|--------------------|------------|
| `4CH1-CON-AR` | Relative atomic mass (Ar) | CONCEPT | 4CH1-1.26 (CORE); 4CH1-1.28 (CORE) | high |
| `4CH1-CON-ATOM` | Atom (definition and subatomic composition) | CONCEPT | 4CH1-1.14 (CORE) | high |
| `4CH1-CON-ATOMIC-NUMBER` | Atomic number | CONCEPT | 4CH1-1.16 (CORE) | high |
| `4CH1-CON-AVOGADRO-CONST` | Avogadro constant | CONCEPT | 4CH1-1.27 (ENRICHMENT) | high |
| `4CH1-CON-AVOGADRO-LAW` | Avogadro's Law | CONCEPT | 4CH1-1.35C (ENRICHMENT) | high |
| `4CH1-CON-CHROMATOGRAM-INTERPRETATION` | Interpreting chromatograms | CONCEPT | 4CH1-1.11 (CORE) | high |
| `4CH1-CON-CHROMATOGRAPHY` | Paper chromatography (separation by differential solubility) | CONCEPT | 4CH1-1.10 (CORE) | high |
| `4CH1-CON-COMPOUND` | Compound | CONCEPT | 4CH1-1.8 (CORE) | high |
| `4CH1-CON-CONC-CALC` | Concentration calculation (mol/dm3) | CONCEPT | 4CH1-1.34C (CORE) | high |
| `4CH1-CON-CONCENTRATION` | Concentration of a solution | CONCEPT | 4CH1-1.34C (CORE) | high |
| `4CH1-CON-CONSERVATION-MASS` | Law of Conservation of Mass | CONCEPT | 4CH1-1.25 (CORE); 4CH1-1.26 (SUPPORTING) | high |
| `4CH1-CON-CRYSTALLISATION` | Crystallisation | CONCEPT | 4CH1-1.10 (CORE) | high |
| `4CH1-CON-DIFFUSION` | Diffusion in gases and liquids | CONCEPT | 4CH1-1.3 (CORE) | high |
| `4CH1-CON-DILUTION` | Dilution of coloured solutions | CONCEPT | 4CH1-1.3 (CORE) | high |
| `4CH1-CON-ELECTRONIC-CONFIGURATION` | Electronic configuration of the first 20 elements (shells 2, 8, 8; configuration and Periodic Table position) | CONCEPT | 4CH1-1.19 (CORE); 4CH1-1.22 (CORE) | high |
| `4CH1-CON-ELEMENT` | Element | CONCEPT | 4CH1-1.8 (CORE) | high |
| `4CH1-CON-EMP-MOL-CALC` | Empirical and molecular formula calculation | CONCEPT | 4CH1-1.33 (CORE) | high |
| `4CH1-CON-EMPIRICAL-FORMULA` | Empirical formula | CONCEPT | 4CH1-1.32 (CORE); 4CH1-1.33 (CORE) | high |
| `4CH1-CON-EQ-STATE-SYM` | State symbols (s), (l), (g), (aq) | CONCEPT | 4CH1-1.25 (CORE) | high |
| `4CH1-CON-EQ-SYMBOL` | Balanced symbol (chemical) equation | CONCEPT | 4CH1-1.25 (CORE) | high |
| `4CH1-CON-EQ-WORD` | Word equation | CONCEPT | 4CH1-1.25 (CORE) | high |
| `4CH1-CON-EVAPORATION-BOILING` | Evaporation and its distinction from boiling | CONCEPT | 4CH1-1.2 (ENRICHMENT) | high |
| `4CH1-CON-EXP-FORMULA-DEDUCTION` | Experimental formula deduction (mass-difference method) | CONCEPT | 4CH1-1.31 (CORE); 4CH1-1.36 (CORE) | high |
| `4CH1-CON-FILTRATION` | Filtration | CONCEPT | 4CH1-1.10 (CORE) | high |
| `4CH1-CON-FRACTIONAL-DISTILLATION` | Fractional distillation | CONCEPT | 4CH1-1.10 (CORE) | high |
| `4CH1-CON-GAS-VOL-CALC` | Gas volume calculation | CONCEPT | 4CH1-1.35C (CORE) | high |
| `4CH1-CON-GROUP-SIMILARITY` | Why elements in the same group have similar chemical properties | CONCEPT | 4CH1-1.23 (CORE) | high |
| `4CH1-CON-HEATING-CONSTANT-MASS` | Heating to constant mass | CONCEPT | 4CH1-1.7C (ENRICHMENT) | high |
| `4CH1-CON-ISOTOPES` | Isotopes and relative atomic mass from isotopic abundances | CONCEPT | 4CH1-1.16 (CORE); 4CH1-1.17 (CORE) | high |
| `4CH1-CON-MASS-NUMBER` | Mass number | CONCEPT | 4CH1-1.16 (CORE) | high |
| `4CH1-CON-METAL-NONMETAL` | Classifying elements as metals or non-metals (by properties and by Periodic Table position) | CONCEPT | 4CH1-1.20 (CORE); 4CH1-1.21 (CORE) | high |
| `4CH1-CON-METALLOID` | Semi-metals (metalloids) — elements bordering the metal/non-metal divide | CONCEPT | 4CH1-1.21 (ENRICHMENT) | high |
| `4CH1-CON-MIXTURE` | Mixture | CONCEPT | 4CH1-1.8 (CORE) | high |
| `4CH1-CON-MOLAR-GAS-VOL` | Molar gas volume at RTP (24 dm3) | CONCEPT | 4CH1-1.35C (CORE) | high |
| `4CH1-CON-MOLAR-MASS` | Molar mass | CONCEPT | 4CH1-1.28 (CORE) | high |
| `4CH1-CON-MOLAR-RATIO` | Molar ratio from balanced equations | CONCEPT | 4CH1-1.29 (CORE) | high |
| `4CH1-CON-MOLE` | The mole (unit of amount of substance) | CONCEPT | 4CH1-1.27 (CORE) | high |
| `4CH1-CON-MOLE-MASS-CONV` | Mole-mass conversion | CONCEPT | 4CH1-1.28 (CORE) | high |
| `4CH1-CON-MOLECULAR-FORMULA` | Molecular formula | CONCEPT | 4CH1-1.32 (CORE); 4CH1-1.33 (CORE) | high |
| `4CH1-CON-MOLECULE` | Molecule | CONCEPT | 4CH1-1.14 (CORE) | high |
| `4CH1-CON-MR` | Relative formula mass (Mr) | CONCEPT | 4CH1-1.26 (CORE); 4CH1-1.28 (CORE) | high |
| `4CH1-CON-NOBLE-GAS-INERTNESS` | Why the noble gases (Group 0) do not readily react | CONCEPT | 4CH1-1.24 (CORE) | high |
| `4CH1-CON-PERCENT-YIELD` | Percentage yield | CONCEPT | 4CH1-1.30 (CORE) | high |
| `4CH1-CON-PERIODIC-TABLE` | Periodic Table arrangement (atomic-number order, groups and periods) | CONCEPT | 4CH1-1.18 (CORE) | high |
| `4CH1-CON-PURE-SUBSTANCE` | Pure substance (chemical sense) and fixed melting/boiling points | CONCEPT | 4CH1-1.9 (CORE) | high |
| `4CH1-CON-REACTING-MASS` | Reacting mass calculation | CONCEPT | 4CH1-1.29 (CORE) | high |
| `4CH1-CON-RF-VALUE` | Retention factor (Rf) | CONCEPT | 4CH1-1.12 (CORE) | high |
| `4CH1-CON-SATURATED-SOLUTION` | Saturated solution | CONCEPT | 4CH1-1.4 (CORE); 4CH1-1.10 (SUPPORTING) | high |
| `4CH1-CON-SIMPLE-DISTILLATION` | Simple distillation | CONCEPT | 4CH1-1.10 (CORE) | high |
| `4CH1-CON-SOLUBILITY` | Solubility (g per 100 g of solvent) | CONCEPT | 4CH1-1.5C (CORE) | high |
| `4CH1-CON-SOLUBILITY-CURVE` | Solubility curves (plotting and interpreting) | CONCEPT | 4CH1-1.6C (CORE) | high |
| `4CH1-CON-SOLUTION` | Solution, solute and solvent | CONCEPT | 4CH1-1.4 (CORE) | high |
| `4CH1-CON-STATE-CHANGES` | Interconversions between the three states (melting, freezing, boiling, condensation, sublimation) | CONCEPT | 4CH1-1.2 (CORE) | high |
| `4CH1-CON-STATE-PARTICLE-MODEL` | Particle arrangement, movement and energy in the three states | CONCEPT | 4CH1-1.1 (CORE); 4CH1-1.3 (SUPPORTING) | high |
| `4CH1-CON-STATES-THREE` | The three states of matter (solid, liquid, gas) | CONCEPT | 4CH1-1.1 (CORE) | high |
| `4CH1-CON-SUBATOMIC-PARTICLES` | Subatomic particles (proton, neutron, electron — positions, relative masses, relative charges) | CONCEPT | 4CH1-1.15 (CORE) | high |
| `4CH1-CON-THEOR-YIELD` | Theoretical yield | CONCEPT | 4CH1-1.30 (CORE) | high |
| `4CH1-CON-VOL-CONVERSION` | Volume unit conversion (cm3/dm3) | CONCEPT | 4CH1-1.34C (CORE) | high |
| `4CH1-CON-WATER-CRYST` | Water of crystallisation and hydrated salts | CONCEPT | 4CH1-1.31 (CORE) | high |
| `4CH1-CON-YIELD` | Yield (actual yield) | CONCEPT | 4CH1-1.30 (CORE) | high |
| `4CH1-CON-YIELD-FACTORS` | Factors reducing yield | CONCEPT | 4CH1-1.30 (ENRICHMENT) | high |
| `4CH1-MIS-CONC-UNIT` | Failing to convert cm3 to dm3 in concentration calculations | MISCONCEPTION |  | high |
| `4CH1-MIS-CRYSTALLISATION-DRYNESS` | Obtaining crystals by evaporating to dryness | MISCONCEPTION |  | high |
| `4CH1-MIS-EQ-SUBSCRIPT` | Balancing equations by altering subscripts | MISCONCEPTION |  | high |
| `4CH1-MIS-GAS-PARTICLES-TOUCH` | Drawing gas particles touching each other or joined by bonds | MISCONCEPTION |  | high |
| `4CH1-MIS-ISOTOPES-DIFFER-PROTONS` | Believing isotopes of an element differ in their number of protons | MISCONCEPTION |  | high |
| `4CH1-MIS-RAM-MASS-NUMBER` | Calling the Periodic Table relative atomic mass the mass number | MISCONCEPTION |  | high |

