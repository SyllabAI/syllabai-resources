---
sib_protocol: SIB-1.0
artifact_id: MS-02
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

# MS-02 — Mark Point Taxonomy

## Purpose

This artifact catalogues the mark-point forms of the 4CH1 mark schemes as parsed in
the official exam corpus of record (SRC-QPMS-4CH1): the "- **(N)**" point lines, the
M1/M2 labels, the pooled per-correct allocations and the point-level conditions that
govern credit. The taxonomy is read strictly off the parsed text — the family law
forbids mark-point inventiveness beyond it — and this artifact writes nothing to any
canonical mark_points plane. Every claim is carried on a bounded, locator-addressed
excerpt from the run's evidence pack. Research artifact.

## Scope

**Covers:** single and pooled point lines; per-point annotations (IGNORE/ALLOW);
step-point chains on calculations; the M1/M2 encoding; point-level dependency and
consequentiality conditions.

**Grounding:** SRC-QPMS-4CH1 (the 2019-06 2C paper of the pack).

**Out of scope:** required-answer elements (MS-03), alternatives breadth (MS-04),
mark-loss semantics (MS-05).

## Executive Summary

The parsed mark schemes encode marks in two coordinated notations: bracketed point
lines ("- **(1)**", "- **(2)**", "- **(3)**") that state what each mark is for, and
M1/M2 labels inside the guidance that name the same points for humans. Points
split cleanly: independent facts each get their own (1) line with per-point
annotations (IGNORE/ALLOW); calculations get step-points with no-working penalties;
table/grid tasks get pooled lines ("1 mark for each correct"). Point-level
conditions — dependency and consequential marking — are printed on the point lines
themselves, so the whole credit structure of an item is machine-readable from the
parsed corpus.

## Main Analysis

### MS-007 — The bracketed point-line inventory

**Claim:** mark points print as bracketed lines "- **(N)**" with N = 1..3 observed,
stating the credit each carries.
**Evidence:** "- **(1)** 13" on the mass-number item (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 19-33); "- **(2)** ALLOW black" on the
colour-completion task (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 64-78);
"- **(3)** 1 mark for each correct" on the opening grid task (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 19-33).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-008 — Independent facts split into annotated points

**Claim:** multi-fact answers split into one point per fact, each with its own
annotation.
**Evidence:** the isotopes sentence completion prints "- **(1)** protons IGNORE
electrons" and "- **(1)** neutrons" (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 43-57), with the M1/M2 labels of the same points in the guidance rows
(SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 30-44).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-009 — Step-points on calculations with no-working rules

**Claim:** calculation marks are step-points — each printed with its working — and
bare answers are capped by no-working notes on the point line.
**Evidence:** the RAM calculation's three points: "- **(1)** (35 × 77.78) + (37 ×
22.22)", "- **(1)** 3544.44 ÷ 100 OR 35.4444 OR M1 ÷ 100" and "- **(1)** 35.4 35.4
with no working scores" (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 84-98).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-010 — Pooled marks for grid and table tasks

**Claim:** table/grid tasks print a single pooled point line whose credit is defined
per correct cell rather than per named answer.
**Evidence:** "- **(3)** 1 mark for each correct" (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 19-33) and the pooled colour-allowance line "-
**(2)** ALLOW black" (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 64-78).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-011 — The M1/M2 encoding of the same points

**Claim:** the guidance rows label points M1/M2 while the point lines print them as
(N) — two encodings of one taxonomy, both present in the parsed text.
**Evidence:** "M1 protons IGNORE electrons / M2 neutrons" in guidance (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 30-44) against "- **(1)** protons IGNORE
electrons / - **(1)** neutrons" in points (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 43-57).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-012 — Point-level conditions on credit

**Claim:** conditions attach at point level — no-working caps and
consequential-marking notes ride on the point lines.
**Evidence:** the RAM scheme's "35.4 with no working scores" cap (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 84-98); the halogen-displacement scheme's
incorrect-answer guard ("incorrect M2" in the same excerpt window, SRC-QPMS-4CH1,
2019-06/4CH1-2C/questions.md lines 84-98).
Temporal scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-QPMS-4CH1 — the 2019-06 2C official extraction (60 bounded
line-window excerpts, locators preserved; mark-scheme text cited verbatim from the
corpus of record). No examiner reports consumed; no specimen material cited;
supplementary sources not consumed for claims.

## Limitations / Coverage Gaps

The taxonomy covers the point forms visible in the pack's excerpts of one 2C paper;
rare forms in other sessions are neither catalogued nor denied. The artifact makes
no claim about the visual mark-scheme grids of the original PDFs beyond what the
parse preserves. No canonical mark_points plane was read or written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-005 (BL-008 pass 5) from the run's evidence
pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 bound all citations
to pack excerpts. Research artifact — evidence-backed, not canonical educational
truth.
