---
sib_protocol: SIB-1.0
artifact_id: EXM-03
artifact_version: 1.0
subject: Chemistry
qualification: International GCSE
specification: 4CH1
curriculum_version: "2017"

research_family: examiner_intelligence
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
generated_at: 2026-10-26

provenance:
  source_manifest: "SRC-ER-4CH1"
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

# EXM-03 — What Examiners Reward

## Purpose

This artifact catalogues what the official 4CH1 examiner reports single out for
reward, as held in the corpus of record (SRC-ER-4CH1): well-answered extended
responses, strong mathematical work, above-expected calculation performance,
well-judged paper balance and preparation that paid. Every claim is carried on a
bounded, page-located excerpt from the run's evidence pack, with paper/session
identity preserved. Research artifact; canonical planes untouched.

## Scope

**Covers:** named well-answered questions; mathematical-skill rewards;
above-expectation performance notes; balance/accessibility judgements; preparation
effects.

**Grounding:** SRC-ER-4CH1 (the 2023-06 1C/1CR/2C and 2024-06 2C report excerpts of
the pack).

**Out of scope:** warnings (EXM-02) and penalties (EXM-04); mark-scheme-derived
sentiment (forbidden substitution — rewards here come only from report text).

## Executive Summary

The reports reward in consistent categories. Extended responses are named
question-by-question when they go well; mathematical skills are praised as a
strength of the cohort, with graph work, mole calculations and RAM calculations
singly cited for full-mark performance; papers are rewarded as well balanced when
they carry accessible marks on all questions; and preparation effects are stated
plainly. For revision design, the reward map is a positive syllabus: the examiners'
own list of what a cohort did well is the list of what good preparation produces.

## Main Analysis

### EXM-010 — Extended responses named for quality

**Claim:** reports name the specific extended-response parts that were particularly
well answered.
**Evidence:** "Some of the extended response questions were particularly well
answered" — the 2023-06 1C introduction praises topic-spanning knowledge ("In
general, candidates performed well on this paper and displayed good knowledge across
a range of topic areas.") (SRC-ER-4CH1, 2023-06/4CH1-1C/er.pdf p3).
Temporal scope: CURRENT — AUTHORITATIVE.

### EXM-011 — Mathematical skills rewarded at full marks

**Claim:** mathematical work (graphs, moles, RAM) is cited for full-mark
performance.
**Evidence:** "Where mathematical skills were assessed eg in graph plotting, in
moles calculations, or in calculating a relative atomic mass, many candidates were
able to score full marks." (SRC-ER-4CH1, 2023-06/4CH1-1C/er.pdf p3).
Temporal scope: CURRENT — AUTHORITATIVE.

### EXM-012 — Calculations performing above expectation

**Claim:** reports note when calculation performance exceeded their expectation, and
attribute it.
**Evidence:** "The calculations on this paper performed better than expected, which
was understandable as overseas candidates often have good mathematical skills..."
(SRC-ER-4CH1, 2023-06/4CH1-1CR/er.pdf p3); the 2C sibling repeats the judgement
(SRC-ER-4CH1, 2023-06/4CH1-2C/er.pdf p3).
Temporal scope: CURRENT — AUTHORITATIVE.

### EXM-013 — Balance and accessibility rewarded

**Claim:** papers are praised for carrying accessible marks across all questions.
**Evidence:** "The paper was well balanced, with accessible marks on all questions."
(SRC-ER-4CH1, 2023-06/4CH1-1CR/er.pdf p3); "well balanced with some accessible marks
on all questions" (SRC-ER-4CH1, 2023-06/4CH1-2C/er.pdf p3).
Temporal scope: CURRENT — AUTHORITATIVE.

### EXM-014 — Performance beyond expectation on novel formats

**Claim:** examiners reward cohorts that handle unfamiliar formats well.
**Evidence:** the 2024-06 2C introduction on the unusual double-curve graph —
"However many candidates did surprisingly well in this question with quite a few
gaining all ten marks." (SRC-ER-4CH1, 2024-06/4CH1-2C/er.pdf p3).
Temporal scope: CURRENT — AUTHORITATIVE.

### EXM-015 — Discrimination praised when fair

**Claim:** reports reward papers that discriminate while staying fair across grades.
**Evidence:** "This paper discriminated well and gave a range of marks over all
grades." (SRC-ER-4CH1, 2023-06/4CH1-1CR/er.pdf p3); "This paper discriminated well
giving a range of marks for all grades." (SRC-ER-4CH1, 2023-06/4CH1-2C/er.pdf p3).
Temporal scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-ER-4CH1 — the 2023-06 and 2024-06 examiner-report PDFs of the
pack (page-located excerpts from the commentary zone; per-file identity carried by
the paper-dir paths). Paper identity rides on SRC-QPMS-4CH1 per the source
manifest's limitation note. No mark schemes were consumed for reward claims; the
examiner-sentiment substitution is forbidden and was not made.

## Limitations / Coverage Gaps

The reward catalogue covers the pack's excerpted reports (2023-06, 2024-06); other
held sessions sit in sibling packs. Sessions without public ERs remain source gaps
of record. No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-005 (BL-008 pass 5) from the run's evidence
pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 bound all citations
to pack excerpts. Research artifact — evidence-backed, not canonical educational
truth.
