---
sib_protocol: SIB-1.0
artifact_id: EXP-07
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

# EXP-07 — Why It Works

## Purpose

This artifact holds the mechanism-first explanations of the 4CH1 course: records that
answer "why does that rule hold?" rather than restating the rule. Each record takes
one rule that candidates learn as a fact — high melting points, conduction patterns,
the Group 0 label, the catalyst's non-effect — and rebuilds it from the structure-and-
forces ground floor using the book of record's own causal chains. The discipline is
the EXP family's forbidden-law boundary: no mechanism may contradict the
specification's own definitions, and where the specification expects a rule without
mechanism (chemistry-only statements excepted), the record says so. Every causal claim
is grounded on the validated v3 chunk corpus at chunk identity. This is a research
artifact; it does not promote itself into canonical educational truth (Subject
Intelligence Build v1, §5).

## Scope

**Covers:** eight mechanism records (EXP-049 … EXP-056): why giant ionic lattices
melt high; why diamond is hard, graphite slippery and only one of them conducts; why
metals conduct and bend; why Group 0 is numbered 0; why conduction needs mobile
charges; why the most reactive metals are the hardest to win back; why a catalyst
cannot shift an equilibrium's position; and why the C=C bond makes alkenes the more
reactive family.

**Does not cover:** the rule-statements themselves in core register (EXP-01),
simple registers (EXP-02), depth extensions beyond mechanism (EXP-03), route
comparisons (EXP-04), analogies (EXP-05), terminology distinctions (EXP-06), and
why-question formats (EXP-08). No legacy content entered any pack.

## Executive Summary

- Eight records, each a rule → mechanism chain carried on 2–4 book chunks; 41 chunks
  / 38,707 bounded chars in this pack; spec pages 17, 18, 19, 20, 21, 22, 27, 28, 29.
- The catalyst record resolves the specification's own demand ("Understand why a
  catalyst does not affect the position of equilibrium") exactly as the book does:
  same-factor speed-up on both directions, so position cannot move.
- The graphite record carries the book's most surprising mechanism note: the
  famous layer-slide lubrication does not work in a vacuum.

## Main Analysis

### EXP-049 — Why ionic compounds have high melting points

**The rule:** ionic compounds melt and boil high (statement 1.42).
**The mechanism:** the lattice is a regular array of alternating charges, so melting
means fighting the attraction between every ion and its oppositely charged neighbours
— the book's chain runs straight from definition to consequence: electrostatic
attraction is "positively charged particles attract negatively charged particles",
and "lonic compounds have high melting points and boiling points because of the strong
electrostatic forces of attraction holding the lattice together. A lot of energy has
to be supplied to break the strong electrostatic forces of attraction between
oppositely charged ions in the giant lattice structure." The crystallinity of ionic
solids is the same regularity seen from outside — magnesium oxide is a white powder
only because its single crystals are too small to see.
**Boundary note:** the mechanism explains melting against attractions, not
conduction: ions in the solid are locked, which is why conduction must wait for
molten or dissolved states (EXP-053's record).
**Evidence:** the property explanation (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 296); the electrostatic definition and
the transfer that builds the lattice (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 269); spec 1.41 and 1.42 at
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p20).

### EXP-050 — Why diamond is hard, graphite is a lubricant, and only one conducts

**The rule:** carbon's giant structures behave completely differently from its
molecular ones.
**The mechanism:** diamond is a single covalent network — "it continues on and on in
three dimensions. It is not a molecule because the number of atoms joined up in a
real diamond is completely variable" — so melting it means breaking genuine
carbon-carbon covalent bonds throughout, "there are no intermolecular forces (it has
a giant structure, there are no molecules)". That is the deep contrast with simple
molecular substances, which melt easily because only weak intermolecular forces
break, not bonds. Every carbon in diamond has committed all four outer electrons to
bonds, so "Diamond doesn't conduct electricity. All the electrons in the outer shells
of the carbon atoms are tightly held in covalent bonds."
**The book's surprise:** the familiar "layers slide" story for graphite's
lubrication is more complicated than it looks — "graphite is not a lubricant in a
vacuum. Graphite being a lubricant relies on water molecules sticking to the surface".
The teaching model works in air; the mechanism has a documented water-assist.
**Evidence:** the giant-structure and melting chain (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 333); the intermolecular-forces contrast
and diamond's conduction failure (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 334); the vacuum caveat
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 336); spec 1.44 and
1.45 at (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p20).

