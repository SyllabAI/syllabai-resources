---
sib_protocol: SIB-1.0
artifact_id: EXP-01
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

# EXP-01 — Core Concept Explanations

## Purpose

This artifact provides the core explanations for Pearson Edexcel International GCSE
Chemistry (4CH1): one complete, specification-anchored explanation for each of the
eight foundation concepts a candidate must own before the rest of the course can make
sense. It is the first artifact of the Explanation Intelligence (EXP) family, and the
first SIB family to be grounded primarily on the validated parse of the of-record
student book (SRC-BOOK-4CH1-SB1, v3 chunk corpus) alongside the specification of
record. Every explanation stays inside the specification's own definitions — the EXP
family's forbidden law — and every substantive claim is carried on a bounded, locator-
addressed excerpt from the run's evidence pack. This is a research artifact: it
supports teaching and revision design; it does not promote itself into canonical
educational truth (Subject Intelligence Build v1, §5).

## Scope

**Covers:** eight core-concept records (EXP-001 … EXP-008) — the particle model and
states of matter; elements, compounds and mixtures; atomic structure; ionic bonding;
covalent bonding; metallic bonding; acids, alkalis and salts; and exothermic versus
endothermic reactions. Each record explains the concept as the book of record explains
it, anchored to the visible specification statements carried in the run's evidence
pack (spec pp. 17–19, 22, 27), with book citations at chunk identity (JSONL line +
chunk id + book pages inside the chunk record).

**Does not cover:** simplified register versions (EXP-02), beyond-specification depth
(EXP-03), alternative teaching routes (EXP-04), analogies (EXP-05), fine distinctions
(EXP-06), mechanism-first why-it-works material (EXP-07), and student-voiced why
questions (EXP-08) — those are sibling artifacts of this pass. Legacy 4CH0 content is
out of scope entirely; no legacy source entered any pack.

## Executive Summary

- Eight records, one per core concept, each grounded on 2–4 book chunks with page
  identity preserved and anchored to the specification statements visible in the pack.
- The book's own pedagogy is preserved: explanations follow the book's sequence
  (particle model → classification → atom → bonding triad → acids → energetics).
- The evidence pack carries 53 v3 chunks (39,316 chars, bounded) from SRC-BOOK-4CH1-SB1
  and 5 bounded spec pages from SRC-SPEC-4CH1 — all sha256-pinned at pack build time.
- OCR-origin caveats ride along from the source's own limitations: formulas in quoted
  chunks are quoted verbatim including parse-era garble, never silently repaired.

## Main Analysis

### EXP-001 — The particle model: states of matter and their interconversions

**Concepts:** states of matter; particle arrangement and energy; melting/freezing
**Specification anchor:** 1.1, 1.2 (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p17)
Temporal scope: CURRENT — AUTHORITATIVE
**The explanation:** everything around us is made of particles too small to see, and
the three states of matter differ only in how those particles are arranged, how they
move, and how much energy they carry. In a solid the particles are held in fixed
positions and only vibrate; in a liquid they can move around each other; in a gas they
move freely and fast. The book grounds the model in everyday experience before any
diagram: the reason you cannot walk through a brick wall is that the particles cannot
move out of your way, while water and air yield because their particles can.
**How the state changes:** heating a solid makes its particles vibrate faster until
the forces of attraction between the particles are no longer strong enough to hold
them in place — the solid melts. The book is explicit that melting needs energy input
because "The particles in the liquid have more kinetic energy than the particles in the
solid", and that melting point and freezing point are the same temperature approached
from opposite directions.
**Why this version is core:** statements 1.1 and 1.2 demand exactly this triple
(arrangement, movement, energy) for the states and for the names and mechanics of each
interconversion; every later topic — diffusion, solubility, rates, equilibrium —
re-uses this model.
**Evidence:** (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 22):
"Solids, liquids and gases are known as the three states of matter."; everyday-experience
grounding (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 23): "You
can't walk through a brick wall"; the full melting mechanism (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 27); spec statements 1.1–1.2 at
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p17).

