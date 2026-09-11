<!-- c10-ratify-audit-2026-09-11 -->
# T-C10 — Pre-Ratification Reconciliation Audit (2026-09-11) — **PASS**

Read-only audit executing the operator-advisor's condition (round 3, re-targeted after round 4) before the staged §12 batch: generator `scripts/c10_ratify_audit.py` (machine record: `C10_RATIFICATION_AUDIT.json`).

| # | check | status | detail |
|---|---|---|---|
| C1 | review record: 61 round-3 pairs, 2 round-4 REJECTs -> 59 distinct CONFIRM pairs | **PASS** | 59 CONFIRM pairs; superseded: 2 (== R4.ROUND4_REJECTS); verdicts scanned: 33 + 1 P4 + 21 P6a + 7 P6b |
| C1b | round-4 REJECTs well-formed and REMOVED from the store (both notes keep >= 1 mapping) | **PASS** | Calculate Relative Mass  Edexcel IGCSE Chemistry Revision Notes 2017 keeps ['4CH1-1.26']; Nitrogen Oxides & Sulfur Dioxide  Edexcel IGCSE Chemistry Revision Not |
| C2 | sheet §12 stages exactly 59 distinct --map specs | **PASS** | 59 specs, 59 distinct; --by 'operator' --date '2026-09-11' |
| C3 | production resolver resolves all 59 specs unambiguously (no code-wide promotion) | **PASS** | 29 bare CODE specs (each code on exactly one note), 30 CODE@FRAGMENT specs; 59 distinct (code, note) targets |
| C4a | every surviving reviewed pair is staged by the command (completeness) | **PASS** | 59/59 staged |
| C4b | every staged target is a reviewed pair (no unreviewed promotion) | **PASS** | 59/59 reviewed |
| C4c | no round-4 REJECTed pair is staged (both live outside the batch) | **PASS** | staged ∩ rejected = ∅ |
| C5 | pre-state: 0 promoted / all 209 SUGGESTED — batch = exactly 59 promotions, 0 no-ops | **PASS** | promoted on disk: 0; all 59 targets in SUGGESTED state: True |
| C6 | store shape: 112 notes / 209 mappings / 176 high / 32 medium / 1 low | **PASS** | 112 notes / 209 mappings / {'high': 176, 'medium': 32, 'low': 1} |
| C7 | corpus stat: 68/112 notes carry 2+ codes (contributory many-to-many is the corpus shape) | **PASS** | 68/112 |
| C8 | VLM archive: 21 verdict JSONs with codes matching the P6a queue exactly | **PASS** | 21 files; sym-diff: none |
| C9 | git provenance: HEAD 49a0478… (round-4 rework commit), tree clean | **PASS** | HEAD 49a0478, tree clean |

## The 59 exact ratification identities

Every pair below is an AI-reviewed CONFIRM that survived the round-4 supersession (review record: `scripts/c10_pr_review_verdicts.py` + `scripts/c10_round4_rejects.py`, rendered in PHASE2_PR_REVIEW_SHEET.md §2–§8 + §12) and resolves, via the production `c10_promote.py` resolver, to exactly the staged §12 spec:

