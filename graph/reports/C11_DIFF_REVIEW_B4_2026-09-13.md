# C11 Diff Review Bundle — pending §18 edge promotions (generated 2026-09-13)

- baseline commit: `b2c880a`
- state fingerprint: `b891d15e7dc4` (promo_count=118)
- actionable: 35 edges (clean 35 / pending-flagged 0); not-actionable: 5; nodes awaiting a pathway: 113
- preview fidelity: simulator re-emits graph/concept_edges.yaml under the generator's own serialization contract with a byte-identity guard — what you read is what G13 will write.

## Batch approval

```bash
cd work/syllabai-resources && python3 scripts/c11_diff_review.py approve \
  '4CH1-CON-BOND-BREAKING-MAKING REQUIRES_PREREQUISITE 4CH1-CON-EXO-ENDO' \
  '4CH1-CON-BOND-ENERGY-CALC REQUIRES_PREREQUISITE 4CH1-CON-BOND-BREAKING-MAKING' \
  '4CH1-CON-BOND-ENERGY-CALC REQUIRES_PREREQUISITE 4CH1-CON-COVALENT-BOND' \
  '4CH1-CON-CATALYST REQUIRES_PREREQUISITE 4CH1-CON-ACTIVATION-ENERGY' \
  '4CH1-CON-DYNAMIC-EQUILIBRIUM REQUIRES_PREREQUISITE 4CH1-CON-REVERSIBLE' \
  '4CH1-CON-ENERGY-LEVEL-DIAGRAM REQUIRES_PREREQUISITE 4CH1-CON-EXO-ENDO' \
  '4CH1-CON-EQ-POSITION REQUIRES_PREREQUISITE 4CH1-CON-CATALYST' \
  '4CH1-CON-EQ-POSITION REQUIRES_PREREQUISITE 4CH1-CON-DYNAMIC-EQUILIBRIUM' \
  '4CH1-CON-EQ-POSITION REQUIRES_PREREQUISITE 4CH1-CON-EXO-ENDO' \
  '4CH1-CON-HEAT-CALC REQUIRES_PREREQUISITE 4CH1-CON-CALORIMETRY' \
  '4CH1-CON-HEAT-CALC REQUIRES_PREREQUISITE 4CH1-CON-EXO-ENDO' \
  '4CH1-CON-MOLAR-ENTHALPY REQUIRES_PREREQUISITE 4CH1-CON-HEAT-CALC' \
  '4CH1-CON-MOLAR-ENTHALPY REQUIRES_PREREQUISITE 4CH1-CON-MOLE' \
  '4CH1-CON-RATE-FACTORS EXPLAINED_BY 4CH1-CON-COLLISION-THEORY' \
  '4CH1-CON-RATE-FACTORS REQUIRES_PREREQUISITE 4CH1-CON-CONCENTRATION' \
  '4CH1-CON-REACTION-PROFILE REQUIRES_PREREQUISITE 4CH1-CON-ACTIVATION-ENERGY' \
  '4CH1-CON-REACTION-PROFILE REQUIRES_PREREQUISITE 4CH1-CON-ENERGY-LEVEL-DIAGRAM' \
  '4CH1-CON-REVERSIBLE REQUIRES_PREREQUISITE 4CH1-CON-EQ-SYMBOL' \
  '4CH1-CON-REVERSIBLE-EXAMPLES REQUIRES_PREREQUISITE 4CH1-CON-REVERSIBLE' \
  '4CH1-CON-REVERSIBLE-EXAMPLES REQUIRES_PREREQUISITE 4CH1-CON-WATER-CRYST' \
  '4CH1-MIS-BOND-ENERGY-COUNT REMEDIATED_BY 4CH1-CON-BOND-ENERGY-CALC' \
  '4CH1-MIS-BOND-ENERGY-COUNT WRONG_ANSWER_PATTERN 4CH1-CON-BOND-ENERGY-CALC' \
  '4CH1-MIS-CATALYST-PARTICLE-ENERGY REMEDIATED_BY 4CH1-CON-CATALYST' \
  '4CH1-MIS-CATALYST-PARTICLE-ENERGY WRONG_ANSWER_PATTERN 4CH1-CON-CATALYST' \
  '4CH1-MIS-ENTHALPY-UNIT-J REMEDIATED_BY 4CH1-CON-MOLAR-ENTHALPY' \
  '4CH1-MIS-ENTHALPY-UNIT-J WRONG_ANSWER_PATTERN 4CH1-CON-MOLAR-ENTHALPY' \
  '4CH1-MIS-EQ-PRESSURE-FEWER REMEDIATED_BY 4CH1-CON-EQ-POSITION' \
  '4CH1-MIS-EQ-PRESSURE-FEWER WRONG_ANSWER_PATTERN 4CH1-CON-EQ-POSITION' \
  '4CH1-MIS-EQ-TEMP-EXO REMEDIATED_BY 4CH1-CON-EQ-POSITION' \
  '4CH1-MIS-EQ-TEMP-EXO WRONG_ANSWER_PATTERN 4CH1-CON-EQ-POSITION' \
  '4CH1-PR-09 REQUIRES_PREREQUISITE 4CH1-CON-CALORIMETRY' \
  '4CH1-PR-10 REQUIRES_PREREQUISITE 4CH1-CON-RATE-EXPERIMENTS' \
  '4CH1-PR-10 REQUIRES_PREREQUISITE 4CH1-CON-RATE-FACTORS' \
  '4CH1-PR-11 REQUIRES_PREREQUISITE 4CH1-CON-CATALYST' \
  '4CH1-PR-11 REQUIRES_PREREQUISITE 4CH1-CON-RATE-EXPERIMENTS' \
  --by <operator> --date 2026-09-13 --review-ref graph/reports/C11_DIFF_REVIEW_B4_2026-09-13.md
```

Pending-flagged (PENDING operator_decision) edges are excluded from the command above; approving them additionally requires `--include-pending` — that flag records the explicit decision this bundle presents.

## Index

| # | identity | confidence | flag |
|---|----------|------------|------|
| 1 | `4CH1-CON-BOND-BREAKING-MAKING REQUIRES_PREREQUISITE 4CH1-CON-EXO-ENDO` | high |  |
| 2 | `4CH1-CON-BOND-ENERGY-CALC REQUIRES_PREREQUISITE 4CH1-CON-BOND-BREAKING-MAKING` | high |  |
| 3 | `4CH1-CON-BOND-ENERGY-CALC REQUIRES_PREREQUISITE 4CH1-CON-COVALENT-BOND` | medium |  |
| 4 | `4CH1-CON-CATALYST REQUIRES_PREREQUISITE 4CH1-CON-ACTIVATION-ENERGY` | high |  |
| 5 | `4CH1-CON-DYNAMIC-EQUILIBRIUM REQUIRES_PREREQUISITE 4CH1-CON-REVERSIBLE` | high |  |
| 6 | `4CH1-CON-ENERGY-LEVEL-DIAGRAM REQUIRES_PREREQUISITE 4CH1-CON-EXO-ENDO` | high |  |
| 7 | `4CH1-CON-EQ-POSITION REQUIRES_PREREQUISITE 4CH1-CON-CATALYST` | high |  |
| 8 | `4CH1-CON-EQ-POSITION REQUIRES_PREREQUISITE 4CH1-CON-DYNAMIC-EQUILIBRIUM` | high |  |
| 9 | `4CH1-CON-EQ-POSITION REQUIRES_PREREQUISITE 4CH1-CON-EXO-ENDO` | high |  |
| 10 | `4CH1-CON-HEAT-CALC REQUIRES_PREREQUISITE 4CH1-CON-CALORIMETRY` | high |  |
| 11 | `4CH1-CON-HEAT-CALC REQUIRES_PREREQUISITE 4CH1-CON-EXO-ENDO` | high |  |
| 12 | `4CH1-CON-MOLAR-ENTHALPY REQUIRES_PREREQUISITE 4CH1-CON-HEAT-CALC` | high |  |
| 13 | `4CH1-CON-MOLAR-ENTHALPY REQUIRES_PREREQUISITE 4CH1-CON-MOLE` | high |  |
| 14 | `4CH1-CON-RATE-FACTORS EXPLAINED_BY 4CH1-CON-COLLISION-THEORY` | high |  |
| 15 | `4CH1-CON-RATE-FACTORS REQUIRES_PREREQUISITE 4CH1-CON-CONCENTRATION` | high |  |
| 16 | `4CH1-CON-REACTION-PROFILE REQUIRES_PREREQUISITE 4CH1-CON-ACTIVATION-ENERGY` | high |  |
| 17 | `4CH1-CON-REACTION-PROFILE REQUIRES_PREREQUISITE 4CH1-CON-ENERGY-LEVEL-DIAGRAM` | high |  |
| 18 | `4CH1-CON-REVERSIBLE REQUIRES_PREREQUISITE 4CH1-CON-EQ-SYMBOL` | high |  |
| 19 | `4CH1-CON-REVERSIBLE-EXAMPLES REQUIRES_PREREQUISITE 4CH1-CON-REVERSIBLE` | high |  |
| 20 | `4CH1-CON-REVERSIBLE-EXAMPLES REQUIRES_PREREQUISITE 4CH1-CON-WATER-CRYST` | high |  |
| 21 | `4CH1-MIS-BOND-ENERGY-COUNT REMEDIATED_BY 4CH1-CON-BOND-ENERGY-CALC` | high |  |
| 22 | `4CH1-MIS-BOND-ENERGY-COUNT WRONG_ANSWER_PATTERN 4CH1-CON-BOND-ENERGY-CALC` | medium |  |
| 23 | `4CH1-MIS-CATALYST-PARTICLE-ENERGY REMEDIATED_BY 4CH1-CON-CATALYST` | high |  |
| 24 | `4CH1-MIS-CATALYST-PARTICLE-ENERGY WRONG_ANSWER_PATTERN 4CH1-CON-CATALYST` | high |  |
| 25 | `4CH1-MIS-ENTHALPY-UNIT-J REMEDIATED_BY 4CH1-CON-MOLAR-ENTHALPY` | high |  |
| 26 | `4CH1-MIS-ENTHALPY-UNIT-J WRONG_ANSWER_PATTERN 4CH1-CON-MOLAR-ENTHALPY` | high |  |
| 27 | `4CH1-MIS-EQ-PRESSURE-FEWER REMEDIATED_BY 4CH1-CON-EQ-POSITION` | high |  |
| 28 | `4CH1-MIS-EQ-PRESSURE-FEWER WRONG_ANSWER_PATTERN 4CH1-CON-EQ-POSITION` | medium |  |
| 29 | `4CH1-MIS-EQ-TEMP-EXO REMEDIATED_BY 4CH1-CON-EQ-POSITION` | high |  |
| 30 | `4CH1-MIS-EQ-TEMP-EXO WRONG_ANSWER_PATTERN 4CH1-CON-EQ-POSITION` | high |  |
| 31 | `4CH1-PR-09 REQUIRES_PREREQUISITE 4CH1-CON-CALORIMETRY` | high |  |
| 32 | `4CH1-PR-10 REQUIRES_PREREQUISITE 4CH1-CON-RATE-EXPERIMENTS` | high |  |
| 33 | `4CH1-PR-10 REQUIRES_PREREQUISITE 4CH1-CON-RATE-FACTORS` | high |  |
| 34 | `4CH1-PR-11 REQUIRES_PREREQUISITE 4CH1-CON-CATALYST` | high |  |
| 35 | `4CH1-PR-11 REQUIRES_PREREQUISITE 4CH1-CON-RATE-EXPERIMENTS` | high |  |