### EXP-002 — Elements, compounds and mixtures

**Concepts:** element; compound; mixture; fixed proportions
**Specification anchor:** 1.8, 1.9 (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p18)
Temporal scope: CURRENT — AUTHORITATIVE
**The explanation:** an element is a substance that "can't be split into anything
simpler by chemical means" and contains only one type of atom; a compound is formed
when two or more elements chemically combine, and "The elements always combine in fixed
proportions" — hydrogen and fluorine always make HF, magnesium and fluorine always make
MgF₂; a mixture is what you get when substances are mixed together with no chemical
reaction, and its components can be present in any proportion. The compound-versus-
mixture boundary is therefore a chemical-bonding boundary, not a visual one: water is
always two-to-one hydrogen-to-oxygen, while a hydrogen/oxygen mixture can be anything
at all.
**Why this version is core:** statement 1.8 is the classification skill the exam
tests directly, and 1.9 adds the observable handle — pure substances melt and boil at
fixed temperatures while mixtures melt and boil over a range — which later grounds
purity and separation work (Chapter 2's separation techniques, Topic 4's crude-oil
fractions).
**Evidence:** element definition (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 63); fixed proportions at line 66; the
mixture definition at line 67 (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 67); spec statements 1.8–1.9 at
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p18).

### EXP-003 — Atomic structure: protons, neutrons, electrons and isotopes

**Concepts:** sub-atomic particles; atomic number; mass number; isotopes
**Specification anchor:** 1.14, 1.15, 1.16, 1.17 (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p18)
Temporal scope: CURRENT — AUTHORITATIVE
**The explanation:** atoms are made of protons, neutrons and electrons — sub-atomic
particles because they are smaller than an atom. The protons and neutrons sit in the
nucleus; virtually all the atom's mass is concentrated there because electrons are far
lighter. The atomic number is the number of protons and it uniquely defines the
element; the mass number counts protons plus neutrons. Isotopes are atoms of the same
element with the same atomic number but different mass numbers — carbon-12, carbon-13
and carbon-14 all have six protons but differing neutron counts — and the book makes
the chemically crucial point that this "makes no difference to their chemical
reactions", because chemical properties are controlled by the electrons, which are
identical across isotopes.
**Why this version is core:** statements 1.14–1.17 are the load-bearing definitions:
every bonding, electrolysis and organic-chapter idea later re-uses the
proton/neutron/electron bookkeeping and the electron-controlled-reactivity principle.
**Evidence:** structure of the atom (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 90); mass concentration in the nucleus at
line 92; atomic and mass number definitions at line 93; the isotope record including
the electron-controlled-reactivity point at line 96 (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 96); spec statements 1.14–1.17 at
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p18).

### EXP-004 — Ionic bonding: electron transfer and electrostatic attraction

**Concepts:** ions; cation; anion; electron transfer; giant ionic lattice
**Specification anchor:** 1.37, 1.40, 1.41, 1.42 (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p20)
Temporal scope: CURRENT — AUTHORITATIVE
**The explanation:** ionic compounds form when a metal reacts with a non-metal: the
metal atom transfers its outer electron (or electrons) to the non-metal atom. Losing
electrons leaves a positive ion (a cation, such as Na⁺); gaining electrons makes a
negative ion (an anion, such as Cl⁻). The book defines the force that then holds the
compound together without jargon: "Electrostatic attraction simply means that
positively charged particles attract negatively charged particles." The ions build a
regular giant lattice, and statement 1.42's high-melting-point consequence follows
from the strength of those attractions (explained mechanistically in EXP-049).
**Why this version is core:** statements 1.37–1.43 form the bonding backbone of
Topic 1: ion formation, dot-and-cross representation, the electrostatic definition,
and the melt-to-conduct rule all hang on this record. The book's sodium-chloride
framing (a dangerously reactive metal plus a poisonous gas giving safe table salt)
also demonstrates why compound properties are not the average of element properties.
**Evidence:** transfer mechanism and ion definitions (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 269); the metal-plus-non-metal recognition
rule at line 265; the dot-and-cross convention and its limits at line 270
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 270); spec statements
1.37–1.42 at (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p20).

