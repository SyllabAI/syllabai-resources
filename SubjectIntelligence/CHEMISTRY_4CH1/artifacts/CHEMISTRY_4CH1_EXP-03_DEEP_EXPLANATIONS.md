---
sib_protocol: SIB-1.0
artifact_id: EXP-03
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

status: GENERATED
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

# EXP-03 — Deep Explanations

## Purpose

This artifact holds the deep versions of the 4CH1 explanations: the mechanisms and
extensions that sit just beyond the core account, drawn deliberately from the book
of record's own EXTENSION WORK and explanation sections. The deepening is bounded by
two disciplines. First, every record is grounded on the same validated v3 chunk corpus
as the rest of the pass — nothing is deepened beyond what the book itself says.
Second, the records label their own status: where the book marks material as extension
or flags an exam boundary ("you will not be asked…"), the record repeats that flag so
a teacher can place the material correctly relative to the specification. This is a
research artifact; it does not promote itself into canonical educational truth
(Subject Intelligence Build v1, §5).

## Scope

**Covers:** eight deep records (EXP-017 … EXP-024): why shells hold 2,8,8 and where
the 2,8,8,2 anomaly comes from; why Group 1 melting points fall down the group; the
size-and-attraction explanation of Group 1 reactivity; halogen reactivity reframed as
oxidising power with the fluorine caveat; selective discharge in electrolysis; the
real chemistry of rust; why pressure barely touches solids and liquids at equilibrium;
and why chlorine's Periodic Table mass is 35.5.

**Does not cover:** core-register accounts (EXP-01), simplified registers (EXP-02),
route comparisons (EXP-04), analogies (EXP-05), terminology distinctions (EXP-06),
single-mechanism why-it-works records (EXP-07), and why-question formats (EXP-08).
No legacy content entered any pack.

## Executive Summary

- Eight records, each extending a core concept using the book's own extension and
  explanation material, with the extension status carried explicitly.
- The book's honest-boundary practice is preserved — including the remarkable
  fluorine note that the International GCSE explanation "is wrong" but should still be
  used in the exam.
- 36 chunks / 34,999 bounded chars from SRC-BOOK-4CH1-SB1 in this pack; spec pages
  17, 18, 20, 21, 22, 27, 28 from SRC-SPEC-4CH1.

## Main Analysis

### EXP-017 — Why shells fill 2, 8, 8 — and why potassium breaks the pattern

**Concepts:** shells; energy levels; subshells; electronic configuration
**Specification anchor:** 1.19 (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p18)
Temporal scope: CURRENT — AUTHORITATIVE
**The deep explanation:** the working model is that "electrons move around the nucleus
in a series of levels called energy levels or shells", each shell holding a fixed
maximum and lower levels filling first. The model predicts 2, 8, 8 for the first
eighteen elements — and then potassium and calcium put their nineteenth and twentieth
electrons into the fourth shell while the third still has room. The book's extension
resolves the anomaly: each shell is actually made of subshells, and "The 4s subshell
(which can hold 2 electrons) is lower in energy than the 3d subshell (which can hold 10
electrons) and so 2 electrons go into the fourth shell before the next 10 go into the
third shell." The book also blesses vocabulary flexibility: shell and energy level are
used interchangeably and "both terms will be accepted in the examination".
**Depth discipline note:** this is the book's own EXTENSION WORK; at International
GCSE the 2,8,8 model is the expected tool, and the subshell story is the why behind
its one visible crack.
**Evidence:** the subshell resolution (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 113); the shell-filling model
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 115); the
terminology hint including potassium and calcium's fourth-shell start
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 117); spec 1.19 at
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p18).

### EXP-018 — Why Group 1 melting points fall down the group

**Concepts:** metallic bonding; melting point trend; electrostatic attraction
**Specification anchor:** Topic 2(a) area of record (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p22)
Temporal scope: CURRENT — AUTHORITATIVE
**The deep explanation:** the alkali metals' melting and boiling points are "very low
for metals, and get lower as you move down the group". The book's extension gives the
mechanism in metallic-bonding terms: as atoms get bigger down the group, "the nuclei
of the positive ions are further from the delocalised electrons in caesium than in
sodium and therefore there is weaker electrostatic attraction". The same
distance-weakens-attraction logic explains the falling hardness and the low densities
(lithium, sodium and potassium all float on water). This record is the Group 1 twin of
the sodium-versus-magnesium contrast in EXP-006: charge and distance together set
metallic bond strength.
**Evidence:** the size-attraction mechanism and the group's physical properties
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 410); spec Topic 2(a)
area at (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p22).

