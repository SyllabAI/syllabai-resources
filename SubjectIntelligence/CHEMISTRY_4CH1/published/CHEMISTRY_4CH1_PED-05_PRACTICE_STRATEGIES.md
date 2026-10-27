---
sib_protocol: SIB-1.0
artifact_id: PED-05
artifact_version: 1.0
subject: Chemistry
qualification: International GCSE
specification: 4CH1
curriculum_version: "2017"

research_family: learning_pedagogy_intelligence
applicability: REQUIRED

temporal_scope:
  current: true
  legacy: false

source_scope:
  specification: true
  textbook: true
  question_papers: false
  mark_schemes: false
  examiner_reports: true
  supplementary: true

# lifecycle: GENERATED -> QA_PASSED -> STAGED
status: PUBLISHED
generated_by: zai_agent
generated_at: 2026-10-26

provenance:
  source_manifest: "SRC-BOOK-4CH1-SB1"
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-006"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "3b6a443d4e3643f461a1cca12c6e1ad47ab6b596"
    syllabai_resources: "8b5a64f1b18724208ff19969b002028d3ed41bed"
---

# PED-05 — Practice Strategies

## Purpose

This artifact analyses the practice machinery of record for 4CH1: how the student
book instruments its questions (SRC-BOOK-4CH1-SB1 Progression icons and Skills
tags), where structured practice lives (end-of-unit question banks), what the
book's own practice-strategy hints instruct, how the examiner report models good
answers and near-miss feedback (SRC-ER-4CH1), and how the notes corpus paces
practice through worked examples (SRC-SME-NOTES-4CH1). Claims ride only on this
artifact's own bounded pack excerpts. Canonical planes are untouched.

## Scope

**Covers:** progression-icon and skills-tag instrumentation of in-book questions;
end-of-unit question banks and their mark-tagged, data-driven task types;
practice-over-memorisation strategy hints; approach-learning scaffolds;
examiner-modelled good answers and off-target answer warnings; notes-level
worked examples with formula scaffolds.

**Out of scope:** assessment-structure facts (ASM family) and mark-scheme
mechanics (MS family).

## Executive Summary

Practice in the evidence of record is instrumented, not generic: every in-book
question carries Progression icons tied to Pearson's Progression scale and Skills
tags naming the demand. Structured practice concentrates in UNIT QUESTIONS banks
that mix mark-tagged calculations, data tables, and graph-plotting tasks, with
tier-marked CHEMISTRY ONLY blocks inside the same banks. The book's own strategy
hints tell learners how to practise: do not memorise hydrocarbon formulae, work
them out across a range; approach polymerisation by thinking of coloured
rectangle monomers. The examiner report closes the loop by publishing model
good answers at specific mark levels and warning against answers to a slightly
different question. The notes corpus paces the same strategy with formula
triangles and stepped worked examples.

## Main Analysis

### PED-028 — In-book practice is instrumented with Progression icons and Skills tags

**Claim:** questions in the book carry two instrumentation layers — Progression
icons mapped to Pearson's Progression scale and Skills tags naming the demand —
so practice is graded, not just set.
**Evidence:** the book's front matter states "You will also find that questions
in this book have Progression icons and Skills tags" tied to Pearson's
Progression scale (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl
line 12); the instrumentation is visible on the question banks themselves, where
unit questions carry stacked skills tags (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 689, line 1057). Temporal scope:
CURRENT — AUTHORITATIVE.

### PED-029 — End-of-unit question banks structure the practice load

**Claim:** each unit closes with UNIT QUESTIONS banks mixing mark-tagged
calculations, experimental data tables, and graph-plotting tasks, so practice
mirrors assessed task types.
**Evidence:** a Unit 1 bank poses an empirical-formula practical question on
lead oxide and a relative-atomic-mass explain task (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 396, line 397); a rate bank gives
four students' limestone data and asks learners to "Plot the rest of the data on
the graph and draw another straight line of best fit" (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 402, line 403); a percentage-yield
item carries its (2) mark allocation (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 401). Temporal scope: CURRENT —
AUTHORITATIVE.

