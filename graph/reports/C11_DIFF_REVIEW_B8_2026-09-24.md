# C11 Diff Review Bundle — pending §18 edge promotions (generated 2026-09-24)

- baseline commit: `c3baa45`
- state fingerprint: `5966412bcadc` (promo_count=206)
- actionable: 10 edges (clean 10 / pending-flagged 0); not-actionable: 5; nodes awaiting a pathway: 165
- preview fidelity: simulator re-emits graph/igcse-chemistry/concept_edges under the generator's own serialization contract with a byte-identity guard — what you read is what G13 will write.

## Batch approval

```bash
cd work/syllabai-resources && python3 scripts/c11_diff_review.py approve \
  '4CH1-CON-ANION-TESTS REQUIRES_PREREQUISITE 4CH1-CON-GAS-TESTS' \
  '4CH1-CON-ANION-TESTS REQUIRES_PREREQUISITE 4CH1-CON-ION-CHARGE-RULES' \
  '4CH1-CON-CATION-TESTS REQUIRES_PREREQUISITE 4CH1-CON-GAS-TESTS' \
  '4CH1-CON-CATION-TESTS REQUIRES_PREREQUISITE 4CH1-CON-ION-CHARGE-RULES' \
  '4CH1-CON-FLAME-TEST RELATED_TO 4CH1-CON-CATION-TESTS' \
  '4CH1-CON-WATER-PURITY-TEST REQUIRES_PREREQUISITE 4CH1-CON-PURE-SUBSTANCE' \
  '4CH1-MIS-GLOWING-SPLINT-HYDROGEN REMEDIATED_BY 4CH1-CON-GAS-TESTS' \
  '4CH1-MIS-GLOWING-SPLINT-HYDROGEN WRONG_ANSWER_PATTERN 4CH1-CON-GAS-TESTS' \
  '4CH1-MIS-HALIDE-TEST-HCL REMEDIATED_BY 4CH1-CON-ANION-TESTS' \
  '4CH1-MIS-HALIDE-TEST-HCL WRONG_ANSWER_PATTERN 4CH1-CON-ANION-TESTS' \
  --by <operator> --date 2026-09-24 --review-ref graph/reports/C11_DIFF_REVIEW_B8_2026-09-24.md
```

Pending-flagged (PENDING operator_decision) edges are excluded from the command above; approving them additionally requires `--include-pending` — that flag records the explicit decision this bundle presents.

## Index

| # | identity | confidence | flag |
|---|----------|------------|------|
| 1 | `4CH1-CON-ANION-TESTS REQUIRES_PREREQUISITE 4CH1-CON-GAS-TESTS` | high |  |
| 2 | `4CH1-CON-ANION-TESTS REQUIRES_PREREQUISITE 4CH1-CON-ION-CHARGE-RULES` | high |  |
| 3 | `4CH1-CON-CATION-TESTS REQUIRES_PREREQUISITE 4CH1-CON-GAS-TESTS` | high |  |
| 4 | `4CH1-CON-CATION-TESTS REQUIRES_PREREQUISITE 4CH1-CON-ION-CHARGE-RULES` | high |  |
| 5 | `4CH1-CON-FLAME-TEST RELATED_TO 4CH1-CON-CATION-TESTS` | medium |  |
| 6 | `4CH1-CON-WATER-PURITY-TEST REQUIRES_PREREQUISITE 4CH1-CON-PURE-SUBSTANCE` | high |  |
| 7 | `4CH1-MIS-GLOWING-SPLINT-HYDROGEN REMEDIATED_BY 4CH1-CON-GAS-TESTS` | high |  |
| 8 | `4CH1-MIS-GLOWING-SPLINT-HYDROGEN WRONG_ANSWER_PATTERN 4CH1-CON-GAS-TESTS` | high |  |
| 9 | `4CH1-MIS-HALIDE-TEST-HCL REMEDIATED_BY 4CH1-CON-ANION-TESTS` | high |  |
| 10 | `4CH1-MIS-HALIDE-TEST-HCL WRONG_ANSWER_PATTERN 4CH1-CON-ANION-TESTS` | high |  |

## Pending items — the exact diff each approval applies

### 1. `4CH1-CON-ANION-TESTS REQUIRES_PREREQUISITE 4CH1-CON-GAS-TESTS` [high]

