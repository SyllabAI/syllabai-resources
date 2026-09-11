<!-- c10-ratify-audit-2026-09-11 -->
# T-C10 — Ratification Reconciliation Audit (2026-09-11, phase: pre) — **PASS**

Read-only audit executing the operator-advisor's condition (rounds 3-5) over BOTH staged batches — §12 (59-spec, round-4 survivors) and §13 (150-spec, round-5 CONFIRMs, staged from `C10_ROUND5_REVIEW.json`); generator `scripts/c10_ratify_audit.py` (machine record: `C10_RATIFICATION_AUDIT.json`). Operator instruction: "Ratify the 59 and promote 150" (2026-09-11).

| # | check | status | detail |
|---|---|---|---|
| C1 | review record: 61 round-3 pairs, 2 round-4 REJECTs -> 59 distinct CONFIRM pairs | **PASS** | 59 CONFIRM pairs; superseded: 2 (== R4.ROUND4_REJECTS); verdicts scanned: 33 + 1 P4 + 21 P6a + 7 P6b |
| C1b | round-4 REJECTs well-formed and REMOVED from the store (both notes keep >= 1 mapping) | **PASS** | Nitrogen Oxides & Sulfur Dioxide  Edexcel IGCSE Chemistry Revision Notes 2017 keeps ['4CH1-4.14', '4CH1-4.16']; Calculate Relative Mass  Edexcel IGCSE Chemistry |
| C1c | round-5 record: 150 pairs, idx 1..150, all CONFIRM, distinct, all in store by exact identity; pre-review SHA c6454c9 an ancestor of HEAD | **PASS** | 150 pairs (150); distinct True; in-store True; pre-review ancestor True; 2 corrections referenced |
| C2 | sheet §12 stages exactly 59 distinct --map specs | **PASS** | 59 specs, 59 distinct; --by 'operator' --date '2026-09-11' |
| C2b | sheet §13 stages exactly 150 distinct --map specs | **PASS** | 150 specs, 150 distinct; --by 'operator' --date '2026-09-11' |
| C3 | production resolver resolves all 59 specs unambiguously (no code-wide promotion) | **PASS** | 29 bare CODE specs (each code on exactly one note), 30 CODE@FRAGMENT specs; 59 distinct (code, note) targets |
| C3b | production resolver resolves all 150 specs unambiguously (bare CODE only where the code lives on exactly one note) | **PASS** | 127 bare CODE specs, 23 CODE@FRAGMENT specs; 150 distinct (code, note) targets |
| C4a | every surviving reviewed pair is staged by §12 (completeness) | **PASS** | 59/59 staged |
| C4b | every §12 staged target is a reviewed pair (no unreviewed promotion) | **PASS** | 59/59 reviewed |
| C4c | no round-4 REJECTed pair is staged (both live outside the batch) | **PASS** | staged ∩ rejected = ∅ |
| C4d | §13 staged pairs == exactly the 150 round-5 CONFIRM pairs (bijection) | **PASS** | 150/150 round-5 pairs staged |
| C4e | §12 ∩ §13 = ∅ and §12 ∪ §13 = the whole 209-mapping store (each mapping staged exactly once) | **PASS** | union 209/209; overlap 0 |
| C5 | pre-state: 0 promoted / all 209 SUGGESTED — the batches are exactly 209 promotions, 0 no-ops | **PASS** | promoted on disk: 0; all 209 targets in SUGGESTED state: True |
| C6 | store shape: 112 notes / 209 mappings / 176 high / 32 medium / 1 low | **PASS** | 112 notes / 209 mappings / {'high': 176, 'medium': 32, 'low': 1} |
| C7 | corpus stat: 68/112 notes carry 2+ codes (contributory many-to-many is the corpus shape) | **PASS** | 68/112 |
| C8 | VLM archive: 29 verdict JSONs (21 round-3/4 + 8 round-5) with codes matching the P6a queue and the round-5 set exactly | **PASS** | 29 files; sym-diff: none |
| C9 | git provenance: HEAD descends from the pushed round-5 state c90f5ae, tree clean apart from this change-set | **PASS** | HEAD 0db00e8; dirty-foreign: none |

## The 59 §12 ratification identities (round-4 survivors)

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

## The 150 §13 ratification identities (round-5 CONFIRMs)

