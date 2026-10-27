---
sib_protocol: SIB-1.0
artifact_id: MIS-05
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

# lifecycle: GENERATED -> QA_PASSED -> STAGED
status: PUBLISHED
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

# MIS-05 — Calculation Errors

## Purpose

This artifact catalogs the calculation errors that the official Pearson examiner corpus
records for Pearson Edexcel International GCSE Chemistry (4CH1): the systematic
arithmetic and technique failures in mole, RAM, titration and precision work — rounding,
stoichiometric-ratio handling, unit conversions, and answer discipline — as examiners
name them. Every record is grounded on an official Pearson examiner report for a named
session and paper, carried in the run's evidence pack with page identity. It is a
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

**Covers:** seven calculation-error records (MIS-036 … MIS-042) grounded on the official
4CH1 examiner reports held by the library (8 held sessions; papers 1C/2C/1CR/2CR),
extracted into the run's evidence pack with bounded page excerpts and page locators.
Each record states the error, why it occurs, the correct technique, the typical
manifestation, and the examiner guidance that addresses it.

**Does not cover:** mark-scheme internals (MS family), reasoning-level failures behind
the arithmetic (MIS-04), legacy 4CH0 sentiment, and sessions without a public ER
(disclosed gaps, never filled).

## Executive Summary

- Premature rounding/truncation is the corpus's most repeated calculation complaint,
  named in four separate series.
- The stoichiometric ratio fails in both directions: neglected entirely, or applied
  twice.
- Unit discipline (volume conversion cm3 → dm3) and final-answer precision (significant
  figures) are named mark-loss points.
- The RAM calculation's purpose is defeated by rounding to the dominant isotope.

## Main Analysis

### MIS-036 — Premature rounding and truncation

**Concepts:** significant figures; calculator discipline
**Specification Points:** 1.26, 1.31
Temporal scope: CURRENT — AUTHORITATIVE
**Error:** intermediates are rounded or truncated and the damage carried forward —
"a significant number of candidates lost marks through simple rounding errors";
"rounding errors to 10.7 were seen" where one decimal place was requested; and "A few
lost a mark by not dividing by 100 or rounding the answer to 11."
**Why it occurs [SIB_INFERENCE]:** calculator-display habits; "one decimal place" applied throughout
rather than to the final answer.
**Correct technique:** carry at least the question data's significant figures through all
intermediates; round once, at the end, to the requested precision.
**Typical manifestation:** final answers off by rounding; examiner advice: "suggesting a
need for greater care in evaluating final answers."
**Diagnostic signals [SIB_INFERENCE]:** multi-step chains; inspect intermediate values.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2025 4CH1/2CR, Introduction (SRC-ER-4CH1,
2025-06/4CH1-2CR/er.pdf p3); November 2023 4CH1/1C, Q2c(ii) (SRC-ER-4CH1,
2023-11/4CH1-1C/er.pdf p3); June 2019 4CH1/2CR, Question 2(b) (SRC-ER-4CH1,
2019-06/4CH1-2CR/er.pdf p3).

### MIS-037 — RAM rounded to the dominant isotope, defeating the calculation

**Concepts:** relative atomic mass; isotopes
**Specification Points:** 1.26, 1.31
Temporal scope: CURRENT — AUTHORITATIVE
**Error:** the computed average is rounded to the most abundant isotope's mass number —
"just rounding the answer to the value of the most abundant isotope defeats the purpose
of doing the calculation."
**Why it occurs [SIB_INFERENCE]:** the answer looks 'wrong' if not a whole number; candidates do not see
that the non-integer IS the result.
**Correct technique:** the weighted mean is the answer; precision is the point of the
calculation.
**Typical manifestation:** 11 offered where the weighted mean was required.
**Diagnostic signals [SIB_INFERENCE]:** RAM-from-isotopes items; check whether the answer preserved the
mean.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2019 4CH1/2CR, Question 2(b) (SRC-ER-4CH1,
2019-06/4CH1-2CR/er.pdf p3).

### MIS-038 — Stoichiometric ratio neglected

**Concepts:** mole calculations; reacting ratios
**Specification Points:** 1.31, 1.42
Temporal scope: CURRENT — AUTHORITATIVE
**Error:** the equation's ratio is ignored and a 1:1 relationship assumed — "Calculation
questions were well attempted, but frequently the stoichiometric ratio was neglected,
and candidates were then unable to score full marks"; and "Ratios in equations were a
problem for some candidates and this was often missed."
**Why it occurs [SIB_INFERENCE]:** the ratio lives in the equation, not the arithmetic habit; mole-map
recipes skip it.
**Correct technique:** mass → moles with plain Mr; apply the ratio ONCE at the mole
stage; convert back.
**Typical manifestation:** correct method, wrong factor of 2/3.
**Diagnostic signals [SIB_INFERENCE]:** any multi-step mole question; check where the ratio entered.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2024 4CH1/2CR, Introduction (SRC-ER-4CH1,
2024-06/4CH1-2CR/er.pdf p3); June 2022 4CH1/1C, Introduction (SRC-ER-4CH1,
2022-06/4CH1-1C/er.pdf p3).

