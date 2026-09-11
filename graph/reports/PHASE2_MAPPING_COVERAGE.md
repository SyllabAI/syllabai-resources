# Phase 2 (T-C10) — Revision-Note to Spec-Point Mapping Coverage

Generated 2026-09-11 by `scripts/c10_map_notes.py` from `scripts/c10_decisions/S*.json` (AI mapping pass, GLM Super Z agent).

## 1. Method

1. **PROVIDER anchor (deterministic, zero-LLM):** each note's Save My Exams source URL embeds a spec-aligned topic-group slug (`…/1-5-chemical-formulae-equations-calculations/…`) which maps 1:1 onto the 28 4CH1 subsections (verified programmatically: 28/28 groups, ordering exact). This subsection anchor is a source fact stored at PROVIDER tier.
2. **AI_SUGGESTED point-level mapping:** an LLM pass (GLM, Super Z agent) read each note's headings/excerpt/body against the full 182-point registry and proposed point-level mappings, each carrying an evidence quote, a confidence (high/medium/low), a rationale, and the model version.
3. **Hard gates (all green):** every mapped code is in the 182-point registry (hence no foreign/4CH0 codes possible); every evidence quote was verified to appear verbatim in the note (anti-hallucination); every note has ≥1 mapping; the note BODY was left byte-identical (front matter only).
4. **Human validation:** nothing here is authoritative. Every mapping carries `validation_status: SUGGESTED`. The git PR review of the front-matter diff IS the HUMAN_VALIDATED gate (operator workflow, §8A.4 four tiers).

## 2. Totals

- Notes mapped: **112 / 112**
- Total mappings: **211** (high 176 · medium 34 · low 1)
- Spec points with ≥1 direct note mapping: **182 / 182**
- Cross-subsection mappings (flagged for PR attention): 1
- Promoted to HUMAN_VALIDATED so far: **0 / 211** (PR review in progress; see `PHASE2_PR_REVIEW_GUIDE.md`)

## 3. Zero-coverage queue (points with no direct note mapping)

The Phase 3/4 enrichment queue handed to the Student Book / question-mapping phases. If this list is empty, the 112 SME notes cover every 4CH1 spec point at point level.

- **EMPTY — all 182 points have ≥1 AI_SUGGESTED note mapping.** Phase 3/4 enrichment should still review *quality* (e.g. poly(tetrafluoroethene) is not among the addition-polymer note's worked examples — see the note's rationale).

## 4. Per-subsection mapping table

| Subsection | SME group | Notes | Mappings | Points covered |
|---|---|---|---|---|
| 4CH1-S1-a States of matter | `1-1-states-of-matter` | 5 | 9 | 7 |
| 4CH1-S1-b Elements, compounds and mixtures | `1-2-elements-compounds-and-mixtures` | 5 | 8 | 6 |
| 4CH1-S1-c Atomic structure | `1-3-atomic-structure` | 2 | 5 | 4 |
| 4CH1-S1-d The Periodic Table | `1-4-the-periodic-table` | 4 | 8 | 7 |
| 4CH1-S1-e Chemical formulae, equations and calculations | `1-5-chemical-formulae-equations-calculations` | 10 | 19 | 13 |
| 4CH1-S1-f Ionic bonding | `1-6-ionic-bonding` | 5 | 9 | 7 |
| 4CH1-S1-g Covalent bonding | `1-7-covalent-bonding` | 4 | 9 | 8 |
| 4CH1-S1-h Metallic bonding | `1-8-metallic-bonding` | 1 | 3 | 3 |
| 4CH1-S1-i Electrolysis | `1-9-electrolysis` | 4 | 8 | 6 |
| 4CH1-S2-a Group 1 (alkali metals) – lithium, sodium and potassium | `2-1-group-1-alkali-metals` | 2 | 4 | 4 |
| 4CH1-S2-b Group 7 (halogens) – chlorine, bromine and iodine | `2-2-group-7-halogens` | 2 | 4 | 4 |
| 4CH1-S2-c Gases in the atmosphere | `2-3-gases-in-the-atmosphere` | 5 | 7 | 6 |
| 4CH1-S2-d Reactivity series | `2-4-reactivity-series` | 6 | 9 | 7 |
| 4CH1-S2-e Extraction and uses of metals | `2-5-extraction-and-uses-of-metals` | 4 | 6 | 6 |
| 4CH1-S2-f Acids, alkalis and titrations | `2-6-acids-alkalis-and-titrations` | 3 | 7 | 6 |
| 4CH1-S2-g Acids, bases and salt preparations | `2-7-acids-bases-and-salt-preparations` | 9 | 12 | 10 |
| 4CH1-S2-h Chemical tests | `2-8-chemical-tests` | 5 | 7 | 7 |
| 4CH1-S3-a Energetics | `3-1-energetics` | 6 | 9 | 8 |
| 4CH1-S3-b Rates of reaction | `3-2-rates-of-reaction` | 6 | 11 | 8 |
| 4CH1-S3-c Reversible reactions and equilibria | `3-3-reversible-reactions-and-equilibria` | 3 | 6 | 6 |
| 4CH1-S4-a Introduction | `4-1-introduction` | 3 | 6 | 6 |
| 4CH1-S4-b Crude oil | `4-2-crude-oil` | 4 | 12 | 12 |
| 4CH1-S4-c Alkanes | `4-3-alkanes` | 2 | 4 | 4 |
| 4CH1-S4-d Alkenes | `4-4-alkenes` | 2 | 6 | 6 |
| 4CH1-S4-e Alcohols | `4-5-alcohols` | 3 | 5 | 5 |
| 4CH1-S4-f Carboxylic acids | `4-6-carboxylic-acids` | 2 | 4 | 4 |
| 4CH1-S4-g Esters | `4-7-esters` | 2 | 7 | 6 |
| 4CH1-S4-h Synthetic polymers | `4-8-synthetic-polymers` | 3 | 7 | 7 |

