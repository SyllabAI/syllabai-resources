---
sib_protocol: SIB-1.0
artifact_id: PRA-03
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
  source_manifest: "SRC-TL-4CH1"
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

# PRA-03 — Practical/Experimental Intelligence

## Purpose

This artifact maps the practical-experimental intelligence layer of record for
4CH1: the declared experimental-skills outcomes, the one-question-many-methods
pattern of the investigation corpus, designated versus suggested practicals, the
assessable experimental-skills band, the planner's week-by-week practical
mapping, and the exam face of practical demand of SRC-SPEC-4CH1, SRC-TL-4CH1, SRC-BOOK-4CH1-SB1 and SRC-QPMS-4CH1. Claims ride only on this artifact's own
bounded pack excerpts. Canonical planes are untouched.

## Scope

**Covers:** declared practical-technique aims; in-book experimental-skills
statements; method-variant investigations for one question; two-route formula
determinations; designated and suggested practical investigations; the
experimental-skills band (variables, analysis, communication, reliability); the
course planner's practical mapping; examined practical demand.

**Out of scope:** procedure steps (PRA-01) and technique micro-patterns
(PRA-02).

## Executive Summary

Practical work in 4CH1 is an intelligence system, not a list. The qualification
aims declare practical techniques as acquirable knowledge alongside facts and
concepts, and the book's front matter states the experimental skills learners
must build (solving practical-context problems, devising and planning
investigations). The investigation corpus deliberately teaches method pluralism:
the percentage of oxygen in air is measured with copper, with rusting iron, and
with phosphorus; the formula of a metal oxide is found by combustion and by
reduction. Beyond the designated practicals (marble-chip rates, catalytic
decomposition), the official guide lists suggested investigations — hydrated
salt formulae, percentage-yield preparations, evaporating to dryness — and its
course planner maps sections and spec codes week by week. The exam examines the
same system through describe-the-test, prepare-the-sample, and electrolysis
items.
The deepened records extend the family-level claim into procedure-internal governance: the metal-acid investigation's controlled comparison with its mole-matching fairness law and deliberate excess-acid choice, the solubility gate that decides which salt-preparation method a sample demands, and the quantitative-electrolysis upgrade that turns the qualitative electrolysis box into a current-laddered, repeated, gas-volume measurement.

## Main Analysis

### PRA-014 — Practical techniques are declared aims, not by-products

**Claim:** the qualification aims state practical techniques as acquired
knowledge in their own right, and the book's front matter states the
experimental skills to be built.
**Evidence:** the aims include "acquire knowledge and understanding of chemical
facts, terminology, concepts, principles and practical techniques"
(SRC-TL-4CH1, gstt-int-gcse-chemistry.pdf p 9); the book's skills page carries
an EXPERIMENTAL SKILLS band including solving problems "set in a practical
context" and devising and planning investigations (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 17). Temporal scope: CURRENT —
AUTHORITATIVE.

### PRA-015 — One question, three methods

**Claim:** the investigation corpus teaches method pluralism: the same
measurement question — percentage of oxygen in air — is answered with three
different practical systems.
**Evidence:** "PRACTICAL: USING COPPER" measures the oxygen percentage with
heated copper in a syringe apparatus (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 466); "PRACTICAL: USING THE
RUSTING OF IRON" uses the rust reaction's oxygen uptake
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 471);
"PRACTICAL: USING PHOSPHORUS" uses phosphorus oxide formation
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 476).
Temporal scope: CURRENT — AUTHORITATIVE.

### PRA-016 — Two routes to one goal

**Claim:** formula determination is taught through two contrasting methods —
combustion and reduction — so method choice itself is part of the learning.
**Evidence:** "PRACTICAL: INVESTIGATING THE FORMULA OF A METAL OXIDE BY
COMBUSTION" determines magnesium oxide's formula by burning (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 176); "PRACTICAL: INVESTIGATING
THE FORMULA OF A METAL OXIDE BY REDUCTION" removes oxygen instead, with the
copper(II) oxide-plus-hydrogen equation given (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 185, line 187). Temporal scope:
CURRENT — AUTHORITATIVE.

### PRA-017 — Designated practicals plus suggested investigations

**Claim:** beyond the specification's designated practicals, the official guide
curates suggested investigations that extend the practical repertoire.
**Evidence:** the guide lists "3.15 practical: investigate the effect of
changing the surface area of marble chips" and "3.16 practical: investigate the
effect of different solids on the catalytic decomposition of hydrogen peroxide
solution" followed by a "Suggested practical investigations" section
(SRC-TL-4CH1, gstt-int-gcse-chemistry.pdf p 11); the suggestions include
"Determine the formula of a hydrated salt such as barium chloride or copper
sulfate" by heating, and "Prepare a substance and calculate the % yield, given
the theoretical yield" (SRC-TL-4CH1, gstt-int-gcse-chemistry.pdf p 12).
**Specification Points:** 3.15, 3.16
Temporal scope: CURRENT — AUTHORITATIVE.

### PRA-018 — The assessable experimental-skills band

**Claim:** the experimental-skills band — variables, analysis, communication,
reliability — is stated as an assessable skill set in the official guidance.
**Evidence:** the Getting Started Guide lists the demands: "identify
independent, dependent and control variables", analysing data consistent with
evidence, communicating with technical language, calculations and graphs, and
assessing "the reliability of an" experimental activity (SRC-TL-4CH1,
gstt-int-gcse-chemistry.pdf p 10). Temporal scope: CURRENT — AUTHORITATIVE.

