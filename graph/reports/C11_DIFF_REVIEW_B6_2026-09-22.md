# C11 Diff Review Bundle — pending §18 edge promotions (generated 2026-09-22)

- baseline commit: `766fdd7`
- state fingerprint: `2e79b836c7d2` (promo_count=171)
- actionable: 16 edges (clean 16 / pending-flagged 0); not-actionable: 5; nodes awaiting a pathway: 142
- preview fidelity: simulator re-emits graph/igcse-chemistry/concept_edges under the generator's own serialization contract with a byte-identity guard — what you read is what G13 will write.

## Batch approval

```bash
cd work/syllabai-resources && python3 scripts/c11_diff_review.py approve \
  '4CH1-CON-ALLOY-HARDNESS REQUIRES_PREREQUISITE 4CH1-CON-ALLOYS' \
  '4CH1-CON-CO2-FROM-CARBONATES REQUIRES_PREREQUISITE 4CH1-CON-REACT-ORDER' \
  '4CH1-CON-EXTRACTION-EVALUATION REQUIRES_PREREQUISITE 4CH1-CON-EXTRACTION-METHOD' \
  '4CH1-CON-EXTRACTION-METHOD REQUIRES_PREREQUISITE 4CH1-CON-ELECTROLYSIS' \
  '4CH1-CON-EXTRACTION-METHOD REQUIRES_PREREQUISITE 4CH1-CON-OX-RED-AGENTS' \
  '4CH1-CON-EXTRACTION-METHOD REQUIRES_PREREQUISITE 4CH1-CON-REACT-ORDER' \
  '4CH1-CON-METAL-DISPLACEMENT REQUIRES_PREREQUISITE 4CH1-CON-REACT-ORDER' \
  '4CH1-CON-METAL-USES REQUIRES_PREREQUISITE 4CH1-CON-METAL-PROPERTIES' \
  '4CH1-CON-O2-PERCENT-DETERMINATION REQUIRES_PREREQUISITE 4CH1-CON-RUSTING' \
  '4CH1-CON-REACT-ORDER REQUIRES_PREREQUISITE 4CH1-CON-REACT-ARRANGE' \
  '4CH1-CON-RUST-PREVENTION REQUIRES_PREREQUISITE 4CH1-CON-OX-RED-AGENTS' \
  '4CH1-CON-RUST-PREVENTION REQUIRES_PREREQUISITE 4CH1-CON-REACT-ORDER' \
  '4CH1-CON-RUST-PREVENTION REQUIRES_PREREQUISITE 4CH1-CON-RUSTING' \
  '4CH1-MIS-ION-OXIDE-REASONING REMEDIATED_BY 4CH1-CON-METAL-DISPLACEMENT' \
  '4CH1-MIS-ION-OXIDE-REASONING WRONG_ANSWER_PATTERN 4CH1-CON-METAL-DISPLACEMENT' \
  '4CH1-PR-06 REQUIRES_PREREQUISITE 4CH1-CON-REACT-ARRANGE' \
  --by <operator> --date 2026-09-22 --review-ref graph/reports/C11_DIFF_REVIEW_B6_2026-09-22.md
```

Pending-flagged (PENDING operator_decision) edges are excluded from the command above; approving them additionally requires `--include-pending` — that flag records the explicit decision this bundle presents.

## Index