## 5. Per-point coverage detail

- **4CH1-1.1**: 1 note(s) — Changing states of matter - IGCSE Chemistry Revision Notes (high)
- **4CH1-1.10**: 2 note(s) — Separation techniques - IGCSE Chemistry Revision Notes (high), Paper chromatography - IGCSE Chemistry Revision Notes (medium)
- **4CH1-1.11**: 1 note(s) — Interpreting chromatograms - IGCSE Chemistry Revision Notes (high)
- **4CH1-1.12**: 1 note(s) — Interpreting chromatograms - IGCSE Chemistry Revision Notes (high)
- **4CH1-1.13**: 1 note(s) — Paper chromatography - IGCSE Chemistry Revision Notes (high)
- **4CH1-1.14**: 1 note(s) — Atoms Definitions & Structure  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-1.15**: 1 note(s) — Atoms Definitions & Structure  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-1.16**: 2 note(s) — Atoms Definitions & Structure  Edexcel IGCSE Chemistry Revision Notes 2017 (medium), Relative atomic mass - IGCSE Chemistry Revision Notes (medium)
- **4CH1-1.17**: 2 note(s) — Relative atomic mass - IGCSE Chemistry Revision Notes (high), Calculate Relative Mass  Edexcel IGCSE Chemistry Revision Notes 2017 (medium)
- **4CH1-1.18**: 1 note(s) — Periodic Table Basics  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-1.19**: 1 note(s) — Electronic Configurations  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-1.2**: 1 note(s) — Changing states of matter - IGCSE Chemistry Revision Notes (high)
- **4CH1-1.20**: 1 note(s) — Metals & non-metals in the Periodic Table - IGCSE Chemistry (high)
- **4CH1-1.21**: 1 note(s) — Metals & non-metals in the Periodic Table - IGCSE Chemistry (high)
- **4CH1-1.22**: 2 note(s) — Electronic Configurations  Edexcel IGCSE Chemistry Revision Notes 2017 (high), Electronic Configuration & Reactivity  Edexcel IGCSE Chemistry Revision Notes 2017 (medium)
- **4CH1-1.23**: 1 note(s) — Electronic Configuration & Reactivity  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-1.24**: 1 note(s) — Electronic Configuration & Reactivity  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-1.25**: 2 note(s) — Writing chemical equations - IGCSE Chemistry Revision Notes (high), Reacting mass calculations - IGCSE Chemistry Revision Notes (medium)
- **4CH1-1.26**: 1 note(s) — Calculate Relative Mass  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-1.27**: 1 note(s) — Calculating moles and mass - IGCSE Chemistry Revision Notes (high)
- **4CH1-1.28**: 2 note(s) — Calculating moles and mass - IGCSE Chemistry Revision Notes (high), Reacting mass calculations - IGCSE Chemistry Revision Notes (medium)
- **4CH1-1.29**: 1 note(s) — Reacting mass calculations - IGCSE Chemistry Revision Notes (high)
- **4CH1-1.3**: 1 note(s) — Diffusion - IGCSE Chemistry Revision Notes (high)
- **4CH1-1.30**: 1 note(s) — Calculate percentage yield - IGCSE Chemistry Revision Notes (high)
- **4CH1-1.31**: 3 note(s) — Investigating metal oxide formulas - IGCSE Revision Notes (high), Simple compound formulae - IGCSE Chemistry Revision Notes (high), Empirical & Molecular Formulae  Edexcel IGCSE Chemistry Revision Notes 2017 (medium)
- **4CH1-1.32**: 1 note(s) — Empirical & Molecular Formulae  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-1.33**: 3 note(s) — Empirical & Molecular Formulae  Edexcel IGCSE Chemistry Revision Notes 2017 (high), Investigating metal oxide formulas - IGCSE Revision Notes (medium), Simple compound formulae - IGCSE Chemistry Revision Notes (medium)
- **4CH1-1.34C**: 1 note(s) — Solution concentration - IGCSE Chemistry Revision Notes (high)
- **4CH1-1.35C**: 1 note(s) — Calculate Gas Volumes - IGCSE Chemistry Revision Notes (high)
- **4CH1-1.36**: 1 note(s) — Investigating metal oxide formulas - IGCSE Revision Notes (high)
- **4CH1-1.37**: 3 note(s) — Formation of ions - IGCSE Chemistry Revision Notes (high), Common Ions  Edexcel IGCSE Chemistry Revision Notes 2017 (medium), Ionic bonding diagrams - IGCSE Chemistry Revision Notes (medium)
- **4CH1-1.38**: 1 note(s) — Common Ions  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-1.39**: 1 note(s) — Formula of ionic compounds - IGCSE Chemistry Revision Notes (high)
- **4CH1-1.4**: 2 note(s) — Solutions - IGCSE Chemistry Revision Notes (high), Solubility - IGCSE Chemistry Revision Notes (low)
- **4CH1-1.40**: 1 note(s) — Ionic bonding diagrams - IGCSE Chemistry Revision Notes (high)
- **4CH1-1.41**: 1 note(s) — Ionic bonding and lattices - IGCSE Chemistry Revision Notes (high)
- **4CH1-1.42**: 1 note(s) — Ionic bonding and lattices - IGCSE Chemistry Revision Notes (high)
- **4CH1-1.43**: 1 note(s) — Ionic bonding and lattices - IGCSE Chemistry Revision Notes (high)
- **4CH1-1.44**: 1 note(s) — Forming covalent bonds - IGCSE Chemistry Revision Notes (high)
- **4CH1-1.45**: 1 note(s) — Forming covalent bonds - IGCSE Chemistry Revision Notes (high)
- **4CH1-1.46**: 1 note(s) — Covalent Bonds Dot & Cross Diagrams  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-1.47**: 1 note(s) — Simple molecular structures - IGCSE Chemistry Revision Notes (high)
- **4CH1-1.48**: 1 note(s) — Simple molecular structures - IGCSE Chemistry Revision Notes (high)
- **4CH1-1.49**: 1 note(s) — Giant covalent structures - IGCSE Chemistry Revision Notes (high)
- **4CH1-1.5C**: 2 note(s) — Solubility - IGCSE Chemistry Revision Notes (high), Investigating solubility - IGCSE Chemistry Revision Notes (medium)
- **4CH1-1.50**: 2 note(s) — Giant covalent structures - IGCSE Chemistry Revision Notes (high), Simple molecular structures - IGCSE Chemistry Revision Notes (medium)
- **4CH1-1.51**: 1 note(s) — Simple molecular structures - IGCSE Chemistry Revision Notes (medium)
- **4CH1-1.52C**: 1 note(s) — Metallic bonding - IGCSE Chemistry Revision Notes (medium)
- **4CH1-1.53C**: 1 note(s) — Metallic bonding - IGCSE Chemistry Revision Notes (high)
- **4CH1-1.54C**: 1 note(s) — Metallic bonding - IGCSE Chemistry Revision Notes (high)
- **4CH1-1.55C**: 1 note(s) — Electronic conductivity - IGCSE Chemistry Revision Notes (high)
- **4CH1-1.56C**: 2 note(s) — Electronic conductivity - IGCSE Chemistry Revision Notes (high), Electrolysis diagram - IGCSE Chemistry Revision Notes (medium)
- **4CH1-1.57C**: 1 note(s) — Electronic conductivity - IGCSE Chemistry Revision Notes (high)
- **4CH1-1.58C**: 2 note(s) — Electrolysis diagram - IGCSE Chemistry Revision Notes (high), Practical Investigate the Electrolysis of Aqueous Solutions  Edexcel IGCSE Chemistry Revision Notes 2017 (medium)
- **4CH1-1.59C**: 1 note(s) — Half equations - IGCSE Chemistry Revision Notes (high)
- **4CH1-1.6C**: 1 note(s) — Solubility - IGCSE Chemistry Revision Notes (high)
- **4CH1-1.60C**: 1 note(s) — Practical Investigate the Electrolysis of Aqueous Solutions  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-1.7C**: 1 note(s) — Investigating solubility - IGCSE Chemistry Revision Notes (high)
- **4CH1-1.8**: 2 note(s) — Element, Compound or Mixture  Edexcel IGCSE Chemistry Revision Notes 2017 (high), Pure substances - IGCSE Chemistry Revision Notes (medium)
- **4CH1-1.9**: 1 note(s) — Pure substances - IGCSE Chemistry Revision Notes (high)
- **4CH1-2.1**: 1 note(s) — Group 1 reactivity & trends - IGCSE Chemistry Revision Notes (high)
- **4CH1-2.10**: 2 note(s) — Composition of air - IGCSE Chemistry Revision Notes (high), Oxygen percentage in air - IGCSE Chemistry Revision Notes (medium)
- **4CH1-2.11**: 1 note(s) — Combustion  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-2.12**: 1 note(s) — Thermal decomposition - IGCSE Chemistry Revision Notes (high)
- **4CH1-2.13**: 1 note(s) — Greenhouse effect - IGCSE Chemistry Revision Notes (high)
- **4CH1-2.14**: 1 note(s) — Oxygen percentage in air - IGCSE Chemistry Revision Notes (high)
- **4CH1-2.15**: 2 note(s) — Metals Reacting with Water & Acids  Edexcel IGCSE Chemistry Revision Notes 2017 (high), Metals reacting with acids - IGCSE Chemistry Revision Notes (medium)
- **4CH1-2.16**: 1 note(s) — Metal displacement - IGCSE Chemistry Revision Notes (high)
- **4CH1-2.17**: 2 note(s) — The reactivity series - IGCSE Chemistry Revision Notes (high), Metals Reacting with Water & Acids  Edexcel IGCSE Chemistry Revision Notes 2017 (medium)
- **4CH1-2.18**: 1 note(s) — Rusting of iron - IGCSE Chemistry Revision Notes (high)
- **4CH1-2.19**: 1 note(s) — Rusting of iron - IGCSE Chemistry Revision Notes (high)
- **4CH1-2.2**: 1 note(s) — Group 1 reactivity & trends - IGCSE Chemistry Revision Notes (high)
- **4CH1-2.20**: 1 note(s) — Oxidation and reduction - IGCSE Chemistry Revision Notes (high)
- **4CH1-2.21**: 1 note(s) — Metals reacting with acids - IGCSE Chemistry Revision Notes (high)
- **4CH1-2.22C**: 1 note(s) — Where does metal come from - IGCSE Chemistry Revision Notes (high)
- **4CH1-2.23C**: 1 note(s) — Extraction of metals from ores - IGCSE Chemistry (high)
- **4CH1-2.24C**: 1 note(s) — Extraction of metals from ores - IGCSE Chemistry (medium)
- **4CH1-2.25C**: 1 note(s) — Metals and their uses - IGCSE Chemistry Revision Notes (high)
- **4CH1-2.26C**: 1 note(s) — Alloys - IGCSE Chemistry Revision Notes (high)
- **4CH1-2.27C**: 1 note(s) — Alloys - IGCSE Chemistry Revision Notes (high)
- **4CH1-2.28**: 1 note(s) — What is an indicator - IGCSE Chemistry Revision Notes (high)
- **4CH1-2.29**: 2 note(s) — What is an indicator - IGCSE Chemistry Revision Notes (high), Acids, Alkalis & Neutralisation - IGCSE Revision Notes (medium)
- **4CH1-2.3**: 1 note(s) — Group 1 reactivity & trends - IGCSE Chemistry Revision Notes (high)
- **4CH1-2.30**: 1 note(s) — What is an indicator - IGCSE Chemistry Revision Notes (high)
- **4CH1-2.31**: 1 note(s) — Acids, Alkalis & Neutralisation - IGCSE Revision Notes (high)
- **4CH1-2.32**: 1 note(s) — Acids, Alkalis & Neutralisation - IGCSE Revision Notes (high)
- **4CH1-2.33C**: 1 note(s) — Acid-Alkali Titrations  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-2.34**: 1 note(s) — Solubility Rules  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-2.35**: 1 note(s) — What are acids and bases - IGCSE Chemistry Revision Notes (high)
- **4CH1-2.36**: 1 note(s) — What are acids and bases - IGCSE Chemistry Revision Notes (high)
- **4CH1-2.37**: 1 note(s) — Reactions of acids - IGCSE Chemistry Revision Notes (high)
- **4CH1-2.38**: 1 note(s) — Bases and alkalis - IGCSE Chemistry Revision Notes (high)
- **4CH1-2.39**: 2 note(s) — Making soluble salts - IGCSE Chemistry Revision Notes (high), Preparing copper sulfate - IGCSE Chemistry Revision Notes (medium)
- **4CH1-2.4C**: 1 note(s) — Group 1 Reactivity & Electronic Configurations  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-2.40C**: 1 note(s) — Prepare a Soluble Salt II  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-2.41C**: 2 note(s) — Prepare an Insoluble Salt  Edexcel IGCSE Chemistry Revision Notes 2017 (high), Preparing lead sulfate - IGCSE Chemistry Revision Notes (medium)
- **4CH1-2.42**: 1 note(s) — Preparing copper sulfate - IGCSE Chemistry Revision Notes (high)
- **4CH1-2.43C**: 1 note(s) — Preparing lead sulfate - IGCSE Chemistry Revision Notes (high)
- **4CH1-2.44**: 1 note(s) — Gas tests - IGCSE Chemistry Revision Notes (high)
- **4CH1-2.45**: 1 note(s) — Flame tests - IGCSE Chemistry Revision Notes (high)
- **4CH1-2.46**: 1 note(s) — Flame tests - IGCSE Chemistry Revision Notes (high)
- **4CH1-2.47**: 1 note(s) — Tests for cations - IGCSE Chemistry Revision Notes (high)
- **4CH1-2.48**: 1 note(s) — Tests for Anions  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-2.49**: 1 note(s) — Chemical test for water - IGCSE Chemistry Revision Notes (high)
- **4CH1-2.5**: 1 note(s) — Group 7 properties - IGCSE Chemistry Revision Notes (high)
- **4CH1-2.50**: 1 note(s) — Chemical test for water - IGCSE Chemistry Revision Notes (high)
- **4CH1-2.6**: 1 note(s) — Group 7 properties - IGCSE Chemistry Revision Notes (high)
- **4CH1-2.7**: 1 note(s) — Group 7 properties - IGCSE Chemistry Revision Notes (high)
- **4CH1-2.8C**: 1 note(s) — Group 7 reactivity - IGCSE Chemistry Revision Notes (high)
- **4CH1-2.9**: 1 note(s) — Composition of air - IGCSE Chemistry Revision Notes (high)
- **4CH1-3.1**: 1 note(s) — Exothermic and endothermic - IGCSE Chemistry Revision Notes (high)
- **4CH1-3.10**: 2 note(s) — Rate of reaction - IGCSE Chemistry Revision Notes (high), Explaining Rates  Edexcel IGCSE Chemistry Revision Notes 2017 (medium)
- **4CH1-3.11**: 1 note(s) — Explaining Rates  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-3.12**: 1 note(s) — Catalysts in Chemistry - IGCSE Chemistry Revision Notes (high)
- **4CH1-3.13**: 1 note(s) — Catalysts in Chemistry - IGCSE Chemistry Revision Notes (high)
- **4CH1-3.14C**: 1 note(s) — What is activation energy- IGCSE Revision Notes (high)
- **4CH1-3.15**: 1 note(s) — How surface area affects rate - IGCSE Revision Notes (high)
- **4CH1-3.16**: 1 note(s) — Investigating catalysts - IGCSE Chemistry Revision Notes (high)
- **4CH1-3.17**: 1 note(s) — Reversible reactions - IGCSE Chemistry Revision Notes (high)
- **4CH1-3.18**: 1 note(s) — Reversible reactions - IGCSE Chemistry Revision Notes (high)
- **4CH1-3.19C**: 1 note(s) — Dynamic equilibrium - IGCSE Chemistry Revision Notes (high)
- **4CH1-3.2**: 2 note(s) — Calorimetry - IGCSE Chemistry Revision Notes (high), Temperature change practical - IGCSE Revision Notes (medium)
- **4CH1-3.20C**: 1 note(s) — Dynamic equilibrium - IGCSE Chemistry Revision Notes (high)
- **4CH1-3.21C**: 1 note(s) — The position of equilibrium - IGCSE Chemistry Revision Notes (high)
- **4CH1-3.22C**: 1 note(s) — The position of equilibrium - IGCSE Chemistry Revision Notes (high)
- **4CH1-3.3**: 1 note(s) — Energetics calculations in chemistry - IGCSE Revision Notes (high)
- **4CH1-3.4**: 1 note(s) — Energetics calculations in chemistry - IGCSE Revision Notes (high)
- **4CH1-3.5C**: 1 note(s) — Energy level diagrams - IGCSE Chemistry Revision Notes (high)
- **4CH1-3.6C**: 1 note(s) — What is bond energy - IGCSE Chemistry Revision Notes (high)
- **4CH1-3.7C**: 1 note(s) — What is bond energy - IGCSE Chemistry Revision Notes (high)
- **4CH1-3.8**: 1 note(s) — Temperature change practical - IGCSE Revision Notes (high)
- **4CH1-3.9**: 3 note(s) — Rate of reaction - IGCSE Chemistry Revision Notes (high), How surface area affects rate - IGCSE Revision Notes (medium), Investigating catalysts - IGCSE Chemistry Revision Notes (medium)
- **4CH1-4.1**: 1 note(s) — Introduction to Organic Chemistry - IGCSE Revision Notes (high)
- **4CH1-4.10**: 1 note(s) — Fractional distillation - IGCSE Chemistry Revision Notes (high)
- **4CH1-4.11**: 1 note(s) — Definition of combustion - IGCSE Chemistry Revision Notes (high)
- **4CH1-4.12**: 1 note(s) — Definition of combustion - IGCSE Chemistry Revision Notes (high)
- **4CH1-4.13**: 1 note(s) — Definition of combustion - IGCSE Chemistry Revision Notes (high)
- **4CH1-4.14**: 1 note(s) — Nitrogen Oxides & Sulfur Dioxide  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-4.15**: 1 note(s) — Nitrogen Oxides & Sulfur Dioxide  Edexcel IGCSE Chemistry Revision Notes 2017 (medium)
- **4CH1-4.16**: 1 note(s) — Nitrogen Oxides & Sulfur Dioxide  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-4.17**: 1 note(s) — What is cracking - IGCSE Chemistry Revision Notes (high)
- **4CH1-4.18**: 1 note(s) — What is cracking - IGCSE Chemistry Revision Notes (high)
- **4CH1-4.19**: 1 note(s) — Alkanes  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-4.2**: 1 note(s) — Introduction to Organic Chemistry - IGCSE Revision Notes (high)
- **4CH1-4.20**: 1 note(s) — Alkanes  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-4.21**: 1 note(s) — Alkanes  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-4.22**: 1 note(s) — Halogens & Alkanes  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-4.23**: 1 note(s) — Alkenes  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-4.24**: 1 note(s) — Alkenes  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-4.25**: 1 note(s) — Alkenes  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-4.26**: 1 note(s) — Alkenes  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-4.27**: 1 note(s) — Bromine & Alkenes  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-4.28**: 1 note(s) — Bromine & Alkenes  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-4.29C**: 1 note(s) — Alcohols  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-4.3**: 1 note(s) — Introduction to Organic Chemistry - IGCSE Revision Notes (high)
- **4CH1-4.30C**: 1 note(s) — Alcohols  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-4.31C**: 1 note(s) — Oxidation of ethanol - IGCSE Chemistry Revision Notes (high)
- **4CH1-4.32C**: 1 note(s) — Manufacture of Ethanol  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-4.33C**: 1 note(s) — Manufacture of Ethanol  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-4.34C**: 1 note(s) — Carboxylic Acids  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-4.35C**: 1 note(s) — Carboxylic Acids  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-4.36C**: 1 note(s) — Reactions of Carboxylic Acids  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-4.37C**: 1 note(s) — Carboxylic Acids  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-4.38C**: 1 note(s) — Making and naming esters - IGCSE Chemistry Revision Notes (high)
- **4CH1-4.39C**: 2 note(s) — Making and naming esters - IGCSE Chemistry Revision Notes (high), Preparation of ethyl ethanoate - IGCSE Chemistry (medium)
- **4CH1-4.4**: 1 note(s) — Naming Organic Compounds  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-4.40C**: 1 note(s) — Making and naming esters - IGCSE Chemistry Revision Notes (medium)
- **4CH1-4.41C**: 1 note(s) — Making and naming esters - IGCSE Chemistry Revision Notes (high)
- **4CH1-4.42C**: 1 note(s) — Making and naming esters - IGCSE Chemistry Revision Notes (high)
- **4CH1-4.43C**: 1 note(s) — Preparation of ethyl ethanoate - IGCSE Chemistry (high)
- **4CH1-4.44**: 1 note(s) — Addition Polymers  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-4.45**: 1 note(s) — Addition Polymers  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-4.46**: 1 note(s) — Addition Polymers  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-4.47**: 1 note(s) — Disposal of polymers - IGCSE Chemistry Revision Notes (high)
- **4CH1-4.48C**: 1 note(s) — Condensation polymerisation - IGCSE Chemistry Revision Notes (high)
- **4CH1-4.49C**: 1 note(s) — Condensation polymerisation - IGCSE Chemistry Revision Notes (high)
- **4CH1-4.5**: 1 note(s) — Introduction to Organic Chemistry - IGCSE Revision Notes (medium)
- **4CH1-4.50C**: 1 note(s) — Condensation polymerisation - IGCSE Chemistry Revision Notes (high)
- **4CH1-4.6**: 1 note(s) — Classifying Organic Reactions  Edexcel IGCSE Chemistry Revision Notes 2017 (high)
- **4CH1-4.7**: 1 note(s) — Fractional distillation - IGCSE Chemistry Revision Notes (high)
- **4CH1-4.8**: 1 note(s) — Fractional distillation - IGCSE Chemistry Revision Notes (high)
- **4CH1-4.9**: 1 note(s) — Fractional distillation - IGCSE Chemistry Revision Notes (high)

