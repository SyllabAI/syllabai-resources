---
sib_protocol: SIB-1.0
artifact_id: MS-06
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

status: GENERATED
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

# MS-06 — Partial Credit Patterns

## Purpose

This artifact catalogues how the 4CH1 mark schemes award partial credit, as parsed in
the official exam corpus of record (SRC-QPMS-4CH1): step-pair splits, no-working
caps with fallback values, dependency-based one-mark outcomes, pick-N pool awards,
diagram-route equivalence and deduction mechanics. The patterns are read strictly off
the parsed text. Every claim is carried on a bounded, locator-addressed excerpt from
the run's evidence pack. Research artifact; canonical planes untouched.

## Scope

**Covers:** step-pair credit; no-working caps and fallback allowances; dependency
partial credit; pooled pick-N awards; diagram-route equivalence; deduction rules.

**Grounding:** SRC-QPMS-4CH1 (the 2019-06 2C/1CR, 2020-01 2C, 2022-01 1CR, 2022-06
2C, 2023-11 2C and 2025-06 2C excerpt windows of the pack).

**Out of scope:** full mark-loss catalogue (MS-05), marking-language lexicon (MS-07).

## Executive Summary

Partial credit on 4CH1 is engineered, not incidental. Two-mark calculations split
into a method point and a result point; a bare correct answer is capped ("with no
working scores 2") while a wrong-but-defensible value can still earn one mark
(fallback allowances); reasoning points that depend on an earlier point say so
("M2 dep on M1 ... scores 1 mark"); pick-N tasks pool their credit into a single
line; diagram routes can earn the same marks as prose routes; and deduction rules
strip a mark for a named omission. The candidate-facing consequence: visible working
is never wasted, and a defensible wrong answer often banks something.

## Main Analysis

### MS-031 — Step-pair credit on two-mark calculations

**Claim:** two-mark calculations print one point for the method and one for the
result.
**Evidence:** "- **(1)** (64 + 63 + 60) ÷3 / - **(1)** = 62" on the mean-evaporation
item (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 172-186).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-032 — No-working caps with fallback allowances

**Claim:** bare answers are capped by printed no-working notes, while named
fallback values can still earn a reduced award.
**Evidence:** "62/62.3 with no working scores 2 / ALLOW 69/69.25/69.3 for 1 mark"
(SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 172-186); the Rf scheme's "0.66
with no working scores 3" and "M2 0.6615 ACCEPT any number of sig fig / M3 0.66
must be 2 sig fig" (SRC-QPMS-4CH1, 2019-06/4CH1-1CR/questions.md lines 282-296).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-033 — Dependency-based one-mark outcomes

**Claim:** a dependent point that loses its anchor can still score one mark where
the scheme says so.
**Evidence:** "M2 (electrons) can move/can flow/are mobile REJECT cations/atoms move
for both marks / M2 dep on M1 or mention of electrons i.e. 'electrons move' scores 1
mark" (SRC-QPMS-4CH1, 2020-01/4CH1-2C/questions.md lines 220-234).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-034 — Pooled pick-N awards

**Claim:** pick-N tasks print a single pooled point whose value is the count of
acceptable picks.
**Evidence:** "Award 1 mark each for any six of the following: Method 1 M1 polystyrene
(insulator so) reduces/prevents heat loss (to atmosphere) OWTTE..." with its point
line "- **(6)** Award 1 mark each for any six of the following:" (SRC-QPMS-4CH1, 2022-01/4CH1-1CR/questions.md lines 1031-1045).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-035 — Diagram-route equivalence

**Claim:** credit routes through diagrams equal the prose route where the scheme
says so.
**Evidence:** "Both marks can be scored from diagrams showing correct electronic
configurations of the ions." alongside the ion points "- **(1)** magnesium/Mg loses
two electrons/becomes 2.8 / - **(1)** oxygen/O gains two electrons/becomes 2.8"
(SRC-QPMS-4CH1, 2022-06/4CH1-2C/questions.md lines 340-354).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-036 — Deduction mechanics

**Claim:** schemes can deduct a mark for a named omission and penalise broken
alternative methods.
**Evidence:** "Deduct 1 mark if no mention of layers/sheets/rows" on the
alloy-hardness scheme (SRC-QPMS-4CH1, 2023-11/4CH1-2C/questions.md lines 274-288);
the titration scheme's "REJECT incorrect ALTERNATIVE METHOD rounding for 1 mark"
with the printed alternative route (SRC-QPMS-4CH1, 2025-06/4CH1-2C/questions.md lines 550-564).
Temporal scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-QPMS-4CH1 — the run's pack of official extractions (bounded
line-window excerpts across the 2019-2025 sessions listed, locators preserved;
mark-scheme text cited verbatim). No examiner reports consumed; no specimen material
cited; supplementary sources not consumed for claims.

## Limitations / Coverage Gaps

The partial-credit catalogue covers the mechanics visible in the pack's excerpt
windows; several session files in the pack are identity-only (no excerpts matched
the query net) and contribute nothing here. Frequency of each pattern across the
corpus is not measured. No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-005 (BL-008 pass 5) from the run's evidence
pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 bound all citations
to pack excerpts. Research artifact — evidence-backed, not canonical educational
truth.
