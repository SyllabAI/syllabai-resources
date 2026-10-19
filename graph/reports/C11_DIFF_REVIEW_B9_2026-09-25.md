# C11 Diff Review Bundle — pending §18 edge promotions (generated 2026-09-25)

- baseline commit: `1e2cf8e`
- state fingerprint: `1735e42ad900` (promo_count=216)
- actionable: 20 edges (clean 20 / pending-flagged 0); not-actionable: 5; nodes awaiting a pathway: 180
- preview fidelity: simulator re-emits graph/igcse-chemistry/concept_edges under the generator's own serialization contract with a byte-identity guard — what you read is what G13 will write.

## Batch approval

```bash
cd work/syllabai-resources && python3 scripts/c11_diff_review.py approve \
  '4CH1-CON-ACID-RAIN-CAUSES REQUIRES_PREREQUISITE 4CH1-CON-FUELS-COMBUSTION' \
  '4CH1-CON-ALKANE-HALOGEN-SUBSTITUTION REQUIRES_PREREQUISITE 4CH1-CON-ALKANES' \
  '4CH1-CON-ALKANE-HALOGEN-SUBSTITUTION REQUIRES_PREREQUISITE 4CH1-CON-ORGANIC-REACTION-CLASSES' \
  '4CH1-CON-ALKANES REQUIRES_PREREQUISITE 4CH1-CON-HOMOLOGOUS-SERIES' \
  '4CH1-CON-CO-POISONING REQUIRES_PREREQUISITE 4CH1-CON-FUELS-COMBUSTION' \
  '4CH1-CON-CRACKING REQUIRES_PREREQUISITE 4CH1-CON-CRUDE-OIL-FRACTIONS' \
  '4CH1-CON-CRUDE-OIL REQUIRES_PREREQUISITE 4CH1-CON-HYDROCARBON' \
  '4CH1-CON-CRUDE-OIL REQUIRES_PREREQUISITE 4CH1-CON-MIXTURE' \
  '4CH1-CON-CRUDE-OIL-FRACTIONS REQUIRES_PREREQUISITE 4CH1-CON-CRUDE-OIL' \
  '4CH1-CON-CRUDE-OIL-FRACTIONS REQUIRES_PREREQUISITE 4CH1-CON-FRACTIONAL-DISTILLATION' \
  '4CH1-CON-FUELS-COMBUSTION REQUIRES_PREREQUISITE 4CH1-CON-COMBUSTION-O2' \
  '4CH1-CON-FUELS-COMBUSTION REQUIRES_PREREQUISITE 4CH1-CON-CRUDE-OIL-FRACTIONS' \
  '4CH1-CON-ISOMERS REQUIRES_PREREQUISITE 4CH1-CON-ORGANIC-FORMULAE' \
  '4CH1-CON-IUPAC-NAMING REQUIRES_PREREQUISITE 4CH1-CON-HOMOLOGOUS-SERIES' \
  '4CH1-CON-ORGANIC-FORMULAE REQUIRES_PREREQUISITE 4CH1-CON-EMPIRICAL-FORMULA' \
  '4CH1-CON-ORGANIC-FORMULAE REQUIRES_PREREQUISITE 4CH1-CON-HYDROCARBON' \
  '4CH1-CON-ORGANIC-FORMULAE REQUIRES_PREREQUISITE 4CH1-CON-MOLECULAR-FORMULA' \
  '4CH1-CON-ORGANIC-REACTION-CLASSES REQUIRES_PREREQUISITE 4CH1-CON-HOMOLOGOUS-SERIES' \
  '4CH1-MIS-KEROSENE-DOUBLE-BONDS REMEDIATED_BY 4CH1-CON-CRUDE-OIL-FRACTIONS' \
  '4CH1-MIS-KEROSENE-DOUBLE-BONDS WRONG_ANSWER_PATTERN 4CH1-CON-CRUDE-OIL-FRACTIONS' \
  --by <operator> --date 2026-09-25 --review-ref graph/reports/C11_DIFF_REVIEW_2026-09-25.md
```

Pending-flagged (PENDING operator_decision) edges are excluded from the command above; approving them additionally requires `--include-pending` — that flag records the explicit decision this bundle presents.

## Index

| # | identity | confidence | flag |
|---|----------|------------|------|
| 1 | `4CH1-CON-ACID-RAIN-CAUSES REQUIRES_PREREQUISITE 4CH1-CON-FUELS-COMBUSTION` | high |  |
| 2 | `4CH1-CON-ALKANE-HALOGEN-SUBSTITUTION REQUIRES_PREREQUISITE 4CH1-CON-ALKANES` | high |  |
| 3 | `4CH1-CON-ALKANE-HALOGEN-SUBSTITUTION REQUIRES_PREREQUISITE 4CH1-CON-ORGANIC-REACTION-CLASSES` | high |  |
| 4 | `4CH1-CON-ALKANES REQUIRES_PREREQUISITE 4CH1-CON-HOMOLOGOUS-SERIES` | high |  |
| 5 | `4CH1-CON-CO-POISONING REQUIRES_PREREQUISITE 4CH1-CON-FUELS-COMBUSTION` | high |  |
| 6 | `4CH1-CON-CRACKING REQUIRES_PREREQUISITE 4CH1-CON-CRUDE-OIL-FRACTIONS` | high |  |
| 7 | `4CH1-CON-CRUDE-OIL REQUIRES_PREREQUISITE 4CH1-CON-HYDROCARBON` | high |  |
| 8 | `4CH1-CON-CRUDE-OIL REQUIRES_PREREQUISITE 4CH1-CON-MIXTURE` | high |  |
| 9 | `4CH1-CON-CRUDE-OIL-FRACTIONS REQUIRES_PREREQUISITE 4CH1-CON-CRUDE-OIL` | high |  |
| 10 | `4CH1-CON-CRUDE-OIL-FRACTIONS REQUIRES_PREREQUISITE 4CH1-CON-FRACTIONAL-DISTILLATION` | high |  |
| 11 | `4CH1-CON-FUELS-COMBUSTION REQUIRES_PREREQUISITE 4CH1-CON-COMBUSTION-O2` | high |  |
| 12 | `4CH1-CON-FUELS-COMBUSTION REQUIRES_PREREQUISITE 4CH1-CON-CRUDE-OIL-FRACTIONS` | high |  |
| 13 | `4CH1-CON-ISOMERS REQUIRES_PREREQUISITE 4CH1-CON-ORGANIC-FORMULAE` | high |  |
| 14 | `4CH1-CON-IUPAC-NAMING REQUIRES_PREREQUISITE 4CH1-CON-HOMOLOGOUS-SERIES` | high |  |
| 15 | `4CH1-CON-ORGANIC-FORMULAE REQUIRES_PREREQUISITE 4CH1-CON-EMPIRICAL-FORMULA` | high |  |
| 16 | `4CH1-CON-ORGANIC-FORMULAE REQUIRES_PREREQUISITE 4CH1-CON-HYDROCARBON` | high |  |
| 17 | `4CH1-CON-ORGANIC-FORMULAE REQUIRES_PREREQUISITE 4CH1-CON-MOLECULAR-FORMULA` | high |  |
| 18 | `4CH1-CON-ORGANIC-REACTION-CLASSES REQUIRES_PREREQUISITE 4CH1-CON-HOMOLOGOUS-SERIES` | high |  |
| 19 | `4CH1-MIS-KEROSENE-DOUBLE-BONDS REMEDIATED_BY 4CH1-CON-CRUDE-OIL-FRACTIONS` | high |  |
| 20 | `4CH1-MIS-KEROSENE-DOUBLE-BONDS WRONG_ANSWER_PATTERN 4CH1-CON-CRUDE-OIL-FRACTIONS` | high |  |

## Pending items — the exact diff each approval applies

### 1. `4CH1-CON-ACID-RAIN-CAUSES REQUIRES_PREREQUISITE 4CH1-CON-FUELS-COMBUSTION` [high]

