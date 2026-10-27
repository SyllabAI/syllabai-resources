---
sib_protocol: SIB-1.0
artifact_id: PRO-02
artifact_version: 1.0
subject: Chemistry
qualification: International GCSE
specification: 4CH1
curriculum_version: "2017"

research_family: problem_solving_intelligence
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
  source_manifest: "SRC-QPMS-4CH1"
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

# PRO-02 — Problem Type to Method Mapping

## Purpose

This artifact maps problem types to their methods of record in 4CH1: the
reacting-mass chain, hydrate-formula determination, titration concentration,
equilibrium-yield explanation, percentage yield, and gas-volume problems — each
with the method the official mark scheme publishes for that type
(SRC-QPMS-4CH1), plus the book's parallel worked mappings (SRC-BOOK-4CH1-SB1)
and the exemplar apparatus that trains the mapping (SRC-TL-4CH1). Claims ride
only on this artifact's own bounded pack excerpts. Canonical planes are
untouched.

## Scope

**Covers:** moles-first reacting-mass chains; mole-ratio hydrate determination;
titration neutralisation calculations; two-point linked equilibrium
explanations; percentage-yield computation; molar-volume gas problems.

**Out of scope:** the framework layer itself (PRO-01) and dead-end analysis
(PRO-05).

## Executive Summary

The problem-type to method mapping is published, not implied: for each recurring
problem type the official mark scheme prints the method as a bullet skeleton.
Reacting-mass problems resolve by the moles-first chain (moles of the known,
then the mass of the target); hydrate-x problems resolve by a mole-ratio
division; titration problems map to the neutralisation calculation; equilibrium
yield questions map to a linked two-point explanation in which even the
Le Chatelier framing earns its own mark; percentage-yield problems map to
actual-over-theoretical; gas-volume problems map to the molar-volume route. The
book teaches the same mappings in prose (interpreting equations in moles,
excess-reagent decisions from the equation), and the exemplars booklet trains
the mapping against real responses.

## Main Analysis

### PRO-008 — Reacting-mass problems map to the moles-first chain

**Claim:** the reacting-mass type maps to the published two-step method: moles
of the given substance, then the mass of the target.
**Evidence:** the methane item's skeleton runs "• calculate moles of methane •
calculate mass of oxygen" with M1 n[CH4] = 32 ÷ 16 and M2 mass of O2 = 128 (g)
(SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 827-842). Temporal scope:
CURRENT — AUTHORITATIVE.

### PRO-009 — Hydrate-x problems map to mole-ratio division

**Claim:** the water-of-crystallisation type maps to a four-step mole-ratio
method, published with its marks.
**Evidence:** the skeleton reads "•calculate moles of (NH4)2SO4.Fe2(SO4)3
•calculate moles of H2O •divide moles of water by moles of" the salt, then give
x to the nearest whole number, with M1-M4 and the OR route attached
(SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 1382-1396, lines
1398-1402). Temporal scope: CURRENT — AUTHORITATIVE.

### PRO-010 — Titration problems map to the neutralisation calculation

**Claim:** concentration-finding titrations map to the volume-concentration
neutralisation method, set up by the printed student method.
**Evidence:** the item opens "A student does a titration to find the
concentration of potassium hydroxide solution." with the method printed
(SRC-QPMS-4CH1, 2023-06/4CH1-2C/questions.md lines 382-396); the calculation
part supplies "15.00 cm3 of sulfuric acid of concentration 0.180 mol / dm3
neutralises 25.0 cm3 of potassium hydroxide solution" (SRC-QPMS-4CH1,
2023-06/4CH1-2C/questions.md lines 447-461). Temporal scope: CURRENT —
AUTHORITATIVE.

### PRO-011 — Equilibrium-yield explanations map to linked two-point reasoning

**Claim:** equilibrium yield questions map to a two-point linked explanation,
with the Le Chatelier framing itself marked.
**Evidence:** the temperature-change scheme reads "An explanation that links the
following two points M1 yield decreases M2 as (forward) reaction is endothermic"
(SRC-QPMS-4CH1, 2023-06/4CH1-2C/questions.md lines 703-723); the pressure
scheme mirrors it with "yield increases" and "as there are fewer moles /
molecules (of gas)" (SRC-QPMS-4CH1, 2023-06/4CH1-2C/questions.md lines
728-743); the Le Chatelier reference appears as a marked element in the scheme
margins (SRC-QPMS-4CH1, 2023-06/4CH1-2C/questions.md lines 717-731).
Temporal scope: CURRENT — AUTHORITATIVE.

### PRO-012 — Percentage-yield problems map to actual-over-theoretical

**Claim:** the yield type maps to computing percentage yield from the actual
and maximum masses, chained from the earlier maximum-mass part.
**Evidence:** the item states "the actual yield of CuSO4.5H2O crystals is 23.92
g. Calculate the percentage yield of CuSO4.5H2O" (SRC-QPMS-4CH1,
2019-06/4CH1-1C/questions.md lines 1298-1312), following the show-that maximum
mass part (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 1274-1288).
Temporal scope: CURRENT — AUTHORITATIVE.

### PRO-013 — Gas-volume problems map to the molar-volume route

**Claim:** gas-volume problems map to the molar-volume method with the data
supplied in the question stem.
**Evidence:** the item asks to "Calculate the volume, in dm3, of methane gas at
rtp needed to produce 6.6 tonnes of hydrogen gas" with the molar volume and
tonne conversion printed in the stem (SRC-QPMS-4CH1,
2023-06/4CH1-2C/questions.md lines 741-755). Temporal scope: CURRENT —
AUTHORITATIVE.

### PRO-014 — The book's prose mappings agree with the published methods

**Claim:** the book teaches the same type-to-method mappings in prose —
theoretical yield computed first, and excess decided by converting both
reagents — matching the mark-scheme skeletons.
**Evidence:** the yield worked example computes the theoretical yield first
before the actual crystal mass is compared (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 224); the excess section frames the
method on the lab reality that "you rarely mix things together in exactly the
right proportions" (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 225); the next worked example
converts 3.2 g of copper against 0.40 mol of acid to decide the excess reagent
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 228); the
exemplars booklet trains the same mappings against real responses
(SRC-TL-4CH1, international-gcse-chemistry-exemplars-commentary.pdf p 3).
Temporal scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-QPMS-4CH1 (2019-06 Paper 1C mark-scheme skeletons with
paper identity preserved via the pack file path) and SRC-BOOK-4CH1-SB1
(prose-mapping chunks at line+chunk-id locators). Supplementary: SRC-TL-4CH1
exemplars-commentary booklet; SRC-SPEC-4CH1 held for context pages. Bounded
excerpts with locators preserved; caps enforced by the pack builder.

## Limitations / Coverage Gaps

The mapping is catalogued for the problem types this pack's windows captured;
further types (for example electrolysis calculations) appear in the run's other
packs and are neither enumerated here nor denied. Mark-scheme skeletons are
cited as published method statements only; the MS family owns the systematic
mark-layer analysis, and no mark_points plane data is consumed or written. No
examiner sentiment is synthesized from mark schemes. OCR-era quirks are quoted
as parsed or paraphrased, never repaired. No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-006 (BL-008 pass 6) from this artifact's
evidence pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 binds
every citation to a pack excerpt. Research artifact — evidence-backed, not
canonical educational truth.