| # | code | note (stem) | queue | confidence |
|---:|---|---|---|---|
| 1 | 4CH1-1.10 | Paper chromatography - IGCSE Chemistry Revision Notes | P1/P2/P5/P3 | medium |
| 2 | 4CH1-1.11 | Interpreting chromatograms - IGCSE Chemistry Revision Notes | P6b missing figures | high |
| 3 | 4CH1-1.12 | Interpreting chromatograms - IGCSE Chemistry Revision Notes | P6b missing figures | high |
| 4 | 4CH1-1.16 | Atoms Definitions & Structure  Edexcel IGCSE Chemistry Revision Notes 2017 | P1/P2/P5/P3 | medium |
| 5 | 4CH1-1.16 | Relative atomic mass - IGCSE Chemistry Revision Notes | P1/P2/P5/P3 | medium |
| 6 | 4CH1-1.17 | Relative atomic mass - IGCSE Chemistry Revision Notes | P4 S1-c high | high |
| 7 | 4CH1-1.22 | Electronic Configuration & Reactivity  Edexcel IGCSE Chemistry Revision Notes 2017 | P1/P2/P5/P3 | medium |
| 8 | 4CH1-1.25 | Reacting mass calculations - IGCSE Chemistry Revision Notes | P1/P2/P5/P3 | medium |
| 9 | 4CH1-1.28 | Reacting mass calculations - IGCSE Chemistry Revision Notes | P1/P2/P5/P3 | medium |
| 10 | 4CH1-1.31 | Empirical & Molecular Formulae  Edexcel IGCSE Chemistry Revision Notes 2017 | P1/P2/P5/P3 | medium |
| 11 | 4CH1-1.33 | Investigating metal oxide formulas - IGCSE Revision Notes | P1/P2/P5/P3 | medium |
| 12 | 4CH1-1.33 | Simple compound formulae - IGCSE Chemistry Revision Notes | P1/P2/P5/P3 | medium |
| 13 | 4CH1-1.37 | Common Ions  Edexcel IGCSE Chemistry Revision Notes 2017 | P1/P2/P5/P3 | medium |
| 14 | 4CH1-1.37 | Ionic bonding diagrams - IGCSE Chemistry Revision Notes | P1/P2/P5/P3 | medium |
| 15 | 4CH1-1.39 | Formula of ionic compounds - IGCSE Chemistry Revision Notes | P6b missing figures | high |
| 16 | 4CH1-1.4 | Solubility - IGCSE Chemistry Revision Notes | P1/P2/P5/P3 | low |
| 17 | 4CH1-1.41 | Ionic bonding and lattices - IGCSE Chemistry Revision Notes | P6a diagram queue | high |
| 18 | 4CH1-1.50 | Simple molecular structures - IGCSE Chemistry Revision Notes | P1/P2/P5/P3 | medium |
| 19 | 4CH1-1.51 | Simple molecular structures - IGCSE Chemistry Revision Notes | P1/P2/P5/P3 | medium |
| 20 | 4CH1-1.52C | Metallic bonding - IGCSE Chemistry Revision Notes | P1/P2/P5/P3 | medium |
| 21 | 4CH1-1.56C | Electrolysis diagram - IGCSE Chemistry Revision Notes | P1/P2/P5/P3 | medium |
| 22 | 4CH1-1.58C | Practical Investigate the Electrolysis of Aqueous Solutions  Edexcel IGCSE Chemistry Revision Notes 2017 | P1/P2/P5/P3 | medium |
| 23 | 4CH1-1.5C | Investigating solubility - IGCSE Chemistry Revision Notes | P1/P2/P5/P3 | medium |
| 24 | 4CH1-1.60C | Practical Investigate the Electrolysis of Aqueous Solutions  Edexcel IGCSE Chemistry Revision Notes 2017 | P6a diagram queue | high |
| 25 | 4CH1-1.8 | Pure substances - IGCSE Chemistry Revision Notes | P1/P2/P5/P3 | medium |
| 26 | 4CH1-2.10 | Oxygen percentage in air - IGCSE Chemistry Revision Notes | P1/P2/P5/P3 | medium |
| 27 | 4CH1-2.15 | Metals reacting with acids - IGCSE Chemistry Revision Notes | P1/P2/P5/P3 | medium |
| 28 | 4CH1-2.17 | Metals Reacting with Water & Acids  Edexcel IGCSE Chemistry Revision Notes 2017 | P1/P2/P5/P3 | medium |
| 29 | 4CH1-2.21 | Metals reacting with acids - IGCSE Chemistry Revision Notes | P6a diagram queue | high |
| 30 | 4CH1-2.24C | Extraction of metals from ores - IGCSE Chemistry | P1/P2/P5/P3 | medium |
| 31 | 4CH1-2.26C | Alloys - IGCSE Chemistry Revision Notes | P6a diagram queue | high |
| 32 | 4CH1-2.29 | Acids, Alkalis & Neutralisation - IGCSE Revision Notes | P1/P2/P5/P3 | medium |
| 33 | 4CH1-2.33C | Acid-Alkali Titrations  Edexcel IGCSE Chemistry Revision Notes 2017 | P6a diagram queue | high |
| 34 | 4CH1-2.39 | Preparing copper sulfate - IGCSE Chemistry Revision Notes | P1/P2/P5/P3 | medium |
| 35 | 4CH1-2.41C | Preparing lead sulfate - IGCSE Chemistry Revision Notes | P1/P2/P5/P3 | medium |
| 36 | 4CH1-2.5 | Group 7 properties - IGCSE Chemistry Revision Notes | P6a diagram queue | high |
| 37 | 4CH1-2.9 | Composition of air - IGCSE Chemistry Revision Notes | P6a diagram queue | high |
| 38 | 4CH1-3.10 | Explaining Rates  Edexcel IGCSE Chemistry Revision Notes 2017 | P1/P2/P5/P3 | medium |
| 39 | 4CH1-3.19C | Dynamic equilibrium - IGCSE Chemistry Revision Notes | P6a diagram queue | high |
| 40 | 4CH1-3.2 | Calorimetry - IGCSE Chemistry Revision Notes | P6a diagram queue | high |
| 41 | 4CH1-3.2 | Temperature change practical - IGCSE Revision Notes | P1/P2/P5/P3 | medium |
| 42 | 4CH1-3.21C | The position of equilibrium - IGCSE Chemistry Revision Notes | P6a diagram queue | high |
| 43 | 4CH1-3.9 | How surface area affects rate - IGCSE Revision Notes | P1/P2/P5/P3 | medium |
| 44 | 4CH1-3.9 | Investigating catalysts - IGCSE Chemistry Revision Notes | P1/P2/P5/P3 | medium |
| 45 | 4CH1-4.10 | Fractional distillation - IGCSE Chemistry Revision Notes | P6b missing figures | high |
| 46 | 4CH1-4.2 | Introduction to Organic Chemistry - IGCSE Revision Notes | P6a diagram queue | high |
| 47 | 4CH1-4.21 | Alkanes  Edexcel IGCSE Chemistry Revision Notes 2017 | P6a diagram queue | high |
| 48 | 4CH1-4.29C | Alcohols  Edexcel IGCSE Chemistry Revision Notes 2017 | P6a diagram queue | high |
| 49 | 4CH1-4.30C | Alcohols  Edexcel IGCSE Chemistry Revision Notes 2017 | P6a diagram queue | high |
| 50 | 4CH1-4.34C | Carboxylic Acids  Edexcel IGCSE Chemistry Revision Notes 2017 | P6a diagram queue | high |
| 51 | 4CH1-4.35C | Carboxylic Acids  Edexcel IGCSE Chemistry Revision Notes 2017 | P6a diagram queue | high |
| 52 | 4CH1-4.38C | Making and naming esters - IGCSE Chemistry Revision Notes | P6a diagram queue | high |
| 53 | 4CH1-4.39C | Preparation of ethyl ethanoate - IGCSE Chemistry | P1/P2/P5/P3 | medium |
| 54 | 4CH1-4.40C | Making and naming esters - IGCSE Chemistry Revision Notes | P1/P2/P5/P3 | medium |
| 55 | 4CH1-4.44 | Addition Polymers  Edexcel IGCSE Chemistry Revision Notes 2017 | P6a diagram queue | high |
| 56 | 4CH1-4.5 | Introduction to Organic Chemistry - IGCSE Revision Notes | P1/P2/P5/P3 | medium |
| 57 | 4CH1-4.7 | Fractional distillation - IGCSE Chemistry Revision Notes | P6b missing figures | high |
| 58 | 4CH1-4.8 | Fractional distillation - IGCSE Chemistry Revision Notes | P6b missing figures | high |
| 59 | 4CH1-4.9 | Fractional distillation - IGCSE Chemistry Revision Notes | P6b missing figures | high |

