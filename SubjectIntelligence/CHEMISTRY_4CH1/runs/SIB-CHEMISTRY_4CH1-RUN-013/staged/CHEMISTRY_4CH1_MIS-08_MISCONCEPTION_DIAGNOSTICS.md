---
sib_protocol: SIB-1.0
artifact_id: MIS-08
artifact_version: 1.2
subject: Chemistry
qualification: International GCSE
specification: 4CH1
curriculum_version: "2017"

research_family: misconception_intelligence
applicability: REQUIRED

temporal_scope:
  current: true
  legacy: false

source_scope:
  specification: false
  textbook: false
  question_papers: true
  mark_schemes: false
  examiner_reports: true
  supplementary: true

status: GENERATED
generated_by: zai_agent
generated_at: 2026-10-27

provenance:
  source_manifest: "SRC-ER-4CH1"
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-013"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "2cb92fe5f56d22f1b231c129a7e0dbc27bf86007"
    syllabai_resources: "74d76bbab72378ac8db02068943b195b5099b3ca"
---

# MIS-08 — Misconception Diagnostics

## Purpose

This artifact derives the diagnostic instruments implied by the official Pearson examiner
corpus for Pearson Edexcel International GCSE Chemistry (4CH1): probe designs and
script-audit procedures a teacher can run to detect the misconception classes the
examiners name — before the high-stakes exam surfaces them. Every record is grounded on
an official Pearson examiner report for a named session and paper, carried in the run's
evidence pack with page identity; the diagnostic reading is the artifact's own
contribution, clearly separated from the examiner evidence that motivates it. It is a
research artifact: it does not promote these observations into canonical educational
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

**Covers:** seven diagnostic records (MIS-057 … MIS-063) grounded on the official 4CH1
examiner reports held by the library (8 held sessions; papers 1C/2C/1CR/2CR), extracted
into the run's evidence pack with bounded page excerpts and page locators. Each record
names the probe, the examiner evidence that motivates it, the signal it tests for, the
fail pattern, and the pass pattern.

**Does not cover:** intervention design beyond detection (MIS-09), the underlying
misconception statements (MIS-01), legacy 4CH0 sentiment, and sessions without a public
ER (disclosed gaps, never filled).

## Executive Summary

- Every diagnostic here is a two-sided probe: the examiner corpus names both the fail
  pattern and the credit-worthy form, which makes the probe designable.
- The highest-yield probes are the two-axis particle probe, the frame-separation probe,
  and the mobile-species probe — each targets a confusion the examiners named in
  multiple sessions.
- Script audits (rounding inspection, practical-vs-theory deltas, question-mapping) turn
  examiner complaints into checkable classroom routines.

## Main Analysis

### MIS-057 — Two-axis particle probe (arrangement AND movement)

**Concepts:** states of matter; particle model
**Specification Points:** 1.1
Temporal scope: CURRENT — AUTHORITATIVE
**Probe [PROPOSED_INTERVENTION]:** ask for arrangement AND movement of particles in each state, in one item, with
both axes marked separately.
**Motivating evidence [OBSERVED_IN_SOURCE]:** examiners report answers that "did not address the question, but
instead described the forces between particles in a solid or referred to the amount of
energy the particles may have", and "the particles do not move, without adding the key
word around or freely".
**Signal tested [SIB_INFERENCE]:** whether vibration is understood as movement, and whether the student
answers both axes on demand.
**Fail pattern [SIB_INFERENCE]:** force/energy substitutions; 'do not move' statements; one-axis answers.
**Pass pattern [SIB_INFERENCE]:** vibration about fixed positions PLUS movement named, both axes
present.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2019 4CH1/1CR, Question 1 (SRC-ER-4CH1,
2019-06/4CH1-1CR/er.pdf p3).

### MIS-058 — Frame-separation probe (physical vs reaction explanation)