Every pair below is a round-5 exhaustive-review CONFIRM (150 CONFIRM / 0 REJECT / 0 HOLD, frozen guide §0.0 + §8 contract; row-level detail with evidence, spec wording and findings: `PHASE2_ROUND5_REVIEW_SHEET.md` §4 / `C10_ROUND5_REVIEW.json`):

| # | code | note (stem) | confidence |
|---:|---|---|---|
| 1 | 4CH1-1.1 | Changing states of matter - IGCSE Chemistry Revision Notes | high |
| 2 | 4CH1-1.2 | Changing states of matter - IGCSE Chemistry Revision Notes | high |
| 3 | 4CH1-1.3 | Diffusion - IGCSE Chemistry Revision Notes | high |
| 4 | 4CH1-1.7C | Investigating solubility - IGCSE Chemistry Revision Notes | high |
| 5 | 4CH1-1.5C | Solubility - IGCSE Chemistry Revision Notes | high |
| 6 | 4CH1-1.6C | Solubility - IGCSE Chemistry Revision Notes | high |
| 7 | 4CH1-1.4 | Solutions - IGCSE Chemistry Revision Notes | high |
| 8 | 4CH1-1.8 | Element, Compound or Mixture  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 9 | 4CH1-1.13 | Paper chromatography - IGCSE Chemistry Revision Notes | high |
| 10 | 4CH1-1.9 | Pure substances - IGCSE Chemistry Revision Notes | high |
| 11 | 4CH1-1.10 | Separation techniques - IGCSE Chemistry Revision Notes | high |
| 12 | 4CH1-1.14 | Atoms Definitions & Structure  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 13 | 4CH1-1.15 | Atoms Definitions & Structure  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 14 | 4CH1-1.23 | Electronic Configuration & Reactivity  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 15 | 4CH1-1.24 | Electronic Configuration & Reactivity  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 16 | 4CH1-1.19 | Electronic Configurations  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 17 | 4CH1-1.22 | Electronic Configurations  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 18 | 4CH1-1.20 | Metals & non-metals in the Periodic Table - IGCSE Chemistry | high |
| 19 | 4CH1-1.21 | Metals & non-metals in the Periodic Table - IGCSE Chemistry | high |
| 20 | 4CH1-1.18 | Periodic Table Basics  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 21 | 4CH1-1.35C | Calculate Gas Volumes - IGCSE Chemistry Revision Notes | high |
| 22 | 4CH1-1.26 | Calculate Relative Mass  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 23 | 4CH1-1.30 | Calculate percentage yield - IGCSE Chemistry Revision Notes | high |
| 24 | 4CH1-1.27 | Calculating moles and mass - IGCSE Chemistry Revision Notes | high |
| 25 | 4CH1-1.28 | Calculating moles and mass - IGCSE Chemistry Revision Notes | high |
| 26 | 4CH1-1.32 | Empirical & Molecular Formulae  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 27 | 4CH1-1.33 | Empirical & Molecular Formulae  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 28 | 4CH1-1.36 | Investigating metal oxide formulas - IGCSE Revision Notes | high |
| 29 | 4CH1-1.31 | Investigating metal oxide formulas - IGCSE Revision Notes | high |
| 30 | 4CH1-1.29 | Reacting mass calculations - IGCSE Chemistry Revision Notes | high |
| 31 | 4CH1-1.31 | Simple compound formulae - IGCSE Chemistry Revision Notes | high |
| 32 | 4CH1-1.34C | Solution concentration - IGCSE Chemistry Revision Notes | high |
| 33 | 4CH1-1.25 | Writing chemical equations - IGCSE Chemistry Revision Notes | high |
| 34 | 4CH1-1.38 | Common Ions  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 35 | 4CH1-1.37 | Formation of ions - IGCSE Chemistry Revision Notes | high |
| 36 | 4CH1-1.42 | Ionic bonding and lattices - IGCSE Chemistry Revision Notes | high |
| 37 | 4CH1-1.43 | Ionic bonding and lattices - IGCSE Chemistry Revision Notes | high |
| 38 | 4CH1-1.40 | Ionic bonding diagrams - IGCSE Chemistry Revision Notes | high |
| 39 | 4CH1-1.46 | Covalent Bonds Dot & Cross Diagrams  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 40 | 4CH1-1.44 | Forming covalent bonds - IGCSE Chemistry Revision Notes | high |
| 41 | 4CH1-1.45 | Forming covalent bonds - IGCSE Chemistry Revision Notes | high |
| 42 | 4CH1-1.49 | Giant covalent structures - IGCSE Chemistry Revision Notes | high |
| 43 | 4CH1-1.50 | Giant covalent structures - IGCSE Chemistry Revision Notes | high |
| 44 | 4CH1-1.47 | Simple molecular structures - IGCSE Chemistry Revision Notes | high |
| 45 | 4CH1-1.48 | Simple molecular structures - IGCSE Chemistry Revision Notes | high |
| 46 | 4CH1-1.53C | Metallic bonding - IGCSE Chemistry Revision Notes | high |
| 47 | 4CH1-1.54C | Metallic bonding - IGCSE Chemistry Revision Notes | high |
| 48 | 4CH1-1.58C | Electrolysis diagram - IGCSE Chemistry Revision Notes | high |
| 49 | 4CH1-1.55C | Electronic conductivity - IGCSE Chemistry Revision Notes | high |
| 50 | 4CH1-1.56C | Electronic conductivity - IGCSE Chemistry Revision Notes | high |
| 51 | 4CH1-1.57C | Electronic conductivity - IGCSE Chemistry Revision Notes | high |
| 52 | 4CH1-1.59C | Half equations - IGCSE Chemistry Revision Notes | high |
| 53 | 4CH1-2.4C | Group 1 Reactivity & Electronic Configurations  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 54 | 4CH1-2.1 | Group 1 reactivity & trends - IGCSE Chemistry Revision Notes | high |
| 55 | 4CH1-2.2 | Group 1 reactivity & trends - IGCSE Chemistry Revision Notes | high |
| 56 | 4CH1-2.3 | Group 1 reactivity & trends - IGCSE Chemistry Revision Notes | high |
| 57 | 4CH1-2.6 | Group 7 properties - IGCSE Chemistry Revision Notes | high |
| 58 | 4CH1-2.7 | Group 7 properties - IGCSE Chemistry Revision Notes | high |
| 59 | 4CH1-2.8C | Group 7 reactivity - IGCSE Chemistry Revision Notes | high |
| 60 | 4CH1-2.11 | Combustion  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 61 | 4CH1-2.10 | Composition of air - IGCSE Chemistry Revision Notes | high |
| 62 | 4CH1-2.13 | Greenhouse effect - IGCSE Chemistry Revision Notes | high |
| 63 | 4CH1-2.14 | Oxygen percentage in air - IGCSE Chemistry Revision Notes | high |
| 64 | 4CH1-2.12 | Thermal decomposition - IGCSE Chemistry Revision Notes | high |
| 65 | 4CH1-2.16 | Metal displacement - IGCSE Chemistry Revision Notes | high |
| 66 | 4CH1-2.15 | Metals Reacting with Water & Acids  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 67 | 4CH1-2.20 | Oxidation and reduction - IGCSE Chemistry Revision Notes | high |
| 68 | 4CH1-2.18 | Rusting of iron - IGCSE Chemistry Revision Notes | high |
| 69 | 4CH1-2.19 | Rusting of iron - IGCSE Chemistry Revision Notes | high |
| 70 | 4CH1-2.17 | The reactivity series - IGCSE Chemistry Revision Notes | high |
| 71 | 4CH1-2.27C | Alloys - IGCSE Chemistry Revision Notes | high |
| 72 | 4CH1-2.23C | Extraction of metals from ores - IGCSE Chemistry | high |
| 73 | 4CH1-2.25C | Metals and their uses - IGCSE Chemistry Revision Notes | high |
| 74 | 4CH1-2.22C | Where does metal come from - IGCSE Chemistry Revision Notes | high |
| 75 | 4CH1-2.31 | Acids, Alkalis & Neutralisation - IGCSE Revision Notes | high |
| 76 | 4CH1-2.32 | Acids, Alkalis & Neutralisation - IGCSE Revision Notes | high |
| 77 | 4CH1-2.28 | What is an indicator - IGCSE Chemistry Revision Notes | high |
| 78 | 4CH1-2.30 | What is an indicator - IGCSE Chemistry Revision Notes | high |
| 79 | 4CH1-2.29 | What is an indicator - IGCSE Chemistry Revision Notes | high |
| 80 | 4CH1-2.38 | Bases and alkalis - IGCSE Chemistry Revision Notes | high |
| 81 | 4CH1-2.39 | Making soluble salts - IGCSE Chemistry Revision Notes | high |
| 82 | 4CH1-2.40C | Prepare a Soluble Salt II  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 83 | 4CH1-2.41C | Prepare an Insoluble Salt  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 84 | 4CH1-2.42 | Preparing copper sulfate - IGCSE Chemistry Revision Notes | high |
| 85 | 4CH1-2.43C | Preparing lead sulfate - IGCSE Chemistry Revision Notes | high |
| 86 | 4CH1-2.37 | Reactions of acids - IGCSE Chemistry Revision Notes | high |
| 87 | 4CH1-2.34 | Solubility Rules  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 88 | 4CH1-2.35 | What are acids and bases - IGCSE Chemistry Revision Notes | high |
| 89 | 4CH1-2.36 | What are acids and bases - IGCSE Chemistry Revision Notes | high |
| 90 | 4CH1-2.49 | Chemical test for water - IGCSE Chemistry Revision Notes | high |
| 91 | 4CH1-2.50 | Chemical test for water - IGCSE Chemistry Revision Notes | high |
| 92 | 4CH1-2.45 | Flame tests - IGCSE Chemistry Revision Notes | high |
| 93 | 4CH1-2.46 | Flame tests - IGCSE Chemistry Revision Notes | high |
| 94 | 4CH1-2.44 | Gas tests - IGCSE Chemistry Revision Notes | high |
| 95 | 4CH1-2.48 | Tests for Anions  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 96 | 4CH1-2.47 | Tests for cations - IGCSE Chemistry Revision Notes | high |
| 97 | 4CH1-3.3 | Energetics calculations in chemistry - IGCSE Revision Notes | high |
| 98 | 4CH1-3.4 | Energetics calculations in chemistry - IGCSE Revision Notes | high |
| 99 | 4CH1-3.5C | Energy level diagrams - IGCSE Chemistry Revision Notes | high |
| 100 | 4CH1-3.1 | Exothermic and endothermic - IGCSE Chemistry Revision Notes | high |
| 101 | 4CH1-3.8 | Temperature change practical - IGCSE Revision Notes | high |
| 102 | 4CH1-3.6C | What is bond energy - IGCSE Chemistry Revision Notes | high |
| 103 | 4CH1-3.7C | What is bond energy - IGCSE Chemistry Revision Notes | high |
| 104 | 4CH1-3.12 | Catalysts in Chemistry - IGCSE Chemistry Revision Notes | high |
| 105 | 4CH1-3.13 | Catalysts in Chemistry - IGCSE Chemistry Revision Notes | high |
| 106 | 4CH1-3.11 | Explaining Rates  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 107 | 4CH1-3.15 | How surface area affects rate - IGCSE Revision Notes | high |
| 108 | 4CH1-3.16 | Investigating catalysts - IGCSE Chemistry Revision Notes | high |
| 109 | 4CH1-3.9 | Rate of reaction - IGCSE Chemistry Revision Notes | high |
| 110 | 4CH1-3.10 | Rate of reaction - IGCSE Chemistry Revision Notes | high |
| 111 | 4CH1-3.14C | What is activation energy- IGCSE Revision Notes | high |
| 112 | 4CH1-3.20C | Dynamic equilibrium - IGCSE Chemistry Revision Notes | high |
| 113 | 4CH1-3.17 | Reversible reactions - IGCSE Chemistry Revision Notes | high |
| 114 | 4CH1-3.18 | Reversible reactions - IGCSE Chemistry Revision Notes | high |
| 115 | 4CH1-3.22C | The position of equilibrium - IGCSE Chemistry Revision Notes | high |
| 116 | 4CH1-4.6 | Classifying Organic Reactions  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 117 | 4CH1-4.1 | Introduction to Organic Chemistry - IGCSE Revision Notes | high |
| 118 | 4CH1-4.3 | Introduction to Organic Chemistry - IGCSE Revision Notes | high |
| 119 | 4CH1-4.4 | Naming Organic Compounds  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 120 | 4CH1-4.11 | Definition of combustion - IGCSE Chemistry Revision Notes | high |
| 121 | 4CH1-4.12 | Definition of combustion - IGCSE Chemistry Revision Notes | high |
| 122 | 4CH1-4.13 | Definition of combustion - IGCSE Chemistry Revision Notes | high |
| 123 | 4CH1-4.14 | Nitrogen Oxides & Sulfur Dioxide  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 124 | 4CH1-4.16 | Nitrogen Oxides & Sulfur Dioxide  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 125 | 4CH1-4.17 | What is cracking - IGCSE Chemistry Revision Notes | high |
| 126 | 4CH1-4.18 | What is cracking - IGCSE Chemistry Revision Notes | high |
| 127 | 4CH1-4.19 | Alkanes  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 128 | 4CH1-4.20 | Alkanes  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 129 | 4CH1-4.22 | Halogens & Alkanes  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 130 | 4CH1-4.23 | Alkenes  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 131 | 4CH1-4.24 | Alkenes  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 132 | 4CH1-4.25 | Alkenes  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 133 | 4CH1-4.26 | Alkenes  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 134 | 4CH1-4.27 | Bromine & Alkenes  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 135 | 4CH1-4.28 | Bromine & Alkenes  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 136 | 4CH1-4.32C | Manufacture of Ethanol  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 137 | 4CH1-4.33C | Manufacture of Ethanol  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 138 | 4CH1-4.31C | Oxidation of ethanol - IGCSE Chemistry Revision Notes | high |
| 139 | 4CH1-4.37C | Carboxylic Acids  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 140 | 4CH1-4.36C | Reactions of Carboxylic Acids  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 141 | 4CH1-4.39C | Making and naming esters - IGCSE Chemistry Revision Notes | high |
| 142 | 4CH1-4.41C | Making and naming esters - IGCSE Chemistry Revision Notes | high |
| 143 | 4CH1-4.42C | Making and naming esters - IGCSE Chemistry Revision Notes | high |
| 144 | 4CH1-4.43C | Preparation of ethyl ethanoate - IGCSE Chemistry | high |
| 145 | 4CH1-4.45 | Addition Polymers  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 146 | 4CH1-4.46 | Addition Polymers  Edexcel IGCSE Chemistry Revision Notes 2017 | high |
| 147 | 4CH1-4.48C | Condensation polymerisation - IGCSE Chemistry Revision Notes | high |
| 148 | 4CH1-4.49C | Condensation polymerisation - IGCSE Chemistry Revision Notes | high |
| 149 | 4CH1-4.50C | Condensation polymerisation - IGCSE Chemistry Revision Notes | high |
| 150 | 4CH1-4.47 | Disposal of polymers - IGCSE Chemistry Revision Notes | high |

