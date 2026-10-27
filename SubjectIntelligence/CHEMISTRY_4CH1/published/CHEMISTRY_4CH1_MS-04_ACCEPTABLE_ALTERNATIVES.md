---
sib_protocol: SIB-1.0
artifact_id: MS-04
artifact_version: 1.0
subject: Chemistry
qualification: International GCSE
specification: 4CH1
curriculum_version: "2017"

research_family: mark_scheme_intelligence
applicability: REQUIRED

temporal_scope:
  current: true
  legacy: false

source_scope:
  specification: false
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

# MS-04 — Acceptable Alternatives

## Purpose

This artifact catalogues the acceptable-alternative machinery of the 4CH1 mark
schemes as parsed in the official exam corpus of record (SRC-QPMS-4CH1): the ALLOW
and ACCEPT annotation classes, product-form and reverse-argument alternatives, and
alternative scoring routes. The catalogue is read strictly off the parsed text; no
alternative is invented beyond it. Every claim is carried on a bounded,
locator-addressed excerpt from the run's evidence pack. Research artifact; canonical
planes untouched.

## Scope

**Covers:** ALLOW (permitted variants); ACCEPT (equivalent responses); product-form
alternatives; reverse-argument acceptance; equation-route scoring.

**Grounding:** SRC-QPMS-4CH1 (the 2019-06 2C and 2CR papers of the pack).

**Out of scope:** mark-loss rules (MS-05), the marking-language inventory's full
span (MS-07).

## Executive Summary

The mark schemes encode three everyday alternative classes and two structural ones.
ALLOW grants a permitted variant of the required answer (any shade combination for an
observation); ACCEPT grants an equivalent response (a paraphrased method step);
name/symbol pairs are printed inline (bromine/Br2). Structurally, some points accept
a reverse argument, and some can be scored through a different route entirely (a
product in an equation). The breadth of these allowances is itself a finding: at 1-2
marks the schemes accept presentation freedom, while the chemistry itself stays
fixed.

## Main Analysis

### MS-019 — ALLOW: permitted variants of the required answer

**Claim:** ALLOW grants variants of the same underlying answer, including partial
descriptions.
**Evidence:** "ALLOW black / ALLOW any combination of grey and black eg grey-black"
on the colour-completion task (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 60-74).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-020 — ACCEPT: equivalent responses to method points

**Claim:** ACCEPT admits an equivalent formulation of a method or action point.
**Evidence:** "M1 add chlorine (solution) to potassium bromide ACCEPT mix the two
(solutions) solutions" (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 96-110).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-021 — Observation and product-form alternatives

**Claim:** observation and product statements accept alternative phrasings printed
inline.
**Evidence:** "M2 (solution) turns orange ALLOW any combination of
orange/yellow/brown" (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 96-110);
the parsed excerpt
(SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 98-112).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-022 — Reverse-argument acceptance

**Claim:** some conclusion points explicitly accept the inverse reasoning route.
**Evidence:** "M4 (therefore) chlorine is more reactive (than bromine) ACCEPT
reverse argument" (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 110-124).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-023 — Name/symbol pairs as printed alternatives

**Claim:** chemical names and formulae are printed as interchangeable pairs in both
answers and allowances.
**Evidence:** "bromine/Br2" across the displacement scheme's points (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 116-130); the noble-gas pair "argon and helium
ALLOW Ar and He" on the 2CR atmosphere item .
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-024 — Alternative scoring routes

**Claim:** a point can name a second route by which it may be earned.
**Evidence:** "M3 can be scored by Br2 as a product in an equation" (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 110-124).
Temporal scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-QPMS-4CH1 — the 2019-06 2C and 2CR official extractions
(bounded line-window excerpts, locators preserved; mark-scheme text cited verbatim).
No examiner reports consumed; no specimen material cited; supplementary sources not
consumed for claims.

## Limitations / Coverage Gaps

The catalogue covers the alternative classes visible in the pack's excerpt windows;
rare allowance forms in other sessions are neither catalogued nor denied. The
halogen-displacement scheme is quoted from consecutive windows of one item; its full
guidance grid extends past the excerpt edges and the unexcerpted remainder is not
paraphrased. No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-005 (BL-008 pass 5) from the run's evidence
pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 bound all citations
to pack excerpts. Research artifact — evidence-backed, not canonical educational
truth.
