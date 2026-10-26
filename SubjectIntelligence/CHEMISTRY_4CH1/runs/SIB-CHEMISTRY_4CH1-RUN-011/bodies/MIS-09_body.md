
# MIS-09 — Misconception Interventions

## Purpose

This artifact derives the intervention playbook implied by the official Pearson examiner
corpus for Pearson Edexcel International GCSE Chemistry (4CH1): the remediation moves the
examiners themselves prescribe, plus drills this artifact designs from the named error
patterns — each intervention anchored to the examiner evidence that motivates it. Every
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

**Covers:** seven intervention records (MIS-064 … MIS-070) grounded on the official 4CH1
examiner reports held by the library (8 held sessions; papers 1C/2C/1CR/2CR), extracted
into the run's evidence pack with bounded page excerpts and page locators. Each record
names the intervention, the examiner evidence that motivates it, the target error class,
the drill design, and the observable success signal.

**Does not cover:** diagnostic probes (MIS-08), the misconception statements themselves
(MIS-01), mark-scheme internals (MS family), legacy 4CH0 sentiment, and sessions without
a public ER (disclosed gaps, never filled).

## Executive Summary

- The examiners' own interventions are explicit: practical experience ("candidates need
  plenty of experience in doing chemistry experiments"), drafting-and-ticking on extended
  answers, and the significant-figures rule.
- Recurring error classes (halogen/halide terminology "an on-going issue"; ratio-once;
  rounding) each support a specific drill.
- Observation completeness and obvious-mistake identification are drillable practical
  skills with examiner-stated criteria.

## Main Analysis

### MIS-064 — Practical-experience drive

**Concepts:** practical techniques; AO3
**Specification Points:** 1.7C, 1.13, 2.44C (Core Practical strand)
Temporal scope: CURRENT — AUTHORITATIVE
**Intervention [PROPOSED_INTERVENTION]:** schedule the 12 Core Practicals plus unfamiliar-context variants, with
observation and error-direction debriefs — the examiners' own prescription.
**Motivating evidence [OBSERVED_IN_SOURCE]:** "Candidates need plenty of experience in doing chemistry
experiments in order to help them answer questions which are related to the practical
aspects of chemistry"; "many candidates had done very little practical work"; "did not
do enough practical work which disadvantaged their success".
**Target error class:** practical under-preparation (MIS-027-class).
**Drill design [PROPOSED_INTERVENTION]:** map every Core Practical to two unfamiliar-context variants; require
qualitative detail and direction-of-error statements in debriefs.
**Success signal [PROPOSED_INTERVENTION]:** practical-context scores close the gap to theory scores.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2019 4CH1/1C, Introduction (SRC-ER-4CH1,
2019-06/4CH1-1C/er.pdf p3); June 2023 4CH1/1CR, Introduction (SRC-ER-4CH1,
2023-06/4CH1-1CR/er.pdf p3); June 2024 4CH1/1CR, Introduction (SRC-ER-4CH1,
2024-06/4CH1-1CR/er.pdf p3).

### MIS-065 — Draft-then-tick discipline on extended answers

**Concepts:** extended writing; demand mapping
**Specification Points:** (assessment-skill strand; AO1/AO2 long-answer items)
Temporal scope: CURRENT — AUTHORITATIVE
**Intervention [PROPOSED_INTERVENTION]:** train the examiners' named technique verbatim — draft ideas first, then
tick parts of the question as they appear in the answer.
**Motivating evidence [OBSERVED_IN_SOURCE]:** "many candidates did not answer the question given and should be
encouraged to draft their ideas first or tick parts of the question off when they appear
in the answer."
**Target error class:** answering beside the question (MIS-050-class).
**Drill design [PROPOSED_INTERVENTION]:** on 4-6 mark items, students decompose the stem into mark points before
writing, then self-tick; teachers audit the ticks.
**Success signal [PROPOSED_INTERVENTION]:** unaddressed-part count falls to zero on timed scripts.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2022 4CH1/1C, Introduction (SRC-ER-4CH1,
2022-06/4CH1-1C/er.pdf p3).

### MIS-066 — Round-once-at-the-end rule