## The 2 round-4 rejections (proven outside the batches)

| code | note (stem) | verdict | disposition |
|---|---|---|---|
| 4CH1-4.15 | Nitrogen Oxides & Sulfur Dioxide  Edexcel IGCSE Chemistry Revision Notes 2017 | **REJECT (round 4, 2026-09-11)** | removed from decisions S4.json (note keeps 4.14 / 4.16); 4.15 -> zero-coverage corpus gap, annotated in PHASE2_MAPPING_C |
| 4CH1-1.17 | Calculate Relative Mass  Edexcel IGCSE Chemistry Revision Notes 2017 | **REJECT (round 4, 2026-09-11)** | removed from decisions S1.json (note keeps 1.26); 1.17 remains covered by its high-confidence in-subsection S1-c mapping |

Both staged batches are exactly the AI-reviewed sets: §12 promotes exactly the 59 round-4-surviving CONFIRMs (both round-4 REJECTs proven removed from the store and absent from the command), §13 promotes exactly the 150 round-5 CONFIRMs, the two batches are disjoint and cover the whole 209-mapping store exactly once, and the pre-state is 0 promoted / 209 SUGGESTED. The operator may execute §12 then §13 as staged.

Provenance: repo HEAD `0db00e8` (descends from the round-5 review state `c90f5ae`; round-5 pre-review SHA `c6454c9`).

After the operator runs §12 then §13, all 209 mappings become HUMAN_VALIDATED (validated_by `operator`, 2026-09-11) — re-run this audit with `--phase post` to machine-verify the executed state (identity bijection, store shape, evidence retention, note-body integrity).
