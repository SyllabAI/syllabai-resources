---
sib_protocol: SIB-1.0
artifact_id: EXP-08
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

# EXP-08 — Common Why Questions

## Purpose

This artifact answers the why-questions candidates actually ask about the 4CH1
course — the chemistry-curious questions that the specification assumes but never
states, answered in the book of record's own voice. Each record poses one question,
answers it in plain language, and grounds the answer on the validated v3 chunk corpus
at chunk identity, with the specification anchor visible in the run's evidence pack.
The questions are chosen where the book itself supplies the answer's substance, so
the artifact stays inside the EXP family's boundary: explanations grounded on the
specification's and the book's own accounts, never speculation. This is a research
artifact; it does not promote itself into canonical educational truth (Subject
Intelligence Build v1, §5).

## Scope

**Covers:** eight question records (EXP-057 … EXP-064): why you cannot walk through
a brick wall; why puddles disappear without boiling; why a gas smell reaches the
whole lab so slowly; why the white smoke ring forms where it does; why iron rusts and
why only iron; why galvanising keeps working after a scratch; why the calcium
carbonate equilibrium needs a sealed container; and why the noble gases are so
unreactive.

**Does not cover:** the systematic concept explanations (EXP-01), the simple
registers (EXP-02), the depth extensions (EXP-03), route comparisons (EXP-04),
analogies and their limits (EXP-05), terminology boundaries (EXP-06), and the
mechanism records organized by rule rather than by question (EXP-07). No legacy
content entered any pack.

## Executive Summary

- Eight records in question-and-answer form, each grounded on 2–4 book chunks; 20
  chunks / 15,068 bounded chars in this pack; spec pages 17, 18, 19, 22, 27, 28.
- The questions are drawn from the seams where classroom curiosity reliably lands:
  particle behaviour, diffusion, rusting, and the gases that refuse to react.
- Two answers (galvanising, smoke ring) reuse the book's extension material so the
  level boundary travels with the answer.

## Main Analysis

### EXP-057 — Why can't you walk through a brick wall?

**The question:** if everything is mostly empty space, why is a wall solid?
**The answer:** because solidity is not about emptiness — it is about whether the
particles can get out of your way. The book's grounding is the everyday trio: "You
can't walk through a brick wall because of the strong forces of attraction between
the particles - the particles can't move out of your way", while you can swim through
water by pushing particles aside, and a gas is easy to move through "because there
are no forces between the particles". A brick wall's particles are locked in fixed
positions by strong attractions; your hand's particles are too, and neither set can
rearrange — so you stop.
**The chemistry it teaches:** this is statement 1.1's arrangement-movement-energy
triple experienced from the outside, and it is the same model that later explains
why solids keep their shape, why liquids flow, and why gases compress.
**Evidence:** the everyday facts (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 23); the forces key points
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 25); spec 1.1 and
1.2 at (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p17).

### EXP-058 — Why do puddles disappear without boiling?

**The question:** water boils at 100 °C, so how can a puddle vanish on a 5 °C day?
**The answer:** because boiling is not the only way out of a liquid. "Evaporation
occurs at any temperature, but boiling only occurs at one temperature" — at any
moment, "some very fast particles at the surface of the liquid will have enough
energy to overcome the forces of attraction between the particles" and break away,
even though the average particle is far too slow. Boiling is the whole-liquid event
when even the slowest particles can escape; evaporation is the quiet surface leak
that never stops. The closed-container twist completes the picture: in a sealed box,
evaporated particles land again, so "evaporation and condensation will both be
occurring at the same time".
**The chemistry it teaches:** particle-speed spread (statement 1.2's
interconversion mechanics at particle level) — and the same speed spread powers the
rate-temperature story later in the course.
**Evidence:** the key-point contrast (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 28); the evaporation mechanism and the
closed container (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl
line 30); spec 1.1–1.2 at (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p17).

