# C11 Diff Review Bundle — pending §18 edge promotions (generated 2026-09-13)

- baseline commit: `b688140`
- state fingerprint: `a956ab5f5f27` (promo_count=79)
- actionable: 39 edges (clean 39 / pending-flagged 0); not-actionable: 5; nodes awaiting a pathway: 91
- preview fidelity: simulator re-emits graph/concept_edges.yaml under the generator's own serialization contract with a byte-identity guard — what you read is what G13 will write.

## Batch approval

```bash
cd work/syllabai-resources && python3 scripts/c11_diff_review.py approve \
  '4CH1-CON-ANODE-CATHODE REQUIRES_PREREQUISITE 4CH1-CON-ION' \
  '4CH1-CON-AQUEOUS-DISCHARGE REQUIRES_PREREQUISITE 4CH1-CON-ELECTROLYSIS' \
  '4CH1-CON-COVALENT-BOND REQUIRES_PREREQUISITE 4CH1-CON-ATOM' \
  '4CH1-CON-COVALENT-BOND REQUIRES_PREREQUISITE 4CH1-CON-ELECTRONIC-CONFIGURATION' \
  '4CH1-CON-COVALENT-CONDUCTION REQUIRES_PREREQUISITE 4CH1-CON-SIMPLE-MOLECULAR' \
  '4CH1-CON-DIAMOND-GRAPHITE RELATED_TO 4CH1-CON-SIMPLE-MOLECULAR' \
  '4CH1-CON-DIAMOND-GRAPHITE REQUIRES_PREREQUISITE 4CH1-CON-GIANT-COVALENT' \
  '4CH1-CON-DOT-CROSS-COVALENT REQUIRES_PREREQUISITE 4CH1-CON-COVALENT-BOND' \
  '4CH1-CON-DOT-CROSS-COVALENT REQUIRES_PREREQUISITE 4CH1-CON-MOLECULE' \
  '4CH1-CON-DOT-CROSS-IONIC REQUIRES_PREREQUISITE 4CH1-CON-ION' \
  '4CH1-CON-ELECTRODE-HALF-EQUATIONS REQUIRES_PREREQUISITE 4CH1-CON-ELECTROLYSIS' \
  '4CH1-CON-ELECTRODE-HALF-EQUATIONS REQUIRES_PREREQUISITE 4CH1-CON-REDOX-ELECTRONS' \
  '4CH1-CON-ELECTROLYSIS REQUIRES_PREREQUISITE 4CH1-CON-ANODE-CATHODE' \
  '4CH1-CON-ELECTROLYSIS REQUIRES_PREREQUISITE 4CH1-CON-IONIC-BOND' \
  '4CH1-CON-ELECTROLYSIS REQUIRES_PREREQUISITE 4CH1-CON-IONIC-CONDUCTION' \
  '4CH1-CON-GIANT-COVALENT REQUIRES_PREREQUISITE 4CH1-CON-COVALENT-BOND' \
  '4CH1-CON-ION REQUIRES_PREREQUISITE 4CH1-CON-ATOM' \
  '4CH1-CON-ION REQUIRES_PREREQUISITE 4CH1-CON-ELECTRONIC-CONFIGURATION' \
  '4CH1-CON-ION-CHARGE-RULES REQUIRES_PREREQUISITE 4CH1-CON-ION' \
  '4CH1-CON-IONIC-BOND COMMONLY_CONFUSED_WITH 4CH1-CON-COVALENT-BOND' \
  '4CH1-CON-IONIC-BOND REQUIRES_PREREQUISITE 4CH1-CON-ION' \
  '4CH1-CON-IONIC-CONDUCTION REQUIRES_PREREQUISITE 4CH1-CON-ION' \
  '4CH1-CON-IONIC-CONDUCTION REQUIRES_PREREQUISITE 4CH1-CON-IONIC-LATTICE' \
  '4CH1-CON-IONIC-FORMULA REQUIRES_PREREQUISITE 4CH1-CON-ION-CHARGE-RULES' \
  '4CH1-CON-IONIC-LATTICE REQUIRES_PREREQUISITE 4CH1-CON-IONIC-BOND' \
  '4CH1-CON-METAL-PROPERTIES EXPLAINED_BY 4CH1-CON-METALLIC-BOND' \
  '4CH1-CON-METALLIC-BOND REQUIRES_PREREQUISITE 4CH1-CON-ION' \
  '4CH1-CON-SIMPLE-MOLECULAR REQUIRES_PREREQUISITE 4CH1-CON-COVALENT-BOND' \
  '4CH1-CON-SIMPLE-MOLECULAR REQUIRES_PREREQUISITE 4CH1-CON-MOLECULE' \
  '4CH1-MIS-COVALENT-BONDS-BROKEN REMEDIATED_BY 4CH1-CON-SIMPLE-MOLECULAR' \
  '4CH1-MIS-COVALENT-BONDS-BROKEN WRONG_ANSWER_PATTERN 4CH1-CON-SIMPLE-MOLECULAR' \
  '4CH1-MIS-GRAPHITE-LAYER-BONDS REMEDIATED_BY 4CH1-CON-DIAMOND-GRAPHITE' \
  '4CH1-MIS-GRAPHITE-LAYER-BONDS WRONG_ANSWER_PATTERN 4CH1-CON-DIAMOND-GRAPHITE' \
  '4CH1-MIS-IONIC-BOND-ATOMS REMEDIATED_BY 4CH1-CON-IONIC-BOND' \
  '4CH1-MIS-IONIC-BOND-ATOMS WRONG_ANSWER_PATTERN 4CH1-CON-IONIC-BOND' \
  '4CH1-MIS-IONIC-CONDUCTION-ELECTRONS MISCONCEPTION_OF 4CH1-CON-IONIC-CONDUCTION' \
  '4CH1-MIS-IONIC-CONDUCTION-ELECTRONS REMEDIATED_BY 4CH1-CON-IONIC-CONDUCTION' \
  '4CH1-PR-04 REQUIRES_PREREQUISITE 4CH1-CON-AQUEOUS-DISCHARGE' \
  '4CH1-PR-04 REQUIRES_PREREQUISITE 4CH1-CON-ELECTROLYSIS' \
  --by <operator> --date 2026-09-13 --review-ref graph/reports/C11_DIFF_REVIEW_B3_2026-09-13.md
```

Pending-flagged (PENDING operator_decision) edges are excluded from the command above; approving them additionally requires `--include-pending` — that flag records the explicit decision this bundle presents.

## Index

