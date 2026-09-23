# C11 Diff Review Bundle — pending §18 edge promotions (generated 2026-09-23)

- baseline commit: `d6eba2d`
- state fingerprint: `7e090e09c8a5` (promo_count=187)
- actionable: 19 edges (clean 19 / pending-flagged 0); not-actionable: 5; nodes awaiting a pathway: 157
- preview fidelity: simulator re-emits graph/igcse-chemistry/concept_edges under the generator's own serialization contract with a byte-identity guard — what you read is what G13 will write.

## Batch approval

```bash
cd work/syllabai-resources && python3 scripts/c11_diff_review.py approve \
  '4CH1-CON-ACID-REACTIONS REQUIRES_PREREQUISITE 4CH1-CON-NEUTRALISATION' \
  '4CH1-CON-ACID-REACTIONS REQUIRES_PREREQUISITE 4CH1-CON-REACT-ORDER' \
  '4CH1-CON-BASES-ALKALIS REQUIRES_PREREQUISITE 4CH1-CON-NEUTRALISATION' \
  '4CH1-CON-NEUTRALISATION REQUIRES_PREREQUISITE 4CH1-CON-ACID-ALKALI-IONS' \
  '4CH1-CON-PROTON-TRANSFER REQUIRES_PREREQUISITE 4CH1-CON-ACID-ALKALI-IONS' \
  '4CH1-CON-SALT-INSOLUBLE-REACTANT REQUIRES_PREREQUISITE 4CH1-CON-ACID-REACTIONS' \
  '4CH1-CON-SALT-INSOLUBLE-REACTANT REQUIRES_PREREQUISITE 4CH1-CON-SOLUBILITY-RULES' \
  '4CH1-CON-SALT-PRECIPITATION REQUIRES_PREREQUISITE 4CH1-CON-SOLUBILITY-RULES' \
  '4CH1-CON-SALT-TITRATION-ROUTE REQUIRES_PREREQUISITE 4CH1-CON-TITRATION' \
  '4CH1-CON-SOLUBILITY-RULES REQUIRES_PREREQUISITE 4CH1-CON-ION-CHARGE-RULES' \
  '4CH1-CON-TITRATION REQUIRES_PREREQUISITE 4CH1-CON-INDICATORS' \
  '4CH1-CON-TITRATION REQUIRES_PREREQUISITE 4CH1-CON-NEUTRALISATION' \
  '4CH1-CON-UNIVERSAL-INDICATOR REQUIRES_PREREQUISITE 4CH1-CON-PH-SCALE' \
  '4CH1-MIS-ENDPOINT-PH-ABOVE-7 REMEDIATED_BY 4CH1-CON-NEUTRALISATION' \
  '4CH1-MIS-ENDPOINT-PH-ABOVE-7 WRONG_ANSWER_PATTERN 4CH1-CON-NEUTRALISATION' \
  '4CH1-MIS-PRECIPITATE-IN-FILTRATE REMEDIATED_BY 4CH1-CON-SALT-PRECIPITATION' \
  '4CH1-MIS-PRECIPITATE-IN-FILTRATE WRONG_ANSWER_PATTERN 4CH1-CON-SALT-PRECIPITATION' \
  '4CH1-PR-07 REQUIRES_PREREQUISITE 4CH1-CON-SALT-INSOLUBLE-REACTANT' \
  '4CH1-PR-08 REQUIRES_PREREQUISITE 4CH1-CON-SALT-PRECIPITATION' \
  --by <operator> --date 2026-09-23 --review-ref graph/reports/C11_DIFF_REVIEW_B7_2026-09-23.md
```

Pending-flagged (PENDING operator_decision) edges are excluded from the command above; approving them additionally requires `--include-pending` — that flag records the explicit decision this bundle presents.

## Index

| # | identity | confidence | flag |
|---|----------|------------|------|
| 1 | `4CH1-CON-ACID-REACTIONS REQUIRES_PREREQUISITE 4CH1-CON-NEUTRALISATION` | high |  |
| 2 | `4CH1-CON-ACID-REACTIONS REQUIRES_PREREQUISITE 4CH1-CON-REACT-ORDER` | high |  |
| 3 | `4CH1-CON-BASES-ALKALIS REQUIRES_PREREQUISITE 4CH1-CON-NEUTRALISATION` | high |  |
| 4 | `4CH1-CON-NEUTRALISATION REQUIRES_PREREQUISITE 4CH1-CON-ACID-ALKALI-IONS` | high |  |
| 5 | `4CH1-CON-PROTON-TRANSFER REQUIRES_PREREQUISITE 4CH1-CON-ACID-ALKALI-IONS` | high |  |
| 6 | `4CH1-CON-SALT-INSOLUBLE-REACTANT REQUIRES_PREREQUISITE 4CH1-CON-ACID-REACTIONS` | high |  |
| 7 | `4CH1-CON-SALT-INSOLUBLE-REACTANT REQUIRES_PREREQUISITE 4CH1-CON-SOLUBILITY-RULES` | high |  |
| 8 | `4CH1-CON-SALT-PRECIPITATION REQUIRES_PREREQUISITE 4CH1-CON-SOLUBILITY-RULES` | high |  |
| 9 | `4CH1-CON-SALT-TITRATION-ROUTE REQUIRES_PREREQUISITE 4CH1-CON-TITRATION` | high |  |
| 10 | `4CH1-CON-SOLUBILITY-RULES REQUIRES_PREREQUISITE 4CH1-CON-ION-CHARGE-RULES` | high |  |
| 11 | `4CH1-CON-TITRATION REQUIRES_PREREQUISITE 4CH1-CON-INDICATORS` | high |  |
| 12 | `4CH1-CON-TITRATION REQUIRES_PREREQUISITE 4CH1-CON-NEUTRALISATION` | high |  |
| 13 | `4CH1-CON-UNIVERSAL-INDICATOR REQUIRES_PREREQUISITE 4CH1-CON-PH-SCALE` | high |  |
| 14 | `4CH1-MIS-ENDPOINT-PH-ABOVE-7 REMEDIATED_BY 4CH1-CON-NEUTRALISATION` | high |  |
| 15 | `4CH1-MIS-ENDPOINT-PH-ABOVE-7 WRONG_ANSWER_PATTERN 4CH1-CON-NEUTRALISATION` | high |  |
| 16 | `4CH1-MIS-PRECIPITATE-IN-FILTRATE REMEDIATED_BY 4CH1-CON-SALT-PRECIPITATION` | high |  |
| 17 | `4CH1-MIS-PRECIPITATE-IN-FILTRATE WRONG_ANSWER_PATTERN 4CH1-CON-SALT-PRECIPITATION` | high |  |
| 18 | `4CH1-PR-07 REQUIRES_PREREQUISITE 4CH1-CON-SALT-INSOLUBLE-REACTANT` | high |  |
| 19 | `4CH1-PR-08 REQUIRES_PREREQUISITE 4CH1-CON-SALT-PRECIPITATION` | high |  |

