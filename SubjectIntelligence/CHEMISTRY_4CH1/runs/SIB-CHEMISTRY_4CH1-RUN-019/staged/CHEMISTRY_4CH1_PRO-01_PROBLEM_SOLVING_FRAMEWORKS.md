---
sib_protocol: SIB-1.0
artifact_id: PRO-01
artifact_version: 1.2
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

status: GENERATED
generated_by: zai_agent
generated_at: 2026-10-29

provenance:
  source_manifest: "SRC-SPEC-4CH1"
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-019"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "e4c1960be234beb0406b9218f4fbb2a95b1e3f28"
    syllabai_resources: "e3d648a195a13e3713b4b14a3095518e4a0d24e5"
---

# PRO-01 — Problem-Solving Frameworks

## Purpose

This artifact catalogues the problem-solving frameworks of record for 4CH1: the
assessment-objective frame that weights application and analysis, the command
word taxonomy that fixes what each demand means, the mark-scheme answer
skeletons that publish the solution framework for multi-step problems, the
precision gating and alternative routes built into those skeletons, and the
book's own decision frameworks. Grounding: SRC-SPEC-4CH1, SRC-QPMS-4CH1, SRC-TL-4CH1 and SRC-BOOK-4CH1-SB1. Claims ride only on this artifact's own bounded pack
excerpts. Canonical planes are untouched.

## Scope

**Covers:** assessment objectives and weightings; command-word definitions and
taxonomy maintenance; mark-scheme solution skeletons (moles chains, hydrate-x
determinations); significant-figure gating; alternative scoring routes;
decision rules in the book prose; exemplar-based framework training.

**Out of scope:** problem-type to method mapping detail (PRO-02) and
multi-step reasoning chains (PRO-03).

## Executive Summary

The problem-solving framework of record operates at three layers. At the top,
the assessment objectives split demand three ways — knowledge, application with
analysis and evaluation, and experimental skills — with per-paper weightings.
The command-word taxonomy then pins the meaning of each demand word, and it is
actively maintained (Issue 3 adds "Which" to the taxonomy). At the working
layer, the official mark schemes publish solution skeletons for multi-step
problems as bullet frameworks — calculate moles, calculate mass, divide, give x
to the nearest whole number — with alternative routes (an OR path) and precision
gating (appropriate significant figures) built in. The book supplies its own
decision frameworks, such as the physical-state rule keyed to melting and
boiling points, and the controlled-comparison pattern for investigation design.
The exemplars booklet trains the framework by walking real student responses
through the mark scheme.

## Main Analysis

### PRO-001 — The assessment-objective frame

**Claim:** problem solving is framed by three assessment objectives, with
application/analysis/evaluation carrying as much weight as knowledge.
**Evidence:** the spec's assessment section states "AO1 Knowledge and
understanding of chemistry" at 38-42%, "AO2 Application of knowledge and
understanding, analysis and evaluation of chemistry" at 38-42%, and "AO3
Experimental skills, analysis and evaluation of data and methods in chemistry"
at 19-21%, with the per-paper split tabulated (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p 35). Temporal scope:
CURRENT — AUTHORITATIVE.

### PRO-002 — The command-word taxonomy fixes the demand semantics

**Claim:** each problem-solving demand word has a pinned definition, and the
taxonomy is maintained across issues.
**Evidence:** the command-word appendix defines "Justify Give evidence to
support" and "Show that Verify the statement given in the question." among its
entries (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p 52); the Issue 3 changes
page records "'Which' added to the command word taxonomy" (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p 3). Temporal scope:
CURRENT — AUTHORITATIVE.

### PRO-003 — Mark-scheme answer skeletons publish the solution framework

**Claim:** the official mark schemes expose multi-step solution frameworks as
bullet skeletons with the mark points attached to the framework steps.
**Evidence:** the methane-combustion skeleton reads "• calculate moles of
methane • calculate mass of oxygen" with the example calculation M1 n[CH4] =
32 ÷ 16 and M2 mass of O2 = 128 (g) (SRC-QPMS-4CH1,
2019-06/4CH1-1C/questions.md lines 827-842); the hydrate-x skeleton runs four
steps — "divide moles of water by moles of" the salt, then give x to the nearest
whole number — with M1-M4 attached and an OR route (SRC-QPMS-4CH1,
2019-06/4CH1-1C/questions.md lines 1382-1396). Temporal scope: CURRENT —
AUTHORITATIVE.

### PRO-004 — Precision gating inside the frameworks

**Claim:** the frameworks gate precision explicitly: an answer must be given to
an appropriate number of significant figures as part of the scored route.
**Evidence:** the copper-sulfate skeleton includes "• give the answer to an
appropriate number of" significant figures as a framework step
(SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 1274-1289). Temporal scope:
CURRENT — AUTHORITATIVE.

### PRO-005 — Alternative scoring routes within one framework

**Claim:** the skeletons carry alternative scoring routes so a validly different
execution of the same framework still scores.
**Evidence:** the methane item's scheme closes with an OR branch — the
alternative answer form — scoring the same two marks, with the framework
steps restated beneath ("scores 2 ... calculate moles of methane")
(SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 838-852). Temporal scope:
CURRENT — AUTHORITATIVE.

### PRO-006 — Decision frameworks in the book prose

