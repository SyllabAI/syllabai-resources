---
sib_protocol: SIB-1.0
artifact_id: EXP-02
artifact_version: 1.0
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

# lifecycle: GENERATED -> QA_PASSED -> STAGED
status: PUBLISHED
generated_by: zai_agent
generated_at: 2026-10-26

provenance:
  source_manifest: "SRC-BOOK-4CH1-SB1"
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-004"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "04df741df6185d2f5b6ccefd219244f36e24d40b"
    syllabai_resources: "c15fc29289e3db199474dd9f0d36c90de2531054"
---

# EXP-02 — Simple Explanations

## Purpose

This artifact restates the core concepts of Pearson Edexcel International GCSE
Chemistry (4CH1) in the simplest accurate register: the versions a candidate should
reach for first when meeting a topic, or when a long explanation has stopped making
sense. Every record here is a faithful simplification of the same book-of-record
grounding used by EXP-01 — same sources, same pack law, shorter chain of reasoning —
and each stays inside the specification's own definitions. Simplicity is the constraint,
never accuracy. Where the book itself flags that a simple version is incomplete (for
example, the isotope caveat on the "one type of atom" definition), that flag is carried
into the record rather than smoothed away. This is a research artifact supporting
teaching and revision design; it does not promote itself into canonical educational
truth (Subject Intelligence Build v1, §5).

## Scope

**Covers:** eight simple-register records (EXP-009 … EXP-016): the three states in
everyday terms; elements versus compounds versus mixtures; the atom and its particles;
how ions get their charge; the pH scale; exothermic versus endothermic in one breath;
what speeds reactions up; and the organic families at a glance. Each record is grounded
on 2–4 book chunks at chunk identity, anchored to specification statements visible in
the run's evidence pack (spec pp. 17, 18, 20, 22, 27, 28, 29).

**Does not cover:** the full core explanations with their reasoning chains (EXP-01),
beyond-specification depth (EXP-03), alternative teaching routes (EXP-04), analogies
and their limits (EXP-05), fine distinctions (EXP-06), mechanism-first explanations
(EXP-07), and student-voiced why questions (EXP-08). No legacy content: no legacy
source entered any pack.

## Executive Summary

- Eight records in deliberately plain language, each traceable to the same v3 chunk
  corpus (37 chunks / 27,090 bounded chars in this pack) and spec pages 17–29.
- The book's own simple handles are preserved: the brick wall and the swim, the
  puddle that evaporates but never boils, the magnet test for iron and sulfur.
- Where simplification would cross into error, the record says so explicitly (the
  alkane "saturated with hydrogen" phrasing carries the book's own "do not write this
  definition down in the exam" warning).

## Main Analysis

### EXP-009 — The three states, in one breath

**Concepts:** solid; liquid; gas; forces between particles
**Specification anchor:** 1.1, 1.2 (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p17)
Temporal scope: CURRENT — AUTHORITATIVE
**The simple explanation:** solids hold their shape because their particles are held
tightly together; liquids flow because you can push their particles out of the way;
gases spread out because their particles are barely held at all. The book's version:
"You can't walk through a brick wall because of the strong forces of attraction between
the particles - the particles can't move out of your way", while "You can swim through
water because you can push the particles out of the way", and a gas is easy to move
through because there are no forces between the particles. Heating and cooling just
move substances between these three arrangements — melting, freezing, boiling,
condensing and the rest are all re-arrangements, not changes of substance.
**Evidence:** everyday facts (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl
line 23); the three key-point forces (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 25); evaporation-versus-boiling distinction
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 28); spec 1.1–1.2 at
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p17).

### EXP-010 — Element, compound, mixture — which is which

