
# MIS-02 — Concept Confusion Atlas

## Purpose

This artifact maps the concept-pair confusions that the official Pearson examiner corpus
records for Pearson Edexcel International GCSE Chemistry (4CH1): places where two
adjacent concepts, labels or vocabulary classes are systematically swapped, blended or
mis-applied by candidates. It extends the Misconception Atlas (MIS-01) at a finer grain —
where MIS-01 records what candidates get wrong, this atlas records which TWO things get
confused with each other. Every record is grounded on an official Pearson examiner report
for a named session and paper, carried in the run's evidence pack with page identity. It
is a research artifact: it does not promote these observations into canonical educational
truth (Subject Intelligence Build v1, §5).

**Claim-type labeling (BL-011, RUN-011):** records separate what the official
examiner corpus says from what SyllabAI infers from it and proposes for the classroom.
`[OBSERVED_IN_SOURCE]` marks fields whose content quotes or directly paraphrases the
cited official evidence (Evidence / Motivating evidence / Examiner guidance fields).
`[SIB_INFERENCE]` marks SyllabAI's own explanatory and diagnostic reasoning, grounded
on but not stated by that evidence (Why it occurs / Why the reasoning fails /
Diagnostic signals / Signal tested / Fail pattern / Pass pattern). `[PROPOSED_INTERVENTION]`
marks proposed classroom actions, not observed facts (Intervention ideas / Intervention /
Intervention note / Drill design / Success signal / Probe). The remaining record fields
(Concepts, Specification Points, Temporal scope, Assessment context, Misconception /
Error / The confusion, Correct understanding / distinction / reasoning / technique /
usage, Typical manifestation, Credit-worthy form) are record descriptors whose grounding
is the record's cited evidence. The per-record `Temporal scope: CURRENT — AUTHORITATIVE`
stamp carries the source-classification vocabulary defined in SOURCE_REQUIREMENTS.md
§4.1 (definitions of record).

## Scope

**Covers:** eight concept-confusion records (MIS-013 … MIS-020) grounded on the official
4CH1 examiner reports held by the library (8 sessions: 2019-06, 2022-06, 2023-06,
2023-11, 2024-06, 2024-11, 2025-06 as held; papers 1C/2C/1CR/2CR), each extracted into
the run's evidence pack with bounded page excerpts and page locators. Each record names
the two sides of the confusion, why the confusion arises, the correct distinction, the
typical manifestation in scripts, and diagnostic and intervention signals.

**Does not cover:** single-sided error catalogs (MIS-03), calculation technique (MIS-05),
terminology drills beyond the confusion grain (MIS-06), legacy 4CH0 sentiment, and any
session for which no public ER exists — those stay disclosed gaps, never filled by
invention.

## Executive Summary

- The corpus's most repeated confusion is halogens vs halide ions in displacement
  answers — flagged as "an on-going issue" across series.
- Bond-vs-intermolecular-force is the second recurring confusion, named in both an
  introduction and a long-response commentary.
- Several confusions are frame-level, not vocabulary-level: collision-theory language
  imported into a physical change, and chemical-equation responses to a change of state.
- Structure→property confusions (which particle moves) and naming confusions (oxidation
  states omitted) round out the atlas.

## Main Analysis

### MIS-013 — Halogens vs halide ions in displacement answers