**Concepts:** evaporation; kinetic theory; reaction kinetics
**Specification Points:** 1.2
Temporal scope: CURRENT — AUTHORITATIVE
**Probe [PROPOSED_INTERVENTION]:** present a heating scenario and require the evaporation explanation; then a
separate reaction scenario requiring the collision-frequency explanation; score frame
selection.
**Motivating evidence [OBSERVED_IN_SOURCE]:** "Some confused this process with reactions by talking about
greater frequency of collisions" where "evaporation involves the more energetic
particles escaping the liquid" was required.
**Signal tested [SIB_INFERENCE]:** whether the student selects the explanatory frame by process class,
not by surface cue.
**Fail pattern [SIB_INFERENCE]:** collision-frequency prose on the physical scenario.
**Pass pattern [SIB_INFERENCE]:** more energetic particles escaping the liquid for evaporation;
frequency of successful collisions reserved for rates.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report November 2023 4CH1/1C, Q1b (SRC-ER-4CH1,
2023-11/4CH1-1C/er.pdf p3).

### MIS-059 — Mobile-species probe (which particle moves where)

**Concepts:** metallic bonding; ionic conduction; malleability
**Specification Points:** 1.37, 1.38
Temporal scope: CURRENT — AUTHORITATIVE
**Probe [PROPOSED_INTERVENTION]:** a two-part item: explain conduction of a metal AND of a molten ionic solid;
then malleability. Require the moving species named in each.
**Motivating evidence [OBSERVED_IN_SOURCE]:** marks lost "for stating that the ions moved" (metal) and
answers that "started saying that electrons moved or slid" (malleability).
**Signal tested [SIB_INFERENCE]:** structure→property reasoning with the correct mobile species.
**Fail pattern [SIB_INFERENCE]:** ions moving in metals; electrons sliding in layers.
**Pass pattern [SIB_INFERENCE]:** delocalised electrons move in metals; ions move in molten/aqueous
ionic compounds; layers slide for malleability.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report November 2024 4CH1/2C, Question 2 (SRC-ER-4CH1,
2024-11/4CH1-2C/er.pdf p3).

### MIS-060 — Precision audit on calculation scripts

**Concepts:** significant figures; calculator discipline
**Specification Points:** 1.26, 1.31
Temporal scope: CURRENT — AUTHORITATIVE
**Probe [PROPOSED_INTERVENTION]:** collect multi-step calculation scripts; inspect intermediate values for
rounded/truncated entries and final answers for over-rounding; report per-student rates.
**Motivating evidence [OBSERVED_IN_SOURCE]:** "rounding errors to 10.7 were seen" where one decimal place was
requested; and the RAM answer rounded "to the value of the most abundant isotope", which
examiners note "defeats the purpose of doing the calculation".
**Signal tested [SIB_INFERENCE]:** whether intermediates preserve precision and rounding happens once.
**Fail pattern [SIB_INFERENCE]:** premature rounding of intermediates; answers rounded to the dominant
isotope.
**Pass pattern [SIB_INFERENCE]:** full-precision working; one rounding step at the end.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report November 2023 4CH1/1C, Q2c(ii) (SRC-ER-4CH1,
2023-11/4CH1-1C/er.pdf p3); June 2019 4CH1/2CR, Question 2(b) (SRC-ER-4CH1,
2019-06/4CH1-2CR/er.pdf p3).

### MIS-061 — Diagram-inference probe (shells ↔ period, labels)

**Concepts:** atomic structure; periodic table
**Specification Points:** 1.17, 1.19, 1.20
Temporal scope: CURRENT — AUTHORITATIVE
**Probe [PROPOSED_INTERVENTION]:** show a particle diagram; ask for mass number, configuration, group and period
in one grid; mark the inference cells separately from the read-off cells.
**Motivating evidence [OBSERVED_IN_SOURCE]:** "errors were most commonly associated with the identification of
the correct group or period number, with some candidates demonstrating a lack of
understanding that the number of electron shells corresponds to the period"; label
switching on the same diagrams.
**Signal tested [SIB_INFERENCE]:** shells→period inference vs direct read-off.
**Fail pattern [SIB_INFERENCE]:** mass number correct, period wrong; proton/neutron labels swapped.
**Pass pattern [SIB_INFERENCE]:** inference cells correct without scaffolding.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2025 4CH1/1C, Questions 1(a) and 1(b)
(SRC-ER-4CH1, 2025-06/4CH1-1C/er.pdf p4 and p5).

### MIS-062 — Practical-vs-theory delta audit

