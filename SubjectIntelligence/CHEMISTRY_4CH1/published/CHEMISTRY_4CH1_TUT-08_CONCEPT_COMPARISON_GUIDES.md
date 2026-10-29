---
sib_protocol: SIB-1.0
artifact_id: TUT-08
artifact_version: 1.3
subject: Chemistry
qualification: International GCSE
specification: 4CH1
curriculum_version: "2017"

research_family: tutor_intelligence
applicability: REQUIRED

temporal_scope:
  current: true
  legacy: false

source_scope:
  specification: false
  textbook: true
  question_papers: false
  mark_schemes: false
  examiner_reports: false
  supplementary: true

# lifecycle: GENERATED -> QA_PASSED -> STAGED
status: PUBLISHED
generated_by: zai_agent
generated_at: 2026-10-30

provenance:
  source_manifest: "SRC-BOOK-4CH1-SB1"
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-021"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "bc4740884"
    syllabai_resources: "7352d2eab0bc822a8273d8dadfbeaefe3faf45d2"
---

# TUT-08 — Concept Comparison Guides

## Purpose

This artifact captures how the 4CH1 evidence of record frames the course's
comparison pairs — the contrasts a tutor most often has to draw — and the
comparison traps each pair carries. Every claim is carried on a bounded,
locator-addressed excerpt from this artifact's own evidence pack; nothing is
asserted beyond the packs.

## Scope

**Covers:** mixture versus compound via fixed ratios; ionic versus covalent
bonding and the metal-nonmetal trap; saturated versus unsaturated; strong versus
weak versus concentrated; fermentation versus hydration as ethanol routes;
the group 1 reactivity comparison wording; and the molar-mass distinction.

**Out of scope:** misconception response sequences (TUT-06) and the deep
mechanistic explanations behind the contrasts (TUT-09).

## Executive Summary

The book and the board's topic guide teach comparisons by fixing the exact
contrast sentence: compounds combine "in fixed proportions" where mixtures do
not; ionic bonding is electrostatic attraction between oppositely charged ions
while covalent bonding shares pairs — with the board warning that metal-plus-
nonmetal does not decide the bond type; saturated means single C-C bonds only
"whereas" unsaturated means at least one double or triple; strong is about
complete dissociation, not concentration. Each contrast sentence is exam-bearing
wording, and the book's own hints show the comparative phrases examiners expect
when students compare reactions.

## Main Analysis

### TUT-043 — Compound versus mixture: fixed proportions are the dividing line

**Claim:** the book draws the compound-mixture contrast through fixed
combining ratios — hydrogen and fluorine "always combine to form hydrogen
fluoride, with formula HF, whereas magnesium and fluorine always combine to form
magnesium fluoride" — the ratio law being the discriminator a tutor should
anchor.
**Evidence:** the book states "Compounds are formed when two or more elements
chemically combine. The elements always combine in fixed proportions." with the
HF and MgF₂ examples (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 66). Temporal scope:
CURRENT — AUTHORITATIVE.

### TUT-044 — Ionic versus covalent bonding, and the metal-nonmetal trap the board names

**Claim:** the board's topic guide defines ionic bonding as "the electrostatic
force of attraction between oppositely charged ions" and warns that claiming
ionic bonding is always metal-plus-nonmetal is "another trap to avoid" —
aluminium chloride and beryllium oxide being covalent — the comparison trap a
tutor must inoculate against.
**Evidence:** the guide states "Ionic bonding is the electrostatic force of
attraction between oppositely charged ions." and "Another trap to avoid is to
state that ionic bonding is always the results of metals combining with
non-metals. Aluminium chloride and beryllium oxide are just two examples of
compounds that are covalent." (SRC-TL-4CH1,
teaching-and-learning-materials/Chemical-bonding---FINAL.pdf p6). Temporal
scope: CURRENT — AUTHORITATIVE.

### TUT-045 — Saturated versus unsaturated is a bond-count contrast with a fixed sentence form