**Concepts:** Group 7; halogens; halide ions; displacement
**Specification Points:** 2.20, 2.21
Temporal scope: CURRENT — AUTHORITATIVE
**The confusion:** the element class ("halogens": Cl2, Br2, I2) and the ion class
("halide ions": Cl-, Br-, I-) are used interchangeably, so displacement products get the
wrong suffix class.
**Why it occurs [SIB_INFERENCE]:** the -ine/-ide distinction is a naming-layer rule sitting on top of
genuinely-understood reactivity chemistry; under exam pressure the labels swap.
**Correct distinction:** a more reactive halogen displaces a less reactive halogen (the
element) from its halide solution — the displaced species is bromine/iodine (the
element), never bromide/iodide (the ion).
**Typical manifestation:** displacement word equations with -ide products; "halide ions"
where the element is meant.
**Diagnostic signals [SIB_INFERENCE]:** displacement items; ask candidates to label every species as
element or ion before writing.
**Intervention ideas [PROPOSED_INTERVENTION]:** examiners' own advice: "Teachers need to encourage them to use
the correct terminology when describing these reactions."
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2023 4CH1/1C, Introduction (SRC-ER-4CH1,
2023-06/4CH1-1C/er.pdf p3): "confusion between halogens and halide ions"; November 2023
4CH1/2C, Question 1 (SRC-ER-4CH1, 2023-11/4CH1-2C/er.pdf p3): "stating that chlorine
displaces bromide and iodide is incorrect rather than displaces bromine and iodine."

### MIS-014 — Covalent bond vs intermolecular force

**Concepts:** covalent bonding; intermolecular forces; physical properties
**Specification Points:** 1.38, 1.39
Temporal scope: CURRENT — AUTHORITATIVE
**The confusion:** bonds between atoms inside a molecule and forces between molecules
are treated as one concept; "intermolecular forces" is also used as an incantation in
long answers.
**Why it occurs [SIB_INFERENCE]:** everyday speech says "bonds hold it together" for both scales; both
concepts live in the same topic neighbourhood.
**Correct distinction:** melting/boiling overcomes intermolecular forces; the covalent
bonds within molecules survive the state change.
**Typical manifestation:** "the covalent bonds break when it melts"; vague
"intermolecular forces" phrasing in extended answers.
**Diagnostic signals [SIB_INFERENCE]:** "what breaks when X melts/boils"; audit long answers for exact
phrase usage.
**Intervention ideas [PROPOSED_INTERVENTION]:** diagram drill with the bond inside and the force between;
examiner-worded model sentences.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2023 4CH1/1C, Introduction (SRC-ER-4CH1,
2023-06/4CH1-1C/er.pdf p3): "Some candidates also do not fully understand the difference
between a bond between two atoms in a molecule, and an intermolecular force between
molecules"; June 2025 4CH1/1C, Introduction (SRC-ER-4CH1, 2025-06/4CH1-1C/er.pdf p3):
long-response candidates "lacked a firm grasp of key terminology (eg incorrect use of
intermolecular forces)".

### MIS-015 — Evaporation explained with reaction-collision language

**Concepts:** states of matter; evaporation; kinetic theory vs reaction kinetics
**Specification Points:** 1.2
Temporal scope: CURRENT — AUTHORITATIVE
**The confusion:** the rates-of-reaction frame (frequency of collisions) is imported into
a physical change.
**Why it occurs [SIB_INFERENCE]:** the collision-frequency explanation is heavily rehearsed and
over-applies to any "what happens when you heat" question.
**Correct distinction:** evaporation involves the more energetic particles at the surface
escaping the liquid; no reaction is occurring.
**Typical manifestation:** "particles collide more often so more evaporate."
**Diagnostic signals [SIB_INFERENCE]:** ask why heating increases evaporation rate; flag collision
answers.
**Intervention ideas [PROPOSED_INTERVENTION]:** contrast-pair drill: rate explanation vs evaporation explanation,
same stimulus.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report November 2023 4CH1/1C, Q1b (SRC-ER-4CH1,
2023-11/4CH1-1C/er.pdf p3): "Far fewer went on to explain that evaporation involves the
more energetic particles escaping the liquid. Some confused this process with reactions
by talking about greater frequency of collisions."

### MIS-016 — Change of state answered as a chemical change

