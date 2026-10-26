
# MIS-04 — Reasoning Errors

## Purpose

This artifact catalogs the reasoning errors that the official Pearson examiner corpus
records for Pearson Edexcel International GCSE Chemistry (4CH1): failures in the shape of
thinking — mis-applied explanatory frames, incomplete causal chains, reasoning at the
wrong level of the model, and arithmetic performed without the underlying model — as
distinct from single-sided errors (MIS-03) and calculation mechanics (MIS-05). Every
record is grounded on an official Pearson examiner report for a named session and paper,
carried in the run's evidence pack with page identity. It is a research artifact: it does
not promote these observations into canonical educational truth (Subject Intelligence
Build v1, §5).

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

**Covers:** seven reasoning-error records (MIS-029 … MIS-035) grounded on the official
4CH1 examiner reports held by the library (8 held sessions; papers 1C/2C/1CR/2CR),
extracted into the run's evidence pack with bounded page excerpts and page locators.
Each record states the error shape, the session evidence, why the reasoning fails, the
correct reasoning form, and diagnostic signals.

**Does not cover:** vocabulary-level confusions (MIS-02), script-level answer defects
(MIS-07), legacy 4CH0 sentiment, and sessions without a public ER (disclosed gaps, never
filled).

## Executive Summary

- Rehearsed frames mis-apply across boundaries: collision-theory language answering a
  physical-change question is the cleanest corpus example.
- Collision-model explanations fail by omission — missing frequency, missing "same
  volume", missing "successful collisions".
- Answers drift to irrelevant, adjacent knowledge (neutrons/isotopes where proton
  identity was asked).
- Arithmetic can be performed without the model: masses added where weighted means were
  required.

## Main Analysis

### MIS-029 — Rehearsed frame mis-applied to a physical change

**Concepts:** evaporation; kinetic theory; reaction kinetics
**Specification Points:** 1.6
Temporal scope: CURRENT — AUTHORITATIVE
**Error shape:** the most-rehearsed explanatory frame in the course (collision frequency)
is applied outside its domain: "Some confused this process with reactions by talking
about greater frequency of collisions."
**Why the reasoning fails [SIB_INFERENCE]:** frame selection is cued by surface features ("heating")
rather than by whether a reaction is occurring.
**Correct reasoning:** identify the process class first (physical escape of more
energetic particles vs reaction), then select the explanation frame.
**Typical manifestation:** collision-frequency prose in evaporation answers.
**Diagnostic signals [SIB_INFERENCE]:** 'explain what happens when you heat' items across topics; check
the frame, not just the vocabulary.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report November 2023 4CH1/1C, Q1b (SRC-ER-4CH1,
2023-11/4CH1-1C/er.pdf p3).

### MIS-030 — Incomplete collision-model chains

**Concepts:** rates of reaction; collision theory
**Specification Points:** 3.3, 3.5
Temporal scope: CURRENT — AUTHORITATIVE
**Error shape:** the causal chain loses required links at specific joints — "stating an
increase in collisions but without a reference to time/frequency", "stating more
particles with no reference to in the same volume", and answers that "did not refer to
successful collisions which was necessary in this part".
**Why the reasoning fails [SIB_INFERENCE]:** the model is recalled as a slogan ("more collisions") rather
than the full rate law (frequency of successful collisions in a given volume).
**Correct reasoning:** more particles per unit volume → more frequent successful
collisions → rate increases.
**Typical manifestation:** one-mark losses at each missing link across a chain question.
**Diagnostic signals [SIB_INFERENCE]:** rate explanations; audit for frequency + volume + successful
collisions.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2019 4CH1/1CR, Question 5(d) (SRC-ER-4CH1,
2019-06/4CH1-1CR/er.pdf p5).

### MIS-031 — "More energy" offered where concentration/particles was asked

**Concepts:** rates of reaction; particle model
**Specification Points:** 3.3, 3.5
Temporal scope: CURRENT — AUTHORITATIVE
**Error shape:** the energy fact displaces the asked quantity — "Some incorrectly stated
the particles would have more energy" where the change was concentration/surface-driven,
and some "forgot to state that the rate of reaction increases" at all.
**Why the reasoning fails [SIB_INFERENCE]:** energy is the most rehearsed particle fact; it is offered
even when the variable changed is not temperature.
**Correct reasoning:** name the variable actually changed (concentration, surface area,
pressure), then the collision consequence, then the rate outcome.
**Typical manifestation:** energy prose beside concentration items; conclusion omitted.
**Diagnostic signals [SIB_INFERENCE]:** rate items varying the changed variable; check the variable named
in the answer.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2019 4CH1/1CR, Question 5(d) (SRC-ER-4CH1,
2019-06/4CH1-1CR/er.pdf p5).

### MIS-032 — Irrelevant adjacent knowledge displacing the demand

**Concepts:** atomic structure; identity of atoms and ions
**Specification Points:** 1.17, 1.18, 1.19
Temporal scope: CURRENT — AUTHORITATIVE
**Error shape:** candidates answer with true-but-irrelevant facts — "many candidates
mentioned neutrons and isotopes which were irrelevant here. The question just needed to
say there were the same number of protons and electrons or the same electron
configuration"; others "just stated that there was the same number of electrons in the
outer shell which was ignored as this did not answer the question."
**Why the reasoning fails [SIB_INFERENCE]:** the question's target (why two species are the same element)
is not identified; adjacent isotope knowledge substitutes.
**Correct reasoning:** identity = proton number (and, for atoms, electron configuration
balance) — not neutrons, not outer-shell counts alone.
**Typical manifestation:** isotope prose beside an identity question; partial credit
lost.
**Diagnostic signals [SIB_INFERENCE]:** 'why are X and Y the same element' items; check the identity
criterion used.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report November 2024 4CH1/2C, Question 1 (SRC-ER-4CH1,
2024-11/4CH1-2C/er.pdf p3).