| # | identity | confidence | flag |
|---|----------|------------|------|
| 1 | `4CH1-CON-ANODE-CATHODE REQUIRES_PREREQUISITE 4CH1-CON-ION` | high |  |
| 2 | `4CH1-CON-AQUEOUS-DISCHARGE REQUIRES_PREREQUISITE 4CH1-CON-ELECTROLYSIS` | high |  |
| 3 | `4CH1-CON-COVALENT-BOND REQUIRES_PREREQUISITE 4CH1-CON-ATOM` | high |  |
| 4 | `4CH1-CON-COVALENT-BOND REQUIRES_PREREQUISITE 4CH1-CON-ELECTRONIC-CONFIGURATION` | high |  |
| 5 | `4CH1-CON-COVALENT-CONDUCTION REQUIRES_PREREQUISITE 4CH1-CON-SIMPLE-MOLECULAR` | high |  |
| 6 | `4CH1-CON-DIAMOND-GRAPHITE RELATED_TO 4CH1-CON-SIMPLE-MOLECULAR` | medium |  |
| 7 | `4CH1-CON-DIAMOND-GRAPHITE REQUIRES_PREREQUISITE 4CH1-CON-GIANT-COVALENT` | high |  |
| 8 | `4CH1-CON-DOT-CROSS-COVALENT REQUIRES_PREREQUISITE 4CH1-CON-COVALENT-BOND` | high |  |
| 9 | `4CH1-CON-DOT-CROSS-COVALENT REQUIRES_PREREQUISITE 4CH1-CON-MOLECULE` | high |  |
| 10 | `4CH1-CON-DOT-CROSS-IONIC REQUIRES_PREREQUISITE 4CH1-CON-ION` | high |  |
| 11 | `4CH1-CON-ELECTRODE-HALF-EQUATIONS REQUIRES_PREREQUISITE 4CH1-CON-ELECTROLYSIS` | high |  |
| 12 | `4CH1-CON-ELECTRODE-HALF-EQUATIONS REQUIRES_PREREQUISITE 4CH1-CON-REDOX-ELECTRONS` | high |  |
| 13 | `4CH1-CON-ELECTROLYSIS REQUIRES_PREREQUISITE 4CH1-CON-ANODE-CATHODE` | high |  |
| 14 | `4CH1-CON-ELECTROLYSIS REQUIRES_PREREQUISITE 4CH1-CON-IONIC-BOND` | high |  |
| 15 | `4CH1-CON-ELECTROLYSIS REQUIRES_PREREQUISITE 4CH1-CON-IONIC-CONDUCTION` | high |  |
| 16 | `4CH1-CON-GIANT-COVALENT REQUIRES_PREREQUISITE 4CH1-CON-COVALENT-BOND` | high |  |
| 17 | `4CH1-CON-ION REQUIRES_PREREQUISITE 4CH1-CON-ATOM` | high |  |
| 18 | `4CH1-CON-ION REQUIRES_PREREQUISITE 4CH1-CON-ELECTRONIC-CONFIGURATION` | high |  |
| 19 | `4CH1-CON-ION-CHARGE-RULES REQUIRES_PREREQUISITE 4CH1-CON-ION` | high |  |
| 20 | `4CH1-CON-IONIC-BOND COMMONLY_CONFUSED_WITH 4CH1-CON-COVALENT-BOND` | high |  |
| 21 | `4CH1-CON-IONIC-BOND REQUIRES_PREREQUISITE 4CH1-CON-ION` | high |  |
| 22 | `4CH1-CON-IONIC-CONDUCTION REQUIRES_PREREQUISITE 4CH1-CON-ION` | high |  |
| 23 | `4CH1-CON-IONIC-CONDUCTION REQUIRES_PREREQUISITE 4CH1-CON-IONIC-LATTICE` | high |  |
| 24 | `4CH1-CON-IONIC-FORMULA REQUIRES_PREREQUISITE 4CH1-CON-ION-CHARGE-RULES` | high |  |
| 25 | `4CH1-CON-IONIC-LATTICE REQUIRES_PREREQUISITE 4CH1-CON-IONIC-BOND` | high |  |
| 26 | `4CH1-CON-METAL-PROPERTIES EXPLAINED_BY 4CH1-CON-METALLIC-BOND` | high |  |
| 27 | `4CH1-CON-METALLIC-BOND REQUIRES_PREREQUISITE 4CH1-CON-ION` | high |  |
| 28 | `4CH1-CON-SIMPLE-MOLECULAR REQUIRES_PREREQUISITE 4CH1-CON-COVALENT-BOND` | high |  |
| 29 | `4CH1-CON-SIMPLE-MOLECULAR REQUIRES_PREREQUISITE 4CH1-CON-MOLECULE` | high |  |
| 30 | `4CH1-MIS-COVALENT-BONDS-BROKEN REMEDIATED_BY 4CH1-CON-SIMPLE-MOLECULAR` | high |  |
| 31 | `4CH1-MIS-COVALENT-BONDS-BROKEN WRONG_ANSWER_PATTERN 4CH1-CON-SIMPLE-MOLECULAR` | high |  |
| 32 | `4CH1-MIS-GRAPHITE-LAYER-BONDS REMEDIATED_BY 4CH1-CON-DIAMOND-GRAPHITE` | high |  |
| 33 | `4CH1-MIS-GRAPHITE-LAYER-BONDS WRONG_ANSWER_PATTERN 4CH1-CON-DIAMOND-GRAPHITE` | high |  |
| 34 | `4CH1-MIS-IONIC-BOND-ATOMS REMEDIATED_BY 4CH1-CON-IONIC-BOND` | high |  |
| 35 | `4CH1-MIS-IONIC-BOND-ATOMS WRONG_ANSWER_PATTERN 4CH1-CON-IONIC-BOND` | high |  |
| 36 | `4CH1-MIS-IONIC-CONDUCTION-ELECTRONS MISCONCEPTION_OF 4CH1-CON-IONIC-CONDUCTION` | high |  |
| 37 | `4CH1-MIS-IONIC-CONDUCTION-ELECTRONS REMEDIATED_BY 4CH1-CON-IONIC-CONDUCTION` | high |  |
| 38 | `4CH1-PR-04 REQUIRES_PREREQUISITE 4CH1-CON-AQUEOUS-DISCHARGE` | high |  |
| 39 | `4CH1-PR-04 REQUIRES_PREREQUISITE 4CH1-CON-ELECTROLYSIS` | high |  |

## Pending items — the exact diff each approval applies

### 1. `4CH1-CON-ANODE-CATHODE REQUIRES_PREREQUISITE 4CH1-CON-ION` [high]

- node 4CH1-CON-ANODE-CATHODE — Anions and cations (negative and positive ions) and their migration to cathode and anode (CONCEPT)
-   spec 4CH1-1.57C [CORE]: know that anion and cation are terms used to refer to negative and positive ions respectively
- node 4CH1-CON-ION — Ion (formation by electron loss or gain) (CONCEPT)
-   spec 4CH1-1.37 [CORE]: understand how ions are formed by electron loss or gain
- derivation: DEFINITIONAL_DEPENDENCY — The 1.57C terms are defined IN TERMS OF ions ("Anions are negatively charged ions; Cations are positively charged ions") — the ion is the definitional operand of both terms.
- `NOTE` Electronic conductivity - IGCSE Chemistry Revision Notes.md — "Anions are negatively charged ions"

```diff
@@ -3068,7 +3068,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.57C @ Electronic Conductivity (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-AQUEOUS-DISCHARGE
```

### 2. `4CH1-CON-AQUEOUS-DISCHARGE REQUIRES_PREREQUISITE 4CH1-CON-ELECTROLYSIS` [high]

- node 4CH1-CON-AQUEOUS-DISCHARGE — Selective discharge in aqueous electrolysis (halide preference at the anode; hydrogen vs metal at the cathode) (CONCEPT)
-   spec 4CH1-1.58C [CORE]: describe experiments to investigate electrolysis, using inert electrodes, of molten compounds...
- node 4CH1-CON-ELECTROLYSIS — Electrolysis (decomposition by direct current: molten binary compounds and their element products, using inert electrodes) (CONCEPT)
-   spec 4CH1-1.58C [CORE]: describe experiments to investigate electrolysis, using inert electrodes, of molten compounds...
- derivation: USED_WITHOUT_RETEACHING — The aqueous discharge rules extend the electrolysis process to mixed-ion electrolytes — the note builds on the already-taught process ("We NOW have an electrolyte...") and the Examiner Tip presupposes the whole setup ("first write down all of the ions present first, only then start comparing their reactivity").
- `NOTE` Electrolysis diagram - IGCSE Chemistry Revision Notes.md — "We now have an electrolyte that contains ions from the compound plus ions from the water"

```diff
@@ -3091,7 +3091,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.58C @ Electrolysis Diagram (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-AR
```

### 3. `4CH1-CON-COVALENT-BOND REQUIRES_PREREQUISITE 4CH1-CON-ATOM` [high]

- node 4CH1-CON-COVALENT-BOND — Covalent bond (shared pair of electrons; electrostatic attraction between the shared pair and the nuclei) (CONCEPT)
-   spec 4CH1-1.44 [CORE]: know that a covalent bond is formed between atoms by the sharing of a pair of electrons
-   spec 4CH1-1.45 [CORE]: understand covalent bonds in terms of electrostatic attractions
- node 4CH1-CON-ATOM — Atom (definition and subatomic composition) (CONCEPT)
-   spec 4CH1-1.14 [CORE]: know what is meant by the terms atom and molecule
- derivation: DEFINITIONAL_DEPENDENCY — Cross-boundary edge (target = the batch-2 CON-ATOM node, sanctioned): the covalent bond is defined as sharing BETWEEN atoms — the atom is the definitional operand (the MOLECULE -> ATOM pattern).
- `NOTE` Forming covalent bonds - IGCSE Chemistry Revision Notes.md — "When atoms share pairs of electrons, they form covalent bonds"

```diff
@@ -3311,7 +3311,9 @@ edges:
       by the batch-2 record (4CH1-1.14)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-COVALENT-BOND
```

### 4. `4CH1-CON-COVALENT-BOND REQUIRES_PREREQUISITE 4CH1-CON-ELECTRONIC-CONFIGURATION` [high]

- node 4CH1-CON-COVALENT-BOND — Covalent bond (shared pair of electrons; electrostatic attraction between the shared pair and the nuclei) (CONCEPT)
-   spec 4CH1-1.44 [CORE]: know that a covalent bond is formed between atoms by the sharing of a pair of electrons
-   spec 4CH1-1.45 [CORE]: understand covalent bonds in terms of electrostatic attractions
- node 4CH1-CON-ELECTRONIC-CONFIGURATION — Electronic configuration of the first 20 elements (shells 2, 8, 8; configuration and Periodic Table position) (CONCEPT)
-   spec 4CH1-1.19 [CORE]: understand how to deduce the electronic configurations of the first 20 elements from their po...
-   spec 4CH1-1.22 [CORE]: understand how the electronic configuration of a main group element is related to its positio...
- derivation: DEFINITIONAL_DEPENDENCY — Cross-boundary edge (target = the batch-2 CON-ELECTRONIC-CONFIGURATION node, sanctioned): the sharing motive is stated as obtaining a FULL OUTER SHELL — the configuration concept is the operand of why covalent bonds form (the ION -> CONFIG pattern applied to the covalent side).
- `NOTE` Forming covalent bonds - IGCSE Chemistry Revision Notes.md — "Non-metal atoms can share electrons with other non-metal atoms to obtain a full outer shell of electrons"

