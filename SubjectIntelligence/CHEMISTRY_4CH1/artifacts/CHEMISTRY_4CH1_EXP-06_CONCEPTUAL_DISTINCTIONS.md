---
sib_protocol: SIB-1.0
artifact_id: EXP-06
artifact_version: 1.1
subject: Chemistry
qualification: International GCSE
specification: 4CH1
curriculum_version: "2017"

research_family: explanation_intelligence
applicability: REQUIRED

temporal_scope:
  current: true
  legacy: false

source_scope:
  specification: true
  textbook: true
  question_papers: false
  mark_schemes: false
  examiner_reports: false
  supplementary: true

status: GENERATED
generated_by: zai_agent
generated_at: 2026-10-27

provenance:
  source_manifest: "SRC-BOOK-4CH1-SB1"
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-011"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "2cb92fe5f56d22f1b231c129a7e0dbc27bf86007"
    syllabai_resources: "a7a34cd97cdff29ee698a86b171c7148bc5e29ed"
---

# EXP-06 — Conceptual Distinctions

## Purpose

This artifact draws the fine boundaries that separate look-alike chemistry words and
ideas in the 4CH1 course: the pairs and triads that candidates blend under exam
pressure and that examiners then flag. Each record states both sides of one boundary,
gives the test that separates them, and cites the book-of-record text that carries
each side — including, in the weak/strong versus concentrated case, the book's own
named warning against the classic misconception. The distinctions here are drawn
entirely inside the specification's vocabulary; nothing is sharpened beyond it.
This is a research artifact; it does not promote itself into canonical educational
truth (Subject Intelligence Build v1, §5).

## Scope

**Covers:** eight distinction records (EXP-041 … EXP-048): evaporation versus
boiling; the naming of gas-to-solid deposition; pure substances versus mixtures at
the thermometer; mass number versus relative atomic mass; strong versus weak versus
concentrated acids; corrosion versus rusting; heating-to-go-faster versus endothermic;
and constant versus equal concentrations at equilibrium.

**Does not cover:** the full explanations from which these boundaries are carved
(EXP-01), simple registers (EXP-02), depth extensions (EXP-03), route comparisons
(EXP-04), analogies (EXP-05), mechanism records (EXP-07), and why-question formats
(EXP-08). No legacy content entered any pack.

## Executive Summary

- Eight boundary records, each carried on 2–4 book chunks; 18 chunks / 15,983
  bounded chars in this pack; spec pages 17, 18, 22, 27, 28, 29.
- The artifact's centre of gravity is the book's own misconception note: "Students
  can have the misconception that strong acids are equivalent to concentrated acids"
  — the strongest distinction in the set is one the source itself flags.
- Several distinctions are exam-wording traps recorded verbatim (corrosion versus
  rusting; constant versus equal), matching the MIS family's observations from the
  examiner-corpus side.

## Main Analysis

### EXP-041 — Evaporation versus boiling

**Side A:** boiling happens at one temperature only, when heating is strong enough
that "the particles are moving fast enough to overcome all the forces of attraction
between them" throughout the liquid — hence the bubbling throughout.
**Side B:** evaporation happens at any temperature: "Evaporation occurs at any
temperature, but boiling only occurs at one temperature – the boiling point of the
liquid." The mechanism is a surface phenomenon — only "some very fast particles at the
surface of the liquid" break away — so puddles quietly disappear at 5 °C without ever
boiling.
**The test that separates them:** bubbles throughout versus silent surface loss; one
temperature versus any temperature. The book's extension adds the closed-container
twist: in a sealed container evaporation and condensation run together.
**Evidence:** the key-point contrast (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 28); the evaporation mechanism and the
closed-container case (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl
line 30); the boiling mechanism (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 29); spec 1.1–1.2 at (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p17).

### EXP-042 — Sublimation and what to call the reverse

