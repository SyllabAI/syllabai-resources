---
sib_protocol: SIB-1.0
artifact_id: ASM-09
artifact_version: 1.0
subject: Chemistry
qualification: International GCSE
specification: 4CH1
curriculum_version: "2017"

research_family: assessment_intelligence
applicability: REQUIRED

temporal_scope:
  current: true
  legacy: false

source_scope:
  specification: true
  textbook: false
  question_papers: true
  mark_schemes: true
  examiner_reports: false
  supplementary: true

status: GENERATED
generated_by: zai_agent
generated_at: 2026-10-26

provenance:
  source_manifest: "SRC-QPMS-4CH1"
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-005"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "f61a5bafe6cacdf538e5e06d86f818e7737cbfe3"
    syllabai_resources: "367b5d61cd5f1ab115f9947ba2981f08389540ee"
---

# ASM-09 — Question Progression Patterns

## Purpose

This artifact analyses how the 4CH1 papers progress question-by-question — where the
big tariffs sit, how investigations are positioned, and what the opening formula of
each question looks like — as parsed in the official exam corpus of record
(SRC-QPMS-4CH1). It reads the question-header grids of six paper files across the
2019-2021 sessions held in the run's pack. Every claim is carried on a bounded,
locator-addressed excerpt from that pack. Research artifact; canonical planes
untouched.

## Scope

**Covers:** the question-opener formula; tariff envelopes across question positions;
the placement of large investigations; and the (non-monotonic) shape of a paper's
difficulty ramp.

**Grounding:** SRC-QPMS-4CH1 (the 2019-06 2C/1CR, 2020-01 2C/1CR, 2020-11 2C/1CR and
2021-01 2C papers of the pack).

**Out of scope:** within-question part progression (ASM-05/ASM-06), cross-session
statistics beyond the held pack.

## Executive Summary

The papers announce every question with a context formula ("This question is about
..."), then allocate tariffs that sustain a mid-band (7-11 marks) through most of the
paper. Large investigations (13-15 marks) appear at varied positions — third,
second-to-last or last — rather than at a fixed slot, and several 2C papers open
their second question at 9-11 marks directly after a short opener. The ramp is NOT
strictly monotonic: 7-mark questions sit beside 15-mark ones late in papers. The
stable signal is a broad middle band and a guaranteed extended investigation
somewhere in the second half, with the closing questions carrying the heaviest
chains.

## Main Analysis

### ASM-049 — The question-opener formula

**Claim:** virtually every question announces its context in a single opening line
before any part appears.
**Evidence:** "This question is about some elements in Group 1 of the Periodic
Table." (SRC-QPMS-4CH1, 2019-06/4CH1-1CR/questions.md lines 71-85); "This question
is about some Group 2 elements and their compounds." (SRC-QPMS-4CH1, 2020-01/4CH1-2C/questions.md lines 620-634); "This question is about the insoluble
salt silver chloride (AgCl)." (SRC-QPMS-4CH1, 2021-01/4CH1-2C/questions.md lines 445-459).
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-050 — The mid-band tariff envelope

**Claim:** the papers sustain a 7-11 mark band across their middle questions.
**Evidence:** the 2019-06 2C headers "## Question 2 (9 marks)", "## Question 3 (9
marks)" (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 47-61),
"## Question 7 (8 marks)" and "## Question 8 (7 marks)" (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 561-575); the 2020-11 1CR run "## Question 9 (11 marks)" (SRC-QPMS-4CH1, 2020-11/4CH1-1CR/questions.md lines 855-869).
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-051 — Extended investigations are not position-locked

**Claim:** the largest investigations appear at different positions — third question
in one paper, closing question in another.
**Evidence:** the 15-mark chromatography investigation opens at Question 3 — "## Question 3 (15 marks) A student uses paper chromatography to investigate the dyes
in five different inks, V, W, X, Y and Z." (SRC-QPMS-4CH1, 2019-06/4CH1-1CR/questions.md lines 138-152); the 15-mark metal-oxide reduction
closes 2020-01 1CR at Question 11 (SRC-QPMS-4CH1, 2020-01/4CH1-1CR/questions.md lines 1073-1087); the 13-mark titration closes 2020-11 1CR at Question 10
(SRC-QPMS-4CH1, 2020-11/4CH1-1CR/questions.md lines 979-993).
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-052 — 2C papers can open big at Question 2

**Claim:** several 2C papers place an 11-mark question at position two, immediately
after a short opener.
**Evidence:** "## Question 2 (11 marks) Crude oil is a mixture of hydrocarbons."
(SRC-QPMS-4CH1, 2020-01/4CH1-2C/questions.md lines 65-79); "## Question 3 (11
marks) This question is about copper and its compounds." with the electrolysis
apparatus (SRC-QPMS-4CH1, 2020-01/4CH1-2C/questions.md lines 203-217); the 2019-06
2C pair at 9 marks (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 47-61).
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-053 — The closing questions carry the heaviest chains

**Claim:** the last questions of the observed 1CR papers run 10-15 marks, closing on
extended practical or synthesis chains.
**Evidence:** the 2020-01 1CR closing run "## Question 10 (11 marks)" on carbon and
its compounds (SRC-QPMS-4CH1, 2020-01/4CH1-1CR/questions.md lines 976-990) and "## Question 11 (15 marks)" on metal-oxide reduction (SRC-QPMS-4CH1, 2020-01/4CH1-1CR/questions.md lines 1073-1087); the 2019-06 1CR closing pair "## Question 9 (11 marks)" and "## Question 10 (10 marks)" (SRC-QPMS-4CH1, 2019-06/4CH1-1CR/questions.md lines 1037-1051).
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-054 — The ramp is not strictly monotonic

**Claim:** question tariffs do not increase strictly with position; 7-8 mark
questions sit beside 14-15 mark ones late in papers.
**Evidence:** the 2021-01 2C tail runs "## Question 6 (15 marks)" then "## Question
7 (14 marks)" (SRC-QPMS-4CH1, 2021-01/4CH1-2C/questions.md lines 445-459), while the 2020-11 2C tail holds a 7-mark gases question — "## Question 7
(7 marks)" (SRC-QPMS-4CH1, 2020-11/4CH1-2C/questions.md lines 669-683) — after an
11-mark titration (SRC-QPMS-4CH1, 2020-11/4CH1-2C/questions.md lines 527-541).
Temporal scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-QPMS-4CH1 — question-header grids excerpted from the 2019-06
2C/1CR, 2020-01 2C/1CR, 2020-11 2C/1CR and 2021-01 2C official extractions (bounded
line-window excerpts with line locators preserved). No ER evidence consumed; no
specimen material cited; supplementary sources not consumed for claims.

## Limitations / Coverage Gaps

The progression analysis covers the pack's seven excerpted paper files across
2019-2021; later sessions are held in the corpus but not excerpted into this pack.
Full-paper tariff sequences are observed only where both the opening and closing
headers fall inside excerpt windows; intermediate questions between windows are not
enumerated. No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-005 (BL-008 pass 5) from the run's evidence
pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 bound all citations
to pack excerpts. Research artifact — evidence-backed, not canonical educational
truth.