```diff
@@ -3335,7 +3335,9 @@ edges:
       by the batch-2 record (4CH1-1.19/1.22)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-COVALENT-CONDUCTION
```

### 5. `4CH1-CON-COVALENT-CONDUCTION REQUIRES_PREREQUISITE 4CH1-CON-SIMPLE-MOLECULAR` [high]

- node 4CH1-CON-COVALENT-CONDUCTION — Covalent compounds do not conduct electricity (no freely moving charged particles) (CONCEPT)
-   spec 4CH1-1.51 [CORE]: know that covalent compounds do not usually conduct electricity
-   spec 4CH1-1.55C [CORE]: understand why covalent compounds do not conduct electricity
- node 4CH1-CON-SIMPLE-MOLECULAR — Simple molecular structures (weak intermolecular forces; low melting and boiling points; the relative-molecular-mass trend) (CONCEPT)
-   spec 4CH1-1.47 [CORE]: explain why substances with a simple molecular structures are gases or liquids, or solids wit...
-   spec 4CH1-1.48 [CORE]: explain why the melting and boiling points of substances with simple molecular structures inc...
- derivation: USED_WITHOUT_RETEACHING — The 1.51/1.55C no-conduction statements are ABOUT simple molecular structures (the note section is titled Conductivity of simple molecular structures) — the classification is the operand the conductivity explanation presupposes; the direct COVALENT-BOND dependency is transitively covered via SIMPLE-MOLECULAR -> COVALENT-BOND.
- `NOTE` Simple molecular structures - IGCSE Chemistry Revision Notes.md — "Simple molecular structures are poor conductors of electricity (even when molten)"
- `NOTE` Simple molecular structures - IGCSE Chemistry Revision Notes.md — "There are no free ions or electrons to move and carry the charge"

```diff
@@ -3363,7 +3363,9 @@ edges:
       4CH1-1.55C @ Electronic Conductivity (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-CRYSTALLISATION
```

### 6. `4CH1-CON-DIAMOND-GRAPHITE RELATED_TO 4CH1-CON-SIMPLE-MOLECULAR` [medium]

- node 4CH1-CON-DIAMOND-GRAPHITE — Structures and properties of diamond, graphite and C60 fullerene (allotropes of carbon) (CONCEPT)
-   spec 4CH1-1.50 [CORE]: explain how the structures of diamond, graphite and C60 fullerene influence their physical pr...
- node 4CH1-CON-SIMPLE-MOLECULAR — Simple molecular structures (weak intermolecular forces; low melting and boiling points; the relative-molecular-mass trend) (CONCEPT)
-   spec 4CH1-1.47 [CORE]: explain why substances with a simple molecular structures are gases or liquids, or solids wit...
-   spec 4CH1-1.48 [CORE]: explain why the melting and boiling points of substances with simple molecular structures inc...
- derivation: RELATED_RESIDUAL — The 1.50 allotrope set spans BOTH structure classes: diamond and graphite are giant covalent (the prereq edge) while C60 fullerene is simple molecular with weak intermolecular forces between the buckyballs — the note states the class assignment directly. A residual association (not a dependency: the diamond/graphite content does not presuppose the simple-molecular concept; not a confusion statement: the corpus documents no term-pair confusability for the two structure classes).
- `NOTE` Simple molecular structures - IGCSE Chemistry Revision Notes.md — "C60 is a simple molecular structure"

```diff
@@ -5488,7 +5488,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.50 @ Simple Molecular Structures (2026-09-11)
     generated_date: '2026-09-12'
   confidence: medium
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   ambiguity_note: First RELATED_TO deployment in the store; the relation is genuinely residual (the C60
     content could alternatively attach the 1.50 SP to CON-SIMPLE-MOLECULAR — an operator identity decision
     on the sheet).
```

### 7. `4CH1-CON-DIAMOND-GRAPHITE REQUIRES_PREREQUISITE 4CH1-CON-GIANT-COVALENT` [high]

- node 4CH1-CON-DIAMOND-GRAPHITE — Structures and properties of diamond, graphite and C60 fullerene (allotropes of carbon) (CONCEPT)
-   spec 4CH1-1.50 [CORE]: explain how the structures of diamond, graphite and C60 fullerene influence their physical pr...
- node 4CH1-CON-GIANT-COVALENT — Giant covalent structures (solids with high melting and boiling points) (CONCEPT)
-   spec 4CH1-1.49 [CORE]: explain why substances with giant covalent structures are solids with high melting and boilin...
- derivation: USED_WITHOUT_RETEACHING — The 1.50 allotrope properties are explained in terms of the giant covalent structure (diamond: each carbon bonded to four others; graphite: high mp "because it has a giant covalent structure") — the note uses the 1.49 structure class as given ground for two of the three allotropes (the C60 half is simple molecular, carried by the RELATED_TO edge).
- `NOTE` Giant covalent structures - IGCSE Chemistry Revision Notes.md — "Examples include diamond and graphite"

```diff
@@ -3438,7 +3438,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.49/1.50 @ Giant Covalent Structures (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-DOT-CROSS-COVALENT
```

### 8. `4CH1-CON-DOT-CROSS-COVALENT REQUIRES_PREREQUISITE 4CH1-CON-COVALENT-BOND` [high]

- node 4CH1-CON-DOT-CROSS-COVALENT — Dot-and-cross diagrams for covalent substances (diatomic, inorganic and organic molecules) (CONCEPT)
-   spec 4CH1-1.46 [CORE]: understand how to use dot-and-cross diagrams to represent covalent bonds in: • diatomic molec...
- node 4CH1-CON-COVALENT-BOND — Covalent bond (shared pair of electrons; electrostatic attraction between the shared pair and the nuclei) (CONCEPT)
-   spec 4CH1-1.44 [CORE]: know that a covalent bond is formed between atoms by the sharing of a pair of electrons
-   spec 4CH1-1.45 [CORE]: understand covalent bonds in terms of electrostatic attractions
- derivation: USED_WITHOUT_RETEACHING — The covalent dot-and-cross convention is legible only in terms of the shared-pair bond it represents ("each covalent bond represents one shared pair of electrons") — the note presupposes the 1.44 bond concept while teaching the 1.46 representation (the DOT-CROSS-IONIC -> ION pattern).
- `NOTE` Covalent Bonds Dot & Cross Diagrams  Edexcel IGCSE Chemistry Revision Notes 2017.md — "Each covalent bond represents one shared pair of electrons"

```diff
@@ -3460,7 +3460,9 @@ edges:
     upstream: 'T-C10 HUMAN_VALIDATED 4CH1-1.46 @ Covalent Bonds: Dot & Cross Diagrams (2026-09-11)'
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-DOT-CROSS-COVALENT
```

### 9. `4CH1-CON-DOT-CROSS-COVALENT REQUIRES_PREREQUISITE 4CH1-CON-MOLECULE` [high]

- node 4CH1-CON-DOT-CROSS-COVALENT — Dot-and-cross diagrams for covalent substances (diatomic, inorganic and organic molecules) (CONCEPT)
-   spec 4CH1-1.46 [CORE]: understand how to use dot-and-cross diagrams to represent covalent bonds in: • diatomic molec...
- node 4CH1-CON-MOLECULE — Molecule (CONCEPT)
-   spec 4CH1-1.14 [CORE]: know what is meant by the terms atom and molecule
- derivation: DEFINITIONAL_DEPENDENCY — Cross-boundary edge (target = the batch-2 CON-MOLECULE node, sanctioned): the covalent diagrams are diagrams OF molecules ("representation of a molecule of hydrogen/chlorine/oxygen...") — the molecule is the definitional operand of what the 1.46 diagrams depict (every caption in the note).
- `NOTE` Covalent Bonds Dot & Cross Diagrams  Edexcel IGCSE Chemistry Revision Notes 2017.md — "Dot & cross representation of a molecule of hydrogen"

```diff
@@ -3484,7 +3484,9 @@ edges:
       node owned by the batch-2 record (4CH1-1.14)'
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-DOT-CROSS-IONIC
```

### 10. `4CH1-CON-DOT-CROSS-IONIC REQUIRES_PREREQUISITE 4CH1-CON-ION` [high]