### EXP-019 — Explaining the increase in Group 1 reactivity

**Concepts:** reactivity trend; electron loss; nuclear attraction; shielding by size
**Specification anchor:** 2.2, 2.4C (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p22)
Temporal scope: CURRENT — AUTHORITATIVE
**The deep explanation:** all Group 1 reactions are electron-loss reactions, so the
trend question reduces to how easily the outer electron is lost. The book's chain:
down the group the atoms have more shells and get bigger, so the outer electron sits
further from the nucleus; "Because it is further from the nucleus it is less strongly
attracted by the nucleus and therefore more easily lost." The trend is dramatic
enough to drive the group's storage rules — lithium, sodium and potassium under oil,
while "Rubidium and caesium are so reactive that they have to be stored in sealed
glass tubes". This is statement 2.4C's chemistry-only demand answered exactly as the
book frames it: bigger atom, weaker hold, easier loss, faster reaction.
**Evidence:** the full explanation (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 423); the storage consequences
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 411); spec 2.2 and
2.4C at (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p22).

### EXP-020 — Halogen reactivity as oxidising power (and the fluorine caveat)

**Concepts:** halogens; displacement; oxidising agent; electron gain
**Specification anchor:** 2.7, 2.8C (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p22)
Temporal scope: CURRENT — AUTHORITATIVE
**The deep explanation:** halogen reactivity can be restated in electron terms: the
halogens react by forming 1– ions, taking electrons from something else, so the trend
is really about how readily each atom gains an electron. A chlorine atom is smaller
than a bromine atom, so the added electron enters a shell closer to the nucleus where
attraction is stronger — "Chlorine therefore has a stronger tendency to form a 1– ion
than bromine". The extension then upgrades the vocabulary: chlorine is "a stronger
oxidising agent than bromine, which is a stronger oxidising agent than iodine", with
each halogen able to oxidise the halide ions below it. The book closes with a striking
honesty note: the size argument does not actually hold for fluorine — its extra
reactivity comes from the weakness of the F–F bond — but at International GCSE the
size explanation is what the exam expects, "even though it is wrong!"
**Evidence:** the oxidising-power restatement (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 451); the size-and-attraction mechanism
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 452); the fluorine
caveat (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 450); spec
2.7 and 2.8C at (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf
p22).

### EXP-021 — Selective discharge: why the reactivity series decides electrolysis products

**Concepts:** electrolysis; cathode; discharge; reactivity series
**Specification anchor:** 1.58C, 1.59C (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p21)
Temporal scope: CURRENT — AUTHORITATIVE
**The deep explanation:** in aqueous electrolysis two positive species compete at the
cathode — metal ions and hydrogen ions from water — and the reactivity series picks
the winner. Electrolysing copper(II) sulfate solution, the book shows copper depositing
because "Copper is below hydrogen in the reactivity series, which means that it is
easier to add electrons to copper ions to form an atom"; with a metal above hydrogen,
"you get hydrogen produced at the cathode instead of the metal". The general key point
makes the whole series work in one sentence: "the more reactive something is, the
greater tendency it has to form an ion" and therefore the harder it is to reverse back
to the atom. The anode side has its own selection rule — halide ions give halogens,
sulfate and nitrate leave oxygen from water instead.
**Evidence:** the copper(II) sulfate case (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 381); the selection rules
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 385); the
reactivity-to-ion-formation key point (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 375); spec 1.58C and 1.59C at
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p21).

### EXP-022 — Rust is a two-step redox process, and galvanising exploits it

**Concepts:** rusting; oxidation states; sacrificial protection
**Specification anchor:** Topic 2(d) area of record (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p22)
Temporal scope: CURRENT — AUTHORITATIVE
**The deep explanation:** the familiar "iron + oxygen + water → rust" line hides a
mechanism the book itself calls "a surprisingly complicated process": iron first loses
electrons to form iron(II) ions, which the air then oxidises to iron(III) ions, with
reactions involving water producing the actual rust (the chunk's Roman numerals and
ion superscripts carry OCR-era mangling, so the mechanism is paraphrased here rather
than quoted — see Limitations). Galvanising attacks the first step: zinc loses electrons more readily than
iron, and those electrons flow into the iron — "If the iron can't form ions, it can't
rust" — which is sacrificial protection working even where the zinc coating is
scratched through.
**Evidence:** the two-step rust mechanism (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 534); the sacrificial-protection
mechanism (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 539); spec
Topic 2(d) area at (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p22).

