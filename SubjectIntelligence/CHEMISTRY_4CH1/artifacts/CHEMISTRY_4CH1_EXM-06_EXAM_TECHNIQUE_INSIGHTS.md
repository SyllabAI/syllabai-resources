---
sib_protocol: SIB-1.0
artifact_id: EXM-06
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

status: GENERATED
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

# EXM-06 — Exam Technique Insights

## Purpose

This artifact distils the exam-technique guidance embedded in the official 4CH1
examiner reports of the corpus of record (SRC-ER-4CH1): the behaviours the examiners
explicitly tell candidates to adopt — specify quantities exactly, write symbols
legibly, link explanation statements, read the method, read table keys correctly and
rehearse practical technique. Every claim is carried on a bounded, page-located
excerpt from the run's evidence pack, with paper/session identity preserved.
Research artifact; canonical planes untouched.

## Scope

**Covers:** six technique insights drawn from the 2023-2024 report excerpts of the
pack.

**Grounding:** SRC-ER-4CH1 (the 2023-06 2C/2CR, 2023-11 1C/2C and 2024-06 1CR
reports of the pack).

**Out of scope:** question-specific mechanics (EXM-05), penalty catalogue (EXM-04).

## Executive Summary

The reports' technique advice is refreshingly concrete. Give values, not gestures: a
charge must be stated as -1, not as "a minus sign with no value". Write subscripts
clearly, because ambiguous formulae lose marks regardless of the chemistry. In
multi-mark explanations, LINK the statements — the link is the mark. Read the method
before answering: variable-control parts fail wholesale when the method is skipped.
Read table keys correctly: relative atomic mass and atomic number sit in different
columns. And treat practical questions as a rehearsed skill, since their performance
is variable "as always". None of this is guesswork — every line is the board's own
advice to the next cohort.

## Main Analysis

### EXM-028 — Specify values exactly, not by gesture

**Claim:** answers must give the exact value; an unquantified sign does not score.
**Evidence:** "The most common error was missing the charge – or giving the wrong
charge – for the electron. Some candidates simply gave a minus sign with no value:
it did need to be – 1 in order to be equal (but opposite) the charge on a proton."
(SRC-ER-4CH1, 2023-06/4CH1-2CR/er.pdf p4).
Temporal scope: CURRENT — AUTHORITATIVE.

### EXM-029 — Write chemical symbols legibly

**Claim:** subscripts and formulae must be unambiguous.
**Evidence:** "Candidates need to take care to write their subscript numbers clearly
wh..." — the 2023-11 1C formula-work advice (SRC-ER-4CH1, 2023-11/4CH1-1C/er.pdf p4).
Temporal scope: CURRENT — AUTHORITATIVE.

### EXM-030 — Link the statements in extended explanations

**Claim:** multi-mark explanations pay for the link, not the statements alone.
**Evidence:** "Many of the candidates struggled with these questions and only the
very best scored full marks. They needed to link the statements to gain all the
marks" (SRC-ER-4CH1, 2024-06/4CH1-1CR/er.pdf p3).
Temporal scope: CURRENT — AUTHORITATIVE.

### EXM-031 — Read the method and its variable-control design

**Claim:** method-led parts fail wholesale when the printed method is skipped.
**Evidence:** "It appears that the candidates either did not read the method or did
not understand the idea of keeping the variables constant. As the acid was added
initially there could not be a change in the volume, concentration or initial
temperature." (SRC-ER-4CH1, 2023-11/4CH1-2C/er.pdf p4).
Temporal scope: CURRENT — AUTHORITATIVE.

### EXM-032 — Read the table keys correctly

**Claim:** data-table literacy (RAM vs atomic number columns) is an examined
technique.
**Evidence:** "A small minority confused relative atomic mass with atomic number and
wrote nitrogen, even though the key on the Periodic Table showed where the atomic
number was." (SRC-ER-4CH1, 2023-06/4CH1-2C/er.pdf p4).
Temporal scope: CURRENT — AUTHORITATIVE.

### EXM-033 — Practical questions reward rehearsed technique

**Claim:** the reports flag practical-situation questions as a persistent variability
— and definition-level precision as a weak spot.
**Evidence:** "Questions on practical situations, as always, produced a variable"
followed by the alloy observation "Candidates answered the question about an alloy's
properties, but were less sure about a definition for an alloy." (SRC-ER-4CH1, 2023-06/4CH1-2CR/er.pdf p3).
Temporal scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-ER-4CH1 — the 2023-06 2C/2CR, 2023-11 1C/2C and 2024-06 1CR
examiner-report PDFs of the pack (page-located excerpts from the commentary zone;
per-file identity carried by the paper-dir paths). One quotation window truncates at
the excerpt cap; the continuation is not paraphrased. No mark schemes were consumed
for technique claims; no specimen material was cited.

## Limitations / Coverage Gaps

The technique inventory covers the pack's 2023-2024 report excerpts; earlier and
later held sessions sit in sibling packs. Sessions without public ERs remain source
gaps of record. No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-005 (BL-008 pass 5) from the run's evidence
pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 bound all citations
to pack excerpts. Research artifact — evidence-backed, not canonical educational
truth.
