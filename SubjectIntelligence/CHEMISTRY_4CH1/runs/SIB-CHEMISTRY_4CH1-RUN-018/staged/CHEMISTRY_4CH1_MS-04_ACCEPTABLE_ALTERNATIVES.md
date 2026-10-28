---
sib_protocol: SIB-1.0
artifact_id: MS-04
artifact_version: 1.1
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
  supplementary: false

status: GENERATED
generated_by: zai_agent
generated_at: 2026-10-29

provenance:
  source_manifest: "SRC-QPMS-4CH1"
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-018"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "2cb92fe5f56d22f1b231c129a7e0dbc27bf86007"
    syllabai_resources: "251b46ba0bd9a08d66d57eca44fc8c80cd283289"
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

**Grounding:** SRC-QPMS-4CH1 (the 2019-06 2C paper of the pack).

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

### MS-058 — Synonym-level allowances at the vocabulary layer

**Claim:** the alternative machinery operates below the phrase level: single words are granted as substitutes (combination for mixture) while a neighbouring cell fences off the chemically wrong vocabulary (compound, or any bonding reference). The allowance and the rejection are adjacent cells of the same point, so the alternative space is defined jointly — what may be swapped, and what may never be. Vocabulary-level tolerance is thus printed, bounded, and as authoritative as the answer itself.
**Evidence:** the alloy-definition point grants "ALLOW combination for mixture" and, in the adjoining cell, "REJECT compound or references to chemical bonding" (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 265-279).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-059 — Reference-scoped allowances: any named instance from a printed set

**Claim:** allowances can be scoped to a reference set rather than enumerated inline: the safety point admits any named alcohol from the question's own table, converting the table into part of the acceptance space. The same point's allowance cell paraphrases the ignition wording (can be easily ignited) while the answer line fixes the chemical fact (flammable). The scope form keeps the scheme compact where the candidate's choice of instance is chemically irrelevant.
**Evidence:** the Bunsen-safety point answers "alcohols/the liquids are flammable/catch fire" with the paraphrase allowance and the scoped extension "ALLOW any named alcohol from the table" (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 145-159).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-060 — Numeric-value allowances on calculated results

**Claim:** alternatives extend to the numbers themselves: a calculation point can print the variants of the accepted value — a rounding neighbour admitted outright — and a band of values earned from a different data route, each priced at its own mark. The mean-time item grants 62.3 beside 62, and the misread-data band 69, 69.25 and 69.3 for one mark. Numeric acceptance is therefore a printed boundary, not marker generosity, and it is priced per route.
**Evidence:** the mean calculation grants "ALLOW 62.3" beside the exact mean and states "62/62.3 with no working scores 2" (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 159-173); the misread-data band prints "ALLOW 69/69.25/69.3 for 1 mark" (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 172-186).
Temporal scope: CURRENT — AUTHORITATIVE.


## Evidence / Source Basis

Primary evidence: SRC-QPMS-4CH1 — the 2019-06 2C official extraction (60 bounded line-window excerpts, locators preserved; mark-scheme text cited verbatim).

## Limitations / Coverage Gaps

The catalogue covers the alternative classes visible in the pack's excerpt windows of the 2019-06 2C paper;
rare allowance forms in other sessions are neither catalogued nor denied. The
halogen-displacement scheme is quoted from consecutive windows of one item; its full
guidance grid extends past the excerpt edges and the unexcerpted remainder is not
paraphrased. No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-005 (BL-008 pass 5) from the run's evidence
pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 bound all citations
to pack excerpts. Deepened under SIB-CHEMISTRY_4CH1-RUN-018 (D3 tranche 2): +3 records (MS-058..060), zero-append mining of the carried RUN-005 pack of record; every quote self-bound to raw excerpt text before the official gate; claim QA re-bound all citations. Research artifact — evidence-backed, not canonical educational truth.
