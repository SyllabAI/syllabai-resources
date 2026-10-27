---
sib_protocol: SIB-1.0
artifact_id: ASM-07
artifact_version: 1.0
subject: Chemistry
qualification: International GCSE
specification: 4CH1
curriculum_version: "2017"

research_family: assessment_intelligence
applicability: REQUIRED

temporal_scope:
  current: true
  legacy: false

source_scope:
  specification: true
  textbook: false
  question_papers: true
  mark_schemes: true
  examiner_reports: false
  supplementary: true

# lifecycle: GENERATED -> QA_PASSED -> STAGED
status: PUBLISHED
generated_by: zai_agent
generated_at: 2026-10-26

provenance:
  source_manifest: "SRC-QPMS-4CH1"
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

# ASM-07 — Multi-Concept Question Patterns

## Purpose

This artifact analyses how the 4CH1 papers combine multiple concepts inside single
questions, as parsed in the official exam corpus of record (SRC-QPMS-4CH1): shared
stimulus boxes, cross-part consequential marking, investigation chains that blend
technique with explanation, and questions whose parts span specification topics. It
extends the archetype view (ASM-03) with the papers' integration machinery. Every
claim is carried on a bounded, locator-addressed excerpt from the run's evidence
pack. Research artifact; canonical planes untouched.

## Scope

**Covers:** shared-stimulus boxes; cross-part mark dependencies (CSQ chains);
investigation chains; topic-spanning question designs.

**Grounding:** SRC-QPMS-4CH1 (the 2019-06 1C and 2CR papers of the pack).

**Out of scope:** single-concept archetype anatomy (ASM-03), tariff statistics
(ASM-05), examiner commentary (EXM family).

## Executive Summary

The papers integrate concepts through four observable devices. A stimulus box (a list
of gases, a table of metals) feeds several parts that each probe a different concept.
Consequential marking (CSQ) chains a part's marks onto an earlier answer, so an early
error propagates — visibly, by design. Extended investigations weave technique,
observation and explanation into one mark tariff. And question-level designs walk a
concept ladder — from identification to property to mechanism — inside a single
question stem. For revision design the implication is direct: isolated fact drills
under-prepare; concept-connection practice is what the papers actually test.

## Main Analysis

### ASM-037 — Shared stimulus boxes feed concept-switching parts

**Claim:** a single stimulus box can feed a run of parts that each interrogate a
different concept of the same list.
**Evidence:** the 2CR opening question gives "The box gives the names of some gases
in the atmosphere. argon carbon dioxide helium nitrogen oxygen" with the rule "Each
gas may be used once, more than once or not at all." (SRC-QPMS-4CH1, 2019-06/4CH1-2CR/questions.md lines 9-23), then asks identification parts across
noble gases, compounds, abundance and greenhouse chemistry (SRC-QPMS-4CH1, 2019-06/4CH1-2CR/questions.md lines 20-34).
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-038 — Consequential marking chains answers across parts

**Claim:** mark schemes explicitly chain later parts onto earlier answers (CSQ), so
the papers build multi-step dependencies inside one question.
**Evidence:** the precipitate-identity part is marked "silver bromide / LiBr Mark CSQ
on (a) and (b)" in its guidance — the parsed line reads "silver bromide / LiBr Mark
CSQ on (a) and" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 204-218); the
2C concentration calculation carries "Mark CSQ on (b)(ii)" .
**Design reading:** CSQ is candidate-friendly — a wrong early answer can still earn
later method marks — and revision should rehearse recovery, not restart.
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-039 — Investigation chains weave technique, observation and explanation

**Claim:** extended investigations integrate apparatus, data handling and explanation
into one tariffed chain.
**Evidence:** the chromatography investigation runs from setup (the parsed excerpt) through
colour-counting to solubility explanation across its parts .
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-040 — One question, several specification strands

**Claim:** single questions can span distinct specification strands — the flame-test
question combines flame chemistry, precipitation testing and metal-property
reasoning.
**Evidence:** the ion-formula part (the parsed excerpt is followed
by precipitate naming 
and a metal-properties table task (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 221-235).
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-041 — Concept ladders inside a part-set

**Claim:** part-sets climb a concept ladder — from naming a member of a class to
classifying by structure to explaining by properties.
**Evidence:** the gases run moves from "Identify the two noble gases" (SRC-QPMS-4CH1, 2019-06/4CH1-2CR/questions.md lines 9-23) through compound and abundance
identification (SRC-QPMS-4CH1, 2019-06/4CH1-2CR/questions.md lines 20-34) to the
greenhouse classification (SRC-QPMS-4CH1, 2019-06/4CH1-2CR/questions.md lines 46-60), and the wire-cleaning part adds the practical-hygiene concept ("State why the wire should be clean when used in the flame test" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 204-218)
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-042 — Industrial-process contexts as integration frames

**Claim:** processing contexts (crude-oil separation) frame questions that integrate
naming, property and use.
**Evidence:** the crude-oil question opens "The diagram shows crude oil being
separated into different fractions" with "Name the process used to separate crude
oil into different fractions." (SRC-QPMS-4CH1, 2019-06/4CH1-2CR/questions.md lines 130-144).
Temporal scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-QPMS-4CH1 — the 2019-06 1C and 2CR official extractions
(bounded line-window excerpts with line locators preserved, embedded mark-scheme text
cited verbatim). No ER evidence consumed (EXM ground); no specimen material cited;
supplementary sources not consumed for claims.

## Limitations / Coverage Gaps

Integration patterns are observed on two paper files of the pack; the inventory is a
floor, not a census. The CSQ chain on the precipitate part is quoted from its parsed
guidance window, whose trailing text is truncated in the excerpt ("Mark CSQ on (a)
and" — the full continuation sits outside the excerpt window and is not quoted).
Quantitative integration statistics belong to ASM-05/ASM-09 ground. No canonical
planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-005 (BL-008 pass 5) from the run's evidence
pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 bound all citations
to pack excerpts. Research artifact — evidence-backed, not canonical educational
truth.