## Pending items — the exact diff each approval applies

### 1. `4CH1-CON-BOND-BREAKING-MAKING REQUIRES_PREREQUISITE 4CH1-CON-EXO-ENDO` [high]

- node 4CH1-CON-BOND-BREAKING-MAKING — Bond-breaking endothermic, bond-making exothermic (CONCEPT)
-   spec 4CH1-3.6C [CORE]: know that bond-breaking is an endothermic process and that bond-making is an exothermic process
- node 4CH1-CON-EXO-ENDO — Exothermic and endothermic reactions (heat energy given out or taken in) (CONCEPT)
-   spec 4CH1-3.1 [CORE]: know that chemical reactions in which heat energy is given out are described as exothermic, a...
- derivation: USED_WITHOUT_RETEACHING — The bond-energy note classifies bond breaking and bond making BY the 3.1 exo/endo classification (each statement hyperlinks back to the exothermic/endothermic note rather than re-teaching it) — the classification terms are the operands of the 3.6C rule.
- `NOTE` What is bond energy - IGCSE Chemistry Revision Notes.md — "Because energy is being taken in, bond breaking is an endothermic process"

```diff
@@ -3889,7 +3889,9 @@ edges:
       this record (4CH1-3.1)
     generated_date: '2026-09-13'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-13'
 - source: 4CH1-CON-BOND-ENERGY-CALC
```

### 2. `4CH1-CON-BOND-ENERGY-CALC REQUIRES_PREREQUISITE 4CH1-CON-BOND-BREAKING-MAKING` [high]

- node 4CH1-CON-BOND-ENERGY-CALC — Bond energy calculations (enthalpy change from bond energies) (CONCEPT)
-   spec 4CH1-3.7C [CORE]: use bond energies to calculate the enthalpy change during a chemical reaction
- node 4CH1-CON-BOND-BREAKING-MAKING — Bond-breaking endothermic, bond-making exothermic (CONCEPT)
-   spec 4CH1-3.6C [CORE]: know that bond-breaking is an endothermic process and that bond-making is an exothermic process
- derivation: DEFINITIONAL_DEPENDENCY — Bond energy is DEFINED over the 3.6C breaking/making energetics ("the amount of energy required to break the bond or... given out when the bond is formed"): the 3.7C calculation's operands are exactly the 3.6C breaking/making energies, and the spec's own order is know-then-use (3.6C -> 3.7C).
- `NOTE` What is bond energy - IGCSE Chemistry Revision Notes.md — "This is the amount of energy required to break the bond or the amount of energy given out when the bond is ..."

```diff
@@ -3913,7 +3913,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-3.6C/3.7C @ What is Bond Energy (2026-09-11)
     generated_date: '2026-09-13'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-13'
 - source: 4CH1-CON-BOND-ENERGY-CALC
```

### 3. `4CH1-CON-BOND-ENERGY-CALC REQUIRES_PREREQUISITE 4CH1-CON-COVALENT-BOND` [medium]

- node 4CH1-CON-BOND-ENERGY-CALC — Bond energy calculations (enthalpy change from bond energies) (CONCEPT)
-   spec 4CH1-3.7C [CORE]: use bond energies to calculate the enthalpy change during a chemical reaction
- node 4CH1-CON-COVALENT-BOND — Covalent bond (shared pair of electrons; electrostatic attraction between the shared pair and the nuclei) (CONCEPT)
-   spec 4CH1-1.44 [CORE]: know that a covalent bond is formed between atoms by the sharing of a pair of electrons
-   spec 4CH1-1.45 [CORE]: understand covalent bonds in terms of electrostatic attractions
- derivation: USED_WITHOUT_RETEACHING — CROSS-SECTION boundary edge (B4-E-07), sanctioned by the session-52 cross-slice boundary ruling ("bond-energy work (3.6C/3.7C) presupposes the covalent bond the energies are measured over"): the calculation presupposes identifying the bonds present in reactants and products, and every bond-energy operand in the note's worked examples (H-H, Cl-Cl, H-Cl, H-Br, Br-Br — the 1.46 diatomic set) is a covalent bond of the S1 concept universe; the covalent-bond concept is used without re-teaching. Confidence medium, recorded not silent: the note's own text says "chemical bond" (not "covalent bond") — the covalent-bond attribution rests on the worked-example bond set plus the ruling, not on the term itself.
- `NOTE` What is bond energy - IGCSE Chemistry Revision Notes.md — "Each chemical bond has a specific bond energy associated with it"
- `NOTE` What is bond energy - IGCSE Chemistry Revision Notes.md — "To do this it is necessary to know the bonds present in both the reactants and products"

```diff
@@ -3945,7 +3945,9 @@ edges:
       the batch-3 record (4CH1-1.44/1.45); session-52 cross-slice boundary ruling sanctioned target
     generated_date: '2026-09-13'
   confidence: medium
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-13'
 - source: 4CH1-CON-CATALYST
```

### 4. `4CH1-CON-CATALYST REQUIRES_PREREQUISITE 4CH1-CON-ACTIVATION-ENERGY` [high]

- node 4CH1-CON-CATALYST — Catalysts (increase rate, chemically unchanged; alternative pathway at lower activation energy) (CONCEPT)
-   spec 4CH1-3.12 [CORE]: know that a catalyst is a substance that increases the rate of a reaction, but is chemically ...
-   spec 4CH1-3.13 [CORE]: know that a catalyst works by providing an alternative pathway with lower activation energy
- node 4CH1-CON-ACTIVATION-ENERGY — Activation energy (minimum energy for reaction; Ea) (CONCEPT)
-   spec 4CH1-3.14C [CORE]: draw and explain reaction profile diagrams showing $\Delta H$ and activation energy
- derivation: USED_WITHOUT_RETEACHING — The 3.13 mechanism is stated in activation-energy terms without defining activation energy (the 3.14C concept — the two notes cross-reference each other): the catalyst mechanism presupposes the Ea quantity it lowers.
- `NOTE` Catalysts in Chemistry - IGCSE Chemistry Revision Notes.md — "The alternative pathway has a lower activation energy"

```diff
@@ -3968,7 +3968,9 @@ edges:
       by this record (4CH1-3.14C)
     generated_date: '2026-09-13'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-13'
 - source: 4CH1-CON-CHROMATOGRAM-INTERPRETATION
```

### 5. `4CH1-CON-DYNAMIC-EQUILIBRIUM REQUIRES_PREREQUISITE 4CH1-CON-REVERSIBLE` [high]

- node 4CH1-CON-DYNAMIC-EQUILIBRIUM — Dynamic equilibrium (sealed container; equal forward and reverse rates; constant concentrations) (CONCEPT)
-   spec 4CH1-3.19C [CORE]: know that a reversible reaction can reach dynamic equilibrium in a sealed container
-   spec 4CH1-3.20C [CORE]: know that the characteristics of a reaction at dynamic equilibrium are: • the forward and rev...
- node 4CH1-CON-REVERSIBLE — Reversible reactions and the ⇌ notation (CONCEPT)
-   spec 4CH1-3.17 [CORE]: know that some reactions are reversible and this is indicated by the symbol $\rightleftharpoo...
- derivation: DEFINITIONAL_DEPENDENCY — Dynamic equilibrium is defined OVER the reversible reaction (the note opens by re-using the 3.17 definition verbatim, then defines equilibrium as the equal-rates state of that reversible reaction) — the 3.19C/3.20C concept presupposes the 3.17 concept it is a state of.
- `NOTE` Dynamic equilibrium - IGCSE Chemistry Revision Notes.md — "A reversible reaction is one which occurs in both directions"
- `NOTE` Dynamic equilibrium - IGCSE Chemistry Revision Notes.md — "When the rate of the forward reaction equals the rate of the reverse reaction, the overall reaction is said..."

```diff
@@ -4375,7 +4375,9 @@ edges:
       by this record (4CH1-3.17)
     generated_date: '2026-09-13'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-13'
 - source: 4CH1-CON-ELECTRODE-HALF-EQUATIONS
```

### 6. `4CH1-CON-ENERGY-LEVEL-DIAGRAM REQUIRES_PREREQUISITE 4CH1-CON-EXO-ENDO` [high]

