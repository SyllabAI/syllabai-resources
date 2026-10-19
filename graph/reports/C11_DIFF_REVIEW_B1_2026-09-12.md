# C11 Diff Review Bundle — pending §18 edge promotions (generated 2026-09-12)

- baseline commit: `50351e1`
- state fingerprint: `14abeb665d95` (promo_count=28)
- actionable: 28 edges (clean 28 / pending-flagged 0); not-actionable: 5; nodes awaiting a pathway: 53
- preview fidelity: simulator re-emits graph/concept_edges.yaml under the generator's own serialization contract with a byte-identity guard — what you read is what G13 will write.

## Batch approval

```bash
cd work/syllabai-resources && python3 scripts/c11_diff_review.py approve \
  '4CH1-CON-CHROMATOGRAM-INTERPRETATION REQUIRES_PREREQUISITE 4CH1-CON-CHROMATOGRAPHY' \
  '4CH1-CON-CHROMATOGRAM-INTERPRETATION REQUIRES_PREREQUISITE 4CH1-CON-PURE-SUBSTANCE' \
  '4CH1-CON-CHROMATOGRAPHY REQUIRES_PREREQUISITE 4CH1-CON-SOLUBILITY' \
  '4CH1-CON-COMPOUND REQUIRES_PREREQUISITE 4CH1-CON-ELEMENT' \
  '4CH1-CON-CRYSTALLISATION EXPLAINED_BY 4CH1-CON-SOLUBILITY' \
  '4CH1-CON-CRYSTALLISATION REQUIRES_PREREQUISITE 4CH1-CON-SATURATED-SOLUTION' \
  '4CH1-CON-DIFFUSION EXPLAINED_BY 4CH1-CON-STATE-PARTICLE-MODEL' \
  '4CH1-CON-DILUTION EXPLAINED_BY 4CH1-CON-STATE-PARTICLE-MODEL' \
  '4CH1-CON-EVAPORATION-BOILING REQUIRES_PREREQUISITE 4CH1-CON-STATE-CHANGES' \
  '4CH1-CON-FILTRATION REQUIRES_PREREQUISITE 4CH1-CON-SOLUTION' \
  '4CH1-CON-FRACTIONAL-DISTILLATION REQUIRES_PREREQUISITE 4CH1-CON-SIMPLE-DISTILLATION' \
  '4CH1-CON-MIXTURE REQUIRES_PREREQUISITE 4CH1-CON-COMPOUND' \
  '4CH1-CON-PURE-SUBSTANCE REQUIRES_PREREQUISITE 4CH1-CON-COMPOUND' \
  '4CH1-CON-PURE-SUBSTANCE REQUIRES_PREREQUISITE 4CH1-CON-STATE-CHANGES' \
  '4CH1-CON-RF-VALUE REQUIRES_PREREQUISITE 4CH1-CON-CHROMATOGRAM-INTERPRETATION' \
  '4CH1-CON-SATURATED-SOLUTION REQUIRES_PREREQUISITE 4CH1-CON-SOLUTION' \
  '4CH1-CON-SIMPLE-DISTILLATION REQUIRES_PREREQUISITE 4CH1-CON-SOLUTION' \
  '4CH1-CON-SIMPLE-DISTILLATION REQUIRES_PREREQUISITE 4CH1-CON-STATE-CHANGES' \
  '4CH1-CON-SOLUBILITY REQUIRES_PREREQUISITE 4CH1-CON-SATURATED-SOLUTION' \
  '4CH1-CON-SOLUBILITY-CURVE REQUIRES_PREREQUISITE 4CH1-CON-SOLUBILITY' \
  '4CH1-CON-STATE-CHANGES REQUIRES_PREREQUISITE 4CH1-CON-STATE-PARTICLE-MODEL' \
  '4CH1-CON-STATE-PARTICLE-MODEL REQUIRES_PREREQUISITE 4CH1-CON-STATES-THREE' \
  '4CH1-MIS-CRYSTALLISATION-DRYNESS REMEDIATED_BY 4CH1-CON-SATURATED-SOLUTION' \
  '4CH1-MIS-CRYSTALLISATION-DRYNESS WRONG_ANSWER_PATTERN 4CH1-CON-CRYSTALLISATION' \
  '4CH1-MIS-GAS-PARTICLES-TOUCH REMEDIATED_BY 4CH1-CON-STATE-PARTICLE-MODEL' \
  '4CH1-MIS-GAS-PARTICLES-TOUCH WRONG_ANSWER_PATTERN 4CH1-CON-STATE-PARTICLE-MODEL' \
  '4CH1-PR-01 REQUIRES_PREREQUISITE 4CH1-CON-SATURATED-SOLUTION' \
  '4CH1-PR-01 REQUIRES_PREREQUISITE 4CH1-CON-SOLUBILITY' \
  --by <operator> --date 2026-09-12 --review-ref graph/reports/C11_DIFF_REVIEW_B1_2026-09-12.md
```

Pending-flagged (PENDING operator_decision) edges are excluded from the command above; approving them additionally requires `--include-pending` — that flag records the explicit decision this bundle presents.

## Index

