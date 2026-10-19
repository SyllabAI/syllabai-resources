# C11 Diff Review Bundle — pending §18 edge promotions (generated 2026-09-22)

- baseline commit: `ae6a5e4`
- state fingerprint: `afc4fc759b3e` (promo_count=153)
- actionable: 18 edges (clean 18 / pending-flagged 0); not-actionable: 5; nodes awaiting a pathway: 129
- preview fidelity: simulator re-emits graph/igcse-chemistry/concept_edges under the generator's own serialization contract with a byte-identity guard — what you read is what G13 will write.

## Batch approval

```bash
cd work/syllabai-resources && python3 scripts/c11_diff_review.py approve \
  '4CH1-CON-AIR-COMPOSITION EXPLAINED_BY 4CH1-CON-O2-PERCENT-DETERMINATION' \
  '4CH1-CON-COMBUSTION-O2 REQUIRES_PREREQUISITE 4CH1-CON-EXO-ENDO' \
  '4CH1-CON-G1-PREDICTION REQUIRES_PREREQUISITE 4CH1-CON-G1-TREND' \
  '4CH1-CON-G1-REACTIVITY-ECONFIG REQUIRES_PREREQUISITE 4CH1-CON-ELECTRONIC-CONFIGURATION' \
  '4CH1-CON-G1-TREND EXPLAINED_BY 4CH1-CON-G1-REACTIVITY-ECONFIG' \
  '4CH1-CON-G1-TREND REQUIRES_PREREQUISITE 4CH1-CON-G1-FAMILY-EVIDENCE' \
  '4CH1-CON-G7-DISPLACEMENT REQUIRES_PREREQUISITE 4CH1-CON-G7-PROPERTIES' \
  '4CH1-CON-G7-DISPLACEMENT REQUIRES_PREREQUISITE 4CH1-CON-G7-REACTIVITY-ECONFIG' \
  '4CH1-CON-G7-PREDICTION REQUIRES_PREREQUISITE 4CH1-CON-G7-PROPERTIES' \
  '4CH1-CON-G7-PREDICTION REQUIRES_PREREQUISITE 4CH1-CON-G7-REACTIVITY-ECONFIG' \
  '4CH1-CON-G7-REACTIVITY-ECONFIG REQUIRES_PREREQUISITE 4CH1-CON-ELECTRONIC-CONFIGURATION' \
  '4CH1-MIS-CUO-COLOUR REMEDIATED_BY 4CH1-CON-CO2-FROM-CARBONATES' \
  '4CH1-MIS-CUO-COLOUR WRONG_ANSWER_PATTERN 4CH1-CON-CO2-FROM-CARBONATES' \
  '4CH1-MIS-G1-SHELL-EXPLANATION REMEDIATED_BY 4CH1-CON-G1-REACTIVITY-ECONFIG' \
  '4CH1-MIS-G1-SHELL-EXPLANATION WRONG_ANSWER_PATTERN 4CH1-CON-G1-REACTIVITY-ECONFIG' \
  '4CH1-MIS-HALOGEN-HALIDE REMEDIATED_BY 4CH1-CON-G7-DISPLACEMENT' \
  '4CH1-MIS-HALOGEN-HALIDE WRONG_ANSWER_PATTERN 4CH1-CON-G7-DISPLACEMENT' \
  '4CH1-PR-05 REQUIRES_PREREQUISITE 4CH1-CON-O2-PERCENT-DETERMINATION' \
  --by <operator> --date 2026-09-22 --review-ref graph/reports/C11_DIFF_REVIEW_B5_2026-09-22.md
```

Pending-flagged (PENDING operator_decision) edges are excluded from the command above; approving them additionally requires `--include-pending` — that flag records the explicit decision this bundle presents.

## Index