| # | identity | confidence | flag |
|---|----------|------------|------|
| 1 | `4CH1-CON-ALLOY-HARDNESS REQUIRES_PREREQUISITE 4CH1-CON-ALLOYS` | high |  |
| 2 | `4CH1-CON-CO2-FROM-CARBONATES REQUIRES_PREREQUISITE 4CH1-CON-REACT-ORDER` | high |  |
| 3 | `4CH1-CON-EXTRACTION-EVALUATION REQUIRES_PREREQUISITE 4CH1-CON-EXTRACTION-METHOD` | high |  |
| 4 | `4CH1-CON-EXTRACTION-METHOD REQUIRES_PREREQUISITE 4CH1-CON-ELECTROLYSIS` | high |  |
| 5 | `4CH1-CON-EXTRACTION-METHOD REQUIRES_PREREQUISITE 4CH1-CON-OX-RED-AGENTS` | high |  |
| 6 | `4CH1-CON-EXTRACTION-METHOD REQUIRES_PREREQUISITE 4CH1-CON-REACT-ORDER` | high |  |
| 7 | `4CH1-CON-METAL-DISPLACEMENT REQUIRES_PREREQUISITE 4CH1-CON-REACT-ORDER` | high |  |
| 8 | `4CH1-CON-METAL-USES REQUIRES_PREREQUISITE 4CH1-CON-METAL-PROPERTIES` | high |  |
| 9 | `4CH1-CON-O2-PERCENT-DETERMINATION REQUIRES_PREREQUISITE 4CH1-CON-RUSTING` | high |  |
| 10 | `4CH1-CON-REACT-ORDER REQUIRES_PREREQUISITE 4CH1-CON-REACT-ARRANGE` | high |  |
| 11 | `4CH1-CON-RUST-PREVENTION REQUIRES_PREREQUISITE 4CH1-CON-OX-RED-AGENTS` | high |  |
| 12 | `4CH1-CON-RUST-PREVENTION REQUIRES_PREREQUISITE 4CH1-CON-REACT-ORDER` | high |  |
| 13 | `4CH1-CON-RUST-PREVENTION REQUIRES_PREREQUISITE 4CH1-CON-RUSTING` | high |  |
| 14 | `4CH1-MIS-ION-OXIDE-REASONING REMEDIATED_BY 4CH1-CON-METAL-DISPLACEMENT` | high |  |
| 15 | `4CH1-MIS-ION-OXIDE-REASONING WRONG_ANSWER_PATTERN 4CH1-CON-METAL-DISPLACEMENT` | high |  |
| 16 | `4CH1-PR-06 REQUIRES_PREREQUISITE 4CH1-CON-REACT-ARRANGE` | high |  |

## Pending items — the exact diff each approval applies

### 1. `4CH1-CON-ALLOY-HARDNESS REQUIRES_PREREQUISITE 4CH1-CON-ALLOYS` [high]

- node 4CH1-CON-ALLOY-HARDNESS — Why alloys are harder than pure metals (distorted layers resist sliding) (CONCEPT)
-   spec 4CH1-2.27C [CORE]: explain why alloys are harder than pure metals
- node 4CH1-CON-ALLOYS — Alloys as mixtures of a metal with other elements (CONCEPT)
-   spec 4CH1-2.26C [CORE]: know that an alloy is a mixture of a metal and one or more elements, usually other metals or ...
- derivation: DEFINITIONAL_DEPENDENCY — The hardness explanation is DEFINED over the mixture structure ("Alloys are harder than pure metals because: Alloys contain atoms of DIFFERENT sizes") — the different-sized atoms are the alloy-defining content the 2.26C node owns; the spec's own 2.26C-then-2.27C order (definition, then the mechanism it explains).
- `NOTE` Alloys - IGCSE Chemistry Revision Notes.md — "Alloys are harder than pure metals because:"
- `NOTE` Alloys - IGCSE Chemistry Revision Notes.md — "Alloys contain atoms of different sizes"

```diff
@@ -5094,7 +5094,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-2.26C/2.27C @ Alloys (2026-09-11)
     generated_date: '2026-09-22'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-22'
   version: 1
   created_at: '2026-09-22'
 - source: 4CH1-CON-ANODE-CATHODE
```

### 2. `4CH1-CON-CO2-FROM-CARBONATES REQUIRES_PREREQUISITE 4CH1-CON-REACT-ORDER` [high]

