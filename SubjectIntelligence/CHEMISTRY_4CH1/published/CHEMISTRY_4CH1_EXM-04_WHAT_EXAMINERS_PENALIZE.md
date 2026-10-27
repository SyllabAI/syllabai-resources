---
sib_protocol: SIB-1.0
artifact_id: EXM-04
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

# EXM-04 — What Examiners Penalize

## Purpose

This artifact catalogues what the official 4CH1 examiner reports identify as penalised
or mark-losing behaviour, as held in the corpus of record (SRC-ER-4CH1): failed
instructions, inattentive formulae work, unread methods, unlinked statements, quantity
confusions and notation misuse. Every claim is carried on a bounded, page-located
excerpt from the run's evidence pack, with paper/session identity preserved. Research
artifact; canonical planes untouched.

## Scope

**Covers:** instruction-following failures; formula and subscript care; method-reading
failures; unlinked-explanation losses; proton/mass-number confusions; notation misuse.

**Grounding:** SRC-ER-4CH1 (the 2023-11 1C/2C and 2024-06 1CR/2C report excerpts of
the pack).

**Out of scope:** mark-scheme-derived loss patterns (MS-05's ground); warnings
framing (EXM-02).

## Executive Summary

The reports are specific about losses. Candidates lose marks for not following
printed instructions (the particle-drawing count), for inattention to the starting
formula in organic work and unclear subscripts, for not reading (or not understanding)
the method's variable-control logic, for failing to LINK statements in multi-mark
explanations, for reaching for the mass number when the atomic number is wanted, and
for misusing notation. The pattern beneath the specifics: the examiners penalise
inattention — to the question's own words, to the chemistry's symbols, and to the
method's design — more than they penalise absence of knowledge.

## Main Analysis

### EXM-016 — Failed printed instructions

**Claim:** not following an explicit instruction voids the intended marks.
**Evidence:** "A few candidates failed to follow the instruction to draw another four
particles." (SRC-ER-4CH1, 2023-11/4CH1-1C/er.pdf p3).
Temporal scope: CURRENT — AUTHORITATIVE.

### EXM-017 — Inattentive formula work and unclear subscripts

**Claim:** organic-formula answers are penalised for ignoring the starting hydrocarbon
and for unreadable subscripts.
**Evidence:** "Many correctly gave the formulae of two alkenes but some did not pay
attention to the starting hydrocarbon formula and gave molecules that were too large
or did not follow the formula for an alkene. Candidates need to take care to write
their subscript numbers clearly wh..." (SRC-ER-4CH1, 2023-11/4CH1-1C/er.pdf p4).
Temporal scope: CURRENT — AUTHORITATIVE.

### EXM-018 — Method-reading failures

**Claim:** not reading (or not understanding) the method's variable-control design
costs whole questions.
**Evidence:** "Question (a) was very poorly answered with the majority gaining no
marks. It appears that the candidates either did not read the method or did not
understand the idea of keeping the variables constant." (SRC-ER-4CH1, 2023-11/4CH1-2C/er.pdf p4).
Temporal scope: CURRENT — AUTHORITATIVE.

### EXM-019 — Unlinked statements in multi-mark explanations

**Claim:** the reports tie lost explanation marks directly to missing links between
statements.
**Evidence:** "There were four questions with 4, 5 or 6 marks. All of these were
explanations. Many of the candidates struggled with these questions and only the very
best scored full marks. They needed to link the statements to gain all the marks"
(SRC-ER-4CH1, 2024-06/4CH1-1CR/er.pdf p3).
Temporal scope: CURRENT — AUTHORITATIVE.

### EXM-020 — Quantity confusions: mass number vs atomic number

**Claim:** reaching for the wrong nuclear quantity is a named, recurring error.
**Evidence:** "A large majority of candidates gave sulfur as the answer. Oxygen was
seen occasionally as they were using the mass number rather than the atomic number."
(SRC-ER-4CH1, 2024-06/4CH1-2C/er.pdf p4).
Temporal scope: CURRENT — AUTHORITATIVE.

### EXM-021 — Notation misuse

**Claim:** misused notation loses marks even when the chemistry is broadly right.
**Evidence:** "However, a significant number of candidates lost a mark as they often
referred to an incorrect use of" — the 2C November introduction's notation warning
(SRC-ER-4CH1, 2023-11/4CH1-2C/er.pdf p3).
Temporal scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-ER-4CH1 — the 2023-11 1C/2C and 2024-06 1CR/2C examiner-report
PDFs of the pack (page-located excerpts from the commentary zone; per-file identity
carried by the paper-dir paths). Paper identity rides on SRC-QPMS-4CH1 per the
source manifest's limitation note. No mark schemes were consumed for penalty claims;
the examiner-sentiment substitution is forbidden and was not made.

## Limitations / Coverage Gaps

The penalty catalogue covers the pack's excerpted reports (2023-11, 2024-06); other
held sessions sit in sibling packs. One quotation window is truncated by the excerpt
cap (the notation warning's continuation is outside the window and is not
paraphrased). Sessions without public ERs remain source gaps of record. No canonical
planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-005 (BL-008 pass 5) from the run's evidence
pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 bound all citations
to pack excerpts. Research artifact — evidence-backed, not canonical educational
truth.