- node 4CH1-CON-DOT-CROSS-IONIC — Dot-and-cross diagrams for ionic compounds (electron transfer) (CONCEPT)
-   spec 4CH1-1.40 [CORE]: draw dot-and-cross diagrams to show the formation of ionic compounds by electron transfer，lim...
- node 4CH1-CON-ION — Ion (formation by electron loss or gain) (CONCEPT)
-   spec 4CH1-1.37 [CORE]: understand how ions are formed by electron loss or gain
- derivation: USED_WITHOUT_RETEACHING — The ionic dot-and-cross convention represents the formation of IONS by electron transfer (brackets, superscript charges) — the note narrates ion formation without re-teaching the ion concept (the 1.37 ground), and the diagram is unreadable without it.
- `NOTE` Ionic bonding diagrams - IGCSE Chemistry Revision Notes.md — "A chlorine atom will gain an electron to form a negatively charged chloride ion with a charge of 1-"

```diff
@@ -3507,7 +3507,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.37/1.40 @ Ionic Bonding Diagrams (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-ELECTRODE-HALF-EQUATIONS
```

### 11. `4CH1-CON-ELECTRODE-HALF-EQUATIONS REQUIRES_PREREQUISITE 4CH1-CON-ELECTROLYSIS` [high]

- node 4CH1-CON-ELECTRODE-HALF-EQUATIONS — Ionic half-equations for the electrode reactions during electrolysis (CONCEPT)
-   spec 4CH1-1.59C [CORE]: write ionic half-equations representing the reactions at the electrodes during electrolysis a...
- node 4CH1-CON-ELECTROLYSIS — Electrolysis (decomposition by direct current: molten binary compounds and their element products, using inert electrodes) (CONCEPT)
-   spec 4CH1-1.58C [CORE]: describe experiments to investigate electrolysis, using inert electrodes, of molten compounds...
- derivation: USED_WITHOUT_RETEACHING — The half equations describe the electrode reactions of the already-established electrolysis process (the note opens with "In electrochemistry we are mostly concerned with the transfer of electrons" and every worked example is one of the 1.58C solutions) — the process is the operand the equations are written about.
- `NOTE` Half equations - IGCSE Chemistry Revision Notes.md — "As the ions come into contact with the electrode, electrons are either lost or gained and they form neutral..."

```diff
@@ -3531,7 +3531,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.59C @ Half Equations (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-ELECTRODE-HALF-EQUATIONS
```

### 12. `4CH1-CON-ELECTRODE-HALF-EQUATIONS REQUIRES_PREREQUISITE 4CH1-CON-REDOX-ELECTRONS` [high]

- node 4CH1-CON-ELECTRODE-HALF-EQUATIONS — Ionic half-equations for the electrode reactions during electrolysis (CONCEPT)
-   spec 4CH1-1.59C [CORE]: write ionic half-equations representing the reactions at the electrodes during electrolysis a...
- node 4CH1-CON-REDOX-ELECTRONS — Oxidation and reduction in terms of electron loss and gain (CONCEPT)
-   spec 4CH1-1.59C [CORE]: write ionic half-equations representing the reactions at the electrodes during electrolysis a...
- derivation: DEFINITIONAL_DEPENDENCY — Classifying each half-equation as oxidation or reduction is defined IN TERMS OF the electron loss/gain definitions — the 1.59C "understand why these reactions are classified" demand is the definitional operand relation between the two sibling nodes.
- `NOTE` Half equations - IGCSE Chemistry Revision Notes.md — "hence the definitions of oxidation and reduction are applied in terms of electron loss or gain rather than ..."

```diff
@@ -3554,7 +3554,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.59C @ Half Equations (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-ELECTROLYSIS
```

### 13. `4CH1-CON-ELECTROLYSIS REQUIRES_PREREQUISITE 4CH1-CON-ANODE-CATHODE` [high]

- node 4CH1-CON-ELECTROLYSIS — Electrolysis (decomposition by direct current: molten binary compounds and their element products, using inert electrodes) (CONCEPT)
-   spec 4CH1-1.58C [CORE]: describe experiments to investigate electrolysis, using inert electrodes, of molten compounds...
- node 4CH1-CON-ANODE-CATHODE — Anions and cations (negative and positive ions) and their migration to cathode and anode (CONCEPT)
-   spec 4CH1-1.57C [CORE]: know that anion and cation are terms used to refer to negative and positive ions respectively
- derivation: USED_WITHOUT_RETEACHING — The electrolysis product rules are stated IN TERMS OF the electrode terms (cathode/anode and their polarities) — the 1.57C terms are used throughout the 1.58C note without re-teaching them (the Worked Example: "Copper ions have a positive charge so are attracted to the cathode").
- `NOTE` Electrolysis diagram - IGCSE Chemistry Revision Notes.md — "The positive ion will migrate towards the cathode and the negative ion will migrate towards the anode"

```diff
@@ -3577,7 +3577,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.58C @ Electrolysis Diagram (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-ELECTROLYSIS
```

### 14. `4CH1-CON-ELECTROLYSIS REQUIRES_PREREQUISITE 4CH1-CON-IONIC-BOND` [high]

- node 4CH1-CON-ELECTROLYSIS — Electrolysis (decomposition by direct current: molten binary compounds and their element products, using inert electrodes) (CONCEPT)
-   spec 4CH1-1.58C [CORE]: describe experiments to investigate electrolysis, using inert electrodes, of molten compounds...
- node 4CH1-CON-IONIC-BOND — Ionic bonding (electrostatic attraction between oppositely charged ions) (CONCEPT)
-   spec 4CH1-1.41 [CORE]: understand ionic bonding in terms of electrostatic attractions
- derivation: USED_WITHOUT_RETEACHING — The 1.58C electrolysis content opens by taking IONIC compounds as its subject without re-teaching the bonding ("Binary ionic compound are compounds consisting of just two elements joined together by ionic bonding" — the note names the 1.41 concept as given ground). Not subsumed by the emitted conduction chain (transitively reachable but carrying different information: the composition of what is electrolysed — the §19 MOLAR-MASS reachable-ne-redundant precedent).
- `NOTE` Electrolysis diagram - IGCSE Chemistry Revision Notes.md — "Binary ionic compound are compounds consisting of just two elements joined together by ionic bonding"

```diff
@@ -3602,7 +3602,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.58C @ Electrolysis Diagram (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-ELECTROLYSIS
```

### 15. `4CH1-CON-ELECTROLYSIS REQUIRES_PREREQUISITE 4CH1-CON-IONIC-CONDUCTION` [high]

- node 4CH1-CON-ELECTROLYSIS — Electrolysis (decomposition by direct current: molten binary compounds and their element products, using inert electrodes) (CONCEPT)
-   spec 4CH1-1.58C [CORE]: describe experiments to investigate electrolysis, using inert electrodes, of molten compounds...
- node 4CH1-CON-IONIC-CONDUCTION — Ionic conduction (solid insulator; molten and aqueous conductor via mobile ions) (CONCEPT)
-   spec 4CH1-1.43 [CORE]: know that ionic compounds do not conduct electricity when solid，but do conduct electricity wh...
-   spec 4CH1-1.56C [CORE]: understand why ionic compounds conduct electricity only when molten or in aqueous solution
- derivation: USED_WITHOUT_RETEACHING — Electrolysis presupposes the molten-conduction mechanism — the note states it as given ground ("they become molten and can conduct electricity as their ions can move freely") in its opening section; the 1.43/1.56C concept is the operand the whole process runs on.
- `NOTE` Electrolysis diagram - IGCSE Chemistry Revision Notes.md — "When these compounds are heated beyond their melting point, they become molten and can conduct electricity ..."

```diff
@@ -3625,7 +3625,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.58C @ Electrolysis Diagram (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-ELECTRONIC-CONFIGURATION
```

### 16. `4CH1-CON-GIANT-COVALENT REQUIRES_PREREQUISITE 4CH1-CON-COVALENT-BOND` [high]

- node 4CH1-CON-GIANT-COVALENT — Giant covalent structures (solids with high melting and boiling points) (CONCEPT)
-   spec 4CH1-1.49 [CORE]: explain why substances with giant covalent structures are solids with high melting and boilin...
- node 4CH1-CON-COVALENT-BOND — Covalent bond (shared pair of electrons; electrostatic attraction between the shared pair and the nuclei) (CONCEPT)
-   spec 4CH1-1.44 [CORE]: know that a covalent bond is formed between atoms by the sharing of a pair of electrons
-   spec 4CH1-1.45 [CORE]: understand covalent bonds in terms of electrostatic attractions
- derivation: DEFINITIONAL_DEPENDENCY — The giant covalent structure is defined IN TERMS OF atoms bonded via strong covalent bonds (the whole 1.49 explanation is "strong covalent bonds between atoms... lots of energy to overcome") — the 1.44 bond is the definitional operand of the 1.49 structure.
- `NOTE` Giant covalent structures - IGCSE Chemistry Revision Notes.md — "They have a huge number of non-metal atoms bonded to other non-metal atoms via strong covalent bonds"

```diff
@@ -3938,7 +3938,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.49 @ Giant Covalent Structures (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-GROUP-SIMILARITY
```

### 17. `4CH1-CON-ION REQUIRES_PREREQUISITE 4CH1-CON-ATOM` [high]

