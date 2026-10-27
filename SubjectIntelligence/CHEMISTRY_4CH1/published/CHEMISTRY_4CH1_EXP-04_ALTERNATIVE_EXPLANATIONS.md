---
sib_protocol: SIB-1.0
artifact_id: EXP-04
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

# EXP-04 — Alternative Explanations

## Purpose

This artifact collects the alternative routes to the same chemistry: cases where the
4CH1 book of record itself presents two or more legitimate ways to reach one conclusion
— two ways to count a mole, two definitions of oxidation, two readings of an
equilibrium — and teaches when each route is the better tool. The value of an
alternative explanation is diagnostic: a candidate stuck on one route can often be
unlocked by the other, and the pair together proves the result is not an artefact of
one derivation. Every route recorded here is taken from the book's own text, grounded
on the validated v3 chunk corpus at chunk identity, and anchored to specification
statements visible in the run's evidence pack. This is a research artifact; it does
not promote itself into canonical educational truth (Subject Intelligence Build v1,
§5).

## Scope

**Covers:** eight route-pair records (EXP-025 … EXP-032): counting moles by particles
versus by mass and Mr; balancing equations as atom bookkeeping versus systematic
element-by-element checking; the oxygen-based versus electron-based definition of
oxidation; displacement read as substitution versus competition; the four practical
routes to a soluble salt; rate curves read graphically versus by collision theory;
equilibrium read as equal rates versus as a position that shifts; and the isoelectronic
shortcut for predicting ion charges, with its documented failure case.

**Does not cover:** the core and simple registers (EXP-01/EXP-02), depth extensions
(EXP-03), analogies (EXP-05), fine distinctions (EXP-06), single-mechanism
why-it-works records (EXP-07), and why-question formats (EXP-08). No legacy content
entered any pack.

## Executive Summary

- Eight records, each grounded on 2–4 book chunks; 30 chunks / 26,172 bounded chars
  in this pack; spec pages 17, 18, 19, 20, 22, 27, 28.
- The book's own rule for choosing between definitions is preserved verbatim where it
  exists ("Use whichever is simpler in the case you are asked about!").
- The isoelectronic record carries the book's own counter-example (Fe²⁺ is "definitely
  not a noble gas structure!"), so the shortcut teaches its own limits.

## Main Analysis

### EXP-025 — Counting a mole two ways: by particles and by mass

**Concepts:** mole; Avogadro constant; relative formula mass
**Specification anchor:** 1.27, 1.28 (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p19)
Temporal scope: CURRENT — AUTHORITATIVE
**Route A (counting):** one mole is a fixed count of particles — "1 mole of 12C …
would have a mass of 12g and contain … about 6 × 10²³ carbon atoms", and the same
count applies to anything: a mole of magnesium is 6 × 10²³ magnesium atoms, a mole of
water is 6 × 10²³ water molecules. This route answers "how many?".
**Route B (massing):** the same mole read on the balance — "You can measure the masses
of compounds on the same carbon-12 scale", giving water's relative formula mass of 18,
so one mole of water is 18 g. This route answers "how much does it weigh?", which is
what a practical scale actually reports.
**When each route helps:** the counting route explains why reacting ratios work at
all ("if we know the number of moles we also know how many particles are present");
the massing route is the one that turns exam questions into arithmetic, because Mr is
what you add up from the Periodic Table. The book adds the safety rule that makes both
routes work: always quote the formula — "1 mole of oxygen" could mean 16 g of atoms or
32 g of molecules.
**Evidence:** the counting route (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 165); the massing route
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 153); the
quote-the-formula rule (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 159); spec 1.27 and 1.28 at
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p19).

### EXP-026 — Balancing equations: atom bookkeeping or systematic audit

**Concepts:** balanced equation; conservation of atoms
**Specification anchor:** 1.25 (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p19)
Temporal scope: CURRENT — AUTHORITATIVE
**Route A (bookkeeping):** reactions only "move their atoms around into new
combinations", so "you must always end up with the same number of atoms that you
started with". The unbalanced methane equation visibly fails this audit — it seems to
gain an oxygen and lose two hydrogens — and since "the substances are all correct, the
proportions must be wrong". Balancing is then just adjusting the proportions until the
atom census closes: "There are now the same number of each type of atom before and
after."
**Route B (systematic audit):** the book's procedure — work across the equation left
to right, one element at a time; count unchanged groups like sulfate as whole blocks;
re-check everything at the end. This is the route that scales to big equations, and the
book's halving note belongs to it: fractions are legal in principle ("it is acceptable
to have halves in equations") and doubling clears them when whole numbers are wanted.
**Evidence:** the conservation framing (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 138); the balanced methane census
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 140); the halves key
point (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 143); spec
1.25 at (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p19).