### PRA-019 — The course planner maps practical work week by week

**Claim:** practical delivery is planned at week grain: the planner rows carry
section, topic, and spec-code sets per week, making practical timing
inspectable.
**Evidence:** the planner pages list weekly rows such as "d) The Periodic Table
1.18, 1.19, 1.20, 1.21" and consolidation/assessment weeks, with a stated 2-year
course planner following the specification and scheme of work (SRC-TL-4CH1,
gstt-int-gcse-chemistry.pdf p 21, p 22). Temporal scope: CURRENT —
AUTHORITATIVE.

### PRA-020 — The exam face of practical demand

**Claim:** the official papers examine practical intelligence as describe-the-test,
describe-the-method, and electrolysis-explanation items.
**Evidence:** a water-test item demands "Describe how anhydrous copper(II)
sulfate is used to test for water" (SRC-QPMS-4CH1,
2019-06/4CH1-1C/questions.md lines 868-882); ion testing asks how to show
copper(II) ions are present in a solution and how copper forms at the negative
electrode (SRC-QPMS-4CH1, 2023-06/4CH1-2C/questions.md lines 491-505, lines
516-530); the five-mark crystal-preparation item closes the loop from PRA-01
(SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 1221-1235). Temporal scope:
CURRENT — AUTHORITATIVE.

### PRA-039 — The metal-acid investigation is a controlled comparison with a stated fairness law

**Claim:** the metal-acid procedures run as controlled comparison — four metals against two acids — and the quantitative variant demands mole-matched samples, controlled surface area, and deliberately excess acid so the comparison stays fair.
**Evidence:** the qualitative protocol fixes the comparison frame — "Set up four test-tubes and put about 2 cm³ of dilute hydrochloric acid into each one." — with magnesium, zinc, iron or copper observed and the gas confirmed because "a squeaky pop indicates the presence of hydrogen gas" (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 513); the quantitative variant states the fairness law in-procedure — "It is therefore important that we use the same number of moles in each experiment rather than the same number of grams." — controls surface area because "it will affect the speed at which the heat is given out", and oversupplies the acid by design: "this amount was chosen so that the hydrochloric acid is in excess" (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 517).
Temporal scope: CURRENT — AUTHORITATIVE.
### PRA-040 — Salt-preparation method choice is gated by solubility knowledge

**Claim:** the book makes solubility knowledge the explicit prerequisite gate for salt-preparation method choice, and pairs the two preparation objectives — soluble salt from acid and alkali, insoluble salt from two soluble reactants — with the designated lead(II) sulfate application.
**Evidence:** the gate is stated before any method is taught — "Before we can do this, we need to know which substances are soluble and which are insoluble in water because the method we use depends on this." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 613); the paired objectives are fixed as demands — "Describe an experiment to prepare a pure, dry sample of a soluble salt, starting from an acid and alkali." and "Describe an experiment to prepare a pure, dry sample of an insoluble salt, starting from two soluble reactants." — with "Practical: Prepare a sample of pure, dry lead(II) sulfate" as the designated application (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 597).
Temporal scope: CURRENT — AUTHORITATIVE.
### PRA-041 — Quantitative electrolysis upgrades the qualitative box into a measured investigation

**Claim:** the book extends electrolysis from qualitative observation to a measured current-volume investigation, stating the apparatus deltas, the fixed-duration protocol, the current ladder, and the repeats-for-reliability step inside the procedure itself.
**Evidence:** the framing is explicit — "We can investigate how much product we get in an electrolysis experiment." — and the apparatus additions are named: "we would also have to put a variable resistor and an ammeter into the circuit to allow us to vary and measure the current" (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 390); the protocol is quantified end-to-end — "Stop the timer after 5 minutes and note the final reading on the gas burette." — laddered across currents, "Repeat for currents of 0.4A, 0.6A, 0.8A and 1.0A.", and closed with the reliability step: "Repeat each experiment to get more reliable results." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 390).
Temporal scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-TL-4CH1 (Getting Started Guide aims, skills band,
practical and suggestion pages, planner pages) and SRC-BOOK-4CH1-SB1
(experimental-skills band and method-variant PRACTICAL chunks at line+chunk-id
locators). Supplementary: SRC-SPEC-4CH1 physical-chemistry practical pages;
SRC-QPMS-4CH1 (2019-06 Paper 1C practical-demand items). Bounded excerpts with
locators preserved; caps enforced by the pack builder.

## Limitations / Coverage Gaps

This artifact catalogues the method families and investigation patterns visible in its pack's excerpt windows; methods outside the captured pages/lines are neither enumerated nor denied. The RUN-020 deepening added records only from the held pack surface (zero-append tranche): no windows were appended, so procedure detail outside the captured surface is neither quoted nor denied. OCR-era quirks of the book parse (doubled KEY POINT stamps, garbled step lines such as the truncated stirring/adding steps in the quantitative metal-acid procedure) are quoted as parsed or paraphrased, never repaired. No examiner sentiment is synthesized from mark schemes. No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-006 (BL-008 pass 6) from this artifact's evidence pack alone; deepened under SIB-CHEMISTRY_4CH1-RUN-020 (D3 REQUIRED-core depth pass, tranche 4 — PRA+PED, zero-append) with +3 records (PRA-039..041) authored only from the held pack excerpts, quotes pre-bound under the markup-transparent self-check; validator of record tools/sib @ 357ace0a; claim QA r3 binds every citation to a pack excerpt. Research artifact — evidence-backed, not canonical educational truth.