### EXP-005 — Covalent bonding: shared pairs and molecular substances

**Concepts:** covalent bond; molecule; simple molecular substances
**Specification anchor:** 1.44, 1.45 (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p20)
Temporal scope: CURRENT — AUTHORITATIVE
**The explanation:** a covalent bond is a shared pair of electrons between two atoms;
a molecule is two or more atoms chemically bonded together, whether the atoms are of
the same element (H₂) or different elements (H₂O). The book stresses scale: there are
"a lot more covalent compounds than ionic compounds", so the bonding model has to work
in far more contexts. Because molecules are neutral and their electrons are locked in
atoms or in bonds, simple molecular substances do not conduct electricity — the book's
own causal chain is that the molecules have no overall charge and no mobile charged
particles.
**Why this version is core:** statements 1.44–1.45 define the second bonding pillar;
the no-conductivity consequence is the exam's favourite contrast against ionic
compounds (1.43 versus 1.55C) and the entry point to intermolecular-force reasoning
developed in EXP-050.
**Evidence:** molecule definition (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 87); the chapter's scale claim at line
302; the no-conductivity causal chain at line 332 (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 332); an organic extension case (ethane)
at line 317; spec statements 1.44–1.45 at (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p20).

### EXP-006 — Metallic bonding: positive ions in a sea of delocalised electrons

**Concepts:** metallic bond; delocalised electrons; metal properties
**Specification anchor:** 1.52C, 1.53C, 1.54C (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p21)
Temporal scope: CURRENT — AUTHORITATIVE
**The explanation:** when metal atoms bond, each atom's outer electron becomes free to
move through the whole structure — the electrons are delocalised — leaving a lattice of
positive ions sitting in a sea of delocalised electrons. Conductivity follows
immediately (the electrons carry charge through the metal), and the book extends the
model quantitatively: sodium delocalises one electron per atom so its bonding is weak
as metals go and it is soft with a low melting point, while magnesium's two
delocalised electrons per atom give 2+ ions, stronger attraction, and a higher melting
point.
**Why this version is core:** statements 1.52C–1.54C are chemistry-only but
load-bearing for the structure-to-property thread; the sodium-versus-magnesium
contrast is the cleanest exam-ready demonstration that bonding strength tracks charge
and electron count, and it re-appears in Group 1 reactivity reasoning (EXP-019).
**Evidence:** delocalisation and the sea-of-electrons model (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 345); the property explanations
including the Na/Mg contrast at line 349 (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 349); chapter framing at line 343; spec
statements 1.52C–1.54C at (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p21).

### EXP-007 — Acids, alkalis, bases and salts

**Concepts:** acid; base; alkali; salt; pH scale
**Specification anchor:** Topic 2(f)/(g) area of record (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p22)
Temporal scope: CURRENT — AUTHORITATIVE
**The explanation:** all acids contain hydrogen, and "When that hydrogen is replaced
by a metal, the compound formed is called a salt" — magnesium sulfate, zinc chloride
and potassium nitrate are all salts. Bases are the counterparty: "bases are substances
that neutralise acids by combining with the hydrogen ions in them to produce water",
typically metal oxides, metal hydroxides or ammonia; alkalis are the soluble subset.
The pH scale runs from about 0 to about 14 and reports how acidic or alkaline a
solution is. The book's mechanism for neutralisation is explicit at this level: in the
copper(II) oxide plus sulfuric acid case, the acid's H⁺ ions combine with the oxide's
O²⁻ ions to make water, and a salt is the other product.
**Why this version is core:** the salt-preparation work of Chapter 17, the titration
calculations of Chapter 6, and the acid-reaction rules all depend on this vocabulary
being exact — which is why the terminology errors surface so consistently in the MIS
family (see MIS-01).
**Evidence:** salt definition (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 596); base definition and the CuO/H⁺ + O²⁻
mechanism at line 607 (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl
line 607); the pH scale at line 571; chapter scope at line 569; spec Topic 2(f)/(g)
area at (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p22).