## Pending items — the exact diff each approval applies

### 1. `4CH1-CON-ACID-REACTIONS REQUIRES_PREREQUISITE 4CH1-CON-NEUTRALISATION` [high]

- node 4CH1-CON-ACID-REACTIONS — Reactions of acids with metals, bases and metal carbonates to form salts (CONCEPT)
-   spec 4CH1-2.37 [CORE]: describe the reactions of hydrochloric acid, sulfuric acid and nitric acid with metals, bases...
- node 4CH1-CON-NEUTRALISATION — Neutralisation (alkalis neutralise acids; H+ + OH- -> water) (CONCEPT)
-   spec 4CH1-2.32 [CORE]: know that alkalis can neutralise acids
- derivation: DEFINITIONAL_DEPENDENCY — The acid+base row of 2.37 is CLASSIFIED as neutralisation ("a neutralisation reaction occurs") — the 2.32 concept organizes the row (and the note's own scope limit distinguishes it from the metal/carbonate rows).
- `NOTE` Reactions of acids - IGCSE Chemistry Revision Notes.md — "When an acid reacts with a base, a neutralisation reaction occurs"
- `NOTE` Reactions of acids - IGCSE Chemistry Revision Notes.md — "In all acid-base neutralisation reactions, a salt and water are produced"

```diff
@@ -5680,7 +5680,9 @@ edges:
       the metal/carbonate rows).
     upstream: T-C10 HUMAN_VALIDATED 4CH1-2.37/2.32 (2026-09-11)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-23'
   version: 1
   created_at: '2026-09-23'
 - source: 4CH1-CON-ACID-REACTIONS
```

### 2. `4CH1-CON-ACID-REACTIONS REQUIRES_PREREQUISITE 4CH1-CON-REACT-ORDER` [high]

- node 4CH1-CON-ACID-REACTIONS — Reactions of acids with metals, bases and metal carbonates to form salts (CONCEPT)
-   spec 4CH1-2.37 [CORE]: describe the reactions of hydrochloric acid, sulfuric acid and nitric acid with metals, bases...
- node 4CH1-CON-REACT-ORDER — The order of reactivity of the named metals (K to Au) (CONCEPT)
-   spec 4CH1-2.17 [CORE]: know the order of reactivity of these metals: potassium, sodium, lithium, calcium, magnesium,...
- derivation: USED_WITHOUT_RETEACHING — SANCTIONED BOUNDARY EDGE (the session-59 ruling, target 1 — the batch-6 CON-REACT-ORDER owner): the 2.37 acid-metal row APPLIES the reactivity-series placement as given (above-hydrogen rule, the vigour gradient) without re-teaching the series — the ruling's "reactivity series" disposition. The target is the ORDER owner, not CON-REACT-ARRANGE (the note uses the placement, not the arrangement method).
- `NOTE` Reactions of acids - IGCSE Chemistry Revision Notes.md — "Only metals above hydrogen in the reactivity series will react with dilute acids"
- `NOTE` Reactions of acids - IGCSE Chemistry Revision Notes.md — "Metals that are placed high on the reactivity series such as potassium and sodium are very dangerous and re..."

```diff
@@ -5709,7 +5709,9 @@ edges:
       method).'
     upstream: T-C10 HUMAN_VALIDATED 4CH1-2.37 (2026-09-11); the batch-6 record (CON-REACT-ORDER, 2.17)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-23'
   version: 1
   created_at: '2026-09-23'
 - source: 4CH1-CON-ALLOY-HARDNESS
```

### 3. `4CH1-CON-BASES-ALKALIS REQUIRES_PREREQUISITE 4CH1-CON-NEUTRALISATION` [high]

- node 4CH1-CON-BASES-ALKALIS — Bases and alkalis (metal oxides/hydroxides/ammonia as bases; alkalis = soluble bases) (CONCEPT)
-   spec 4CH1-2.38 [CORE]: know that metal oxides, metal hydroxides and ammonia can act as bases, and that alkalis are b...
- node 4CH1-CON-NEUTRALISATION — Neutralisation (alkalis neutralise acids; H+ + OH- -> water) (CONCEPT)
-   spec 4CH1-2.32 [CORE]: know that alkalis can neutralise acids
- derivation: DEFINITIONAL_DEPENDENCY — The 2.38 base DEFINITION is stated through neutralisation ("substances which can neutralise an acid") — the concept presupposes the 2.32 frame it is defined by.
- `NOTE` Bases and alkalis - IGCSE Chemistry Revision Notes.md — "Bases are substances which can neutralise an acid, forming a salt and water"
- `NOTE` Bases and alkalis - IGCSE Chemistry Revision Notes.md — "So, all alkalis are bases, but not all bases are alkalis"

```diff
@@ -5862,7 +5862,9 @@ edges:
       neutralise an acid") — the concept presupposes the 2.32 frame it is defined by.
     upstream: T-C10 HUMAN_VALIDATED 4CH1-2.38/2.32 (2026-09-11)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-23'
   version: 1
   created_at: '2026-09-23'
 - source: 4CH1-CON-BOND-BREAKING-MAKING
```

### 4. `4CH1-CON-NEUTRALISATION REQUIRES_PREREQUISITE 4CH1-CON-ACID-ALKALI-IONS` [high]

- node 4CH1-CON-NEUTRALISATION — Neutralisation (alkalis neutralise acids; H+ + OH- -> water) (CONCEPT)
-   spec 4CH1-2.32 [CORE]: know that alkalis can neutralise acids
- node 4CH1-CON-ACID-ALKALI-IONS — Acids as hydrogen-ion sources and alkalis as hydroxide-ion sources in aqueous solution (CONCEPT)
-   spec 4CH1-2.31 [CORE]: know that acids in aqueous solution are a source of hydrogen ions and alkalis in a aqueous so...
- derivation: DEFINITIONAL_DEPENDENCY — The neutralisation mechanism is STATED in terms of the ion sources: "the H+ ions react with the OH- ions to produce water" — the 2.32 definition presupposes the 2.31 picture (the spec's own 2.31-then-2.32 order).
- `NOTE` Acids, Alkalis & Neutralisation - IGCSE Revision Notes.md — "A neutralisation reaction occurs when an acid reacts with an alkali"
- `NOTE` Acids, Alkalis & Neutralisation - IGCSE Revision Notes.md — "When these substances react together in a neutralisation reaction, the H+ ions react with the OH- ions to p..."

```diff
@@ -8116,7 +8116,9 @@ edges:
       spec''s own 2.31-then-2.32 order).'
     upstream: T-C10 HUMAN_VALIDATED 4CH1-2.32/2.31 @ Acids, Alkalis & Neutralisation (2026-09-11)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-23'
   version: 1
   created_at: '2026-09-23'
 - source: 4CH1-CON-NOBLE-GAS-INERTNESS
```

### 5. `4CH1-CON-PROTON-TRANSFER REQUIRES_PREREQUISITE 4CH1-CON-ACID-ALKALI-IONS` [high]

- node 4CH1-CON-PROTON-TRANSFER — Acids and bases as proton transfer (donor and acceptor) (CONCEPT)
-   spec 4CH1-2.35 [CORE]: understand acids and bases in terms of proton transfer
-   spec 4CH1-2.36 [CORE]: understand that an acid is a proton donor and a base is a proton acceptor
- node 4CH1-CON-ACID-ALKALI-IONS — Acids as hydrogen-ion sources and alkalis as hydroxide-ion sources in aqueous solution (CONCEPT)
-   spec 4CH1-2.31 [CORE]: know that acids in aqueous solution are a source of hydrogen ions and alkalis in a aqueous so...
- derivation: EXPLICIT_TEACH_SEQUENCE — The note STATES the dependency: the proton-transfer framework "extends the earlier definition" — the earlier definition IS the 2.31 ion-source picture; the donor/acceptor definitions presuppose the H+/OH- solution ions they donate/accept.
- `NOTE` What are acids and bases - IGCSE Chemistry Revision Notes.md — "The earlier definition of an acid and a base can be extended"
- `NOTE` What are acids and bases - IGCSE Chemistry Revision Notes.md — "In terms of proton transfer, we can further define each substance in how they interact with protons"

```diff
@@ -8299,7 +8299,9 @@ edges:
       presuppose the H+/OH- solution ions they donate/accept.'
     upstream: T-C10 HUMAN_VALIDATED 4CH1-2.35/2.36 @ What are acids and bases + 4CH1-2.31 (2026-09-11)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-23'
   version: 1
   created_at: '2026-09-23'
 - source: 4CH1-CON-PURE-SUBSTANCE
```

### 6. `4CH1-CON-SALT-INSOLUBLE-REACTANT REQUIRES_PREREQUISITE 4CH1-CON-ACID-REACTIONS` [high]

- node 4CH1-CON-SALT-INSOLUBLE-REACTANT — Preparing a pure, dry soluble salt from an insoluble reactant (excess-base route) (CONCEPT)
-   spec 4CH1-2.39 [CORE]: describe an experiment to prepare a pure, dry sample of a soluble salt, starting from an inso...
- node 4CH1-CON-ACID-REACTIONS — Reactions of acids with metals, bases and metal carbonates to form salts (CONCEPT)
-   spec 4CH1-2.37 [CORE]: describe the reactions of hydrochloric acid, sulfuric acid and nitric acid with metals, bases...
- derivation: DEFINITIONAL_DEPENDENCY — The route RUNS the 2.37 acid+base reaction family (the note's own CuO + H2SO4 equation is that family's chemistry) — the preparation presupposes the reaction it scales up.
- `NOTE` Making soluble salts - IGCSE Chemistry Revision Notes.md — "A soluble salt can be made from the reaction of an acid with an insoluble base"
- `NOTE` Making soluble salts - IGCSE Chemistry Revision Notes.md — "CuO (s) + H2SO4&nbsp; (aq) ⟶ CuSO4&nbsp; (aq) + H2O (l)"

```diff
@@ -8762,7 +8762,9 @@ edges:
       is that family's chemistry) — the preparation presupposes the reaction it scales up.
     upstream: T-C10 HUMAN_VALIDATED 4CH1-2.39/2.37 (2026-09-11)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-23'
   version: 1
   created_at: '2026-09-23'
 - source: 4CH1-CON-SALT-INSOLUBLE-REACTANT
```

### 7. `4CH1-CON-SALT-INSOLUBLE-REACTANT REQUIRES_PREREQUISITE 4CH1-CON-SOLUBILITY-RULES` [high]

- node 4CH1-CON-SALT-INSOLUBLE-REACTANT — Preparing a pure, dry soluble salt from an insoluble reactant (excess-base route) (CONCEPT)
-   spec 4CH1-2.39 [CORE]: describe an experiment to prepare a pure, dry sample of a soluble salt, starting from an inso...
- node 4CH1-CON-SOLUBILITY-RULES — Solubility rules for ionic compounds in water (the salt-preparation method-selection frame) (CONCEPT)
-   spec 4CH1-2.34 [CORE]: know the general rules for predicting the solubility of ionic compounds in water:
- derivation: DEFINITIONAL_DEPENDENCY — The method-SELECTION logic is explicit: knowing the solubility of the target salt "determines the most appropriate method" — the insoluble-reactant route IS the route the rules select when the PRODUCT is soluble and the reactant is not (the solubility note's own framing sentence).
- `NOTE` Solubility Rules  Edexcel IGCSE Chemistry Revision Notes 2017.md — "A knowledge of the solubility of ionic compounds helps us to determine the most appropriate method for the ..."
- `NOTE` Making soluble salts - IGCSE Chemistry Revision Notes.md — "A soluble salt can be made from the reaction of an acid with an insoluble base"

```diff
@@ -8789,7 +8789,9 @@ edges:
       when the PRODUCT is soluble and the reactant is not (the solubility note''s own framing sentence).'
     upstream: T-C10 HUMAN_VALIDATED 4CH1-2.34/2.39 (2026-09-11)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-23'
   version: 1
   created_at: '2026-09-23'
 - source: 4CH1-CON-SALT-PRECIPITATION
```

### 8. `4CH1-CON-SALT-PRECIPITATION REQUIRES_PREREQUISITE 4CH1-CON-SOLUBILITY-RULES` [high]

- node 4CH1-CON-SALT-PRECIPITATION — Preparing a pure, dry insoluble salt from two soluble reactants (precipitation) (CONCEPT)
-   spec 4CH1-2.41C [CORE]: describe an experiment to prepare a pure, dry sample of an insoluble salt, starting from two ...
- node 4CH1-CON-SOLUBILITY-RULES — Solubility rules for ionic compounds in water (the salt-preparation method-selection frame) (CONCEPT)
-   spec 4CH1-2.34 [CORE]: know the general rules for predicting the solubility of ionic compounds in water:
- derivation: DEFINITIONAL_DEPENDENCY — The route's own FEASIBILITY CONDITION is the solubility rules: the product must be insoluble AND both reactants soluble — the note applies the rules explicitly (the nitrates-all-soluble rule selects the starting materials; the silver/lead(II) insolubility selects the products).
- `NOTE` Prepare an Insoluble Salt  Edexcel IGCSE Chemistry Revision Notes 2017.md — "The solid salt obtained is the precipitate, thus in order to successfully use this method the solid salt be..."
- `NOTE` Prepare an Insoluble Salt  Edexcel IGCSE Chemistry Revision Notes 2017.md — "This method is a good way to prepare silver and lead(II) salts which are often insoluble; the starting mate..."

```diff
@@ -8817,7 +8817,9 @@ edges:
       rule selects the starting materials; the silver/lead(II) insolubility selects the products).'
     upstream: T-C10 HUMAN_VALIDATED 4CH1-2.41C/2.34 (2026-09-11)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-23'
   version: 1
   created_at: '2026-09-23'
 - source: 4CH1-CON-SALT-TITRATION-ROUTE
```

### 9. `4CH1-CON-SALT-TITRATION-ROUTE REQUIRES_PREREQUISITE 4CH1-CON-TITRATION` [high]

- node 4CH1-CON-SALT-TITRATION-ROUTE — Preparing a pure, dry soluble salt from an acid and alkali (titration route) (CONCEPT)
-   spec 4CH1-2.40C [CORE]: describe an experiment to prepare a pure, dry sample of a soluble salt, starting from an acid...
- node 4CH1-CON-TITRATION — Acid-alkali titration technique (pipette, burette, endpoint, concordant titres) (CONCEPT)
-   spec 4CH1-2.33C [CORE]: describe how to carry out an acid-alkali titration
- derivation: EXPLICIT_TEACH_SEQUENCE — The route IS the 2.33C technique applied to preparation (the note's own sentence; the method steps reuse the titration apparatus vocabulary) — the preparation presupposes the technique that measures its neutralisation volume.
- `NOTE` Prepare a Soluble Salt II  Edexcel IGCSE Chemistry Revision Notes 2017.md — "A titration can be used for this"
- `NOTE` Prepare a Soluble Salt II  Edexcel IGCSE Chemistry Revision Notes 2017.md — "Use a pipette to measure the alkali into a conical flask and add a few drops of indicator (phenolphthalein ..."

```diff
@@ -8844,7 +8844,9 @@ edges:
       that measures its neutralisation volume.
     upstream: T-C10 HUMAN_VALIDATED 4CH1-2.40C/2.33C (2026-09-11)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-23'
   version: 1
   created_at: '2026-09-23'
 - source: 4CH1-CON-SATURATED-SOLUTION
```

### 10. `4CH1-CON-SOLUBILITY-RULES REQUIRES_PREREQUISITE 4CH1-CON-ION-CHARGE-RULES` [high]

- node 4CH1-CON-SOLUBILITY-RULES — Solubility rules for ionic compounds in water (the salt-preparation method-selection frame) (CONCEPT)
-   spec 4CH1-2.34 [CORE]: know the general rules for predicting the solubility of ionic compounds in water:
- node 4CH1-CON-ION-CHARGE-RULES — Common ion charges (group-based and named-ion table, with the deduction rule) (CONCEPT)
-   spec 4CH1-1.38 [CORE]: know the charges of these ions:
- derivation: USED_WITHOUT_RETEACHING — SANCTIONED BOUNDARY EDGE (the session-59 ruling, target 2 — the batch-3 CON-ION-CHARGE-RULES owner): the 2.34 rules table is organised by ION families (Na/K/NH4+, nitrates, chlorides, sulfates, carbonates, hydroxides) and predicts solubility from ion identity — the named-ion/charge vocabulary applied as given, never re-taught by the 2.34 note. "Ca(OH)2 sparingly soluble" is itself an ion-family rule (the calcium hydroxide exception).
- `NOTE` Solubility Rules  Edexcel IGCSE Chemistry Revision Notes 2017.md — "A knowledge of the solubility of ionic compounds helps us to determine the most appropriate method for the ..."
- `NOTE` Solubility Rules  Edexcel IGCSE Chemistry Revision Notes 2017.md — "Note that calcium hydroxide is slightly soluble in water"

```diff
@@ -9046,7 +9046,9 @@ edges:
       rule (the calcium hydroxide exception).'
     upstream: T-C10 HUMAN_VALIDATED 4CH1-2.34 (2026-09-11); the batch-3 record (CON-ION-CHARGE-RULES)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-23'
   version: 1
   created_at: '2026-09-23'
 - source: 4CH1-CON-STATE-CHANGES
```

### 11. `4CH1-CON-TITRATION REQUIRES_PREREQUISITE 4CH1-CON-INDICATORS` [high]

- node 4CH1-CON-TITRATION — Acid-alkali titration technique (pipette, burette, endpoint, concordant titres) (CONCEPT)
-   spec 4CH1-2.33C [CORE]: describe how to carry out an acid-alkali titration
- node 4CH1-CON-INDICATORS — Indicators for distinguishing acidic and alkaline solutions (litmus, phenolphthalein, methyl orange) (CONCEPT)
-   spec 4CH1-2.28 [CORE]: describe the use of litmus, phenolphthalein and methyl orange to distinguish between acidic a...
- derivation: EXPLICIT_TEACH_SEQUENCE — The titration method DEPENDS on indicator choice for the endpoint (the sharp-change requirement); the indicator note teaches the suitability content explicitly (litmus unsuitable — purple transition; phenolphthalein/methyl orange the titration indicators).
- `NOTE` Acid-Alkali Titrations  Edexcel IGCSE Chemistry Revision Notes 2017.md — "Add a few drops of a suitable indicator to the solution to the conical flask"
- `NOTE` What is an indicator - IGCSE Chemistry Revision Notes.md — "Synthetic indicators are used to show the endpoint in titrations as they have a very sharp change of colour..."

```diff
@@ -9169,7 +9169,9 @@ edges:
       purple transition; phenolphthalein/methyl orange the titration indicators).
     upstream: T-C10 HUMAN_VALIDATED 4CH1-2.33C/2.28 (2026-09-11)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-23'
   version: 1
   created_at: '2026-09-23'
 - source: 4CH1-CON-TITRATION
```

### 12. `4CH1-CON-TITRATION REQUIRES_PREREQUISITE 4CH1-CON-NEUTRALISATION` [high]

- node 4CH1-CON-TITRATION — Acid-alkali titration technique (pipette, burette, endpoint, concordant titres) (CONCEPT)
-   spec 4CH1-2.33C [CORE]: describe how to carry out an acid-alkali titration
- node 4CH1-CON-NEUTRALISATION — Neutralisation (alkalis neutralise acids; H+ + OH- -> water) (CONCEPT)
-   spec 4CH1-2.32 [CORE]: know that alkalis can neutralise acids
- derivation: DEFINITIONAL_DEPENDENCY — The titration's PURPOSE is defined by neutralisation: "how much alkali is needed to neutralise a quantity of acid" — the endpoint IS the neutralisation point; without the 2.32 concept the procedure has no meaning.
- `NOTE` Acid-Alkali Titrations  Edexcel IGCSE Chemistry Revision Notes 2017.md — "They can determine exactly how much alkali is needed to neutralise a quantity of acid - and vice versa"
- `NOTE` Acid-Alkali Titrations  Edexcel IGCSE Chemistry Revision Notes 2017.md — "Titrations can also be used to prepare salts"

```diff
@@ -9196,7 +9196,9 @@ edges:
       the procedure has no meaning.'
     upstream: T-C10 HUMAN_VALIDATED 4CH1-2.33C/2.32 (2026-09-11)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-23'
   version: 1
   created_at: '2026-09-23'
 - source: 4CH1-CON-UNIVERSAL-INDICATOR
```

### 13. `4CH1-CON-UNIVERSAL-INDICATOR REQUIRES_PREREQUISITE 4CH1-CON-PH-SCALE` [high]

- node 4CH1-CON-UNIVERSAL-INDICATOR — Universal indicator as approximate pH measurement (colour-chart matching) (CONCEPT)
-   spec 4CH1-2.30 [CORE]: describe the use of universal indicator to measure the approximate pH value of an aqueous sol...
- node 4CH1-CON-PH-SCALE — The pH scale 0-14 and the acidity/alkalinity classification bands (CONCEPT)
-   spec 4CH1-2.29 [CORE]: understand how to use the pH scale, from 0–14, can be used to classify solutions as strongly ...
- derivation: EXPLICIT_TEACH_SEQUENCE — The 2.30 technique MEASURES what the 2.29 scale defines: the colour is "matched with a colour chart which indicates the pH" — reading a universal-indicator result IS using the pH scale (the note's own order: indicators -> pH scale -> universal indicator).
- `NOTE` What is an indicator - IGCSE Chemistry Revision Notes.md — "A few drops are added to the solution and the colour is matched with a colour chart which indicates the pH ..."
- `NOTE` What is an indicator - IGCSE Chemistry Revision Notes.md — "Universal indicator is a wide range indicator and can give only an approximate value for pH"

```diff
@@ -9223,7 +9223,9 @@ edges:
       pH scale (the note''s own order: indicators -> pH scale -> universal indicator).'
     upstream: T-C10 HUMAN_VALIDATED 4CH1-2.30/2.29 @ What is an indicator (2026-09-11)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-23'
   version: 1
   created_at: '2026-09-23'
 - source: 4CH1-CON-WATER-CRYST
```

### 14. `4CH1-MIS-ENDPOINT-PH-ABOVE-7 REMEDIATED_BY 4CH1-CON-NEUTRALISATION` [high]

- node 4CH1-MIS-ENDPOINT-PH-ABOVE-7 — Identifying complete neutralisation as the pH changing to any value above 7 (instead of the temperature maximum / pH reaching 7) (MISCONCEPTION)
- node 4CH1-CON-NEUTRALISATION — Neutralisation (alkalis neutralise acids; H+ + OH- -> water) (CONCEPT)
-   spec 4CH1-2.32 [CORE]: know that alkalis can neutralise acids
- derivation: ASSESSMENT_DOCUMENTED — Remediation target = WAP target (the B1-E-25 pattern): the corrective content IS the neutralisation definition ("an acid reacts with an alkali") plus the MS's own accepted completion signals ("when pH = 7/when pH is less than 7" — the neutral point, not any value above it).
- `NOTE` Acids, Alkalis & Neutralisation - IGCSE Revision Notes.md — "A neutralisation reaction occurs when an acid reacts with an alkali"
- `MARK_SCHEME` ACIDS_ALKALIS_TITRATIONS_MS_P2.txt — "Accept measure pH/when pH = 7/when pH is less than 7"

```diff
@@ -10813,7 +10813,9 @@ edges:
     upstream: pinned ACIDS_ALKALIS_TITRATIONS_MS_P2 (sha1_12 14b605bc2f87) Q2a(iv); Acids, Alkalis & Neutralisation
       note (2026-09-11)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-23'
   version: 1
   created_at: '2026-09-23'
 - source: 4CH1-MIS-ENTHALPY-UNIT-J
```

### 15. `4CH1-MIS-ENDPOINT-PH-ABOVE-7 WRONG_ANSWER_PATTERN 4CH1-CON-NEUTRALISATION` [high]

- node 4CH1-MIS-ENDPOINT-PH-ABOVE-7 — Identifying complete neutralisation as the pH changing to any value above 7 (instead of the temperature maximum / pH reaching 7) (MISCONCEPTION)
- node 4CH1-CON-NEUTRALISATION — Neutralisation (alkalis neutralise acids; H+ + OH- -> water) (CONCEPT)
-   spec 4CH1-2.32 [CORE]: know that alkalis can neutralise acids
- derivation: ASSESSMENT_DOCUMENTED — The WAP target is the concept whose completion the question probes: the acid-alkali neutralisation (2.32) — the MS caps the "any pH value > 7" answer class on exactly that surface (the B5/B6 WAP-target pattern). The question's temperature-experiment context is recorded (the S3 3.8/PR-09 future_boundary_note).
- `MARK_SCHEME` ACIDS_ALKALIS_TITRATIONS_MS_P2.txt — "Reject changing to any pH value > 7"
- `MARK_SCHEME` ACIDS_ALKALIS_TITRATIONS_MS_P2.txt — "temperature goes down/stops rising/stays constant"

```diff
@@ -10336,7 +10336,9 @@ edges:
     upstream: pinned ACIDS_ALKALIS_TITRATIONS_MS_P2 (sha1_12 14b605bc2f87) Q2a(iv); spec 4CH1-2.32 official
       wording
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-23'
   version: 1
   created_at: '2026-09-23'
 - source: 4CH1-MIS-ENTHALPY-UNIT-J
```

### 16. `4CH1-MIS-PRECIPITATE-IN-FILTRATE REMEDIATED_BY 4CH1-CON-SALT-PRECIPITATION` [high]

- node 4CH1-MIS-PRECIPITATE-IN-FILTRATE — Recovering the insoluble salt from the filtrate instead of the residue in a precipitation preparation (MISCONCEPTION)
- node 4CH1-CON-SALT-PRECIPITATION — Preparing a pure, dry insoluble salt from two soluble reactants (precipitation) (CONCEPT)
-   spec 4CH1-2.41C [CORE]: describe an experiment to prepare a pure, dry sample of an insoluble salt, starting from two ...
- derivation: ASSESSMENT_DOCUMENTED — Remediation target = WAP target (the B1-E-25 pattern): the corrective content IS the method's own teaching — the PRECIPITATE (the residue on the filter paper) is the salt; the MS's expected answer ("they should have used the residue") is the same statement in assessment form.
- `NOTE` Prepare an Insoluble Salt  Edexcel IGCSE Chemistry Revision Notes 2017.md — "The precipitate is recovered by filtration"
- `MARK_SCHEME` ACIDS_BASES_SALT_PREP_MS_P2.txt — "they should have used the residue"

```diff
@@ -11151,7 +11151,9 @@ edges:
     upstream: pinned ACIDS_BASES_SALT_PREP_MS_P2 (sha1_12 4f34b1580a60) Q2a(iii); Prepare an Insoluble
       Salt note (2026-09-11)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-23'
   version: 1
   created_at: '2026-09-23'
 - source: 4CH1-MIS-RAM-MASS-NUMBER
```

### 17. `4CH1-MIS-PRECIPITATE-IN-FILTRATE WRONG_ANSWER_PATTERN 4CH1-CON-SALT-PRECIPITATION` [high]

- node 4CH1-MIS-PRECIPITATE-IN-FILTRATE — Recovering the insoluble salt from the filtrate instead of the residue in a precipitation preparation (MISCONCEPTION)
- node 4CH1-CON-SALT-PRECIPITATION — Preparing a pure, dry insoluble salt from two soluble reactants (precipitation) (CONCEPT)
-   spec 4CH1-2.41C [CORE]: describe an experiment to prepare a pure, dry sample of an insoluble salt, starting from two ...
- derivation: ASSESSMENT_DOCUMENTED — The WAP target is the concept the wrong answer misapplies: the precipitation preparation (2.41C) — the MS caps the "product in the filtrate" class on exactly that surface (the B5/B6 WAP-target pattern; the lead(II) sulfate preparation is the 2.41C/2.43C exemplar).
- `MARK_SCHEME` ACIDS_BASES_SALT_PREP_MS_P2.txt — "the filtrate does not contain lead(II) sulfate/the insoluble salt"
- `MARK_SCHEME` ACIDS_BASES_SALT_PREP_MS_P2.txt — "they would obtain sodium nitrate instead"

```diff
@@ -10607,7 +10607,9 @@ edges:
     upstream: pinned ACIDS_BASES_SALT_PREP_MS_P2 (sha1_12 4f34b1580a60) Q2a(iii); spec 4CH1-2.41C official
       wording
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-23'
   version: 1
   created_at: '2026-09-23'
 - source: 4CH1-MIS-RAM-MASS-NUMBER
```

### 18. `4CH1-PR-07 REQUIRES_PREREQUISITE 4CH1-CON-SALT-INSOLUBLE-REACTANT` [high]

- node 4CH1-CON-SALT-INSOLUBLE-REACTANT — Preparing a pure, dry soluble salt from an insoluble reactant (excess-base route) (CONCEPT)
-   spec 4CH1-2.39 [CORE]: describe an experiment to prepare a pure, dry sample of a soluble salt, starting from an inso...
- derivation: USED_WITHOUT_RETEACHING — Practical->conceptual (the PR-05/PR-06 shape): the 2.42 practical RUNS the method its concept owns — the named practical IS the insoluble-reactant route with copper(II) oxide ("the base stops dissolving" = the excess-endpoint observation). 2.42 attaches NO concept node (the 1.13/1.60C/2.14/2.21 precedent; 4CH1-PR-07 owns it).
- `NOTE` Preparing copper sulfate - IGCSE Chemistry Revision Notes.md — "To prepare a pure, dry sample of hydrated copper(II) sulfate crystals"
- `NOTE` Preparing copper sulfate - IGCSE Chemistry Revision Notes.md — "Add the copper(II) oxide slowly to the hot dilute acid and stir until the base is in excess (i.e. until the..."

```diff
@@ -9517,7 +9517,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-2.42/2.39 @ Preparing copper sulfate (2026-09-11); the practical
       record 4CH1-PR-07 (practicals.yaml, RULE_DERIVED)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-23'
   version: 1
   created_at: '2026-09-23'
 - source: 4CH1-PR-08
```

### 19. `4CH1-PR-08 REQUIRES_PREREQUISITE 4CH1-CON-SALT-PRECIPITATION` [high]

- node 4CH1-CON-SALT-PRECIPITATION — Preparing a pure, dry insoluble salt from two soluble reactants (precipitation) (CONCEPT)
-   spec 4CH1-2.41C [CORE]: describe an experiment to prepare a pure, dry sample of an insoluble salt, starting from two ...
- derivation: USED_WITHOUT_RETEACHING — Practical->conceptual (the PR-05/PR-06 shape): the 2.43C practical RUNS the precipitation route its concept owns — lead(II) nitrate + potassium sulfate IS the two-soluble-reactants precipitation (the practical's own aim sentence restates the concept's feasibility condition). 2.43C attaches NO concept node (4CH1-PR-08 owns it).
- `NOTE` Preparing lead sulfate - IGCSE Chemistry Revision Notes.md — "The solid salt obtained is the precipitate, thus in order to successfully use this method the solid salt be..."
- `NOTE` Preparing lead sulfate - IGCSE Chemistry Revision Notes.md — "Filter to remove precipitate from mixture"

```diff
@@ -9546,7 +9546,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-2.43C/2.41C @ Preparing lead sulfate (2026-09-11); the practical
       record 4CH1-PR-08 (practicals.yaml, RULE_DERIVED)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-23'
   version: 1
   created_at: '2026-09-23'
 - source: 4CH1-PR-09
```

## File-level meta hunks (once, for the whole batch)

```diff
@@ -196,8 +196,10 @@ meta:
     remediated_by_edges: 21
     requires_prerequisite_edges: 154
     wrong_answer_pattern_edges: 19
-    promoted_edges: 304
-    human_validated_edges: 304
+    promoted_edges: 323
+    human_validated_edges: 323
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
| `4CH1-CON-ACID-REACTIONS` | Reactions of acids with metals, bases and metal carbonates to form salts | CONCEPT | 4CH1-2.37 (CORE) | high |
| `4CH1-CON-ACTIVATION-ENERGY` | Activation energy (minimum energy for reaction; Ea) | CONCEPT | 4CH1-3.14C (CORE) | high |
| `4CH1-CON-AIR-COMPOSITION` | Composition of dry air (approximate percentages of the four most abundant gases) | CONCEPT | 4CH1-2.9 (CORE) | high |
| `4CH1-CON-ALLOY-HARDNESS` | Why alloys are harder than pure metals (distorted layers resist sliding) | CONCEPT | 4CH1-2.27C (CORE) | high |
| `4CH1-CON-ALLOYS` | Alloys as mixtures of a metal with other elements | CONCEPT | 4CH1-2.26C (CORE) | high |
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
| `4CH1-CON-EXTRACTION-EVALUATION` | Commenting on a metal extraction process from given information | CONCEPT | 4CH1-2.24C (CORE) | high |
| `4CH1-CON-EXTRACTION-METHOD` | Extraction method related to reactivity-series position (electrolysis above carbon; carbon reduction below) | CONCEPT | 4CH1-2.23C (CORE) | high |
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
| `4CH1-CON-INDICATORS` | Indicators for distinguishing acidic and alkaline solutions (litmus, phenolphthalein, methyl orange) | CONCEPT | 4CH1-2.28 (CORE) | high |
| `4CH1-CON-ION` | Ion (formation by electron loss or gain) | CONCEPT | 4CH1-1.37 (CORE) | high |
| `4CH1-CON-ION-CHARGE-RULES` | Common ion charges (group-based and named-ion table, with the deduction rule) | CONCEPT | 4CH1-1.38 (CORE) | high |
| `4CH1-CON-IONIC-BOND` | Ionic bonding (electrostatic attraction between oppositely charged ions) | CONCEPT | 4CH1-1.41 (CORE) | high |
| `4CH1-CON-IONIC-CONDUCTION` | Ionic conduction (solid insulator; molten and aqueous conductor via mobile ions) | CONCEPT | 4CH1-1.43 (CORE); 4CH1-1.56C (CORE) | high |
| `4CH1-CON-IONIC-FORMULA` | Writing formulae for ionic compounds (charge cancellation and swap-and-drop) | CONCEPT | 4CH1-1.39 (CORE) | high |
| `4CH1-CON-IONIC-LATTICE` | Giant ionic lattice and why ionic compounds have high melting and boiling points | CONCEPT | 4CH1-1.42 (CORE) | high |
| `4CH1-CON-ISOTOPES` | Isotopes and relative atomic mass from isotopic abundances | CONCEPT | 4CH1-1.16 (CORE); 4CH1-1.17 (CORE) | high |
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
| `4CH1-MIS-GRAPHITE-LAYER-BONDS` | Saying graphite layers are held together by bonds (instead of weak forces of attraction between the layers) | MISCONCEPTION |  | high |
| `4CH1-MIS-HALOGEN-HALIDE` | Treating a halogen and its halide ion as having the same (or different) reactivity in displacement reasoning | MISCONCEPTION |  | high |
| `4CH1-MIS-ION-OXIDE-REASONING` | Explaining a metal-oxide displacement outcome by references to ions and oxides instead of the reactivity comparison | MISCONCEPTION |  | high |
| `4CH1-MIS-IONIC-BOND-ATOMS` | Describing ionic bonding as attraction between atoms or molecules (or as intermolecular forces) | MISCONCEPTION |  | high |
| `4CH1-MIS-IONIC-CONDUCTION-ELECTRONS` | Believing ionic compounds conduct electricity because electrons move and carry the charge | MISCONCEPTION |  | high |
| `4CH1-MIS-ISOTOPES-DIFFER-PROTONS` | Believing isotopes of an element differ in their number of protons | MISCONCEPTION |  | high |
| `4CH1-MIS-PRECIPITATE-IN-FILTRATE` | Recovering the insoluble salt from the filtrate instead of the residue in a precipitation preparation | MISCONCEPTION |  | high |
| `4CH1-MIS-RAM-MASS-NUMBER` | Calling the Periodic Table relative atomic mass the mass number | MISCONCEPTION |  | high |