**Concepts:** condensation; physical vs chemical change; state symbols
**Specification Points:** 1.2
Temporal scope: CURRENT — AUTHORITATIVE
**The confusion:** the instruction "write an equation" triggers a new-substance equation
where a state-symbol equation was asked.
**Why it occurs [SIB_INFERENCE]:** equation-writing is rehearsed as "always make a new substance
equation"; the state-change context is overridden by the cue.
**Correct distinction:** a change of state alters arrangement and energy, not the
molecules: H2O(g) → H2O(l).
**Typical manifestation:** an equation for the formation of water where condensation was
asked.
**Diagnostic signals [SIB_INFERENCE]:** any state-change equation item; check whether the formula changes
across the arrow.
**Intervention ideas [PROPOSED_INTERVENTION]:** physical-vs-chemical sort; state-symbol equation drills.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report November 2023 4CH1/1C, Q1c(ii) (SRC-ER-4CH1,
2023-11/4CH1-1C/er.pdf p3): "A few incorrectly wrote an equation for the formation of
water. They did not realise that a change of state does not alter the molecules
themselves."

### MIS-017 — "Particles do not move": vibration vs movement

**Concepts:** states of matter; particle model; vibration
**Specification Points:** 1.1
Temporal scope: CURRENT — AUTHORITATIVE
**The confusion:** everyday "not moving" (no translation) vs the kinetic model, where
vibration IS movement; adjacent descriptions (forces, energy, fixed shape) are
substituted for the arrangement+movement axes.
**Why it occurs [SIB_INFERENCE]:** the question's two axes (arrangement, movement) are pattern-matched to
whichever particle facts the candidate rehearsed.
**Correct distinction:** particles in a solid vibrate about fixed positions — vibration is
a type of movement.
**Typical manifestation:** "the particles do not move" without "around/freely"; forces or
energy prose where arrangement+movement was asked.
**Diagnostic signals [SIB_INFERENCE]:** arrangement-AND-movement prompts; watch for force/energy
substitutions.
**Intervention ideas [PROPOSED_INTERVENTION]:** three-column drill (arrangement / movement / energy) per state.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2019 4CH1/1CR, Question 1 (SRC-ER-4CH1,
2019-06/4CH1-1CR/er.pdf p3): candidates "gave the impression they did not appreciate that
vibration is a type of movement".

### MIS-018 — Which particle moves: electrons vs ions in metallic conduction

**Concepts:** metallic bonding; electrical conductivity; malleability
**Specification Points:** 1.37, 1.38
Temporal scope: CURRENT — AUTHORITATIVE
**The confusion:** in structure→property explanations the mobile species is swapped:
"ions moved" for metallic conduction, or "electrons moved or slid" for malleability.
**Why it occurs [SIB_INFERENCE]:** "charged things move" is over-generalised; the structure→property
chain is memorised per-material rather than reasoned.
**Correct distinction:** metals conduct because delocalised electrons move; layers sliding
(not ions or electrons) explains malleability.
**Typical manifestation:** both marks lost "for stating that the ions moved"; electrons
said to slide.
**Diagnostic signals [SIB_INFERENCE]:** conduction + malleability in one item; cross-check the mobile
species named in each.
**Intervention ideas [PROPOSED_INTERVENTION]:** species-table drill (which particles move where); examiner wording
as model answers.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report November 2024 4CH1/2C, Question 2 (SRC-ER-4CH1,
2024-11/4CH1-2C/er.pdf p3): malleability answers "started saying that electrons moved or
slid"; conduction answers lost marks "for stating that the ions moved".

### MIS-019 — Compound names without oxidation states (rust)

**Concepts:** rusting; oxidation states; nomenclature
**Specification Points:** 2.17, 2.18
Temporal scope: CURRENT — AUTHORITATIVE
**The confusion:** the everyday word "rust" (no oxidation-state content) is treated as a
sufficient chemical name; process words ("oxidation") are offered where a name is asked.
**Why it occurs [SIB_INFERENCE]:** the naming convention is under-rehearsed as an examinable fact; the
(III) state feels optional because everyday speech omits it.
**Correct distinction:** rust is hydrated iron(III) oxide — the name must carry the
oxidation state.
**Typical manifestation:** "iron(II) oxide", "iron hydroxide", "iron oxide" with no state;
"oxidation" as the name; zero scored despite knowing "rust was an oxide of iron".
**Diagnostic signals [SIB_INFERENCE]:** any corrosion item; require the full chemical name.
**Intervention ideas [PROPOSED_INTERVENTION]:** naming-with-oxidation-state drills on common compounds.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2023 4CH1/1C, Q2(a)(i) (SRC-ER-4CH1,
2023-06/4CH1-1C/er.pdf p6): "the oxidation state was frequently missing and so no mark
was scored"; November 2024 4CH1/1C, Q3(a)(ii) (SRC-ER-4CH1, 2024-11/4CH1-1C/er.pdf p3):
"errors of iron(II) oxide, iron hydroxide, and iron oxide with no oxidation state given".

