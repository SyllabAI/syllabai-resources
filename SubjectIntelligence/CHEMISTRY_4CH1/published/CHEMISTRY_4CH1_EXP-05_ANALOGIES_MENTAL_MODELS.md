---
sib_protocol: SIB-1.0
artifact_id: EXP-05
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

# EXP-05 — Analogies & Mental Models

## Purpose

This artifact collects the analogies and mental models that carry 4CH1 chemistry —
including the ones the book of record itself uses, and, critically, the places where
each model stops matching reality. An analogy in this artifact is never decoration:
each record states what the model is, what it explains, what it gets wrong, and
therefore when a candidate must drop it and reason from particles directly. The
book's own practice is followed here — it introduces the brick-wall experience, the
planet-orbit warning, the gold-bar scale, and the PANiC mnemonic, and it is also the
source of the honest limit statements that accompany them. Every record is grounded
on the validated v3 chunk corpus at chunk identity. This is a research artifact; it
does not promote itself into canonical educational truth (Subject Intelligence Build
v1, §5).

## Scope

**Covers:** eight model records (EXP-033 … EXP-040): the brick wall and the swim;
the planet-orbit model and why the book flags it as misleading; gold bars and the
mole's scale; dot-and-cross diagrams as conventions rather than pictures; PANiC and
the mobile-charge rule it rides on; the sealed container as the precondition of
equilibrium; the white smoke ring as diffusion made visible; and the noble-gas
configuration as a target state, with its transition-metal failure.

**Does not cover:** the full explanations behind each model (EXP-01), simple
registers (EXP-02), depth extensions (EXP-03), route comparisons (EXP-04),
terminology distinctions (EXP-06), mechanism records (EXP-07), and why-question
formats (EXP-08). No legacy content entered any pack.

## Executive Summary

- Eight records; every model is paired with its documented limits, and three limits
  come from the book's own margin notes rather than from the agent.
- The planet-orbit record is the artifact's spine: it is the book explicitly teaching
  the skill of doubting a mental model.
- 44 chunks / 38,772 bounded chars in this pack; spec pages 17, 18, 19, 20, 21, 27, 28.

## Main Analysis

### EXP-033 — The brick wall and the swim: states as crowd behaviour

**The model:** particles in a solid are a packed crowd behind a wall — you cannot get
through because "the particles can't move out of your way"; particles in a liquid are
a crowd that yields — "You can swim through water because you can push the particles
out of the way"; particles in a gas are a sparse crowd you walk through easily "because
there are no forces between the particles".
**Where it works:** it converts the abstract triad of arrangement, movement and
energy (statement 1.1) into an experience every candidate already has, and it predicts
the density story — most liquids are less dense than the solid they freeze from
because their particles ended up slightly further apart.
**Where it breaks:** the model is static; it says nothing about why heating breaks
the crowd up. The interconversion mechanism needs energy added to the picture —
vibration outgrowing attraction (EXP-001's line-27 mechanism) — which the crowd
analogy does not carry.
**Evidence:** the everyday facts (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 23); the three key-point forces
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 25); the arrangement
and energy summary behind the model (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 26); spec 1.1 and 1.2 at
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p17).

### EXP-034 — Planets orbiting the sun: the model the book itself warns against

**The model:** electrons drawn as little planets circling a nuclear sun.
**Where it works:** as a cartoon it gets two things across — electrons are outside
the nucleus, and different electrons sit at different typical distances.
**Where it breaks:** the book's key point is blunt: electrons drawn "orbiting the
nucleus rather like planets around the sun. This can be misleading." Electrons are
always moving and "it is impossible to know exactly where they are at any moment in
time" — the honest picture is an energy and a likelihood of being found in a region of
space, which is what the shell model is an approximation to. The book is teaching the
meta-lesson with the warning attached: a model can be useful and wrong at the same
time, and the exam-level fix is to talk in shells and energies, not orbits.
**Evidence:** the misleading-orbits key point (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 88); spec 1.19 area at
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p18).

### EXP-035 — Gold bars and 6 × 10²³: thinking in moles

