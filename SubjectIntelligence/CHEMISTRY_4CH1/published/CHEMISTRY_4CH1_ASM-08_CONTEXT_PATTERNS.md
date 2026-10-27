---
sib_protocol: SIB-1.0
artifact_id: ASM-08
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

# ASM-08 — Context Patterns

## Purpose

This artifact analyses the contexts in which the 4CH1 papers set their questions, as
parsed in the official exam corpus of record (SRC-QPMS-4CH1): industrial-process
framing, everyday applications, laboratory investigations, materials engineering and
staged-manufacture narratives. Context is the papers' AO2 vehicle — the same core
chemistry probed through changing scenarios — and this artifact catalogues the
context families candidates will meet. Every claim is carried on a bounded,
locator-addressed excerpt from the run's evidence pack. Research artifact; canonical
planes untouched.

## Scope

**Covers:** five observable context families and the way contexts carry application
demands.

**Grounding:** SRC-QPMS-4CH1 (the 2019-06 1C/2C, 2020-01 1C and 2021-01 2C papers of
the pack).

**Out of scope:** archetype anatomy (ASM-03), multi-concept mechanics (ASM-07),
examiner commentary on contexts (EXM family).

## Executive Summary

Four context families recur. Industrial chemistry is the heaviest: ammonia and
ethanol manufacture, nitric-acid production in named stages, aluminium extraction by
electrolysis and zinc galvanising all appear as question frames. Everyday
application contexts (pencils, cutting tools, airships, fire extinguishers) carry
structure-property reasoning. Laboratory-investigation contexts (chromatography,
rates, temperature change) carry the practical strand. And staged narratives —
"manufactured in three stages" — chain several reactions into one question. Across
all families the pattern is constant: the context is new, the chemistry is spec
core; the papers use context to test application, never to test exotic facts.

## Main Analysis

### ASM-043 — Industrial-process contexts with named chemistry

**Claim:** the papers frame questions inside real industrial processes, naming
reagents and catalysts.
**Evidence:** "Hydrogen is used to manufacture ammonia, NH3 Hydrogen is reacted with
nitrogen using an iron catalyst." (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 328-342); "Ethanol is also manufactured by reacting steam with ethene, C2H4" with
the conditions question "State the conditions of temperature and pressure used in
this process." (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 502-516).
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-044 — Everyday-application contexts carry structure-property reasoning

**Claim:** familiar objects frame structure-and-bonding explanations.
**Evidence:** the diamond/graphite uses item — "diamonds are used in cutting tools ●
graphite is used in pencils to make marks on paper" — demands structure-and-bonding
reasoning for each use (SRC-QPMS-4CH1, 2020-01/4CH1-1C/questions.md lines 887-901);
the airship frame opens the hydrogen/helium reasoning chain (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 328-342).
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-045 — Laboratory-investigation contexts carry the practical strand

**Claim:** investigation contexts (chromatography, evaporation, temperature change,
rates) frame data-handling and method questions.
**Evidence:** the chromatography frame "A student uses this apparatus to investigate
the colours in four different inks, A, B, C and D." and the
alcohol-evaporation table investigation .
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-046 — Materials-engineering contexts

**Claim:** extraction and protection of metals frame electrochemistry and reactivity
questions.
**Evidence:** "Aluminium is extracted industrially by the electrolysis of molten
aluminium oxide Al2O3" (SRC-QPMS-4CH1, 2021-01/4CH1-2C/questions.md lines 306-320)
and the coating item "Name the process used to coat iron with zinc." with mark
scheme "galvanising ACCEPT galvanisation" (SRC-QPMS-4CH1, 2020-01/4CH1-1C/questions.md lines 153-167).
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-047 — Staged-manufacture narratives chain reactions

**Claim:** multi-stage narratives present consecutive reactions as one question
frame.
**Evidence:** "Nitric acid (HNO3) is used in the production of fertilisers. Nitric
acid is manufactured in three stages." with Stage 1 ammonia-oxidation chemistry
printed in the stem (SRC-QPMS-4CH1, 2020-01/4CH1-1C/questions.md lines 1094-1108);
the two-stage chloroethene process "Ethene (C2H4) can be converted into
chloroethene (C2H3Cl) in a two-stage process." (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 563-577).
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-048 — The constant: new context, core chemistry

**Claim:** across all context families the tested demand stays on specification-core
application — conditions, properties, equations — rather than contextual trivia.
**Evidence:** the ammonia frame asks for the standard catalyst-rate reasoning
("State why a catalyst is used in this reaction." (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 386-400) with the rate/activation-energy
mark scheme, SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 386-400); the
ethanol frame asks the standard conditions; the polymer frame asks for the polymer
name from the monomer .
Temporal scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-QPMS-4CH1 — the 2019-06 1C/2C, 2020-01 1C and 2021-01 2C
official extractions (bounded line-window excerpts, locators preserved, embedded
mark-scheme text cited verbatim). No ER evidence consumed; no specimen material
cited; supplementary sources not consumed for claims.

## Limitations / Coverage Gaps

The context inventory is observed over four paper files of the pack; additional
context families (e.g. environmental/acid-rain frames) appear in the corpus but were
not excerpted into this pack and are therefore not catalogued here. Context-to-AO
mapping is asserted qualitatively from the stems' demands, not statistically. No
canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-005 (BL-008 pass 5) from the run's evidence
pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 bound all citations
to pack excerpts. Research artifact — evidence-backed, not canonical educational
truth.