**Concepts:** element; compound; mixture; impurity
**Specification anchor:** 1.8, 1.9 (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p18)
Temporal scope: CURRENT — AUTHORITATIVE
**The simple explanation:** an element is one substance made of one type of atom and
it "can't be split into anything simpler by chemical means"; a compound is two or more
elements chemically joined in fixed ratios; a mixture is things just sitting together
with "no chemical reaction occurs", in any proportions. Two quick tests follow from the
book: mixtures keep their parts' properties (iron stays magnetic, sulfur stays yellow)
and can be pulled apart physically — a magnet separates iron from sulfur — while a
compound such as iron sulfide behaves completely differently from either element and
only chemistry separates it again.
**One honest caveat:** the book notes it "isn't completely true to say that elements
consist of only one type of atom" — isotopes share the same atomic number, so the
precise definition is same-atomic-number, not identical atoms.
**Evidence:** element definition (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 63); the isotope caveat (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 64); mixture definition and the
magnet/iron-sulfide tests (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl
lines 67 and 69); spec 1.8–1.9 at (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p18).

### EXP-011 — The atom, simply

**Concepts:** proton; neutron; electron; atomic number; mass number
**Specification anchor:** 1.14, 1.15, 1.16 (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p18)
Temporal scope: CURRENT — AUTHORITATIVE
**The simple explanation:** every atom is made of protons and neutrons packed into a
tiny centre (the nucleus) with electrons whizzing around outside. Protons are positive,
neutrons have no charge, electrons are negative and almost weightless — "Virtually all
the mass of the atom is concentrated in the nucleus". The atomic number is just the
number of protons, and it is the atom's identity card: eight protons means oxygen, no
exceptions. The mass number is protons plus neutrons. That is all the bookkeeping a
candidate needs before bonding makes sense.
**Evidence:** structure of the atom (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 90); where the mass lives (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 92); atomic and mass number
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 93); spec 1.14–1.16 at
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p18).

### EXP-012 — How atoms get charges: ions

**Concepts:** ion; cation; anion; electron loss or gain
**Specification anchor:** 1.37 (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p20)
Temporal scope: CURRENT — AUTHORITATIVE
**The simple explanation:** an atom is neutral because its protons (+) and electrons
(–) balance. Remove an electron and the balance tips positive: that charged atom is a
positive ion. Add an electron and it tips negative. The book's own arithmetic for
sodium: eleven protons (11+) against eleven electrons (11–) gives zero, but the sodium
ion keeps only ten electrons, "so with 11+ and 10– there is an overall charge of 1+".
Metals lose electrons to form ions, non-metals gain them, and ionic compounds — like
sodium chloride, the best-known example — are what form when the two trade electrons.
**Evidence:** ion-formation objectives and ion charges (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 264); the metal-plus-non-metal recognition
rule (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 265); the
sodium-charge check (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl
line 268); spec 1.37 at (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p20).

### EXP-013 — The pH scale, simply

**Concepts:** pH; acidic; alkaline; indicator
**Specification anchor:** Topic 2(f) area of record (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p22)
Temporal scope: CURRENT — AUTHORITATIVE
**The simple explanation:** pH is a 0-to-14 ladder that says how acidic or how
alkaline a solution is — the book's phrasing is that the scale "tells you how acidic or
how alkaline a solution is". Numbers below 7 are acidic (lemon juice, vinegar), 7 is
neutral (pure water), and numbers above 7 are alkaline (soap, oven cleaner). Indicators
are dyes that change colour depending on which side of the ladder they sit, which is
what makes titrations readable. The book's extension note honestly adds that the 0–14
range is approximate and concentration-dependent.
**Evidence:** chapter scope (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 569); the pH scale and its extension note
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 571); spec Topic 2(f)
area at (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p22).

### EXP-014 — Hotter or colder? Exothermic and endothermic, simply

**Concepts:** exothermic; endothermic; temperature change
**Specification anchor:** 3.1 (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p27)
Temporal scope: CURRENT — AUTHORITATIVE
**The simple explanation:** if the test tube gets warmer, the reaction is exothermic —
"a reaction that gives out heat to the surroundings is said to be exothermic". If it
gets colder, the reaction is endothermic — it is "a reaction that absorbs heat from the
surroundings". That is the whole test: temperature up means heat flowed out of the
chemicals; temperature down means heat flowed in. The book adds one practical wrinkle:
a slow exothermic reaction can barely warm anything because the heat leaks away as it
is released, which is why fast reactions give the biggest thermometer readings.
**Evidence:** exothermic definition (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 713); endothermic definition
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 722); the
rate-versus-heat-loss point (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 516); spec 3.1 at (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p27).