**The model:** scale calibration. A single gold bar holds "almost 4 × 10²⁵ gold
atoms. That's 4 followed by 25 noughts!" — and a mole is a fixed count of 6 × 10²³
particles whatever the substance, so 12 g of carbon-12, 24 g of magnesium and 18 g of
water all contain the same number of particles.
**Where it works:** it gives the mole a size in the imagination — atoms are so small
that even visible objects hold astronomical counts — and it explains why chemists
count in moles at all: reactions are particle-counting problems, and scales read mass,
so the mole is the exchange rate between the two (the route pair of EXP-025).
**Where it breaks:** the model invites "a mole is a big number and that's all" —
but the book's Niagara-falls figure (10³² water molecules per second) is there to
show the scale has structure: even absurdly large flows are countable, and the
Avogadro constant is a defined bridge, not a fuzzy "lots". The model must always be
attached to a formula — one mole of oxygen is ambiguous until O or O₂ is named.
**Evidence:** the gold-bar opener (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 134); the Avogadro definition and the
counting rationale (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl
line 165); spec 1.27 at (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p19).

### EXP-036 — Dots and crosses: diagrams as conventions, not photographs

**The model:** in dot-and-cross diagrams the electrons of the two reacting atoms are
drawn with different marks so their origins stay visible after transfer.
**Where it works:** it makes electron transfer and sharing countable and markable —
the exam skill of statement 1.40 is exactly this drawing — and the book's own rule
keeps it honest: "there is absolutely no difference between them in reality. The dots
and the crosses simply show that the electrons have come from two different atoms."
Two coloured dots would do the same job.
**Where it breaks:** the marks imply electron identity that does not exist, and the
diagram's neat outer shells imply the shells are the whole story (EXP-034's warning
applies to every drawn shell). The book adds the practical failure mode for the
diagram itself: candidates forget that the drawn species are ions — "don't forget the
charges on the ions" — so the model's commonest break is leaving the bracketed charge
off.
**Evidence:** the no-difference convention (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 270); the MgO worked diagram and its
charge reminder (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl
line 271); spec 1.40 at (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p20).

### EXP-037 — PANiC and the mobile-charge rule

**The model:** PANiC — "positive anode, negative (is) cathode" — a memory peg for
which electrode is which, riding on the deeper rule for conduction: "there must be
charged particles present and these charged particles must be free to move".
**Where it works:** the mnemonic never swaps, and the conduction rule beneath it
explains the whole pattern at once — ionic compounds don't conduct when solid because
"the ions are held tightly in position in the lattice", do conduct molten or dissolved
because "the ions then become free to move around", metals conduct by delocalised
electrons, and covalent molecular substances don't because their molecules carry no
overall charge. One rule, four material classes sorted.
**Where it breaks:** mnemonics carry no mechanism — PANiC says nothing about why
the ions move to those electrodes, and it silently hides the exception the book
records: covalent compounds that ionise on dissolving (ammonia solution, hydrogen
chloride in water) DO conduct, because the rule is mobile charges, not "covalent means
no conduction". The fix is to always answer conduction questions through the rule,
using the mnemonic only for electrode naming.
**Evidence:** the PANiC hint and the ionic conduction case (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 356); the conduction rule
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 355); spec 1.55C and
1.56C at (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p21).

### EXP-038 — The sealed container: why equilibrium needs a lid