- node 4CH1-CON-ANION-TESTS — Tests for aqueous anions (halides, sulfate, carbonate) (CONCEPT)
-   spec 4CH1-2.48 [CORE]: describe tests for these anions:
- node 4CH1-CON-GAS-TESTS — Chemical tests for gases (hydrogen, oxygen, carbon dioxide, ammonia, chlorine) (CONCEPT)
-   spec 4CH1-2.44 [CORE]: describe tests for these gases:
- derivation: EXPLICIT_TEACH_SEQUENCE — The 2.48 carbonate route is DEFINED by the 2.44 CO2 gas test: "using hydrochloric acid and identifying the gas evolved" (the spec bullet's own words) — the identification IS the limewater cloudiness result, which the anion note states and the gas note owns as the 2.44 test. Without the gas-test family the carbonate route has no identification step. (The session-59 ruling's limewater/CO2-test future note lands exactly here.)
- `NOTE` Tests for Anions  Edexcel IGCSE Chemistry Revision Notes 2017.md — "Bubble the gas released through limewater"
- `NOTE` Gas tests - IGCSE Chemistry Revision Notes.md — "If the gas is carbon dioxide, the limewater turns cloudy white"

```diff
@@ -6138,7 +6138,9 @@ edges:
       limewater/CO2-test future note lands exactly here.)'
     upstream: T-C10 HUMAN_VALIDATED 4CH1-2.48/2.44 (2026-09-11)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-24'
   version: 1
   created_at: '2026-09-24'
 - source: 4CH1-CON-ANION-TESTS
```

### 2. `4CH1-CON-ANION-TESTS REQUIRES_PREREQUISITE 4CH1-CON-ION-CHARGE-RULES` [high]

- node 4CH1-CON-ANION-TESTS — Tests for aqueous anions (halides, sulfate, carbonate) (CONCEPT)
-   spec 4CH1-2.48 [CORE]: describe tests for these anions:
- node 4CH1-CON-ION-CHARGE-RULES — Common ion charges (group-based and named-ion table, with the deduction rule) (CONCEPT)
-   spec 4CH1-1.38 [CORE]: know the charges of these ions:
- derivation: USED_WITHOUT_RETEACHING — SANCTIONED BOUNDARY EDGE (the session-61 ruling, target 1 — the batch-3 CON-ION-CHARGE-RULES owner): the 2.48 tests are organised by ION identity — the spec bullets name the anions with their charges (Cl-, Br-, I-, SO4 2-, CO3 2-) and the note's equations (Ba 2+ + SO4 2- -> BaSO4) presuppose the named-ion/charge vocabulary applied as given, never re-taught by the 2.48 note (the B7-E-10 class at the anion boundary).
- `NOTE` Tests for Anions  Edexcel IGCSE Chemistry Revision Notes 2017.md — "Sulfate compounds contain the sulfate ion, SO42-"
- `NOTE` Tests for Anions  Edexcel IGCSE Chemistry Revision Notes 2017.md — "Carbonate compounds contain the carbonate ion, CO32-"

```diff
@@ -6166,7 +6166,9 @@ edges:
       class at the anion boundary).'
     upstream: T-C10 HUMAN_VALIDATED 4CH1-2.48 (2026-09-11); the batch-3 record (CON-ION-CHARGE-RULES)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-24'
   version: 1
   created_at: '2026-09-24'
 - source: 4CH1-CON-ANODE-CATHODE
```

### 3. `4CH1-CON-CATION-TESTS REQUIRES_PREREQUISITE 4CH1-CON-GAS-TESTS` [high]