### EXP-023 — Why pressure barely moves equilibria that have no gases

**Concepts:** equilibrium position; pressure; concentration
**Specification anchor:** Topic 3(c) area of record (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p28)
Temporal scope: CURRENT — AUTHORITATIVE
**The deep explanation:** pressure changes shift equilibria by changing
concentrations — but "The particles in solids and liquids are very close together and
they are affected very little by changes in pressure. Their concentration does not
really change as the pressure changes." So a reversible reaction involving only solids
and liquids has no pressure lever at all. The same chunk carries the deeper conceptual
point the exams reward: the position of equilibrium is about the direction of change
when conditions move, "It does not matter that we still have more A than B" — the
forward and reverse reactions are defined by direction (the book's A ⇌ 2B framing),
and equilibrium means constant concentrations, never equal ones.
**Evidence:** the pressure key point and the constant-versus-equal distinction
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 836); the
forward/reverse definitions (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 835); spec Topic 3(c) area at
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p28).

### EXP-024 — Why chlorine weighs 35.5: isotopes and weighted averages

**Concepts:** isotopes; relative atomic mass; weighted mean
**Specification anchor:** 1.16, 1.17 (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p18)
Temporal scope: CURRENT — AUTHORITATIVE
**The deep explanation:** a Periodic Table mass of 35.5 for chlorine cannot be a mass
number — subtracting the proton count gives "18.5" neutrons, "and so there must be
something wrong with this". The resolution: 35.5 is the relative atomic mass, a
weighted average over the naturally occurring isotope mix (³⁵Cl and ³⁷Cl). The book's
worked boron example makes the arithmetic concrete: with 20% ¹⁰B and 80% ¹¹B,
imagine 100 atoms, add up the total mass (20 × 10 + 80 × 11) and divide by 100 to get
10.8. The underlying reason a weighted average is meaningful at all is the isotope
invariance recorded at EXP-003: neutrons do not change chemical behaviour, so the
element reacts as one substance even while its atoms differ in mass.
**Evidence:** the 35.5 resolution (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 97); the boron worked example
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 101); the isotope
invariance (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 96); spec
1.16 and 1.17 at (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p18).

## Evidence / Source Basis

- **Primary — SRC-BOOK-4CH1-SB1** (CURRENT — AUTHORITATIVE): validated v3 parse of the
  Pearson 4CH1 student book, cited at chunk identity. 36 chunks / 34,999 bounded chars
  in this pack. The EXTENSION WORK chunks carry their own status labels, preserved here.
- **Primary — SRC-SPEC-4CH1** (CURRENT — AUTHORITATIVE): Issue 3 specification PDF,
  page identity citations at pp. 17, 18, 20, 21, 22, 27, 28; statement numbers read
  from pack-visible excerpts only.
- **Supplementary — SRC-TL-4CH1**: identity-level presence only.
- Pack spec: `evidence/EXP-03/pack_spec.json`; pack sha256 in the run manifest.

## Limitations / Coverage Gaps

- Depth is bounded by the book's own extension material: subshell energetics are named
  but not developed (orbital shapes, ionisation-energy fine structure are beyond both
  the book and this artifact).
- The fluorine caveat is recorded as the book states it — including its self-declared
  wrongness at this level; no attempt is made to supply the beyond-level correct
  mechanism (hydration enthalpy considerations) because no pack source carries it.
- Equilibrium statement numbers are anchored at page level (p. 28) because the pack's
  bounded excerpt of that page ends as the equilibrium sub-topic opens; the
  equilibrium statements themselves are not quoted numerically.
- OCR-origin garble in quoted chunks is quoted verbatim; one figure caption inside
  line 113's chunk (the "real shape" Periodic Table) is context, not quotation.

## Research Status

Status GENERATED under SIB-GEN run SIB-CHEMISTRY_4CH1-RUN-004 (BL-008 pass 3, EXP
family). Structural QA passed at the validator of record; evidence-claim QA passed
with zero violations; educational review against the five pilot acceptance criteria
passed. Research output, not canonical curriculum truth; staging and publication
remain operator gates.