- node 4CH1-CON-ENERGY-LEVEL-DIAGRAM — Energy level diagrams for exothermic and endothermic reactions (CONCEPT)
-   spec 4CH1-3.5C [CORE]: draw and explain energy level diagrams to represent exothermic and endothermic reactions
- node 4CH1-CON-EXO-ENDO — Exothermic and endothermic reactions (heat energy given out or taken in) (CONCEPT)
-   spec 4CH1-3.1 [CORE]: know that chemical reactions in which heat energy is given out are described as exothermic, a...
- derivation: DEFINITIONAL_DEPENDENCY — The diagram's semantics are defined BY the 3.1 classification: which level sits higher, which way the arrow points (down = exo, up = endo), and the sign of the energy change — drawing and reading a 3.5C diagram presupposes the exo/endo distinction it encodes.
- `NOTE` Energy level diagrams - IGCSE Chemistry Revision Notes.md — "Arrows on the diagrams indicate whether the reaction is exothermic (downwards pointing) or endothermic (upw..."
- `NOTE` Energy level diagrams - IGCSE Chemistry Revision Notes.md — "The difference in height between the energy of reactants and products represents the overall enthalpy chang..."

```diff
@@ -4652,7 +4652,9 @@ edges:
       by this record (4CH1-3.1)
     generated_date: '2026-09-13'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-13'
 - source: 4CH1-CON-EQ-POSITION
```

### 7. `4CH1-CON-EQ-POSITION REQUIRES_PREREQUISITE 4CH1-CON-CATALYST` [high]

- node 4CH1-CON-EQ-POSITION — Position of equilibrium (temperature and pressure effects; catalyst does not affect it) (CONCEPT)
-   spec 4CH1-3.21C [CORE]: understand why a catalyst does not affect the position of equilibrium in a reversible reaction
-   spec 4CH1-3.22C [CORE]: know the effect of changing either temperature or pressure on the position of equilibrium in ...
- node 4CH1-CON-CATALYST — Catalysts (increase rate, chemically unchanged; alternative pathway at lower activation energy) (CONCEPT)
-   spec 4CH1-3.12 [CORE]: know that a catalyst is a substance that increases the rate of a reaction, but is chemically ...
-   spec 4CH1-3.13 [CORE]: know that a catalyst works by providing an alternative pathway with lower activation energy
- derivation: USED_WITHOUT_RETEACHING — 3.21C is stated over the catalyst concept (the sentence is about the catalyst's effect on the equilibrium) without re-teaching what a catalyst is — the 3.12/3.13 concept is the operand of the 3.21C rule.
- `NOTE` The position of equilibrium - IGCSE Chemistry Revision Notes.md — "The presence of a catalyst does not affect the position of equilibrium but it does increase the rate at whi..."

```diff
@@ -4676,7 +4676,9 @@ edges:
       owned by this record (4CH1-3.12/3.13)
     generated_date: '2026-09-13'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-13'
 - source: 4CH1-CON-EQ-POSITION
```

### 8. `4CH1-CON-EQ-POSITION REQUIRES_PREREQUISITE 4CH1-CON-DYNAMIC-EQUILIBRIUM` [high]

- node 4CH1-CON-EQ-POSITION — Position of equilibrium (temperature and pressure effects; catalyst does not affect it) (CONCEPT)
-   spec 4CH1-3.21C [CORE]: understand why a catalyst does not affect the position of equilibrium in a reversible reaction
-   spec 4CH1-3.22C [CORE]: know the effect of changing either temperature or pressure on the position of equilibrium in ...
- node 4CH1-CON-DYNAMIC-EQUILIBRIUM — Dynamic equilibrium (sealed container; equal forward and reverse rates; constant concentrations) (CONCEPT)
-   spec 4CH1-3.19C [CORE]: know that a reversible reaction can reach dynamic equilibrium in a sealed container
-   spec 4CH1-3.20C [CORE]: know that the characteristics of a reaction at dynamic equilibrium are: • the forward and rev...
- derivation: DEFINITIONAL_DEPENDENCY — The position of equilibrium is defined as the relative amounts of reactants and products AT equilibrium — the 3.21C/3.22C rules are about a property of the 3.19C/3.20C equilibrium state, which they presuppose.
- `NOTE` The position of equilibrium - IGCSE Chemistry Revision Notes.md — "The relative amounts of all the reactants and products at equilibrium depend on the conditions of the reaction"

```diff
@@ -4700,7 +4700,9 @@ edges:
       node owned by this record (4CH1-3.19C/3.20C)
     generated_date: '2026-09-13'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-13'
 - source: 4CH1-CON-EQ-POSITION
```

### 9. `4CH1-CON-EQ-POSITION REQUIRES_PREREQUISITE 4CH1-CON-EXO-ENDO` [high]

- node 4CH1-CON-EQ-POSITION — Position of equilibrium (temperature and pressure effects; catalyst does not affect it) (CONCEPT)
-   spec 4CH1-3.21C [CORE]: understand why a catalyst does not affect the position of equilibrium in a reversible reaction
-   spec 4CH1-3.22C [CORE]: know the effect of changing either temperature or pressure on the position of equilibrium in ...
- node 4CH1-CON-EXO-ENDO — Exothermic and endothermic reactions (heat energy given out or taken in) (CONCEPT)
-   spec 4CH1-3.1 [CORE]: know that chemical reactions in which heat energy is given out are described as exothermic, a...
- derivation: USED_WITHOUT_RETEACHING — The corpus states the prerequisite explicitly: applying the 3.22C temperature rule "is necessary to know whether the reaction is exothermic or endothermic" — the 3.1 classification is the operand of the temperature-shift rule (the strongest possible used-without-reteaching evidence: the note itself declares the dependency).
- `NOTE` The position of equilibrium - IGCSE Chemistry Revision Notes.md — "To make this prediction it is necessary to know whether the reaction is exothermic or endothermic"

```diff
@@ -4724,7 +4724,9 @@ edges:
       owned by this record (4CH1-3.1)
     generated_date: '2026-09-13'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-13'
 - source: 4CH1-CON-EVAPORATION-BOILING
```

### 10. `4CH1-CON-HEAT-CALC REQUIRES_PREREQUISITE 4CH1-CON-CALORIMETRY` [high]

- node 4CH1-CON-HEAT-CALC — Heat energy change calculation (Q = mcΔT) (CONCEPT)
-   spec 4CH1-3.3 [CORE]: calculate the heat energy change from a measured temperature change using the expression $ Q=...
- node 4CH1-CON-CALORIMETRY — Simple calorimetry experiments (reactions in solution and combustion) (CONCEPT)
-   spec 4CH1-3.2 [CORE]: describe simple calorimetry experiments for reactions such as combustion, displacement, disso...
- derivation: EXPLICIT_TEACH_SEQUENCE — The 3.2 calorimetry note teaches the Q calculation INSIDE the experimental method (each method ends "The energy released would be calculated using: Q = m x c x ΔT"), and the 3.3 note's worked example then runs on calorimetry data (set "in a calorimeter", temperature rise measured) — the 3.3 calculation operates on the measured temperature change the 3.2 experiments produce (the spec's own "from a measured temperature change").
- `NOTE` Calorimetry - IGCSE Chemistry Revision Notes.md — "The energy released would be calculated using"
- `NOTE` Energetics calculations in chemistry - IGCSE Revision Notes.md — "Excess iron powder was added to 100.0 cm"

```diff
@@ -4972,7 +4972,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-3.2 @ Calorimetry + 4CH1-3.3 @ Energetics Calculations (2026-09-11)
     generated_date: '2026-09-13'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-13'
 - source: 4CH1-CON-HEAT-CALC
```

### 11. `4CH1-CON-HEAT-CALC REQUIRES_PREREQUISITE 4CH1-CON-EXO-ENDO` [high]

- node 4CH1-CON-HEAT-CALC — Heat energy change calculation (Q = mcΔT) (CONCEPT)
-   spec 4CH1-3.3 [CORE]: calculate the heat energy change from a measured temperature change using the expression $ Q=...
- node 4CH1-CON-EXO-ENDO — Exothermic and endothermic reactions (heat energy given out or taken in) (CONCEPT)
-   spec 4CH1-3.1 [CORE]: know that chemical reactions in which heat energy is given out are described as exothermic, a...
- derivation: USED_WITHOUT_RETEACHING — The sign-application step of the 3.3 procedure uses the 3.1 exo/endo classification without re-teaching it (the worked example: "Apply the sign: The temperature increased... So, the reaction is exothermic... Exothermic reactions have a negative enthalpy change") — the classification is the operand of the sign step.
- `NOTE` Energetics calculations in chemistry - IGCSE Revision Notes.md — "Exothermic reactions have a negative enthalpy change"

```diff
@@ -4996,7 +4996,9 @@ edges:
       by this record (4CH1-3.1)
     generated_date: '2026-09-13'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-13'
 - source: 4CH1-CON-ION
```

### 12. `4CH1-CON-MOLAR-ENTHALPY REQUIRES_PREREQUISITE 4CH1-CON-HEAT-CALC` [high]