### EXP-015 — What makes a reaction go faster, simply

**Concepts:** rate; temperature; concentration; surface area; catalyst
**Specification anchor:** 3.9, 3.12 (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p28)
Temporal scope: CURRENT — AUTHORITATIVE
**The simple explanation:** the rate is just how quickly reactants are used up or
products appear — "the speed at which the amount of reactants decreases or the amount
of products increases". Four levers make it faster: more surface area (powdered marble
chips react faster than lumps), higher concentration, higher temperature, and a
catalyst — "substances that speed up chemical reactions, but aren't used up". The
marble-chips-and-acid experiment is the canonical measurement: gas escapes, the balance
reading drops, and the steeper the line the faster the reaction.
**Evidence:** rate definition (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 784); the marble-chip practical
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 786); the temperature
lever (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 807); the
catalyst definition (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl
line 809); spec 3.9 and 3.12 at (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p28).

### EXP-016 — The organic families at a glance

**Concepts:** hydrocarbon; alkane; alkene; homologous series; polymer
**Specification anchor:** 4.1, 4.3 (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p29)
Temporal scope: CURRENT — AUTHORITATIVE
**The simple explanation:** organic chemistry is the chemistry of hydrocarbons —
compounds of carbon and hydrogen only — organised into families. The alkanes are "the
simplest family of hydrocarbons, containing only carbon-carbon and carbon-hydrogen
single bonds"; the alkenes are "another family of hydrocarbons" that all contain a
carbon-carbon double bond and are much more reactive. Families are called homologous
series: same functional group, similar chemistry, a trend in physical properties, and
each member differing from the next by one -CH₂- unit. Chain the small alkene
molecules together and you get polymers — "Polymers are everywhere", from proteins to
plastic bags.
**One honest caveat:** the book warns candidates not to write the "saturated with
hydrogen" shorthand as the definition of an alkane in the exam — the safe definition is
the single-bonds one.
**Evidence:** alkanes chapter opener (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 939); the saturation definition and its
warning (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 941); the
homologous-series definition (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 946); the alkenes opener and the
unsaturated definition (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl
lines 955 and 961); the polymers opener (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 1027); spec 4.1 and 4.3 at
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p29).

## Evidence / Source Basis

- **Primary — SRC-BOOK-4CH1-SB1** (CURRENT — AUTHORITATIVE): the validated v3 parse of
  the Pearson 4CH1 student book, cited at chunk identity (JSONL line + chunk id; book
  pages inside the chunk record). 37 chunks / 27,090 bounded chars in this pack.
- **Primary — SRC-SPEC-4CH1** (CURRENT — AUTHORITATIVE): Issue 3 specification PDF,
  cited at page identity (pp. 17, 18, 20, 22, 27, 28, 29); statement numbers in records
  are read from those pages' excerpts.
- **Supplementary — SRC-TL-4CH1**: identity-level presence only; no content quotes
  needed.
- Pack spec: `evidence/EXP-02/pack_spec.json`; pack sha256 in the run manifest.

## Limitations / Coverage Gaps

- Simple register trades completeness for accessibility: calculations, electrolysis
  rules and equilibrium reasoning are absent by design and live in sibling artifacts.
- The organic-families record is an orientation, not coverage: naming rules, cracking
  and polymerisation mechanisms get their own treatment in EXP-07/EXP-08 and a future
  pass if operated.
- SME-note sources remain failed preflight (disclosed run-wide); the simple register
  has not been student-tested — the educational review of this run is the only
  audience check on record.
- OCR-origin garble in quoted chunks is quoted verbatim and never repaired.

## Research Status

Status GENERATED under SIB-GEN run SIB-CHEMISTRY_4CH1-RUN-004 (BL-008 pass 3, EXP
family). Structural QA passed at the validator of record; evidence-claim QA passed
with zero violations; educational review against the five pilot acceptance criteria
passed. Research output, not canonical curriculum truth; staging and publication
remain operator gates.