- node 4CH1-CON-ACID-RAIN-CAUSES — Nitrogen oxides and sulfur dioxide as acid-rain causes (CONCEPT)
-   spec 4CH1-4.14 [CORE]: know that, in car engines, the temperature reached is high enough to allow nitrogen and oxyge...
-   spec 4CH1-4.16 [CORE]: understand how sulfur dioxide and oxides of nitrogen contribute to acid rain
- node 4CH1-CON-FUELS-COMBUSTION — Fuels and the products of complete and incomplete combustion (CONCEPT)
-   spec 4CH1-4.11 [CORE]: know that a fuel is a substance that, when burned, releases heat energy
-   spec 4CH1-4.12 [CORE]: know the possible products of complete and incomplete combustion of hydrocarbons with oxygen ...
- derivation: USED_WITHOUT_RETEACHING — the acid-rain chemistry presupposes the fuels/ combustion surface (both named pollutants are 'produced from the combustion' — the engines/combustion context is applied as given, never re-taught by the NOx/SO2 note)
- `NOTE` Nitrogen Oxides & Sulfur Dioxide  Edexcel IGCSE Chemistry Revision Notes 2017.md — "The sulfur dioxide produced from the combustion of fossil fuels dissolves in rainwater droplets to form **s..."
- `NOTE` Nitrogen Oxides & Sulfur Dioxide  Edexcel IGCSE Chemistry Revision Notes 2017.md — "**Nitrogen dioxide** produced from car engines reacts with rain water to form a mixture of **nitrous** and ..."

```diff
@@ -6823,7 +6823,9 @@ edges:
       by the NOx/SO2 note)
     upstream: T-C10 HUMAN_VALIDATED 4CH1-4.14/4.16 @ Nitrogen Oxides & Sulfur Dioxide note (2026-09-11)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-25'
   version: 1
   created_at: '2026-09-24'
 - source: 4CH1-CON-ACID-REACTIONS
```

### 2. `4CH1-CON-ALKANE-HALOGEN-SUBSTITUTION REQUIRES_PREREQUISITE 4CH1-CON-ALKANES` [high]

- node 4CH1-CON-ALKANE-HALOGEN-SUBSTITUTION — Alkane substitution reactions with halogens under ultraviolet radiation (CONCEPT)
-   spec 4CH1-4.22 [CORE]: describe the reactions of alkanes with halogens in the presence of ultraviolet radiation, lim...
- node 4CH1-CON-ALKANES — Alkanes (general formula, saturated hydrocarbons, first five members) (CONCEPT)
-   spec 4CH1-4.19 [CORE]: know the general formula for alkanes
-   spec 4CH1-4.20 [CORE]: explain why alkanes are classified as saturated hydrocarbons
-   spec 4CH1-4.21 [CORE]: understand how to draw the structural and displayed formulae for alkanes with up to five carb...
- derivation: EXPLICIT_TEACH_SEQUENCE — the substitution reactions take the ALKANES as the reacting family (methane named as an alkane in the equations; the note presupposes the alkane identities/names)
- `NOTE` Halogens & Alkanes  Edexcel IGCSE Chemistry Revision Notes 2017.md — "Alkanes undergo a substitution reaction with halogens in the presence of ultraviolet radiation"
- `NOTE` Halogens & Alkanes  Edexcel IGCSE Chemistry Revision Notes 2017.md — "**methane + bromine → bromomethane + hydrogen bromide**"

```diff
@@ -6907,7 +6907,9 @@ edges:
       as an alkane in the equations; the note presupposes the alkane identities/names)
     upstream: T-C10 HUMAN_VALIDATED 4CH1-4.22 @ Halogens & Alkanes note (2026-09-11)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-25'
   version: 1
   created_at: '2026-09-24'
 - source: 4CH1-CON-ALKANE-HALOGEN-SUBSTITUTION
```

### 3. `4CH1-CON-ALKANE-HALOGEN-SUBSTITUTION REQUIRES_PREREQUISITE 4CH1-CON-ORGANIC-REACTION-CLASSES` [high]

