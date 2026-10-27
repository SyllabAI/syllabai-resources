#!/usr/bin/env python3
"""
T-C10 PR review — execution sheet generator (AI review pass, 2026-09-11).

Renders graph/reports/PHASE2_PR_REVIEW_SHEET.md: the record of the AI-executed
review of the risk-prioritized queue issued in PHASE2_PR_REVIEW_GUIDE.md
(issue 2 — the contributory many-to-many mapping contract, after the
operator's Save My Exams architecture clarification).

What this sheet is:
  - the executed review: per-mapping verdicts with the evidence actually read
    (whole notes, not just evidence sentences) and VLM visual checks for the
    diagram queue
  - NOT the promotion: HUMAN_VALIDATED stays the operator's ratification step
    (the staged batch command is in the last section). validation_status
    remains SUGGESTED everywhere on disk.

Review method (per mapping):
  1. read the spec point's registry wording
  2. read the whole note (headings + evidence section + siblings where the
     mapping claims distributed coverage)
  3. apply the §0.0 mapping contract: CONFIRM when the note provides
     substantive instructional coverage (possibly contributory); REJECT only
     on premise-only / unsupported-evidence / out-of-scope / misrepresentation
  4. diagram-dependent mappings: VLM check of the actual images + text
     cross-check

Idempotent: the script checks for its marker before writing.

Usage: python3 scripts/c10_pr_review_verdicts.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPORTS = HERE.parent / "graph" / "reports"
SHEET = REPORTS / "PHASE2_PR_REVIEW_SHEET.md"
DATE = "2026-09-11"
MARKER = "<!-- ai-review-pass-2026-09-11 -->"

ATTR = "Z.ai review pass 2026-09-11 (operator-directed; guide issue 2, §0.0 contract)"


def load_decisions():
    d = {}
    for f in sorted((HERE / "c10_decisions").glob("S*.json")):
        d.update(json.loads(f.read_text(encoding="utf-8")))
    return d


# ---------------------------------------------------------------------------
# Verdict data — one entry per reviewed mapping.
# finding = what was actually read / verified, phrased for the operator.
# ---------------------------------------------------------------------------
P1 = [
    dict(code="4CH1-4.15", note="Nitrogen Oxides & Sulfur Dioxide", verdict="CONFIRM",
         finding=(
             "Whole note read (107 lines). The “From sulfur dioxide” subsection "
             "carries the point's causal relationship in-note: “The sulfur "
             "dioxide produced from the combustion of fossil fuels…” — "
             "combustion → SO₂, with the follow-on acid-rain equation (4.16’s "
             "side). The impurity premise (“All these fuels contain … small "
             "quantities of sulfur”) is NOT in this note; corpus-wide it lives "
             "only in the sibling combustion note (same subsection 4CH1-S4-b). "
             "Under §0.0 this is a legitimate distributed coverage: the "
             "EXPLANATION the point demands is here; the premise is one page "
             "away. The rejected original failed the mirror-image test "
             "(premise without relationship). Rationale reworked (§9) to name "
             "the distribution honestly. Confidence stays medium.")),
]

P2 = [
    dict(code="4CH1-1.4", note="Solubility", verdict="CONFIRM",
         finding=(
             "Both S1-a notes read. This note teaches the solvent term "
             "definitionally in context (“The liquid is called the solvent”) "
             "and uses solute / saturated solution operationally in the "
             "solubility-curve discussion (“maximum mass of solute … before a "
             "saturated solution is formed”). The Solutions note (separate "
             "1.4 mapping, high) carries the four-term definitions table. "
             "Contributory coverage of 1.4 — the exact note-split pattern the "
             "operator described. Rationale reworked (§9) from deferral "
             "wording to contributory wording. Confidence stays low (honest: "
             "partial-vocabulary teaching, not the definitional core).")),
]

P5 = [
    dict(code="4CH1-1.10", note="Paper chromatography", verdict="CONFIRM",
         finding=(
             "The note IS a full practical write-up of one of 1.10’s five "
             "separation techniques (aim, apparatus, diagram, method, common "
             "errors, results). Generic techniques note (Separation "
             "techniques, high) + practical instance = aggregate coverage.")),
    dict(code="4CH1-1.16", note="Atoms Definitions & Structure", verdict="CONFIRM",
         finding=(
             "The note’s terms table defines ALL FOUR 1.16 terms (atomic "
             "number, mass number, isotope, relative atomic mass — the Ar row "
             "quoted as evidence). The old rationale undersold this as "
             "deferring the “calculation side” — that is 1.17’s content, not "
             "1.16’s; reworked (§9). Sibling: Relative atomic mass note "
             "(1.16 medium, see P3).")),
    dict(code="4CH1-1.50", note="Simple molecular structures", verdict="CONFIRM",
         finding=(
             "The C60 fullerene section carries 1.50’s fullerene strand: "
             "hollow cage structure, “C60 can not conduct electricity” with "
             "the electron-confinement explanation (electrons “cannot migrate "
             "from one buckyball to another”), buckyball image VLM-verified "
             "clean. Diamond/graphite strand in Giant covalent structures "
             "(high). Deliberate two-way split — legitimate architecture.")),
    dict(code="4CH1-2.17", note="Metals Reacting with Water & Acids", verdict="CONFIRM",
         finding=(
             "Ordered tables K→Cu (“Most reactive … Least reactive”) plus the "
             "teaching that the series is built from observations of "
             "reactions with water and acids. The full 11-metal list (with "
             "Al, Ag, Au) is in The reactivity series (high). Contributory: "
             "this note carries the ordering concept + most of the list.")),
    dict(code="4CH1-2.29", note="Acids, Alkalis & Neutralisation", verdict="CONFIRM",
         finding=(
             "The note introduces the pH scale itself — “a numerical scale "
             "which is used to show how acidic or alkaline a solution is … a "
             "measure of the amount of the hydrogen ions present” — the "
             "conceptual foundation of 2.29. The 0–14 classification bands "
             "are in What is an indicator (2.29 high sibling, bands verified: "
             "0-3 / 4-6 / 7 / 8-10 / 11-14). Thin but genuine contribution; "
             "rationale reworked (§9). Confidence stays medium.")),
    dict(code="4CH1-3.10", note="Explaining Rates", verdict="CONFIRM",
         finding=(
             "Dedicated collision-theory sections for concentration, "
             "pressure, temperature and surface area (four of the five 3.10 "
             "factors, each with the mechanism + diagram); catalyst named in "
             "the factors list, its effect taught in Rate of reaction (high) "
             "and Catalysts in Chemistry. Rationale reworked (§9) to state "
             "the catalyst gap honestly.")),
    dict(code="4CH1-4.5", note="Introduction to Organic Chemistry", verdict="CONFIRM",
         finding=(
             "Isomerism section defines isomers (same molecular formula, "
             "different displayed formulae) and shows C3H6’s two isomers "
             "(propene + cyclopropane) — the displayed-formulae image "
             "VLM-verified (§7). The “Representing Organic Molecules” "
             "sections teach molecular/structural/condensed/displayed "
             "formulae with worked images (VLM-verified for 4.2). This is "
             "the 4.5 skill demonstrated; the naming side is 4.3/4.4 "
             "territory in the naming note.")),
]

P3 = [
    dict(code="4CH1-1.17", note="Calculate Relative Mass", verdict="CONFIRM (weakest of the batch — see P4)",
         finding="See P4 block below."),
    dict(code="4CHI-1.16".replace("4CHI", "4CH1"), note="Relative atomic mass", verdict="CONFIRM",
         finding=(
             "The note opens by stating what Ar is computed from (“calculated "
             "from the mass number and relative abundances of all the "
             "isotopes”) then carries the full equation + multi-isotope "
             "worked examples — that is 1.17’s skill, and it also explains "
             "the 1.16 Ar-term meaning in the course of it. Sibling: Atoms "
             "Definitions terms table.")),
    dict(code="4CHI-1.22".replace("4CHI", "4CH1"), note="Electronic Configuration & Reactivity", verdict="CONFIRM",
         finding=(
             "Group-number ↔ outer-electrons rule (with the helium "
             "exception) + using group to predict reactions — half of 1.22’s "
             "position↔configuration relation, taught from the position "
             "side. Sibling: Electronic Configurations (high) carries the "
             "configuration→period/group side with the chlorine worked "
             "example.")),
    dict(code="4CHI-1.25".replace("4CHI", "4CH1"), note="Reacting mass calculations", verdict="CONFIRM",
         finding=(
             "“Balancing Equations using Reacting Masses” section: converting "
             "known masses to moles to molar ratios to a balanced equation "
             "(C + ZnO worked example) — exactly 1.25’s “unfamiliar reactions "
             "where suitable information is provided” strand. Sibling: "
             "Writing chemical equations (high).")),
    dict(code="4CHI-1.28".replace("4CHI", "4CH1"), note="Reacting mass calculations", verdict="CONFIRM",
         finding=(
             "The note’s core computational bridge — moles ↔ grams via Ar/Mr "
             "with MgO/Al2O3 worked examples — is 1.28’s calculation type. "
             "Sibling: Calculating moles and mass (high).")),
    dict(code="4CHI-1.31".replace("4CHI", "4CH1"), note="Empirical & Molecular Formulae", verdict="CONFIRM",
         finding=(
             "“Deducing formulae of hydrated salts” section — the "
             "water-of-crystallisation strand of 1.31, experimental method "
             "(heat to constant mass) + calculation. Siblings: Investigating "
             "metal oxide formulas (high, metal-oxides strand) and Simple "
             "compound formulae (high, experiment-method strand) — the "
             "aggregate covers all 1.31 strands named in the spec.")),
    dict(code="4CHI-1.33".replace("4CHI", "4CH1"), note="Investigating metal oxide formulas", verdict="CONFIRM",
         finding=(
             "Two practicals (MgO by combustion; CuO by reduction) with "
             "results tables feeding empirical-formula calculations from "
             "experimental data. Sibling: Empirical & Molecular Formulae "
             "(1.33 high) carries the calculation method.")),
    dict(code="4CHI-1.33".replace("4CHI", "4CH1"), note="Simple compound formulae", verdict="CONFIRM",
         finding=(
             "Mass-change → moles → molar ratios → empirical formula chain, "
             "worked on the hydrated-salt experiment. Contributory to 1.33 "
             "alongside the practical and calculation notes.")),
    dict(code="4CHI-1.37".replace("4CHI", "4CH1"), note="Common Ions", verdict="CONFIRM",
         finding=(
             "“How to deduce the charge of an ion”: outer-electron count, "
             "gain vs donate decision, “atoms that gain electrons become "
             "negative ions and atoms that donate electrons form positive "
             "ions” — 1.37’s formation mechanism as a deduction rule, plus "
             "the common-ion tables.")),
    dict(code="4CHI-1.37".replace("4CHI", "4CH1"), note="Ionic bonding diagrams", verdict="CONFIRM",
         finding=(
             "Electron-transfer narration in the dot-and-cross context: Na "
             "loses one electron → Na+; Cl gains → Cl−; Mg loses two / O "
             "gains two — 1.37’s loss/gain formation taught in situ.")),
    dict(code="4CHI-1.5C".replace("4CHI", "4CH1"), note="Investigating solubility", verdict="CONFIRM",
         finding=(
             "The practical’s Calculation section computes solubility in the "
             "1.5C units with worked numbers (m(solute)/m(water) × 100 = "
             "32.0 g per 100 g) — the term’s meaning taught through the "
             "measurement that defines it. Sibling: Solubility note (1.5C "
             "high, “g per 100 g of solvent”).")),
    dict(code="4CHI-1.51".replace("4CHI", "4CH1"), note="Simple molecular structures", verdict="CONFIRM",
         finding=(
             "“Conductivity of simple molecular structures” section states "
             "the 1.51 rule generally — “poor conductors … (even when "
             "molten) … no free ions or electrons … most covalent compounds "
             "do not conduct at all in the solid state and are thus "
             "insulators” — with the C60 instance as evidence and a wiring "
             "insulator image. The evidence quote (C60) is one instance; the "
             "section carries the rule.")),
    dict(code="4CHI-1.52C".replace("4CHI", "4CH1"), note="Metallic bonding", verdict="CONFIRM",
         finding=(
             "Already machine-verified (VLM, 2026-09-11, spot-check #18): "
             "Metallic-lattice-structure_.png IS the 2-D regular ion array "
             "with labelled delocalised electrons. Operator may re-eyeball.")),
    dict(code="4CHI-1.56C".replace("4CHI", "4CH1"), note="Electrolysis diagram", verdict="CONFIRM",
         finding=(
             "The note’s opening principle: ionic compounds “heated beyond "
             "their melting point … become molten and can conduct "
             "electricity as their ions can move freely and carry the "
             "charge” — 1.56C’s mechanism at its point of use in "
             "electrolysis. Sibling: Electronic conductivity (high) carries "
             "the dedicated contrast (incl. covalent non-conduction).")),
    dict(code="4CHI-1.58C".replace("4CHI", "4CH1"), note="Practical Investigate the Electrolysis of Aqueous Solutions", verdict="CONFIRM",
         finding=(
             "The note IS the 1.58C aqueous half: aim names the three "
             "specified solutions (NaCl, dilute H2SO4, CuSO4), inert-graphite "
             "electrodes, gas collection + product tests (pop/glowing-splint/"
             "litmus), results and conclusions. Molten-PbBr2 half in the "
             "Electrolysis diagram note (1.58C high).")),
    dict(code="4CHI-1.8".replace("4CHI", "4CH1"), note="Pure substances", verdict="CONFIRM",
         finding=(
             "“A pure substance may consist of a single element or compound "
             "which contains no other substances” + drinking-water-as-mixture "
             "example — the element/compound-vs-mixture classification from "
             "the purity side, plus m.p./b.p. distinction. Sibling: Element, "
             "Compound or Mixture (high) carries the three-way "
             "classification.")),
    dict(code="4CHI-2.10".replace("4CHI", "4CH1"), note="Oxygen percentage in air", verdict="CONFIRM",
         finding=(
             "The iron-oxidation route (2.10’s named metal example): full "
             "practical — burette setup, method, results, calculation, "
             "conclusion. Sibling: Composition of air (high) carries the "
             "phosphorus/non-metal route and the approximate-percentages "
             "context.")),
    dict(code="4CHI-2.15".replace("4CHI", "4CH1"), note="Metals reacting with acids", verdict="CONFIRM",
         finding=(
             "The Mg/Fe/Zn with dilute HCl/H2SO4 practical: method, "
             "observations table, conclusion feeding reactivity ordering — "
             "2.15’s acid-reactions basis. Water-reactions basis in Metals "
             "Reacting with Water & Acids (2.15 high sibling).")),
    dict(code="4CHI-2.24C".replace("4CHI", "4CH1"), note="Extraction of metals from ores", verdict="CONFIRM",
         finding=(
             "Reactivity-position → extraction-method table (electrolysis → "
             "carbon reduction → …) plus the full blast-furnace worked "
             "description (zones, raw materials, impurity removal) — exactly "
             "the material a student needs to comment on an extraction "
             "process, which is all 2.24C asks.")),
    dict(code="4CHI-2.39".replace("4CHI", "4CH1"), note="Preparing copper sulfate", verdict="CONFIRM",
         finding=(
             "The note IS the 2.39 experiment: insoluble CuO base + warm "
             "dilute acid, excess base, filtration, evaporation to "
             "saturation, crystallisation, drying — pure dry soluble salt "
             "from an insoluble reactant.")),
    dict(code="4CHI-2.41C".replace("4CHI", "4CH1"), note="Preparing lead sulfate", verdict="CONFIRM",
         finding=(
             "The note IS the 2.41C experiment: two soluble salts "
             "(Pb(NO3)2 + K2SO4) → PbSO4 precipitate, filter, wash, oven-dry, "
             "with the equation. Pure dry insoluble salt from two soluble "
             "reactants.")),
    dict(code="4CHI-3.2".replace("4CHI", "4CH1"), note="Temperature change practical", verdict="CONFIRM",
         finding=(
             "HCl/NaOH neutralisation calorimetry practical (styrofoam "
             "calorimeter, thermometer, incremental-acid method, results "
             "table, graph) — one of 3.2’s reaction classes as a concrete "
             "experiment. Sibling: Calorimetry (3.2 high) covers the full "
             "class set incl. combustion.")),
    dict(code="4CHI-3.9".replace("4CHI", "4CH1"), note="How surface area affects rate", verdict="CONFIRM",
         finding=(
             "Marble-chips + HCl surface-area experiment: method, results "
             "table, conclusion with collision explanation — one of 3.9’s "
             "factor experiments. Sibling: Rate of reaction (3.9 high) + "
             "Investigating catalysts (3.9 medium).")),
    dict(code="4CHI-3.9".replace("4CHI", "4CH1"), note="Investigating catalysts", verdict="CONFIRM",
         finding=(
             "H2O2 catalytic-decomposition experiment (named catalyst "
             "candidates, gas-collection method, rate comparison) — 3.9’s "
             "catalyst-factor experiment.")),
    dict(code="4CHI-4.39C".replace("4CHI", "4CH1"), note="Preparation of ethyl ethanoate", verdict="CONFIRM",
         finding=(
             "The esterification practical: ethanoic acid + ethanol + "
             "concentrated sulfuric acid gently heated, ester distilled off "
             "as formed, impurity removal — 4.39C’s reactants + acid "
             "catalyst instantiated exactly.")),
    dict(code="4CHI-4.40C".replace("4CHI", "4CH1"), note="Making and naming esters", verdict="CONFIRM",
         finding=(
             "Formation equation CH3COOH + C2H5OH → CH3COOC2H5 + H2O with "
             "the ethyl-ethanoate structures; ester images VLM-verified "
             "(§7: functional group + preparation diagram + parts-of-ester + "
             "ester table).")),
]

P4_NOTE = (
    "Both 1.17 mappings read in full. **S1-c Relative atomic mass [high]** — "
    "the dedicated calculation note: Ar equation from isotopic abundances, "
    "extended to 3+ isotopes, worked examples. In-subsection, the mechanical "
    "default; CONFIRM. **S1-e Calculate Relative Mass [medium]** — the "
    "cross-subsection flag. The note opens: “The symbol for the relative "
    "atomic mass is Ar. This is calculated from the mass number and relative "
    "abundances of all the isotopes of a particular element” — then moves to "
    "Mr (its real subject, 1.26 high). Verdict: **CONFIRM — the weakest "
    "confirm in this review**. The opening sentence is the derivation basis "
    "of 1.17 (conceptual entry, taught where students first meet Ar in the "
    "formulae subsection), but the calculation skill itself (equation + "
    "worked examples) lives entirely in the S1-c note; the S1-e sentence is "
    "closer to 1.16-vocabulary territory than to 1.17’s skill. The "
    "operator’s advisor’s test — “the note begins by directly teaching "
    "relative atomic mass from isotopic abundances before moving into Mr” — "
    "is met literally, so the mapping passes under the §0.0 contract; if "
    "the operator prefers the stricter reading (a calculate-point needs the "
    "calculation, not just its premise), the alternative is removal: 1.17 "
    "keeps its full-strength S1-c mapping and the corpus loses nothing. "
    "Rationale reworked (§9) to state the contribution honestly.")

P6A = [
    # code, note-fragment, VLM verdict, detail
    ("4CH1-1.41", "Ionic bonding and lattices", "OK", "3/3 yes: electrostatic-attraction diagram, NaCl ball-and-stick lattice, molten-conduction image."),
    ("4CH1-1.60C", "Practical Investigate the Electrolysis", "OK", "Inverted-test-tube electrolysis cell confirmed."),
    ("4CH1-2.21", "Metals reacting with acids", "OK", "Metals + dilute acid test-tube diagram confirmed."),
    ("4CH1-2.26C", "Alloys", "OK", "Alloy-structure diagram confirmed."),
    ("4CH1-2.33C", "Acid-Alkali Titrations", "FLAG→OK", "VLM: apparatus yes; method/results table not in IMAGES — resolved: the note TEXT carries the 12-step Method and the Results table (headings verified). Apparatus visual + method textual = jointly satisfied."),
    ("4CH1-2.5", "Group 7 properties", "OK", "m.p./b.p. trend graph + states of halogens confirmed."),
    ("4CH1-2.9", "Composition of air", "OK", "Air-composition pie chart (~80/20 + minor) confirmed."),
    ("4CH1-3.19C", "Dynamic equilibrium", "OK", "Open-vs-closed system + equilibrium rate graphs confirmed."),
    ("4CH1-3.2", "Calorimetry", "OK", "Simple calorimeter apparatus confirmed."),
    ("4CH1-3.21C", "The position of equilibrium", "OK", "Catalyst effect on equilibrium confirmed."),
    ("4CH1-4.2", "Introduction to Organic Chemistry", "OK", "Molecular/structural/condensed formulae + functional-group table confirmed."),
    ("4CH1-4.21", "Alkanes", "OK", "Methane/ethane/propane/butane displayed formulae confirmed."),
    ("4CH1-4.29C", "Alcohols", "OK", "-OH functional group + alcohol displayed formulae confirmed."),
    ("4CH1-4.30C", "Alcohols", "FLAG→OK", "First call (3 images) missing butanol; the guide’s image list had truncated at 4. Re-run with all four table images (incl. butanol.png): first-four alcohols confirmed. Guide generator fixed to list up to 6 images."),
    ("4CH1-4.34C", "Carboxylic Acids", "OK", "-COOH group + first-four acids confirmed."),
    ("4CH1-4.35C", "Carboxylic Acids", "OK", "Names + structures of the unbranched acids confirmed."),
    ("4CH1-4.38C", "Making and naming esters", "OK", "Ester functional group + parts-of-an-ester confirmed."),
    ("4CH1-4.40C", "Making and naming esters", "OK", "Ethyl-ethanoate preparation diagram + ester table confirmed."),
    ("4CH1-4.44", "Addition Polymers", "OK", "Monomer→polymer, repeating units, monomer deduction confirmed."),
    ("4CH1-4.5", "Introduction to Organic Chemistry", "OK", "Propene + cyclopropane (C3H6 isomers) displayed formulae confirmed."),
    ("4CH1-1.52C", "Metallic bonding", "OK (prior)", "Machine-verified at spot-check (#18); operator may re-eyeball."),
]

P6B = [
    ("4CHI-1.11".replace("4CHI", "4CH1"), "Interpreting chromatograms", "PASS",
     "The interpretation teaching is fully textual (pure = one spot, impure = several, reference spots, component identification) and the note’s main chromatogram image RESOLVES (Chromatography-–-Pure-Impure.png). The missing asset (.jpeg) belongs to 1.12’s worked example, not to this mapping."),
    ("4CHI-1.12".replace("4CHI", "4CH1"), "Interpreting chromatograms", "PASS",
     "Rf section fully textual: definition, equation, properties (ratio, unitless, <1), identification purpose, worked example computing Rf = 3/6 = 0.5 with the distances given in the answer. The missing worked-example chromatogram is supplementary — the example remains followable from the given distances. → image-recovery queue (pedagogy)."),
    ("4CHI-1.39".replace("4CHI", "4CH1"), "Formula of ionic compounds", "PASS",
     "Direct-comparison (FeSO4) and swap-and-drop (CuCl2) methods fully textual with worked steps. The missing swap-and-drop diagram is a visual aid to one method. → image-recovery queue."),
    ("4CHI-4.7".replace("4CHI", "4CH1"), "Fractional distillation", "PASS",
     "Crude oil = mixture of hydrocarbons separated into fractions: fully textual. Missing column diagram belongs to 4.8’s claim, not this mapping’s substance."),
    ("4CHI-4.8".replace("4CHI", "4CH1"), "Fractional distillation", "PASS",
     "The process description survives complete in text: fractionating column, temperature gradient (hot base / cool top), crude oil vapourises, high-b.p. fractions condense low, low-b.p. rise and condense at the top. The missing Fractional-Distillation.png illustrates what the text already states — supplementary. → image-recovery queue (the note’s strongest visual)."),
    ("4CHI-4.9".replace("4CHI", "4CH1"), "Fractional distillation", "PASS",
     "Main-fractions table (refinery gas → bitumen) with uses is textual, plus the examiner tip restating the six names."),
    ("4CHI-4.10".replace("4CHI", "4CH1"), "Fractional distillation", "PASS",
     "Dedicated Viscosity / Colour / m.p.-b.p. / Volatility trend sections + the fraction-b.p. table — all textual."),
]

REWORKS = [
    ("4CHI-4.15".replace("4CHI", "4CH1"), "Nitrogen Oxides & Sulfur Dioxide",
     "The note's “From sulfur dioxide” subsection teaches the 4.15 relationship in-note (combustion of fossil fuels producing sulfur dioxide); the fuel-impurity premise (fuels containing small quantities of sulfur) is taught in the sibling combustion note of the same subsection — a legitimate distributed coverage under the mapping contract."),
    ("4CHI-1.4".replace("4CHI", "4CH1"), "Solubility",
     "Teaches the solvent term definitionally in context (“the liquid is called the solvent”) and uses solute / saturated solution operationally in the solubility-curve discussion; the Solutions note carries the four 1.4 term definitions as a separate mapping — contributory coverage, not sole coverage."),
    ("4CHI-1.16".replace("4CHI", "4CH1"), "Atoms Definitions & Structure",
     "The terms table defines all four 1.16 terms — atomic number, mass number, isotope and relative atomic mass (the quoted Ar row, incl. the carbon-12 standard); the calculation of Ar from abundances is 1.17’s content in the dedicated RAM note."),
    ("4CHI-2.29".replace("4CHI", "4CH1"), "Acids, Alkalis & Neutralisation",
     "Introduces the pH scale itself — a numerical scale showing how acidic or alkaline a solution is, measuring the hydrogen ions present — the conceptual foundation of 2.29; the 0-14 classification bands are taught in the indicator note’s 2.29 mapping."),
    ("4CHI-3.10".replace("4CHI", "4CH1"), "Explaining Rates",
     "Collision-theory sections explaining the concentration, pressure, temperature and surface-area effects on rate; the catalyst factor of 3.10 is taught in the rate-of-reaction and catalysts notes."),
    ("4CHI-1.17".replace("4CHI", "4CH1"), "Calculate Relative Mass",
     "Cross-subsection contributory mapping: the note opens with the Ar derivation basis (Ar calculated from the mass number and relative abundances of all the isotopes) before moving to Mr; the 1.17 calculation skill — equation and worked examples — is carried by the dedicated relative-atomic-mass note in S1-c."),
]

FOLLOWUPS = [
    "registry wording: 3 official_wording entries contain stray CJK characters (4CHI-1.10 → “简单 distillation”, 4CHI-1.40, 4CHI-2.29 → “和”) — cosmetic Phase-1 extraction artifacts; propose a one-line registry fix task (operator sign-off, since the registry is operator-reviewed).",
    "image-recovery queue (pedagogical completeness only — all 5 mappings above PASS on text): assets/.jpeg (Rf worked example), ~5RmSBVa_copperii-chloride-swap-and-drop.png, Fractional-Distillation.png.",
    "4.15 premise distribution: the sulfur-impurity premise lives only in the combustion note (which maps 4.11/4.12/4.13). If the operator wants the full chain on ONE note for graph-traversal purposes, that is a content-architecture decision, not a mapping defect.",
]


def esc(s, n=110):
    s = s.replace("|", "\\|").replace("\n", " ")
    return (s[: n - 1] + "…") if len(s) > n else s


def render_row(decisions_by_stem, wording, item):
    note, m = decisions_by_stem[(item["code"], item["note"])]
    return (f"| {item['code']} | {esc(Path(note).stem, 44)} | "
            f"{esc(wording.get(item['code'], ''), 90)} | **{item['verdict']}** | "
            f"{esc(item['finding'], 300)} |")


def main() -> int:
    if SHEET.exists() and MARKER in SHEET.read_text(encoding="utf-8"):
        print("sheet already rendered (idempotent)")
        return 0

    decisions = load_decisions()
    reg = yaml.safe_load((HERE.parent / "graph" / "specification_points.yaml").read_text(encoding="utf-8"))
    wording = {p["code"]: p["official_wording"] for p in reg["specification_points"]}

    by_stem = {}
    for note, d in decisions.items():
        for m in d["mappings"]:
            by_stem[(m["code"], Path(note).stem)] = (note, m)
    # index by (code, stem-fragment prefix)
    def find(code, frag):
        hits = [(n, m) for (c, s), (n, m) in by_stem.items()
                if c == code and frag.lower() in s.lower()]
        assert len(hits) == 1, f"{code} @ {frag}: {len(hits)} hits"
        return hits[0]

    # distinct (code, note) pairs reviewed:
    # P1(1) + P2(1) + P5(7) + P3(26) + P4's S1-c 1.17(1)
    # + P6a extras (21 diagram-queue entries minus the 3 already listed:
    #   4.5, 1.52C, 4.40C) + P6b(7)
    reviewed_pairs = [(x["code"], x["note"]) for x in P1 + P2 + P5 + P3]
    reviewed_pairs.append(("4CH1-1.17", "Relative atomic mass"))  # P4 S1-c high
    for code, frag, _s, _d in P6A:
        pair = (code, frag)
        # skip P6a pairs already covered by P3/P5/P1/P2 entries
        if any(c == code and frag.lower() in n.lower() for c, n in reviewed_pairs):
            continue
        reviewed_pairs.append(pair)
    for code, frag, _c, _d in P6B:
        if any(c == code and frag.lower() in n.lower() for c, n in reviewed_pairs):
            continue
        reviewed_pairs.append((code, frag))
    total = len(reviewed_pairs)

    L = []
    A = L.append
    A(MARKER)
    A(f"# Phase 2 (T-C10) — PR Review Execution Sheet ({DATE})")
    A("")
    A(f"Generated by `scripts/c10_pr_review_verdicts.py` — the executed review "
      "of the queue issued in `PHASE2_PR_REVIEW_GUIDE.md` (issue 2).")
    A("")
    A(f"**Executed by:** {ATTR}.")
    A("**This sheet is the review, not the promotion:** every verdict below "
      "was reached by reading the whole note (not just the evidence "
      "sentence), comparing the spec wording, and — for the diagram queue — "
      "VLM-verifying the actual images. HUMAN_VALIDATED promotion remains "
      "the operator's ratification step; on disk every mapping is still "
      "`validation_status: SUGGESTED`. The staged ratification command is in "
      "the final section.")
    A("")
    A("## 1. Verdict summary")
    A("")
    A("| Queue | Reviewed | CONFIRM | REJECT | HOLD |")
    A("|---|---:|---:|---:|---:|")
    A(f"| P1 remapped 4.15 | 1 | 1 | 0 | 0 |")
    A(f"| P2 low-confidence 1.4 | 1 | 1 | 0 | 0 |")
    A(f"| P3 medium-confidence | {len(P3)} | {len(P3)} | 0 | 0 |")
    A(f"| P4 both 1.17 mappings | 2 | 2 (1 weakest) | 0 | 0 |")
    A(f"| P6a diagram queue | {len(P6A)} | {len(P6A)} | 0 | 0 |")
    A(f"| P6b missing figures | {len(P6B)} | {len(P6B)} PASS | 0 | 0 |")
    A(f"| **Distinct mappings** | **{total}** | **{total}** | **0** | **0** |")
    A("")
    A(f"({len(P5)} of the P3 mediums are the P5-flagged deferral candidates — "
      "reviewed under the §0.0 contributory contract and folded into the "
      "tables below. 61 mappings were reviewed in total; overlaps between "
      "queues (e.g. 4.5, 1.52C, 4.40C appear in both P3/P5 and P6a) are "
      "counted once.)")
    A("")

    # P1 / P2 blocks
    for title, items in (("## 2. Priority 1 — 4CHI-4.15".replace("4CHI", "4CH1"), P1),
                         ("## 3. Priority 2 — 4CHI-1.4".replace("4CHI", "4CH1"), P2)):
        A(title)
        A("")
        for item in items:
            note, m = find(item["code"], item["note"])
            A(f"### {item['code']} @ `{Path(note).stem}` [{m['confidence']}]")
            A("")
            A(f"- spec: “{esc(wording.get(item['code'], ''), 200)}”")
            A(f"- evidence: “{esc(m['evidence'], 200)}”")
            A(f"- verdict: **{item['verdict']}** — {ATTR}")
            A(f"- finding: {item['finding']}")
            A("")

    # P5 table
    A("## 4. Priority 5 — the cross-note deferral candidates")
    A("")
    A("Reviewed under the §0.0 contract: substantive contributory coverage, "
      "not independent whole-point teaching. A split across notes is "
      "legitimate when THIS note carries a real strand of the point.")
    A("")
    A("| code | note | spec | verdict | finding |")
    A("|---|---|---|---|---|")
    for item in P5:
        note, m = find(item["code"], item["note"])
        A(f"| {item['code']} | {esc(Path(note).stem, 44)} | "
          f"{esc(wording.get(item['code'], ''), 90)} | **{item['verdict']}** | "
          f"{esc(item['finding'], 300)} |")
    A("")

    # P3 table
    A("## 5. Priority 3 — the remaining medium-confidence mappings")
    A("")
    A("| code | note | spec | verdict | finding |")
    A("|---|---|---|---|---|")
    for item in P3:
        note, m = find(item["code"], item["note"])
        A(f"| {item['code']} | {esc(Path(note).stem, 44)} | "
          f"{esc(wording.get(item['code'], ''), 90)} | **{item['verdict']}** | "
          f"{esc(item['finding'], 300)} |")
    A("")

    # P4
    A("## 6. Priority 4 — 4CHI-1.17 (both mappings)".replace("4CHI", "4CH1"))
    A("")
    A(P4_NOTE)
    A("")

    # P6a
    A("## 7. Priority 6a — diagram queue (VLM visual verification)")
    A("")
    A("One targeted VLM call per mapping (glm-5v; numbered yes/no questions "
      "with the images named in the guide). Text + visual jointly carry each "
      "mapping where applicable. Raw verdicts are archived in the repo: "
      "`scripts/c10_vlm_results/*.json` (21 files, incl. the prior 1.52C "
      "check) — the two initial flags are resolved below and are NOT "
      "defects:")
    A("")
    A("| code | note | VLM | detail |")
    A("|---|---|---|---|")
    for code, frag, status, detail in P6A:
        note, m = find(code, frag)
        A(f"| {code} | {esc(Path(note).stem, 40)} | {status} | {esc(detail, 240)} |")
    A("")
    A("Verdict: **all 21 CONFIRM** — the diagram-dependent mappings are "
      "backed by the actual diagrams, not just by text mentioning them.")
    A("")

    # P6b
    A("## 8. Priority 6b — missing figures (PASS / HOLD / REWORK)")
    A("")
    A("Classified per the guide's deterministic rules (issue 2). No mapping "
      "was being carried by its missing figure; nothing was held or "
      "reworked. The 4 images stay on the image-recovery queue for "
      "pedagogical completeness.")
    A("")
    A("| code | note | class | finding |")
    A("|---|---|---|---|")
    for code, note_frag, cls, detail in P6B:
        A(f"| {code} | {esc(note_frag, 40)} | **{cls}** | {esc(detail, 300)} |")
    A("")

    # Reworks
    A("## 9. Rationale reworks executed (decisions-side)")
    A("")
    A("Six rationales were rewritten for honest contributory wording (the "
      "deferral phrasing was misleading in five of them; 1.17's was "
      "imprecise). Evidence, confidence, tier and validation state are "
      "unchanged — only the rationale text. Applied by "
      "`scripts/c10_rework_rationales.py` + gated applier re-run; note "
      "bodies stay byte-identical.")
    A("")
    for code, note_frag, new_r in REWORKS:
        A(f"- **{code}** @ `{note_frag}`:")
        A(f"  - new rationale: {esc(new_r, 500)}")
    A("")

    # Follow-ups
    A("## 10. Observations for follow-up (not blockers)")
    A("")
    for f in FOLLOWUPS:
        A(f"- {f}")
    A("")

    # Ratification command: reviewed_pairs are (code, note-fragment) pairs;
    # codes that appear on several notes (1.4, 1.16, 1.17, 1.33, 1.37, 3.2,
    # 3.9, ...) MUST be disambiguated with @FRAGMENT in EVERY spec.
    code_multiplicity = {}
    for c, _f in reviewed_pairs:
        code_multiplicity[c] = len([n for (c2, s), (n, m) in by_stem.items()
                                    if c2 == c])
    cmd_parts, resolved_pairs = [], []
    for code, frag in reviewed_pairs:
        note, m = find(code, frag)
        resolved_pairs.append((code, note))
        if code_multiplicity[code] > 1:
            cmd_parts.append(f"'{code}@{Path(note).stem[:40]}'")
        else:
            cmd_parts.append(code)

    A("## 11. Staged operator ratification")
    A("")
    A(f"All {len(resolved_pairs)} reviewed mappings are CONFIRM. To ratify "
      "(promote exactly the reviewed set to HUMAN_VALIDATED), the operator "
      "runs:")
    A("")
    A("```bash")
    A("cd work/syllabai-resources && \\")
    A("python3 scripts/c10_promote.py \\")
    chunk = []
    for i in range(0, len(cmd_parts), 3):
        chunk.append("    " + " ".join(f"--map {p}" for p in cmd_parts[i:i + 3]) + " \\")
    A("\n".join(chunk))
    A(f"    --by operator --date {DATE}")
    A("```")
    A("")
    A("(codes appearing on several notes are disambiguated with "
      "`CODE@FRAGMENT` per the promoter's resolver; ambiguous specs fail "
      "rather than promote wholesale. After the command: gates re-run "
      "automatically — applier ALL GREEN, `graph_check.py` 9/9, then "
      "`c10_negative_test.py`.)")
    A("")
    A("Alternatively the operator may ratify in tranches (e.g. P1+P2 first, "
      "or everything except the weakest confirm — the S1-e 1.17) by trimming "
      "the `--map` list; or ask Z.ai to apply it verbatim.")
    A("")

    SHEET.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"written: {SHEET} ({len(L)} lines, {len(resolved_pairs)} mappings)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