**Claim:** the book supplies its own reusable decision frameworks for routine
problems and for investigation comparisons.
**Evidence:** the states section gives the phase decision rule — "A substance is
a solid at temperatures below its melting point" and liquid between melting and
boiling (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 33);
the rates section frames the controlled comparison: "We can do the original
experiment again" at a higher temperature while keeping everything else exactly
the same (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 807).
Temporal scope: CURRENT — AUTHORITATIVE.

### PRO-007 — Framework training through exemplars

**Claim:** the exemplars booklet trains the framework by pairing real student
responses with the examining team's mark-scheme application.
**Evidence:** the booklet explains it shows "real student responses to these
questions" and how the examining team follow the mark scheme to demonstrate
mark award (SRC-TL-4CH1, international-gcse-chemistry-exemplars-commentary.pdf
p 3); its first exemplar works a malachite-and-acid rates investigation with the
method steps printed (SRC-TL-4CH1,
international-gcse-chemistry-exemplars-commentary.pdf p 4). Temporal scope:
CURRENT — AUTHORITATIVE.

### PRO-045 — The taxonomy's meta-rows: compound verbs and MCQ commands

**Claim:** the command-word taxonomy carries rows about the taxonomy's own application: a verb-preceding mechanism, where a data-directed verb compounds with a command word — the printed worked row pairs a directive with its gloss — and a dedicated multiple-choice row that pins a distinct command set for objective items. The taxonomy therefore governs not only the demand words themselves but how they compose and where they specialise, which is the difference between reading a definition and parsing a compound demand.
**Evidence:** the verb-preceding row prints "Analyse the data/graph" with the gloss "Examine the data/graph in detail to provide an explanation" (SRC-SPEC-4CH1, Official-Specifications/igcse-chemistry/international-gcse-chemistry-2017-specification.pdf p52); the multiple-choice row prints "What, Why, Which" as the "Direct command words used for multiple-choice questions" (SRC-SPEC-4CH1, Official-Specifications/igcse-chemistry/international-gcse-chemistry-2017-specification.pdf p52).
Temporal scope: CURRENT — AUTHORITATIVE.

### PRO-046 — Printed weighting ranges and their per-component decomposition

**Claim:** the framework publishes its own assessment-objective weightings as ranges rather than point values, and the ranges decompose per component: the whole-qualification bands are printed alongside each paper's own band, so a problem-solving demand can be located inside a quantified frame whose tolerance is explicit. The decomposition is arithmetic in shape — each paper's three bands sum to its total — while each band itself stays a range, so the frame is exact at the boundaries and tolerant inside them.
**Evidence:** the AO table prints "Knowledge and understanding of chemistry" at "38–42%" and "Experimental skills, analysis and evaluation of data and methods in chemistry" at "19–21%" (SRC-SPEC-4CH1, Official-Specifications/igcse-chemistry/international-gcse-chemistry-2017-specification.pdf p35); the per-unit block prints "Chemistry Paper 1" at "23.2–25.7%" for AO1 and closes with "All components will be available for assessment from June 2019" (SRC-SPEC-4CH1, Official-Specifications/igcse-chemistry/international-gcse-chemistry-2017-specification.pdf p35).
Temporal scope: CURRENT — AUTHORITATIVE.

### PRO-047 — Per-item precision envelopes inside one framework

**Claim:** precision gating is set per item, not globally: one multi-step yield calculation floors its final answer at a printed significant-figure count while the successor percentage-yield part explicitly allows any figure count, and both print their stance on the point. A reader of the framework therefore cannot inherit a precision rule from one item to the next; the envelope travels with the item's own mark points.
**Evidence:** the crystal-mass scheme prints "M3 = 29.9 Final answer must" and "be to 3 sig figs" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 1274-1288); the successor part prints "M2 = 80(%)" with "ALLOW any" and "number of sig figs" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 1298-1312).
Temporal scope: CURRENT — AUTHORITATIVE.


## Evidence / Source Basis

Primary evidence: SRC-SPEC-4CH1 (assessment-objective, command-word, and
changes pages at page locators) and SRC-QPMS-4CH1 (2019-06 Paper 1C mark-scheme
skeletons with paper identity preserved via the pack file path).
Supplementary: SRC-TL-4CH1 exemplars-commentary booklet; SRC-BOOK-4CH1-SB1
decision-rule chunks. Bounded excerpts with locators preserved; caps enforced
by the pack builder.

## Limitations / Coverage Gaps

Frameworks are catalogued from this pack's excerpt windows; the full command
word table and further skeletons are neither enumerated nor denied. Mark-scheme
skeletons are cited as published answer frameworks only — no mark_points plane
data is consumed or written, and the MS family owns the systematic mark-layer
analysis. No examiner sentiment is synthesized from mark schemes. OCR-era
quirks are quoted as parsed or paraphrased, never repaired. No canonical planes
were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-006 (BL-008 pass 6) from this artifact's
evidence pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 binds
every citation to a pack excerpt. Deepened under SIB-CHEMISTRY_4CH1-RUN-019 (D3 tranche 3): +3 records (PRO-045..047), zero-append mining of the carried pack of record; every quote self-bound to raw excerpt text before the official gate; claim QA re-bound all citations. Research artifact — evidence-backed, not
canonical educational truth.
