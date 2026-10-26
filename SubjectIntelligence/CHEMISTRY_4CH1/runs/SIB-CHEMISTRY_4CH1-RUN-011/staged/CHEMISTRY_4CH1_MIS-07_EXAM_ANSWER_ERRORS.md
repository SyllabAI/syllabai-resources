---
sib_protocol: SIB-1.0
artifact_id: MIS-07
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

# MIS-07 — Exam Answer Errors

## Purpose

This artifact catalogs the exam-technique answer errors that the official Pearson
examiner corpus records for Pearson Edexcel International GCSE Chemistry (4CH1): failures
in how answers are formed and presented — demand mismatches, vagueness, unlinked chains,
wrong answer forms, diagram/equation conventions and legibility — as distinct from the
chemistry itself. Every record is grounded on an official Pearson examiner report for a
named session and paper, carried in the run's evidence pack with page identity. It is a
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

**Covers:** seven exam-answer-error records (MIS-050 … MIS-056) grounded on the official
4CH1 examiner reports held by the library (8 held sessions; papers 1C/2C/1CR/2CR),
extracted into the run's evidence pack with bounded page excerpts and page locators.
Each record states the presentation error, why it occurs, the credit-worthy form, and
the examiner guidance that addresses it.

**Does not cover:** concept confusions (MIS-02), calculation technique (MIS-05),
mark-scheme internals (MS family), legacy 4CH0 sentiment, and sessions without a public
ER (disclosed gaps, never filled).

## Executive Summary

- "Did not answer the question given" is the corpus's named extended-response failure;
  examiners prescribe drafting and ticking off parts.
- Vagueness is the repeat phrasing complaint across at least three series.
- The requested answer form (name vs formula) matters even when the content is allowed.
- Diagram and equation conventions (ruler, arrow length, equilibrium arrows, balancing)
  are explicit mark carriers.

## Main Analysis

### MIS-050 — Not answering the question given (extended response)

**Concepts:** extended writing; demand mapping
**Specification Points:** (assessment-skill strand; AO1/AO2 long-answer items)
Temporal scope: CURRENT — AUTHORITATIVE
**Error:** "In extended response questions, many candidates did not answer the question
given and should be encouraged to draft their ideas first or tick parts of the question
off when they appear in the answer."
**Why it occurs [SIB_INFERENCE]:** long answers are drafted as fact dumps; the demand is not decomposed
into parts to hit.
**Credit-worthy form:** map each mark point to a sentence; tick it off as written.
**Typical manifestation:** all facts present, the asked chain absent.
**Diagnostic signals [SIB_INFERENCE]:** 4-6 mark items; compare the script against the question's parts.
**Examiner guidance [OBSERVED_IN_SOURCE]:** examiners prescribe the exact technique (draft first; tick off).
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2022 4CH1/1C, Introduction (SRC-ER-4CH1,
2022-06/4CH1-1C/er.pdf p3).

### MIS-051 — Answering beside the demand in observation items

**Concepts:** observations; question focus
**Specification Points:** 1.7C, 2.44C
Temporal scope: CURRENT — AUTHORITATIVE
**Error:** the reaction is described where the product's appearance was asked, and
impossible observations offered — "A few described the bright white flame, but the
question asked for the appearance of the magnesium oxide not the reaction that occurred.
A few candidates lost the mark for stating that there was a white precipitate. A
precipitate would only occur if it formed a precipitate at the bottom of a solution, not
in the basin."
**Why it occurs [SIB_INFERENCE]:** rehearsed reaction descriptions fire before the question's noun
('appearance of the product') is registered.
**Credit-worthy form:** answer the noun asked; keep observations physically possible in
the stated context.
**Typical manifestation:** flame description for appearance marks; precipitate claims in
evaporation basins.
**Diagnostic signals [SIB_INFERENCE]:** observation items; check the answer's subject noun.
**Examiner guidance [OBSERVED_IN_SOURCE]:** examiners separate 'the reaction' from 'the product' explicitly.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report November 2023 4CH1/2C, Question 2 (SRC-ER-4CH1,
2023-11/4CH1-2C/er.pdf p3).

### MIS-052 — Vague prose where precision marks live

**Concepts:** explanation quality; precision
**Specification Points:** (assessment-skill strand; AO2 items)
Temporal scope: CURRENT — AUTHORITATIVE
**Error:** "many candidates lost unnecessary marks as they were often too vague when
writing their answers" — repeated across series introductions.
**Why it occurs [SIB_INFERENCE]:** answers are written at the everyday-precision level; mark points pay
for technical specificity.
**Credit-worthy form:** technical nouns and conditions named (the exact reagent, colour,
state, direction).
**Typical manifestation:** partial credit on otherwise-correct explanations.
**Diagnostic signals [SIB_INFERENCE]:** audit scripts for generic verbs ('it reacts', 'it changes')
where a named species/observation was available.
**Examiner guidance [OBSERVED_IN_SOURCE]:** the complaint is named in the same words in multiple series.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2022 4CH1/2C, Introduction (SRC-ER-4CH1,
2022-06/4CH1-2C/er.pdf p3); June 2023 4CH1/2C, Introduction (SRC-ER-4CH1,
2023-06/4CH1-2C/er.pdf p3).