**Concepts:** practical techniques; AO3
**Specification Points:** 1.7C, 1.13, 2.44C (Core Practical strand)
Temporal scope: CURRENT — AUTHORITATIVE
**Probe [PROPOSED_INTERVENTION]:** per student, compare average scores on practical-context items vs theoretical
items across two mocks; flag deltas beyond a set threshold.
**Motivating evidence [OBSERVED_IN_SOURCE]:** "questions involving practical work and demonstrations tended to
score lower marks than more theoretical questions"; "Candidates did not score very well
when they were involved with practical questions which implied that many candidates did
not do enough practical work".
**Signal tested [SIB_INFERENCE]:** whether thin practical experience is the student's binding constraint.
**Fail pattern [SIB_INFERENCE]:** large positive delta (theory >> practical) at student level.
**Pass pattern [SIB_INFERENCE]:** deltas within noise.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner reports June 2023 4CH1/1CR, Introduction (SRC-ER-4CH1,
2023-06/4CH1-1CR/er.pdf p3); June 2024 4CH1/1CR, Introduction (SRC-ER-4CH1,
2024-06/4CH1-1CR/er.pdf p3).

### MIS-063 — Question-mapping audit on extended answers

**Concepts:** extended writing; demand mapping
**Specification Points:** (assessment-skill strand; AO1/AO2 long-answer items)
Temporal scope: CURRENT — AUTHORITATIVE
**Probe [PROPOSED_INTERVENTION]:** on extended-response scripts, underline each question part in the stem, then
tick where the script addresses it; count unaddressed parts and stem-paraphrase lines.
**Motivating evidence [OBSERVED_IN_SOURCE]:** "many candidates did not answer the question given and should
be encouraged to draft their ideas first or tick parts of the question off"; "candidates
should read all the questions carefully, as they often contain information such as
formulae, and other advice to help them in their answers."
**Signal tested [SIB_INFERENCE]:** whether the answer walks the question's parts.
**Fail pattern [SIB_INFERENCE]:** unaddressed parts; repeated stem wording as 'explanation'.
**Pass pattern [SIB_INFERENCE]:** every part ticked off with linked, non-stem content.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2022 4CH1/1C, Introduction (SRC-ER-4CH1,
2022-06/4CH1-1C/er.pdf p3); June 2022 4CH1/2CR, Introduction (SRC-ER-4CH1,
2022-06/4CH1-2CR/er.pdf p3).

## Evidence / Source Basis

- **Primary evidence:** SRC-ER-4CH1 — official Pearson examiner reports; bounded page
  excerpts with page locators in this run's MIS-08 evidence pack
  (evidence/MIS-08/evidence_pack.json, sha256 of record in the run manifest and
  (census.json, artifacts.MIS-08.pack_sha256)); 10 report files, 13 excerpts extracted.
- **Paper/session identity:** SRC-QPMS-4CH1 (SRC-QPMS-4CH1, identity) — the official
  QP/MS corpus of record; identities preserved.
- **SUPPLEMENTARY (identity):** SRC-TL-4CH1 (SRC-TL-4CH1, identity);
  SRC-BOOK-4CH1-SB1 (SRC-BOOK-4CH1-SB1, identity) — image-only scan, identity-only.
- **Contribution boundary:** the probe designs are this artifact's research reading of
  the examiner evidence; the evidence lines are quoted only from the pack.

## Limitations / Coverage Gaps

- **No public ER exists** for 4CH1 sessions 2020-01, 2020-11, 2021-01, 2021-11, 2022-01,
  2023-01 and 2021-06; Nov-2025/June-2026 PEFs sit behind Pearson's silver tier. Nothing
  is extrapolated across the gaps.
- **Extraction disclosure:** the 2024-06 4CH1/1C ER is glyph-garbled on extraction and is
  EXCLUDED from this pack, not cited by any record.
- The probes are classroom diagnostics derived from examiner commentary, not validated
  psychometric instruments; no efficacy claim is made.
- Examiner sentiment is session-specific commentary, not a controlled study.

## Research Status

status: GENERATED (research artifact; not educational truth). Generated by SIB-GEN run
SIB-CHEMISTRY_4CH1-RUN-003 under the provider-neutral pipeline, grounded exclusively on
the run's MIS-08 evidence pack. Current/legacy separation: fully CURRENT assessment
evidence; no legacy claims. Determinism: content fingerprint recorded in the run
manifest; regeneration produces a new artifact_version.