**Claim:** the book's alkene teaching fixes the contrast sentence — saturated
means "single C-C bonds only whereas an unsaturated compound contains one or
more double or triple C-C bonds" — and the book's comparison hints model the
phrasing examiners expect when students compare reactions.
**Evidence:** the book states "A saturated compound contains single C-C bonds
only whereas an unsaturated compound contains one or more double or triple C-C
bonds." (SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl
line 961); the group 1 comparison hint instructs "you can say that it fizzes
more slowly, or the lithium moves around more slowly, or takes longer to
disappear." (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 419). Temporal scope:
CURRENT — AUTHORITATIVE.

### TUT-046 — Strong versus weak versus concentrated: the dissociation criterion, not degree

**Claim:** the book's extension work separates the strong-weak axis (extent of
dissociation) from the concentrated-dilute axis (amount per volume), explicitly
naming the student misconception that equates them — the comparison pair with
the largest documented error rate.
**Evidence:** the book states "Ethanoic acid is a weak acid, whereas the acids
we have met before, hydrochloric acid or sulfuric acid, are called strong
acids. Students can have the misconception that strong acids are equivalent to
concentrated acids. Whether an acid is strong or weak has, in fact, nothing to
do with its concentration. Strong acids dissociate completely into their
constituent ions in water" (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 1006). Temporal scope:
CURRENT — AUTHORITATIVE.

**Family seam (RUN-011):** the conceptual-distinctions treatment of this same
contrast — the book's own misconception warning plus the observable reaction-rate
consequence — lives in EXP-06 record EXP-045; both records ground on the same book
passage cited in their Evidence lines and are consistent by construction.

### TUT-047 — Two ethanol routes compared: fermentation limits versus hydration conditions

**Claim:** the book's ethanol teaching contrasts fermentation (killed above
about 15% alcohol, purified by distillation exploiting the boiling-point
difference) with ethene-plus-steam hydration (300 °C, 60-70 atmospheres,
phosphoric acid) — a process-comparison a tutor can tabulate from the book's
own numbers.
**Evidence:** the book states "Yeast is killed by more than about 15% of alcohol
in the mixture" and "This takes advantage of the difference in boiling point
between ethanol and water. Water boils at 100 °C whereas ethanol boils at78℃.",
then lists the hydration route's conditions as label/value lines — temperature
300℃, pressure 60-70 atmospheres, catalyst phosphoric acid (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 990). Temporal scope:
CURRENT — AUTHORITATIVE.

### TUT-048 — Vocabulary pairs the course keeps distinct: molar mass versus mass of one mole, and dot-and-cross convention

**Claim:** the book explicitly maintains fine distinctions — molar mass (g/mol)
versus mass of 1 mole (g), flagged as a beyond-the-exam refinement — and the
dot-and-cross convention (dots versus crosses mark origin, not identity), both
distinctions a tutor should preserve rather than blur.
**Evidence:** the extension work states "'molar mass' and 'mass of 1 mole' are
not exactly the same thing and have different units: molar mass has units of
g/mol and the mass of 1 mole has units of g." (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 161); on diagrams, "there is
absolutely no difference between them in reality. The dots and the crosses
simply show that the electrons have come from two different atoms."
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 270).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-082 — Coefficient versus subscript is taught as the book's own minimal pair: 2Cl against Cl2

**Claim:** The book teaches the notation distinction with a genuine minimal pair rather than a rule recital: a big number in front of a formula is a coefficient and counts whole units, a small subscript number counts atoms inside one unit, and the pair 2Cl versus Cl2 makes the difference visible — two separate atoms against one joined molecule. The counting consequences are then worked in both directions, including the bracket rule where the subscript distributes over everything inside. The tutor inherits a ready-made concept comparison whose two terms differ by exactly one line of notation, which is why the confusion it prevents is so costly.
**Evidence:** the distinction: "you must understand the difference between big numbers written in front of formulae (sometimes called coefficients), such as the 2 in 2HCl, and the smaller, subscript (slightly lower on the line) numbers, such as the 3 in CaCO3." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 137); the minimal pair: "Another chemical equation is 2Cl → Cl2. Here, 2CI represents 2 separate Cl atoms and Cl2 means that the atoms are joined together in a molecule." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 137); the bracket rule: "If you have brackets in a formula, the small number refers to everything inside the brackets." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 137).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-083 — The excess calculation is taught as a head-to-head answer comparison with a both-ways test