**Concepts:** significant figures; calculator discipline
**Specification Points:** 1.26, 1.31
Temporal scope: CURRENT — AUTHORITATIVE
**Intervention [PROPOSED_INTERVENTION]:** institutionalize the examiners' rule as a written calculation
convention: full precision until the final line; round once, as requested.
**Motivating evidence [OBSERVED_IN_SOURCE]:** "The majority gave their answer correctly to one decimal place
as requested though some rounding errors to 10.7 were seen"; and moles answers "quoting
the answer to only one significant figure, which from the given data was not
reasonable".
**Target error class:** premature rounding/truncation (MIS-036-class).
**Drill design [PROPOSED_INTERVENTION]:** mark mock calculations in two colours — chemistry vs precision; require
precision repairs before content repairs.
**Success signal [PROPOSED_INTERVENTION]:** zero precision losses on the next mock's calculation chain.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report November 2023 4CH1/1C, Q2c(ii) (SRC-ER-4CH1,
2023-11/4CH1-1C/er.pdf p3); June 2019 4CH1/1CR, Question 10 (SRC-ER-4CH1,
2019-06/4CH1-1CR/er.pdf p7).

### MIS-067 — Ratio-once mole discipline

**Concepts:** mole calculations; stoichiometry
**Specification Points:** 1.31, 1.42
Temporal scope: CURRENT — AUTHORITATIVE
**Intervention [PROPOSED_INTERVENTION]:** teach the mole map with the ratio applied at exactly one labelled step;
ban double-ratio working explicitly.
**Motivating evidence [OBSERVED_IN_SOURCE]:** "Candidates just need to take care, in moles calculations, to
consider the ratio only once. Some candidates incorporate the ratio in the calculation
of Mr – which is an acceptable method – but then consider it again later in the
calculation"; and the neglected-ratio complaint "Ratios in equations were a problem for
some candidates and this was often missed."
**Target error class:** ratio neglected or double-counted (MIS-038/039-class).
**Drill design [PROPOSED_INTERVENTION]:** mole-map worksheets where students must circle the single step where
the ratio multiplies; peer-check the circled step.
**Success signal [PROPOSED_INTERVENTION]:** full marks on ratio-bearing chains in the next assessment.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2023 4CH1/2CR, Introduction (SRC-ER-4CH1,
2023-06/4CH1-2CR/er.pdf p3); June 2022 4CH1/1C, Introduction (SRC-ER-4CH1,
2022-06/4CH1-1C/er.pdf p3).

### MIS-068 — Terminology mastery drills (halogens/halides and bonding vocabulary)

**Concepts:** Group 7 nomenclature; bonding vocabulary
**Specification Points:** 2.20, 2.21, 1.37, 1.38
Temporal scope: CURRENT — AUTHORITATIVE
**Intervention [PROPOSED_INTERVENTION]:** run the examiners' advice as a standing drill: species-type labelling
(element vs ion) before any displacement answer; bonding-vocabulary sentence frames using
examiner wording.
**Motivating evidence [OBSERVED_IN_SOURCE]:** the halogen/halide confusion "affected two questions… This is
an on-going issue, so would be one for candidates to try and master"; and long-response
candidates "lacked a firm grasp of key terminology".
**Target error class:** -ine/-ide and metallic/ionic vocabulary (MIS-043/046-class).
**Drill design [PROPOSED_INTERVENTION]:** -ine/-ide suffix table; species-label-then-write routine; examiner-worded
model sentences for conduction and malleability.
**Success signal [PROPOSED_INTERVENTION]:** zero suffix-class errors on the next displacement item.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2023 4CH1/2CR, Introduction (SRC-ER-4CH1,
2023-06/4CH1-2CR/er.pdf p3); June 2025 4CH1/1C, Introduction (SRC-ER-4CH1,
2025-06/4CH1-1C/er.pdf p3).

### MIS-069 — Obvious-mistake identification practice (practical evaluation)