| # | identity | confidence | flag |
|---|----------|------------|------|
| 1 | `4CH1-CON-CHROMATOGRAM-INTERPRETATION REQUIRES_PREREQUISITE 4CH1-CON-CHROMATOGRAPHY` | high |  |
| 2 | `4CH1-CON-CHROMATOGRAM-INTERPRETATION REQUIRES_PREREQUISITE 4CH1-CON-PURE-SUBSTANCE` | high |  |
| 3 | `4CH1-CON-CHROMATOGRAPHY REQUIRES_PREREQUISITE 4CH1-CON-SOLUBILITY` | high |  |
| 4 | `4CH1-CON-COMPOUND REQUIRES_PREREQUISITE 4CH1-CON-ELEMENT` | high |  |
| 5 | `4CH1-CON-CRYSTALLISATION EXPLAINED_BY 4CH1-CON-SOLUBILITY` | high |  |
| 6 | `4CH1-CON-CRYSTALLISATION REQUIRES_PREREQUISITE 4CH1-CON-SATURATED-SOLUTION` | high |  |
| 7 | `4CH1-CON-DIFFUSION EXPLAINED_BY 4CH1-CON-STATE-PARTICLE-MODEL` | high |  |
| 8 | `4CH1-CON-DILUTION EXPLAINED_BY 4CH1-CON-STATE-PARTICLE-MODEL` | high |  |
| 9 | `4CH1-CON-EVAPORATION-BOILING REQUIRES_PREREQUISITE 4CH1-CON-STATE-CHANGES` | high |  |
| 10 | `4CH1-CON-FILTRATION REQUIRES_PREREQUISITE 4CH1-CON-SOLUTION` | high |  |
| 11 | `4CH1-CON-FRACTIONAL-DISTILLATION REQUIRES_PREREQUISITE 4CH1-CON-SIMPLE-DISTILLATION` | high |  |
| 12 | `4CH1-CON-MIXTURE REQUIRES_PREREQUISITE 4CH1-CON-COMPOUND` | high |  |
| 13 | `4CH1-CON-PURE-SUBSTANCE REQUIRES_PREREQUISITE 4CH1-CON-COMPOUND` | high |  |
| 14 | `4CH1-CON-PURE-SUBSTANCE REQUIRES_PREREQUISITE 4CH1-CON-STATE-CHANGES` | high |  |
| 15 | `4CH1-CON-RF-VALUE REQUIRES_PREREQUISITE 4CH1-CON-CHROMATOGRAM-INTERPRETATION` | high |  |
| 16 | `4CH1-CON-SATURATED-SOLUTION REQUIRES_PREREQUISITE 4CH1-CON-SOLUTION` | high |  |
| 17 | `4CH1-CON-SIMPLE-DISTILLATION REQUIRES_PREREQUISITE 4CH1-CON-SOLUTION` | high |  |
| 18 | `4CH1-CON-SIMPLE-DISTILLATION REQUIRES_PREREQUISITE 4CH1-CON-STATE-CHANGES` | high |  |
| 19 | `4CH1-CON-SOLUBILITY REQUIRES_PREREQUISITE 4CH1-CON-SATURATED-SOLUTION` | high |  |
| 20 | `4CH1-CON-SOLUBILITY-CURVE REQUIRES_PREREQUISITE 4CH1-CON-SOLUBILITY` | high |  |
| 21 | `4CH1-CON-STATE-CHANGES REQUIRES_PREREQUISITE 4CH1-CON-STATE-PARTICLE-MODEL` | high |  |
| 22 | `4CH1-CON-STATE-PARTICLE-MODEL REQUIRES_PREREQUISITE 4CH1-CON-STATES-THREE` | high |  |
| 23 | `4CH1-MIS-CRYSTALLISATION-DRYNESS REMEDIATED_BY 4CH1-CON-SATURATED-SOLUTION` | high |  |
| 24 | `4CH1-MIS-CRYSTALLISATION-DRYNESS WRONG_ANSWER_PATTERN 4CH1-CON-CRYSTALLISATION` | high |  |
| 25 | `4CH1-MIS-GAS-PARTICLES-TOUCH REMEDIATED_BY 4CH1-CON-STATE-PARTICLE-MODEL` | high |  |
| 26 | `4CH1-MIS-GAS-PARTICLES-TOUCH WRONG_ANSWER_PATTERN 4CH1-CON-STATE-PARTICLE-MODEL` | high |  |
| 27 | `4CH1-PR-01 REQUIRES_PREREQUISITE 4CH1-CON-SATURATED-SOLUTION` | high |  |
| 28 | `4CH1-PR-01 REQUIRES_PREREQUISITE 4CH1-CON-SOLUBILITY` | high |  |

## Pending items — the exact diff each approval applies

### 1. `4CH1-CON-CHROMATOGRAM-INTERPRETATION REQUIRES_PREREQUISITE 4CH1-CON-CHROMATOGRAPHY` [high]

- node 4CH1-CON-CHROMATOGRAM-INTERPRETATION — Interpreting chromatograms (CONCEPT)
-   spec 4CH1-1.11 [CORE]: understand how a chromatogram provides information about the composition of a mixture
- node 4CH1-CON-CHROMATOGRAPHY — Paper chromatography (separation by differential solubility) (CONCEPT)
-   spec 4CH1-1.10 [CORE]: describe these experimental techniques for the separation of mixtures: 简单 distillation fracti...
- derivation: EXAMINER_TIP_EXPLICIT — The examiner tip defines the chromatogram AS the output of a chromatography run — interpreting the output presupposes the run that produced it (spots, baseline, solvent travel); the note explicitly warns the two are different things.
- `NOTE` Separation techniques - IGCSE Chemistry Revision Notes.md — "Paper chromatography is the name given to the overall separation technique while a chromatogram is the name..."