### EXP-008 — Exothermic and endothermic reactions

**Concepts:** exothermic; endothermic; energy level; temperature change
**Specification anchor:** 3.1, 3.5C (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p27)
Temporal scope: CURRENT — AUTHORITATIVE
**The explanation:** a reaction "that gives out heat to the surroundings is said to be
exothermic" — the test tube gets warmer because chemical energy is converted to heat
energy; the products end up with less chemical energy than the reactants, which is
what "the products are more stable than the reactants" means on an energy level
diagram. An endothermic reaction is the mirror image: it absorbs heat from the
surroundings, the mixture gets colder, and the products carry more chemical energy
than the reactants, with heat converted into chemical energy. The book adds the
exam-critical caveat that needing heat is not the same as being endothermic: "Not all
reactions that have to be heated are endothermic reactions. Sometimes we just heat
something to make it go faster."
**Why this version is core:** statement 3.1 is the definition pair and 3.5C the
diagram skill; the stability language introduced here is the same language the
equilibrium chapter later re-uses, and the temperature-change experiments of 3.8 are
the practical side of the same record.
**Evidence:** exothermic definition and energy conversion (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 713); the stability phrasing at line 721;
endothermic definition at line 722; the heating caveat at line 723
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 723); spec statements
3.1 and 3.5C at (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf
p27).

## Evidence / Source Basis

- **Primary — SRC-BOOK-4CH1-SB1** (CURRENT — AUTHORITATIVE): the validated v3 parse of
  the Pearson 4CH1 student book (books/CATALOG.md §3.1, audit GREEN 2026-10-18), cited
  at chunk identity — JSONL line number plus chunk id, with book page numbers carried
  inside each chunk record. 53 chunks / 39,316 bounded chars in this pack, under the
  pack caps (60 excerpts / 1,600 chars / 40,000 chars per source).
- **Primary — SRC-SPEC-4CH1** (CURRENT — AUTHORITATIVE): the Issue 3 specification
  PDF, cited at page identity (pp. 17-22 and 27 in this pack); statement numbers
  quoted in records are read from those pages' excerpts, never from memory.
- **Supplementary — SRC-TL-4CH1**: present in the pack at identity level (the
  teaching-materials index of record); no content quotes were needed for these records.
- Pack spec: `evidence/EXP-01/pack_spec.json` (agent-authored extraction plan,
  committed to the run record). Pack sha256 recorded in the run manifest.

## Limitations / Coverage Gaps

- The book source is an image-only scan origin: quoted chunks carry parse-era OCR
  garble verbatim (e.g. line 263's mid-sentence garble). Quotes are never silently
  repaired; where a quote is unusable the record paraphrases and cites instead.
- Eight core concepts is a deliberate slice, not the whole of Topic 1: electrolysis,
  the mole calculations and the periodic-table trends get their own records in sibling
  EXP artifacts rather than compressed ones here.
- Statement anchors for Topic 2(f)/(g) acids/salts are page-level only in this run's
  packs (spec p. 22 carries Topic 2's opening statements 2.1–2.8C); the acid statements
  further into the topic are not quoted numerically from the pack and are therefore
  not claimed as per-statement anchors.
- SME-note sources (SRC-SME-NOTES-4CH1, SRC-SME-EXAMQ-4CH1) failed preflight and stay
  disclosed gaps; no classroom-validated review has occurred beyond the recorded
  educational review of this run.

## Research Status

Status GENERATED under SIB-GEN run SIB-CHEMISTRY_4CH1-RUN-004 (BL-008 pass 3, EXP
family). Structural QA passed against the validator of record; evidence-claim QA
passed with zero violations; educational review against the five pilot acceptance
criteria passed. This artifact is research output, not canonical curriculum truth;
staging and publication remain operator gates.
