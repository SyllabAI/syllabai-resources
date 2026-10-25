---
sib_protocol: SIB-1.0
artifact_id: EXM-05
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

# EXM-05 — Question-Specific Examiner Insights

## Purpose

This artifact collects the examiner reports' question-specific insights for 4CH1, as
held in the corpus of record (SRC-ER-4CH1): what individual questions and parts
actually tested, where candidates succeeded, and where they failed — anchored
question-by-question with paper/session identity. Every claim is carried on a
bounded, page-located excerpt from the run's evidence pack. Research artifact;
canonical planes untouched.

## Scope

**Covers:** per-question insights on the 2019-06 papers of the pack — particle
labelling, mass-number deduction, particle-description demands, the oxygen test,
displacement reasoning and the stem-repeat ruling.

**Grounding:** SRC-ER-4CH1 (the 2019-06 1C/1CR/2C/2CR reports) with paper-identity
headers from SRC-QPMS-4CH1.

**Out of scope:** general technique advice (EXM-06), warning/reward catalogues
(EXM-02/EXM-03).

## Executive Summary

The report commentary works at part granularity. On the 2019-06 papers it records:
the atom-labelling opener succeeded because the particle names were given in a box,
yet a minority confused protons with neutrons; the mass-number part demanded
deduction from a diagram; the solid-particle description paid two marks for
arrangement-plus-movement; the oxygen test failed on reagent choice (splints); the
displacement explanation failed on the missing causal link; and the group-similarity
part was ruled not creditworthy when answered by repeating the stem. Each insight is
a teaching note written by the board itself.

## Main Analysis

### EXM-022 — Atom labelling: box-supported success, proton/neutron confusion

**Claim:** the opening labelling part succeeded broadly because names were supplied,
but particle confusion persisted in a minority.
**Evidence:** "Question 1 (a) As anticipated, the great majority of candidates were
able to correctly label the diagram of an atom using the names of some particles
which were given in the box. A small minority confused protons and neutrons in the
nucleus." (SRC-ER-4CH1, 2019-06/4CH1-2C/er.pdf p4).
Temporal scope: CURRENT — AUTHORITATIVE.

### EXM-023 — Mass-number deduction from a diagram

**Claim:** the follow-on part demanded deduction, not recall.
**Evidence:** "Question 1 (b) Candidates had to deduce the mass number of the atom
from the..." — the 2C report's part note (SRC-ER-4CH1, 2019-06/4CH1-2C/er.pdf p4).
Temporal scope: CURRENT — AUTHORITATIVE.

### EXM-024 — The solid-particle description demand

**Claim:** the 1CR opening description part paid for arrangement AND movement, with
most candidates banking at least two marks.
**Evidence:** "In (b) the question specifically asked for a description of the
arrangement and movement of particles in a solid. Most candidates were able to score
at least two marks with many..." (SRC-ER-4CH1, 2019-06/4CH1-1CR/er.pdf p3).
Temporal scope: CURRENT — AUTHORITATIVE.

### EXM-025 — The oxygen test: reagent choice is the discriminator

**Claim:** the gas-test part was lost on reagent choice, not on knowledge of gases.
**Evidence:** "Part (a) was very well answered by the majority of candidates, but
some lost the mark in (b) for using a lighted or unlit splint to test for oxygen."
(SRC-ER-4CH1, 2019-06/4CH1-2CR/er.pdf p3).
Temporal scope: CURRENT — AUTHORITATIVE.

### EXM-026 — Displacement: observation without mechanism

**Claim:** the halogen-displacement part separated candidates who linked the
reactivity cause from those who only named the product.
**Evidence:** "Some knew bromine was formed but failed to explain that this was
because chlorine is more reactive than bromine. A number of candidates, despite
noting correctly that bromine was formed, attributed the or..." (SRC-ER-4CH1, 2019-06/4CH1-2CR/er.pdf p4).
Temporal scope: CURRENT — AUTHORITATIVE.

### EXM-027 — The stem-repeat ruling on the group-similarity part

**Claim:** the 1C group-similarity part was ruled not creditworthy for stem
repetition.
**Evidence:** "Those who did not score here often just stated that the elements were
in the same group, which was just a repeat of the stem of the question and is,
therefore, not creditworthy." (SRC-ER-4CH1, 2019-06/4CH1-1C/er.pdf p4).
Temporal scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-ER-4CH1 — the 2019-06 1C/1CR/2C/2CR examiner-report PDFs
(page-located excerpts from the commentary zone; per-file identity carried by the
paper-dir paths); SRC-QPMS-4CH1 supplies the papers' own question headers in the
pack for cross-reference. Two quotation windows truncate mid-sentence at the excerpt
cap; the unexcerpted continuations are not paraphrased. No mark schemes were
consumed for insight claims.

## Limitations / Coverage Gaps

The question-specific insights cover the pack's 2019-06 reports; the corpus's later
held sessions (2022-2025) are analysed only where sibling packs carry them. Sessions
without public ERs remain source gaps of record. No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-005 (BL-008 pass 5) from the run's evidence
pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 bound all citations
to pack excerpts. Research artifact — evidence-backed, not canonical educational
truth.