- node 4CH1-CON-ION — Ion (formation by electron loss or gain) (CONCEPT)
-   spec 4CH1-1.37 [CORE]: understand how ions are formed by electron loss or gain
- node 4CH1-CON-ATOM — Atom (definition and subatomic composition) (CONCEPT)
-   spec 4CH1-1.14 [CORE]: know what is meant by the terms atom and molecule
- derivation: DEFINITIONAL_DEPENDENCY — Cross-boundary edge (target = the batch-2 CON-ATOM node, sanctioned per FN-B1-2/FN-B2-2 — no duplicate atom mint): the ion definition is stated IN TERMS OF the atom ("an electrically charged atom or group of atoms") — the atom is the definitional operand (the batch-2 MOLECULE -> ATOM pattern).
- `NOTE` Formation of ions - IGCSE Chemistry Revision Notes.md — "An ion is an electrically charged atom or group of atoms formed by the loss or gain of electrons"

```diff
@@ -3986,7 +3986,9 @@ edges:
       batch-2 record (4CH1-1.14)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-ION
```

### 18. `4CH1-CON-ION REQUIRES_PREREQUISITE 4CH1-CON-ELECTRONIC-CONFIGURATION` [high]

- node 4CH1-CON-ION — Ion (formation by electron loss or gain) (CONCEPT)
-   spec 4CH1-1.37 [CORE]: understand how ions are formed by electron loss or gain
- node 4CH1-CON-ELECTRONIC-CONFIGURATION — Electronic configuration of the first 20 elements (shells 2, 8, 8; configuration and Periodic Table position) (CONCEPT)
-   spec 4CH1-1.19 [CORE]: understand how to deduce the electronic configurations of the first 20 elements from their po...
-   spec 4CH1-1.22 [CORE]: understand how the electronic configuration of a main group element is related to its positio...
- derivation: DEFINITIONAL_DEPENDENCY — Cross-boundary edge (target = the batch-2 CON-ELECTRONIC-CONFIGURATION node, sanctioned): the ion-formation mechanism is defined BY the full-outer-shell configuration goal — the outer-shell concept is the definitional operand of why ions form.
- `NOTE` Formation of ions - IGCSE Chemistry Revision Notes.md — "This loss or gain of electrons takes place to obtain a full outer shell of electrons"

```diff
@@ -4009,7 +4009,9 @@ edges:
       batch-2 record (4CH1-1.19/1.22)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-ION-CHARGE-RULES
```

### 19. `4CH1-CON-ION-CHARGE-RULES REQUIRES_PREREQUISITE 4CH1-CON-ION` [high]

- node 4CH1-CON-ION-CHARGE-RULES — Common ion charges (group-based and named-ion table, with the deduction rule) (CONCEPT)
-   spec 4CH1-1.38 [CORE]: know the charges of these ions: •metals in Groups 1,2 and 3 •non-metals in Groups 5,6 and 7 •...
- node 4CH1-CON-ION — Ion (formation by electron loss or gain) (CONCEPT)
-   spec 4CH1-1.37 [CORE]: understand how ions are formed by electron loss or gain
- derivation: USED_WITHOUT_RETEACHING — The 1.38 charge tables and the deduction rule are charges OF ions — the note states the gain/donate-to-charge rule without re-teaching what an ion is (the 1.37 ground), and the examiner tip presupposes it ("the charges of all the ions shown in the above tables").
- `NOTE` Common Ions  Edexcel IGCSE Chemistry Revision Notes 2017.md — "Atoms that gain electrons become negative ions and atoms that donate electron forms positive ion"

```diff
@@ -4032,7 +4032,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.37/1.38 @ Common Ions (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-IONIC-BOND
```

### 20. `4CH1-CON-IONIC-BOND COMMONLY_CONFUSED_WITH 4CH1-CON-COVALENT-BOND` [high]

- node 4CH1-CON-IONIC-BOND — Ionic bonding (electrostatic attraction between oppositely charged ions) (CONCEPT)
-   spec 4CH1-1.41 [CORE]: understand ionic bonding in terms of electrostatic attractions
- node 4CH1-CON-COVALENT-BOND — Covalent bond (shared pair of electrons; electrostatic attraction between the shared pair and the nuclei) (CONCEPT)
-   spec 4CH1-1.44 [CORE]: know that a covalent bond is formed between atoms by the sharing of a pair of electrons
-   spec 4CH1-1.45 [CORE]: understand covalent bonds in terms of electrostatic attractions
- derivation: EXAMINER_TIP_EXPLICIT — The corpus itself documents the bond-type contrast as a key learning difference (the Examiner Tips block states the share-vs-transfer distinction explicitly) and both pinned Paper-2 MS document the cross-referenced REJECTs (ionic answers rejected for mentioning covalent, covalent answers capped for mentioning ionic/metallic — inadmissible as CCW evidence per G07 but recorded here as assessment context). The second CCW edge in the store (the batch-2 ATOMIC-NUMBER/MASS-NUMBER precedent).
- `NOTE` Forming covalent bonds - IGCSE Chemistry Revision Notes.md — "A key difference between covalent bonds and ionic bonds is that in covalent bonds the electrons are shared ..."

```diff
@@ -5557,7 +5557,9 @@ edges:
       IONIC_MS_P2/COVALENT_MS_P2 (pinned 4ccfc377514a/ed012522d306)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   ambiguity_note: One-directional storage of a symmetric relation (source ionic, target covalent — the
     batch-2 CCW convention); the MS cross-REJECTs are assessment context only, not CCW evidence (G07 admits
     MARK_SCHEME anchors for misconception-family relations only).
```

### 21. `4CH1-CON-IONIC-BOND REQUIRES_PREREQUISITE 4CH1-CON-ION` [high]

- node 4CH1-CON-IONIC-BOND — Ionic bonding (electrostatic attraction between oppositely charged ions) (CONCEPT)
-   spec 4CH1-1.41 [CORE]: understand ionic bonding in terms of electrostatic attractions
- node 4CH1-CON-ION — Ion (formation by electron loss or gain) (CONCEPT)
-   spec 4CH1-1.37 [CORE]: understand how ions are formed by electron loss or gain
- derivation: DEFINITIONAL_DEPENDENCY — Ionic bonding is defined as attraction BETWEEN oppositely charged IONS — the ion is the definitional operand of the bond concept (the batch-2 MOLECULE -> ATOM pattern at the bonding level).
- `NOTE` Ionic bonding and lattices - IGCSE Chemistry Revision Notes.md — "Between positive and negative ions are strong electrostatic forces of attraction which act in all directions"

```diff
@@ -4055,7 +4055,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.41 @ Ionic Bonding and Lattices (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-IONIC-CONDUCTION
```

### 22. `4CH1-CON-IONIC-CONDUCTION REQUIRES_PREREQUISITE 4CH1-CON-ION` [high]

- node 4CH1-CON-IONIC-CONDUCTION — Ionic conduction (solid insulator; molten and aqueous conductor via mobile ions) (CONCEPT)
-   spec 4CH1-1.43 [CORE]: know that ionic compounds do not conduct electricity when solid，but do conduct electricity wh...
-   spec 4CH1-1.56C [CORE]: understand why ionic compounds conduct electricity only when molten or in aqueous solution
- node 4CH1-CON-ION — Ion (formation by electron loss or gain) (CONCEPT)
-   spec 4CH1-1.37 [CORE]: understand how ions are formed by electron loss or gain
- derivation: DEFINITIONAL_DEPENDENCY — The conduction mechanism is stated IN TERMS OF the ions ("the ions are able to move and carry a charge") — the ion is the operand of the conduction explanation in both the 1.43 and 1.56C note sections.
- `NOTE` Ionic bonding and lattices - IGCSE Chemistry Revision Notes.md — "When the ionic compound is melted or dissolved in water, the ions are able to move and carry a charge"

```diff
@@ -4078,7 +4078,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.43 @ Ionic Bonding and Lattices (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-IONIC-CONDUCTION
```

### 23. `4CH1-CON-IONIC-CONDUCTION REQUIRES_PREREQUISITE 4CH1-CON-IONIC-LATTICE` [high]

- node 4CH1-CON-IONIC-CONDUCTION — Ionic conduction (solid insulator; molten and aqueous conductor via mobile ions) (CONCEPT)
-   spec 4CH1-1.43 [CORE]: know that ionic compounds do not conduct electricity when solid，but do conduct electricity wh...
-   spec 4CH1-1.56C [CORE]: understand why ionic compounds conduct electricity only when molten or in aqueous solution
- node 4CH1-CON-IONIC-LATTICE — Giant ionic lattice and why ionic compounds have high melting and boiling points (CONCEPT)
-   spec 4CH1-1.42 [CORE]: understand why compounds with giant ionic lattices have high melting and boiling points
- derivation: DEFINITIONAL_DEPENDENCY — The 1.56C why-only-when-molten explanation is stated IN TERMS OF the lattice ("the ions are in fixed positions in the lattice and are unable to move") — the lattice is the operand of the solid-state half of the conduction story.
- `NOTE` Ionic bonding and lattices - IGCSE Chemistry Revision Notes.md — "The ions are in fixed positions in the lattice"