**Side A:** sublimation is the solid-to-gas direct change — "The conversion of a
solid into a gas is known as sublimation".
**Side B:** the reverse (gas to solid) has unsettled names: "Some people call it
'de-sublimation' or 'deposition' and others just use the word 'sublimation' again."
The book's dry-ice demonstration shows the direct solid-gas route and why the white
cloud is condensed water vapour, not the invisible carbon dioxide itself.
**The test that separates them:** direction. Solid → gas is unambiguously
sublimation; gas → solid is the word in dispute, and a careful answer names it
(deposition) rather than re-using sublimation.
**Evidence:** the sublimation/deposition text (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 30); the naming key point
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 29); spec 1.2 at
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p17).

### EXP-043 — Pure substance versus mixture, read off the thermometer

**Side A:** "Pure substances, such as elements and pure compounds, melt and boil at
fixed temperatures."
**Side B:** "mixtures usually melt or boil over a range of temperatures", and
impurities push both the wrong way — the salt-in-water example lowers the melting
point to about −0.6 °C and raises the boiling point to about 100.2 °C.
**The test that separates them:** melt a sample and record start-to-finish. The
book's aspirin case is the model: pure aspirin melts at 138 °C; a sample melting
across 128–134 °C "is quite impure because it melts over a wide range". A mixture is
also — by definition — "not a pure substance", so the magnet test on iron-and-sulfur
versus iron sulfide lands on the same boundary from the composition side.
**Evidence:** the fixed-versus-range rule and the aspirin case (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 70); the impurity key point and the
magnet test (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 69);
spec 1.9 at (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf
p18).

### EXP-044 — Mass number versus relative atomic mass

**Side A:** mass number is a whole-number count for one atom — "mass number =
number of protons + number of neutrons".
**Side B:** the number printed above a symbol in the International GCSE Periodic
Table "is a relative atomic mass and not a mass number", and it is usually the mass
number of the most common isotope — "The only exceptions to this are chlorine (35.5)
and copper (63.5)" — because it is a weighted average across isotopes (mechanism in
EXP-024).
**The test that separates them:** try to compute neutrons with the printed number.
Chlorine gives 35.5 − 17 = 18.5 neutrons, and since "It is not possible to have half a
neutron … there must be something wrong with this", the printed number was never a
mass number.
**Evidence:** the atomic/mass-number definitions (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 93); the Periodic-Table key point
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 95); the chlorine
resolution (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 97);
spec 1.16 at (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf
p18).

### EXP-045 — Strong versus weak versus concentrated: the book's own warning

**Side A:** strength is about dissociation — "Strong acids dissociate completely
into their constituent ions in water"; in weak acids "the dissociation is only
partial" (about 1 in ~75 ethanoic acid molecules). Ethanoic acid and the other
carboxylic acids are the book's canonical weak acids, with pH around 3–5.
**Side B:** concentration is about how much acid is dissolved in how much water —
a 0.10 mol/dm³ solution of ethanoic acid still has a pH of 2.88, showing the two
axes are independent.
**The book's own warning:** "Students can have the misconception that strong acids
are equivalent to concentrated acids. Whether an acid is strong or weak has, in fact,
nothing to do with its concentration." The observable consequence makes the boundary
physical: at equal concentrations, ethanoic acid reacts with metals and carbonates
"much more slowly than the hydrochloric acid as the concentration of the H⁺ ions is
much less" — same volume, same molarity, different ion population, different fizz.
**Evidence:** the misconception extension (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 1006); the weak-acid properties and
the salt-formula caution (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 1003); the pH scale and its
concentration-dependence note (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 571); spec Topic 4(f) area at
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p29).

**Family seam (RUN-011):** the tutor-comparison framing of this same contrast
lives in TUT-08 record TUT-046 (the dissociation criterion, not degree); both records
ground on the same book passage cited in their Evidence lines and are consistent by
construction.

### EXP-046 — Corrosion versus rusting