- node 4CH1-CON-CO2-FROM-CARBONATES — Carbon dioxide from thermal decomposition of metal carbonates (CONCEPT)
-   spec 4CH1-2.12 [CORE]: describe the formation of carbon dioxide from the thermal decomposition of metal carbonates, ...
- node 4CH1-CON-REACT-ORDER — The order of reactivity of the named metals (K to Au) (CONCEPT)
-   spec 4CH1-2.17 [CORE]: know the order of reactivity of these metals: potassium, sodium, lithium, calcium, magnesium,...
- derivation: USED_WITHOUT_RETEACHING — CROSS-SECTION boundary edge (sanctioned target, session-57 ruling — closes the batch-5 ruling's recorded deferral): the decomposition family presupposes reactivity-series placement ("Carbonates of metals from the LOWER HALF of the reactivity series tend to decompose" — the batch-5 note states the dependency and the batch-5 record held the edge for want of an owner, B5-H-10); batch 6 mints the owner and this edge closes the deferral. The anchor resolves via the source's own SP (the thermal-decomposition note T-C10-maps to 4CH1-2.12).
- `NOTE` Thermal decomposition - IGCSE Chemistry Revision Notes.md — "Carbonates of metals from the lower half of the reactivity series tend to decompose on heating to produce t..."

```diff
@@ -5405,7 +5405,9 @@ edges:
       future_boundary_note deferred exactly this edge
     generated_date: '2026-09-22'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-22'
   version: 1
   created_at: '2026-09-22'
 - source: 4CH1-CON-COMBUSTION-O2
```

### 3. `4CH1-CON-EXTRACTION-EVALUATION REQUIRES_PREREQUISITE 4CH1-CON-EXTRACTION-METHOD` [high]

- node 4CH1-CON-EXTRACTION-EVALUATION — Commenting on a metal extraction process from given information (CONCEPT)
-   spec 4CH1-2.24C [CORE]: be able to comment on a metal extraction process, given appropriate information detailed know...
- node 4CH1-CON-EXTRACTION-METHOD — Extraction method related to reactivity-series position (electrolysis above carbon; carbon reduction below) (CONCEPT)
-   spec 4CH1-2.23C [CORE]: explain how the method of extraction of a metal is related to its position in the reactivity ...
- derivation: USED_WITHOUT_RETEACHING — The comment-on-a-process skill operates ON the taught method-position framework (the note's own Examiner Tip ties the evaluation question to the electrolysis-vs-reduction explanation); the worked information surfaces (blast-furnace zones, cryolite cell, electricity expense) are all descriptions OF the method node's content — the evaluation presupposes it.
- `NOTE` Extraction of metals from ores - IGCSE Chemistry.md — "Make sure you can explain why aluminium is extracted by electrolysis while iron is extracted by reduction a..."

```diff
@@ -6196,7 +6196,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-2.24C/2.23C @ Extraction of metals from ores (2026-09-11)
     generated_date: '2026-09-22'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-22'
   version: 1
   created_at: '2026-09-22'
 - source: 4CH1-CON-EXTRACTION-METHOD
```

### 4. `4CH1-CON-EXTRACTION-METHOD REQUIRES_PREREQUISITE 4CH1-CON-ELECTROLYSIS` [high]

- node 4CH1-CON-EXTRACTION-METHOD — Extraction method related to reactivity-series position (electrolysis above carbon; carbon reduction below) (CONCEPT)
-   spec 4CH1-2.23C [CORE]: explain how the method of extraction of a metal is related to its position in the reactivity ...
- node 4CH1-CON-ELECTROLYSIS — Electrolysis (decomposition by direct current: molten binary compounds and their element products, using inert electrodes) (CONCEPT)
-   spec 4CH1-1.58C [CORE]: describe experiments to investigate electrolysis, using inert electrodes, of molten compounds...
- derivation: USED_WITHOUT_RETEACHING — CROSS-SECTION boundary edge (sanctioned target, session-57 ruling — owner 4CH1-CON-ELECTROLYSIS, batch 3, 1.58C): the electrolysis route APPLIES the electrolysis framework AS GIVEN ("extracted by electrolysis", the cell, electrodes, ion discharge at electrodes) — the note never re-defines electrolysis or the electrolyte. The anode/cathode terms carry inline parenthetical glosses ("cathode (negative electrode)") and the electrode half-equations are OD-2 enrichment beyond the method-position demand — both dispositions in the ruling, no second boundary edge (one edge per dependency surface).
- `NOTE` Extraction of metals from ores - IGCSE Chemistry.md — "Instead, aluminium is extracted by electrolysis"
- `NOTE` Extraction of metals from ores - IGCSE Chemistry.md — "Higher placed metals (above carbon) have to be extracted using electrolysis as they are too reactive and ca..."

```diff
@@ -6227,7 +6227,9 @@ edges:
       owned by the batch-3 record (4CH1-1.58C); session-57 boundary ruling sanctioned target
     generated_date: '2026-09-22'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-22'
   version: 1
   created_at: '2026-09-22'
 - source: 4CH1-CON-EXTRACTION-METHOD
```

### 5. `4CH1-CON-EXTRACTION-METHOD REQUIRES_PREREQUISITE 4CH1-CON-OX-RED-AGENTS` [high]

- node 4CH1-CON-EXTRACTION-METHOD — Extraction method related to reactivity-series position (electrolysis above carbon; carbon reduction below) (CONCEPT)
-   spec 4CH1-2.23C [CORE]: explain how the method of extraction of a metal is related to its position in the reactivity ...
- node 4CH1-CON-OX-RED-AGENTS — Oxidation, reduction, oxidising and reducing agents (oxygen and electron frameworks) (CONCEPT)
-   spec 4CH1-2.20 [CORE]: understand the terms:
- derivation: USED_WITHOUT_RETEACHING — The carbon-reduction route OPERATES on the reduction concept AS GIVEN ("heating with carbon which reduces them"; zone 3 "Carbon monoxide reduces the iron(III) oxide") — the extraction note never re-teaches what reduction is (the definitions live in the target node's note; the Where-does note's "reduction process since oxygen is being removed" bridges the same vocabulary at 2.22C context).
- `NOTE` Extraction of metals from ores - IGCSE Chemistry.md — "Lower placed metals can be extracted by heating with carbon which reduces them"
- `NOTE` Extraction of metals from ores - IGCSE Chemistry.md — "Carbon monoxide reduces the iron(III) oxide in the iron ore to form iron"

```diff
@@ -6255,7 +6255,9 @@ edges:
       owned by this record (4CH1-2.20)
     generated_date: '2026-09-22'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-22'
   version: 1
   created_at: '2026-09-22'
 - source: 4CH1-CON-EXTRACTION-METHOD
```

### 6. `4CH1-CON-EXTRACTION-METHOD REQUIRES_PREREQUISITE 4CH1-CON-REACT-ORDER` [high]

- node 4CH1-CON-EXTRACTION-METHOD — Extraction method related to reactivity-series position (electrolysis above carbon; carbon reduction below) (CONCEPT)
-   spec 4CH1-2.23C [CORE]: explain how the method of extraction of a metal is related to its position in the reactivity ...
- node 4CH1-CON-REACT-ORDER — The order of reactivity of the named metals (K to Au) (CONCEPT)
-   spec 4CH1-2.17 [CORE]: know the order of reactivity of these metals: potassium, sodium, lithium, calcium, magnesium,...
- derivation: DEFINITIONAL_DEPENDENCY — The spec's own 2.23C demand verbatim ("how the method of extraction of a metal is related to its position in the reactivity series") and the note's own thesis line ("The position of the metal on the reactivity series determines the method of extraction") — the method-position relation is unintelligible without the order; the strongest in-batch dependency.
- `NOTE` Extraction of metals from ores - IGCSE Chemistry.md — "The position of the metal on the reactivity series determines the method of extraction"

```diff
@@ -6279,7 +6279,9 @@ edges:
       owned by this record (4CH1-2.17)
     generated_date: '2026-09-22'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-22'
   version: 1
   created_at: '2026-09-22'
 - source: 4CH1-CON-FILTRATION
```

### 7. `4CH1-CON-METAL-DISPLACEMENT REQUIRES_PREREQUISITE 4CH1-CON-REACT-ORDER` [high]

- node 4CH1-CON-METAL-DISPLACEMENT — Metal displacement reactions as reactivity-series evidence (metal + metal oxide; metal + salt solution) (CONCEPT)
-   spec 4CH1-2.16 [CORE]: understand how metals can be arranged in a reactivity series based on their displacement reac...
- node 4CH1-CON-REACT-ORDER — The order of reactivity of the named metals (K to Au) (CONCEPT)
-   spec 4CH1-2.17 [CORE]: know the order of reactivity of these metals: potassium, sodium, lithium, calcium, magnesium,...
- derivation: DEFINITIONAL_DEPENDENCY — Displacement is DEFINED over the reactivity order ("The reactivity of metals decreases going down the reactivity series. This means that a more reactive metal will displace a less reactive metal from its compounds") — the definitional operands are exactly the order the 2.17 node owns (the batch-5 CON-G7-DISPLACEMENT -> CON-G7-REACTIVITY-ECONFIG definitional shape). The reverse direction (the comparison line "can be compared using displacement reactions") is 2.16's own arrangement demand living inside this node — the B6-H-06 hold blocks the reverse edge.
- `NOTE` Metal displacement - IGCSE Chemistry Revision Notes.md — "The reactivity of metals decreases going down the reactivity series."
- `NOTE` Metal displacement - IGCSE Chemistry Revision Notes.md — "This means that a more reactive metal will displace a less reactive metal from its compounds"

```diff
@@ -7036,7 +7036,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-2.16/2.17 @ Metal displacement + The reactivity series (2026-09-11)
     generated_date: '2026-09-22'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-22'
   version: 1
   created_at: '2026-09-22'
 - source: 4CH1-CON-METAL-NONMETAL
```

### 8. `4CH1-CON-METAL-USES REQUIRES_PREREQUISITE 4CH1-CON-METAL-PROPERTIES` [high]

- node 4CH1-CON-METAL-USES — Uses of aluminium, copper, iron and steel explained by their properties (CONCEPT)
-   spec 4CH1-2.25C [CORE]: explain the uses of aluminium, copper, iron and steel in terms of their properties the types ...
- node 4CH1-CON-METAL-PROPERTIES — Typical physical properties of metals (electrical conductivity and malleability) and their explanations (CONCEPT)
-   spec 4CH1-1.54C [CORE]: explain typical physical properties of metals, including electrical conductivity and malleabi...
- derivation: USED_WITHOUT_RETEACHING — CROSS-SECTION boundary edge (sanctioned target, session-57 ruling — owner 4CH1-CON-METAL-PROPERTIES, batch 3, 1.54C): the 2.25C demand is verbatim "in terms of their properties" and the uses tables apply the property vocabulary (conductivity, malleability, ductility) AS GIVEN — the uses note never re-teaches what conductivity or malleability are (the 1.54C owner's own surface carries them).
- `NOTE` Metals and their uses - IGCSE Chemistry Revision Notes.md — "Very good conductor of electricity and ductile"
- `NOTE` Metals and their uses - IGCSE Chemistry Revision Notes.md — "Unreactive (does not react with water), non-toxic and malleable"

```diff
@@ -7088,7 +7088,9 @@ edges:
       by the batch-3 record (4CH1-1.54C); session-57 boundary ruling sanctioned target
     generated_date: '2026-09-22'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-22'
   version: 1
   created_at: '2026-09-22'
 - source: 4CH1-CON-METALLIC-BOND
```

### 9. `4CH1-CON-O2-PERCENT-DETERMINATION REQUIRES_PREREQUISITE 4CH1-CON-RUSTING` [high]

- node 4CH1-CON-O2-PERCENT-DETERMINATION — Determining the percentage of oxygen in air (metal and non-metal routes) (CONCEPT)
-   spec 4CH1-2.10 [CORE]: understand how to determine the percentage by volume of oxygen in air using experiments invol...
- node 4CH1-CON-RUSTING — Rusting of iron (both oxygen and water required; the control-tube investigation) (CONCEPT)
-   spec 4CH1-2.18 [CORE]: know the conditions under which iron rusts
- derivation: USED_WITHOUT_RETEACHING — CROSS-SECTION boundary edge (sanctioned target, session-57 ruling — closes the batch-5 ruling's recorded deferral): the iron-wool route presupposes iron rusting ("using the oxidation of iron" — the slow iron/water/air reaction over 3-4 days IS the rusting phenomenon whose conditions the 2.18 node owns; the experiment design applies them: iron in contact with BOTH air and water); the batch-5 record held the edge for want of an owner (its future_boundary_note deferred it verbatim to "the batch that mints it"). The anchor resolves via the source's own SP (the oxygen-percentage note T-C10-maps to 4CH1-2.10).
- `NOTE` Oxygen percentage in air - IGCSE Chemistry Revision Notes.md — "To determine the percentage of oxygen in air using the oxidation of iron"
- `NOTE` Oxygen percentage in air - IGCSE Chemistry Revision Notes.md — "After 3-4 days note the new position of the water level"

```diff
@@ -7462,7 +7462,9 @@ edges:
       future_boundary_note deferred exactly this edge
     generated_date: '2026-09-22'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-22'
   version: 1
   created_at: '2026-09-22'
 - source: 4CH1-CON-PERCENT-YIELD
```

### 10. `4CH1-CON-REACT-ORDER REQUIRES_PREREQUISITE 4CH1-CON-REACT-ARRANGE` [high]

- node 4CH1-CON-REACT-ORDER — The order of reactivity of the named metals (K to Au) (CONCEPT)
-   spec 4CH1-2.17 [CORE]: know the order of reactivity of these metals: potassium, sodium, lithium, calcium, magnesium,...
- node 4CH1-CON-REACT-ARRANGE — Arranging metals into a reactivity series from water and dilute-acid reactions (CONCEPT)
-   spec 4CH1-2.15 [CORE]: understand how metals can be arranged in a reactivity series based on their reactions with:
- derivation: DEFINITIONAL_DEPENDENCY — The order is the PRODUCT of the arrangement methods: "Based on these reactions a reactivity series of metals can be produced" — the 2.17 order is the graded pattern the 2.15 water/acid comparisons produce (the spec's own 2.15-then-2.17 order: arrangement method, then the resulting order).
- `NOTE` Metals Reacting with Water & Acids  Edexcel IGCSE Chemistry Revision Notes 2017.md — "Based on these reactions a reactivity series of metals can be produced"
- `NOTE` Metals Reacting with Water & Acids  Edexcel IGCSE Chemistry Revision Notes 2017.md — "The series can be used to place a group of metals in order of reactivity based on the observations of their..."

```diff
@@ -7669,7 +7669,9 @@ edges:
       series (2026-09-11)
     generated_date: '2026-09-22'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-22'
   version: 1
   created_at: '2026-09-22'
 - source: 4CH1-CON-REACTING-MASS
```

### 11. `4CH1-CON-RUST-PREVENTION REQUIRES_PREREQUISITE 4CH1-CON-OX-RED-AGENTS` [high]

- node 4CH1-CON-RUST-PREVENTION — Preventing rusting (barrier methods, sacrificial protection, galvanising) (CONCEPT)
-   spec 4CH1-2.19 [CORE]: understand how the rusting of iron may be prevented by:
- node 4CH1-CON-OX-RED-AGENTS — Oxidation, reduction, oxidising and reducing agents (oxygen and electron frameworks) (CONCEPT)
-   spec 4CH1-2.20 [CORE]: understand the terms:
- derivation: USED_WITHOUT_RETEACHING — The sacrificial mechanism is STATED in terms of oxidation ("will oxidise and therefore corrode first", "is oxidised more easily") — explaining WHY sacrifice protects applies the oxidation concept AS GIVEN (the rusting note never re-teaches what oxidation is; the target node's own note carries the definitions). Both frameworks appear (oxygen-framework "oxidise"; electron-framework "lose its electrons more easily") — the target node owns both (the B6-ID-01 scope).
- `NOTE` Rusting of iron - IGCSE Chemistry Revision Notes.md — "The more reactive metal will oxidise and therefore corrode first, protecting the less reactive metal from c..."
- `NOTE` Rusting of iron - IGCSE Chemistry Revision Notes.md — "Zinc is more reactive than iron therefore will lose its electrons more easily than iron and is oxidised mor..."

```diff
@@ -7933,7 +7933,9 @@ edges:
       record (4CH1-2.20)
     generated_date: '2026-09-22'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-22'
   version: 1
   created_at: '2026-09-22'
 - source: 4CH1-CON-RUST-PREVENTION
```

### 12. `4CH1-CON-RUST-PREVENTION REQUIRES_PREREQUISITE 4CH1-CON-REACT-ORDER` [high]

- node 4CH1-CON-RUST-PREVENTION — Preventing rusting (barrier methods, sacrificial protection, galvanising) (CONCEPT)
-   spec 4CH1-2.19 [CORE]: understand how the rusting of iron may be prevented by:
- node 4CH1-CON-REACT-ORDER — The order of reactivity of the named metals (K to Au) (CONCEPT)
-   spec 4CH1-2.17 [CORE]: know the order of reactivity of these metals: potassium, sodium, lithium, calcium, magnesium,...
- derivation: USED_WITHOUT_RETEACHING — Sacrificial protection operates ON the taught reactivity order AS GIVEN ("Iron can be prevented from rusting using the reactivity series. A more reactive metal can be attached to a less reactive metal") — selecting the sacrificial metal REQUIRES the order; the note never re-derives it.
- `NOTE` Rusting of iron - IGCSE Chemistry Revision Notes.md — "Iron can be prevented from rusting using the reactivity series"
- `NOTE` Rusting of iron - IGCSE Chemistry Revision Notes.md — "A more reactive metal can be attached to a less reactive metal"

```diff
@@ -7961,7 +7961,9 @@ edges:
       record (4CH1-2.17)
     generated_date: '2026-09-22'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-22'
   version: 1
   created_at: '2026-09-22'
 - source: 4CH1-CON-RUST-PREVENTION
```

### 13. `4CH1-CON-RUST-PREVENTION REQUIRES_PREREQUISITE 4CH1-CON-RUSTING` [high]

- node 4CH1-CON-RUST-PREVENTION — Preventing rusting (barrier methods, sacrificial protection, galvanising) (CONCEPT)
-   spec 4CH1-2.19 [CORE]: understand how the rusting of iron may be prevented by:
- node 4CH1-CON-RUSTING — Rusting of iron (both oxygen and water required; the control-tube investigation) (CONCEPT)
-   spec 4CH1-2.18 [CORE]: know the conditions under which iron rusts
- derivation: DEFINITIONAL_DEPENDENCY — Prevention is DEFINED over the rusting conditions: the barrier method is "barriers that prevent the iron from coming into contact with water and oxygen" — the exact 2.18 condition pair; every prevention family (barrier/sacrificial/galvanising) presupposes knowing WHAT must be excluded or substituted (the spec's own 2.18-then-2.19 order).
- `NOTE` Rusting of iron - IGCSE Chemistry Revision Notes.md — "Rust can be prevented by coating iron with barriers that prevent the iron from coming into contact with wat..."
- `NOTE` Rusting of iron - IGCSE Chemistry Revision Notes.md — "If the coating is damaged or scratched, the iron is still protected from rusting by sacrificial protection"

```diff
@@ -7990,7 +7990,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-2.18/2.19 @ Rusting of iron (2026-09-11)
     generated_date: '2026-09-22'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-22'
   version: 1
   created_at: '2026-09-22'
 - source: 4CH1-CON-SATURATED-SOLUTION
```

### 14. `4CH1-MIS-ION-OXIDE-REASONING REMEDIATED_BY 4CH1-CON-METAL-DISPLACEMENT` [high]

- node 4CH1-MIS-ION-OXIDE-REASONING — Explaining a metal-oxide displacement outcome by references to ions and oxides instead of the reactivity comparison (MISCONCEPTION)
- node 4CH1-CON-METAL-DISPLACEMENT — Metal displacement reactions as reactivity-series evidence (metal + metal oxide; metal + salt solution) (CONCEPT)
-   spec 4CH1-2.16 [CORE]: understand how metals can be arranged in a reactivity series based on their displacement reac...
- derivation: ASSESSMENT_DOCUMENTED — Remediation target = WAP target (the B1-E-25 pattern): the corrective content IS the displacement rule ("a more reactive metal will displace a less reactive metal from its compounds") and the MS's own expected answer ("aluminium replaces iron (from a compound)") is the same statement in assessment form.
- `NOTE` Metal displacement - IGCSE Chemistry Revision Notes.md — "This means that a more reactive metal will displace a less reactive metal from its compounds"
- `MARK_SCHEME` REACTIVITY_MS_P2.txt — "aluminium replaces iron (from a compound)"

```diff
@@ -9945,7 +9945,9 @@ edges:
     upstream: pinned REACTIVITY_MS_P2 (sha1_12 8e883dd7d68d) Q2a/b + Metal displacement note (2026-09-11)
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

### 15. `4CH1-MIS-ION-OXIDE-REASONING WRONG_ANSWER_PATTERN 4CH1-CON-METAL-DISPLACEMENT` [high]

- node 4CH1-MIS-ION-OXIDE-REASONING — Explaining a metal-oxide displacement outcome by references to ions and oxides instead of the reactivity comparison (MISCONCEPTION)
- node 4CH1-CON-METAL-DISPLACEMENT — Metal displacement reactions as reactivity-series evidence (metal + metal oxide; metal + salt solution) (CONCEPT)
-   spec 4CH1-2.16 [CORE]: understand how metals can be arranged in a reactivity series based on their displacement reac...
- derivation: ASSESSMENT_DOCUMENTED — The WAP target is the concept whose wrong explanations the MS caps — the aluminium/iron-oxide question is a metal-oxide displacement item (2.16a strand) and the Reject column caps the non-reactivity explanation class on exactly that surface (the B5 WAP-target pattern).
- `MARK_SCHEME` REACTIVITY_MS_P2.txt — "Reject references to ions and oxides"
- `MARK_SCHEME` REACTIVITY_MS_P2.txt — "(it/iron is) less reactive (than aluminium)"

```diff
@@ -9481,7 +9481,9 @@ edges:
     upstream: pinned REACTIVITY_MS_P2 (sha1_12 8e883dd7d68d) Q2a; spec 4CH1-2.16 official wording
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

### 16. `4CH1-PR-06 REQUIRES_PREREQUISITE 4CH1-CON-REACT-ARRANGE` [high]

- node 4CH1-CON-REACT-ARRANGE — Arranging metals into a reactivity series from water and dilute-acid reactions (CONCEPT)
-   spec 4CH1-2.15 [CORE]: understand how metals can be arranged in a reactivity series based on their reactions with:
- derivation: USED_WITHOUT_RETEACHING — Practical->conceptual (the pilot test #5 requirement, the PR-05->CON-O2-PERCENT-DETERMINATION shape): the 2.21 practical RUNS the acid-metal comparison its concept owns — the investigation's conclusion ("The metals can be ranked in reactivity order Mg > Zn > Fe") is the arrangement method in action. 2.21 attaches NO concept node (the 1.13/1.60C/2.14/3.8/3.15/3.16 precedent; 4CH1-PR-06 owns it).
- `NOTE` Metals reacting with acids - IGCSE Chemistry Revision Notes.md — "To investigate the reactions between dilute hydrochloric and sulfuric acids with the metals magnesium, iron..."
- `NOTE` Metals reacting with acids - IGCSE Chemistry Revision Notes.md — "The metals can be ranked in reactivity order Mg > Zn > Fe"

```diff
@@ -8522,7 +8522,9 @@ edges:
       record 4CH1-PR-06 (practicals.yaml, RULE_DERIVED)
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
@@ -175,8 +175,10 @@ meta:
     remediated_by_edges: 19
     requires_prerequisite_edges: 139
     wrong_answer_pattern_edges: 17
-    promoted_edges: 288
-    human_validated_edges: 288
+    promoted_edges: 304
+    human_validated_edges: 304
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
| `4CH1-CON-ALLOY-HARDNESS` | Why alloys are harder than pure metals (distorted layers resist sliding) | CONCEPT | 4CH1-2.27C (CORE) | high |
| `4CH1-CON-ALLOYS` | Alloys as mixtures of a metal with other elements | CONCEPT | 4CH1-2.26C (CORE) | high |
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
| `4CH1-CON-NOBLE-GAS-INERTNESS` | Why the noble gases (Group 0) do not readily react | CONCEPT | 4CH1-1.24 (CORE) | high |
| `4CH1-CON-O2-PERCENT-DETERMINATION` | Determining the percentage of oxygen in air (metal and non-metal routes) | CONCEPT | 4CH1-2.10 (CORE) | high |
| `4CH1-CON-ORES` | Ores and native (uncombined) metals as sources of metals | CONCEPT | 4CH1-2.22C (CORE) | high |
| `4CH1-CON-OX-RED-AGENTS` | Oxidation, reduction, oxidising and reducing agents (oxygen and electron frameworks) | CONCEPT | 4CH1-2.20 (CORE) | high |
| `4CH1-CON-PERCENT-YIELD` | Percentage yield | CONCEPT | 4CH1-1.30 (CORE) | high |
| `4CH1-CON-PERIODIC-TABLE` | Periodic Table arrangement (atomic-number order, groups and periods) | CONCEPT | 4CH1-1.18 (CORE) | high |
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
| `4CH1-MIS-ION-OXIDE-REASONING` | Explaining a metal-oxide displacement outcome by references to ions and oxides instead of the reactivity comparison | MISCONCEPTION |  | high |
| `4CH1-MIS-IONIC-BOND-ATOMS` | Describing ionic bonding as attraction between atoms or molecules (or as intermolecular forces) | MISCONCEPTION |  | high |
| `4CH1-MIS-IONIC-CONDUCTION-ELECTRONS` | Believing ionic compounds conduct electricity because electrons move and carry the charge | MISCONCEPTION |  | high |
| `4CH1-MIS-ISOTOPES-DIFFER-PROTONS` | Believing isotopes of an element differ in their number of protons | MISCONCEPTION |  | high |
| `4CH1-MIS-RAM-MASS-NUMBER` | Calling the Periodic Table relative atomic mass the mass number | MISCONCEPTION |  | high |