| # | identity | confidence | flag |
|---|----------|------------|------|
| 1 | `4CH1-CON-AIR-COMPOSITION EXPLAINED_BY 4CH1-CON-O2-PERCENT-DETERMINATION` | high |  |
| 2 | `4CH1-CON-COMBUSTION-O2 REQUIRES_PREREQUISITE 4CH1-CON-EXO-ENDO` | high |  |
| 3 | `4CH1-CON-G1-PREDICTION REQUIRES_PREREQUISITE 4CH1-CON-G1-TREND` | high |  |
| 4 | `4CH1-CON-G1-REACTIVITY-ECONFIG REQUIRES_PREREQUISITE 4CH1-CON-ELECTRONIC-CONFIGURATION` | high |  |
| 5 | `4CH1-CON-G1-TREND EXPLAINED_BY 4CH1-CON-G1-REACTIVITY-ECONFIG` | high |  |
| 6 | `4CH1-CON-G1-TREND REQUIRES_PREREQUISITE 4CH1-CON-G1-FAMILY-EVIDENCE` | high |  |
| 7 | `4CH1-CON-G7-DISPLACEMENT REQUIRES_PREREQUISITE 4CH1-CON-G7-PROPERTIES` | high |  |
| 8 | `4CH1-CON-G7-DISPLACEMENT REQUIRES_PREREQUISITE 4CH1-CON-G7-REACTIVITY-ECONFIG` | high |  |
| 9 | `4CH1-CON-G7-PREDICTION REQUIRES_PREREQUISITE 4CH1-CON-G7-PROPERTIES` | high |  |
| 10 | `4CH1-CON-G7-PREDICTION REQUIRES_PREREQUISITE 4CH1-CON-G7-REACTIVITY-ECONFIG` | high |  |
| 11 | `4CH1-CON-G7-REACTIVITY-ECONFIG REQUIRES_PREREQUISITE 4CH1-CON-ELECTRONIC-CONFIGURATION` | high |  |
| 12 | `4CH1-MIS-CUO-COLOUR REMEDIATED_BY 4CH1-CON-CO2-FROM-CARBONATES` | high |  |
| 13 | `4CH1-MIS-CUO-COLOUR WRONG_ANSWER_PATTERN 4CH1-CON-CO2-FROM-CARBONATES` | high |  |
| 14 | `4CH1-MIS-G1-SHELL-EXPLANATION REMEDIATED_BY 4CH1-CON-G1-REACTIVITY-ECONFIG` | high |  |
| 15 | `4CH1-MIS-G1-SHELL-EXPLANATION WRONG_ANSWER_PATTERN 4CH1-CON-G1-REACTIVITY-ECONFIG` | high |  |
| 16 | `4CH1-MIS-HALOGEN-HALIDE REMEDIATED_BY 4CH1-CON-G7-DISPLACEMENT` | high |  |
| 17 | `4CH1-MIS-HALOGEN-HALIDE WRONG_ANSWER_PATTERN 4CH1-CON-G7-DISPLACEMENT` | high |  |
| 18 | `4CH1-PR-05 REQUIRES_PREREQUISITE 4CH1-CON-O2-PERCENT-DETERMINATION` | high |  |

## Pending items — the exact diff each approval applies

### 1. `4CH1-CON-AIR-COMPOSITION EXPLAINED_BY 4CH1-CON-O2-PERCENT-DETERMINATION` [high]

- node 4CH1-CON-AIR-COMPOSITION — Composition of dry air (approximate percentages of the four most abundant gases) (CONCEPT)
-   spec 4CH1-2.9 [CORE]: know the approximate percentages by volume of the four most abundant gases in dry air
- node 4CH1-CON-O2-PERCENT-DETERMINATION — Determining the percentage of oxygen in air (metal and non-metal routes) (CONCEPT)
-   spec 4CH1-2.10 [CORE]: understand how to determine the percentage by volume of oxygen in air using experiments invol...
- derivation: SINGLE_SOURCE_CAUSAL_TEACHING — The determination procedure DERIVES the composition value IN ONE SOURCE: the iron-wool note runs method -> initial/final volumes -> volume of oxygen -> "percentage of oxygen = 19.7%" -> conclusion "The oxygen takes up approximately 20% of the air" — the ~20% oxygen fact the composition node owns is grounded by the determination (the composition note itself states it as given). Direction: the procedure grounds the fact, not the reverse (the batch-4 EXPLAINED_BY grounding shape).
- `NOTE` Oxygen percentage in air - IGCSE Chemistry Revision Notes.md — "percentage of oxygen = 19.7%"
- `NOTE` Oxygen percentage in air - IGCSE Chemistry Revision Notes.md — "The oxygen takes up approximately 20% of the air"

```diff
@@ -7728,7 +7728,9 @@ edges:
       (2026-09-11)
     generated_date: '2026-09-22'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-22'
   version: 1
   created_at: '2026-09-22'
 - source: 4CH1-CON-CRYSTALLISATION
```

### 2. `4CH1-CON-COMBUSTION-O2 REQUIRES_PREREQUISITE 4CH1-CON-EXO-ENDO` [high]

- node 4CH1-CON-COMBUSTION-O2 — Combustion of elements in oxygen (magnesium, hydrogen, sulfur) (CONCEPT)
-   spec 4CH1-2.11 [CORE]: describe the combustion of elements in oxygen, including magnesium, hydrogen and sulfur
- node 4CH1-CON-EXO-ENDO — Exothermic and endothermic reactions (heat energy given out or taken in) (CONCEPT)
-   spec 4CH1-3.1 [CORE]: know that chemical reactions in which heat energy is given out are described as exothermic, a...
- derivation: USED_WITHOUT_RETEACHING — CROSS-SECTION boundary edge (sanctioned target, session-55 ruling — owner 4CH1-CON-EXO-ENDO, batch 4): the 2.11 note APPLIES the exo/endo classification as given ("give out heat, so they will always be exothermic reactions") without re-teaching it — the classification term is the predicate of the combustion family statement (the session-52 ruling sanctioned CON-EXO-ENDO as the S3 boundary owner; the S2 boundary reuses the SAME owner, no re-mint).
- `NOTE` Combustion  Edexcel IGCSE Chemistry Revision Notes 2017.md — "Combustion reactions give out heat, so they will always be exothermic reactions"

```diff
@@ -4839,7 +4839,9 @@ edges:
       record (4CH1-3.1); session-55 boundary ruling sanctioned target
     generated_date: '2026-09-22'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-22'
   version: 1
   created_at: '2026-09-22'
 - source: 4CH1-CON-COMPOUND
```