- node 4CH1-CON-CATION-TESTS — Tests for aqueous cations (sodium hydroxide precipitate colours; ammonium ion via ammonia gas) (CONCEPT)
-   spec 4CH1-2.47 [CORE]: describe tests for these cations:
- node 4CH1-CON-GAS-TESTS — Chemical tests for gases (hydrogen, oxygen, carbon dioxide, ammonia, chlorine) (CONCEPT)
-   spec 4CH1-2.44 [CORE]: describe tests for these gases:
- derivation: EXPLICIT_TEACH_SEQUENCE — The 2.47 NH4+ route is DEFINED by the 2.44 gas test: "using sodium hydroxide solution and identifying the gas evolved" (the spec bullet's own words) — the identification IS the ammonia test (the note's own link sentence re-states the damp-red-litmus result; the gas note's ammonia section names the ammonium-ion + NaOH context). Without the gas-test family the cation route has no identification step.
- `NOTE` Tests for cations - IGCSE Chemistry Revision Notes.md — "Test for ammonia gas: Ammonia turns damp red litmus paper blue"
- `NOTE` Gas tests - IGCSE Chemistry Revision Notes.md — "If you are testing for ammonia produced from ammonium ions and sodium hydroxide, avoiding touching the side..."

```diff
@@ -6431,7 +6431,9 @@ edges:
       no identification step.'
     upstream: T-C10 HUMAN_VALIDATED 4CH1-2.47/2.44 (2026-09-11)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-24'
   version: 1
   created_at: '2026-09-24'
 - source: 4CH1-CON-CATION-TESTS
```

### 4. `4CH1-CON-CATION-TESTS REQUIRES_PREREQUISITE 4CH1-CON-ION-CHARGE-RULES` [high]

- node 4CH1-CON-CATION-TESTS — Tests for aqueous cations (sodium hydroxide precipitate colours; ammonium ion via ammonia gas) (CONCEPT)
-   spec 4CH1-2.47 [CORE]: describe tests for these cations:
- node 4CH1-CON-ION-CHARGE-RULES — Common ion charges (group-based and named-ion table, with the deduction rule) (CONCEPT)
-   spec 4CH1-1.38 [CORE]: know the charges of these ions:
- derivation: USED_WITHOUT_RETEACHING — SANCTIONED BOUNDARY EDGE (the session-61 ruling, target 2 — the second edge into the batch-3 owner; the batch-5 x2-into-one-owner precedent): the 2.47 tests are likewise organised by ION identity — the spec bullets name NH4+, Cu2+, Fe2+, Fe3+ and the note's precipitate table writes the ionic equations (Cu2+ + 2OH- -> Cu(OH)2) — the named-ion/charge vocabulary applied as given (the B7-E-10 class at the cation boundary).
- `NOTE` Tests for cations - IGCSE Chemistry Revision Notes.md — "Test for ammonium ion, NH4+"
- `NOTE` Tests for cations - IGCSE Chemistry Revision Notes.md — "Cu2+ (aq) + 2OH– (aq) → Cu(OH)2 (s)"

```diff
@@ -6459,7 +6459,9 @@ edges:
       given (the B7-E-10 class at the cation boundary).'
     upstream: T-C10 HUMAN_VALIDATED 4CH1-2.47 (2026-09-11); the batch-3 record (CON-ION-CHARGE-RULES)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-24'
   version: 1
   created_at: '2026-09-24'
 - source: 4CH1-CON-CHROMATOGRAM-INTERPRETATION
```

### 5. `4CH1-CON-FLAME-TEST RELATED_TO 4CH1-CON-CATION-TESTS` [medium]

- node 4CH1-CON-FLAME-TEST — Flame tests for metal cations (technique and flame colours) (CONCEPT)
-   spec 4CH1-2.45 [CORE]: describe how to carry out a flame test
-   spec 4CH1-2.46 [CORE]: know the colours formed in flame tests for these cations:
- node 4CH1-CON-CATION-TESTS — Tests for aqueous cations (sodium hydroxide precipitate colours; ammonium ion via ammonia gas) (CONCEPT)
-   spec 4CH1-2.47 [CORE]: describe tests for these cations:
- derivation: RELATED_RESIDUAL — Both notes open by defining their test as THE way to identify metal cations (by flame colour vs by precipitate colour) — a parallel-method association inside the same S2-h family, not a dependency (the 2.47 note never references the flame test and vice versa).
- `NOTE` Flame tests - IGCSE Chemistry Revision Notes.md — "The flame test is used to identify the positive metal ion (cations) by the colour of the flame they produce"
- `NOTE` Tests for cations - IGCSE Chemistry Revision Notes.md — "Metal cations in aqueous solution can be identified by the colour of the precipitate formed when sodium hyd..."

```diff
@@ -10611,7 +10611,9 @@ edges:
       precedent).
     upstream: T-C10 HUMAN_VALIDATED 4CH1-2.45-2.47 (2026-09-11)
   confidence: medium
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-24'
   ambiguity_note: 'Both notes lead with the same identification claim (flame test: "used to identify the
     positive metal ion (cations)"; NaOH test: "Metal cations ... can be identified by the colour of the
     precipitate") — the association is genuinely residual: neither technique presupposes the other, and
```

### 6. `4CH1-CON-WATER-PURITY-TEST REQUIRES_PREREQUISITE 4CH1-CON-PURE-SUBSTANCE` [high]

- node 4CH1-CON-WATER-PURITY-TEST — Physical test for water purity (boiling point exactly 100 C) (CONCEPT)
-   spec 4CH1-2.50 [CORE]: describe a physical test to show whether a sample of water is pure
- node 4CH1-CON-PURE-SUBSTANCE — Pure substance (chemical sense) and fixed melting/boiling points (CONCEPT)
-   spec 4CH1-1.9 [CORE]: understand that a pure substance has a fixed melting and boiling point, but that a mixture ma...
- derivation: USED_WITHOUT_RETEACHING — SANCTIONED BOUNDARY EDGE (the session-61 ruling, target 3 — the batch-1 CON-PURE-SUBSTANCE owner): the 2.50 physical purity test works BECAUSE pure substances have fixed boiling points — the note teaches the impurity effect inline, which IS the batch-1 owner's exact surface ("Pure substance (chemical sense) and fixed melting/boiling points"; aliases "pure", "purity"). The dependency is load-bearing, not naming: without the fixed-boiling-point principle the "exactly 100 C" check has no meaning.
- `NOTE` Chemical test for water - IGCSE Chemistry Revision Notes.md — "Any impurities present will usually tend to raise the boiling point and depress the melting point of pure s..."
- `NOTE` Chemical test for water - IGCSE Chemistry Revision Notes.md — "Using a thermometer, you can check if the boiling point is exactly 100 oC"

```diff
@@ -9785,7 +9785,9 @@ edges:
       has no meaning.'
     upstream: T-C10 HUMAN_VALIDATED 4CH1-2.50 (2026-09-11); the batch-1 record (CON-PURE-SUBSTANCE)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-24'
   version: 1
   created_at: '2026-09-24'
 - source: 4CH1-PR-01
```

### 7. `4CH1-MIS-GLOWING-SPLINT-HYDROGEN REMEDIATED_BY 4CH1-CON-GAS-TESTS` [high]

- node 4CH1-MIS-GLOWING-SPLINT-HYDROGEN — Testing for hydrogen with a glowing splint or an unflamed splint, or naming only the squeaky pop (instead of a burning splint at the tube mouth) (MISCONCEPTION)
- node 4CH1-CON-GAS-TESTS — Chemical tests for gases (hydrogen, oxygen, carbon dioxide, ammonia, chlorine) (CONCEPT)
-   spec 4CH1-2.44 [CORE]: describe tests for these gases:
- derivation: ASSESSMENT_DOCUMENTED — The remediation target = the WAP target (the B1-E-25 pattern): the gas-test family owns BOTH the correct hydrogen technique the MS demands AND the note's own examiner-tip ligHted/glOwing mnemonic that names the confusion the Reject guards.
- `NOTE` Gas tests - IGCSE Chemistry Revision Notes.md — "Try to remember that a ligHted splint has an H for Hydrogen, while a glOwing splint has an O for Oxygen."
- `NOTE` Gas tests - IGCSE Chemistry Revision Notes.md — "The test for hydrogen consists of holding a burning splint at the open end of a test tube of gas"

```diff
@@ -11631,7 +11631,9 @@ edges:
       mnemonic that names the confusion the Reject guards.'
     upstream: T-C10 HUMAN_VALIDATED 4CH1-2.44 @ Gas tests (2026-09-11); pinned CHEMICAL_TESTS_MS_P2 Q4a
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-24'
   version: 1
   created_at: '2026-09-24'
 - source: 4CH1-MIS-GRAPHITE-LAYER-BONDS
```

### 8. `4CH1-MIS-GLOWING-SPLINT-HYDROGEN WRONG_ANSWER_PATTERN 4CH1-CON-GAS-TESTS` [high]

- node 4CH1-MIS-GLOWING-SPLINT-HYDROGEN — Testing for hydrogen with a glowing splint or an unflamed splint, or naming only the squeaky pop (instead of a burning splint at the tube mouth) (MISCONCEPTION)
- node 4CH1-CON-GAS-TESTS — Chemical tests for gases (hydrogen, oxygen, carbon dioxide, ammonia, chlorine) (CONCEPT)
-   spec 4CH1-2.44 [CORE]: describe tests for these gases:
- derivation: ASSESSMENT_DOCUMENTED — The WAP target is the concept whose test the question probes: the 2.44 gas-test family (the hydrogen row) — the MS caps the glowing-splint/unflamed-splint/pop-only answer class on exactly that surface (the B5/B6/B7 WAP-target pattern).
- `MARK_SCHEME` CHEMICAL_TESTS_MS_P2.txt — "Reject reference to glowing splint"
- `MARK_SCHEME` CHEMICAL_TESTS_MS_P2.txt — "Reference to splint/match with no indication of flame is not enough"

```diff
@@ -11065,7 +11065,9 @@ edges:
       on exactly that surface (the B5/B6/B7 WAP-target pattern).'
     upstream: pinned CHEMICAL_TESTS_MS_P2 (sha1_12 68356f71b4bc) Q4a; spec 4CH1-2.44 official wording
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-24'
   version: 1
   created_at: '2026-09-24'
 - source: 4CH1-MIS-GRAPHITE-LAYER-BONDS
```

### 9. `4CH1-MIS-HALIDE-TEST-HCL REMEDIATED_BY 4CH1-CON-ANION-TESTS` [high]

- node 4CH1-MIS-HALIDE-TEST-HCL — Acidifying the halide test with hydrochloric acid (instead of nitric acid) (MISCONCEPTION)
- node 4CH1-CON-ANION-TESTS — Tests for aqueous anions (halides, sulfate, carbonate) (CONCEPT)
-   spec 4CH1-2.48 [CORE]: describe tests for these anions:
- derivation: ASSESSMENT_DOCUMENTED — The remediation target = the WAP target (the B1-E-25 pattern): the anion-test family owns BOTH the nitric-acid rule the MS demands AND the silver-halide result table the rejected acidifier would contaminate.
- `NOTE` Tests for Anions  Edexcel IGCSE Chemistry Revision Notes 2017.md — "Acidify the sample with nitric acid"
- `NOTE` Tests for Anions  Edexcel IGCSE Chemistry Revision Notes 2017.md — "The colour of the silver halide precipitate depends on the halide ion:"

```diff
@@ -11683,7 +11683,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-2.48 @ Tests for Anions (2026-09-11); pinned CHEMICAL_TESTS_MS_P2
       Q4b(i)
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-24'
   version: 1
   created_at: '2026-09-24'
 - source: 4CH1-MIS-HALOGEN-HALIDE
```

### 10. `4CH1-MIS-HALIDE-TEST-HCL WRONG_ANSWER_PATTERN 4CH1-CON-ANION-TESTS` [high]

- node 4CH1-MIS-HALIDE-TEST-HCL — Acidifying the halide test with hydrochloric acid (instead of nitric acid) (MISCONCEPTION)
- node 4CH1-CON-ANION-TESTS — Tests for aqueous anions (halides, sulfate, carbonate) (CONCEPT)
-   spec 4CH1-2.48 [CORE]: describe tests for these anions:
- derivation: ASSESSMENT_DOCUMENTED — The WAP target is the concept whose test the question probes: the 2.48 anion-test family (the halide row) — the MS caps the hydrochloric-acid answer class on exactly that surface (the B5/B6/B7 WAP-target pattern).
- `MARK_SCHEME` CHEMICAL_TESTS_MS_P2.txt — "Reject hydrochloric acid / HCl"
- `MARK_SCHEME` CHEMICAL_TESTS_MS_P2.txt — "(dilute) nitric acid / HNO3"

```diff
@@ -11112,7 +11112,9 @@ edges:
       (the B5/B6/B7 WAP-target pattern).'
     upstream: pinned CHEMICAL_TESTS_MS_P2 (sha1_12 68356f71b4bc) Q4b(i); spec 4CH1-2.48 official wording
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-24'
   version: 1
   created_at: '2026-09-24'
 - source: 4CH1-MIS-HALOGEN-HALIDE
```

## File-level meta hunks (once, for the whole batch)

```diff
@@ -206,8 +206,10 @@ meta:
     remediated_by_edges: 23
     requires_prerequisite_edges: 159
     wrong_answer_pattern_edges: 21
-    promoted_edges: 323
-    human_validated_edges: 323
+    promoted_edges: 333
+    human_validated_edges: 333
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
| `4CH1-CON-FLAME-TEST` | Flame tests for metal cations (technique and flame colours) | CONCEPT | 4CH1-2.45 (CORE); 4CH1-2.46 (CORE) | high |
| `4CH1-CON-FRACTIONAL-DISTILLATION` | Fractional distillation | CONCEPT | 4CH1-1.10 (CORE) | high |
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
| `4CH1-MIS-PRECIPITATE-IN-FILTRATE` | Recovering the insoluble salt from the filtrate instead of the residue in a precipitation preparation | MISCONCEPTION |  | high |
| `4CH1-MIS-RAM-MASS-NUMBER` | Calling the Periodic Table relative atomic mass the mass number | MISCONCEPTION |  | high |

