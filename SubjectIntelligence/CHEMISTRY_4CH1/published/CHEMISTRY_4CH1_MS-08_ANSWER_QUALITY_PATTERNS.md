---
sib_protocol: SIB-1.0
artifact_id: MS-08
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

# MS-08 — Answer Quality Patterns

## Purpose

This artifact catalogues what the 4CH1 mark schemes treat as a QUALITY answer, as
parsed in the official exam corpus of record (SRC-QPMS-4CH1): precision of named
quantities, breadth on pick-N tasks, sign and value discipline, justified-option
completeness on MCQs, procedural answers with dependencies and rejections, and
graphical-answer tolerances. Quality is read strictly off the parsed marking text.
Every claim is carried on a bounded, locator-addressed excerpt from the run's
evidence pack. Research artifact; canonical planes untouched.

## Scope

**Covers:** precision; breadth; sign/value discipline; MCQ justification depth;
procedural dependencies and rejections; graphical tolerances.

**Grounding:** SRC-QPMS-4CH1 (the 2019-06 2C/1CR papers of the pack).

**Out of scope:** mark-loss catalogue (MS-05), marking lexicon (MS-07).

## Executive Summary

The mark schemes define answer quality operationally. A quality control-variable
answer names the quantity and its holder ("the volume of liquid/alcohol"); a quality
pick-N answer draws on the full printed pool; a quality calculation carries its sign
and its working, because the scheme caps unsigned and no-working results; a quality
MCQ performance is measured by the scheme's own full rationales for every option; a
quality procedural answer respects printed dependencies (drying depends on washing)
and avoids named rejections; and a quality graph meets half-square plotting tolerance
with ruled best-fit lines. Quality, in short, is exactly what the point structure
pays for — nothing more exotic than that.

## Main Analysis

### MS-043 — Precision: name the quantity and its holder

**Claim:** valid-variable answers name the specific quantity controlled.
**Evidence:** "M1 the volume of liquid/alcohol ALLOW amou..." — the parsed guidance
opens the accepted set with the named quantity (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 130-144).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-044 — Breadth: the printed pool defines the quality ceiling

**Claim:** pick-N answers are judged against the full printed pool, so quality means
range across it.
**Evidence:** "Any two from the following: M1 good conductor of heat/thermal energy
M2 does not react with food/affect flavour of food..." (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 242-256).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-045 — Sign and value discipline on calculations

**Claim:** the schemes enforce sign and working as quality conditions with printed
penalties.
**Evidence:** "M3 If Σ(bonds made) > Σ(bonds broken) final answer must be negative
... -788 with no working scores 3 / (+) 788 scores 2" (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 349-363).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-046 — Justified-option depth on MCQs

**Claim:** the schemes model full option-level justification — every distractor gets
a chemical reason — which is the quality bar for MCQ explanation work.
**Evidence:** "A is incorrect as at 0°C the enzymes would not be active ... D is
incorrect as at 80°C the enzymes would be denatured" around the keyed "C (30 °C) is
correct as it is the most suitable temperature for fermentation" (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 427-441).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-047 — Procedural quality: dependencies and rejections

**Claim:** procedural answers must respect printed dependencies and avoid named
rejections to be credit-worthy.
**Evidence:** the crystal-preparation scheme's "M9 suitable method to dry the
crystals eg using filter paper/using paper towel/in warm oven/in a desiccator
REJECT hot oven or any method of direct heating e.g. Bunsen ... M9 DEP M8" (SRC-QPMS-4CH1, 2019-06/4CH1-1CR/questions.md lines 835-849).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-048 — Graphical answer quality and its tolerances

**Claim:** graph answers carry explicit tolerances (half-square plotting, ruled
lines) and leniency notes.
**Evidence:** "M1 all points plotted correctly to +/– half a square / M2 first best
fit line drawn with a ruler / M3 second best fit line drawn with a ruler ... DO NOT
PENALISE HERE IF LINES DO NOT CROSS" (SRC-QPMS-4CH1, 2019-06/4CH1-1CR/questions.md lines 988-1002).
Temporal scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-QPMS-4CH1 — the 2019-06 2C and 1CR official extractions (15
bounded line-window excerpts across the two files, locators preserved; marking text
cited verbatim). No examiner reports consumed; no specimen material cited;
supplementary sources not consumed for claims.

## Limitations / Coverage Gaps

Quality patterns are anchored on two paper files of the pack; the pattern inventory
is a demonstrated floor rather than a census. Graphical tolerance claims are
anchored on one grid item. No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-005 (BL-008 pass 5) from the run's evidence
pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 bound all citations
to pack excerpts. Research artifact — evidence-backed, not canonical educational
truth.