### PED-030 — Practise-over-memorise strategy hints

**Claim:** the book's practice hints explicitly direct effort from memorisation
to rehearsed method over varied cases.
**Evidence:** the alkanes chapter instructs "Don't try to learn these equations!
Practise working them out for a wide range" of hydrocarbons, with guidance
signposted (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line
947). Temporal scope: CURRENT — AUTHORITATIVE.

### PED-031 — Approach-learning scaffolds for hard manipulations

**Claim:** for hard procedures the book teaches an approach to learn with, not
just the content: monomers become coloured rectangles with functional groups at
the ends.
**Evidence:** the polymers hint states "This is how you should approach learning
this." and works the red-rectangle monomer imagery with the hydroxyl-ended group
positions (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line
1052). Temporal scope: CURRENT — AUTHORITATIVE.

### PED-032 — Examiner-modelled answers and off-target warnings

**Claim:** the examiner report supplies practice feedback of both kinds — a model
good answer at a stated mark level, and a warning that a common answer responds
to a slightly different question.
**Evidence:** the 2023-06 report prints a model answer introduced as "A good
answer which scores 3 marks." crediting the lower-kinetic-energy and
decreased-collision-frequency reasoning (SRC-ER-4CH1, er.pdf p 55); the same
report warns that many answers to the catalyst question were answers "to a
slightly different question" focused on what a catalyst does rather than the
demanded explanation (SRC-ER-4CH1, er.pdf p 57). Temporal scope: CURRENT —
AUTHORITATIVE.

### PED-033 — Notes-level worked examples pace the same strategy

**Claim:** the notes corpus paces practice through formula scaffolds and stepped
worked examples bound to spec points.
**Evidence:** the moles note presents a formula triangle for moles, mass and
molar mass and then worked examples such as "What is the mass of 0.250 moles of
zinc?" with each step shown (SRC-SME-NOTES-4CH1, 1-5-3-moles-mass-and-rfm.md
lines 55-74). Temporal scope: CURRENT — AUTHORITATIVE.

### PED-034 — Tier-aware practice blocks inside the same banks

**Claim:** practice banks carry tier marking inside the bank — CHEMISTRY ONLY
blocks sit within unit questions rather than in a separate tier-only section.
**Evidence:** a Unit 3 bank marks a bond-energy calculation and a reaction-profile
diagram completion as CHEMISTRY ONLY (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 850, line 861); the salts-dissolving
investigation block likewise opens under an END OF CHEMISTRY ONLY header region
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 852). Temporal
scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-BOOK-4CH1-SB1 (front-matter instrumentation statement,
unit-question banks, strategy hints at line+chunk-id locators) and SRC-ER-4CH1
(2023-06 Paper 1C report pages p 55 and p 57 with session identity preserved via
the pack file path). Supplementary: SRC-SME-NOTES-4CH1 worked-example notes;
SRC-TL-4CH1 Getting Started Guide planning pages and identity-pinned scheme of
work; SRC-SPEC-4CH1 contents page. Bounded excerpts with locators preserved;
caps enforced by the pack builder.

## Limitations / Coverage Gaps

Question banks are evidenced from the bank chunks this pack's window captured;
other units' banks are neither enumerated nor denied. The Progression scale's
internal levels are referenced by the book's own statement but their numeric
bands are not claimed here. OCR-era quirks (stacked skills tags rendered without
spaces; a stray glyph in one mark allocation) are quoted as parsed or
paraphrased, never repaired. The legacy examiner-report entry is present for
identity only; no legacy claim is made. No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-006 (BL-008 pass 6) from this artifact's
evidence pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 binds
every citation to a pack excerpt. Research artifact — evidence-backed, not
canonical educational truth.