### MIS-020 — Element/atom vs compound vs mixture in classification answers

**Concepts:** classification of matter; elements; compounds; mixtures
**Specification Points:** 1.8, 1.9
Temporal scope: CURRENT — AUTHORITATIVE
**The confusion:** the classification labels themselves: "element" or "atom" written for
compound; "mixture" included in a compound classification.
**Why it occurs [SIB_INFERENCE]:** particle-level and substance-level vocabularies overlap in everyday
use; classification questions demand exactly one label at the substance level.
**Correct distinction:** a compound contains two or more elements chemically combined —
not a mixture; "element"/"atom" is the wrong level for a compound answer.
**Typical manifestation:** classification marks lost with "not quite reaching enough
detail… or incorrectly including the term 'mixture'".
**Diagnostic signals [SIB_INFERENCE]:** classification items; demand the defining sentence, not the label
alone.
**Intervention ideas [PROPOSED_INTERVENTION]:** label-at-level drills: substance-level vs particle-level answers.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2019 4CH1/1CR, Question 4 (SRC-ER-4CH1,
2019-06/4CH1-1CR/er.pdf p4): "Some candidates lost credit by using the term element or
atom for compound"; November 2024 4CH1/1C, Question 2 (SRC-ER-4CH1,
2024-11/4CH1-1C/er.pdf p3): HCl classification answers "incorrectly including the term
'mixture'".

## Evidence / Source Basis

- **Primary evidence:** SRC-ER-4CH1 — official Pearson examiner reports; bounded page
  excerpts with page locators in this run's MIS-02 evidence pack
  (evidence/MIS-02/evidence_pack.json, sha256 of record in the run manifest and
  (census.json, artifacts.MIS-02.pack_sha256)); 13 report files, 17 excerpts extracted.
- **Paper/session identity:** SRC-QPMS-4CH1 (SRC-QPMS-4CH1, identity) — the official
  QP/MS corpus of record; each ER is commentary on its own paper, identities preserved.
- **SUPPLEMENTARY (identity):** SRC-TL-4CH1 (SRC-TL-4CH1, identity);
  SRC-BOOK-4CH1-SB1 (SRC-BOOK-4CH1-SB1, identity) — image-only scan carried as
  identity-only per the wave-1 law.

## Limitations / Coverage Gaps

- **No public ER exists** for 4CH1 sessions 2020-01, 2020-11, 2021-01, 2021-11, 2022-01,
  2023-01 (COVID-era/Jan-Nov publishing) and 2021-06 (cancelled); Nov-2025/June-2026 PEFs
  sit behind Pearson's silver tier. Nothing is extrapolated across the gaps.
- **Extraction disclosure:** the 2024-06 4CH1/1C ER is glyph-garbled on extraction
  (embedded-font failure) and is EXCLUDED from this pack, not cited by any record.
- The pack carries bounded excerpts (first ~1,600 characters per cited page), so records
  reflect the granularity the pack holds; question-level nuance beyond those pages is not
  claimed.
- Examiner sentiment is session-specific commentary, not a controlled study; recurrence
  across series (stated where examiners say so) is the only trend evidence.

## Research Status

status: GENERATED (research artifact; not educational truth). Generated by SIB-GEN run
SIB-CHEMISTRY_4CH1-RUN-003 under the provider-neutral pipeline, grounded exclusively on
the run's MIS-02 evidence pack. Current/legacy separation: fully CURRENT assessment
evidence; no legacy claims. Determinism: content fingerprint recorded in the run
manifest; regeneration produces a new artifact_version.
