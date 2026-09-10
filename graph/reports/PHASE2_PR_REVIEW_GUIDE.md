# Phase 2 (T-C10) — PR Front-Matter Review Guide

Generated 2026-09-11 by `scripts/c10_pr_review_guide.py` (deterministic: decisions JSON + 182-point registry + note image-resolution scan).

**Status context:** the operator spot-check is CLOSED (19/20 confirmed, 1 rejected and remapped — verdicts and the review record live on `PHASE2_SPOT_CHECK_SHEET.md`, which is locked against regeneration). T-C10 is **implementation-complete but not yet HUMAN_VALIDATED**: this guide is the work order for the remaining gate, the git PR front-matter review, in the operator's stated priority order (2026-09-11).

## 0. Review mechanics and promotion protocol

1. **Unit of review** = one `spec_map.spec_points[]` entry in a note's front matter: `code` + `provenance.confidence` + `provenance.evidence` + `provenance.rationale`. Open the note, read the block, open the spec wording (below or `graph/specification_points.yaml`).
2. **The two standing lessons** (from the operator's spot-check): (a) *evidence-existence is not semantic validity* — the quote existing in the note does not show the note teaches what the point demands (the 4.15 case); (b) *diagram-dependent mappings need eyes on the diagram*, not just the text (the 1.52C case).
3. **CONFIRMED → promotion (decisions-side, never note hand-edits):** add a `validation` block to that mapping's entry in `scripts/c10_decisions/S*.json`:
   ```
   "validation": {"validation_status": "HUMAN_VALIDATED",
                     "validated_by": "operator",
                     "validated_date": "2026-09-11"}
   ```
   then re-run `python3 scripts/c10_map_notes.py` — or use the batch helper `scripts/c10_promote.py`, which edits the decisions and re-runs the applier in one step. The front matter is regenerated carrying the promotion; note bodies stay byte-identical. Hand-edits on note front matter are the WRONG route: the applier regenerates front matter from the decisions and would silently revert them on the next rework re-run. The `tier` stays `AI_SUGGESTED` forever (origin is immutable); only the review state changes. The validator accepts exactly `SUGGESTED` (clean — no stray promotion fields) or `HUMAN_VALIDATED` (with `validated_by` + `validated_date`); anything else fails, and a promoted mapping with the tier flipped is still caught (premature authority).
4. **REJECT → rework:** edit `scripts/c10_decisions/S*.json` (remove or re-map with in-note evidence) and re-run `python3 scripts/c10_map_notes.py` — all hard gates re-validate, the locked spot-check sheet is preserved. Precedent: `scripts/c10_rework_415.py`.

## 1. Priority 1 — the remapped 4CH1-4.15

The one mapping changed by the spot-check rework. Verify the note now teaches the point's causal relationship in-note.

- code: **4CH1-4.15** (confidence **medium**)
- note: `Chemistry IGCSE Revision Notes/4. Organic Chemistry/b. Crude Oil/Nitrogen Oxides & Sulfur Dioxide  Edexcel IGCSE Chemistry Revision Notes 2017.md`
- spec: “explain how the combustion of some impurities in hydrocarbon fuels results in the formation of sulfur dioxide”
- evidence: “The sulfur dioxide produced from the combustion of fossil fuels”
- rationale: Remapped after the operator spot-check (2026-09-11) rejected the combustion-note mapping, whose evidence proved only the fuel-impurity premise. This note states the 4.15 causal relationship directly - combustion of foss…

Review question: does the evidence sentence establish **combustion of fossil fuels → sulfur dioxide** in this note (the impurity premise is contextual)? The rejected combustion-note mapping proved only the premise; this remap must prove the causal claim.

## 2. Priority 2 — the 1 low-confidence mapping

- code: **4CH1-1.4** (confidence **low**)
- note: `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/a. States of Matter/Solubility - IGCSE Chemistry Revision Notes.md`
- spec: “know what is meant by the terms: • solvent • solute • solution • saturated solution.”
- evidence: “The liquid is called the solvent”
- rationale: Uses the solvent/saturated-solution vocabulary in context; the dedicated terminology note covers 1.4 fully.
- ⚠ also a priority-5 flag: the rationale itself defers to “the dedicated terminology note” — decide whether THIS note teaches 1.4 or only uses its vocabulary (the 4.15 pattern).

## 3. Priority 3 — the 34 medium-confidence mappings

Ordered: priority-5-flagged first, then the cross-subsection flag (1.17), then registry order. `P5` = cross-note deferral flag (§5); `P6` = diagram-dependent (§6); `XSUB` = cross-subsection.

| # | code | note | evidence | flags |
|---|---|---|---|---|
| 1 | 4CH1-1.10 | Paper chromatography - IGCSE Chemistry Revis… | Investigate how paper chromatography can be used to separat… | P5 |
| 2 | 4CH1-1.16 | Atoms Definitions & Structure  Edexcel IGCSE… | It is equal to 1/12th the mass of an atom of carbon-12 | P5 |
| 3 | 4CH1-1.50 | Simple molecular structures - IGCSE Chemistr… | Fullerenes are a group of carbon allotropes | P5 |
| 4 | 4CH1-2.17 | Metals Reacting with Water & Acids  Edexcel … | The series can be used to place a group of metals in order … | P5 |
| 5 | 4CH1-2.29 | Acids, Alkalis & Neutralisation - IGCSE Revi… | The pH scale is a numerical scale which is used to show how… | P5 |
| 6 | 4CH1-3.10 | Explaining Rates  Edexcel IGCSE Chemistry Re… | Increasing the concentration of a solution increases the ra… | P5 |
| 7 | 4CH1-4.5 | Introduction to Organic Chemistry - IGCSE Re… | Isomers of C3H6 | P5, P6 |
| 8 | 4CH1-4.15 | Nitrogen Oxides & Sulfur Dioxide  Edexcel IG… | The sulfur dioxide produced from the combustion of fossil f… | P5 |
| 9 | 4CH1-1.17 | Calculate Relative Mass  Edexcel IGCSE Chemi… | This is calculated from the mass number and relative abunda… | XSUB |
| 10 | 4CH1-1.16 | Relative atomic mass - IGCSE Chemistry Revis… | The relative atomic mass of each element is calculated from… | — |
| 11 | 4CH1-1.22 | Electronic Configuration & Reactivity  Edexc… | The group number of an element which is given on the Period… | — |
| 12 | 4CH1-1.25 | Reacting mass calculations - IGCSE Chemistry… | Balancing Equations using Reacting Masses | — |
| 13 | 4CH1-1.28 | Reacting mass calculations - IGCSE Chemistry… | Once the moles have been determined they can then be conver… | — |
| 14 | 4CH1-1.31 | Empirical & Molecular Formulae  Edexcel IGCS… | Deducing formulae of hydrated salts | — |
| 15 | 4CH1-1.33 | Investigating metal oxide formulas - IGCSE R… | To determine the empirical formula of magnesium oxide by co… | — |
| 16 | 4CH1-1.33 | Simple compound formulae - IGCSE Chemistry R… | Using the moles of reactants and products it is possible to… | — |
| 17 | 4CH1-1.37 | Common Ions  Edexcel IGCSE Chemistry Revisio… | Find out if it is easier for the atom to gain electron or t… | — |
| 18 | 4CH1-1.37 | Ionic bonding diagrams - IGCSE Chemistry Rev… | Sodium is a Group 1 metal so will lose one outer electron t… | — |
| 19 | 4CH1-1.5C | Investigating solubility - IGCSE Chemistry R… | evaporating the solvent, and measuring the mass of the soli… | — |
| 20 | 4CH1-1.51 | Simple molecular structures - IGCSE Chemistr… | cannot migrate from one buckyball to another, so C60 does n… | — |
| 21 | 4CH1-1.52C | Metallic bonding - IGCSE Chemistry Revision … | Metals consist of giant structures of atoms arranged in a r… | P6 |
| 22 | 4CH1-1.56C | Electrolysis diagram - IGCSE Chemistry Revis… | When these compounds are heated beyond their melting point,… | — |
| 23 | 4CH1-1.58C | Practical Investigate the Electrolysis of Aq… | To electrolyse aqueous solutions of sodium chloride, sulfur… | — |
| 24 | 4CH1-1.8 | Pure substances - IGCSE Chemistry Revision N… | In chemistry, a pure substance may consist of a single elem… | — |
| 25 | 4CH1-2.10 | Oxygen percentage in air - IGCSE Chemistry R… | To determine the percentage of oxygen in air using the oxid… | — |
| 26 | 4CH1-2.15 | Metals reacting with acids - IGCSE Chemistry… | To investigate the reactions between dilute hydrochloric an… | — |
| 27 | 4CH1-2.24C | Extraction of metals from ores - IGCSE Chemi… | The position of the metal on the reactivity series determin… | — |
| 28 | 4CH1-2.39 | Preparing copper sulfate - IGCSE Chemistry R… | The preparation of copper(II) sulfate by the insoluble base… | — |
| 29 | 4CH1-2.41C | Preparing lead sulfate - IGCSE Chemistry Rev… | The preparation of lead(II)sulfate by precipitation from tw… | — |
| 30 | 4CH1-3.2 | Temperature change practical - IGCSE Revisio… | To perform a calorimetry study of the reaction between HCl … | — |
| 31 | 4CH1-3.9 | How surface area affects rate - IGCSE Revisi… | Investigating the effect of different size marble chips on … | — |
| 32 | 4CH1-3.9 | Investigating catalysts - IGCSE Chemistry Re… | To investigate the effect of different solids on the cataly… | — |
| 33 | 4CH1-4.39C | Preparation of ethyl ethanoate - IGCSE Chemi… | A mixture of ethanoic acid, ethanol and concentrated sulfur… | — |
| 34 | 4CH1-4.40C | Making and naming esters - IGCSE Chemistry R… | CH3COOH + C2H5OH → CH3COOC2H5 + H2O | P6 |

## 4. Priority 4 — the 4CH1-1.17 cross-subsection flag

1.17 is mapped on TWO notes. Only one of them is the actual cross-subsection case (note anchored to a different subsection than the point's registry subsection); the other is the ordinary in-subsection mapping and is listed for contrast.

- code: **4CH1-1.17** (confidence **high**)
- note: `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/c. Atomic Structure/Relative atomic mass - IGCSE Chemistry Revision Notes.md`
- spec: “be able to calculate the relative atomic mass of an element $ A_{r} $ from isotopic abundances”
- evidence: “The relative atomic mass of each element is calculated from the mass number and relative abundances of all the isotopes of a particular element”
- rationale: Ar-from-isotopic-abundances equation with multi-isotope worked examples.
- subsections: note anchored **4CH1-S1-c** = point's registry subsection **4CH1-S1-c** — in-subsection, the mechanical default (not the flag).

- code: **4CH1-1.17** (confidence **medium**)
- note: `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculate Relative Mass  Edexcel IGCSE Chemistry Revision Notes 2017.md`
- spec: “be able to calculate the relative atomic mass of an element $ A_{r} $ from isotopic abundances”
- evidence: “This is calculated from the mass number and relative abundances of all the isotopes of a particular element”
- rationale: Cross-subsection: the note's opening defines Ar via isotopic abundances (the 1.17 calculation) before moving to Mr. Flagged for PR attention as an out-of-subsection mapping.
- subsections: note anchored **4CH1-S1-e** but point sits in **4CH1-S1-c** — **the cross-subsection flag**: the note is anchored by its source-URL slug to its own subsection, yet opens by teaching this point's content before moving on; legitimate but the least mechanical mapping in the batch.

## 5. Priority 5 — cross-note deferral candidates (semantic completeness)

Computed scan: rationales containing explicit deferral language (“the dedicated … note carries …”, “lives in”, “are in the”, “carried separately”, …). For each, the review question is the operator's: **does this note independently teach the mapped point, or does the point's substance live in the other note?** (the 4.15 pattern). A split across two notes is sometimes legitimate content architecture — the reviewer decides, mapping by mapping.

- **4CH1-1.10** [medium] — `Paper chromatography - IGCSE Chemistry Revision Notes`
  - rationale: Paper chromatography is one of the five separation techniques listed in 1.10; the technique note is the generic one, this is the practical instance.
- **4CH1-1.16** [medium] — `Atoms Definitions & Structure  Edexcel IGCSE Chemistry Revision Notes 2017`
  - rationale: Terms table includes atomic number, mass number, isotope and relative atomic mass (quoted: Ar row); the dedicated RAM note carries the calculation side.
- **4CH1-1.4** [low] — `Solubility - IGCSE Chemistry Revision Notes` **(low — priority 2)**
  - rationale: Uses the solvent/saturated-solution vocabulary in context; the dedicated terminology note covers 1.4 fully.
- **4CH1-1.50** [medium] — `Simple molecular structures - IGCSE Chemistry Revision Notes`
  - rationale: C60 fullerene section of 1.50 lives here (hollow cage, does not conduct); diamond/graphite are in the giant-covalent note.
- **4CH1-2.17** [medium] — `Metals Reacting with Water & Acids  Edexcel IGCSE Chemistry Revision Notes 2017`
  - rationale: The tables order K through Cu; the dedicated reactivity-series note carries the full 2.17 list.
- **4CH1-2.29** [medium] — `Acids, Alkalis & Neutralisation - IGCSE Revision Notes`
  - rationale: pH scale introduced; the indicator note carries the full 0-14 classification bands.
- **4CH1-3.10** [medium] — `Explaining Rates  Edexcel IGCSE Chemistry Revision Notes 2017`
  - rationale: Describes the factor effects (the full effect descriptions are also in the rate-of-reaction note).
- **4CH1-4.15** [medium] — `Nitrogen Oxides & Sulfur Dioxide  Edexcel IGCSE Chemistry Revision Notes 2017` **(the 4.15 remap — priority 1; 'carried separately' refers to 4.16's acid-rain content, not to 4.15)**
  - rationale: Remapped after the operator spot-check (2026-09-11) rejected the combustion-note mapping, whose evidence proved only the fuel-impurity premise. This note states the 4.15 causal relationship directly …
- **4CH1-4.5** [medium] — `Introduction to Organic Chemistry - IGCSE Revision Notes`
  - rationale: Isomerism section writes alternative structural/displayed formulae from a molecular formula (the 4.5 skill); the naming side lives in the dedicated naming note.

## 6. Priority 6 — diagram-dependent mappings (visual verification queue)

Computed scan: mappings whose rationale leans on a diagram / graph / pie chart / displayed formulae. The textual evidence quote alone is **not sufficient** for these — eyeball the referenced image in the note. Image paths below resolve in the corpus.

### 6a. Visual eyeball queue (images resolve)

- **4CH1-1.41** [high] — `Ionic bonding and lattices - IGCSE Chemistry Revision Notes` 
  - rationale: Ionic bonding as electrostatic attraction, giant lattice description, NaCl lattice diagram.
  - images: `Oppositely-charged-ions-attraction-due-to-electrostatic-attraction.png.png`, `NaCl-Lattice_-Ball-Ball-Stick.png`, `Molten-ionic-substances-conduct-electricity-1.png`
- **4CH1-1.52C** [medium] — `Metallic bonding - IGCSE Chemistry Revision Notes` — machine-verified 2026-09-11 (VLM: 2-D regular ion array + labelled delocalised electrons) — operator may re-eyeball
  - rationale: The lattice diagram and regular-pattern description support the 2-D metallic lattice representation.
  - images: `Metallic-lattice-structure_.png`, `sdy1M7M0_malleability.png`
- **4CH1-1.60C** [high] — `Practical Investigate the Electrolysis of Aqueous Solutions  Edexcel IGCSE Chemistry Revision Notes 2017` 
  - rationale: This IS the named practical (aim, apparatus diagram, method, product testing, results, conclusions).
  - images: `Electrolysis-Apparatus-Inverted-Test-Tubes.png`
- **4CH1-2.21** [high] — `Metals reacting with acids - IGCSE Chemistry Revision Notes` 
  - rationale: This IS the named practical (aim, diagram, method, observations table, conclusion).
  - images: `2.4.6-Investigating-Acids-with-Metals-Diagram.png`
- **4CH1-2.26C** [high] — `Alloys - IGCSE Chemistry Revision Notes` 
  - rationale: Alloy definition with steel (iron + carbon) example and alloy-structure diagram.
  - images: `Structure-of-alloy.png`
- **4CH1-2.33C** [high] — `Acid-Alkali Titrations  Edexcel IGCSE Chemistry Revision Notes 2017` 
  - rationale: Full titration description: apparatus diagram, step-by-step method, titration results table (the 2.33C content).
  - images: `39888_titration-setup1.png`, `Titration-apparatus.png`
- **4CH1-2.5** [high] — `Group 7 properties - IGCSE Chemistry Revision Notes` 
  - rationale: Physical properties table (state, appearance, colour in solution) and the melting/boiling-point trend graph.
  - images: `Melting-boiling-points-of-the-Halogens.png`, `States-of-the-Halogens.png`, `Ionic-bonding-–-Sodium-Chloride.png`
- **4CH1-2.9** [high] — `Composition of air - IGCSE Chemistry Revision Notes` 
  - rationale: Atmosphere composition with pie chart: N2 approx 80%, O2 approx 20%, plus the smaller proportions (CO2, noble gases).
  - images: `Pie-chart-showing-composition-of-air.png`, `Oxygen-in-air-using-combustion.png`
- **4CH1-3.19C** [high] — `Dynamic equilibrium - IGCSE Chemistry Revision Notes` 
  - rationale: Dynamic equilibrium in a sealed/closed container with the open-vs-closed system comparison and rate-vs-progress graph.
  - images: `Equilibrium-in-open-closed-systems.png`, `Dynamic-Equilibrium.png`
- **4CH1-3.2** [high] — `Calorimetry - IGCSE Chemistry Revision Notes` 
  - rationale: Simple calorimetry for reactions in solution (neutralisation, dissolving, displacement) and combustion, with apparatus diagram and error analysis.
  - images: `18446_1-5-chemical-energetics-calorime.png`, `50507_5-1-4-simple-calorimeter-1.png`
- **4CH1-3.21C** [high] — `The position of equilibrium - IGCSE Chemistry Revision Notes` 
  - rationale: Dedicated catalysts-and-equilibrium section with the equal-rate-increase mechanism diagram.
  - images: `Effect-catalyst-on-equilibrium-position.png`
- **4CH1-4.2** [high] — `Introduction to Organic Chemistry - IGCSE Revision Notes` 
  - rationale: Dedicated sections with worked examples for empirical, molecular, general, structural and displayed formulae.
  - images: `10.1.2-The-Molecular-Formulae-of-Butane-and-Butene-1.png`, `10.1.2-The-Structural-Formulae-of-2-methylbutane-1.png`, `10.1.2-Representing-Condensed-Structrual-Formulae-of-Straight-Chains.png`, `14.1.3-Names-and-structures-of-the-functional-groups-table.png`
- **4CH1-4.21** [high] — `Alkanes  Edexcel IGCSE Chemistry Revision Notes 2017` 
  - rationale: Table and displayed formulae (methane through pentane) with the unbranched names.
  - images: `methane.png`, `ethane.png`, `propane.png`, `butane.png`
- **4CH1-4.29C** [high] — `Alcohols  Edexcel IGCSE Chemistry Revision Notes 2017` 
  - rationale: The -OH functional group as the reactive part of alcohols, with the ethanol molecule diagram.
  - images: `Alcohol-Functional-Group-1.png`, `methanol-.png`, `screenshot-2024-02-18-191221.png`, `propanol-displayed.png`
- **4CH1-4.30C** [high] — `Alcohols  Edexcel IGCSE Chemistry Revision Notes 2017` 
  - rationale: Methanol, ethanol, propanol and butanol with displayed formulae and names.
  - images: `Alcohol-Functional-Group-1.png`, `methanol-.png`, `screenshot-2024-02-18-191221.png`, `propanol-displayed.png`
- **4CH1-4.34C** [high] — `Carboxylic Acids  Edexcel IGCSE Chemistry Revision Notes 2017` 
  - rationale: The -COOH functional group with structure diagram and general formula.
  - images: `28940_carboxylic-acid-functional-group.png`, `Carboxylic-Acids-The-First-Four-1.png`
- **4CH1-4.35C** [high] — `Carboxylic Acids  Edexcel IGCSE Chemistry Revision Notes 2017` 
  - rationale: Naming section with worked examples and displayed formulae for the unbranched-chain acids up to four carbons.
  - images: `28940_carboxylic-acid-functional-group.png`, `Carboxylic-Acids-The-First-Four-1.png`
- **4CH1-4.38C** [high] — `Making and naming esters - IGCSE Chemistry Revision Notes` 
  - rationale: Ester functional group with structure diagram.
  - images: `8218_ester-functional-group.png`, `Preparing-Ethyl-Ethanoate_.png`, `Parts-of-an-Ester_.png`, `updated-ester-table.png`
- **4CH1-4.40C** [medium] — `Making and naming esters - IGCSE Chemistry Revision Notes` 
  - rationale: Structural/displayed formulae of ethyl ethanoate shown via the formation equation and diagram.
  - images: `8218_ester-functional-group.png`, `Preparing-Ethyl-Ethanoate_.png`, `Parts-of-an-Ester_.png`, `updated-ester-table.png`
- **4CH1-4.44** [high] — `Addition Polymers  Edexcel IGCSE Chemistry Revision Notes 2017` 
  - rationale: Addition polymerisation from monomers, with the monomer-to-polymer diagram.
  - images: `Polymers-Basic-.png`, `7.7-Polymerisation-Polymers-From-One-Alkene-Monomer.png`, `Drawing-repeating-units.png`, `Deducing-monomer-structure-from-repeat-units.png`
- **4CH1-4.5** [medium] — `Introduction to Organic Chemistry - IGCSE Revision Notes` 
  - rationale: Isomerism section writes alternative structural/displayed formulae from a molecular formula (the 4.5 skill); the naming side lives in the dedicated n…
  - images: `10.1.2-The-Molecular-Formulae-of-Butane-and-Butene-1.png`, `10.1.2-The-Structural-Formulae-of-2-methylbutane-1.png`, `10.1.2-Representing-Condensed-Structrual-Formulae-of-Straight-Chains.png`, `14.1.3-Names-and-structures-of-the-functional-groups-table.png`

### 6b. Missing figures — mapping leans on a visual that is NOT in the corpus

Three notes carry `figure-missing` markers (download failed during clipping; tracked since the corpus-repair pass). Their mappings must be decided on the surviving text alone, downgraded, or held for image recovery.

- **`Interpreting chromatograms - IGCSE Chemistry Revision Notes`** — missing: `../../assets/.jpeg`
  - 4CH1-1.11 [high] (textual evidence) — evidence: “We can use a chromatogram to compare the substances present in a mixture to known substan…”
  - 4CH1-1.12 [high] (textual evidence) — evidence: “retention factor, Rf, is calculated by the equation:”
- **`Formula of ionic compounds - IGCSE Chemistry Revision Notes`** — missing: `../../assets/~5RmSBVa_copperii-chloride-swap-and-drop.png`
  - 4CH1-1.39 [high] (textual evidence) — evidence: “The formula of an ionic compound can be determined by directly comparing the charges of t…”
- **`Fractional distillation - IGCSE Chemistry Revision Notes`** — missing: `../../assets/Fractional-Distillation.png`
  - 4CH1-4.7 [high] (textual evidence) — evidence: “the different hydrocarbons that make up the mixture, called fractions”
  - 4CH1-4.8 [high] (**leans on visuals**) — evidence: “The fractions in petroleum are separated from each other in a process called fractional d…”
  - 4CH1-4.9 [high] (textual evidence) — evidence: “Refinery gas \| Domestic heating & cooking”
  - 4CH1-4.10 [high] (textual evidence) — evidence: “darker as it gets thicker and more viscous”

## 7. Pass criteria and what follows

The PR review passes when every mapping in this guide is either **confirmed** (promoted to HUMAN_VALIDATED via the §0.3 protocol — `scripts/c10_promote.py` batches it) or **rejected-and-reworked** (decisions edit + gated re-run, §0.4), and the gate suite is green afterwards (`graph_check.py` 9/9, `c10_negative_test.py` 10 classes + positive control, applier ALL GREEN). Then T-C11 (Phase 3 concept/prerequisite/misconception graph) legitimately begins — see `TODO.md`.