**Concepts:** practical evaluation; error explanation
**Specification Points:** 1.7C, 2.44C
Temporal scope: CURRENT — AUTHORITATIVE
**Intervention [PROPOSED_INTERVENTION]:** train the two-step evaluation move examiners reward: identify the most
obvious mistake, then explain clearly WHY it is a mistake (mechanism, not assertion).
**Motivating evidence [OBSERVED_IN_SOURCE]:** "When identifying mistakes in a practical situation candidates
should look for the most obvious ones and explain clearly why they are mistakes"; the
exemplar requires "some indication that the inks will mix with the water (therefore,
preventing them from moving through the paper)" — the explanation, not the
identification, carried the second mark.
**Target error class:** insufficient evaluation explanations (MIS-027-adjacent).
**Drill design [PROPOSED_INTERVENTION]:** flawed-method cards; students list obvious mistakes + mechanism
sentences; swap and mark against the two-point rule.
**Success signal [PROPOSED_INTERVENTION]:** mechanism sentences present in every evaluation answer.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2019 4CH1/1C, Question 4 (SRC-ER-4CH1,
2019-06/4CH1-1C/er.pdf p8).

### MIS-070 — Observation-completeness drills (tests AND results)

**Concepts:** chemical tests; qualitative observations
**Specification Points:** 1.7C, 2.44C
Temporal scope: CURRENT — AUTHORITATIVE
**Intervention [PROPOSED_INTERVENTION]:** drill complete observation statements: test AND result; colour AND
solid; species names at the markable grain — the exact axes examiners pay for.
**Motivating evidence [OBSERVED_IN_SOURCE]:** "colour changes and observations were not always well known";
naming failures "rather than writing 'silver bromide' many just wrote 'bromide',
'bromine' or sometimes 'bromine nitrate'"; and "It was apparent that many centres had not
observed sulfur burning."
**Target error class:** half-answers on observations (MIS-023/024-class).
**Drill design [PROPOSED_INTERVENTION]:** test-and-result flash cards for all named tests; observation sentence
templates with both axes; live demonstrations where a centre's experience is thin.
**Success signal [PROPOSED_INTERVENTION]:** two-axis observation statements on every qualitative item.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2022 4CH1/2C, Introduction (SRC-ER-4CH1,
2022-06/4CH1-2C/er.pdf p3); June 2019 4CH1/1C, Question 3 (SRC-ER-4CH1,
2019-06/4CH1-1C/er.pdf p6); June 2023 4CH1/1CR, Question 1(b)(i) (SRC-ER-4CH1,
2023-06/4CH1-1CR/er.pdf p4).

## Evidence / Source Basis

- **Primary evidence:** SRC-ER-4CH1 — official Pearson examiner reports; bounded page
  excerpts with page locators in this run's MIS-09 evidence pack
  (evidence/MIS-09/evidence_pack.json, sha256 of record in the run manifest and
  (census.json, artifacts.MIS-09.pack_sha256)); 11 report files, 16 excerpts extracted.
- **Paper/session identity:** SRC-QPMS-4CH1 (SRC-QPMS-4CH1, identity) — the official
  QP/MS corpus of record; identities preserved.
- **SUPPLEMENTARY (identity):** SRC-TL-4CH1 (SRC-TL-4CH1, identity);
  SRC-BOOK-4CH1-SB1 (SRC-BOOK-4CH1-SB1, identity) — image-only scan, identity-only.
- **Contribution boundary:** drill designs are this artifact's research reading of the
  examiner evidence; the evidence lines are quoted only from the pack.

## Limitations / Coverage Gaps

- **No public ER exists** for 4CH1 sessions 2020-01, 2020-11, 2021-01, 2021-11, 2022-01,
  2023-01 and 2021-06; Nov-2025/June-2026 PEFs sit behind Pearson's silver tier. Nothing
  is extrapolated across the gaps.
- **Extraction disclosure:** the 2024-06 4CH1/1C ER is glyph-garbled on extraction and is
  EXCLUDED from this pack, not cited by any record.
- The drills are classroom interventions derived from examiner commentary, not validated
  efficacy-tested programs; no outcome claim is made.
- Examiner sentiment is session-specific commentary, not a controlled study.

## Research Status

status: GENERATED (research artifact; not educational truth). Generated by SIB-GEN run
SIB-CHEMISTRY_4CH1-RUN-003 under the provider-neutral pipeline, grounded exclusively on
the run's MIS-09 evidence pack. Current/legacy separation: fully CURRENT assessment
evidence; no legacy claims. Determinism: content fingerprint recorded in the run
manifest; regeneration produces a new artifact_version.