### EXP-051 — Why metals conduct and bend: delocalised electrons

**The rule:** metals conduct electricity and heat, and can be hammered into shape
(statement 1.54C).
**The mechanism:** the metallic lattice is positive ions in "a sea of delocalised
electrons" — electrons freed from individual atoms and owned by the whole structure.
Conduction is then immediate: "Metals conduct electricity because the delocalised
electrons are free to move throughout the structure." Malleability follows from the
same non-directional bonding: the ions sit in a uniform electron sea, so layers can
shift without snapping specific bonds. And the model is quantitative — sodium
delocalises one electron per atom (1+ ions, weaker bonding, soft, low melting point)
while magnesium delocalises two (2+ ions, "a much stronger electrostatic attraction",
higher melting point), which is why the metals' property list carries the exceptions
note: mercury is a liquid.
**Evidence:** delocalisation (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 345); the Na/Mg contrast and conduction
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 349); the metal
property list (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 132);
spec 1.53C and 1.54C at (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p21).

### EXP-052 — Why Group 0 is numbered 0

**The rule:** the noble gases' group number does not count outer electrons.
**The mechanism:** the zero is historical chemistry, not arithmetic — "when they
were first discovered it was believed that noble gases did not combine with anything,
they had zero combining power (valency)". The unreactivity itself has an
electronic mechanism: "The noble gases are unreactive because the outer shell is
full, and so there is no tendency to lose, gain or share electrons" — helium and
neon "don't react with anything" at all. The book's extension adds the honest
fine-print that only helium and neon truly have full outer shells (the third holds
18, the fourth 32), which is the same subshell seam EXP-017 records — at this level
the full-shell model is the expected tool.
**Boundary note:** the full-shell explanation is the exam answer for statement 1.24;
the "eight electrons" phrasing must not be over-generalised to helium (two).
**Evidence:** the Group 0 naming key point (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 121); the noble gases and the full-shell
mechanism with its extension (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 123); spec 1.24 at (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p19).

### EXP-053 — Why conduction needs mobile charges

**The rule:** solids that never conduct may conduct once melted or dissolved
(statements 1.43, 1.55C, 1.56C).
**The mechanism:** the book reduces conduction to one criterion — "there must be
charged particles present and these charged particles must be free to move" — and
sorts every material class with it. Ionic solids fail because "the ions are not free
to move"; molten or aqueous ionic compounds pass because the ions then are; metals
pass even solid because "the delocalised electrons are free to move"; covalent
molecular substances fail in every state because their molecules are uncharged and
their electrons locked in bonds. The book's closing contrast is the discipline the
exams test: "ionic substances: ions move … metals: electrons move" — name the
carrier, not just "charges".
**Evidence:** the conduction criterion (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 355); the four-class sorting key point
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 348); spec 1.43 and
1.55C–1.56C at (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p20 and p21).

### EXP-054 — Why the most reactive metals are the hardest to win back

**The rule:** electrolysis and reduction favour the less reactive; the reactive ones
stay ions.
**The mechanism:** reactivity is electron-dropping ease, so the reverse process must
be electron-regaining difficulty — "The more reactive something is, the greater
tendency it has to form an ion. This means that the more reactive something is, the
more difficult it is to turn it back into an atom." That single sentence is why
reactive metals (sodium, potassium, aluminium above carbon) resist displacement and
electrolytic deposition, and why the historical extraction methods track the
reactivity series — the metal that drops its electron most eagerly is the one the
electron must be forced back onto hardest.
**Boundary note:** the record stops where the book stops: the same key point
continues into electrolysis product rules (EXP-021), and no electrode-potential
account is added because the specification and book do not carry one.
**Evidence:** the reactive-ion key point (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 375); spec Topic 2(d) area at
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p22).

### EXP-055 — Why a catalyst cannot shift an equilibrium's position