**The model:** equilibrium as a reversible reaction that only gets the chance to
balance itself if nothing escapes — the book's squares model, where removing a yellow
square as it forms would drive the process one-way for ever.
**Where it works:** it converts "closed system" from a phrase into a causal
requirement: "you can set up a dynamic equilibrium only if the system is closed in a
sealed container". The calcium carbonate case makes it concrete — "If this were not
done in a closed container then all the CO₂ would escape and the reverse reaction
would not occur" — and it explains why industrial equilibria are run in enclosed
plant.
**Where it breaks:** the model is binary (open/closed) and says nothing about how
far the balance tips; reading position (EXP-031's Route B) needs the
condition-change machinery the squares model does not carry. It also quietly assumes
constant temperature — the one condition the squares room does not test.
**Evidence:** the calcium carbonate case (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 834); the sealed-container precondition
in the squares model (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl
line 833); spec Topic 3(c) area at (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p28).

### EXP-039 — The white smoke ring: diffusion made visible

**The model:** two cotton wool plugs — one soaked in concentrated ammonia solution,
one in concentrated hydrochloric acid — at the ends of a sealed glass tube; the gases
diffuse towards each other and "A white ring of solid ammonium chloride forms where
they meet", closer to the acid end because ammonia particles are lighter and faster.
**Where it works:** it turns an invisible process into a measurable race, and the
book's arithmetic behind it is a model in its own right: ammonia particles at about
600 m/s should cross a lab in 0.01 s, yet the smell takes a minute — "each ammonia
particle may have travelled 30 or more kilometres" of zigzag bouncing off air on the
way. Diffusion is fast per step and slow per journey.
**Where it breaks:** the race model suggests speed depends only on the racers; the
real constraint is the collision-rich medium (air in the tube, air in the lab). It
also hides that "concentrated" in the reagents is doing work as the gas source — the
distinction between concentration and strength is EXP-045's business, not this
model's.
**Evidence:** the tube demonstration (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 39); the diffusion arithmetic
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 34); spec 1.3 at
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p17).

### EXP-040 — Noble-gas configurations as a target state

**The model:** atoms react so as to reach the nearest noble gas's electron count —
sodium drops to [2,8] like neon, chlorine climbs to [2,8,8] like argon; "For the
first 20 elements, atoms lose or gain electrons so that they achieve a noble gas
electronic configuration."
**Where it works:** for the main-group block it is a fast, mostly-correct predictor
of ion charges (Groups 1/2/3 lose, Groups 5/6/7 gain), it explains the book's
"isoelectronic" vocabulary, and it even survives across periods (rubidium to krypton,
iodine to xenon).
**Where it breaks:** the book prints the counter-example in its own margin — an
Fe²⁺ ion, "definitely not a noble gas structure!" — so beyond the first twenty
elements and outside the main groups the target-state model fails, and the safe
ground truth reverts to the ion-charge list of statement 1.38. The model also risks
the causal exaggeration "atoms want noble gas configurations"; the book's phrasing
is a pattern description, not a desire, and EXP-019's attraction-and-distance
mechanism is the real driver where one is demanded.
**Evidence:** the isoelectronic key point (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 272); the target-state rule with the
Fe²⁺ failure case (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl
line 273); spec 1.38 area at (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p20).

## Evidence / Source Basis

- **Primary — SRC-BOOK-4CH1-SB1** (CURRENT — AUTHORITATIVE): validated v3 parse of
  the Pearson 4CH1 student book, cited at chunk identity. 44 chunks / 38,772 bounded
  chars in this pack.
- **Primary — SRC-SPEC-4CH1** (CURRENT — AUTHORITATIVE): Issue 3 specification PDF,
  page identity citations at pp. 17, 18, 19, 20, 21, 27, 28; statement numbers read
  from pack-visible excerpts only.
- **Supplementary — SRC-TL-4CH1**: identity-level presence only.
- Pack spec: `evidence/EXP-05/pack_spec.json`; pack sha256 in the run manifest.

## Limitations / Coverage Gaps

- Analogy selection is bounded by the book's own models and margins; no imported
  analogies (simulation-based or otherwise) are recorded here, so the artifact is as
  conservative as its source.
- Where the book gives no explicit limit for a model it uses informally, the limit
  statement in this artifact is the agent's pedagogical analysis, grounded on the same
  chunk text but not itself a quotation — such passages are phrased as analysis, and
  no quotation marks are placed on them.
- The analogies do not cover quantitative topics (titration arithmetic, yield) where
  the book's own worked examples are the better mental model; those belong to a
  future PED-family pass.
- OCR-origin garble in quoted chunks is quoted verbatim and never repaired.

## Research Status

Status GENERATED under SIB-GEN run SIB-CHEMISTRY_4CH1-RUN-004 (BL-008 pass 3, EXP
family). Structural QA passed at the validator of record; evidence-claim QA passed
with zero violations; educational review against the five pilot acceptance criteria
passed. Research output, not canonical curriculum truth; staging and publication
remain operator gates.