### 3. `4CH1-CON-G1-PREDICTION REQUIRES_PREREQUISITE 4CH1-CON-G1-TREND` [high]

- node 4CH1-CON-G1-PREDICTION — Predicting alkali-metal properties from Group 1 trends (CONCEPT)
-   spec 4CH1-2.3 [CORE]: use knowledge of trends in Group 1 to predict the properties of other alkali metals
- node 4CH1-CON-G1-TREND — Group 1 reactivity trend from air/water reaction differences (CONCEPT)
-   spec 4CH1-2.2 [CORE]: understand how the differences between the reactions of these elements with air and water pro...
- derivation: USED_WITHOUT_RETEACHING — The prediction section operates on the taught trends AS GIVEN ("Following these trends, we can say that: ...") — the trends are never re-derived in the prediction section; the spec's own use-demand (2.3 "use knowledge of trends") presupposes the 2.2 trend.
- `NOTE` Group 1 reactivity & trends - IGCSE Chemistry Revision Notes.md — "Following these trends, we can say that:"

```diff
@@ -5652,7 +5652,9 @@ edges:
       by this record (4CH1-2.2)
     generated_date: '2026-09-22'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-22'
   version: 1
   created_at: '2026-09-22'
 - source: 4CH1-CON-G1-REACTIVITY-ECONFIG
```

### 4. `4CH1-CON-G1-REACTIVITY-ECONFIG REQUIRES_PREREQUISITE 4CH1-CON-ELECTRONIC-CONFIGURATION` [high]