```diff
@@ -4100,7 +4100,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.43 @ Ionic Bonding and Lattices (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-IONIC-FORMULA
```

### 24. `4CH1-CON-IONIC-FORMULA REQUIRES_PREREQUISITE 4CH1-CON-ION-CHARGE-RULES` [high]

- node 4CH1-CON-IONIC-FORMULA — Writing formulae for ionic compounds (charge cancellation and swap-and-drop) (CONCEPT)
-   spec 4CH1-1.39 [CORE]: write formulae for compounds formed between the ions listed above
- node 4CH1-CON-ION-CHARGE-RULES — Common ion charges (group-based and named-ion table, with the deduction rule) (CONCEPT)
-   spec 4CH1-1.38 [CORE]: know the charges of these ions: •metals in Groups 1,2 and 3 •non-metals in Groups 5,6 and 7 •...
- derivation: DEFINITIONAL_DEPENDENCY — The formula-writing procedure is defined IN TERMS OF the ion charges (the explicit conditional "if you know the charge on the ions") — the charge table is the procedural operand of every method taught in the note (direct comparison and swap-and-drop).
- `NOTE` Formula of ionic compounds - IGCSE Chemistry Revision Notes.md — "The formulae of simple ionic compounds can be determined if you know the charge on the ions"

```diff
@@ -4122,7 +4122,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.39 @ Formula of Ionic Compounds (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-IONIC-LATTICE
```

### 25. `4CH1-CON-IONIC-LATTICE REQUIRES_PREREQUISITE 4CH1-CON-IONIC-BOND` [high]

- node 4CH1-CON-IONIC-LATTICE — Giant ionic lattice and why ionic compounds have high melting and boiling points (CONCEPT)
-   spec 4CH1-1.42 [CORE]: understand why compounds with giant ionic lattices have high melting and boiling points
- node 4CH1-CON-IONIC-BOND — Ionic bonding (electrostatic attraction between oppositely charged ions) (CONCEPT)
-   spec 4CH1-1.41 [CORE]: understand ionic bonding in terms of electrostatic attractions
- derivation: DEFINITIONAL_DEPENDENCY — The lattice is the structure held together BY the ionic bonding ("Between positive and negative ions are strong electrostatic forces of attraction... These are what hold the ionic compound together") — the high-mp/bp explanation of 1.42 is stated in terms of the 1.41 forces (the emitted sentence is the lattice section caption).
- `NOTE` Ionic bonding and lattices - IGCSE Chemistry Revision Notes.md — "There are strong electrostatic forces of attraction between oppositely charged ions in all directions"

```diff
@@ -4146,7 +4146,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.41/1.42 @ Ionic Bonding and Lattices (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-ISOTOPES
```

### 26. `4CH1-CON-METAL-PROPERTIES EXPLAINED_BY 4CH1-CON-METALLIC-BOND` [high]

- node 4CH1-CON-METAL-PROPERTIES — Typical physical properties of metals (electrical conductivity and malleability) and their explanations (CONCEPT)
-   spec 4CH1-1.54C [CORE]: explain typical physical properties of metals, including electrical conductivity and malleabi...
- node 4CH1-CON-METALLIC-BOND — Metallic bonding (positive metal ions and delocalised electrons; the 2-D metallic lattice representation) (CONCEPT)
-   spec 4CH1-1.52C [CORE]: know how to represent a metallic lattice by a 2-D diagram
-   spec 4CH1-1.53C [CORE]: understand metallic bonding in terms of electrostatic attractions
- derivation: SINGLE_SOURCE_CAUSAL_TEACHING — 1.54C is an explicit explain-demand and the note teaches each property with an explicit causal statement — malleability ("This is BECAUSE the atoms/ions are arranged in layers which can slide"), conductivity ("delocalised electrons available to move and carry charge"), high mp/bp ("strong electrostatic forces... need lots of energy") — all operands of the metallic-bonding structure. The EXPLAINED_BY class per the batch-2 GROUP-SIMILARITY pattern (one relation per pair; no prereq edge on this pair).
- `NOTE` Metallic bonding - IGCSE Chemistry Revision Notes.md — "This is because the atoms/ions are arranged in layers which can slide over each other when a force is applied"
- `NOTE` Metallic bonding - IGCSE Chemistry Revision Notes.md — "There are delocalised electrons available to move and carry charge"
- `NOTE` Metallic bonding - IGCSE Chemistry Revision Notes.md — "There are strong electrostatic forces of attraction between the positive metal ions and the negative deloca..."

```diff
@@ -5387,7 +5387,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.54C @ Metallic Bonding (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-MOLAR-GAS-VOL
```

### 27. `4CH1-CON-METALLIC-BOND REQUIRES_PREREQUISITE 4CH1-CON-ION` [high]

- node 4CH1-CON-METALLIC-BOND — Metallic bonding (positive metal ions and delocalised electrons; the 2-D metallic lattice representation) (CONCEPT)
-   spec 4CH1-1.52C [CORE]: know how to represent a metallic lattice by a 2-D diagram
-   spec 4CH1-1.53C [CORE]: understand metallic bonding in terms of electrostatic attractions
- node 4CH1-CON-ION — Ion (formation by electron loss or gain) (CONCEPT)
-   spec 4CH1-1.37 [CORE]: understand how ions are formed by electron loss or gain
- derivation: DEFINITIONAL_DEPENDENCY — Metallic bonding is defined as attraction between positive metal IONS and delocalised electrons — the ion concept is the definitional operand of the 1.53C bond (the note states the atoms-become-ions step as given, presupposing the 1.37 ground).
- `NOTE` Metallic bonding - IGCSE Chemistry Revision Notes.md — "Within the metal lattice, the atoms lose their outer electrons and become positively charged metal ions"

```diff
@@ -4265,7 +4265,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.53C @ Metallic Bonding (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-MIXTURE
```

### 28. `4CH1-CON-SIMPLE-MOLECULAR REQUIRES_PREREQUISITE 4CH1-CON-COVALENT-BOND` [high]

- node 4CH1-CON-SIMPLE-MOLECULAR — Simple molecular structures (weak intermolecular forces; low melting and boiling points; the relative-molecular-mass trend) (CONCEPT)
-   spec 4CH1-1.47 [CORE]: explain why substances with a simple molecular structures are gases or liquids, or solids wit...
-   spec 4CH1-1.48 [CORE]: explain why the melting and boiling points of substances with simple molecular structures inc...
- node 4CH1-CON-COVALENT-BOND — Covalent bond (shared pair of electrons; electrostatic attraction between the shared pair and the nuclei) (CONCEPT)
-   spec 4CH1-1.44 [CORE]: know that a covalent bond is formed between atoms by the sharing of a pair of electrons
-   spec 4CH1-1.45 [CORE]: understand covalent bonds in terms of electrostatic attractions
- derivation: DEFINITIONAL_DEPENDENCY — The simple molecular structure is defined IN TERMS OF covalent bonds joining the atoms (with the intermolecular forces between the molecules as the contrast operand) — the 1.44 bond is the definitional operand of the 1.47 structure.
- `NOTE` Simple molecular structures - IGCSE Chemistry Revision Notes.md — "Simple molecular structures have covalent bonds joining the atoms together, but intermolecular forces that ..."

```diff
@@ -4862,7 +4862,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.47 @ Simple Molecular Structures (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-SIMPLE-MOLECULAR
```

### 29. `4CH1-CON-SIMPLE-MOLECULAR REQUIRES_PREREQUISITE 4CH1-CON-MOLECULE` [high]

- node 4CH1-CON-SIMPLE-MOLECULAR — Simple molecular structures (weak intermolecular forces; low melting and boiling points; the relative-molecular-mass trend) (CONCEPT)
-   spec 4CH1-1.47 [CORE]: explain why substances with a simple molecular structures are gases or liquids, or solids wit...
-   spec 4CH1-1.48 [CORE]: explain why the melting and boiling points of substances with simple molecular structures inc...
- node 4CH1-CON-MOLECULE — Molecule (CONCEPT)
-   spec 4CH1-1.14 [CORE]: know what is meant by the terms atom and molecule
- derivation: DEFINITIONAL_DEPENDENCY — Cross-boundary edge (target = the batch-2 CON-MOLECULE node, sanctioned): "simple MOLECULAR" names molecule-based structures and every explanation sentence in the note is about forces between molecules / molecules increasing in size — the molecule is the definitional operand of the structure class.
- `NOTE` Simple molecular structures - IGCSE Chemistry Revision Notes.md — "intermolecular forces that act between neighbouring molecules are weak"

