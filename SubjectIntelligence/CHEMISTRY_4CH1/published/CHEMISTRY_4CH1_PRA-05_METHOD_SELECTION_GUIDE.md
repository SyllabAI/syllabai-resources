---
sib_protocol: SIB-1.0
artifact_id: PRA-05
artifact_version: 1.0
subject: Chemistry
qualification: International GCSE
specification: 4CH1
curriculum_version: "2017"

research_family: practical_procedural_intelligence
applicability: REQUIRED

temporal_scope:
  current: true
  legacy: false

source_scope:
  specification: true
  textbook: true
  question_papers: true
  mark_schemes: true
  examiner_reports: false
  supplementary: false

# lifecycle: GENERATED -> QA_PASSED -> STAGED
status: PUBLISHED
generated_by: zai_agent
generated_at: 2026-10-26

provenance:
  source_manifest: "SRC-SPEC-4CH1"
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

# PRA-05 — Method Selection Guide

## Purpose

This artifact builds the method-selection guide for 4CH1 practical work from the
evidence of record: how the materials teach choosing between methods — route
split by solubility class for salt preparation, method pluralism for one
measurement question, apparatus-role variants — and how selection competence is
diagnosed on the exam face through mistake-analysis items — for sources SRC-BOOK-4CH1-SB1, SRC-SPEC-4CH1, SRC-TL-4CH1 and
SRC-QPMS-4CH1. Claims ride only on this artifact's
own bounded pack excerpts. Canonical planes are untouched.

## Scope

**Covers:** solubility-class route selection for salt preparation; method
variants for one question; the official core-practical index as the selection
menu; specification statements that demand described methods; mistake-analysis
items as selection assessment.

**Out of scope:** procedure steps (PRA-01) and technique micro-patterns
(PRA-02).

## Executive Summary

Method selection in the evidence of record is rule-based, not taste-based. Salt
preparation is the canonical case: before methods are taught, the book insists
on knowing which substances are involved, and the route then follows the
solubility class — excess solid plus acid with filtration for soluble salts,
double decomposition with a precipitate for insoluble ones. For measurement
questions the materials deliberately present competing methods (three ways to
measure oxygen in air; two ways to find a metal oxide's formula), making
selection an explicit object of study. The official core-practicals guide is the
selection menu — every procedure indexed to its spec code — and the
specification demands described methods as statements. On the exam face,
selection competence is assessed by mistake-analysis: explaining what a student
did wrong when setting up an investigation.

## Main Analysis

### PRA-027 — Salt-preparation routes follow the solubility class

**Claim:** the book gates salt-preparation method choice on a stated prior
question — which substances are involved — and the route then follows the
solubility class.
**Evidence:** the salt-preparations section announces the gate: "In the next
sections we will learn about some practical methods to make salts. Before we
can do this, we need to know which substanc"es are involved
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 613); the
soluble-salt route runs excess solid plus acid, then filtration of the excess
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 617); the
insoluble-salt route mixes two solutions so a precipitate forms
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 633).
Temporal scope: CURRENT — AUTHORITATIVE.

### PRA-028 — Competing methods taught side by side

**Claim:** for one measurement question the materials present competing methods
as peers, making method choice an explicit learning object.
**Evidence:** the oxygen-percentage question is answered by "PRACTICAL: USING
COPPER", "PRACTICAL: USING THE RUSTING OF IRON" and "PRACTICAL: USING
PHOSPHORUS" in sequence (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 466, line 471, line 476); the
metal-oxide formula is found "BY COMBUSTION" and "BY REDUCTION" as named
alternatives (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line
176, line 185). Temporal scope: CURRENT — AUTHORITATIVE.

### PRA-029 — The official guide is the selection menu

**Claim:** the core-practicals guide functions as the method-selection menu: it
counts each science's core practicals and indexes every procedure to its
specification code.
**Evidence:** the guide's sections open by counting the core practicals per
science — "There are 9 core practicals in the biolog"y section shown — with the
contents listing the practicals chapters (SRC-TL-4CH1,
biology-chemistry-physics-core-practical-guide.pdf p 6, p 3); chemistry-side
entries bind procedures to codes such as the chromatography core practical at
1.13 (SRC-TL-4CH1, biology-chemistry-physics-core-practical-guide.pdf p 75).
**Specification Points:** 1.13
Temporal scope: CURRENT — AUTHORITATIVE.

### PRA-030 — The specification demands described methods

**Claim:** method-selection competence is specification content: statements
demand described experiments, so a chosen method must be articulable, not just
executable.
**Evidence:** the rates statement demands describing experiments across surface
area, concentration, temperature and catalyst changes, as the guide's rates
pages print it (SRC-TL-4CH1,
biology-chemistry-physics-core-practical-guide.pdf p 128); the acids section
designates the metals reaction as a practical statement (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p 24); the book's
chemistry-only items mirror the demand — "Describe an experiment to prepare a
pure, dry sample of a soluble salt, starting from an acid and alkali"
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 597).
**Specification Points:** 3.9, 2.21
Temporal scope: CURRENT — AUTHORITATIVE.

### PRA-031 — Selection competence assessed by mistake analysis

**Claim:** the exam assesses method selection by asking candidates to diagnose a
flawed setup — the selection rules applied in reverse.
**Evidence:** the chromatography investigation item presents a student's four-ink
setup and demands "Explain two mistakes the student made when setting up his
experiment" at the start of an eight-mark question (SRC-QPMS-4CH1,
2019-06/4CH1-1C/questions.md lines 241-263). Temporal scope: CURRENT —
AUTHORITATIVE.

### PRA-032 — Quantitative-versus-qualitative method selection

**Claim:** selection extends to the quantitative/qualitative decision itself:
the same apparatus supports an observational investigation or a measured one,
and the book marks the upgrade explicitly.
**Evidence:** the electrolysis chapter follows its qualitative aqueous-solutions
investigation with "PRACTICAL: QUANTITATIVE ELECTROLYSIS" opening
"Quantitative means related to numbers" and investigating how much product is
obtained (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 390).
Temporal scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-BOOK-4CH1-SB1 (route-split, method-variant, and bank
chunks at line+chunk-id locators), SRC-SPEC-4CH1 (practical statement pages),
and SRC-TL-4CH1 (core-practicals guide index pages). Supplementary: SRC-QPMS-4CH1
(2019-06 Paper 1C mistake-analysis and demand items with paper identity
preserved via the pack file path). Bounded excerpts with locators preserved;
caps enforced by the pack builder.

## Limitations / Coverage Gaps

The selection rules catalogued are those visible in this pack's excerpt windows;
further variant families outside the windows are neither enumerated nor denied.
The core-practicals guide's chemistry-section roster is cited through its index
pages and one chemistry entry; the full chemistry roster is indexed in the
library's curriculum registry and consumed family-wide. OCR-era quirks are
quoted as parsed or paraphrased, never repaired. No examiner sentiment is
synthesized from mark schemes. No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-006 (BL-008 pass 6) from this artifact's
evidence pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 binds
every citation to a pack excerpt. Research artifact — evidence-backed, not
canonical educational truth.