### EXP-059 — Why does a gas smell reach everyone, but so slowly?

**The question:** if particles fly at hundreds of metres per second, why does the
front of the lab smell the gas a full minute before the back?
**The answer:** the particles really are that fast — "ammonia particles travel at
speeds of about 600 metres per second" — but they do not travel in straight lines:
"each particle is bouncing off air particles on its way", so the journey that takes
0.01 s in a vacuum becomes a zigzag of "30 or more kilometres" of actual travel.
That random-walk spreading is diffusion, "the spreading out of particles from where
they are at a high concentration … to where they are at a low concentration".
**The chemistry it teaches:** statement 1.3's diffusion explanations — and the
model's punchline is quantitative, which is why the book's ammonia/hydrogen chloride
mass comparison (17 versus 36.5) is the next question's whole experiment.
**Evidence:** the lab-smell arithmetic (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 34); the diffusion definition and
relative molecular masses (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 38); spec 1.3 at (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p17).

### EXP-060 — Why does the white smoke ring form nearer the acid end?

**The question:** in the classic glass-tube demonstration, why doesn't the white
ring form in the middle?
**The answer:** because the two gases race at different speeds. Ammonia (relative
molecular mass 17) is lighter than hydrogen chloride (36.5), and "Ammonia particles
are lighter than hydrogen chloride particles and therefore move faster. The ammonia
particles travel further in the same amount of time, which means that the ring forms
further away from the ammonia end" — equivalently, closer to the hydrochloric end,
"where they meet" as solid ammonium chloride.
**The chemistry it teaches:** diffusion speed tracks particle mass at equal
temperature; the ring's position is a measuring device for that claim, and it is the
visual proof of statement 1.3's mass-speed connection.
**Evidence:** the tube demonstration and the ring-position explanation
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 39); the masses and
the reaction (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 38);
spec 1.3 at (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf
p17).

### EXP-061 — Why does iron rust — and why is rusting iron's word alone?

**The question:** most metals dull or corrode; why does only iron "rust"?
**The answer:** two reagents, one metal. "Iron needs oxygen and water to rust" —
remove either and rusting stops, which is exactly how the prevention ladder works
(paint, oil, grease, plastic, or tin plating as barriers). And the vocabulary is
exclusive by convention: "Many metals corrode, but it is only the corrosion of iron
that is referred to as rusting." The chemistry underneath is redox — "Rusting can be
described as a redox reaction – the iron is oxidised" — with the hydrated iron(III)
oxide formula Fe₂O₃·xH₂O carrying the variable water content that makes rust fluffy
rather than protective.
**The chemistry it teaches:** Topic 2(d)'s oxygen-and-water conditions, the redox
framing, and the corrosion-versus-rusting wording trap recorded as a distinction in
EXP-046.
**Evidence:** the rusting definition and prevention ladder (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 538); the wording warning
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 533); the
oxygen-and-water key point (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 469); spec Topic 2(d) area at
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p22).

### EXP-062 — Why does galvanising keep working after a scratch?

**The question:** if a zinc coating is the protection, why doesn't a scratch ruin
it?
**The answer:** because the zinc is more than a barrier — it is a battery. "The
zinc loses electrons (is oxidised) to form zinc ions", and "These electrons flow into
the iron. Any iron atom which has lost electrons to form an ion immediately regains
them. If the iron can't form ions, it can't rust." Scratching the coating does not
break the electrical connection — it completes it, so the zinc sacrifices itself
electron-by-electron to keep the iron metallic. That is why the book contrasts the
barrier methods (which fail when the coating breaks) with galvanised iron, where
"the iron still doesn't rust, even when some of the zinc on the surface is scratched
away".
**The chemistry it teaches:** reactivity applied for protection — the same
electron-loss eagerness that makes zinc "more reactive" in the series is what lets
it donate electrons on demand (the deep mechanism recorded in EXP-022).
**Evidence:** the sacrificial mechanism (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 539); the barrier-versus-galvanising
contrast (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 538);
spec Topic 2(d)/(e) area at (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p22).