**Claim:** The book stages the limiting-reagent concept as a comparison between two candidate answers: the tempting 0.4 g route from the magnesium moles is set out honestly, declared not the correct answer, and then explained through the equation's own arithmetic — 0.2 mol of magnesium would need 0.4 mol of acid, and there was only 0.2 mol. The correct route is re-run from the acid, and the closing instruction generalises the method: try both numbers of moles in the equation and compare. The comparison structure is the pedagogy — the student sees precisely why one line of reasoning collapses and the other stands, instead of being handed a procedure.
**Evidence:** the honest staging: "We might be tempted to say that 0.2 mol Mg produces 0.2 mol H2(g) and the mass of H2 = 0.2 × 2 = 0.4 g. Unfortunately this is not the correct answer!" (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 227); the resolution and the generalisation: "Because we know that all the HCl reacts we can use the number of moles of HCl to work out how much H2 is produced." and "To deduce which substance is in excess we try both numbers of moles in the chemical equation and compare the numbers." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 227).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-084 — Same-reaction-different-rate is the comparison frame for the alkali metals, with a phrase kit and a flame discriminator

**Claim:** The Group 1 teaching is built as a controlled comparison: every group metal reacts with water in the same way to the same products, and the only moving part is how quickly — so the concept to compare across lithium, sodium and potassium is rate, not chemistry. The comparison is then equipped with the exact comparative phrases the exam rewards (fizzes more vigorously, moves around more quickly, disappears more quickly) and closed with a qualitative discriminator that no adverb grading reaches: potassium's hydrogen ignites, sodium's usually does not. The tutor therefore teaches the shared mechanism, the graded language, and the binary observation in one frame.
**Evidence:** the common mechanism: "All these metals react in the same way with water to produce a metal hydroxide and hydrogen:" with the rate frame: "The main difference between the reactions is how quickly they happen." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 416); the phrase kit: "Again, if you are asked to compare potassium with sodium use phrases such as:" followed by "'fizzes more vigorously'", "'moves around more quickly'" and "'disappears more quickly'" (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 420); the discriminator: "The key difference though is that with potassium the hydrogen bursts into flames but with sodium it usually does not." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 420).
Temporal scope: CURRENT — AUTHORITATIVE.
## Evidence / Source Basis

Primary evidence: SRC-BOOK-4CH1-SB1 (the parse v3 corpus — the compounds page,
molar-mass extension, group 1 reactions and comparison hints, alkene and
ethanol pages, and the weak-acid extension work). Supplementary: SRC-TL-4CH1
(the bonding topic guide's ionic-bonding and covalent-formation pages). SRC-SPEC-4CH1
(change-summary page) and SRC-ER-4CH1 (June 2019 1C report cover page) are held
as single-page identity-presence entries and consumed for no claim. All excerpts
are bounded with locators preserved; caps enforced by the pack builder.

## Limitations / Coverage Gaps

The pack window holds the 41 matches of the comparison query; comparison-rich
areas outside the matched vocabulary (e.g. the periodic-table group contrasts in
Unit 2 beyond group 1, the physical-property trends of the alkanes versus
alkenes) are not sampled here. The OCR layer's numeral quirks (e.g. temperature
readings in the ethanol chunk) are quoted only where the value reads cleanly.
The board's bonding guide is held at three pages; its full octet-critique is
TUT-06's territory. No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-008 (BL-008 pass 8) from this artifact's
evidence pack alone; validator of record tools/sib @ 357ace0a; claim QA binds
every citation to a pack excerpt. Research artifact — evidence-backed, not
canonical educational truth. Deepened under SIB-CHEMISTRY_4CH1-RUN-021 (D3 REQUIRED-core depth pass, tranche 5: TUT): +3 records (TUT-082..TUT-084), zero-append mining of the carried pack of record on the OCR text-of-record basis resolved by operator ruling (gate_resolution_sb1_ebook.json); every quote self-bound to raw excerpt text before the official gate; claim QA re-bound all citations.