- node 4CH1-CON-G1-REACTIVITY-ECONFIG — Group 1 reactivity trend explained by electronic configurations (CONCEPT)
-   spec 4CH1-2.4C [CORE]: explain the trend in reactivity in Group 1 in terms of electronic configurations
- node 4CH1-CON-ELECTRONIC-CONFIGURATION — Electronic configuration of the first 20 elements (shells 2, 8, 8; configuration and Periodic Table position) (CONCEPT)
-   spec 4CH1-1.19 [CORE]: understand how to deduce the electronic configurations of the first 20 elements from their po...
-   spec 4CH1-1.22 [CORE]: understand how the electronic configuration of a main group element is related to its positio...
- derivation: USED_WITHOUT_RETEACHING — CROSS-SECTION boundary edge (sanctioned target, session-55 ruling — owner 4CH1-CON-ELECTRONIC-CONFIGURATION, batch 2): the 2.4C explanation reasons wholly in shell terms (shell diagrams, "the number of shells of electrons increases by 1", "noble gas configuration") using the electronic-configuration framework AS GIVEN — the note never re-teaches shell filling (the 2.4C note's own shell-diagram caption points at the taught configurations). No S1 identity is re-minted.
- `NOTE` Group 1 Reactivity & Electronic Configurations  Edexcel IGCSE Chemistry Revision Notes 2017.md — "As you go down Group 1, the number of shells of electrons increases by 1"

```diff
@@ -5678,7 +5678,9 @@ edges:
       target
     generated_date: '2026-09-22'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-22'
   version: 1
   created_at: '2026-09-22'
 - source: 4CH1-CON-G1-TREND
```

### 5. `4CH1-CON-G1-TREND EXPLAINED_BY 4CH1-CON-G1-REACTIVITY-ECONFIG` [high]

- node 4CH1-CON-G1-TREND — Group 1 reactivity trend from air/water reaction differences (CONCEPT)
-   spec 4CH1-2.2 [CORE]: understand how the differences between the reactions of these elements with air and water pro...
- node 4CH1-CON-G1-REACTIVITY-ECONFIG — Group 1 reactivity trend explained by electronic configurations (CONCEPT)
-   spec 4CH1-2.4C [CORE]: explain the trend in reactivity in Group 1 in terms of electronic configurations
- derivation: SINGLE_SOURCE_CAUSAL_TEACHING — The 2.4C note teaches the causal chain IN ONE SOURCE (shells increase -> outer electron further -> weaker attraction -> lost more easily -> "So, the alkali metals get more reactive as you descend the group") — the trend is the explanandum, the electronic-configuration mechanism the explainer (the batch-4 RATE-FACTORS EXPLAINED_BY COLLISION-THEORY shape).
- `NOTE` Group 1 Reactivity & Electronic Configurations  Edexcel IGCSE Chemistry Revision Notes 2017.md — "Less energy is required to overcome the force of attraction as it gets weaker, so the outer electron is los..."
- `NOTE` Group 1 Reactivity & Electronic Configurations  Edexcel IGCSE Chemistry Revision Notes 2017.md — "So, the alkali metals get more reactive as you descend the group"

```diff
@@ -7856,7 +7856,9 @@ edges:
       source node owned by this record (4CH1-2.2)
     generated_date: '2026-09-22'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-22'
   version: 1
   created_at: '2026-09-22'
 - source: 4CH1-CON-GROUP-SIMILARITY
```

### 6. `4CH1-CON-G1-TREND REQUIRES_PREREQUISITE 4CH1-CON-G1-FAMILY-EVIDENCE` [high]

- node 4CH1-CON-G1-TREND — Group 1 reactivity trend from air/water reaction differences (CONCEPT)
-   spec 4CH1-2.2 [CORE]: understand how the differences between the reactions of these elements with air and water pro...
- node 4CH1-CON-G1-FAMILY-EVIDENCE — Group 1 water-reaction similarities as family evidence (alkali metals) (CONCEPT)
-   spec 4CH1-2.1 [CORE]: understand how the similarities in the reactions of these elements with water provide evidenc...
- derivation: DEFINITIONAL_DEPENDENCY — The trend is DEFINED over the family reaction comparisons: "the differences between the reactions ... provide evidence of trends" — the 2.2 trend is the graded pattern OF the 2.1 water/oxygen reactions (the vigour gradient is stated over the same reactions the family node owns); the spec's own 2.1-then-2.2 order (similarities evidence, then differences evidence).
- `NOTE` Group 1 reactivity & trends - IGCSE Chemistry Revision Notes.md — "The differences between the reactions of the group 1 metals with water and oxygen provide evidence of trend..."
- `NOTE` Group 1 reactivity & trends - IGCSE Chemistry Revision Notes.md — "The reactions of the alkali metals with water get more vigorous as you descend the group"

```diff
@@ -5706,7 +5706,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-2.1/2.2 @ Group 1 reactivity & trends (2026-09-11)
     generated_date: '2026-09-22'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-22'
   version: 1
   created_at: '2026-09-22'
 - source: 4CH1-CON-G7-DISPLACEMENT
```

### 7. `4CH1-CON-G7-DISPLACEMENT REQUIRES_PREREQUISITE 4CH1-CON-G7-PROPERTIES` [high]

- node 4CH1-CON-G7-DISPLACEMENT — Halogen displacement reactions (evidence for the Group 7 reactivity trend) (CONCEPT)
-   spec 4CH1-2.7 [CORE]: understand how displacement reactions involving halogens and halides provide evidence for the...
- node 4CH1-CON-G7-PROPERTIES — Halogen colours, states and physical-property trends (Group 7) (CONCEPT)
-   spec 4CH1-2.5 [CORE]: know the colours, physical states (at room temperature) and trends in physical properties of ...
- derivation: USED_WITHOUT_RETEACHING — The displacement observations IDENTIFY the displaced halogen BY the taught colour-in-solution facts (orange = bromine, brown = iodine — the 2.5 property table's Colour-in-solution column) without re-teaching them — identifying WHAT formed from the colour requires the 2.5 knowledge (the GROUP7_MS Q3 observation accept/reject lists mine the same surface).
- `NOTE` Group 7 properties - IGCSE Chemistry Revision Notes.md — "The solution becomes orange as bromine is formed or"
- `NOTE` Group 7 properties - IGCSE Chemistry Revision Notes.md — "The solution becomes brown as iodine is formed"

```diff
@@ -5733,7 +5733,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-2.5/2.7 @ Group 7 properties (2026-09-11)
     generated_date: '2026-09-22'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-22'
   version: 1
   created_at: '2026-09-22'
 - source: 4CH1-CON-G7-DISPLACEMENT
```

### 8. `4CH1-CON-G7-DISPLACEMENT REQUIRES_PREREQUISITE 4CH1-CON-G7-REACTIVITY-ECONFIG` [high]

- node 4CH1-CON-G7-DISPLACEMENT — Halogen displacement reactions (evidence for the Group 7 reactivity trend) (CONCEPT)
-   spec 4CH1-2.7 [CORE]: understand how displacement reactions involving halogens and halides provide evidence for the...
- node 4CH1-CON-G7-REACTIVITY-ECONFIG — Group 7 reactivity trend explained by electronic configurations (CONCEPT)
-   spec 4CH1-2.8C [CORE]: explain the trend in reactivity in Group 7 in terms of electronic configurations
- derivation: DEFINITIONAL_DEPENDENCY — Displacement is DEFINED over the reactivity order ("a MORE reactive halogen displaces a LESS reactive halogen") — the definitional operands are exactly the Group 7 reactivity trend the 2.8C node owns (its evidence states the trend AND explains it; the spec's own 2.7 demand is the displacement family AS EVIDENCE for that trend). The batch-4 BOND-ENERGY-CALC -> BOND-BREAKING-MAKING definitional shape.
- `NOTE` Group 7 properties - IGCSE Chemistry Revision Notes.md — "A halogen displacement reaction occurs when a more reactive halogen displaces a less reactive halogen from ..."

```diff
@@ -5758,7 +5758,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-2.7 @ Group 7 properties + 4CH1-2.8C @ Group 7 reactivity (2026-09-11)
     generated_date: '2026-09-22'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-22'
   version: 1
   created_at: '2026-09-22'
 - source: 4CH1-CON-G7-PREDICTION
```

### 9. `4CH1-CON-G7-PREDICTION REQUIRES_PREREQUISITE 4CH1-CON-G7-PROPERTIES` [high]

- node 4CH1-CON-G7-PREDICTION — Predicting halogen properties from Group 7 trends (metal and non-metal halides) (CONCEPT)
-   spec 4CH1-2.6 [CORE]: use knowledge of trends in Group 7 to predict the properties of other halogens
- node 4CH1-CON-G7-PROPERTIES — Halogen colours, states and physical-property trends (Group 7) (CONCEPT)
-   spec 4CH1-2.5 [CORE]: know the colours, physical states (at room temperature) and trends in physical properties of ...
- derivation: USED_WITHOUT_RETEACHING — The prediction sections extend the taught PHYSICAL trends AS GIVEN (the MP/BP increase, the gas-liquid-solid state progression, the darkening colours — the 2.5 table) to the unknown halogens without re-deriving them; the spec's own use-demand (2.6 "use knowledge of trends"). Pass-2 re-authoring (FP-B5-5): this edge originally cited the reactivity-decrease sentence, whose trend owner is the 2.8C node — that dependency is now its own edge below; the physical-trend surface stays here.
- `NOTE` Group 7 properties - IGCSE Chemistry Revision Notes.md — "The melting and boiling points of the halogens increase as you go down the group"
- `NOTE` Group 7 properties - IGCSE Chemistry Revision Notes.md — "At room temperature (20 °C), the physical state of the halogens changes as you go down the group"

```diff
@@ -5787,7 +5787,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-2.5/2.6 @ Group 7 properties (2026-09-11)
     generated_date: '2026-09-22'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-22'
   version: 1
   created_at: '2026-09-22'
 - source: 4CH1-CON-G7-PREDICTION
```

### 10. `4CH1-CON-G7-PREDICTION REQUIRES_PREREQUISITE 4CH1-CON-G7-REACTIVITY-ECONFIG` [high]

- node 4CH1-CON-G7-PREDICTION — Predicting halogen properties from Group 7 trends (metal and non-metal halides) (CONCEPT)
-   spec 4CH1-2.6 [CORE]: use knowledge of trends in Group 7 to predict the properties of other halogens
- node 4CH1-CON-G7-REACTIVITY-ECONFIG — Group 7 reactivity trend explained by electronic configurations (CONCEPT)
-   spec 4CH1-2.8C [CORE]: explain the trend in reactivity in Group 7 in terms of electronic configurations
- derivation: USED_WITHOUT_RETEACHING — The prediction sections operate on the taught REACTIVITY trend AS GIVEN (the decrease down the group, the slower/less vigorous reactions further down — stated in the metal-halide and non-metal-halide prediction sections themselves) — the trend owner is the 2.8C node (its evidence states the trend AND explains it); the pass-2 re-authoring (FP-B5-5) moved this dependency off the mistargeted properties edge.
- `NOTE` Group 7 properties - IGCSE Chemistry Revision Notes.md — "The halogens decrease in reactivity moving down the group, but they still form halide salts with some metal..."
- `NOTE` Group 7 properties - IGCSE Chemistry Revision Notes.md — "The rate of reaction is slower for halogens which are further down the group such as bromine and iodine"

```diff
@@ -5817,7 +5817,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-2.6 @ Group 7 properties + 4CH1-2.8C @ Group 7 reactivity (2026-09-11)
     generated_date: '2026-09-22'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-22'
   version: 1
   created_at: '2026-09-22'
 - source: 4CH1-CON-G7-REACTIVITY-ECONFIG
```

### 11. `4CH1-CON-G7-REACTIVITY-ECONFIG REQUIRES_PREREQUISITE 4CH1-CON-ELECTRONIC-CONFIGURATION` [high]

- node 4CH1-CON-G7-REACTIVITY-ECONFIG — Group 7 reactivity trend explained by electronic configurations (CONCEPT)
-   spec 4CH1-2.8C [CORE]: explain the trend in reactivity in Group 7 in terms of electronic configurations
- node 4CH1-CON-ELECTRONIC-CONFIGURATION — Electronic configuration of the first 20 elements (shells 2, 8, 8; configuration and Periodic Table position) (CONCEPT)
-   spec 4CH1-1.19 [CORE]: understand how to deduce the electronic configurations of the first 20 elements from their po...
-   spec 4CH1-1.22 [CORE]: understand how the electronic configuration of a main group element is related to its positio...
- derivation: USED_WITHOUT_RETEACHING — CROSS-SECTION boundary edge (sanctioned target, session-55 ruling — owner 4CH1-CON-ELECTRONIC-CONFIGURATION, batch 2): the note states the dependency VERBATIM ("We can use electronic configuration to explain the trends...") and reasons in shell terms AS GIVEN (seven outer electrons, shells increasing down the group) — never re-teaching shell filling. No S1 identity is re-minted.
- `NOTE` Group 7 reactivity - IGCSE Chemistry Revision Notes.md — "We can use electronic configuration to explain the trends in chemical reactivity down Group 7"

```diff
@@ -5842,7 +5842,9 @@ edges:
       the batch-2 record (4CH1-1.39/1.40); session-55 boundary ruling sanctioned target
     generated_date: '2026-09-22'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-22'
   version: 1
   created_at: '2026-09-22'
 - source: 4CH1-CON-GAS-VOL-CALC
```

### 12. `4CH1-MIS-CUO-COLOUR REMEDIATED_BY 4CH1-CON-CO2-FROM-CARBONATES` [high]

- node 4CH1-MIS-CUO-COLOUR — Stating a colour other than black for the copper(II) oxide decomposition product (MISCONCEPTION)
- node 4CH1-CON-CO2-FROM-CARBONATES — Carbon dioxide from thermal decomposition of metal carbonates (CONCEPT)
-   spec 4CH1-2.12 [CORE]: describe the formation of carbon dioxide from the thermal decomposition of metal carbonates, ...
- derivation: ASSESSMENT_DOCUMENTED — Remediation target = the misconception target (the B1-E-25 pattern): the corrective content IS the taught colour-change statement (the 2.12 note's "slowly darkens as black copper(II) oxide is produced", quoted in the node's remediation_evidence).
- `NOTE` Thermal decomposition - IGCSE Chemistry Revision Notes.md — "Copper(II) carbonate is a green powder and slowly darkens as black copper(II) oxide is produced"

```diff
@@ -8720,7 +8720,9 @@ edges:
       Q1c expected answer
     generated_date: '2026-09-22'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-22'
   version: 1
   created_at: '2026-09-22'
 - source: 4CH1-MIS-ENTHALPY-UNIT-J
```

### 13. `4CH1-MIS-CUO-COLOUR WRONG_ANSWER_PATTERN 4CH1-CON-CO2-FROM-CARBONATES` [high]

- node 4CH1-MIS-CUO-COLOUR — Stating a colour other than black for the copper(II) oxide decomposition product (MISCONCEPTION)
- node 4CH1-CON-CO2-FROM-CARBONATES — Carbon dioxide from thermal decomposition of metal carbonates (CONCEPT)
-   spec 4CH1-2.12 [CORE]: describe the formation of carbon dioxide from the thermal decomposition of metal carbonates, ...
- derivation: ASSESSMENT_DOCUMENTED — The pinned GASES MS Q1c documents the wrong-answer pattern OF the carbonate-decomposition concept's named example: any colour other than black for the CuO product is rejected (IGNORE brown / REJECT all other colours against the expected "black").
- `MARK_SCHEME` GASES_MS_P2.txt — "REJECT all other colours"

```diff
@@ -8326,7 +8326,9 @@ edges:
     upstream: pinned GASES_MS_P2 (sha1_12 c65669a9c763) Q1c Notes column; spec 4CH1-2.12 official wording
     generated_date: '2026-09-22'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-22'
   version: 1
   created_at: '2026-09-22'
 - source: 4CH1-MIS-ENTHALPY-UNIT-J
```

### 14. `4CH1-MIS-G1-SHELL-EXPLANATION REMEDIATED_BY 4CH1-CON-G1-REACTIVITY-ECONFIG` [high]

- node 4CH1-MIS-G1-SHELL-EXPLANATION — Explaining Group 1 reactivity via more shells / larger radius / shielding instead of outer-electron distance and weaker attraction (MISCONCEPTION)
- node 4CH1-CON-G1-REACTIVITY-ECONFIG — Group 1 reactivity trend explained by electronic configurations (CONCEPT)
-   spec 4CH1-2.4C [CORE]: explain the trend in reactivity in Group 1 in terms of electronic configurations
- derivation: ASSESSMENT_DOCUMENTED — Remediation target = the misconception target (the B1-E-25/batch-2/3/4 pattern): the corrective content IS the taught distance+attraction mechanism (the 2.4C note's mechanism statements, quoted in the node's remediation_evidence) — the exact form the MS award rules reward ("potassium loses its outer/valence electron more easily/readily" + "because it is further from (the attraction of) nucleus").
- `NOTE` Group 1 Reactivity & Electronic Configurations  Edexcel IGCSE Chemistry Revision Notes 2017.md — "Less energy is required to overcome the force of attraction as it gets weaker, so the outer electron is los..."

```diff
@@ -8849,7 +8849,9 @@ edges:
       pinned GROUP1_MS_P2 Q1d accept surface
     generated_date: '2026-09-22'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-22'
   version: 1
   created_at: '2026-09-22'
 - source: 4CH1-MIS-GAS-PARTICLES-TOUCH
```

### 15. `4CH1-MIS-G1-SHELL-EXPLANATION WRONG_ANSWER_PATTERN 4CH1-CON-G1-REACTIVITY-ECONFIG` [high]

- node 4CH1-MIS-G1-SHELL-EXPLANATION — Explaining Group 1 reactivity via more shells / larger radius / shielding instead of outer-electron distance and weaker attraction (MISCONCEPTION)
- node 4CH1-CON-G1-REACTIVITY-ECONFIG — Group 1 reactivity trend explained by electronic configurations (CONCEPT)
-   spec 4CH1-2.4C [CORE]: explain the trend in reactivity in Group 1 in terms of electronic configurations
- derivation: ASSESSMENT_DOCUMENTED — The pinned GROUP1 MS documents the wrong-answer pattern OF the 2.4C explanation concept: shell-count/larger-radius/shielding explanations are explicitly non-scoring (Q1d IGNORE list + Q3d "Ignore references to shielding" + the nucleus/protons award restriction).
- `MARK_SCHEME` GROUP1_MS_P2.txt — "IGNORE references to more shells / larger atomic radius / more"

```diff
@@ -8424,7 +8424,9 @@ edges:
     upstream: pinned GROUP1_MS_P2 (sha1_12 7c27bbfc09cd) Q1d/Q3d; spec 4CH1-2.4C official wording
     generated_date: '2026-09-22'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-22'
   version: 1
   created_at: '2026-09-22'
 - source: 4CH1-MIS-GAS-PARTICLES-TOUCH
```

### 16. `4CH1-MIS-HALOGEN-HALIDE REMEDIATED_BY 4CH1-CON-G7-DISPLACEMENT` [high]

- node 4CH1-MIS-HALOGEN-HALIDE — Treating a halogen and its halide ion as having the same (or different) reactivity in displacement reasoning (MISCONCEPTION)
- node 4CH1-CON-G7-DISPLACEMENT — Halogen displacement reactions (evidence for the Group 7 reactivity trend) (CONCEPT)
-   spec 4CH1-2.7 [CORE]: understand how displacement reactions involving halogens and halides provide evidence for the...
- derivation: ASSESSMENT_DOCUMENTED — Remediation target = the misconception target (the B1-E-25 pattern): the corrective content IS the displacement rule (the note's definition, quoted in the node's remediation_evidence) and the MS's own expected-answer surface ("a halogen/an element cannot displace itself"; "a halogen cannot displace a more reactive halogen").
- `NOTE` Group 7 properties - IGCSE Chemistry Revision Notes.md — "A halogen displacement reaction occurs when a more reactive halogen displaces a less reactive halogen from ..."

```diff
@@ -8925,7 +8925,9 @@ edges:
       expected answers
     generated_date: '2026-09-22'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-22'
   version: 1
   created_at: '2026-09-22'
 - source: 4CH1-MIS-IONIC-BOND-ATOMS
```

### 17. `4CH1-MIS-HALOGEN-HALIDE WRONG_ANSWER_PATTERN 4CH1-CON-G7-DISPLACEMENT` [high]

- node 4CH1-MIS-HALOGEN-HALIDE — Treating a halogen and its halide ion as having the same (or different) reactivity in displacement reasoning (MISCONCEPTION)
- node 4CH1-CON-G7-DISPLACEMENT — Halogen displacement reactions (evidence for the Group 7 reactivity trend) (CONCEPT)
-   spec 4CH1-2.7 [CORE]: understand how displacement reactions involving halogens and halides provide evidence for the...
- derivation: ASSESSMENT_DOCUMENTED — The pinned GROUP7 MS Q1bii Reject column documents the wrong-answer pattern OF the displacement concept: reasoning about a halogen's reactivity relative to a HALIDE ION (either direction) is explicitly rejected — the displacement rule operates halogen-vs-halogen through its halide solution.
- `MARK_SCHEME` GROUP7_MS_P2.txt — "Reject any references to a halogen"

```diff
@@ -8493,7 +8493,9 @@ edges:
     upstream: pinned GROUP7_MS_P2 (sha1_12 10edeea32c73) Q1bii Reject column; spec 4CH1-2.7 official wording
     generated_date: '2026-09-22'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-22'
   version: 1
   created_at: '2026-09-22'
 - source: 4CH1-MIS-IONIC-BOND-ATOMS
```

### 18. `4CH1-PR-05 REQUIRES_PREREQUISITE 4CH1-CON-O2-PERCENT-DETERMINATION` [high]

- node 4CH1-CON-O2-PERCENT-DETERMINATION — Determining the percentage of oxygen in air (metal and non-metal routes) (CONCEPT)
-   spec 4CH1-2.10 [CORE]: understand how to determine the percentage by volume of oxygen in air using experiments invol...
- derivation: USED_WITHOUT_RETEACHING — Practical -> conceptual (the pilot test #5 requirement, the PR-09 -> CON-CALORIMETRY batch-4 shape): the 2.14 practical IS the iron-route INSTANCE of the 2.10 determination — its aim, method, results, calculation and conclusion sections run the determination procedure (aim "To determine the percentage of oxygen in air using the oxidation of iron"; the percentage calculation "percentage of oxygen = volume of oxygen / initial volume of air x 100"); the practical presupposes the determination concept the 2.10 node owns.
- `NOTE` Oxygen percentage in air - IGCSE Chemistry Revision Notes.md — "To determine the percentage of oxygen in air using the oxidation of iron"
- `NOTE` Oxygen percentage in air - IGCSE Chemistry Revision Notes.md — "percentage of oxygen ="

```diff
@@ -7568,7 +7568,9 @@ edges:
       4CH1-PR-05 (spec_point 4CH1-2.14)
     generated_date: '2026-09-22'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-22'
   version: 1
   created_at: '2026-09-22'
 - source: 4CH1-PR-09
```

## File-level meta hunks (once, for the whole batch)

```diff
@@ -158,8 +158,10 @@ meta:
     remediated_by_edges: 18
     requires_prerequisite_edges: 125
     wrong_answer_pattern_edges: 16
-    promoted_edges: 270
-    human_validated_edges: 270
+    promoted_edges: 288
+    human_validated_edges: 288
   promotion_record: scripts/c11_promotions.yaml
   attachment_promotion_record: scripts/c19_promotions.yaml
 edges:
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
| `4CH1-CON-AIR-COMPOSITION` | Composition of dry air (approximate percentages of the four most abundant gases) | CONCEPT | 4CH1-2.9 (CORE) | high |
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
| `4CH1-CON-CO2-FROM-CARBONATES` | Carbon dioxide from thermal decomposition of metal carbonates | CONCEPT | 4CH1-2.12 (CORE) | high |
| `4CH1-CON-CO2-GREENHOUSE` | Carbon dioxide as a greenhouse gas and the climate-change link | CONCEPT | 4CH1-2.13 (CORE) | high |
| `4CH1-CON-COLLISION-THEORY` | Collision-theory explanations of rate changes (frequency and success of collisions) | CONCEPT | 4CH1-3.11 (CORE) | high |
| `4CH1-CON-COMBUSTION-O2` | Combustion of elements in oxygen (magnesium, hydrogen, sulfur) | CONCEPT | 4CH1-2.11 (CORE) | high |
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
| `4CH1-CON-G1-FAMILY-EVIDENCE` | Group 1 water-reaction similarities as family evidence (alkali metals) | CONCEPT | 4CH1-2.1 (CORE) | high |
| `4CH1-CON-G1-PREDICTION` | Predicting alkali-metal properties from Group 1 trends | CONCEPT | 4CH1-2.3 (CORE) | high |
| `4CH1-CON-G1-REACTIVITY-ECONFIG` | Group 1 reactivity trend explained by electronic configurations | CONCEPT | 4CH1-2.4C (CORE) | high |
| `4CH1-CON-G1-TREND` | Group 1 reactivity trend from air/water reaction differences | CONCEPT | 4CH1-2.2 (CORE) | high |
| `4CH1-CON-G7-DISPLACEMENT` | Halogen displacement reactions (evidence for the Group 7 reactivity trend) | CONCEPT | 4CH1-2.7 (CORE) | high |
| `4CH1-CON-G7-PREDICTION` | Predicting halogen properties from Group 7 trends (metal and non-metal halides) | CONCEPT | 4CH1-2.6 (CORE) | high |
| `4CH1-CON-G7-PROPERTIES` | Halogen colours, states and physical-property trends (Group 7) | CONCEPT | 4CH1-2.5 (CORE) | high |
| `4CH1-CON-G7-REACTIVITY-ECONFIG` | Group 7 reactivity trend explained by electronic configurations | CONCEPT | 4CH1-2.8C (CORE) | high |
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
| `4CH1-CON-O2-PERCENT-DETERMINATION` | Determining the percentage of oxygen in air (metal and non-metal routes) | CONCEPT | 4CH1-2.10 (CORE) | high |
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
| `4CH1-MIS-CUO-COLOUR` | Stating a colour other than black for the copper(II) oxide decomposition product | MISCONCEPTION |  | high |
| `4CH1-MIS-ENTHALPY-UNIT-J` | Quoting the molar enthalpy change as the unconverted joule value (e.g. 50 000) instead of kilojoules | MISCONCEPTION |  | high |
| `4CH1-MIS-EQ-PRESSURE-FEWER` | Predicting that a pressure change shifts equilibrium to the side with fewer gas molecules in the wrong direction | MISCONCEPTION |  | medium |
| `4CH1-MIS-EQ-SUBSCRIPT` | Balancing equations by altering subscripts | MISCONCEPTION |  | high |
| `4CH1-MIS-EQ-TEMP-EXO` | Predicting that raising the temperature shifts equilibrium in the exothermic direction | MISCONCEPTION |  | high |
| `4CH1-MIS-G1-SHELL-EXPLANATION` | Explaining Group 1 reactivity via more shells / larger radius / shielding instead of outer-electron distance and weaker attraction | MISCONCEPTION |  | high |
| `4CH1-MIS-GAS-PARTICLES-TOUCH` | Drawing gas particles touching each other or joined by bonds | MISCONCEPTION |  | high |
| `4CH1-MIS-GRAPHITE-LAYER-BONDS` | Saying graphite layers are held together by bonds (instead of weak forces of attraction between the layers) | MISCONCEPTION |  | high |
| `4CH1-MIS-HALOGEN-HALIDE` | Treating a halogen and its halide ion as having the same (or different) reactivity in displacement reasoning | MISCONCEPTION |  | high |
| `4CH1-MIS-IONIC-BOND-ATOMS` | Describing ionic bonding as attraction between atoms or molecules (or as intermolecular forces) | MISCONCEPTION |  | high |
| `4CH1-MIS-IONIC-CONDUCTION-ELECTRONS` | Believing ionic compounds conduct electricity because electrons move and carry the charge | MISCONCEPTION |  | high |
| `4CH1-MIS-ISOTOPES-DIFFER-PROTONS` | Believing isotopes of an element differ in their number of protons | MISCONCEPTION |  | high |
| `4CH1-MIS-RAM-MASS-NUMBER` | Calling the Periodic Table relative atomic mass the mass number | MISCONCEPTION |  | high |