### EXP-027 — Two definitions of oxidation — and the book's rule for choosing

**Concepts:** oxidation; reduction; oxidising agent; reducing agent
**Specification anchor:** Topic 2(d) area of record (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p22)
Temporal scope: CURRENT — AUTHORITATIVE
**Route A (oxygen-based):** oxidation as gaining oxygen, reduction as losing it — the
older definition that matches combustion and metal-extraction examples directly.
**Route B (electron-based):** oxidation as electron loss, reduction as electron gain,
with agents defined reciprocally: "An oxidising agent is something that oxidises
something else by taking electrons away from it", while a reducing agent gives
electrons and is itself oxidised. The copper-in-silver-nitrate case shows the electron
route at work: copper gives electrons to Ag⁺ ions and is itself oxidised.
**The book's rule for choosing:** "You now have two definitions of oxidation (and its
reverse, reduction). Which one should you use? Use whichever is simpler in the case you
are asked about! Both definitions are true." The deep reason both work is that the
reactions are coupled — "if something gains electrons, it has to get them from
somewhere, so something else must lose electrons".
**Evidence:** the both-definitions hint (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 503); the copper/silver-nitrate worked
case with agent roles (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 505); spec Topic 2(d) area at
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p22).

### EXP-028 — Displacement as substitution — or as a competition

**Concepts:** displacement; competition; ionic equation; spectator ions
**Specification anchor:** 2.7 (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p22)
Temporal scope: CURRENT — AUTHORITATIVE
**Route A (substitution):** a more reactive element takes the place of a less
reactive one in a compound — hydrogen displaces copper from copper oxide, copper
displaces silver from silver nitrate ("Silver is below copper in the reactivity
series"), zinc displaces copper from copper(II) sulfate with the blue colour fading.
**Route B (competition):** the same events read as contests for electrons — the book's
own parenthetical calls displacement "a displacement (or competition) reaction", and
the ionic equation shows why: stripping the sulfate spectators leaves zinc atoms and
copper ions fighting over two electrons, which is exactly the redox framing of
EXP-027's Route B.
**When each route helps:** the substitution route predicts products fast (metal plus
salt solution, swap by reactivity); the competition route explains why the reaction
happens at all and links Topic 2 to the electron story.
**Evidence:** the competition parenthetical and the CuO/hydrogen case
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl lines 186 and 187); the
zinc/copper(II) sulfate case with spectator-ion stripping (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 502); the copper/silver-nitrate
substitution case (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl
line 505); spec 2.7 at (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p22).

### EXP-029 — Four routes to a soluble salt

**Concepts:** soluble salt preparation; metal; base; carbonate; indicator choice
**Specification anchor:** Topic 2(g) area of record (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p22)
Temporal scope: CURRENT — AUTHORITATIVE
**The routes:** the book's list for making a soluble salt (sodium, potassium and
ammonium salts excepted) is one reaction family with three solid reagent options —
"acid + metal (but only for the moderately reactive metals from magnesium to iron in
the reactivity series)"; "acid + metal oxide or hydroxide"; "acid + carbonate" — and
the method is "basically the same" for all. The base route's mechanism is the neutral
core of all four: bases "neutralise acids by combining with the hydrogen ions in them
to produce water", leaving the salt as the other product; the alkalis that dissolve in
water (Group 1 oxides and hydroxides, ammonia solution) are the soluble subset of the
same idea.
**When each route helps:** carbonate route for speed ("Carbonates react with dilute
acids in the cold"); oxide/hydroxide route when a solid must be added in excess and
filtered off; metal route only in the safe middle of the reactivity series; and the
indicator note that closes the loop — methyl orange runs red to yellow with an orange
endpoint, which is the practical signal the reaction is complete.
**Evidence:** the route list (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 616); the base mechanism
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 607); alkalis as
hydroxide-ion sources (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 608); the methyl-orange endpoint note
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 622); spec Topic
2(g) area at (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p22).

### EXP-030 — Reading a rate curve: graphically or by collision theory

**Concepts:** rate graph; collision theory; activation energy; successful collision
**Specification anchor:** 3.9, 3.11 (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p28)
Temporal scope: CURRENT — AUTHORITATIVE
**Route A (graphical):** the curve itself is the first explanation — steep means
fast, flat means finished. "Where the graph is falling most quickly (is steepest), it
shows that the reaction is fastest", and the graph "becomes horizontal because the
reaction has stopped when all the acid has been consumed". The rate definition
underneath is plain: change in amount per unit time.
**Route B (collision theory):** the same shape explained by particles — reactions
need collisions with at least the activation energy, "The collisions with energy
greater than or equal to the activation energy are usually called successful
collisions", and as acid particles are used up the collision rate falls, so the curve
flattens. Temperature's lever also lands here: hotter particles collide more often but
that "only accounts for a small part of the increase in rate" — the big effect is the
swell in the population of particles above activation energy.
**When each route helps:** Route A reads any curve in seconds; Route B is what the
explanatory marks pay for — and the book's pairing of the two is exactly statement
3.11's demand.
**Evidence:** the graphical reading (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 791); the rate definition
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 784); the temperature
analysis (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 807); spec
3.9 and 3.11 at (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf
p28).