### MIS-033 — Diagram-to-inference failures: shells ↔ period

**Concepts:** atomic structure; periodic table; electron shells
**Specification Points:** 1.17, 1.20
Temporal scope: CURRENT — AUTHORITATIVE
**Error shape:** when reading a particle diagram, directly-readable quantities (mass
number, configuration) are handled well but the inference chain (shells → period;
protons → position) fails — "errors were most commonly associated with the identification
of the correct group or period number, with some candidates demonstrating a lack of
understanding that the number of electron shells corresponds to the period."
**Why the reasoning fails [SIB_INFERENCE]:** the shells↔period rule is known as a slogan but not applied
as an inference from the diagram.
**Correct reasoning:** count shells → period; proton number → identity; configuration
pattern → group.
**Typical manifestation:** mass number correct, period wrong, on the same diagram.
**Diagnostic signals [SIB_INFERENCE]:** diagram items asking group/period; isolate the inference step.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2025 4CH1/1C, Question 1(b) (SRC-ER-4CH1,
2025-06/4CH1-1C/er.pdf p5); label-switching on the same diagrams at Question 1(a)
(SRC-ER-4CH1, 2025-06/4CH1-1C/er.pdf p4).

### MIS-034 — Qualitative reasoning missing behind successful procedures

**Concepts:** solubility; energetics; qualitative vs quantitative mastery
**Specification Points:** (AO2/AO3 strand; qualitative items on calculation-typical topics)
Temporal scope: CURRENT — AUTHORITATIVE
**Error shape:** candidates execute the calculation but cannot reason the underlying
chemistry — "Qualitative questions based on topics more typically assessed through
calculations, such as solubility and energetics, proved more challenging. This highlights
the need for candidates to develop a deeper understanding of the chemistry underlying the
calculations they are often able to carry out successfully."
**Why the reasoning fails [SIB_INFERENCE]:** procedures are rehearsed as recipes; the submicroscopic
story behind the numbers is not.
**Correct reasoning:** connect each procedural step to its chemical meaning before
computing.
**Typical manifestation:** strong maths scores beside weak qualitative answers on the
same topic.
**Diagnostic signals [SIB_INFERENCE]:** paired quantitative/qualitative items on one topic; compare the
score delta.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2025 4CH1/2CR, Introduction (SRC-ER-4CH1,
2025-06/4CH1-2CR/er.pdf p3).

### MIS-035 — Arithmetic without the model: masses added where weighted means required

**Concepts:** relative atomic mass; isotope abundance
**Specification Points:** 1.26, 1.31
Temporal scope: CURRENT — AUTHORITATIVE
**Error shape:** the calculation's model step is skipped — "many candidates ignored
multiplying the three protons and four neutrons with the masses and just added the
masses together" (the isotope-table arithmetic performed as plain addition).
**Why the reasoning fails [SIB_INFERENCE]:** the weighted-mean structure (mass × abundance, summed) is
not represented; the numbers invite direct addition.
**Correct reasoning:** each isotope's mass multiplies its fractional abundance before
summing.
**Typical manifestation:** correct-method answers earning one of two marks; standard-form
rescues.
**Diagnostic signals [SIB_INFERENCE]:** isotope-table items; check where abundance entered the working.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report November 2024 4CH1/2C, Question 1 (SRC-ER-4CH1,
2024-11/4CH1-2C/er.pdf p3).

## Evidence / Source Basis

- **Primary evidence:** SRC-ER-4CH1 — official Pearson examiner reports; bounded page
  excerpts with page locators in this run's MIS-04 evidence pack
  (evidence/MIS-04/evidence_pack.json, sha256 of record in the run manifest and
  (census.json, artifacts.MIS-04.pack_sha256)); 10 report files, 14 excerpts extracted.
- **Paper/session identity:** SRC-QPMS-4CH1 (SRC-QPMS-4CH1, identity) — the official
  QP/MS corpus of record; identities preserved.
- **SUPPLEMENTARY (identity):** SRC-TL-4CH1 (SRC-TL-4CH1, identity);
  SRC-BOOK-4CH1-SB1 (SRC-BOOK-4CH1-SB1, identity) — image-only scan, identity-only.

## Limitations / Coverage Gaps

- **No public ER exists** for 4CH1 sessions 2020-01, 2020-11, 2021-01, 2021-11, 2022-01,
  2023-01 and 2021-06; Nov-2025/June-2026 PEFs sit behind Pearson's silver tier. Nothing
  is extrapolated across the gaps.
- **Extraction disclosure:** the 2024-06 4CH1/1C ER is glyph-garbled on extraction and is
  EXCLUDED from this pack, not cited by any record.
- The pack carries bounded excerpts (first ~1,600 characters per cited page); records
  reflect the granularity the pack holds.
- Examiner sentiment is session-specific commentary, not a controlled study.

## Research Status

status: GENERATED (research artifact; not educational truth). Generated by SIB-GEN run
SIB-CHEMISTRY_4CH1-RUN-003 under the provider-neutral pipeline, grounded exclusively on
the run's MIS-04 evidence pack. Current/legacy separation: fully CURRENT assessment
evidence; no legacy claims. Determinism: content fingerprint recorded in the run
manifest; regeneration produces a new artifact_version.