## 6. PR review guide

1. Review the front-matter diff of this commit — each note's `spec_map:` block is a small, self-contained review unit (code + confidence + evidence quote + rationale). The full work order in the operator's stated priority order is `graph/reports/PHASE2_PR_REVIEW_GUIDE.md` (remapped 4.15 first, then the low/medium set, then the semantic completeness and diagram-verification scans).
2. Start with **medium/low** confidence mappings and the cross-subsection flags below — they are the ones where the mapping judgment is least mechanical.
3. Spot-check status (2026-09-11): the 20-sample sheet (`graph/reports/PHASE2_SPOT_CHECK_SHEET.md`) was operator-reviewed — 19 confirmed (1 of them after machine visual verification of the metallic-lattice diagram), 1 rejected and remapped (4CH1-4.15, see the sheet's review record).
4. Approve/adjust via the PR: a confirmed mapping is promoted by adding a `validation` block (HUMAN_VALIDATED + validated_by + validated_date) to its entry in `scripts/c10_decisions/S*.json` and re-running the gated applier — `scripts/c10_promote.py` batches this. The note front matter is then regenerated carrying `validation_status: HUMAN_VALIDATED`. NEVER hand-edit the front matter for promotion: the applier regenerates it from decisions and would silently revert the edit on the next rework re-run.
5. **Evidence-existence is not semantic validity.** The automated G3 gate proves a mapping's evidence quote exists verbatim in the note; it cannot prove the quote covers the spec point's semantics. The 4.15 case is the canonical example: a true quote (fuel sulfur impurities) that never established the impurity -> combustion -> sulfur-dioxide causal chain the point demands. Read every mapping as *does this note teach what the point asks*, not as *does this sentence exist*.

### Cross-subsection mappings (flagged)

- `4CH1-1.17` — note anchored in 4CH1-S1-e (slug), point sits in 4CH1-S1-c: Calculate Relative Mass  Edexcel IGCSE Chemistry Revision Notes 2017.md