### EXP-031 — Equilibrium: equal rates or shifting position

**Concepts:** dynamic equilibrium; forward/reverse rate; position of equilibrium
**Specification anchor:** Topic 3(c) area of record (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p28)
Temporal scope: CURRENT — AUTHORITATIVE
**Route A (equal rates):** equilibrium is what the book's blue-and-yellow-squares
model shows — both reactions still running, "the rate of the forward reaction is equal
to the rate of the reverse reaction", totals constant. The exam trap is built into the
picture: "the concentrations of the reactants and products at equilibrium are constant,
they are not equal."
**Route B (position):** the same system described by where the balance sits — the
forward reaction defined as the left-to-right direction, the position of equilibrium
"to the left" or "to the right" as conditions change, with the arithmetic of A and B
at equilibrium illustrating that absolute amounts do not matter, only the direction of
change.
**When each route helps:** Route A answers "what is happening at equilibrium?"
(dynamic, not stopped); Route B answers "what happens when we change conditions?" —
and the closed-system precondition recorded in EXP-038 applies to both.
**Evidence:** the dynamic key point (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 838); the constant-not-equal hint and the
squares model (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 833);
the forward/reverse and position definitions (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 835); spec Topic 3(c) area at
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p28).

### EXP-032 — The isoelectronic shortcut, and where it breaks

**Concepts:** isoelectronic; noble gas configuration; ion charges
**Specification anchor:** 1.19 (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p18)
Temporal scope: CURRENT — AUTHORITATIVE
**The shortcut:** for the first twenty elements, "atoms lose or gain electrons so that
they achieve a noble gas electronic configuration" — sodium's [2,8,1] sheds one
electron to become [2,8], "isoelectronic" with neon. The word itself means "have the
same number of electrons", and the shortcut predicts Group 1/2/3 cations and Group
5/6/7 anions in one step, even across periods (rubidium ending up isoelectronic with
krypton).
**Where it breaks:** the book's own margin shows an Fe²⁺ ion — "definitely not a
noble gas structure!" — because transition-metal ion formation does not follow the
noble-gas target at all. The shortcut is therefore a model for the main-group s/p
block, not a law; the correct general rule remains the ion list and charges of
statement 1.38.
**Evidence:** the isoelectronic definition (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 272); the noble-gas-configuration rule
and its transition-metal failure case (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 273); spec 1.19 at (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p18).

## Evidence / Source Basis

- **Primary — SRC-BOOK-4CH1-SB1** (CURRENT — AUTHORITATIVE): validated v3 parse of the
  Pearson 4CH1 student book, cited at chunk identity. 30 chunks / 26,172 bounded chars
  in this pack.
- **Primary — SRC-SPEC-4CH1** (CURRENT — AUTHORITATIVE): Issue 3 specification PDF,
  page identity citations at pp. 17, 18, 19, 20, 22, 27, 28; statement numbers read
  from pack-visible excerpts only.
- **Supplementary — SRC-TL-4CH1**: identity-level presence only.
- Pack spec: `evidence/EXP-04/pack_spec.json`; pack sha256 in the run manifest.

## Limitations / Coverage Gaps

- Route pairs are limited to what the book itself presents as alternative or
  complementary framings; no external pedagogy was imported, so routes the book does
  not offer (e.g. formal equilibrium constants) are absent — correctly, since they are
  beyond the specification.
- The oxidation-definitions record anchors at Topic 2(d) page level: the redox
  statements themselves sit further into the topic than the pack's bounded p. 22
  excerpt reaches, so no redox statement number is claimed.
- The isoelectronic record inherits the book's own limit (transition metals) rather
  than adding the fuller d-block account, which no pack source carries.
- OCR-origin garble in quoted chunks is quoted verbatim and never repaired.

## Research Status

Status GENERATED under SIB-GEN run SIB-CHEMISTRY_4CH1-RUN-004 (BL-008 pass 3, EXP
family). Structural QA passed at the validator of record; evidence-claim QA passed
with zero violations; educational review against the five pilot acceptance criteria
passed. Research output, not canonical curriculum truth; staging and publication
remain operator gates.