```diff
@@ -4886,7 +4886,9 @@ edges:
       owned by the batch-2 record (4CH1-1.14)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-SOLUBILITY
```

### 30. `4CH1-MIS-COVALENT-BONDS-BROKEN REMEDIATED_BY 4CH1-CON-SIMPLE-MOLECULAR` [high]

- node 4CH1-MIS-COVALENT-BONDS-BROKEN — Saying covalent bonds are broken when simple molecular substances melt or boil (instead of weak intermolecular forces) (MISCONCEPTION)
- node 4CH1-CON-SIMPLE-MOLECULAR — Simple molecular structures (weak intermolecular forces; low melting and boiling points; the relative-molecular-mass trend) (CONCEPT)
-   spec 4CH1-1.47 [CORE]: explain why substances with a simple molecular structures are gases or liquids, or solids wit...
-   spec 4CH1-1.48 [CORE]: explain why the melting and boiling points of substances with simple molecular structures inc...
- derivation: ASSESSMENT_DOCUMENTED — Remediation target = the WAP target (the B1-E-25 pattern): the corrective content is the IMF-vs-covalent-bond distinction — the note states it as an explicit Remember tip.
- `NOTE` Simple molecular structures - IGCSE Chemistry Revision Notes.md — "it is not the covalent bonds between the atoms which are broken, but the weak intermolecular forces"

```diff
@@ -5840,7 +5840,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.47 @ Simple Molecular Structures (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-MIS-CRYSTALLISATION-DRYNESS
```

### 31. `4CH1-MIS-COVALENT-BONDS-BROKEN WRONG_ANSWER_PATTERN 4CH1-CON-SIMPLE-MOLECULAR` [high]

- node 4CH1-MIS-COVALENT-BONDS-BROKEN — Saying covalent bonds are broken when simple molecular substances melt or boil (instead of weak intermolecular forces) (MISCONCEPTION)
- node 4CH1-CON-SIMPLE-MOLECULAR — Simple molecular structures (weak intermolecular forces; low melting and boiling points; the relative-molecular-mass trend) (CONCEPT)
-   spec 4CH1-1.47 [CORE]: explain why substances with a simple molecular structures are gases or liquids, or solids wit...
-   spec 4CH1-1.48 [CORE]: explain why the melting and boiling points of substances with simple molecular structures inc...
- derivation: ASSESSMENT_DOCUMENTED — The wrong answer manifests in simple-molecular melting/boiling question contexts (the Q1(d) fullerene-vs-diamond comparison rejects bonds-between-molecules answers and caps covalent-bonds-broken mentions) — the pattern corrupts the 1.47 explanation.
- `MARK_SCHEME` COVALENT_MS_P2.txt — "Any reference to bonds between molecules"

```diff
@@ -5654,7 +5654,9 @@ edges:
       sha1 ed012522d306)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-MIS-CRYSTALLISATION-DRYNESS
```

### 32. `4CH1-MIS-GRAPHITE-LAYER-BONDS REMEDIATED_BY 4CH1-CON-DIAMOND-GRAPHITE` [high]

- node 4CH1-MIS-GRAPHITE-LAYER-BONDS — Saying graphite layers are held together by bonds (instead of weak forces of attraction between the layers) (MISCONCEPTION)
- node 4CH1-CON-DIAMOND-GRAPHITE — Structures and properties of diamond, graphite and C60 fullerene (allotropes of carbon) (CONCEPT)
-   spec 4CH1-1.50 [CORE]: explain how the structures of diamond, graphite and C60 fullerene influence their physical pr...
- derivation: ASSESSMENT_DOCUMENTED — Remediation target = the WAP target (the B1-E-25 pattern): the corrective content is the layers-are-held-by-weak-forces-not-bonds statement (the note states it directly in the softness explanation).
- `NOTE` Giant covalent structures - IGCSE Chemistry Revision Notes.md — "The layers are free to slide over each other because there are only weak forces between the layers, not cov..."

```diff
@@ -5937,7 +5937,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.50 @ Giant Covalent Structures (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-MIS-IONIC-BOND-ATOMS
```

### 33. `4CH1-MIS-GRAPHITE-LAYER-BONDS WRONG_ANSWER_PATTERN 4CH1-CON-DIAMOND-GRAPHITE` [high]

- node 4CH1-MIS-GRAPHITE-LAYER-BONDS — Saying graphite layers are held together by bonds (instead of weak forces of attraction between the layers) (MISCONCEPTION)
- node 4CH1-CON-DIAMOND-GRAPHITE — Structures and properties of diamond, graphite and C60 fullerene (allotropes of carbon) (CONCEPT)
-   spec 4CH1-1.50 [CORE]: explain how the structures of diamond, graphite and C60 fullerene influence their physical pr...
- derivation: ASSESSMENT_DOCUMENTED — The wrong answer manifests in graphite-property question contexts (the Q1(b) why-is-graphite-soft question rejects bonds-between-layers answers) — the pattern corrupts the 1.50 graphite explanation.
- `MARK_SCHEME` COVALENT_MS_P2.txt — "Any reference to bonds between layers / molecules"

```diff
@@ -5723,7 +5723,9 @@ edges:
       sha1 ed012522d306)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-MIS-IONIC-BOND-ATOMS
```

### 34. `4CH1-MIS-IONIC-BOND-ATOMS REMEDIATED_BY 4CH1-CON-IONIC-BOND` [high]

- node 4CH1-MIS-IONIC-BOND-ATOMS — Describing ionic bonding as attraction between atoms or molecules (or as intermolecular forces) (MISCONCEPTION)
- node 4CH1-CON-IONIC-BOND — Ionic bonding (electrostatic attraction between oppositely charged ions) (CONCEPT)
-   spec 4CH1-1.41 [CORE]: understand ionic bonding in terms of electrostatic attractions
- derivation: ASSESSMENT_DOCUMENTED — Remediation target = the WAP target (the B1-E-25 pattern): the corrective content is the correct definition — attraction between oppositely charged IONS, not atoms/molecules/IMF.
- `NOTE` Ionic bonding and lattices - IGCSE Chemistry Revision Notes.md — "Between positive and negative ions are strong electrostatic forces of attraction which act in all directions"

```diff
@@ -5959,7 +5959,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.41 @ Ionic Bonding and Lattices (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-MIS-IONIC-CONDUCTION-ELECTRONS
```

### 35. `4CH1-MIS-IONIC-BOND-ATOMS WRONG_ANSWER_PATTERN 4CH1-CON-IONIC-BOND` [high]

- node 4CH1-MIS-IONIC-BOND-ATOMS — Describing ionic bonding as attraction between atoms or molecules (or as intermolecular forces) (MISCONCEPTION)
- node 4CH1-CON-IONIC-BOND — Ionic bonding (electrostatic attraction between oppositely charged ions) (CONCEPT)
-   spec 4CH1-1.41 [CORE]: understand ionic bonding in terms of electrostatic attractions
- derivation: ASSESSMENT_DOCUMENTED — The wrong answer manifests in ionic-bonding question contexts (the Q2(a)(iii) explain-high-mp question zeroes atom/molecule/electron attraction answers; the Q1(a) REJECT column rejects intermolecular forces) — the pattern corrupts the 1.41 concept.
- `MARK_SCHEME` IONIC_MS_P2.txt — "If any reference to attraction between atoms/molecul es/electrons scores 0/3"

```diff
@@ -5745,7 +5745,9 @@ edges:
       sha1 4ccfc377514a)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-MIS-ISOTOPES-DIFFER-PROTONS
```

### 36. `4CH1-MIS-IONIC-CONDUCTION-ELECTRONS MISCONCEPTION_OF 4CH1-CON-IONIC-CONDUCTION` [high]

- node 4CH1-MIS-IONIC-CONDUCTION-ELECTRONS — Believing ionic compounds conduct electricity because electrons move and carry the charge (MISCONCEPTION)
- node 4CH1-CON-IONIC-CONDUCTION — Ionic conduction (solid insulator; molten and aqueous conductor via mobile ions) (CONCEPT)
-   spec 4CH1-1.43 [CORE]: know that ionic compounds do not conduct electricity when solid，but do conduct electricity wh...
-   spec 4CH1-1.56C [CORE]: understand why ionic compounds conduct electricity only when molten or in aqueous solution
- derivation: EXAMINER_TIP_EXPLICIT — The misconception is ABOUT the ionic conduction mechanism (the target concept) — the note documents the wrong carrier (electrons) vs the correct carrier (ions).
- `NOTE` Ionic bonding and lattices - IGCSE Chemistry Revision Notes.md — "A common mistake students make in exams is to say that ionic compounds conduct electricity because 'electro..."

```diff
@@ -5608,7 +5608,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.43 @ Ionic Bonding and Lattices (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-MIS-CONC-UNIT
```

### 37. `4CH1-MIS-IONIC-CONDUCTION-ELECTRONS REMEDIATED_BY 4CH1-CON-IONIC-CONDUCTION` [high]