```diff
@@ -1634,7 +1634,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.10 @ Separation techniques (2026-09-11); 1.11 note
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

### 2. `4CH1-CON-CHROMATOGRAM-INTERPRETATION REQUIRES_PREREQUISITE 4CH1-CON-PURE-SUBSTANCE` [high]

- node 4CH1-CON-CHROMATOGRAM-INTERPRETATION — Interpreting chromatograms (CONCEPT)
-   spec 4CH1-1.11 [CORE]: understand how a chromatogram provides information about the composition of a mixture
- node 4CH1-CON-PURE-SUBSTANCE — Pure substance (chemical sense) and fixed melting/boiling points (CONCEPT)
-   spec 4CH1-1.9 [CORE]: understand that a pure substance has a fixed melting and boiling point,but that a mixture may...
- derivation: USED_WITHOUT_RETEACHING — The 1.11 reading rule (one spot = pure, more than one = impure/mixture) USES the 1.9 purity concept without re-teaching it; the note states the criterion directly. Cross-subtopic prerequisite (1.9 -> 1.11).
- `NOTE` Interpreting chromatograms - IGCSE Chemistry Revision Notes.md — "Pure substances will produce only one spot on the chromatogram"

```diff
@@ -1656,7 +1656,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.11 @ Interpreting chromatograms (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-CHROMATOGRAPHY
```

### 3. `4CH1-CON-CHROMATOGRAPHY REQUIRES_PREREQUISITE 4CH1-CON-SOLUBILITY` [high]

- node 4CH1-CON-CHROMATOGRAPHY — Paper chromatography (separation by differential solubility) (CONCEPT)
-   spec 4CH1-1.10 [CORE]: describe these experimental techniques for the separation of mixtures: 简单 distillation fracti...
- node 4CH1-CON-SOLUBILITY — Solubility (g per 100 g of solvent) (CONCEPT)
-   spec 4CH1-1.5C [CORE]: know what is meant by the term solubility in the units g per 100 g of solvent
- derivation: USED_WITHOUT_RETEACHING — The technique is DEFINED by differential solubility ("separate substances that have different solubilities in a given solvent"; "higher solubility will travel further") — the solubility concept (and its solvent) is the operative mechanism, presupposed not re-taught. Cross-subtopic prerequisite (1.5C -> 1.10).
- `NOTE` Separation techniques - IGCSE Chemistry Revision Notes.md — "Those substances with higher solubility will travel further than the others"

```diff
@@ -1679,7 +1679,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.10 @ Separation techniques (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-COMPOUND
```

### 4. `4CH1-CON-COMPOUND REQUIRES_PREREQUISITE 4CH1-CON-ELEMENT` [high]

- node 4CH1-CON-COMPOUND — Compound (CONCEPT)
-   spec 4CH1-1.8 [CORE]: understand how to classify a substance as an element,compound or mixture
- node 4CH1-CON-ELEMENT — Element (CONCEPT)
-   spec 4CH1-1.8 [CORE]: understand how to classify a substance as an element,compound or mixture
- derivation: DEFINITIONAL_DEPENDENCY — The compound definition is stated IN TERMS OF elements ("two or more different elements chemically combined"); the note defines element before compound (teach order) and the definition presupposes it.
- `NOTE` Element, Compound or Mixture  Edexcel IGCSE Chemistry Revision Notes 2017.md — "A pure substance made up of two or more different elements chemically combined"

```diff
@@ -1701,7 +1701,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.8 @ Element, Compound or Mixture (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-CONC-CALC
```

### 5. `4CH1-CON-CRYSTALLISATION EXPLAINED_BY 4CH1-CON-SOLUBILITY` [high]

- node 4CH1-CON-CRYSTALLISATION — Crystallisation (CONCEPT)
-   spec 4CH1-1.10 [CORE]: describe these experimental techniques for the separation of mixtures: 简单 distillation fracti...
- node 4CH1-CON-SOLUBILITY — Solubility (g per 100 g of solvent) (CONCEPT)
-   spec 4CH1-1.5C [CORE]: know what is meant by the term solubility in the units g per 100 g of solvent
- derivation: SINGLE_SOURCE_CAUSAL_TEACHING — The note explains WHY crystals grow on cooling CAUSALLY by the solubility-temperature relation ("due to decreasing solubility") — the mechanism is the 1.5C temperature dependence of solubility taught in the Solubility note.
- `NOTE` Separation techniques - IGCSE Chemistry Revision Notes.md — "Crystals begin to grow as solids will come out of solution due to decreasing solubility"

```diff
@@ -2722,7 +2722,9 @@ edges:
       Solubility note
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-DIFFUSION
```

### 6. `4CH1-CON-CRYSTALLISATION REQUIRES_PREREQUISITE 4CH1-CON-SATURATED-SOLUTION` [high]

- node 4CH1-CON-CRYSTALLISATION — Crystallisation (CONCEPT)
-   spec 4CH1-1.10 [CORE]: describe these experimental techniques for the separation of mixtures: 简单 distillation fracti...
- node 4CH1-CON-SATURATED-SOLUTION — Saturated solution (CONCEPT)
-   spec 4CH1-1.4 [CORE]: know what is meant by the terms: • solvent • solute • solution • saturated solution.
-   spec 4CH1-1.10 [SUPPORTING]: describe these experimental techniques for the separation of mixtures: 简单 distillation fracti...
- derivation: USED_WITHOUT_RETEACHING — The crystallisation method's central step is producing and testing a saturated solution (glass-rod test: "If the solution is saturated, crystals will form on the glass rod") — the 1.4 term used without re-teaching, load-bearing for the method.
- `NOTE` Separation techniques - IGCSE Chemistry Revision Notes.md — "The solution is heated, allowing the solvent to evaporate, leaving a saturated solution behind"

```diff
@@ -1771,7 +1771,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.10 @ Separation techniques (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-CRYSTALLISATION
```

### 7. `4CH1-CON-DIFFUSION EXPLAINED_BY 4CH1-CON-STATE-PARTICLE-MODEL` [high]

- node 4CH1-CON-DIFFUSION — Diffusion in gases and liquids (CONCEPT)
-   spec 4CH1-1.3 [CORE]: understand how the results of experiments involving the dilution of coloured solutions and di...
- node 4CH1-CON-STATE-PARTICLE-MODEL — Particle arrangement, movement and energy in the three states (CONCEPT)
-   spec 4CH1-1.1 [CORE]: understand the three states of matter in terms of the arrangement, movement and energy of the...
-   spec 4CH1-1.3 [SUPPORTING]: understand how the results of experiments involving the dilution of coloured solutions and di...
- derivation: SINGLE_SOURCE_CAUSAL_TEACHING — The note explains diffusion CAUSALLY by particle behavior ("due to the random motion"): the high-to-low movement and the gas-jar/liquid experiments are each explained by random motion + gaps between particles — the "due to" sentence is the direct causal link.
- `NOTE` Diffusion - IGCSE Chemistry Revision Notes.md — "Diffusion occurs in gases and liquids, due to the random motion of their particles"

```diff
@@ -2744,7 +2744,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.3 @ Diffusion (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-DILUTION
```

### 8. `4CH1-CON-DILUTION EXPLAINED_BY 4CH1-CON-STATE-PARTICLE-MODEL` [high]

- node 4CH1-CON-DILUTION — Dilution of coloured solutions (CONCEPT)
-   spec 4CH1-1.3 [CORE]: understand how the results of experiments involving the dilution of coloured solutions and di...
- node 4CH1-CON-STATE-PARTICLE-MODEL — Particle arrangement, movement and energy in the three states (CONCEPT)
-   spec 4CH1-1.1 [CORE]: understand the three states of matter in terms of the arrangement, movement and energy of the...
-   spec 4CH1-1.3 [SUPPORTING]: understand how the results of experiments involving the dilution of coloured solutions and di...
- derivation: SINGLE_SOURCE_CAUSAL_TEACHING — The note explains the dilution observation (colour fades but does not disappear, particles spread but remain) BY the particle model — the "therefore the particles must be very small" sentence is the taught inference, the exact 1.3 evidence relation.
- `NOTE` Diffusion - IGCSE Chemistry Revision Notes.md — "This indicates that there are a lot of particles in a small amount of potassium manganate (VII) and therefo..."

```diff
@@ -2767,7 +2767,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.3 @ Diffusion (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-EQ-SYMBOL
```

### 9. `4CH1-CON-EVAPORATION-BOILING REQUIRES_PREREQUISITE 4CH1-CON-STATE-CHANGES` [high]

- node 4CH1-CON-EVAPORATION-BOILING — Evaporation and its distinction from boiling (CONCEPT)
-   spec 4CH1-1.2 [ENRICHMENT]: understand the interconversions between the three states of matter in terms of: • the names o...
- node 4CH1-CON-STATE-CHANGES — Interconversions between the three states (melting, freezing, boiling, condensation, sublimation) (CONCEPT)
-   spec 4CH1-1.2 [CORE]: understand the interconversions between the three states of matter in terms of: • the names o...
- derivation: DEFINITIONAL_DEPENDENCY — The evaporation-vs-boiling distinction is defined against boiling (a named interconversion with its boiling point); the note introduces boiling before contrasting evaporation with it ("a key difference between boiling and evaporation").
- `NOTE` Changing states of matter - IGCSE Chemistry Revision Notes.md — "It can happen at temperatures below the boiling point of the liquid"

```diff
@@ -1890,7 +1890,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.2 @ Changing states of matter (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-EXP-FORMULA-DEDUCTION
```

### 10. `4CH1-CON-FILTRATION REQUIRES_PREREQUISITE 4CH1-CON-SOLUTION` [high]

- node 4CH1-CON-FILTRATION — Filtration (CONCEPT)
-   spec 4CH1-1.10 [CORE]: describe these experimental techniques for the separation of mixtures: 简单 distillation fracti...
- node 4CH1-CON-SOLUTION — Solution, solute and solvent (CONCEPT)
-   spec 4CH1-1.4 [CORE]: know what is meant by the terms: • solvent • solute • solution • saturated solution.
- derivation: USED_WITHOUT_RETEACHING — The technique is defined by its object (undissolved solid vs liquid/solution) presupposing the dissolved/undissolved distinction carried by the 1.4 solution vocabulary; used without re-teaching.
- `NOTE` Separation techniques - IGCSE Chemistry Revision Notes.md — "Filtration is used to separate an undissolved solid from a mixture of the solid and a liquid / solution"

```diff
@@ -1936,7 +1936,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.10 @ Separation techniques (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-FRACTIONAL-DISTILLATION
```

### 11. `4CH1-CON-FRACTIONAL-DISTILLATION REQUIRES_PREREQUISITE 4CH1-CON-SIMPLE-DISTILLATION` [high]

- node 4CH1-CON-FRACTIONAL-DISTILLATION — Fractional distillation (CONCEPT)
-   spec 4CH1-1.10 [CORE]: describe these experimental techniques for the separation of mixtures: 简单 distillation fracti...
- node 4CH1-CON-SIMPLE-DISTILLATION — Simple distillation (CONCEPT)
-   spec 4CH1-1.10 [CORE]: describe these experimental techniques for the separation of mixtures: 简单 distillation fracti...
- derivation: EXPLICIT_TEACH_SEQUENCE — The note teaches simple distillation FIRST, then fractional as the controlled version of the same process (heat -> evaporate -> condenser -> collect), adding boiling-point control per component; the fractional description presupposes the distillation process rather than re-teaching it.
- `NOTE` Separation techniques - IGCSE Chemistry Revision Notes.md — "All of the substance is evaporated and collected, leaving behind the other components(s) of the mixture"

```diff
@@ -1960,7 +1960,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.10 @ Separation techniques (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-GAS-VOL-CALC
```

### 12. `4CH1-CON-MIXTURE REQUIRES_PREREQUISITE 4CH1-CON-COMPOUND` [high]

- node 4CH1-CON-MIXTURE — Mixture (CONCEPT)
-   spec 4CH1-1.8 [CORE]: understand how to classify a substance as an element,compound or mixture
- node 4CH1-CON-COMPOUND — Compound (CONCEPT)
-   spec 4CH1-1.8 [CORE]: understand how to classify a substance as an element,compound or mixture
- derivation: DEFINITIONAL_DEPENDENCY — The mixture definition is stated IN TERMS OF elements and compounds ("elements and/or compounds ... not chemically combined"); the not-chemically-combined contrast presupposes the compound concept. The direct mixture->element edge is transitively subsumed via this chain (held candidate B1-H-01).
- `NOTE` Element, Compound or Mixture  Edexcel IGCSE Chemistry Revision Notes 2017.md — "A combination of two or more substances (elements and/or compounds) that are not chemically combined"

```diff
@@ -2056,7 +2056,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.8 @ Element, Compound or Mixture (2026-09-11)
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

### 13. `4CH1-CON-PURE-SUBSTANCE REQUIRES_PREREQUISITE 4CH1-CON-COMPOUND` [high]

- node 4CH1-CON-PURE-SUBSTANCE — Pure substance (chemical sense) and fixed melting/boiling points (CONCEPT)
-   spec 4CH1-1.9 [CORE]: understand that a pure substance has a fixed melting and boiling point,but that a mixture may...
- node 4CH1-CON-COMPOUND — Compound (CONCEPT)
-   spec 4CH1-1.8 [CORE]: understand how to classify a substance as an element,compound or mixture
- derivation: DEFINITIONAL_DEPENDENCY — The chemical purity definition is stated IN TERMS OF elements and compounds ("a single element or compound"); the compound edge is emitted as the chain representative (pure->compound->element; the direct pure->element edge is transitively subsumed — held candidate B1-H-10).
- `NOTE` Pure substances - IGCSE Chemistry Revision Notes.md — "In chemistry, a pure substance may consist of a single element or compound which contains no other substances"

```diff
@@ -2313,7 +2313,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.9 @ Pure substances (2026-09-11)
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

### 14. `4CH1-CON-PURE-SUBSTANCE REQUIRES_PREREQUISITE 4CH1-CON-STATE-CHANGES` [high]

- node 4CH1-CON-PURE-SUBSTANCE — Pure substance (chemical sense) and fixed melting/boiling points (CONCEPT)
-   spec 4CH1-1.9 [CORE]: understand that a pure substance has a fixed melting and boiling point,but that a mixture may...
- node 4CH1-CON-STATE-CHANGES — Interconversions between the three states (melting, freezing, boiling, condensation, sublimation) (CONCEPT)
-   spec 4CH1-1.2 [CORE]: understand the interconversions between the three states of matter in terms of: • the names o...
- derivation: USED_WITHOUT_RETEACHING — The 1.9 criterion USES melting and boiling (and their fixed points — taught under 1.2) without re-teaching them; the note assumes the student knows what melting/boiling points are when it states the sharp-vs-range contrast.
- `NOTE` Pure substances - IGCSE Chemistry Revision Notes.md — "Pure substances melt and boil at specific and sharp temperatures"

```diff
@@ -2335,7 +2335,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.9 @ Pure substances (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-REACTING-MASS
```

### 15. `4CH1-CON-RF-VALUE REQUIRES_PREREQUISITE 4CH1-CON-CHROMATOGRAM-INTERPRETATION` [high]

- node 4CH1-CON-RF-VALUE — Retention factor (Rf) (CONCEPT)
-   spec 4CH1-1.12 [CORE]: understand how to use the calculation of $ R_{f} $ values to identify the components of a mix...
- node 4CH1-CON-CHROMATOGRAM-INTERPRETATION — Interpreting chromatograms (CONCEPT)
-   spec 4CH1-1.11 [CORE]: understand how a chromatogram provides information about the composition of a mixture
- derivation: USED_WITHOUT_RETEACHING — The Rf calculation takes its two measurements FROM the chromatogram's structure (baseline, spots, solvent front) presupposing the 1.11 reading conventions — the examiner tip's measurement rule is the direct use-without-reteaching evidence.
- `NOTE` Interpreting chromatograms - IGCSE Chemistry Revision Notes.md — "For both measurements, the distance should be measured from the baseline to the centre of the dot."

```diff
@@ -2425,7 +2425,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.12 @ Interpreting chromatograms (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-SATURATED-SOLUTION
```

### 16. `4CH1-CON-SATURATED-SOLUTION REQUIRES_PREREQUISITE 4CH1-CON-SOLUTION` [high]

- node 4CH1-CON-SATURATED-SOLUTION — Saturated solution (CONCEPT)
-   spec 4CH1-1.4 [CORE]: know what is meant by the terms: • solvent • solute • solution • saturated solution.
-   spec 4CH1-1.10 [SUPPORTING]: describe these experimental techniques for the separation of mixtures: 简单 distillation fracti...
- node 4CH1-CON-SOLUTION — Solution, solute and solvent (CONCEPT)
-   spec 4CH1-1.4 [CORE]: know what is meant by the terms: • solvent • solute • solution • saturated solution.
- derivation: DEFINITIONAL_DEPENDENCY — The saturated-solution definition is stated IN TERMS OF solution/solute/solvent ("maximum concentration of solute dissolved in the solvent") — the term triple is the definitional operand set, taught as the preceding table rows in the same note.
- `NOTE` Solutions - IGCSE Chemistry Revision Notes.md — "A solution with the maximum concentration of solute dissolved in the solvent"

```diff
@@ -2447,7 +2447,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.4 @ Solutions (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-SIMPLE-DISTILLATION
```

### 17. `4CH1-CON-SIMPLE-DISTILLATION REQUIRES_PREREQUISITE 4CH1-CON-SOLUTION` [high]

- node 4CH1-CON-SIMPLE-DISTILLATION — Simple distillation (CONCEPT)
-   spec 4CH1-1.10 [CORE]: describe these experimental techniques for the separation of mixtures: 简单 distillation fracti...
- node 4CH1-CON-SOLUTION — Solution, solute and solvent (CONCEPT)
-   spec 4CH1-1.4 [CORE]: know what is meant by the terms: • solvent • solute • solution • saturated solution.
- derivation: USED_WITHOUT_RETEACHING — The technique is defined by WHAT it separates, stated in solution vocabulary (liquid + soluble solid, from a solution) presupposing the 1.4 term triple; the separation note uses the terms without re-teaching them (they are the Solutions note's job).
- `NOTE` Separation techniques - IGCSE Chemistry Revision Notes.md — "Simple distillation is used to separate a liquid and soluble solid from a solution"

```diff
@@ -2469,7 +2469,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.10 @ Separation techniques (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-SIMPLE-DISTILLATION
```

### 18. `4CH1-CON-SIMPLE-DISTILLATION REQUIRES_PREREQUISITE 4CH1-CON-STATE-CHANGES` [high]

- node 4CH1-CON-SIMPLE-DISTILLATION — Simple distillation (CONCEPT)
-   spec 4CH1-1.10 [CORE]: describe these experimental techniques for the separation of mixtures: 简单 distillation fracti...
- node 4CH1-CON-STATE-CHANGES — Interconversions between the three states (melting, freezing, boiling, condensation, sublimation) (CONCEPT)
-   spec 4CH1-1.2 [CORE]: understand the interconversions between the three states of matter in terms of: • the names o...
- derivation: USED_WITHOUT_RETEACHING — Distillation IS applied evaporation + condensation: the method description uses "evaporates", "vapour", "cools and condenses" — the 1.2 interconversion processes — without re-teaching them. Cross-subtopic prerequisite (1.2 -> 1.10).
- `NOTE` Separation techniques - IGCSE Chemistry Revision Notes.md — "The vapour passes through the condenser, where it cools and condenses, turning into the pure liquid that is..."

```diff
@@ -2492,7 +2492,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.10 @ Separation techniques (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-SOLUBILITY
```

### 19. `4CH1-CON-SOLUBILITY REQUIRES_PREREQUISITE 4CH1-CON-SATURATED-SOLUTION` [high]

- node 4CH1-CON-SOLUBILITY — Solubility (g per 100 g of solvent) (CONCEPT)
-   spec 4CH1-1.5C [CORE]: know what is meant by the term solubility in the units g per 100 g of solvent
- node 4CH1-CON-SATURATED-SOLUTION — Saturated solution (CONCEPT)
-   spec 4CH1-1.4 [CORE]: know what is meant by the terms: • solvent • solute • solution • saturated solution.
-   spec 4CH1-1.10 [SUPPORTING]: describe these experimental techniques for the separation of mixtures: 简单 distillation fracti...
- derivation: DEFINITIONAL_DEPENDENCY — Solubility (the g-per-100g measurement) is defined operationally via the saturation point ("the maximum mass ... before a saturated solution is formed"); the mapped note uses the saturated-solution concept to define what is measured.
- `NOTE` Solubility - IGCSE Chemistry Revision Notes.md — "the maximum mass of solute that can be dissolved in 100 g of water before a saturated solution is formed, i..."

```diff
@@ -2515,7 +2515,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.5C @ Solubility (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-SOLUBILITY-CURVE
```

### 20. `4CH1-CON-SOLUBILITY-CURVE REQUIRES_PREREQUISITE 4CH1-CON-SOLUBILITY` [high]

- node 4CH1-CON-SOLUBILITY-CURVE — Solubility curves (plotting and interpreting) (CONCEPT)
-   spec 4CH1-1.6C [CORE]: understand how to plot and interpret solubility curves
- node 4CH1-CON-SOLUBILITY — Solubility (g per 100 g of solvent) (CONCEPT)
-   spec 4CH1-1.5C [CORE]: know what is meant by the term solubility in the units g per 100 g of solvent
- derivation: DEFINITIONAL_DEPENDENCY — A solubility curve is DEFINED as the graph OF solubility against temperature; interpreting/plotting the curve presupposes the solubility quantity it plots (definition vs procedure split — the 1.32/1.33 pattern).
- `NOTE` Solubility - IGCSE Chemistry Revision Notes.md — "Solubility graphs or curves represent solubility in g per 100 g of water plotted against temperature"

```diff
@@ -2537,7 +2537,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.6C @ Solubility (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-STATE-CHANGES
```

### 21. `4CH1-CON-STATE-CHANGES REQUIRES_PREREQUISITE 4CH1-CON-STATE-PARTICLE-MODEL` [high]

- node 4CH1-CON-STATE-CHANGES — Interconversions between the three states (melting, freezing, boiling, condensation, sublimation) (CONCEPT)
-   spec 4CH1-1.2 [CORE]: understand the interconversions between the three states of matter in terms of: • the names o...
- node 4CH1-CON-STATE-PARTICLE-MODEL — Particle arrangement, movement and energy in the three states (CONCEPT)
-   spec 4CH1-1.1 [CORE]: understand the three states of matter in terms of the arrangement, movement and energy of the...
-   spec 4CH1-1.3 [SUPPORTING]: understand how the results of experiments involving the dilution of coloured solutions and di...
- derivation: USED_WITHOUT_RETEACHING — The state-change sections explain melting/boiling/condensation in terms of particle energy and forces between particles without re-teaching the particle model (the properties table comes first in the note and is presupposed).
- `NOTE` Changing states of matter - IGCSE Chemistry Revision Notes.md — "State changes require a change in the energy of the particles"

```diff
@@ -2559,7 +2559,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.2 @ Changing states of matter (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-STATE-PARTICLE-MODEL
```

### 22. `4CH1-CON-STATE-PARTICLE-MODEL REQUIRES_PREREQUISITE 4CH1-CON-STATES-THREE` [high]

- node 4CH1-CON-STATE-PARTICLE-MODEL — Particle arrangement, movement and energy in the three states (CONCEPT)
-   spec 4CH1-1.1 [CORE]: understand the three states of matter in terms of the arrangement, movement and energy of the...
-   spec 4CH1-1.3 [SUPPORTING]: understand how the results of experiments involving the dilution of coloured solutions and di...
- node 4CH1-CON-STATES-THREE — The three states of matter (solid, liquid, gas) (CONCEPT)
-   spec 4CH1-1.1 [CORE]: understand the three states of matter in terms of the arrangement, movement and energy of the...
- derivation: DEFINITIONAL_DEPENDENCY — The particle model is the model OF the three states — describing arrangement/movement/energy per state presupposes the states themselves; the note introduces and names the three states before representing them by the sphere model.
- `NOTE` Changing states of matter - IGCSE Chemistry Revision Notes.md — "The three states of matter can be represented by a simple model"

```diff
@@ -2581,7 +2581,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.1 @ Changing states of matter (2026-09-11)
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

### 23. `4CH1-MIS-CRYSTALLISATION-DRYNESS REMEDIATED_BY 4CH1-CON-SATURATED-SOLUTION` [high]

- node 4CH1-MIS-CRYSTALLISATION-DRYNESS — Obtaining crystals by evaporating to dryness (MISCONCEPTION)
- node 4CH1-CON-SATURATED-SOLUTION — Saturated solution (CONCEPT)
-   spec 4CH1-1.4 [CORE]: know what is meant by the terms: • solvent • solute • solution • saturated solution.
-   spec 4CH1-1.10 [SUPPORTING]: describe these experimental techniques for the separation of mixtures: 简单 distillation fracti...
- derivation: EXPLICIT_TEACH_SEQUENCE — Remediation = the correct method's key step: stop heating at the saturated solution and cool slowly so crystals grow (the MS itself awards "heat to form a saturated/concentrated solution ... leave to crystallise"); the saturating step is the exact corrective content for the to-dryness error.
- `NOTE` Separation techniques - IGCSE Chemistry Revision Notes.md — "The solution is heated, allowing the solvent to evaporate, leaving a saturated solution behind"

```diff
@@ -2979,7 +2979,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.10 @ Separation techniques (2026-09-11)
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

### 24. `4CH1-MIS-CRYSTALLISATION-DRYNESS WRONG_ANSWER_PATTERN 4CH1-CON-CRYSTALLISATION` [high]

- node 4CH1-MIS-CRYSTALLISATION-DRYNESS — Obtaining crystals by evaporating to dryness (MISCONCEPTION)
- node 4CH1-CON-CRYSTALLISATION — Crystallisation (CONCEPT)
-   spec 4CH1-1.10 [CORE]: describe these experimental techniques for the separation of mixtures: 简单 distillation fracti...
- derivation: ASSESSMENT_DOCUMENTED — The wrong answer is documented against the 1.10/1.7C-class crystallisation method question (ECM2 MS Q1(d) — salt-from-solution preparation): evaporating to dryness zeroes the question; the concept being tested is the crystallisation technique.
- `MARK_SCHEME` ECM2_MS_P1.txt — "If evaporated to dryness then award no marks for whole question"

```diff
@@ -2911,7 +2911,9 @@ edges:
       sha1 3c31a1a0e154)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-MIS-GAS-PARTICLES-TOUCH
```

### 25. `4CH1-MIS-GAS-PARTICLES-TOUCH REMEDIATED_BY 4CH1-CON-STATE-PARTICLE-MODEL` [high]

- node 4CH1-MIS-GAS-PARTICLES-TOUCH — Drawing gas particles touching each other or joined by bonds (MISCONCEPTION)
- node 4CH1-CON-STATE-PARTICLE-MODEL — Particle arrangement, movement and energy in the three states (CONCEPT)
-   spec 4CH1-1.1 [CORE]: understand the three states of matter in terms of the arrangement, movement and energy of the...
-   spec 4CH1-1.3 [SUPPORTING]: understand how the results of experiments involving the dilution of coloured solutions and di...
- derivation: EXPLICIT_TEACH_SEQUENCE — Remediation = teaching the correct model itself: gas particles far apart, moving quickly and randomly (the properties table + diagram descriptions). Unlike the pilot misconception pairs, the misconception target and the remediating concept coincide — there is no deeper in-slice concept below the particle model, so the remediation edge returns to the same concept the wrong answer misrepresents.
- `NOTE` Changing states of matter - IGCSE Chemistry Revision Notes.md — "the particles in a gas are far apart and moving quickly and randomly"

```diff
@@ -3026,6 +3026,8 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.1 @ Changing states of matter (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
```

### 26. `4CH1-MIS-GAS-PARTICLES-TOUCH WRONG_ANSWER_PATTERN 4CH1-CON-STATE-PARTICLE-MODEL` [high]

- node 4CH1-MIS-GAS-PARTICLES-TOUCH — Drawing gas particles touching each other or joined by bonds (MISCONCEPTION)
- node 4CH1-CON-STATE-PARTICLE-MODEL — Particle arrangement, movement and energy in the three states (CONCEPT)
-   spec 4CH1-1.1 [CORE]: understand the three states of matter in terms of the arrangement, movement and energy of the...
-   spec 4CH1-1.3 [SUPPORTING]: understand how the results of experiments involving the dilution of coloured solutions and di...
- derivation: ASSESSMENT_DOCUMENTED — The wrong answer is documented against the 1.1-assessed drawing task (particles in a gas): SOM MS Q3(a)(i) and Q4(a) both reject touching/bonded circles; the concept whose understanding is being tested is the particle model of the states.
- `MARK_SCHEME` SOM_MS_P1.txt — "Reject any touching circles"

```diff
@@ -2933,7 +2933,9 @@ edges:
       sha1 e41e67f27cd5)
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

### 27. `4CH1-PR-01 REQUIRES_PREREQUISITE 4CH1-CON-SATURATED-SOLUTION` [high]

- node 4CH1-CON-SATURATED-SOLUTION — Saturated solution (CONCEPT)
-   spec 4CH1-1.4 [CORE]: know what is meant by the terms: • solvent • solute • solution • saturated solution.
-   spec 4CH1-1.10 [SUPPORTING]: describe these experimental techniques for the separation of mixtures: 简单 distillation fracti...
- derivation: USED_WITHOUT_RETEACHING — The practical USES the saturation criterion as its key method step (add solid "until no more will dissolve and some undissolved solid remains ... This ensures that the solution is saturated") without re-teaching it — the concept is load-bearing for why the method works.
- `NOTE` Investigating solubility - IGCSE Chemistry Revision Notes.md — "This ensures that the solution is saturated"

```diff
@@ -2652,7 +2652,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.7C @ Investigating solubility (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-12'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-PR-01
```

### 28. `4CH1-PR-01 REQUIRES_PREREQUISITE 4CH1-CON-SOLUBILITY` [high]

- node 4CH1-CON-SOLUBILITY — Solubility (g per 100 g of solvent) (CONCEPT)
-   spec 4CH1-1.5C [CORE]: know what is meant by the term solubility in the units g per 100 g of solvent
- derivation: USED_WITHOUT_RETEACHING — The practical's final step computes THE 1.5C quantity ("solubility in g per 100 g water" via mass-of-solute / mass-of-water x 100) without re-teaching the definition — the practical's output IS a solubility value.
- `NOTE` Investigating solubility - IGCSE Chemistry Revision Notes.md — "Calculate the solubility of copper(II) sulfate in water at 30°C using the masses recorded"

```diff
@@ -2674,7 +2674,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.7C + 4CH1-1.5C @ Investigating solubility (2026-09-11)
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
@@ -66,8 +66,10 @@ meta:
     remediated_by_edges: 4
     requires_prerequisite_edges: 47
     wrong_answer_pattern_edges: 3
-    promoted_edges: 28
-    human_validated_edges: 28
+    promoted_edges: 56
+    human_validated_edges: 56
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
| `4CH1-CON-HEATING-CONSTANT-MASS` | Heating to constant mass | CONCEPT | 4CH1-1.7C (ENRICHMENT) | high |
| `4CH1-CON-MIXTURE` | Mixture | CONCEPT | 4CH1-1.8 (CORE) | high |
| `4CH1-CON-MOLAR-GAS-VOL` | Molar gas volume at RTP (24 dm3) | CONCEPT | 4CH1-1.35C (CORE) | high |
| `4CH1-CON-MOLAR-MASS` | Molar mass | CONCEPT | 4CH1-1.28 (CORE) | high |
| `4CH1-CON-MOLAR-RATIO` | Molar ratio from balanced equations | CONCEPT | 4CH1-1.29 (CORE) | high |
| `4CH1-CON-MOLE` | The mole (unit of amount of substance) | CONCEPT | 4CH1-1.27 (CORE) | high |
| `4CH1-CON-MOLE-MASS-CONV` | Mole-mass conversion | CONCEPT | 4CH1-1.28 (CORE) | high |
| `4CH1-CON-MOLECULAR-FORMULA` | Molecular formula | CONCEPT | 4CH1-1.32 (CORE); 4CH1-1.33 (CORE) | high |
| `4CH1-CON-MR` | Relative formula mass (Mr) | CONCEPT | 4CH1-1.26 (CORE); 4CH1-1.28 (CORE) | high |
| `4CH1-CON-PERCENT-YIELD` | Percentage yield | CONCEPT | 4CH1-1.30 (CORE) | high |
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
| `4CH1-CON-THEOR-YIELD` | Theoretical yield | CONCEPT | 4CH1-1.30 (CORE) | high |
| `4CH1-CON-VOL-CONVERSION` | Volume unit conversion (cm3/dm3) | CONCEPT | 4CH1-1.34C (CORE) | high |
| `4CH1-CON-WATER-CRYST` | Water of crystallisation and hydrated salts | CONCEPT | 4CH1-1.31 (CORE) | high |
| `4CH1-CON-YIELD` | Yield (actual yield) | CONCEPT | 4CH1-1.30 (CORE) | high |
| `4CH1-CON-YIELD-FACTORS` | Factors reducing yield | CONCEPT | 4CH1-1.30 (ENRICHMENT) | high |
| `4CH1-MIS-CONC-UNIT` | Failing to convert cm3 to dm3 in concentration calculations | MISCONCEPTION |  | high |
| `4CH1-MIS-CRYSTALLISATION-DRYNESS` | Obtaining crystals by evaporating to dryness | MISCONCEPTION |  | high |
| `4CH1-MIS-EQ-SUBSCRIPT` | Balancing equations by altering subscripts | MISCONCEPTION |  | high |
| `4CH1-MIS-GAS-PARTICLES-TOUCH` | Drawing gas particles touching each other or joined by bonds | MISCONCEPTION |  | high |