## The 2 round-4 rejections (proven outside the batch)

| code | note (stem) | verdict | disposition |
|---|---|---|---|
| 4CH1-4.15 | Nitrogen Oxides & Sulfur Dioxide  Edexcel IGCSE Chemistry Revision Notes 2017 | **REJECT (round 4, 2026-09-11)** | removed from decisions S4.json (note keeps 4.14 / 4.16); 4.15 -> zero-coverage corpus gap, annotated in PHASE2_MAPPING_C |
| 4CH1-1.17 | Calculate Relative Mass  Edexcel IGCSE Chemistry Revision Notes 2017 | **REJECT (round 4, 2026-09-11)** | removed from decisions S1.json (note keeps 1.26); 1.17 remains covered by its high-confidence in-subsection S1-c mapping |

The staged 59-spec c10_promote.py batch in PHASE2_PR_REVIEW_SHEET.md §12 promotes exactly the 59 round-4-surviving AI-reviewed CONFIRM mappings — exact (note, code) identity proven, zero unreviewed or code-wide promotions, zero ambiguity, both round-4 REJECTs proven removed from the store and absent from the command, store pre-state 0 promoted / 209 SUGGESTED. The operator may execute the §12 batch as staged.

Provenance: repo HEAD `49a0478` (the round-4 rework commit, carrying the two removals and the green gates); tree clean before this audit's report files.

After the operator runs the §12 command, those 59 mappings become HUMAN_VALIDATED (validated_by `operator`) — a distinct state from this AI CONFIRM, per the provenance chain. The 150 mappings outside the reviewed set remain SUGGESTED (risk-tiered validation state, guide §7), and 4CH1-4.15 remains an honest zero-coverage corpus gap (T-C11 input).