### MIS-053 — Unlinked statement chains in 4-6 mark explanations

**Concepts:** extended writing; causal chains
**Specification Points:** (assessment-skill strand; AO1/AO2 long-answer items)
Temporal scope: CURRENT — AUTHORITATIVE
**Error:** "There were four questions with 4, 5 or 6 marks. All of these were
explanations. Many of the candidates struggled with these questions and only the very
best scored full marks. They needed to link the statements to gain all the marks which
many candidates found difficult."
**Why it occurs [SIB_INFERENCE]:** linking words and because→therefore structure are not rehearsed as
exam skills.
**Credit-worthy form:** each mark is a linked step: identify → because → so → therefore.
**Typical manifestation:** correct fragments, low marks.
**Diagnostic signals [SIB_INFERENCE]:** long-answer items; count links, not facts.
**Examiner guidance [OBSERVED_IN_SOURCE]:** the linking requirement is the examiners' own named criterion.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2024 4CH1/1CR, Introduction (SRC-ER-4CH1,
2024-06/4CH1-1CR/er.pdf p3).

### MIS-054 — Answer form not as requested (name vs formula)

**Concepts:** answer conventions; command wording
**Specification Points:** (assessment-skill strand)
Temporal scope: CURRENT — AUTHORITATIVE
**Error:** "some provided the formula rather than the required name. Whilst the formula
is allowed under the mark scheme it is recommended that candidates read the question
carefully and provide the answer in the form requested which in this instance was the
name (not the formula)."
**Why it occurs [SIB_INFERENCE]:** the shortest correct token is offered; the question's form request is
skipped.
**Credit-worthy form:** the requested form — even when an alternative would be accepted.
**Typical manifestation:** formula-for-name answers; avoided-risk losses.
**Diagnostic signals [SIB_INFERENCE]:** items naming a form ('name', 'state', 'draw'); check the form
delivered.
**Examiner guidance [OBSERVED_IN_SOURCE]:** examiners frame this as reading discipline, not chemistry.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report November 2024 4CH1/1C, Question 2 (SRC-ER-4CH1,
2024-11/4CH1-1C/er.pdf p3).

### MIS-055 — Equation and diagram conventions ignored

**Concepts:** equations; energy diagrams; equilibrium arrows
**Specification Points:** 1.21, 1.22, 3.14 (convention strand)
Temporal scope: CURRENT — AUTHORITATIVE
**Error (cluster):** balancing and formula slips — "Common mistakes included failing to
balance the equation, the formulae being MgO2, Mg2 or O as a single atom rather than
O2"; and evolving conventions — "Q02(e) is no longer allowed for double arrows or just
straight lines. It has to be arrows shown in the right directions."
**Why it occurs [SIB_INFERENCE]:** conventions are treated as presentation extras; marks say otherwise.
**Credit-worthy form:** balanced equations; ruled diagrams with arrows of adequate
length; full equilibrium arrows in the correct directions.
**Typical manifestation:** one-mark losses on form, zero on chemistry.
**Diagnostic signals [SIB_INFERENCE]:** equation/diagram items; audit form before content.
**Examiner guidance [OBSERVED_IN_SOURCE]:** each convention is named with its mark consequence.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report November 2023 4CH1/2C, Question 2 (SRC-ER-4CH1,
2023-11/4CH1-2C/er.pdf p3); June 2025 4CH1/2C, Introduction (SRC-ER-4CH1,
2025-06/4CH1-2C/er.pdf p3).

### MIS-056 — Handwriting and legibility of key terms

**Concepts:** legibility; awarding risk
**Specification Points:** (assessment-skill strand)
Temporal scope: CURRENT — AUTHORITATIVE
**Error:** "marks were occasionally lost due to the word 'boron' not being fully formed.
While benefit of doubt was applied where appropriate, it is important to remind
candidates of the need to write clearly and complete words fully. In other questions,
such as Q09(c), illegible responses had a more significant implication for the awarding
of marks."
**Why it occurs [SIB_INFERENCE]:** exam-speed handwriting degrades exactly the high-frequency terms.
**Credit-worthy form:** complete, unambiguous words and letters.
**Typical manifestation:** benefit-of-doubt awards that flip to zero elsewhere.
**Diagnostic signals [SIB_INFERENCE]:** check scripts for ambiguous letters before mock marking.
**Examiner guidance [OBSERVED_IN_SOURCE]:** candidates should "write clearly and complete words fully".
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2025 4CH1/1C, Question 1(c) (SRC-ER-4CH1,
2025-06/4CH1-1C/er.pdf p6).

## Evidence / Source Basis

- **Primary evidence:** SRC-ER-4CH1 — official Pearson examiner reports; bounded page
  excerpts with page locators in this run's MIS-07 evidence pack
  (evidence/MIS-07/evidence_pack.json, sha256 of record in the run manifest and
  (census.json, artifacts.MIS-07.pack_sha256)); 10 report files, 16 excerpts extracted.
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
the run's MIS-07 evidence pack. Current/legacy separation: fully CURRENT assessment
evidence; no legacy claims. Determinism: content fingerprint recorded in the run
manifest; regeneration produces a new artifact_version.