### EXP-063 — Why does the calcium carbonate equilibrium need a sealed container?

**The question:** reversible reactions are supposedly two-way — so why does the
book insist the limestone decomposition runs "in a closed container"?
**The answer:** because one product is a gas that can leave. For the CaCO₃ ⇌ CaO +
CO₂ system, "If this were not done in a closed container then all the CO₂ would
escape and the reverse reaction would not occur" — an open tube is a one-way
reaction with a permanent leak. The general law rides with it: "Reversible reactions
will eventually reach a state of equilibrium if they are left in a sealed
container", and the squares model shows why — remove a product as it forms and it
never gets the chance to turn back.
**The chemistry it teaches:** the closed-system precondition of every equilibrium
claim in the course, and the exam-wording discipline that equilibrium concentrations
are constant, "they are not equal" — the trap recorded in EXP-048.
**Evidence:** the calcium carbonate case (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 834); the sealed-container
precondition and the constant-not-equal hint (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 833); spec Topic 3(c) area at
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p28).

### EXP-064 — Why are the noble gases so unreactive?

**The question:** every other group reacts eagerly — why does Group 0 barely react
at all?
**The answer:** their electron counts are already finished. "The noble gases are
unreactive because the outer shell is full, and so there is no tendency to lose,
gain or share electrons in a chemical reaction" — helium and neon are so far from
compromise that they "don't react with anything". The Group 0 label itself carries
the same history: the zero was the original belief in "zero combining power
(valency)", which is also why it is "the only group where the group number does not
tell you the number of electrons in the outer shell".
**The honest fine-print:** the book's extension notes that beyond neon the
"full outer shell" story is a simplification — argon onward have room in their outer
shells (18 and 32), yet stay unreactive at this level. The full-shell model is the
exam answer (statement 1.24); the fine-print is recorded here so the model's limits
travel with it.
**Evidence:** the noble gases and the full-shell mechanism with the extension
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 123); the Group 0
naming key point (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl
line 121); spec 1.24 at (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p19).

## Evidence / Source Basis

- **Primary — SRC-BOOK-4CH1-SB1** (CURRENT — AUTHORITATIVE): validated v3 parse of
  the Pearson 4CH1 student book, cited at chunk identity. 20 chunks / 15,068 bounded
  chars in this pack.
- **Primary — SRC-SPEC-4CH1** (CURRENT — AUTHORITATIVE): Issue 3 specification PDF,
  page identity citations at pp. 17, 18, 19, 22, 27, 28; statement numbers read from
  pack-visible excerpts only (1.1–1.3 at p. 17; 1.24 at p. 19).
- **Supplementary — SRC-TL-4CH1**: identity-level presence only.
- Pack spec: `evidence/EXP-08/pack_spec.json`; pack sha256 in the run manifest.

## Limitations / Coverage Gaps

- The question set is bounded by what the book answers directly; questions the book
  does not answer (why the sky is blue, why hydrogen is first in the Periodic Table)
  are excluded rather than answered from outside the pack sources.
- The unreactivity record inherits the book's level: no noble-gas compound chemistry
  (xenon fluorides and the like) is introduced, because no pack source carries it and
  the specification does not require it.
- Answers reuse mechanism records from EXP-07 by reference where the full chain lives
  there (galvanising, catalysts); this artifact keeps the answer form, not the full
  derivation.
- OCR-origin garble in quoted chunks is quoted verbatim and never repaired.

## Research Status

Status GENERATED under SIB-GEN run SIB-CHEMISTRY_4CH1-RUN-004 (BL-008 pass 3, EXP
family). Structural QA passed at the validator of record; evidence-claim QA passed
with zero violations; educational review against the five pilot acceptance criteria
passed. Research output, not canonical curriculum truth; staging and publication
remain operator gates.