- node 4CH1-MIS-IONIC-CONDUCTION-ELECTRONS — Believing ionic compounds conduct electricity because electrons move and carry the charge (MISCONCEPTION)
- node 4CH1-CON-IONIC-CONDUCTION — Ionic conduction (solid insulator; molten and aqueous conductor via mobile ions) (CONCEPT)
-   spec 4CH1-1.43 [CORE]: know that ionic compounds do not conduct electricity when solid，but do conduct electricity wh...
-   spec 4CH1-1.56C [CORE]: understand why ionic compounds conduct electricity only when molten or in aqueous solution
- derivation: EXAMINER_TIP_EXPLICIT — Remediation target = the misconception target (the B1-E-25/batch-2 pattern): the corrective content IS the ions-as-carriers conduction statement (plus the metal-electrons/solution-ions contrast tip of the conductivity note, quoted in the node remediation_evidence).
- `NOTE` Ionic bonding and lattices - IGCSE Chemistry Revision Notes.md — "When the ionic compound is melted or dissolved in water, the ions are able to move and carry a charge"

```diff
@@ -5982,7 +5982,9 @@ edges:
     upstream: T-C10 HUMAN_VALIDATED 4CH1-1.43 @ Ionic Bonding and Lattices (2026-09-11)
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-MIS-ISOTOPES-DIFFER-PROTONS
```

### 38. `4CH1-PR-04 REQUIRES_PREREQUISITE 4CH1-CON-AQUEOUS-DISCHARGE` [high]

- node 4CH1-CON-AQUEOUS-DISCHARGE — Selective discharge in aqueous electrolysis (halide preference at the anode; hydrogen vs metal at the cathode) (CONCEPT)
-   spec 4CH1-1.58C [CORE]: describe experiments to investigate electrolysis, using inert electrodes, of molten compounds...
- derivation: USED_WITHOUT_RETEACHING — The practical conclusions are the discharge-rule outcomes for the three named solutions (hydrogen not sodium at the cathode of NaCl; copper at the cathode of CuSO4) — the practical note demonstrates the rules without re-teaching them (the PR-02 -> CON-RF-VALUE pattern).
- `NOTE` Practical Investigate the Electrolysis of Aqueous Solutions  Edexcel IGCSE Chemistry Revision Notes 2017.md — "Sodium chloride solutions produces hydrogen at the cathode and chlorine at the anode"

```diff
@@ -5205,7 +5205,9 @@ edges:
       Solutions (2026-09-11)'
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-PR-04
```

### 39. `4CH1-PR-04 REQUIRES_PREREQUISITE 4CH1-CON-ELECTROLYSIS` [high]

- node 4CH1-CON-ELECTROLYSIS — Electrolysis (decomposition by direct current: molten binary compounds and their element products, using inert electrodes) (CONCEPT)
-   spec 4CH1-1.58C [CORE]: describe experiments to investigate electrolysis, using inert electrodes, of molten compounds...
- derivation: USED_WITHOUT_RETEACHING — The 1.60C practical is an investigation OF electrolysis (its Aim sentence) — the process concept is the practical ground (the batch-2 PR-02 -> CON-CHROMATOGRAPHY pattern).
- `NOTE` Practical Investigate the Electrolysis of Aqueous Solutions  Edexcel IGCSE Chemistry Revision Notes 2017.md — "To electrolyse aqueous solutions of sodium chloride, sulfuric acid and copper(II)sulfate, and to collect an..."

```diff
@@ -5228,7 +5228,9 @@ edges:
       Solutions (2026-09-11)'
     generated_date: '2026-09-12'
   confidence: high
-  validation_status: SUGGESTED
+  validation_status: HUMAN_VALIDATED
+  validated_by: operator
+  validated_date: '2026-09-13'
   version: 1
   created_at: '2026-09-12'
 - source: 4CH1-CON-CRYSTALLISATION
```

## File-level meta hunks (once, for the whole batch)

```diff
@@ -112,8 +112,10 @@ meta:
     remediated_by_edges: 10
     requires_prerequisite_edges: 91
     wrong_answer_pattern_edges: 8
-    promoted_edges: 79
-    human_validated_edges: 79
+    promoted_edges: 118
+    human_validated_edges: 118
   promotion_record: scripts/c11_promotions.yaml
 edges:
 - source: 4CH1-CON-ANODE-CATHODE
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
| `4CH1-CON-ANODE-CATHODE` | Anions and cations (negative and positive ions) and their migration to cathode and anode | CONCEPT | 4CH1-1.57C (CORE) | high |
| `4CH1-CON-AQUEOUS-DISCHARGE` | Selective discharge in aqueous electrolysis (halide preference at the anode; hydrogen vs metal at the cathode) | CONCEPT | 4CH1-1.58C (CORE) | high |
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
| `4CH1-CON-COVALENT-BOND` | Covalent bond (shared pair of electrons; electrostatic attraction between the shared pair and the nuclei) | CONCEPT | 4CH1-1.44 (CORE); 4CH1-1.45 (CORE) | high |
| `4CH1-CON-COVALENT-CONDUCTION` | Covalent compounds do not conduct electricity (no freely moving charged particles) | CONCEPT | 4CH1-1.51 (CORE); 4CH1-1.55C (CORE) | high |
| `4CH1-CON-CRYSTALLISATION` | Crystallisation | CONCEPT | 4CH1-1.10 (CORE) | high |
| `4CH1-CON-DIAMOND-GRAPHITE` | Structures and properties of diamond, graphite and C60 fullerene (allotropes of carbon) | CONCEPT | 4CH1-1.50 (CORE) | high |
| `4CH1-CON-DIFFUSION` | Diffusion in gases and liquids | CONCEPT | 4CH1-1.3 (CORE) | high |
| `4CH1-CON-DILUTION` | Dilution of coloured solutions | CONCEPT | 4CH1-1.3 (CORE) | high |
| `4CH1-CON-DOT-CROSS-COVALENT` | Dot-and-cross diagrams for covalent substances (diatomic, inorganic and organic molecules) | CONCEPT | 4CH1-1.46 (CORE) | high |
| `4CH1-CON-DOT-CROSS-IONIC` | Dot-and-cross diagrams for ionic compounds (electron transfer) | CONCEPT | 4CH1-1.40 (CORE) | high |
| `4CH1-CON-ELECTRODE-HALF-EQUATIONS` | Ionic half-equations for the electrode reactions during electrolysis | CONCEPT | 4CH1-1.59C (CORE) | high |
| `4CH1-CON-ELECTROLYSIS` | Electrolysis (decomposition by direct current: molten binary compounds and their element products, using inert electrodes) | CONCEPT | 4CH1-1.58C (CORE) | high |
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
| `4CH1-CON-GIANT-COVALENT` | Giant covalent structures (solids with high melting and boiling points) | CONCEPT | 4CH1-1.49 (CORE) | high |
| `4CH1-CON-GROUP-SIMILARITY` | Why elements in the same group have similar chemical properties | CONCEPT | 4CH1-1.23 (CORE) | high |
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
| `4CH1-CON-REDOX-ELECTRONS` | Oxidation and reduction in terms of electron loss and gain | CONCEPT | 4CH1-1.59C (CORE) | high |
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
| `4CH1-MIS-CONC-UNIT` | Failing to convert cm3 to dm3 in concentration calculations | MISCONCEPTION |  | high |
| `4CH1-MIS-COVALENT-BONDS-BROKEN` | Saying covalent bonds are broken when simple molecular substances melt or boil (instead of weak intermolecular forces) | MISCONCEPTION |  | high |
| `4CH1-MIS-CRYSTALLISATION-DRYNESS` | Obtaining crystals by evaporating to dryness | MISCONCEPTION |  | high |
| `4CH1-MIS-EQ-SUBSCRIPT` | Balancing equations by altering subscripts | MISCONCEPTION |  | high |
| `4CH1-MIS-GAS-PARTICLES-TOUCH` | Drawing gas particles touching each other or joined by bonds | MISCONCEPTION |  | high |
| `4CH1-MIS-GRAPHITE-LAYER-BONDS` | Saying graphite layers are held together by bonds (instead of weak forces of attraction between the layers) | MISCONCEPTION |  | high |
| `4CH1-MIS-IONIC-BOND-ATOMS` | Describing ionic bonding as attraction between atoms or molecules (or as intermolecular forces) | MISCONCEPTION |  | high |
| `4CH1-MIS-IONIC-CONDUCTION-ELECTRONS` | Believing ionic compounds conduct electricity because electrons move and carry the charge | MISCONCEPTION |  | high |
| `4CH1-MIS-ISOTOPES-DIFFER-PROTONS` | Believing isotopes of an element differ in their number of protons | MISCONCEPTION |  | high |
| `4CH1-MIS-RAM-MASS-NUMBER` | Calling the Periodic Table relative atomic mass the mass number | MISCONCEPTION |  | high |

