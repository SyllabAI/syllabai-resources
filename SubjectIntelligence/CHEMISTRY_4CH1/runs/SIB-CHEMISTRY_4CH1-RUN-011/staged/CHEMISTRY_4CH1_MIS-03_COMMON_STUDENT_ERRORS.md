---
sib_protocol: SIB-1.0
artifact_id: MIS-03
artifact_version: 1.1
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
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-011"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "2cb92fe5f56d22f1b231c129a7e0dbc27bf86007"
    syllabai_resources: "a7a34cd97cdff29ee698a86b171c7148bc5e29ed"
---

# MIS-03 — Common Student Errors

## Purpose

This artifact catalogs the common student errors that the official Pearson examiner
corpus records for Pearson Edexcel International GCSE Chemistry (4CH1) at whole-script
grain: the recurring answer failures that cost marks across topics and sessions, as
distinguished from concept confusions (MIS-02) and calculation technique (MIS-05). Every
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

**Covers:** eight common-error records (MIS-021 … MIS-028) grounded on the official 4CH1
examiner reports held by the library (8 held sessions; papers 1C/2C/1CR/2CR), each
extracted into the run's evidence pack with bounded page excerpts and page locators.
Each record states the error, where it appears, why it occurs, what credit-worthy
answering looks like, and the examiner guidance that addresses it.

**Does not cover:** concept-pair confusions (MIS-02), calculation-specific technique
(MIS-05), terminology drills (MIS-06), legacy 4CH0 sentiment, and sessions without a
public ER (disclosed gaps, never filled).

## Executive Summary

- The dominant script-level error is answering beside the question actually set — from
  repeating the stem to filtering steps irrelevant to the demand.
- Vague prose is the most repeated phrasing-level complaint: candidates "lost unnecessary
  marks as they were often too vague".
- Observation and test answers lose marks for half-answers (result without test; colour
  without solid).
- Practical under-preparation remains the corpus's structural weak strand.

## Main Analysis

### MIS-021 — Repeating the stem instead of explaining

**Concepts:** explanation questions; credit-worthy reasoning
**Specification Points:** (assessment-skill strand; AO2 'explain' items)
Temporal scope: CURRENT — AUTHORITATIVE
**Error:** candidates answer an 'explain' question by restating given information —
"just stated that the elements were in the same group, which was just a repeat of the
stem of the question and is, therefore, not creditworthy".
**Why it occurs [SIB_INFERENCE]:** the stem's wording feels like content; the extra reasoning step the
command word demands is not performed.
**Credit-worthy form:** the explanation must add the causal link the stem does not carry.
**Typical manifestation:** stem-paraphrase answers scoring zero on explanation marks.
**Diagnostic signals [SIB_INFERENCE]:** 'explain' items; compare the answer against the stem for novelty.
**Examiner guidance [OBSERVED_IN_SOURCE]:** the report contrasts the failing pattern with answers that give "a
clear explanation as to why R has 33 protons".
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2019 4CH1/1C, Question 2(b)-(c) (SRC-ER-4CH1,
2019-06/4CH1-1C/er.pdf p4).

### MIS-022 — Wrong layer of the model in 'why' answers

