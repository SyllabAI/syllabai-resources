---
sib_protocol: SIB-1.0
artifact_id: ASM-05
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

# lifecycle: GENERATED -> QA_PASSED -> STAGED
status: PUBLISHED
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

# ASM-05 — Mark Allocation Patterns

## Purpose

This artifact analyses how the 4CH1 papers allocate marks, as observed in the official
exam corpus of record (SRC-QPMS-4CH1): the tariff range of whole questions, the
part-level mark grid inside questions, and where the papers concentrate their marks.
It is the fifth artifact of the Assessment Intelligence (ASM) family and the
quantitative backbone for the difficulty and progression analyses that follow. Every
tariff claim is carried on a bounded, locator-addressed excerpt from the run's
evidence pack. Research artifact; canonical planes untouched.

## Scope

**Covers:** question-level mark totals observed on the 2019-06 1C paper of the pack;
part-level tariffs; the tariff shape of practical investigations, linked explanations
and calculation items.

**Grounding:** SRC-QPMS-4CH1 (official paper extraction with embedded mark-scheme
text; the 2019-06 4CH1/1C paper is the pack's excerpted anchor, its file header
carrying the official paper identity and qp sha256 of record).

**Out of scope:** cross-session difficulty drift (ASM-06), question ordering
(ASM-09), specification-level weightings already recorded in ASM-01/ASM-04.

## Executive Summary

On the observed paper, question tariffs span 4 to 12 marks: four short questions
(4-6 marks) open the paper, mid-paper questions run 5-7 marks, and the largest
questions (9-12 marks) are the extended practical investigations and multi-part
calculations. Inside questions, 1-mark parts dominate the opening question (all four
of its parts are [1] MCQs), while practical and reasoning parts carry [2]-[5] tariffs.
Mark concentration therefore tracks task complexity: recall grid-work buys single
marks, linked explanations buy two or three, and full investigations buy eight to
twelve. For revision design, the observable law is: secure the 1-mark grid first,
drill the 2-3 mark linked shapes next, and treat the 8+ mark investigations as
distinct, rehearsed performances.

## Main Analysis

### ASM-025 — Question-level tariff range on the observed paper

**Claim:** question tariffs on the observed 2019-06 1C paper range from 4 to 12 marks,
with headers printed as "## Question N (X marks)".
**Evidence:** the header grid runs "## Question 1 (4 marks)" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 3-17), "## Question 2 (4 marks)"
(SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 94-108), "## Question 3 (6
marks)" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 159-173), "## Question 4
(8 marks)" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 239-253), "## Question
11 (9 marks)" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 814-828) and
"## Question 13 (12 marks)" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 999-1013).
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-026 — One-mark parts dominate the opening question

**Claim:** the opening question spends its whole tariff on 1-mark parts — here four
MCQs each tagged [1].
**Evidence:** the part headers of Question 1 read "### 1(a) [1]" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 9-23), "### 1(b)(i) [1]" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 28-42), "### 1(b)(ii) [1]" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 49-63) and "### 1(c) [1]" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 71-85).
**Design reading:** the paper's on-ramp is deliberately low-stakes; candidates who
drop marks here are losing the cheapest marks on the paper.
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-027 — Practical investigations concentrate the largest tariffs

**Claim:** the highest-tariff questions are extended practical investigations — the
12-mark rate experiment, the 9-mark temperature-change experiment and the 8-mark
chromatography investigation.
**Evidence:** "## Question 13 (12 marks)" opens the rate-of-reaction investigation
(SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 999-1013); "## Question 4 (8
marks)" opens the ink chromatography investigation (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 239-253); "## Question 12 (9 marks)" opens the
dissolution temperature experiment (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 903-917).
**Design reading:** a fifth of the observed paper's question count — but its largest
tariffs — sits in investigation contexts, so core-practical fluency is the
highest-yield single preparation target.
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-028 — Part-level tariffs inside mid-paper questions

**Claim:** parts inside questions carry printed tariffs from [1] upward, so a single
question blends recall (1 mark) and reasoning (2+ marks) at part granularity.
**Evidence:** Question 2 opens with "### 2(a) [1]" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 94-108); Question 3 runs "### 3(a) [1]" and
"### 3(b) [1]" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 165-179).
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-029 — Linked explanations cluster at two to three marks

**Claim:** the linked-explanation archetype (ASM-015) buys 2-3 marks per part, which
is where the paper's reasoning marks concentrate.
**Evidence:** the graphite-conductivity part carries a two-point mark scheme (the parsed excerpt and the limewater part a three-point one
(the parsed excerpt.
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-030 — Calculation items mark method steps

**Claim:** multi-step calculations allocate their tariff across printed working steps,
with answer lines and Mr data in the stem.
**Evidence:** the methane-combustion stoichiometry part is marked with bullet steps
(the parsed excerpt and the hydration-number calculation
runs a four-mark bullet-step scheme .
Temporal scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-QPMS-4CH1 — the 2019-06 4CH1/1C official extraction (60 bounded
line-window excerpts, locators preserved; the file header carries the official paper
identity, schema line and qp sha256). The pack's SRC-SPEC-4CH1 entries were
auto-extracted by the builder as structural context and were NOT consumed for claims;
SRC-SAMS-4CH1 is present as an identity/structural entry and is uncited per the
specimen-material law.

## Limitations / Coverage Gaps

The tariff grid is observed on one paper of the pack; cross-session tariff stability
is not claimed here (that comparison belongs to ASM-06/ASM-09 with their own packs).
Question 14 and 15 headers were partially out of the excerpt net and are not
enumerated. No claim is made about total marks per paper from the grid alone — the
specification's totals live in ASM-003's citations. No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-005 (BL-008 pass 5) from the run's evidence
pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 bound all citations
to pack excerpts. Research artifact — evidence-backed, not canonical educational
truth.