**Side A:** corrosion is the general class — "Many metals corrode".
**Side B:** rusting is the member — "it is only the corrosion of iron that is
referred to as rusting", and it needs both reagents: "Iron needs oxygen and water to
rust", producing hydrated iron(III) oxide and nothing else deserves the name.
**The test that separates them:** name the metal. Copper patina and aluminium oxide
are corrosion; only iron (and mild steel) rusts. The book's prevention note draws the
same boundary practically: barrier methods protect any metal, but galvanising is iron-
specific insurance because zinc's sacrificial electron flow (EXP-022) keeps the iron
from forming ions at all.
**Evidence:** the exam-wording warning (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 533); the rusting definition, formula
and prevention ladder (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 538); the two-reagent key point
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 469); spec Topic
2(d) area at (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf
p22).

### EXP-047 — Hotter is not the same as endothermic

**Side A:** endothermic is an energy-direction word — the reaction "absorbs heat
from the surroundings", the mixture gets colder, and "This heat energy is converted to
chemical energy".
**Side B:** heating is a rate tool — "Not all reactions that have to be heated are
endothermic reactions. Sometimes we just heat something to make it go faster." The
book's own example pair makes the boundary real: carbonates must be heated constantly
to decompose (genuinely endothermic), while plenty of exothermic reactions are lit or
warmed only to get them going.
**The test that separates them:** watch the thermometer during the reaction, not
the bunsen before it. Temperature falling during reaction means endothermic; a flame
used to start or speed a reaction says nothing about energy direction.
**Evidence:** the heating reminder and the heat-to-chemical-energy conversion
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 723); the
exothermic counter-case (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 713); spec 3.1 at (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p27).

### EXP-048 — Constant versus equal at equilibrium

**Side A:** "the concentrations of the reactants and products at equilibrium are
constant, they are not equal" — the book's own exam-wording hint, with the
blue-and-yellow-squares model showing totals steady while every individual square
keeps flipping.
**Side B:** equal is the wrong target: at equilibrium "the rate of the forward
reaction is equal to the rate of the reverse reaction" — it is the rates that match,
not the amounts, and the position of equilibrium is a separate question about which
side holds more (EXP-031's Route B).
**The test that separates them:** any sentence claiming equilibrium means 50:50 is
Side-B language misapplied to amounts; the correct claim fixes the rates and lets the
amounts sit wherever the position puts them, constant until conditions change.
**Evidence:** the constant-not-equal hint and the squares model (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 833); spec Topic 3(c) area at
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p28).

## Evidence / Source Basis

- **Primary — SRC-BOOK-4CH1-SB1** (CURRENT — AUTHORITATIVE): validated v3 parse of
  the Pearson 4CH1 student book, cited at chunk identity. 18 chunks / 15,983 bounded
  chars in this pack.
- **Primary — SRC-SPEC-4CH1** (CURRENT — AUTHORITATIVE): Issue 3 specification PDF,
  page identity citations at pp. 17, 18, 22, 27, 28, 29; statement numbers read from
  pack-visible excerpts only.
- **Supplementary — SRC-TL-4CH1**: identity-level presence only.
- Pack spec: `evidence/EXP-06/pack_spec.json`; pack sha256 in the run manifest.

## Limitations / Coverage Gaps

- The weak/strong record inherits the book's level of treatment: partial dissociation
  is quantified only by the book's own "1 in ~75" figure, and no equilibrium
  description of weak-acid dissociation is added because none exists in the pack
  sources.
- The strong-acid examples are confined to the book's pair (hydrochloric, sulfuric);
  nitric acid is not quoted as strong here because no pack chunk does so.
- The equilibrium distinction anchors at page level (p. 28) with no equilibrium
  statement numbers claimed, for the run-wide p. 28 excerpt-bound reason recorded in
  EXP-03.
- OCR-origin garble in quoted chunks is quoted verbatim and never repaired; one
  equation in the weak-acid chunk (the magnesium ethanoate line) carries a parse-era
  formula mangle and is therefore paraphrased, not quoted.

## Research Status

Status GENERATED under SIB-GEN run SIB-CHEMISTRY_4CH1-RUN-004 (BL-008 pass 3, EXP
family). Structural QA passed at the validator of record; evidence-claim QA passed
with zero violations; educational review against the five pilot acceptance criteria
passed. Research output, not canonical curriculum truth; staging and publication
remain operator gates.