**The rule:** catalysts speed reactions up but leave reversible systems at the same
position (the specification's own demand).
**The mechanism:** the book's summary makes the symmetry explicit — "Adding a
catalyst speeds up reactions. In a reversible change, it speeds up the forward and
reverse reactions by the same proportion. For example, if it speeds up the forward
reaction ten times, it speeds up the reverse reaction ten times as well." If both
directions accelerate equally, the crossing point where the rates meet — the
equilibrium of EXP-031's Route A — moves not at all: "there is no change in the
position of equilibrium if you add a catalyst. The catalyst is added to increase the
rate at which equilibrium is reached." Temperature, by contrast, acts asymmetrically
("the position of equilibrium shifts in the endothermic direction"), which is why it
moves position while the catalyst cannot.
**Evidence:** the catalyst summary (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 842); the specification-anchored
learning objectives (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl
line 828); the equal-rates key point (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 838); spec Topic 3(c) area at
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p28).

### EXP-056 — Why alkenes are more reactive than alkanes

**The rule:** alkanes are sluggish; alkenes add things across their double bond.
**The mechanism:** the bond inventory is the mechanism. The alkanes are "saturated
hydrocarbons because they contain only C-C single bonds" — every valence is spent,
which is what saturation means; the alkenes carry "a carbon-carbon double bond", and
they are "unsaturated compounds because they contain a C=C bond". The book's hint
gives the intuitive handle — the alkenes "are not saturated with H atoms, they do not
have the maximum number of H atoms for that number of C atoms" — so there is
reactivity to spend: the double bond can open and take on additional atoms, which is
exactly the addition behaviour that distinguishes the family, and which cracking
exploits by manufacturing alkenes from alkanes in the first place.
**Boundary note:** mechanism detail beyond "the C=C is there and reactive" (bond
enthalpies, electrophilic addition) is beyond both the book and the specification's
own note that "knowledge of reaction mechanisms is not required"; the record stops at
the structural difference, as statement 4.6 expects.
**Evidence:** the alkenes opener (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 955); the unsaturation hint
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 959); the
unsaturated definition (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 961); the saturated definition and its
exam warning (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 941);
spec 4.6 area at (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p29).

## Evidence / Source Basis

- **Primary — SRC-BOOK-4CH1-SB1** (CURRENT — AUTHORITATIVE): validated v3 parse of
  the Pearson 4CH1 student book, cited at chunk identity. 41 chunks / 38,707 bounded
  chars in this pack.
- **Primary — SRC-SPEC-4CH1** (CURRENT — AUTHORITATIVE): Issue 3 specification PDF,
  page identity citations at pp. 17–29 as listed per record; statement numbers read
  from pack-visible excerpts only (1.24 at p. 19; 1.41–1.45 at p. 20; 1.53C–1.56C at
  p. 21).
- **Supplementary — SRC-TL-4CH1**: identity-level presence only.
- Pack spec: `evidence/EXP-07/pack_spec.json`; pack sha256 in the run manifest.

## Limitations / Coverage Gaps

- Mechanisms are bounded by the book's level: no electrode potentials, no orbital
  overlap pictures, no bond-enthalpy arithmetic beyond the book's own statements —
  each omission matches a specification boundary rather than a source gap, and is
  recorded as such.
- The graphite lubrication record reflects the book's own extension claim; no
  independent tribology source entered the pack, so the vacuum caveat stands as
  book-of-record assertion.
- The catalyst mechanism is the book's proportionality argument; a rate-constant
  treatment is beyond the level and deliberately absent.
- Statement anchors for the organic records are page-level (p. 29 visible range
  4.1–4.7); the alkene statements further into the topic are not claimed numerically.
- OCR-origin garble in quoted chunks is quoted verbatim and never repaired.

## Research Status

Status GENERATED under SIB-GEN run SIB-CHEMISTRY_4CH1-RUN-004 (BL-008 pass 3, EXP
family). Structural QA passed at the validator of record; evidence-claim QA passed
with zero violations; educational review against the five pilot acceptance criteria
passed. Research output, not canonical curriculum truth; staging and publication
remain operator gates.