- node 4CH1-CON-MOLAR-ENTHALPY — Molar enthalpy change (ΔH = Q/n) (CONCEPT)
-   spec 4CH1-3.4 [CORE]: calculate the molar enthalpy change ($\Delta H$) from the heat energy change, $ Q $
- node 4CH1-CON-HEAT-CALC — Heat energy change calculation (Q = mcΔT) (CONCEPT)
-   spec 4CH1-3.3 [CORE]: calculate the heat energy change from a measured temperature change using the expression $ Q=...
- derivation: EXPLICIT_TEACH_SEQUENCE — The note teaches the sequence explicitly: Q is calculated FIRST, then the per-gram/per-mole conversion — the 3.4 molar enthalpy is computed FROM the 3.3 heat energy change (ΔH = Q/n; the spec's own 3.3-then-3.4 order).
- `NOTE` Energetics calculations in chemistry - IGCSE Revision Notes.md — "In both cases, the energy released (Q) is calculated first"

```diff
@@ -5364,7 +5364,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-3.3/3.4 @ Energetics Calculations (2026-09-11)
     generated_date: '2026-09-13'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-13'
 - source: 4CH1-CON-MOLAR-ENTHALPY
```

### 13. `4CH1-CON-MOLAR-ENTHALPY REQUIRES_PREREQUISITE 4CH1-CON-MOLE` [high]

- node 4CH1-CON-MOLAR-ENTHALPY — Molar enthalpy change (ΔH = Q/n) (CONCEPT)
-   spec 4CH1-3.4 [CORE]: calculate the molar enthalpy change ($\Delta H$) from the heat energy change, $ Q $
- node 4CH1-CON-MOLE — The mole (unit of amount of substance) (CONCEPT)
-   spec 4CH1-1.27 [CORE]: know that the mole(mol) is the unit for the amount of a substance
- derivation: USED_WITHOUT_RETEACHING — CROSS-SECTION boundary edge (B4-E-04), sanctioned by the session-52 cross-slice boundary ruling ("molar enthalpy calculation (3.4) presupposes the mole (Q/n)"): the mole is the denominator operand of the molar enthalpy expression (OD-1 operand rule — the pilot's yield-triple operand class); the note's per-gram/per-mole comparison and the worked example's mol-to-mass machinery (mass = moles × Mr) use the mole without re-teaching it. No S1 identity is re-minted.
- `NOTE` Energetics calculations in chemistry - IGCSE Revision Notes.md — "We can compare the amount of energy released per gram and per mole for different fuels"
- `NOTE` Energetics calculations in chemistry - IGCSE Revision Notes.md — "The energy released per mole is also known as the molar enthalpy change"

```diff
@@ -5393,7 +5393,9 @@ edges:
       by the pilot record (4CH1-1.26); session-52 cross-slice boundary ruling sanctioned target
     generated_date: '2026-09-13'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-13'
 - source: 4CH1-CON-MOLAR-GAS-VOL
```

### 14. `4CH1-CON-RATE-FACTORS EXPLAINED_BY 4CH1-CON-COLLISION-THEORY` [high]

- node 4CH1-CON-RATE-FACTORS — Factors affecting the rate of reaction (surface area, concentration and pressure, temperature, catalyst) (CONCEPT)
-   spec 4CH1-3.10 [CORE]: describe the effects of changes in surface area of a solid, concentration of a solution, pres...
- node 4CH1-CON-COLLISION-THEORY — Collision-theory explanations of rate changes (frequency and success of collisions) (CONCEPT)
-   spec 4CH1-3.11 [CORE]: explain the effects of changes in surface area of a solid, concentration of a solution, press...
- derivation: SINGLE_SOURCE_CAUSAL_TEACHING — 3.11 is an explicit explain-demand and the note teaches each 3.10 factor effect with an explicit particle-collision cause (concentration/pressure: more particles per volume or same particles in a smaller volume; temperature: more kinetic energy; surface area: more exposed particles — each "causes more collisions per second, leading to more frequent and successful collisions"). The EXPLAINED_BY class per the batch-2/3 pattern (one relation per pair; no prereq edge on this pair — the factors are described before they are explained, but the dependency that matters is explanatory).
- `NOTE` Explaining Rates  Edexcel IGCSE Chemistry Revision Notes 2017.md — "We can use collision theory to explain why these factors influence the reaction rate"
- `NOTE` Explaining Rates  Edexcel IGCSE Chemistry Revision Notes 2017.md — "Increasing the concentration means that there are more reactant particles in a given volume"

```diff
@@ -6857,7 +6857,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-3.10/3.11 @ Explaining Rates (2026-09-11)
     generated_date: '2026-09-13'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-13'
 - source: 4CH1-CON-YIELD
```

### 15. `4CH1-CON-RATE-FACTORS REQUIRES_PREREQUISITE 4CH1-CON-CONCENTRATION` [high]

- node 4CH1-CON-RATE-FACTORS — Factors affecting the rate of reaction (surface area, concentration and pressure, temperature, catalyst) (CONCEPT)
-   spec 4CH1-3.10 [CORE]: describe the effects of changes in surface area of a solid, concentration of a solution, pres...
- node 4CH1-CON-CONCENTRATION — Concentration of a solution (CONCEPT)
-   spec 4CH1-1.34C [CORE]: understand how to carry out calculations involving amount of substance, volume and concentrat...
- derivation: USED_WITHOUT_RETEACHING — CROSS-SECTION boundary edge (B4-E-09), sanctioned by the session-52 cross-slice boundary ruling ("the concentration-rate factor (3.9-3.11) presupposes the concentration-of-solution concept"): the concentration factor is stated over the pilot's concentration-of-solution concept ("concentration of a solution", "more reactant particles in a given volume") without re-teaching it. No S1 identity is re-minted.
- `NOTE` Explaining Rates  Edexcel IGCSE Chemistry Revision Notes 2017.md — "Increasing the concentration of a solution increases the rate of reaction"
- `NOTE` Explaining Rates  Edexcel IGCSE Chemistry Revision Notes 2017.md — "Increasing the concentration means that there are more reactant particles in a given volume"

```diff
@@ -5805,7 +5805,9 @@ edges:
       by the pilot record (4CH1-1.35C); session-52 cross-slice boundary ruling sanctioned target
     generated_date: '2026-09-13'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-13'
 - source: 4CH1-CON-REACTING-MASS
```

### 16. `4CH1-CON-REACTION-PROFILE REQUIRES_PREREQUISITE 4CH1-CON-ACTIVATION-ENERGY` [high]

- node 4CH1-CON-REACTION-PROFILE — Reaction profile diagrams (showing ΔH and activation energy) (CONCEPT)
-   spec 4CH1-3.14C [CORE]: draw and explain reaction profile diagrams showing $\Delta H$ and activation energy
- node 4CH1-CON-ACTIVATION-ENERGY — Activation energy (minimum energy for reaction; Ea) (CONCEPT)
-   spec 4CH1-3.14C [CORE]: draw and explain reaction profile diagrams showing $\Delta H$ and activation energy
- derivation: DEFINITIONAL_DEPENDENCY — The profile's defining feature IS the activation energy (the initial rise to the peak of the curve) plus the ΔH difference — drawing and labelling a 3.14C profile presupposes the Ea concept the peak represents. Companion to the profile -> level-diagram edge (different claims: the representation lineage vs the quantity displayed).
- `NOTE` What is activation energy- IGCSE Revision Notes.md — "The initial increase in energy, from the reactants to the peak of the curve, represents the activation energy"

```diff
@@ -5897,7 +5897,9 @@ edges:
       by this record (4CH1-3.14C)
     generated_date: '2026-09-13'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-13'
 - source: 4CH1-CON-REACTION-PROFILE
```

### 17. `4CH1-CON-REACTION-PROFILE REQUIRES_PREREQUISITE 4CH1-CON-ENERGY-LEVEL-DIAGRAM` [high]

- node 4CH1-CON-REACTION-PROFILE — Reaction profile diagrams (showing ΔH and activation energy) (CONCEPT)
-   spec 4CH1-3.14C [CORE]: draw and explain reaction profile diagrams showing $\Delta H$ and activation energy
- node 4CH1-CON-ENERGY-LEVEL-DIAGRAM — Energy level diagrams for exothermic and endothermic reactions (CONCEPT)
-   spec 4CH1-3.5C [CORE]: draw and explain energy level diagrams to represent exothermic and endothermic reactions
- derivation: USED_WITHOUT_RETEACHING — The corpus itself states the dependency: profiles are "similar to energy level diagrams seen in a previous topic, but in addition... they also show how the energy changes as the reaction progresses" — the 3.14C representation extends the 3.5C one and presupposes its reading (levels, axes, the ΔH arrow).
- `NOTE` What is activation energy- IGCSE Revision Notes.md — "Reaction profiles are similar to energy level diagrams seen in a previous topic"

```diff
@@ -5921,7 +5921,9 @@ edges:
       by this record (4CH1-3.5C)
     generated_date: '2026-09-13'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-13'
 - source: 4CH1-CON-REVERSIBLE
```

### 18. `4CH1-CON-REVERSIBLE REQUIRES_PREREQUISITE 4CH1-CON-EQ-SYMBOL` [high]

- node 4CH1-CON-REVERSIBLE — Reversible reactions and the ⇌ notation (CONCEPT)
-   spec 4CH1-3.17 [CORE]: know that some reactions are reversible and this is indicated by the symbol $\rightleftharpoo...
- node 4CH1-CON-EQ-SYMBOL — Balanced symbol (chemical) equation (CONCEPT)
-   spec 4CH1-1.25 [CORE]: write word equations and balanced chemical equations(including state symbols):for reactions s...
- derivation: USED_WITHOUT_RETEACHING — CROSS-SECTION boundary edge (B4-E-19), sanctioned by the session-52 cross-slice boundary ruling ("reversible-reaction notation (3.17, the ⇌ symbol) presupposes balanced symbol equations"): the 3.17 demand is the reversible notation "in equations" — a variation on the pilot's symbol-equation skill, used without re-teaching equation-writing or balancing. No S1 identity is re-minted.
- `NOTE` Reversible reactions - IGCSE Chemistry Revision Notes.md — "When writing chemical equations for reversible reactions, two opposing arrows are used to indicate the forw..."

```diff
@@ -5947,7 +5947,9 @@ edges:
       the pilot record (4CH1-1.18); session-52 cross-slice boundary ruling sanctioned target
     generated_date: '2026-09-13'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-13'
 - source: 4CH1-CON-REVERSIBLE-EXAMPLES
```

### 19. `4CH1-CON-REVERSIBLE-EXAMPLES REQUIRES_PREREQUISITE 4CH1-CON-REVERSIBLE` [high]

- node 4CH1-CON-REVERSIBLE-EXAMPLES — Named reversible reactions (ammonium chloride; hydrated copper(II) sulfate) (CONCEPT)
-   spec 4CH1-3.18 [CORE]: describe reversible reactions such as the dehydration of hydrated copper(II) sulfate and the ...
- node 4CH1-CON-REVERSIBLE — Reversible reactions and the ⇌ notation (CONCEPT)
-   spec 4CH1-3.17 [CORE]: know that some reactions are reversible and this is indicated by the symbol $\rightleftharpoo...
- derivation: USED_WITHOUT_RETEACHING — The 3.18 examples are presented as instances OF reversible reactions (the note re-uses the 3.17 concept and its ⇌ notation to write both named equations); the spec's own order is know-reversible (3.17) then describe-examples (3.18).
- `NOTE` Reversible reactions - IGCSE Chemistry Revision Notes.md — "Reversible reactions can be seen in some hydrated salts"
- `NOTE` Reversible reactions - IGCSE Chemistry Revision Notes.md — "Heating ammonium chloride produces ammonia and hydrogen chloride gases"

```diff
@@ -5973,7 +5973,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-3.17/3.18 @ Reversible Reactions (2026-09-11)
     generated_date: '2026-09-13'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-13'
 - source: 4CH1-CON-REVERSIBLE-EXAMPLES
```

### 20. `4CH1-CON-REVERSIBLE-EXAMPLES REQUIRES_PREREQUISITE 4CH1-CON-WATER-CRYST` [high]

- node 4CH1-CON-REVERSIBLE-EXAMPLES — Named reversible reactions (ammonium chloride; hydrated copper(II) sulfate) (CONCEPT)
-   spec 4CH1-3.18 [CORE]: describe reversible reactions such as the dehydration of hydrated copper(II) sulfate and the ...
- node 4CH1-CON-WATER-CRYST — Water of crystallisation and hydrated salts (CONCEPT)
-   spec 4CH1-1.31 [CORE]: understand how the formulae of simple compounds can be obtained experimentally, including met...
- derivation: USED_WITHOUT_RETEACHING — CROSS-SECTION boundary edge (B4-E-18), sanctioned by the session-52 cross-slice boundary ruling ("the 3.18 dehydration-of-hydrated-copper(II)-sulfate example presupposes water of crystallisation (the pilot node owns the term; 3.18 owns the reversible behaviour, NOT the hydration term)"): the example uses the water-of-crystallisation and hydrated/anhydrous-salt concepts without re-teaching them. No S1 identity is re-minted; 3.18 owns the reversible behaviour.
- `NOTE` Reversible reactions - IGCSE Chemistry Revision Notes.md — "These are salts that contain water of crystallisation which affects their shape and colour"
- `NOTE` Reversible reactions - IGCSE Chemistry Revision Notes.md — "The hydrated salt can be heated / dehydrated to form anhydrous copper(II) sulfate"

```diff
@@ -6003,7 +6003,9 @@ edges:
       target
     generated_date: '2026-09-13'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-13'
 - source: 4CH1-CON-RF-VALUE
```

### 21. `4CH1-MIS-BOND-ENERGY-COUNT REMEDIATED_BY 4CH1-CON-BOND-ENERGY-CALC` [high]

- node 4CH1-MIS-BOND-ENERGY-COUNT — Counting the wrong number or type of bonds in bond-energy calculations (ignoring balancing numbers) (MISCONCEPTION)
- node 4CH1-CON-BOND-ENERGY-CALC — Bond energy calculations (enthalpy change from bond energies) (CONCEPT)
-   spec 4CH1-3.7C [CORE]: use bond energies to calculate the enthalpy change during a chemical reaction
- derivation: EXAMINER_TIP_EXPLICIT — Remediation target = the misconception target (the B1-E-25 pattern): the corrective content IS the note's Examiner Tips and Tricks strategy — write the displayed-formula equation first, then identify the type and number of bonds, counting the balancing numbers.
- `NOTE` What is bond energy - IGCSE Chemistry Revision Notes.md — "For bond energy questions, it is helpful to write down a displayed formula equation for the reaction before..."
- `NOTE` What is bond energy - IGCSE Chemistry Revision Notes.md — "Don't forget to take into account the balancing numbers when working out how many of each type of bond is b..."

```diff
@@ -7381,7 +7381,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-3.7C @ What is Bond Energy (2026-09-11)
     generated_date: '2026-09-13'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-13'
 - source: 4CH1-MIS-CATALYST-PARTICLE-ENERGY
```

### 22. `4CH1-MIS-BOND-ENERGY-COUNT WRONG_ANSWER_PATTERN 4CH1-CON-BOND-ENERGY-CALC` [medium]

- node 4CH1-MIS-BOND-ENERGY-COUNT — Counting the wrong number or type of bonds in bond-energy calculations (ignoring balancing numbers) (MISCONCEPTION)
- node 4CH1-CON-BOND-ENERGY-CALC — Bond energy calculations (enthalpy change from bond energies) (CONCEPT)
-   spec 4CH1-3.7C [CORE]: use bond energies to calculate the enthalpy change during a chemical reaction
- derivation: ASSESSMENT_DOCUMENTED — The wrong answer manifests in bond-energy question contexts (the pinned ENERGETICS Paper-2 MS deducts a mark per mistake in the bond-sum expressions "(4 × C-H) + (2 × O=O)" / "(2 × C=O) + (4 × H-O)"; the examiner tip names the mistake class — balancing numbers ignored in the bond count) — the pattern corrupts the 3.7C bond-sum held by CON-BOND-ENERGY-CALC.
- `MARK_SCHEME` ENERGETICS_MS_P2.txt — "Deduct 1 mark for each mistake"
- `NOTE` What is bond energy - IGCSE Chemistry Revision Notes.md — "Don't forget to take into account the balancing numbers when working out how many of each type of bond is b..."

```diff
@@ -7064,7 +7064,9 @@ edges:
       0288d7d15006); T-C10 HUMAN_VALIDATED 4CH1-3.7C @ What is Bond Energy (2026-09-11)
     generated_date: '2026-09-13'
   confidence: medium
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-13'
 - source: 4CH1-MIS-CATALYST-PARTICLE-ENERGY
```

### 23. `4CH1-MIS-CATALYST-PARTICLE-ENERGY REMEDIATED_BY 4CH1-CON-CATALYST` [high]

- node 4CH1-MIS-CATALYST-PARTICLE-ENERGY — Explaining a catalyst's effect as particles gaining energy or moving more quickly (MISCONCEPTION)
- node 4CH1-CON-CATALYST — Catalysts (increase rate, chemically unchanged; alternative pathway at lower activation energy) (CONCEPT)
-   spec 4CH1-3.12 [CORE]: know that a catalyst is a substance that increases the rate of a reaction, but is chemically ...
-   spec 4CH1-3.13 [CORE]: know that a catalyst works by providing an alternative pathway with lower activation energy
- derivation: ASSESSMENT_DOCUMENTED — Remediation target = the misconception target (the B1-E-25/batch-2/batch-3 pattern): the corrective content IS the alternative-pathway/lower-activation-energy mechanism statement (plus the activation-energy note's catalyst paragraph quoted in the node's remediation_evidence).
- `NOTE` Catalysts in Chemistry - IGCSE Chemistry Revision Notes.md — "They provide an alternative pathway for the reaction to occur"
- `NOTE` Catalysts in Chemistry - IGCSE Chemistry Revision Notes.md — "The alternative pathway has a lower activation energy"

```diff
@@ -7407,7 +7407,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-3.12/3.13 @ Catalysts in Chemistry (2026-09-11)
     generated_date: '2026-09-13'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-13'
 - source: 4CH1-MIS-CONC-UNIT
```

### 24. `4CH1-MIS-CATALYST-PARTICLE-ENERGY WRONG_ANSWER_PATTERN 4CH1-CON-CATALYST` [high]

- node 4CH1-MIS-CATALYST-PARTICLE-ENERGY — Explaining a catalyst's effect as particles gaining energy or moving more quickly (MISCONCEPTION)
- node 4CH1-CON-CATALYST — Catalysts (increase rate, chemically unchanged; alternative pathway at lower activation energy) (CONCEPT)
-   spec 4CH1-3.12 [CORE]: know that a catalyst is a substance that increases the rate of a reaction, but is chemically ...
-   spec 4CH1-3.13 [CORE]: know that a catalyst works by providing an alternative pathway with lower activation energy
- derivation: ASSESSMENT_DOCUMENTED — The wrong answer manifests in catalyst-mechanism question contexts (both pinned S3 Paper-2 MS cap the answer at 1 mark when it references particles gaining energy or moving more quickly) — the pattern corrupts the 3.13 mechanism held by CON-CATALYST.
- `MARK_SCHEME` RATES_MS_P2.txt — "MAX 1 if any reference to particles gaining energy or moving more quickly"
- `MARK_SCHEME` RRE_MS_P2.txt — "MAX 1 if any reference to particles gaining energy or moving more quickly"

```diff
@@ -7089,7 +7089,9 @@ edges:
       RATES_MS_P2.txt sha1 97876cf4ffe7 + RRE_MS_P2.txt sha1 7d50fc44586b)
     generated_date: '2026-09-13'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-13'
 - source: 4CH1-MIS-CONC-UNIT
```

### 25. `4CH1-MIS-ENTHALPY-UNIT-J REMEDIATED_BY 4CH1-CON-MOLAR-ENTHALPY` [high]

- node 4CH1-MIS-ENTHALPY-UNIT-J — Quoting the molar enthalpy change as the unconverted joule value (e.g. 50 000) instead of kilojoules (MISCONCEPTION)
- node 4CH1-CON-MOLAR-ENTHALPY — Molar enthalpy change (ΔH = Q/n) (CONCEPT)
-   spec 4CH1-3.4 [CORE]: calculate the molar enthalpy change ($\Delta H$) from the heat energy change, $ Q $
- derivation: ASSESSMENT_DOCUMENTED — Remediation target = the misconception target (the B1-E-25 pattern): the corrective content IS the explicit J-to-kJ conversion step and the kJ/mol units statement of the molar-enthalpy section.
- `NOTE` Energetics calculations in chemistry - IGCSE Revision Notes.md — "Convert from J to kJ (divide by 1000)"
- `NOTE` Energetics calculations in chemistry - IGCSE Revision Notes.md — "The units are kJ / mol"

```diff
@@ -7505,7 +7505,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-3.4 @ Energetics Calculations in Chemistry (2026-09-11)
     generated_date: '2026-09-13'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-13'
 - source: 4CH1-MIS-EQ-PRESSURE-FEWER
```

### 26. `4CH1-MIS-ENTHALPY-UNIT-J WRONG_ANSWER_PATTERN 4CH1-CON-MOLAR-ENTHALPY` [high]

- node 4CH1-MIS-ENTHALPY-UNIT-J — Quoting the molar enthalpy change as the unconverted joule value (e.g. 50 000) instead of kilojoules (MISCONCEPTION)
- node 4CH1-CON-MOLAR-ENTHALPY — Molar enthalpy change (ΔH = Q/n) (CONCEPT)
-   spec 4CH1-3.4 [CORE]: calculate the molar enthalpy change ($\Delta H$) from the heat energy change, $ Q $
- derivation: ASSESSMENT_DOCUMENTED — The wrong answer manifests in molar-enthalpy question contexts (the pinned ENERGETICS Paper-2 MS awards 1/2 for the unconverted 50 000 answer, full credit only with J/mol units on the line) — the pattern corrupts the 3.4 unit conversion held by CON-MOLAR-ENTHALPY.
- `MARK_SCHEME` ENERGETICS_MS_P2.txt — "Award 1 mark for 50 000"
- `MARK_SCHEME` ENERGETICS_MS_P2.txt — "Award 2 marks for 50 000 if units changed to J/mol on answer line"

```diff
@@ -7186,7 +7186,9 @@ edges:
       0288d7d15006)
     generated_date: '2026-09-13'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-13'
 - source: 4CH1-MIS-EQ-PRESSURE-FEWER
```

### 27. `4CH1-MIS-EQ-PRESSURE-FEWER REMEDIATED_BY 4CH1-CON-EQ-POSITION` [high]

- node 4CH1-MIS-EQ-PRESSURE-FEWER — Predicting that a pressure change shifts equilibrium to the side with fewer gas molecules in the wrong direction (MISCONCEPTION)
- node 4CH1-CON-EQ-POSITION — Position of equilibrium (temperature and pressure effects; catalyst does not affect it) (CONCEPT)
-   spec 4CH1-3.21C [CORE]: understand why a catalyst does not affect the position of equilibrium in a reversible reaction
-   spec 4CH1-3.22C [CORE]: know the effect of changing either temperature or pressure on the position of equilibrium in ...
- derivation: ASSESSMENT_DOCUMENTED — Remediation target = the misconception target (the B1-E-25 pattern): the corrective content IS the both-directions molecule-count rule (increase -> fewest molecules; decrease -> most molecules; no effect when the counts are equal — the note's Pressure section).
- `NOTE` The position of equilibrium - IGCSE Chemistry Revision Notes.md — "An increase in pressure will favour the reaction that produces the least number of molecules"
- `NOTE` The position of equilibrium - IGCSE Chemistry Revision Notes.md — "A decrease in pressure will favour the reaction that produces the greatest number of molecules"

```diff
@@ -7531,7 +7531,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-3.22C @ The Position of Equilibrium (2026-09-11)
     generated_date: '2026-09-13'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-13'
 - source: 4CH1-MIS-EQ-SUBSCRIPT
```

### 28. `4CH1-MIS-EQ-PRESSURE-FEWER WRONG_ANSWER_PATTERN 4CH1-CON-EQ-POSITION` [medium]

- node 4CH1-MIS-EQ-PRESSURE-FEWER — Predicting that a pressure change shifts equilibrium to the side with fewer gas molecules in the wrong direction (MISCONCEPTION)
- node 4CH1-CON-EQ-POSITION — Position of equilibrium (temperature and pressure effects; catalyst does not affect it) (CONCEPT)
-   spec 4CH1-3.21C [CORE]: understand why a catalyst does not affect the position of equilibrium in a reversible reaction
-   spec 4CH1-3.22C [CORE]: know the effect of changing either temperature or pressure on the position of equilibrium in ...
- derivation: ASSESSMENT_DOCUMENTED — The wrong answer manifests in equilibrium-shift question contexts (the pinned RRE Paper-2 MS rejects "shifts to the side with fewer (gas) moles/molecules" on the pressure question) — the pattern reverses the molecule-count direction of the 3.22C pressure rule held by CON-EQ-POSITION. Layout caveat: the pdftotext column scrambling makes the reject attribution antonym-based (recorded in the node derivation_notes) — hence medium confidence on this row.
- `MARK_SCHEME` RRE_MS_P2.txt — "shifts to the side with fewer (gas) moles/molecules"

```diff
@@ -7210,7 +7210,9 @@ edges:
       sha1 7d50fc44586b)
     generated_date: '2026-09-13'
   confidence: medium
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-13'
 - source: 4CH1-MIS-EQ-TEMP-EXO
```

### 29. `4CH1-MIS-EQ-TEMP-EXO REMEDIATED_BY 4CH1-CON-EQ-POSITION` [high]

- node 4CH1-MIS-EQ-TEMP-EXO — Predicting that raising the temperature shifts equilibrium in the exothermic direction (MISCONCEPTION)
- node 4CH1-CON-EQ-POSITION — Position of equilibrium (temperature and pressure effects; catalyst does not affect it) (CONCEPT)
-   spec 4CH1-3.21C [CORE]: understand why a catalyst does not affect the position of equilibrium in a reversible reaction
-   spec 4CH1-3.22C [CORE]: know the effect of changing either temperature or pressure on the position of equilibrium in ...
- derivation: ASSESSMENT_DOCUMENTED — Remediation target = the misconception target (the B1-E-25 pattern): the corrective content IS the endothermic-direction rule for a temperature increase (the note's Temperature section; the MS Accept entry is the same statement in assessment form).
- `NOTE` The position of equilibrium - IGCSE Chemistry Revision Notes.md — "The equilibrium will shift in the direction of the endothermic reaction"

```diff
@@ -7576,7 +7576,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-3.22C @ The Position of Equilibrium (2026-09-11)
     generated_date: '2026-09-13'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-13'
 - source: 4CH1-MIS-GAS-PARTICLES-TOUCH
```

### 30. `4CH1-MIS-EQ-TEMP-EXO WRONG_ANSWER_PATTERN 4CH1-CON-EQ-POSITION` [high]

- node 4CH1-MIS-EQ-TEMP-EXO — Predicting that raising the temperature shifts equilibrium in the exothermic direction (MISCONCEPTION)
- node 4CH1-CON-EQ-POSITION — Position of equilibrium (temperature and pressure effects; catalyst does not affect it) (CONCEPT)
-   spec 4CH1-3.21C [CORE]: understand why a catalyst does not affect the position of equilibrium in a reversible reaction
-   spec 4CH1-3.22C [CORE]: know the effect of changing either temperature or pressure on the position of equilibrium in ...
- derivation: ASSESSMENT_DOCUMENTED — The wrong answer manifests in equilibrium-shift question contexts (the pinned RRE Paper-2 MS rejects "moves in the exothermic direction" on the temperature question — its Accept column takes the antonym) — the pattern corrupts the 3.22C temperature rule held by CON-EQ-POSITION.
- `MARK_SCHEME` RRE_MS_P2.txt — "moves in the exothermic direction"

```diff
@@ -7232,7 +7232,9 @@ edges:
       sha1 7d50fc44586b)
     generated_date: '2026-09-13'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-13'
 - source: 4CH1-MIS-GAS-PARTICLES-TOUCH
```

### 31. `4CH1-PR-09 REQUIRES_PREREQUISITE 4CH1-CON-CALORIMETRY` [high]

- node 4CH1-CON-CALORIMETRY — Simple calorimetry experiments (reactions in solution and combustion) (CONCEPT)
-   spec 4CH1-3.2 [CORE]: describe simple calorimetry experiments for reactions such as combustion, displacement, disso...
- derivation: USED_WITHOUT_RETEACHING — Practical edge (the PR-01/PR-02/PR-03/PR-04 pattern: the practical's Aim sentence names the target concept): the 3.8 practical IS a calorimetry study (styrofoam calorimeter + lid, thermometer, stirrer) — the 3.2 method deployed as the named practical.
- `NOTE` Temperature change practical - IGCSE Revision Notes.md — "To perform a calorimetry study of the reaction between HCl and NaOH"

```diff
@@ -6521,7 +6521,9 @@ edges:
       owned by this record (4CH1-3.2)
     generated_date: '2026-09-13'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-13'
 - source: 4CH1-PR-10
```

### 32. `4CH1-PR-10 REQUIRES_PREREQUISITE 4CH1-CON-RATE-EXPERIMENTS` [high]

- node 4CH1-CON-RATE-EXPERIMENTS — Rate-of-reaction experiments (gas collection, disappearing cross, timing methods) (CONCEPT)
-   spec 4CH1-3.9 [CORE]: describe experiments to investigate the effects of changes in surface area of a solid, concen...
- derivation: USED_WITHOUT_RETEACHING — Practical edge (the PR-02 -> CHROMATOGRAPHY pattern): the 3.15 practical deploys the 3.9 fixed-time gas-collection family (conical flask + delivery tube + inverted measuring cylinder, gas volume in a fixed time) — the aim and method are the 3.9 experiment family applied to marble chips.
- `NOTE` How surface area affects rate - IGCSE Revision Notes.md — "Investigating the effect of different size marble chips on the rate of reaction between calcium carbonate a..."

```diff
@@ -6546,7 +6546,9 @@ edges:
       owned by this record (4CH1-3.9)
     generated_date: '2026-09-13'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-13'
 - source: 4CH1-PR-10
```

### 33. `4CH1-PR-10 REQUIRES_PREREQUISITE 4CH1-CON-RATE-FACTORS` [high]

- node 4CH1-CON-RATE-FACTORS — Factors affecting the rate of reaction (surface area, concentration and pressure, temperature, catalyst) (CONCEPT)
-   spec 4CH1-3.10 [CORE]: describe the effects of changes in surface area of a solid, concentration of a solution, pres...
- derivation: USED_WITHOUT_RETEACHING — Practical edge (the PR-02 -> RF-VALUE pattern: the practical's conclusion states the factor rule it investigates): the 3.15 practical's conclusion is the surface-area factor rule — the 3.10 effects are the practical's explanatory frame, used without re-teaching.
- `NOTE` How surface area affects rate - IGCSE Revision Notes.md — "Increasing the surface area of the marble chip, increases the rate of reaction"

```diff
@@ -6569,7 +6569,9 @@ edges:
       owned by this record (4CH1-3.10)
     generated_date: '2026-09-13'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-13'
 - source: 4CH1-PR-11
```

### 34. `4CH1-PR-11 REQUIRES_PREREQUISITE 4CH1-CON-CATALYST` [high]

- node 4CH1-CON-CATALYST — Catalysts (increase rate, chemically unchanged; alternative pathway at lower activation energy) (CONCEPT)
-   spec 4CH1-3.12 [CORE]: know that a catalyst is a substance that increases the rate of a reaction, but is chemically ...
-   spec 4CH1-3.13 [CORE]: know that a catalyst works by providing an alternative pathway with lower activation energy
- derivation: USED_WITHOUT_RETEACHING — Practical edge (the PR-04 -> ELECTROLYSIS pattern): the 3.16 practical's independent variable IS the catalyst (different solids — MnO2, PbO, Fe2O3, CuO — on the catalytic decomposition); the 3.12/3.13 concept is the practical's subject, used without re-teaching.
- `NOTE` Investigating catalysts - IGCSE Chemistry Revision Notes.md — "To investigate the effect of different solids on the catalytic decomposition of hydrogen peroxide"
- `NOTE` Investigating catalysts - IGCSE Chemistry Revision Notes.md — "Repeat experiment with different catalysts and compare results"

```diff
@@ -6596,7 +6596,9 @@ edges:
       by this record (4CH1-3.12/3.13)
     generated_date: '2026-09-13'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-13'
 - source: 4CH1-PR-11
```

### 35. `4CH1-PR-11 REQUIRES_PREREQUISITE 4CH1-CON-RATE-EXPERIMENTS` [high]

- node 4CH1-CON-RATE-EXPERIMENTS — Rate-of-reaction experiments (gas collection, disappearing cross, timing methods) (CONCEPT)
-   spec 4CH1-3.9 [CORE]: describe experiments to investigate the effects of changes in surface area of a solid, concen...
- derivation: USED_WITHOUT_RETEACHING — Practical edge (the PR-02 pattern): the 3.16 practical deploys the same 3.9 fixed-time gas-collection family (delivery tube to an inverted measuring cylinder in a water trough, gas volume in a fixed time) for the catalyst comparison.
- `NOTE` Investigating catalysts - IGCSE Chemistry Revision Notes.md — "Use a delivery tube to connect this flask to a measuring cylinder upside down in water trough"

```diff
@@ -6619,7 +6619,9 @@ edges:
       by this record (4CH1-3.9)
     generated_date: '2026-09-13'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-13'
 - source: 4CH1-CON-CRYSTALLISATION
```

## File-level meta hunks (once, for the whole batch)

```diff
@@ -140,8 +140,10 @@ meta:
     remediated_by_edges: 15
     requires_prerequisite_edges: 115
     wrong_answer_pattern_edges: 13
-    promoted_edges: 118
-    human_validated_edges: 118
+    promoted_edges: 153
+    human_validated_edges: 153
   promotion_record: scripts/c11_promotions.yaml
 edges:
 - source: 4CH1-CON-ACTIVATION-ENERGY
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
| `4CH1-CON-ACTIVATION-ENERGY` | Activation energy (minimum energy for reaction; Ea) | CONCEPT | 4CH1-3.14C (CORE) | high |
| `4CH1-CON-ANODE-CATHODE` | Anions and cations (negative and positive ions) and their migration to cathode and anode | CONCEPT | 4CH1-1.57C (CORE) | high |
| `4CH1-CON-AQUEOUS-DISCHARGE` | Selective discharge in aqueous electrolysis (halide preference at the anode; hydrogen vs metal at the cathode) | CONCEPT | 4CH1-1.58C (CORE) | high |
| `4CH1-CON-AR` | Relative atomic mass (Ar) | CONCEPT | 4CH1-1.26 (CORE); 4CH1-1.28 (CORE) | high |
| `4CH1-CON-ATOM` | Atom (definition and subatomic composition) | CONCEPT | 4CH1-1.14 (CORE) | high |
| `4CH1-CON-ATOMIC-NUMBER` | Atomic number | CONCEPT | 4CH1-1.16 (CORE) | high |
| `4CH1-CON-AVOGADRO-CONST` | Avogadro constant | CONCEPT | 4CH1-1.27 (ENRICHMENT) | high |
| `4CH1-CON-AVOGADRO-LAW` | Avogadro's Law | CONCEPT | 4CH1-1.35C (ENRICHMENT) | high |
| `4CH1-CON-BOND-BREAKING-MAKING` | Bond-breaking endothermic, bond-making exothermic | CONCEPT | 4CH1-3.6C (CORE) | high |
| `4CH1-CON-BOND-ENERGY-CALC` | Bond energy calculations (enthalpy change from bond energies) | CONCEPT | 4CH1-3.7C (CORE) | high |
| `4CH1-CON-CALORIMETRY` | Simple calorimetry experiments (reactions in solution and combustion) | CONCEPT | 4CH1-3.2 (CORE) | high |
| `4CH1-CON-CATALYST` | Catalysts (increase rate, chemically unchanged; alternative pathway at lower activation energy) | CONCEPT | 4CH1-3.12 (CORE); 4CH1-3.13 (CORE) | high |
| `4CH1-CON-CHROMATOGRAM-INTERPRETATION` | Interpreting chromatograms | CONCEPT | 4CH1-1.11 (CORE) | high |
| `4CH1-CON-CHROMATOGRAPHY` | Paper chromatography (separation by differential solubility) | CONCEPT | 4CH1-1.10 (CORE) | high |
| `4CH1-CON-COLLISION-THEORY` | Collision-theory explanations of rate changes (frequency and success of collisions) | CONCEPT | 4CH1-3.11 (CORE) | high |
| `4CH1-CON-COMPOUND` | Compound | CONCEPT | 4CH1-1.8 (CORE) | high |
| `4CH1-CON-CONC-CALC` | Concentration calculation (mol/dm3) | CONCEPT | 4CH1-1.34C (CORE) | high |
| `4CH1-CON-CONCENTRATION` | Concentration of a solution | CONCEPT | 4CH1-1.34C (CORE) | high |
| `4CH1-CON-CONSERVATION-MASS` | Law of Conservation of Mass | CONCEPT | 4CH1-1.25 (CORE); 4CH1-1.26 (SUPPORTING) | high |
| `4CH1-CON-COVALENT-BOND` | Covalent bond (shared pair of electrons; electrostatic attraction between the shared pair and the nuclei) | CONCEPT | 4CH1-1.44 (CORE); 4CH1-1.45 (CORE) | high |
| `4CH1-CON-COVALENT-CONDUCTION` | Covalent compounds do not conduct electricity (no freely moving charged particles) | CONCEPT | 4CH1-1.51 (CORE); 4CH1-1.55C (CORE) | high |
| `4CH1-CON-CRYSTALLISATION` | Crystallisation | CONCEPT | 4CH1-1.10 (CORE) | high |
| `4CH1-CON-DIAMOND-GRAPHITE` | Structures and properties of diamond, graphite and C60 fullerene (allotropes of carbon) | CONCEPT | 4CH1-1.50 (CORE) | high |
| `4CH1-CON-DIFFUSION` | Diffusion in gases and liquids | CONCEPT | 4CH1-1.3 (CORE) | high |
| `4CH1-CON-DILUTION` | Dilution of coloured solutions | CONCEPT | 4CH1-1.3 (CORE) | high |
| `4CH1-CON-DOT-CROSS-COVALENT` | Dot-and-cross diagrams for covalent substances (diatomic, inorganic and organic molecules) | CONCEPT | 4CH1-1.46 (CORE) | high |
| `4CH1-CON-DOT-CROSS-IONIC` | Dot-and-cross diagrams for ionic compounds (electron transfer) | CONCEPT | 4CH1-1.40 (CORE) | high |
| `4CH1-CON-DYNAMIC-EQUILIBRIUM` | Dynamic equilibrium (sealed container; equal forward and reverse rates; constant concentrations) | CONCEPT | 4CH1-3.19C (CORE); 4CH1-3.20C (CORE) | high |
| `4CH1-CON-ELECTRODE-HALF-EQUATIONS` | Ionic half-equations for the electrode reactions during electrolysis | CONCEPT | 4CH1-1.59C (CORE) | high |
| `4CH1-CON-ELECTROLYSIS` | Electrolysis (decomposition by direct current: molten binary compounds and their element products, using inert electrodes) | CONCEPT | 4CH1-1.58C (CORE) | high |
| `4CH1-CON-ELECTRONIC-CONFIGURATION` | Electronic configuration of the first 20 elements (shells 2, 8, 8; configuration and Periodic Table position) | CONCEPT | 4CH1-1.19 (CORE); 4CH1-1.22 (CORE) | high |
| `4CH1-CON-ELEMENT` | Element | CONCEPT | 4CH1-1.8 (CORE) | high |
| `4CH1-CON-EMP-MOL-CALC` | Empirical and molecular formula calculation | CONCEPT | 4CH1-1.33 (CORE) | high |
| `4CH1-CON-EMPIRICAL-FORMULA` | Empirical formula | CONCEPT | 4CH1-1.32 (CORE); 4CH1-1.33 (CORE) | high |
| `4CH1-CON-ENERGY-LEVEL-DIAGRAM` | Energy level diagrams for exothermic and endothermic reactions | CONCEPT | 4CH1-3.5C (CORE) | high |
| `4CH1-CON-EQ-POSITION` | Position of equilibrium (temperature and pressure effects; catalyst does not affect it) | CONCEPT | 4CH1-3.21C (CORE); 4CH1-3.22C (CORE) | high |
| `4CH1-CON-EQ-STATE-SYM` | State symbols (s), (l), (g), (aq) | CONCEPT | 4CH1-1.25 (CORE) | high |
| `4CH1-CON-EQ-SYMBOL` | Balanced symbol (chemical) equation | CONCEPT | 4CH1-1.25 (CORE) | high |
| `4CH1-CON-EQ-WORD` | Word equation | CONCEPT | 4CH1-1.25 (CORE) | high |
| `4CH1-CON-EVAPORATION-BOILING` | Evaporation and its distinction from boiling | CONCEPT | 4CH1-1.2 (ENRICHMENT) | high |
| `4CH1-CON-EXO-ENDO` | Exothermic and endothermic reactions (heat energy given out or taken in) | CONCEPT | 4CH1-3.1 (CORE) | high |
| `4CH1-CON-EXP-FORMULA-DEDUCTION` | Experimental formula deduction (mass-difference method) | CONCEPT | 4CH1-1.31 (CORE); 4CH1-1.36 (CORE) | high |
| `4CH1-CON-FILTRATION` | Filtration | CONCEPT | 4CH1-1.10 (CORE) | high |
| `4CH1-CON-FRACTIONAL-DISTILLATION` | Fractional distillation | CONCEPT | 4CH1-1.10 (CORE) | high |
| `4CH1-CON-GAS-VOL-CALC` | Gas volume calculation | CONCEPT | 4CH1-1.35C (CORE) | high |
| `4CH1-CON-GIANT-COVALENT` | Giant covalent structures (solids with high melting and boiling points) | CONCEPT | 4CH1-1.49 (CORE) | high |
| `4CH1-CON-GROUP-SIMILARITY` | Why elements in the same group have similar chemical properties | CONCEPT | 4CH1-1.23 (CORE) | high |
| `4CH1-CON-HEAT-CALC` | Heat energy change calculation (Q = mcΔT) | CONCEPT | 4CH1-3.3 (CORE) | high |
| `4CH1-CON-HEATING-CONSTANT-MASS` | Heating to constant mass | CONCEPT | 4CH1-1.7C (ENRICHMENT) | high |
| `4CH1-CON-ION` | Ion (formation by electron loss or gain) | CONCEPT | 4CH1-1.37 (CORE) | high |
| `4CH1-CON-ION-CHARGE-RULES` | Common ion charges (group-based and named-ion table, with the deduction rule) | CONCEPT | 4CH1-1.38 (CORE) | high |
| `4CH1-CON-IONIC-BOND` | Ionic bonding (electrostatic attraction between oppositely charged ions) | CONCEPT | 4CH1-1.41 (CORE) | high |
| `4CH1-CON-IONIC-CONDUCTION` | Ionic conduction (solid insulator; molten and aqueous conductor via mobile ions) | CONCEPT | 4CH1-1.43 (CORE); 4CH1-1.56C (CORE) | high |
| `4CH1-CON-IONIC-FORMULA` | Writing formulae for ionic compounds (charge cancellation and swap-and-drop) | CONCEPT | 4CH1-1.39 (CORE) | high |
| `4CH1-CON-IONIC-LATTICE` | Giant ionic lattice and why ionic compounds have high melting and boiling points | CONCEPT | 4CH1-1.42 (CORE) | high |
| `4CH1-CON-ISOTOPES` | Isotopes and relative atomic mass from isotopic abundances | CONCEPT | 4CH1-1.16 (CORE); 4CH1-1.17 (CORE) | high |
| `4CH1-CON-MASS-NUMBER` | Mass number | CONCEPT | 4CH1-1.16 (CORE) | high |
| `4CH1-CON-METAL-NONMETAL` | Classifying elements as metals or non-metals (by properties and by Periodic Table position) | CONCEPT | 4CH1-1.20 (CORE); 4CH1-1.21 (CORE) | high |
| `4CH1-CON-METAL-PROPERTIES` | Typical physical properties of metals (electrical conductivity and malleability) and their explanations | CONCEPT | 4CH1-1.54C (CORE) | high |
| `4CH1-CON-METALLIC-BOND` | Metallic bonding (positive metal ions and delocalised electrons; the 2-D metallic lattice representation) | CONCEPT | 4CH1-1.52C (CORE); 4CH1-1.53C (CORE) | high |
| `4CH1-CON-METALLOID` | Semi-metals (metalloids) — elements bordering the metal/non-metal divide | CONCEPT | 4CH1-1.21 (ENRICHMENT) | high |
| `4CH1-CON-MIXTURE` | Mixture | CONCEPT | 4CH1-1.8 (CORE) | high |
| `4CH1-CON-MOLAR-ENTHALPY` | Molar enthalpy change (ΔH = Q/n) | CONCEPT | 4CH1-3.4 (CORE) | high |
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
| `4CH1-CON-RATE-EXPERIMENTS` | Rate-of-reaction experiments (gas collection, disappearing cross, timing methods) | CONCEPT | 4CH1-3.9 (CORE) | high |
| `4CH1-CON-RATE-FACTORS` | Factors affecting the rate of reaction (surface area, concentration and pressure, temperature, catalyst) | CONCEPT | 4CH1-3.10 (CORE) | high |
| `4CH1-CON-REACTING-MASS` | Reacting mass calculation | CONCEPT | 4CH1-1.29 (CORE) | high |
| `4CH1-CON-REACTION-PROFILE` | Reaction profile diagrams (showing ΔH and activation energy) | CONCEPT | 4CH1-3.14C (CORE) | high |
| `4CH1-CON-REDOX-ELECTRONS` | Oxidation and reduction in terms of electron loss and gain | CONCEPT | 4CH1-1.59C (CORE) | high |
| `4CH1-CON-REVERSIBLE` | Reversible reactions and the ⇌ notation | CONCEPT | 4CH1-3.17 (CORE) | high |
| `4CH1-CON-REVERSIBLE-EXAMPLES` | Named reversible reactions (ammonium chloride; hydrated copper(II) sulfate) | CONCEPT | 4CH1-3.18 (CORE) | high |
| `4CH1-CON-RF-VALUE` | Retention factor (Rf) | CONCEPT | 4CH1-1.12 (CORE) | high |
| `4CH1-CON-SATURATED-SOLUTION` | Saturated solution | CONCEPT | 4CH1-1.4 (CORE); 4CH1-1.10 (SUPPORTING) | high |
| `4CH1-CON-SIMPLE-DISTILLATION` | Simple distillation | CONCEPT | 4CH1-1.10 (CORE) | high |
| `4CH1-CON-SIMPLE-MOLECULAR` | Simple molecular structures (weak intermolecular forces; low melting and boiling points; the relative-molecular-mass trend) | CONCEPT | 4CH1-1.47 (CORE); 4CH1-1.48 (CORE) | high |
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
| `4CH1-MIS-BOND-ENERGY-COUNT` | Counting the wrong number or type of bonds in bond-energy calculations (ignoring balancing numbers) | MISCONCEPTION |  | medium |
| `4CH1-MIS-CATALYST-PARTICLE-ENERGY` | Explaining a catalyst's effect as particles gaining energy or moving more quickly | MISCONCEPTION |  | high |
| `4CH1-MIS-CONC-UNIT` | Failing to convert cm3 to dm3 in concentration calculations | MISCONCEPTION |  | high |
| `4CH1-MIS-COVALENT-BONDS-BROKEN` | Saying covalent bonds are broken when simple molecular substances melt or boil (instead of weak intermolecular forces) | MISCONCEPTION |  | high |
| `4CH1-MIS-CRYSTALLISATION-DRYNESS` | Obtaining crystals by evaporating to dryness | MISCONCEPTION |  | high |
| `4CH1-MIS-ENTHALPY-UNIT-J` | Quoting the molar enthalpy change as the unconverted joule value (e.g. 50 000) instead of kilojoules | MISCONCEPTION |  | high |
| `4CH1-MIS-EQ-PRESSURE-FEWER` | Predicting that a pressure change shifts equilibrium to the side with fewer gas molecules in the wrong direction | MISCONCEPTION |  | medium |
| `4CH1-MIS-EQ-SUBSCRIPT` | Balancing equations by altering subscripts | MISCONCEPTION |  | high |
| `4CH1-MIS-EQ-TEMP-EXO` | Predicting that raising the temperature shifts equilibrium in the exothermic direction | MISCONCEPTION |  | high |
| `4CH1-MIS-GAS-PARTICLES-TOUCH` | Drawing gas particles touching each other or joined by bonds | MISCONCEPTION |  | high |
| `4CH1-MIS-GRAPHITE-LAYER-BONDS` | Saying graphite layers are held together by bonds (instead of weak forces of attraction between the layers) | MISCONCEPTION |  | high |
| `4CH1-MIS-IONIC-BOND-ATOMS` | Describing ionic bonding as attraction between atoms or molecules (or as intermolecular forces) | MISCONCEPTION |  | high |
| `4CH1-MIS-IONIC-CONDUCTION-ELECTRONS` | Believing ionic compounds conduct electricity because electrons move and carry the charge | MISCONCEPTION |  | high |
| `4CH1-MIS-ISOTOPES-DIFFER-PROTONS` | Believing isotopes of an element differ in their number of protons | MISCONCEPTION |  | high |
| `4CH1-MIS-RAM-MASS-NUMBER` | Calling the Periodic Table relative atomic mass the mass number | MISCONCEPTION |  | high |