### MIS-039 — Stoichiometric ratio applied twice

**Concepts:** mole calculations; Mr usage
**Specification Points:** 1.31, 1.42
Temporal scope: CURRENT — AUTHORITATIVE
**Error:** the mirror-image failure — "Candidates just need to take care, in moles
calculations, to consider the ratio only once. Some candidates incorporate the ratio in
the calculation of Mr – which is an acceptable method – but then consider it again later
in the calculation."
**Why it occurs [SIB_INFERENCE]:** the ratio is mis-filed as belonging to 'the Mr step' AND 'the mole
step'; both habits fire.
**Correct technique:** the ratio enters the calculation at exactly one point — either
inside Mr (acceptable) or at the mole conversion (standard), never both.
**Typical manifestation:** correct-looking working with a systematic factor error.
**Diagnostic signals [SIB_INFERENCE]:** mole chains; count how many times the ratio multiplies.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2023 4CH1/2CR, Introduction (SRC-ER-4CH1,
2023-06/4CH1-2CR/er.pdf p3).

### MIS-040 — Volume conversion omitted in titration work

**Concepts:** titrations; moles; cm3 → dm3
**Specification Points:** 1.31, 1.42
Temporal scope: CURRENT — AUTHORITATIVE
**Error:** "The most common error was to omit the volume conversion, giving an answer of
1.25 which was awarded one mark" where 0.00125 was required.
**Why it occurs [SIB_INFERENCE]:** the ÷1000 step is attached to 'chemistry numbers' rather than to the
unit; the raw division looks finished.
**Correct technique:** convert cm3 → dm3 before moles = conc × vol; carry units through
the chain.
**Typical manifestation:** factor-of-1000 answers; one of two marks salvaged.
**Diagnostic signals [SIB_INFERENCE]:** titration chains; check the unit on every volume.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2019 4CH1/2CR, Question 6(d)(i) (SRC-ER-4CH1,
2019-06/4CH1-2CR/er.pdf p6).

### MIS-041 — Final-answer precision and 'deduce' discipline

**Concepts:** significant figures; command-word economy
**Specification Points:** 1.26, 1.31
Temporal scope: CURRENT — AUTHORITATIVE
**Error:** two terminal mistakes — answers "to only one significant figure" where the
data did not justify it, and wasted effort against the command word: "When a question is
just worth one mark and starts with the command word 'deduce' this usually means that no
calculation is necessary… some candidates wasted time attempting to calculate the moles
of ethanoic acid."
**Why it occurs [SIB_INFERENCE]:** precision rules are applied as defaults; command words are skimmed.
**Correct technique:** give the answer at the precision the data supports; read 'deduce'
as 'no calculation required'.
**Typical manifestation:** precision marks dropped; time lost on unnecessary work.
**Diagnostic signals [SIB_INFERENCE]:** one-mark items; audit final-answer figures.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2019 4CH1/2CR, Question 6(d) (SRC-ER-4CH1,
2019-06/4CH1-2CR/er.pdf p6).

### MIS-042 — Electron configuration vs total electron count

**Concepts:** atomic structure; electron configuration
**Specification Points:** 1.17, 1.19, 1.20
Temporal scope: CURRENT — AUTHORITATIVE
**Error:** the configuration is answered with a scalar — "a few wrote the total number
of electrons (5) instead of the electron configuration (2,3)"; relatedly "A minority
thought boron was in period 1".
**Why it occurs [SIB_INFERENCE]:** the question's noun (configuration) is read as 'how many electrons'.
**Correct technique:** configuration is a per-shell list; period follows shell count.
**Typical manifestation:** '5' where '2,3' was asked.
**Diagnostic signals [SIB_INFERENCE]:** configuration items; require the comma-list form.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2019 4CH1/2CR, Question 2(a) (SRC-ER-4CH1,
2019-06/4CH1-2CR/er.pdf p3).

## Evidence / Source Basis

- **Primary evidence:** SRC-ER-4CH1 — official Pearson examiner reports; bounded page
  excerpts with page locators in this run's MIS-05 evidence pack
  (evidence/MIS-05/evidence_pack.json, sha256 of record in the run manifest and
  (census.json, artifacts.MIS-05.pack_sha256)); 8 report files, 14 excerpts extracted.
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
the run's MIS-05 evidence pack. Current/legacy separation: fully CURRENT assessment
evidence; no legacy claims. Determinism: content fingerprint recorded in the run
manifest; regeneration produces a new artifact_version.