**Concepts:** atomic structure; subatomic particles
**Specification Points:** 1.17, 1.18
Temporal scope: CURRENT — AUTHORITATIVE
**Error:** candidates answer a proton-level question with electron/shell talk — "Some
lost marks by talking about electrons and electron shells rather than protons."
**Why it occurs [SIB_INFERENCE]:** electron-configuration facts are more rehearsed than the identity law
(proton number defines the element), so the dominant fact displaces the asked one.
**Credit-worthy form:** the answer must operate at the particle layer the question names.
**Typical manifestation:** correct-but-irrelevant electronic structure prose beside a
proton question.
**Diagnostic signals [SIB_INFERENCE]:** atomic-identity items; check the particle named in the answer.
**Examiner guidance [OBSERVED_IN_SOURCE]:** examiners reward answers that name the layer explicitly ("This is
an 'explain' question so an explanation needs to be given").
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2019 4CH1/1C, Question 2(c) (SRC-ER-4CH1,
2019-06/4CH1-1C/er.pdf p4).

### MIS-023 — Half-answers on observations and tests

**Concepts:** practical observations; chemical tests
**Specification Points:** 1.7C, 2.44C (Core Practical strand)
Temporal scope: CURRENT — AUTHORITATIVE
**Error:** observation answers give one axis where two were demanded — "many lost the
mark as they referred to the colour, but not solid or vice versa. Both colour and solid
or powder or ash was needed"; precipitate claims offered where none is physically
possible — "A few candidates lost the mark for stating that there was a white
precipitate. A precipitate would only occur if it formed a precipitate at the bottom of
a solution, not in the basin."
**Why it occurs [SIB_INFERENCE]:** observation vocabulary is recalled as single tokens; the mark scheme
pays for complete descriptions (test AND result, colour AND solid).
**Credit-worthy form:** both axes of the observation, in the physical context asked.
**Typical manifestation:** one-mark scripts on two-mark observation items.
**Diagnostic signals [SIB_INFERENCE]:** observation/test items; require both axes before accepting.
**Examiner guidance [OBSERVED_IN_SOURCE]:** examiners model the complete two-axis form.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report November 2023 4CH1/2C, Question 2 (SRC-ER-4CH1,
2023-11/4CH1-2C/er.pdf p3).

### MIS-024 — Imprecise naming of test products and ions

**Concepts:** flame tests; halide tests; ionic formulae
**Specification Points:** 1.7C, 2.44C
Temporal scope: CURRENT — AUTHORITATIVE
**Error:** candidates name the test's chemistry at the wrong grain — "just wrote
'lithium' or 'Li' rather than giving the formula of the ion"; "rather than writing
'silver bromide' many just wrote 'bromide', 'bromine' or sometimes 'bromine nitrate'".
**Why it occurs [SIB_INFERENCE]:** the everyday name and the species name coincide in speech; the mark
pays for the species.
**Credit-worthy form:** ion formulae in flame-test answers; the precipitate's compound
name in halide tests.
**Typical manifestation:** known chemistry scoring zero on naming marks.
**Diagnostic signals [SIB_INFERENCE]:** qualitative analysis items; check the species named.
**Examiner guidance [OBSERVED_IN_SOURCE]:** candidates "need to mention impurities etc. which may be on the
wire" for the cleaning mark.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2019 4CH1/1C, Question 3(a)-(d)(i)
(SRC-ER-4CH1, 2019-06/4CH1-1C/er.pdf p6).

### MIS-025 — Method answers that answer a different question

**Concepts:** practical method writing; salt preparation
**Specification Points:** 1.7C, 2.44C
Temporal scope: CURRENT — AUTHORITATIVE
**Error:** well-rehearsed method fragments are pasted where they add nothing — "They
have been asked to produce crystals of salt from salt solution. The comments about
filtering at the start were therefore ignored as filtering would add nothing to the
method."
**Why it occurs [SIB_INFERENCE]:** crystallisation methods are memorised as full pipelines; the question
starts mid-pipeline.
**Credit-worthy form:** "Read the question twice. Highlight what is important before
answering" (examiners' own instruction).
**Typical manifestation:** irrelevant first steps; marks dropped without wrong chemistry.
**Diagnostic signals [SIB_INFERENCE]:** method items with a given starting point; check each step against
the demand.
**Examiner guidance [OBSERVED_IN_SOURCE]:** examiners explicitly ignored the irrelevant step — the error is
demand-mapping, not chemistry.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2022 4CH1/1C, Question 2(b)(iii)
(SRC-ER-4CH1, 2022-06/4CH1-1C/er.pdf p5).

### MIS-026 — Ranges given where the specification quotes a value

**Concepts:** reaction conditions; cracking
**Specification Points:** 3.1, 3.2
Temporal scope: CURRENT — AUTHORITATIVE
**Error:** answers widen a quoted condition into a losing range — "Avoid giving a range
for answers. The specification quotes 600-700ºC so the range given here doesn't score
marks as 750ºC is too high."
**Why it occurs [SIB_INFERENCE]:** candidates hedge with ranges; the mark scheme pays for the
specification value.
**Credit-worthy form:** the specification's own value range, not an extended one.
**Typical manifestation:** 750ºC offered where 600-700ºC was quoted.
**Diagnostic signals [SIB_INFERENCE]:** condition items; compare against the spec's quoted window.
**Examiner guidance [OBSERVED_IN_SOURCE]:** the report names the repair directly ("Avoid giving a range").
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2022 4CH1/1C, Question 3(b)(i) (SRC-ER-4CH1,
2022-06/4CH1-1C/er.pdf p7).

### MIS-027 — Practical under-preparation as a structural error source

**Concepts:** practical techniques; unfamiliar contexts
**Specification Points:** 1.7C, 1.13, 2.44C (Core Practical strand)
Temporal scope: CURRENT — AUTHORITATIVE
**Error (cluster):** thin laboratory experience defeats candidates in practical-context
items even when the underlying chemistry is known — "many candidates had done very
little practical work as questions involving practical work and demonstrations tended to
score lower marks than more theoretical questions"; and "Candidates need plenty of
experience in doing chemistry experiments in order to help them answer questions which
are related to the practical aspects of chemistry."
**Why it occurs [SIB_INFERENCE]:** exam questions assess practical skills on paper; candidates without
hands-on work cannot import the sensory and procedural detail the answers need.
**Credit-worthy form:** specific detail and direction-of-error reasoning in practical
answers.
**Typical manifestation:** strong theory beside weak practical-context scores.
**Diagnostic signals [SIB_INFERENCE]:** practical-context items answered below the candidate's theory
average.
**Examiner guidance [OBSERVED_IN_SOURCE]:** examiners tie the deficit to intervention ("plenty of experience
in doing chemistry experiments").
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner reports June 2023 4CH1/1CR, Introduction (SRC-ER-4CH1,
2023-06/4CH1-1CR/er.pdf p3); June 2024 4CH1/1CR, Introduction (SRC-ER-4CH1,
2024-06/4CH1-1CR/er.pdf p3); June 2019 4CH1/1C, Introduction (SRC-ER-4CH1,
2019-06/4CH1-1C/er.pdf p3).

### MIS-028 — Unlinked statements in extended explanations

**Concepts:** extended writing; explanation quality
**Specification Points:** (assessment-skill strand; AO1/AO2 long-answer items)
Temporal scope: CURRENT — AUTHORITATIVE
**Error:** correct chemistry fragments appear without the linking the marks demand —
"All of these were explanations. Many of the candidates struggled with these questions
and only the very best scored full marks. They needed to link the statements to gain all
the marks which many candidates found difficult."
**Why it occurs [SIB_INFERENCE]:** long answers are drafted as fact dumps; linking is not rehearsed as a
skill.
**Credit-worthy form:** each mark is a linked step: identify → because → so → therefore.
**Typical manifestation:** all facts present, few marks awarded; vagueness alongside —
"lost unnecessary marks as they were often too vague when writing their answers".
**Diagnostic signals [SIB_INFERENCE]:** 4+ mark explanations; compare script content against the mark
scheme's chain steps.
**Examiner guidance [OBSERVED_IN_SOURCE]:** the linking requirement itself is the examiners' named criterion.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2024 4CH1/1CR, Introduction (SRC-ER-4CH1,
2024-06/4CH1-1CR/er.pdf p3); June 2022 4CH1/2C, Introduction (SRC-ER-4CH1,
2022-06/4CH1-2C/er.pdf p3).

## Evidence / Source Basis

- **Primary evidence:** SRC-ER-4CH1 — official Pearson examiner reports; bounded page
  excerpts with page locators in this run's MIS-03 evidence pack
  (evidence/MIS-03/evidence_pack.json, sha256 of record in the run manifest and
  (census.json, artifacts.MIS-03.pack_sha256)); 14 report files, 22 excerpts extracted.
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
- Examiner sentiment is session-specific commentary, not a controlled study; recurrence
  across series (stated where examiners say so) is the only trend evidence.

## Research Status

status: GENERATED (research artifact; not educational truth). Generated by SIB-GEN run
SIB-CHEMISTRY_4CH1-RUN-003 under the provider-neutral pipeline, grounded exclusively on
the run's MIS-03 evidence pack. Current/legacy separation: fully CURRENT assessment
evidence; no legacy claims. Determinism: content fingerprint recorded in the run
manifest; regeneration produces a new artifact_version.