- node 4CH1-CON-ALKANE-HALOGEN-SUBSTITUTION — Alkane substitution reactions with halogens under ultraviolet radiation (CONCEPT)
-   spec 4CH1-4.22 [CORE]: describe the reactions of alkanes with halogens in the presence of ultraviolet radiation, lim...
- node 4CH1-CON-ORGANIC-REACTION-CLASSES — Classifying organic reactions (substitution, addition, combustion) (CONCEPT)
-   spec 4CH1-4.6 [CORE]: understand how to classify reactions of organic compounds as substitution, addition and combu...
- derivation: USED_WITHOUT_RETEACHING — the note opens by referencing the substitution CLASS (the 4.6 owner's definition — 'In a substitution reaction...') and the 4.6 node's own substitution example IS methane+bromine — the same reaction taught as class member first, then as the alkane-specific instance
- `NOTE` Halogens & Alkanes  Edexcel IGCSE Chemistry Revision Notes 2017.md — "In a substitution reaction, one atom is swapped with another atom"
- `NOTE` Classifying Organic Reactions  Edexcel IGCSE Chemistry Revision Notes 2017.md — "A **substitution** reaction takes place when one functional group is replaced by another"

```diff
@@ -6933,7 +6933,9 @@ edges:
       — the same reaction taught as class member first, then as the alkane-specific instance
     upstream: T-C10 HUMAN_VALIDATED 4CH1-4.6/4.22 @ Classifying + Halogens notes (2026-09-11)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-25'
   version: 1
   created_at: '2026-09-24'
 - source: 4CH1-CON-ALKANES
```

### 4. `4CH1-CON-ALKANES REQUIRES_PREREQUISITE 4CH1-CON-HOMOLOGOUS-SERIES` [high]

- node 4CH1-CON-ALKANES — Alkanes (general formula, saturated hydrocarbons, first five members) (CONCEPT)
-   spec 4CH1-4.19 [CORE]: know the general formula for alkanes
-   spec 4CH1-4.20 [CORE]: explain why alkanes are classified as saturated hydrocarbons
-   spec 4CH1-4.21 [CORE]: understand how to draw the structural and displayed formulae for alkanes with up to five carb...
- node 4CH1-CON-HOMOLOGOUS-SERIES — Homologous series and functional groups (CONCEPT)
-   spec 4CH1-4.3 [CORE]: know what is meant by the terms homologous series, functional group and isomerism
- derivation: USED_WITHOUT_RETEACHING — the general formula IS the homologous-series tool (the 'n' ratio apparatus from 4.3/4.2) applied to the alkane family — the note's caption names the table 'members of the alkane homologous series' without re-defining the series concept
- `NOTE` Alkanes  Edexcel IGCSE Chemistry Revision Notes 2017.md — "of the alkanes is **C**<sub><b>n</b></sub>**H**<sub><b>2n+2</b></sub>"
- `NOTE` Alkanes  Edexcel IGCSE Chemistry Revision Notes 2017.md — "**_The first five members of the alkane homologous series_**"

```diff
@@ -6959,7 +6959,9 @@ edges:
       homologous series' without re-defining the series concept
     upstream: T-C10 HUMAN_VALIDATED 4CH1-4.19 @ Alkanes note (2026-09-11)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-25'
   version: 1
   created_at: '2026-09-24'
 - source: 4CH1-CON-ALLOY-HARDNESS
```

### 5. `4CH1-CON-CO-POISONING REQUIRES_PREREQUISITE 4CH1-CON-FUELS-COMBUSTION` [high]

- node 4CH1-CON-CO-POISONING — Why carbon monoxide is poisonous (blood oxygen transport) (CONCEPT)
-   spec 4CH1-4.13 [CORE]: understand why carbon monoxide is poisonous, in terms of its effect on the capacity of blood ...
- node 4CH1-CON-FUELS-COMBUSTION — Fuels and the products of complete and incomplete combustion (CONCEPT)
-   spec 4CH1-4.11 [CORE]: know that a fuel is a substance that, when burned, releases heat energy
-   spec 4CH1-4.12 [CORE]: know the possible products of complete and incomplete combustion of hydrocarbons with oxygen ...
- derivation: EXPLICIT_TEACH_SEQUENCE — the CO section is DEFINED by the incomplete- combustion products surface ('produced during the incomplete combustion') — the note teaches CO's danger as the direct continuation of the combustion-products thread
- `NOTE` Definition of combustion - IGCSE Chemistry Revision Notes.md — "Carbon monoxide (CO) is a highly poisonous gas produced during the incomplete combustion of carbon-containi..."
- `NOTE` Definition of combustion - IGCSE Chemistry Revision Notes.md — "The products of these reactions are unburnt fuel (soot), carbon monoxide and water"

```diff
@@ -7446,7 +7446,9 @@ edges:
       the combustion-products thread
     upstream: T-C10 HUMAN_VALIDATED 4CH1-4.12/4.13 @ Definition of combustion note (2026-09-11)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-25'
   version: 1
   created_at: '2026-09-24'
 - source: 4CH1-CON-CO2-FROM-CARBONATES
```

### 6. `4CH1-CON-CRACKING REQUIRES_PREREQUISITE 4CH1-CON-CRUDE-OIL-FRACTIONS` [high]

- node 4CH1-CON-CRACKING — Catalytic cracking of long-chain fractions (process and why it is necessary) (CONCEPT)
-   spec 4CH1-4.17 [CORE]: describe how long-chain alkanes are converted to alkenes and shorter-chain alkanes by catalyt...
-   spec 4CH1-4.18 [CORE]: explain why cracking is necessary, in terms of the balance between supply and demand for diff...
- node 4CH1-CON-CRUDE-OIL-FRACTIONS — Fractional distillation of crude oil — the fractions, their uses and their trends (CONCEPT)
-   spec 4CH1-4.8 [CORE]: describe how the industrial process of fractional distillation separates crude oil into fract...
-   spec 4CH1-4.9 [CORE]: know the names and uses of the main fractions obtained from crude oil: refinery gases, gasoli...
-   spec 4CH1-4.10 [CORE]: know the trend in colour, boiling point and viscosity of the main fractions
- derivation: EXPLICIT_TEACH_SEQUENCE — cracking operates ON the fractions (the supply/demand section names the surplus fractions cracked into the demanded ones) — the cracking family presupposes the fractions family
- `NOTE` What is cracking - IGCSE Chemistry Revision Notes.md — "The demand for certain fractions outstrips the supply so **cracking** is used to convert excess unwanted fr..."
- `NOTE` What is cracking - IGCSE Chemistry Revision Notes.md — "You can see from the chart that fuel oil and bitumen are surplus fractions so they are cracked and modified..."

```diff
@@ -7683,7 +7683,9 @@ edges:
       fractions cracked into the demanded ones) — the cracking family presupposes the fractions family
     upstream: T-C10 HUMAN_VALIDATED 4CH1-4.17/4.18 @ What is cracking note (2026-09-11)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-25'
   version: 1
   created_at: '2026-09-24'
 - source: 4CH1-CON-CRUDE-OIL
```

### 7. `4CH1-CON-CRUDE-OIL REQUIRES_PREREQUISITE 4CH1-CON-HYDROCARBON` [high]

- node 4CH1-CON-CRUDE-OIL — Crude oil as a mixture of hydrocarbons (CONCEPT)
-   spec 4CH1-4.7 [CORE]: know that crude oil is a mixture of hydrocarbons
- node 4CH1-CON-HYDROCARBON — Hydrocarbon (a compound of hydrogen and carbon only) (CONCEPT)
-   spec 4CH1-4.1 [CORE]: know that a hydrocarbon is a compound of hydrogen and carbon only
- derivation: USED_WITHOUT_RETEACHING — the crude-oil definition is stated IN hydrocarbon vocabulary applied as given ('a mixture of hydrocarbons' — the spec's own wording; the note names the mixture's components without re-defining them)
- `NOTE` Fractional distillation - IGCSE Chemistry Revision Notes.md — "However, the different hydrocarbons that make up the mixture, called fractions, are enormously valuable"
- `NOTE` What is cracking - IGCSE Chemistry Revision Notes.md — "Cracking is an industrial process used to break **low demand, long chain hydrocarbon molecules** into more ..."

```diff
@@ -7711,7 +7711,9 @@ edges:
       re-defining them)
     upstream: T-C10 HUMAN_VALIDATED 4CH1-4.7 @ Fractional distillation note (2026-09-11)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-25'
   version: 1
   created_at: '2026-09-24'
 - source: 4CH1-CON-CRUDE-OIL
```

### 8. `4CH1-CON-CRUDE-OIL REQUIRES_PREREQUISITE 4CH1-CON-MIXTURE` [high]

- node 4CH1-CON-CRUDE-OIL — Crude oil as a mixture of hydrocarbons (CONCEPT)
-   spec 4CH1-4.7 [CORE]: know that crude oil is a mixture of hydrocarbons
- node 4CH1-CON-MIXTURE — Mixture (CONCEPT)
-   spec 4CH1-1.8 [CORE]: understand how to classify a substance as an element, compound or mixture
- derivation: USED_WITHOUT_RETEACHING — SANCTIONED BOUNDARY EDGE (ruling target 5) — 4.7's definition applies the batch-1 mixture concept (not chemically combined, physically separable — which is exactly why the distillation works); the mixture concept is never re-taught
- `NOTE` Fractional distillation - IGCSE Chemistry Revision Notes.md — "Crude oil as a mixture is not a very useful substance"
- `NOTE` Fractional distillation - IGCSE Chemistry Revision Notes.md — "The molecules in each fraction have similar **properties** and **boiling points**"

```diff
@@ -7738,7 +7738,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-4.7 @ Fractional distillation note (2026-09-11); the batch-1
       owner
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-25'
   version: 1
   created_at: '2026-09-24'
 - source: 4CH1-CON-CRUDE-OIL-FRACTIONS
```

### 9. `4CH1-CON-CRUDE-OIL-FRACTIONS REQUIRES_PREREQUISITE 4CH1-CON-CRUDE-OIL` [high]

- node 4CH1-CON-CRUDE-OIL-FRACTIONS — Fractional distillation of crude oil — the fractions, their uses and their trends (CONCEPT)
-   spec 4CH1-4.8 [CORE]: describe how the industrial process of fractional distillation separates crude oil into fract...
-   spec 4CH1-4.9 [CORE]: know the names and uses of the main fractions obtained from crude oil: refinery gases, gasoli...
-   spec 4CH1-4.10 [CORE]: know the trend in colour, boiling point and viscosity of the main fractions
- node 4CH1-CON-CRUDE-OIL — Crude oil as a mixture of hydrocarbons (CONCEPT)
-   spec 4CH1-4.7 [CORE]: know that crude oil is a mixture of hydrocarbons
- derivation: EXPLICIT_TEACH_SEQUENCE — the note's own frame — crude oil (the mixture) is taught first as not-useful, THEN the fractions separated from it are the valuable part; the fractions concept presupposes its source mixture
- `NOTE` Fractional distillation - IGCSE Chemistry Revision Notes.md — "Crude oil as a mixture is not a very useful substance"
- `NOTE` Fractional distillation - IGCSE Chemistry Revision Notes.md — "The fractions in petroleum are separated from each other in a process called **fractional distillation**"

```diff
@@ -7764,7 +7764,9 @@ edges:
       mixture
     upstream: T-C10 HUMAN_VALIDATED 4CH1-4.7/4.8 @ Fractional distillation note (2026-09-11)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-25'
   version: 1
   created_at: '2026-09-24'
 - source: 4CH1-CON-CRUDE-OIL-FRACTIONS
```

### 10. `4CH1-CON-CRUDE-OIL-FRACTIONS REQUIRES_PREREQUISITE 4CH1-CON-FRACTIONAL-DISTILLATION` [high]

- node 4CH1-CON-CRUDE-OIL-FRACTIONS — Fractional distillation of crude oil — the fractions, their uses and their trends (CONCEPT)
-   spec 4CH1-4.8 [CORE]: describe how the industrial process of fractional distillation separates crude oil into fract...
-   spec 4CH1-4.9 [CORE]: know the names and uses of the main fractions obtained from crude oil: refinery gases, gasoli...
-   spec 4CH1-4.10 [CORE]: know the trend in colour, boiling point and viscosity of the main fractions
- node 4CH1-CON-FRACTIONAL-DISTILLATION — Fractional distillation (CONCEPT)
-   spec 4CH1-1.10 [CORE]: describe these experimental techniques for the separation of mixtures:
- derivation: USED_WITHOUT_RETEACHING — SANCTIONED BOUNDARY EDGE (ruling target 1) — the 4.8 industrial separation runs the batch-1 technique (column, temperature gradient, vapourise/condense) applied to petroleum; the technique is never re-defined by the 4.8 note
- `NOTE` Fractional distillation - IGCSE Chemistry Revision Notes.md — "The fractions in petroleum are separated from each other in a process called **fractional distillation**"
- `NOTE` Fractional distillation - IGCSE Chemistry Revision Notes.md — "Fractional distillation is carried out in a **fractionating column** which has a temperature gradient"

```diff
@@ -7792,7 +7792,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-4.8 @ Fractional distillation note (2026-09-11); the batch-1
       owner
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-25'
   version: 1
   created_at: '2026-09-24'
 - source: 4CH1-CON-CRYSTALLISATION
```

### 11. `4CH1-CON-FUELS-COMBUSTION REQUIRES_PREREQUISITE 4CH1-CON-COMBUSTION-O2` [high]

- node 4CH1-CON-FUELS-COMBUSTION — Fuels and the products of complete and incomplete combustion (CONCEPT)
-   spec 4CH1-4.11 [CORE]: know that a fuel is a substance that, when burned, releases heat energy
-   spec 4CH1-4.12 [CORE]: know the possible products of complete and incomplete combustion of hydrocarbons with oxygen ...
- node 4CH1-CON-COMBUSTION-O2 — Combustion of elements in oxygen (magnesium, hydrogen, sulfur) (CONCEPT)
-   spec 4CH1-2.11 [CORE]: describe the combustion of elements in oxygen, including magnesium, hydrogen and sulfur
- derivation: USED_WITHOUT_RETEACHING — SANCTIONED BOUNDARY EDGE (ruling target 4) — the complete/incomplete combustion products presuppose the batch-5 combustion-in-oxygen owner (the oxygen reactant and the burning-as-reaction surface are the owner's, applied as given)
- `NOTE` Definition of combustion - IGCSE Chemistry Revision Notes.md — "Complete combustion occurs when there is **excess oxygen**"
- `NOTE` Classifying Organic Reactions  Edexcel IGCSE Chemistry Revision Notes 2017.md — "This is the scientific term for burning. In a **combustion** reaction, an organic substance reacts with oxy..."

```diff
@@ -8571,7 +8571,9 @@ edges:
       surface are the owner's, applied as given)
     upstream: T-C10 HUMAN_VALIDATED 4CH1-4.11/4.12 @ combustion notes (2026-09-11); the batch-5 owner
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-25'
   version: 1
   created_at: '2026-09-24'
 - source: 4CH1-CON-FUELS-COMBUSTION
```

### 12. `4CH1-CON-FUELS-COMBUSTION REQUIRES_PREREQUISITE 4CH1-CON-CRUDE-OIL-FRACTIONS` [high]

- node 4CH1-CON-FUELS-COMBUSTION — Fuels and the products of complete and incomplete combustion (CONCEPT)
-   spec 4CH1-4.11 [CORE]: know that a fuel is a substance that, when burned, releases heat energy
-   spec 4CH1-4.12 [CORE]: know the possible products of complete and incomplete combustion of hydrocarbons with oxygen ...
- node 4CH1-CON-CRUDE-OIL-FRACTIONS — Fractional distillation of crude oil — the fractions, their uses and their trends (CONCEPT)
-   spec 4CH1-4.8 [CORE]: describe how the industrial process of fractional distillation separates crude oil into fract...
-   spec 4CH1-4.9 [CORE]: know the names and uses of the main fractions obtained from crude oil: refinery gases, gasoli...
-   spec 4CH1-4.10 [CORE]: know the trend in colour, boiling point and viscosity of the main fractions
- derivation: EXPLICIT_TEACH_SEQUENCE — the fuels note EXPLICITLY grounds the fuels in the fractions (obtained from crude oil by fractional distillation; petrol/kerosene/diesel named as the fractions-as-fuels) — the fuels family presupposes the fractions family
- `NOTE` Definition of combustion - IGCSE Chemistry Revision Notes.md — "Non-renewable fossil fuels are obtained from **crude oil** by fractional distillation"
- `NOTE` Definition of combustion - IGCSE Chemistry Revision Notes.md — "Petrol is used as a fuel in **cars**, kerosene is used to fuel **aircraft** and diesel oil is used as a fue..."

```diff
@@ -8598,7 +8598,9 @@ edges:
       family presupposes the fractions family
     upstream: T-C10 HUMAN_VALIDATED 4CH1-4.11 @ Definition of combustion note (2026-09-11)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-25'
   version: 1
   created_at: '2026-09-24'
 - source: 4CH1-CON-G1-PREDICTION
```

### 13. `4CH1-CON-ISOMERS REQUIRES_PREREQUISITE 4CH1-CON-ORGANIC-FORMULAE` [high]

- node 4CH1-CON-ISOMERS — Isomers and drawing possible structures from a molecular formula (CONCEPT)
-   spec 4CH1-4.5 [CORE]: understand how to write the possible structural and displayed formulae of an organic molecule...
- node 4CH1-CON-ORGANIC-FORMULAE — Representing organic molecules (empirical, molecular, general, structural, displayed formulae) (CONCEPT)
-   spec 4CH1-4.2 [CORE]: understand how to represent organic molecules using empirical formulae, molecular formulae, g...
- derivation: USED_WITHOUT_RETEACHING — the isomer definition USES two of the formula types (molecular + displayed) as given — enumerating possible structures for a molecular formula (4.5) presupposes the representation toolkit (4.2); the MS Q1a(i) marking points mark the same two formula types
- `NOTE` Introduction to Organic Chemistry - IGCSE Revision Notes.md — "**Isomers** are compounds that have the same **molecular** formula but different **displayed** formulae"

```diff
@@ -9227,7 +9227,9 @@ edges:
       (4.2); the MS Q1a(i) marking points mark the same two formula types
     upstream: T-C10 HUMAN_VALIDATED 4CH1-4.5 @ Introduction note + the Alkanes MS isomer definition (2026-09-11)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-25'
   version: 1
   created_at: '2026-09-24'
 - source: 4CH1-CON-ISOTOPES
```

### 14. `4CH1-CON-IUPAC-NAMING REQUIRES_PREREQUISITE 4CH1-CON-HOMOLOGOUS-SERIES` [high]

- node 4CH1-CON-IUPAC-NAMING — IUPAC naming of organic compounds (stems and suffixes) (CONCEPT)
-   spec 4CH1-4.4 [CORE]: understand how to name compounds relevant to this specification using the rules of Internatio...
- node 4CH1-CON-HOMOLOGOUS-SERIES — Homologous series and functional groups (CONCEPT)
-   spec 4CH1-4.3 [CORE]: know what is meant by the terms homologous series, functional group and isomerism
- derivation: EXPLICIT_TEACH_SEQUENCE — the naming system's suffix half is DEFINED in terms of the functional-group vocabulary (the stem/suffix table's Family column maps suffixes to alkane/alkene/alcohol families) — without the series/functional-group definitions the suffix rules have no referent
- `NOTE` Naming Organic Compounds  Edexcel IGCSE Chemistry Revision Notes 2017.md — "The suffix tells you what **functional group** is on the compound"
- `NOTE` Introduction to Organic Chemistry - IGCSE Revision Notes.md — "**Functional group:** A group of atoms bonded in a specific arrangement that influences the properties of t..."

```diff
@@ -9277,7 +9277,9 @@ edges:
       the series/functional-group definitions the suffix rules have no referent
     upstream: T-C10 HUMAN_VALIDATED 4CH1-4.3/4.4 @ Introduction/Naming notes (2026-09-11)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-25'
   version: 1
   created_at: '2026-09-24'
 - source: 4CH1-CON-MASS-NUMBER
```

### 15. `4CH1-CON-ORGANIC-FORMULAE REQUIRES_PREREQUISITE 4CH1-CON-EMPIRICAL-FORMULA` [high]

- node 4CH1-CON-ORGANIC-FORMULAE — Representing organic molecules (empirical, molecular, general, structural, displayed formulae) (CONCEPT)
-   spec 4CH1-4.2 [CORE]: understand how to represent organic molecules using empirical formulae, molecular formulae, g...
- node 4CH1-CON-EMPIRICAL-FORMULA — Empirical formula (CONCEPT)
-   spec 4CH1-1.32 [CORE]: know what is meant by the terms empirical formula and molecular formula
-   spec 4CH1-1.33 [CORE]: calculate empirical and molecular formulae from experimental data
- derivation: USED_WITHOUT_RETEACHING — SANCTIONED BOUNDARY EDGE (ruling target 2) — the 4.2 representation toolkit includes the pilot's empirical-formula definition applied to organic molecules; the definition sentence is the owner's surface restated, not re-taught
- `NOTE` Introduction to Organic Chemistry - IGCSE Revision Notes.md — "The **empirical formula** shows the **simplest possible ratio** of the atoms in a molecule"

```diff
@@ -9838,7 +9838,9 @@ edges:
       the owner's surface restated, not re-taught
     upstream: T-C10 HUMAN_VALIDATED 4CH1-4.2 @ Introduction note (2026-09-11); the pilot owner
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-25'
   version: 1
   created_at: '2026-09-24'
 - source: 4CH1-CON-ORGANIC-FORMULAE
```

### 16. `4CH1-CON-ORGANIC-FORMULAE REQUIRES_PREREQUISITE 4CH1-CON-HYDROCARBON` [high]

- node 4CH1-CON-ORGANIC-FORMULAE — Representing organic molecules (empirical, molecular, general, structural, displayed formulae) (CONCEPT)
-   spec 4CH1-4.2 [CORE]: understand how to represent organic molecules using empirical formulae, molecular formulae, g...
- node 4CH1-CON-HYDROCARBON — Hydrocarbon (a compound of hydrogen and carbon only) (CONCEPT)
-   spec 4CH1-4.1 [CORE]: know that a hydrocarbon is a compound of hydrogen and carbon only
- derivation: EXPLICIT_TEACH_SEQUENCE — the note DEFINES the hydrocarbon first ('What is a hydrocarbon?' section) and only then teaches the representation toolkit for those molecules — the representation section's own opening presupposes the defined object
- `NOTE` Introduction to Organic Chemistry - IGCSE Revision Notes.md — "Organic compounds can be represented in a number of ways:"
- `NOTE` Introduction to Organic Chemistry - IGCSE Revision Notes.md — "A compound that contains **only** hydrogen and carbon atoms"

```diff
@@ -9864,7 +9864,9 @@ edges:
       presupposes the defined object
     upstream: T-C10 HUMAN_VALIDATED 4CH1-4.1/4.2 @ Introduction to Organic Chemistry (2026-09-11)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-25'
   version: 1
   created_at: '2026-09-24'
 - source: 4CH1-CON-ORGANIC-FORMULAE
```

### 17. `4CH1-CON-ORGANIC-FORMULAE REQUIRES_PREREQUISITE 4CH1-CON-MOLECULAR-FORMULA` [high]

- node 4CH1-CON-ORGANIC-FORMULAE — Representing organic molecules (empirical, molecular, general, structural, displayed formulae) (CONCEPT)
-   spec 4CH1-4.2 [CORE]: understand how to represent organic molecules using empirical formulae, molecular formulae, g...
- node 4CH1-CON-MOLECULAR-FORMULA — Molecular formula (CONCEPT)
-   spec 4CH1-1.32 [CORE]: know what is meant by the terms empirical formula and molecular formula
-   spec 4CH1-1.33 [CORE]: calculate empirical and molecular formulae from experimental data
- derivation: USED_WITHOUT_RETEACHING — SANCTIONED BOUNDARY EDGE (ruling target 3) — as above for the pilot's molecular-formula owner
- `NOTE` Introduction to Organic Chemistry - IGCSE Revision Notes.md — "The **molecular formula** shows the **actual number** of atoms in a molecule"

```diff
@@ -9885,7 +9885,9 @@ edges:
       owner
     upstream: T-C10 HUMAN_VALIDATED 4CH1-4.2 @ Introduction note (2026-09-11); the pilot owner
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-25'
   version: 1
   created_at: '2026-09-24'
 - source: 4CH1-CON-ORGANIC-REACTION-CLASSES
```

### 18. `4CH1-CON-ORGANIC-REACTION-CLASSES REQUIRES_PREREQUISITE 4CH1-CON-HOMOLOGOUS-SERIES` [high]

- node 4CH1-CON-ORGANIC-REACTION-CLASSES — Classifying organic reactions (substitution, addition, combustion) (CONCEPT)
-   spec 4CH1-4.6 [CORE]: understand how to classify reactions of organic compounds as substitution, addition and combu...
- node 4CH1-CON-HOMOLOGOUS-SERIES — Homologous series and functional groups (CONCEPT)
-   spec 4CH1-4.3 [CORE]: know what is meant by the terms homologous series, functional group and isomerism
- derivation: USED_WITHOUT_RETEACHING — the substitution definition is stated IN functional-group vocabulary ('one functional group is replaced by another') — the classification system presupposes the 4.3 apparatus; the note never re-defines functional group
- `NOTE` Classifying Organic Reactions  Edexcel IGCSE Chemistry Revision Notes 2017.md — "A **substitution** reaction takes place when one functional group is replaced by another"

```diff
@@ -9907,7 +9907,9 @@ edges:
       never re-defines functional group
     upstream: T-C10 HUMAN_VALIDATED 4CH1-4.6 @ Classifying Organic Reactions (2026-09-11)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-25'
   version: 1
   created_at: '2026-09-24'
 - source: 4CH1-CON-PERCENT-YIELD
```

### 19. `4CH1-MIS-KEROSENE-DOUBLE-BONDS REMEDIATED_BY 4CH1-CON-CRUDE-OIL-FRACTIONS` [high]

- node 4CH1-MIS-KEROSENE-DOUBLE-BONDS — Claiming kerosene (a crude-oil fraction) contains double bonds (MISCONCEPTION)
- node 4CH1-CON-CRUDE-OIL-FRACTIONS — Fractional distillation of crude oil — the fractions, their uses and their trends (CONCEPT)
-   spec 4CH1-4.8 [CORE]: describe how the industrial process of fractional distillation separates crude oil into fract...
-   spec 4CH1-4.9 [CORE]: know the names and uses of the main fractions obtained from crude oil: refinery gases, gasoli...
-   spec 4CH1-4.10 [CORE]: know the trend in colour, boiling point and viscosity of the main fractions
- derivation: ASSESSMENT_DOCUMENTED — remediation target = WAP target (the B1-E-25 pattern); the corrective content is the fractions node's own single-bonds sentence — the fractions ARE alkane-dominated
- `NOTE` Fractional distillation - IGCSE Chemistry Revision Notes.md — "Most fractions contain mainly **alkanes**, which are compounds of carbon and hydrogen with only **single** ..."

```diff
@@ -13114,7 +13114,9 @@ edges:
       the fractions node's own single-bonds sentence — the fractions ARE alkane-dominated
     upstream: T-C10 HUMAN_VALIDATED 4CH1-4.10 @ Fractional distillation note (2026-09-11)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-25'
   version: 1
   created_at: '2026-09-24'
 - source: 4CH1-MIS-PRECIPITATE-IN-FILTRATE
```

### 20. `4CH1-MIS-KEROSENE-DOUBLE-BONDS WRONG_ANSWER_PATTERN 4CH1-CON-CRUDE-OIL-FRACTIONS` [high]

- node 4CH1-MIS-KEROSENE-DOUBLE-BONDS — Claiming kerosene (a crude-oil fraction) contains double bonds (MISCONCEPTION)
- node 4CH1-CON-CRUDE-OIL-FRACTIONS — Fractional distillation of crude oil — the fractions, their uses and their trends (CONCEPT)
-   spec 4CH1-4.8 [CORE]: describe how the industrial process of fractional distillation separates crude oil into fract...
-   spec 4CH1-4.9 [CORE]: know the names and uses of the main fractions obtained from crude oil: refinery gases, gasoli...
-   spec 4CH1-4.10 [CORE]: know the trend in colour, boiling point and viscosity of the main fractions
- derivation: ASSESSMENT_DOCUMENTED — the pinned Crude Oil MS Q2b Reject column documents the wrong-answer class against the crude-oil-vs-kerosene comparison question (Q2b's correct differences — viscosity, colour, boiling point — double bonds are REJECTED)
- `MARK_SCHEME` CRUDE_OIL_MS_P2.txt — "Reject references to double bonds in kerosene"
- `MARK_SCHEME` CRUDE_OIL_MS_P2.txt — "larger molecules in crude oil"

```diff
@@ -12487,7 +12487,9 @@ edges:
       point — double bonds are REJECTED)
     upstream: T-C10 HUMAN_VALIDATED 4CH1-4.10 @ Crude Oil MS pin (2026-09-11)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-25'
   version: 1
   created_at: '2026-09-24'
 - source: 4CH1-MIS-PRECIPITATE-IN-FILTRATE
```

## File-level meta hunks (once, for the whole batch)

```diff
@@ -230,8 +230,10 @@ meta:
     remediated_by_edges: 24
     requires_prerequisite_edges: 177
     wrong_answer_pattern_edges: 22
-    promoted_edges: 333
-    human_validated_edges: 333
+    promoted_edges: 353
+    human_validated_edges: 353
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
| `4CH1-CON-ACID-ALKALI-IONS` | Acids as hydrogen-ion sources and alkalis as hydroxide-ion sources in aqueous solution | CONCEPT | 4CH1-2.31 (CORE) | high |
| `4CH1-CON-ACID-RAIN-CAUSES` | Nitrogen oxides and sulfur dioxide as acid-rain causes | CONCEPT | 4CH1-4.14 (CORE); 4CH1-4.16 (CORE) | high |
| `4CH1-CON-ACID-REACTIONS` | Reactions of acids with metals, bases and metal carbonates to form salts | CONCEPT | 4CH1-2.37 (CORE) | high |
| `4CH1-CON-ACTIVATION-ENERGY` | Activation energy (minimum energy for reaction; Ea) | CONCEPT | 4CH1-3.14C (CORE) | high |
| `4CH1-CON-AIR-COMPOSITION` | Composition of dry air (approximate percentages of the four most abundant gases) | CONCEPT | 4CH1-2.9 (CORE) | high |
| `4CH1-CON-ALKANE-HALOGEN-SUBSTITUTION` | Alkane substitution reactions with halogens under ultraviolet radiation | CONCEPT | 4CH1-4.22 (CORE) | high |
| `4CH1-CON-ALKANES` | Alkanes (general formula, saturated hydrocarbons, first five members) | CONCEPT | 4CH1-4.19 (CORE); 4CH1-4.20 (CORE); 4CH1-4.21 (CORE) | high |
| `4CH1-CON-ALLOY-HARDNESS` | Why alloys are harder than pure metals (distorted layers resist sliding) | CONCEPT | 4CH1-2.27C (CORE) | high |
| `4CH1-CON-ALLOYS` | Alloys as mixtures of a metal with other elements | CONCEPT | 4CH1-2.26C (CORE) | high |
| `4CH1-CON-ANION-TESTS` | Tests for aqueous anions (halides, sulfate, carbonate) | CONCEPT | 4CH1-2.48 (CORE) | high |
| `4CH1-CON-ANODE-CATHODE` | Anions and cations (negative and positive ions) and their migration to cathode and anode | CONCEPT | 4CH1-1.57C (CORE) | high |
| `4CH1-CON-AQUEOUS-DISCHARGE` | Selective discharge in aqueous electrolysis (halide preference at the anode; hydrogen vs metal at the cathode) | CONCEPT | 4CH1-1.58C (CORE) | high |
| `4CH1-CON-AR` | Relative atomic mass (Ar) | CONCEPT | 4CH1-1.26 (CORE); 4CH1-1.28 (CORE) | high |
| `4CH1-CON-ATOM` | Atom (definition and subatomic composition) | CONCEPT | 4CH1-1.14 (CORE) | high |
| `4CH1-CON-ATOMIC-NUMBER` | Atomic number | CONCEPT | 4CH1-1.16 (CORE) | high |
| `4CH1-CON-AVOGADRO-CONST` | Avogadro constant | CONCEPT | 4CH1-1.27 (ENRICHMENT) | high |
| `4CH1-CON-AVOGADRO-LAW` | Avogadro's Law | CONCEPT | 4CH1-1.35C (ENRICHMENT) | high |
| `4CH1-CON-BASES-ALKALIS` | Bases and alkalis (metal oxides/hydroxides/ammonia as bases; alkalis = soluble bases) | CONCEPT | 4CH1-2.38 (CORE) | high |
| `4CH1-CON-BOND-BREAKING-MAKING` | Bond-breaking endothermic, bond-making exothermic | CONCEPT | 4CH1-3.6C (CORE) | high |
| `4CH1-CON-BOND-ENERGY-CALC` | Bond energy calculations (enthalpy change from bond energies) | CONCEPT | 4CH1-3.7C (CORE) | high |
| `4CH1-CON-CALORIMETRY` | Simple calorimetry experiments (reactions in solution and combustion) | CONCEPT | 4CH1-3.2 (CORE) | high |
| `4CH1-CON-CATALYST` | Catalysts (increase rate, chemically unchanged; alternative pathway at lower activation energy) | CONCEPT | 4CH1-3.12 (CORE); 4CH1-3.13 (CORE) | high |
| `4CH1-CON-CATION-TESTS` | Tests for aqueous cations (sodium hydroxide precipitate colours; ammonium ion via ammonia gas) | CONCEPT | 4CH1-2.47 (CORE) | high |
| `4CH1-CON-CHROMATOGRAM-INTERPRETATION` | Interpreting chromatograms | CONCEPT | 4CH1-1.11 (CORE) | high |
| `4CH1-CON-CHROMATOGRAPHY` | Paper chromatography (separation by differential solubility) | CONCEPT | 4CH1-1.10 (CORE) | high |
| `4CH1-CON-CO-POISONING` | Why carbon monoxide is poisonous (blood oxygen transport) | CONCEPT | 4CH1-4.13 (CORE) | high |
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
| `4CH1-CON-CRACKING` | Catalytic cracking of long-chain fractions (process and why it is necessary) | CONCEPT | 4CH1-4.17 (CORE); 4CH1-4.18 (CORE) | high |
| `4CH1-CON-CRUDE-OIL` | Crude oil as a mixture of hydrocarbons | CONCEPT | 4CH1-4.7 (CORE) | high |
| `4CH1-CON-CRUDE-OIL-FRACTIONS` | Fractional distillation of crude oil — the fractions, their uses and their trends | CONCEPT | 4CH1-4.8 (CORE); 4CH1-4.9 (CORE); 4CH1-4.10 (CORE) | high |
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
| `4CH1-CON-EXTRACTION-EVALUATION` | Commenting on a metal extraction process from given information | CONCEPT | 4CH1-2.24C (CORE) | high |
| `4CH1-CON-EXTRACTION-METHOD` | Extraction method related to reactivity-series position (electrolysis above carbon; carbon reduction below) | CONCEPT | 4CH1-2.23C (CORE) | high |
| `4CH1-CON-FILTRATION` | Filtration | CONCEPT | 4CH1-1.10 (CORE) | high |
| `4CH1-CON-FLAME-TEST` | Flame tests for metal cations (technique and flame colours) | CONCEPT | 4CH1-2.45 (CORE); 4CH1-2.46 (CORE) | high |
| `4CH1-CON-FRACTIONAL-DISTILLATION` | Fractional distillation | CONCEPT | 4CH1-1.10 (CORE) | high |
| `4CH1-CON-FUELS-COMBUSTION` | Fuels and the products of complete and incomplete combustion | CONCEPT | 4CH1-4.11 (CORE); 4CH1-4.12 (CORE) | high |
| `4CH1-CON-G1-FAMILY-EVIDENCE` | Group 1 water-reaction similarities as family evidence (alkali metals) | CONCEPT | 4CH1-2.1 (CORE) | high |
| `4CH1-CON-G1-PREDICTION` | Predicting alkali-metal properties from Group 1 trends | CONCEPT | 4CH1-2.3 (CORE) | high |
| `4CH1-CON-G1-REACTIVITY-ECONFIG` | Group 1 reactivity trend explained by electronic configurations | CONCEPT | 4CH1-2.4C (CORE) | high |
| `4CH1-CON-G1-TREND` | Group 1 reactivity trend from air/water reaction differences | CONCEPT | 4CH1-2.2 (CORE) | high |
| `4CH1-CON-G7-DISPLACEMENT` | Halogen displacement reactions (evidence for the Group 7 reactivity trend) | CONCEPT | 4CH1-2.7 (CORE) | high |
| `4CH1-CON-G7-PREDICTION` | Predicting halogen properties from Group 7 trends (metal and non-metal halides) | CONCEPT | 4CH1-2.6 (CORE) | high |
| `4CH1-CON-G7-PROPERTIES` | Halogen colours, states and physical-property trends (Group 7) | CONCEPT | 4CH1-2.5 (CORE) | high |
| `4CH1-CON-G7-REACTIVITY-ECONFIG` | Group 7 reactivity trend explained by electronic configurations | CONCEPT | 4CH1-2.8C (CORE) | high |
| `4CH1-CON-GAS-TESTS` | Chemical tests for gases (hydrogen, oxygen, carbon dioxide, ammonia, chlorine) | CONCEPT | 4CH1-2.44 (CORE) | high |
| `4CH1-CON-GAS-VOL-CALC` | Gas volume calculation | CONCEPT | 4CH1-1.35C (CORE) | high |
| `4CH1-CON-GIANT-COVALENT` | Giant covalent structures (solids with high melting and boiling points) | CONCEPT | 4CH1-1.49 (CORE) | high |
| `4CH1-CON-GROUP-SIMILARITY` | Why elements in the same group have similar chemical properties | CONCEPT | 4CH1-1.23 (CORE) | high |
| `4CH1-CON-HEAT-CALC` | Heat energy change calculation (Q = mcΔT) | CONCEPT | 4CH1-3.3 (CORE) | high |
| `4CH1-CON-HEATING-CONSTANT-MASS` | Heating to constant mass | CONCEPT | 4CH1-1.7C (ENRICHMENT) | high |
| `4CH1-CON-HOMOLOGOUS-SERIES` | Homologous series and functional groups | CONCEPT | 4CH1-4.3 (CORE) | high |
| `4CH1-CON-HYDROCARBON` | Hydrocarbon (a compound of hydrogen and carbon only) | CONCEPT | 4CH1-4.1 (CORE) | high |
| `4CH1-CON-INDICATORS` | Indicators for distinguishing acidic and alkaline solutions (litmus, phenolphthalein, methyl orange) | CONCEPT | 4CH1-2.28 (CORE) | high |
| `4CH1-CON-ION` | Ion (formation by electron loss or gain) | CONCEPT | 4CH1-1.37 (CORE) | high |
| `4CH1-CON-ION-CHARGE-RULES` | Common ion charges (group-based and named-ion table, with the deduction rule) | CONCEPT | 4CH1-1.38 (CORE) | high |
| `4CH1-CON-IONIC-BOND` | Ionic bonding (electrostatic attraction between oppositely charged ions) | CONCEPT | 4CH1-1.41 (CORE) | high |
| `4CH1-CON-IONIC-CONDUCTION` | Ionic conduction (solid insulator; molten and aqueous conductor via mobile ions) | CONCEPT | 4CH1-1.43 (CORE); 4CH1-1.56C (CORE) | high |
| `4CH1-CON-IONIC-FORMULA` | Writing formulae for ionic compounds (charge cancellation and swap-and-drop) | CONCEPT | 4CH1-1.39 (CORE) | high |
| `4CH1-CON-IONIC-LATTICE` | Giant ionic lattice and why ionic compounds have high melting and boiling points | CONCEPT | 4CH1-1.42 (CORE) | high |
| `4CH1-CON-ISOMERS` | Isomers and drawing possible structures from a molecular formula | CONCEPT | 4CH1-4.5 (CORE) | high |
| `4CH1-CON-ISOTOPES` | Isotopes and relative atomic mass from isotopic abundances | CONCEPT | 4CH1-1.16 (CORE); 4CH1-1.17 (CORE) | high |
| `4CH1-CON-IUPAC-NAMING` | IUPAC naming of organic compounds (stems and suffixes) | CONCEPT | 4CH1-4.4 (CORE) | high |
| `4CH1-CON-MASS-NUMBER` | Mass number | CONCEPT | 4CH1-1.16 (CORE) | high |
| `4CH1-CON-METAL-DISPLACEMENT` | Metal displacement reactions as reactivity-series evidence (metal + metal oxide; metal + salt solution) | CONCEPT | 4CH1-2.16 (CORE) | high |
| `4CH1-CON-METAL-NONMETAL` | Classifying elements as metals or non-metals (by properties and by Periodic Table position) | CONCEPT | 4CH1-1.20 (CORE); 4CH1-1.21 (CORE) | high |
| `4CH1-CON-METAL-PROPERTIES` | Typical physical properties of metals (electrical conductivity and malleability) and their explanations | CONCEPT | 4CH1-1.54C (CORE) | high |
| `4CH1-CON-METAL-USES` | Uses of aluminium, copper, iron and steel explained by their properties | CONCEPT | 4CH1-2.25C (CORE) | high |
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
| `4CH1-CON-NEUTRALISATION` | Neutralisation (alkalis neutralise acids; H+ + OH- -> water) | CONCEPT | 4CH1-2.32 (CORE) | high |
| `4CH1-CON-NOBLE-GAS-INERTNESS` | Why the noble gases (Group 0) do not readily react | CONCEPT | 4CH1-1.24 (CORE) | high |
| `4CH1-CON-O2-PERCENT-DETERMINATION` | Determining the percentage of oxygen in air (metal and non-metal routes) | CONCEPT | 4CH1-2.10 (CORE) | high |
| `4CH1-CON-ORES` | Ores and native (uncombined) metals as sources of metals | CONCEPT | 4CH1-2.22C (CORE) | high |
| `4CH1-CON-ORGANIC-FORMULAE` | Representing organic molecules (empirical, molecular, general, structural, displayed formulae) | CONCEPT | 4CH1-4.2 (CORE) | high |
| `4CH1-CON-ORGANIC-REACTION-CLASSES` | Classifying organic reactions (substitution, addition, combustion) | CONCEPT | 4CH1-4.6 (CORE) | high |
| `4CH1-CON-OX-RED-AGENTS` | Oxidation, reduction, oxidising and reducing agents (oxygen and electron frameworks) | CONCEPT | 4CH1-2.20 (CORE) | high |
| `4CH1-CON-PERCENT-YIELD` | Percentage yield | CONCEPT | 4CH1-1.30 (CORE) | high |
| `4CH1-CON-PERIODIC-TABLE` | Periodic Table arrangement (atomic-number order, groups and periods) | CONCEPT | 4CH1-1.18 (CORE) | high |
| `4CH1-CON-PH-SCALE` | The pH scale 0-14 and the acidity/alkalinity classification bands | CONCEPT | 4CH1-2.29 (CORE) | high |
| `4CH1-CON-PROTON-TRANSFER` | Acids and bases as proton transfer (donor and acceptor) | CONCEPT | 4CH1-2.35 (CORE); 4CH1-2.36 (CORE) | high |
| `4CH1-CON-PURE-SUBSTANCE` | Pure substance (chemical sense) and fixed melting/boiling points | CONCEPT | 4CH1-1.9 (CORE) | high |
| `4CH1-CON-RATE-EXPERIMENTS` | Rate-of-reaction experiments (gas collection, disappearing cross, timing methods) | CONCEPT | 4CH1-3.9 (CORE) | high |
| `4CH1-CON-RATE-FACTORS` | Factors affecting the rate of reaction (surface area, concentration and pressure, temperature, catalyst) | CONCEPT | 4CH1-3.10 (CORE) | high |
| `4CH1-CON-REACT-ARRANGE` | Arranging metals into a reactivity series from water and dilute-acid reactions | CONCEPT | 4CH1-2.15 (CORE) | high |
| `4CH1-CON-REACT-ORDER` | The order of reactivity of the named metals (K to Au) | CONCEPT | 4CH1-2.17 (CORE) | high |
| `4CH1-CON-REACTING-MASS` | Reacting mass calculation | CONCEPT | 4CH1-1.29 (CORE) | high |
| `4CH1-CON-REACTION-PROFILE` | Reaction profile diagrams (showing ΔH and activation energy) | CONCEPT | 4CH1-3.14C (CORE) | high |
| `4CH1-CON-REDOX-ELECTRONS` | Oxidation and reduction in terms of electron loss and gain | CONCEPT | 4CH1-1.59C (CORE) | high |
| `4CH1-CON-REVERSIBLE` | Reversible reactions and the ⇌ notation | CONCEPT | 4CH1-3.17 (CORE) | high |
| `4CH1-CON-REVERSIBLE-EXAMPLES` | Named reversible reactions (ammonium chloride; hydrated copper(II) sulfate) | CONCEPT | 4CH1-3.18 (CORE) | high |
| `4CH1-CON-RF-VALUE` | Retention factor (Rf) | CONCEPT | 4CH1-1.12 (CORE) | high |
| `4CH1-CON-RUST-PREVENTION` | Preventing rusting (barrier methods, sacrificial protection, galvanising) | CONCEPT | 4CH1-2.19 (CORE) | high |
| `4CH1-CON-RUSTING` | Rusting of iron (both oxygen and water required; the control-tube investigation) | CONCEPT | 4CH1-2.18 (CORE) | high |
| `4CH1-CON-SALT-INSOLUBLE-REACTANT` | Preparing a pure, dry soluble salt from an insoluble reactant (excess-base route) | CONCEPT | 4CH1-2.39 (CORE) | high |
| `4CH1-CON-SALT-PRECIPITATION` | Preparing a pure, dry insoluble salt from two soluble reactants (precipitation) | CONCEPT | 4CH1-2.41C (CORE) | high |
| `4CH1-CON-SALT-TITRATION-ROUTE` | Preparing a pure, dry soluble salt from an acid and alkali (titration route) | CONCEPT | 4CH1-2.40C (CORE) | high |
| `4CH1-CON-SATURATED-SOLUTION` | Saturated solution | CONCEPT | 4CH1-1.4 (CORE); 4CH1-1.10 (SUPPORTING) | high |
| `4CH1-CON-SIMPLE-DISTILLATION` | Simple distillation | CONCEPT | 4CH1-1.10 (CORE) | high |
| `4CH1-CON-SIMPLE-MOLECULAR` | Simple molecular structures (weak intermolecular forces; low melting and boiling points; the relative-molecular-mass trend) | CONCEPT | 4CH1-1.47 (CORE); 4CH1-1.48 (CORE) | high |
| `4CH1-CON-SOLUBILITY` | Solubility (g per 100 g of solvent) | CONCEPT | 4CH1-1.5C (CORE) | high |
| `4CH1-CON-SOLUBILITY-CURVE` | Solubility curves (plotting and interpreting) | CONCEPT | 4CH1-1.6C (CORE) | high |
| `4CH1-CON-SOLUBILITY-RULES` | Solubility rules for ionic compounds in water (the salt-preparation method-selection frame) | CONCEPT | 4CH1-2.34 (CORE) | high |
| `4CH1-CON-SOLUTION` | Solution, solute and solvent | CONCEPT | 4CH1-1.4 (CORE) | high |
| `4CH1-CON-STATE-CHANGES` | Interconversions between the three states (melting, freezing, boiling, condensation, sublimation) | CONCEPT | 4CH1-1.2 (CORE) | high |
| `4CH1-CON-STATE-PARTICLE-MODEL` | Particle arrangement, movement and energy in the three states | CONCEPT | 4CH1-1.1 (CORE); 4CH1-1.3 (SUPPORTING) | high |
| `4CH1-CON-STATES-THREE` | The three states of matter (solid, liquid, gas) | CONCEPT | 4CH1-1.1 (CORE) | high |
| `4CH1-CON-SUBATOMIC-PARTICLES` | Subatomic particles (proton, neutron, electron — positions, relative masses, relative charges) | CONCEPT | 4CH1-1.15 (CORE) | high |
| `4CH1-CON-THEOR-YIELD` | Theoretical yield | CONCEPT | 4CH1-1.30 (CORE) | high |
| `4CH1-CON-TITRATION` | Acid-alkali titration technique (pipette, burette, endpoint, concordant titres) | CONCEPT | 4CH1-2.33C (CORE) | high |
| `4CH1-CON-UNIVERSAL-INDICATOR` | Universal indicator as approximate pH measurement (colour-chart matching) | CONCEPT | 4CH1-2.30 (CORE) | high |
| `4CH1-CON-VOL-CONVERSION` | Volume unit conversion (cm3/dm3) | CONCEPT | 4CH1-1.34C (CORE) | high |
| `4CH1-CON-WATER-CRYST` | Water of crystallisation and hydrated salts | CONCEPT | 4CH1-1.31 (CORE) | high |
| `4CH1-CON-WATER-CUSO4-TEST` | Chemical test for water (anhydrous copper(II) sulfate turns white to blue) | CONCEPT | 4CH1-2.49 (CORE) | high |
| `4CH1-CON-WATER-PURITY-TEST` | Physical test for water purity (boiling point exactly 100 C) | CONCEPT | 4CH1-2.50 (CORE) | high |
| `4CH1-CON-YIELD` | Yield (actual yield) | CONCEPT | 4CH1-1.30 (CORE) | high |
| `4CH1-CON-YIELD-FACTORS` | Factors reducing yield | CONCEPT | 4CH1-1.30 (ENRICHMENT) | high |
| `4CH1-MIS-BOND-ENERGY-COUNT` | Counting the wrong number or type of bonds in bond-energy calculations (ignoring balancing numbers) | MISCONCEPTION |  | medium |
| `4CH1-MIS-CATALYST-PARTICLE-ENERGY` | Explaining a catalyst's effect as particles gaining energy or moving more quickly | MISCONCEPTION |  | high |
| `4CH1-MIS-CONC-UNIT` | Failing to convert cm3 to dm3 in concentration calculations | MISCONCEPTION |  | high |
| `4CH1-MIS-COVALENT-BONDS-BROKEN` | Saying covalent bonds are broken when simple molecular substances melt or boil (instead of weak intermolecular forces) | MISCONCEPTION |  | high |
| `4CH1-MIS-CRYSTALLISATION-DRYNESS` | Obtaining crystals by evaporating to dryness | MISCONCEPTION |  | high |
| `4CH1-MIS-CUO-COLOUR` | Stating a colour other than black for the copper(II) oxide decomposition product | MISCONCEPTION |  | high |
| `4CH1-MIS-ENDPOINT-PH-ABOVE-7` | Identifying complete neutralisation as the pH changing to any value above 7 (instead of the temperature maximum / pH reaching 7) | MISCONCEPTION |  | high |
| `4CH1-MIS-ENTHALPY-UNIT-J` | Quoting the molar enthalpy change as the unconverted joule value (e.g. 50 000) instead of kilojoules | MISCONCEPTION |  | high |
| `4CH1-MIS-EQ-PRESSURE-FEWER` | Predicting that a pressure change shifts equilibrium to the side with fewer gas molecules in the wrong direction | MISCONCEPTION |  | medium |
| `4CH1-MIS-EQ-SUBSCRIPT` | Balancing equations by altering subscripts | MISCONCEPTION |  | high |
| `4CH1-MIS-EQ-TEMP-EXO` | Predicting that raising the temperature shifts equilibrium in the exothermic direction | MISCONCEPTION |  | high |
| `4CH1-MIS-G1-SHELL-EXPLANATION` | Explaining Group 1 reactivity via more shells / larger radius / shielding instead of outer-electron distance and weaker attraction | MISCONCEPTION |  | high |
| `4CH1-MIS-GAS-PARTICLES-TOUCH` | Drawing gas particles touching each other or joined by bonds | MISCONCEPTION |  | high |
| `4CH1-MIS-GLOWING-SPLINT-HYDROGEN` | Testing for hydrogen with a glowing splint or an unflamed splint, or naming only the squeaky pop (instead of a burning splint at the tube mouth) | MISCONCEPTION |  | high |
| `4CH1-MIS-GRAPHITE-LAYER-BONDS` | Saying graphite layers are held together by bonds (instead of weak forces of attraction between the layers) | MISCONCEPTION |  | high |
| `4CH1-MIS-HALIDE-TEST-HCL` | Acidifying the halide test with hydrochloric acid (instead of nitric acid) | MISCONCEPTION |  | high |
| `4CH1-MIS-HALOGEN-HALIDE` | Treating a halogen and its halide ion as having the same (or different) reactivity in displacement reasoning | MISCONCEPTION |  | high |
| `4CH1-MIS-ION-OXIDE-REASONING` | Explaining a metal-oxide displacement outcome by references to ions and oxides instead of the reactivity comparison | MISCONCEPTION |  | high |
| `4CH1-MIS-IONIC-BOND-ATOMS` | Describing ionic bonding as attraction between atoms or molecules (or as intermolecular forces) | MISCONCEPTION |  | high |
| `4CH1-MIS-IONIC-CONDUCTION-ELECTRONS` | Believing ionic compounds conduct electricity because electrons move and carry the charge | MISCONCEPTION |  | high |
| `4CH1-MIS-ISOTOPES-DIFFER-PROTONS` | Believing isotopes of an element differ in their number of protons | MISCONCEPTION |  | high |
| `4CH1-MIS-KEROSENE-DOUBLE-BONDS` | Claiming kerosene (a crude-oil fraction) contains double bonds | MISCONCEPTION |  | high |
| `4CH1-MIS-PRECIPITATE-IN-FILTRATE` | Recovering the insoluble salt from the filtrate instead of the residue in a precipitation preparation | MISCONCEPTION |  | high |
| `4CH1-MIS-RAM-MASS-NUMBER` | Calling the Periodic Table relative atomic mass the mass number | MISCONCEPTION |  | high |

