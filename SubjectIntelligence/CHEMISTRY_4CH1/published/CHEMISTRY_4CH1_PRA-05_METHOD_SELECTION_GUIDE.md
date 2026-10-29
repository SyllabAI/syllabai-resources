---
sib_protocol: SIB-1.0
artifact_id: PRA-05
artifact_version: 1.1
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
generated_at: 2026-10-29

provenance:
  source_manifest: "SRC-SPEC-4CH1"
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-020"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "f39fc0fde3ee12f97efa5c031e16c17c25243fd5"
    syllabai_resources: "923232c73d9ac7dca748b29ccca1c8067ba741aa"
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
The deepened records extend the selection claim into its inner structure: the two designated preparation routes taught as full procedures with their own purity disciplines (an endpoint read from excess solid and a glass-rod saturation test, against a washed-and-dried precipitate), the single cup-calorimetry template generalised across displacement, dissolving and neutralisation with the measured extremum flipping between maximum and minimum, and the sequencing law that puts acid-reaction chemistry — with its reactivity-series violence ceiling — before any salt-preparation method.

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

### PRA-045 — The two preparation routes carry their own endpoint and purity disciplines

**Claim:** the designated preparation procedures are taught with route-specific discipline: the excess-solid route reads its own endpoint and saturation state, while the precipitation route washes and dries the insoluble product clean of everything else.
**Evidence:** the copper(II) sulfate route states its endpoint law — "At this stage, we have added excess copper(Ill) oxide - there is more than enough to react with all the acid present." so "When there is copper(II) oxide left, we know that all the acid has been neutralised." — and its saturation test: "If crystals form on the glass rod when we remove it we know that the solution is very close to saturated" (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 617); the lead(II) sulfate route prices purity in washing terms — "Wash the residue with distilled water by pouring a 20 cm³ portion (the amount is not important) into the filter paper" — and gives the reason: "We must wash the lead(II) sulfate with distilled (pure) water because tap water contains dissolved substances." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 633).
Temporal scope: CURRENT — AUTHORITATIVE.
### PRA-046 — One calorimetry template, many reaction classes

**Claim:** the book generalises a single cup-calorimetry template across reaction classes — displacement, dissolving, neutralisation — reusing the same apparatus pattern while the measured extremum flips with the reaction's heat direction.
**Evidence:** the generalisation is stated once and instantiated repeatedly — "You can use very similar methods for measuring molar enthalpy changes in displacement reactions" (with dissolving and neutralisation named alongside), and the water role is reframed: "These experiments also involve heating water, but this time the water is part of the solutions we are using." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 740); the displacement procedure closes on "Record the maximum temperature reached." while the dissolving procedure closes on "Record the minimum temperature." — the template identical, the extremum inverted (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 742, line 748).
Temporal scope: CURRENT — AUTHORITATIVE.
### PRA-047 — Method selection is sequenced behind prerequisite chemistry

**Claim:** the book orders its practical methods: acid-reaction chemistry — with the reactivity series as both the predictive frame and the violence ceiling — is taught before salt preparation, and the series itself is designated as built from reaction classes.
**Evidence:** the sequencing is explicit — "Before we look at some practical methods to make salts, we need to study the reactions of acids." — and the acid rules are series-indexed: "Metals below hydrogen in the series don't react with dilute acids." while "The higher the metal is in the reactivity series, the more vigorous the reaction." with the safety ceiling "You would never mix metals such as sodium or potassium with acids because their reactions are too violent." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 603); the series is constructed from designated evidence classes — "Understand how metals can be arranged in a reactivity series based on their reactions with:" water, dilute acids and displacement pairs — down to the fixed order from potassium to gold (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 491).
Temporal scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-BOOK-4CH1-SB1 (route-split, method-variant, and bank
chunks at line+chunk-id locators), SRC-SPEC-4CH1 (practical statement pages),
and SRC-TL-4CH1 (core-practicals guide index pages). Supplementary: SRC-QPMS-4CH1
(2019-06 Paper 1C mistake-analysis and demand items with paper identity
preserved via the pack file path). Bounded excerpts with locators preserved;
caps enforced by the pack builder.

## Limitations / Coverage Gaps

This artifact catalogues the method-selection patterns visible in its pack's excerpt windows; selection rules outside the captured pages/lines are neither enumerated nor denied. The RUN-020 deepening added records only from the held pack surface (zero-append tranche): no windows were appended, so selection detail outside the captured surface is neither quoted nor denied. OCR-era quirks of the book parse (the '(Ill)' oxide token, doubled MASH reminder stamps) are quoted as parsed or paraphrased, never repaired. The soluble-salt titration route for sodium/potassium/ammonium salts lies outside this pack's captured windows and is not claimed here. No examiner sentiment is synthesized from mark schemes. No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-006 (BL-008 pass 6) from this artifact's evidence pack alone; deepened under SIB-CHEMISTRY_4CH1-RUN-020 (D3 REQUIRED-core depth pass, tranche 4 — PRA+PED, zero-append) with +3 records (PRA-045..047) authored only from the held pack excerpts, quotes pre-bound under the markup-transparent self-check; validator of record tools/sib @ 357ace0a; claim QA r3 binds every citation to a pack excerpt. Research artifact — evidence-backed, not canonical educational truth.
