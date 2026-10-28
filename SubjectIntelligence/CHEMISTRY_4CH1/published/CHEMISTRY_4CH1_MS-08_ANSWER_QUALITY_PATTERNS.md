---
sib_protocol: SIB-1.0
artifact_id: MS-08
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

# lifecycle: GENERATED -> QA_PASSED -> STAGED
status: PUBLISHED
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

**Grounding:** SRC-QPMS-4CH1 (the 2019-06 2C/1CR papers of the pack and the 2020-2023 session windows the records cite).

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

### MS-070 — ECF amnesties forgive drafting errors on graph answers

**Claim:** graph-based answers carry printed error-carried-forward amnesties that decouple the chemistry read-off from the drafting: a mis-plotted point can still earn the downstream read-off marks, and an energy-level sketch earns its marks even when the curve is drawn as a straight line. The amnesty is per-item and printed on the point, so the quality judgement is explicitly about the chemistry performed on the graph, not the graph's accuracy.
**Evidence:** the anomalous-result item prints "ALLOW ECF from incorrect plotting" beside its read-off rows (SRC-QPMS-4CH1, 2021-06/4CH1-2C/questions.md lines 335-349); the solubility item states "Mark ECF on (ii), even if a straight line is drawn" (SRC-QPMS-4CH1, 2023-01/4CH1-2C/questions.md lines 238-252).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-071 — Expected-answer windows define the quality band

**Claim:** the schemes print expected answers as ranges with their own award logic — a calculated mass is expected around a printed value, a solubility difference earns its two marks inside a printed numeric window, and a sign-flipped enthalpy banks three marks only with working and two without. The expected window is the quality specification: it tells the candidate what numerical neighbourhood counts as full credit before the exam, and the no-working bands price the shortcut.
**Evidence:** the bond-enthalpy scheme prints "-788 with no working scores 3" against its expected final answer (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 349-363) and caps the wrong sign, "(+) 788 scores 2" in the same window (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 349-363); the graph-read item expects its mass "expected answer around 44 g" (SRC-QPMS-4CH1, 2021-06/4CH1-2C/questions.md lines 335-349); the solubility item prices its window with "If no working shown, score M2 only" (SRC-QPMS-4CH1, 2023-01/4CH1-2C/questions.md lines 238-252).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-072 — Precision is a dedicated mark point

**Claim:** significant-figure discipline is not a style note but a scored point of its own: within one session's papers, the chromatography Rf result and the yield evaluation each reserve their third mark for the printed precision — two significant figures on one, one decimal place on the other — while the preceding points carry the working. The same windows price the shortcut, so the precision point and its no-working band print side by side. Precision is thus separately-awarded answer quality, priceable directly from the parsed point values rather than inferred from rounding habits.
**Evidence:** "M3 answer to 2 sig fig" scores the chromatography result, with "correct answer with no working scores 3" as the band on the same class of answer (SRC-QPMS-4CH1, 2021-01/4CH1-1CR/questions.md lines 134-148); "M3 correct to 1 dp" scores the yield evaluation (SRC-QPMS-4CH1, 2021-01/4CH1-1CR/questions.md lines 1024-1038).
Temporal scope: CURRENT — AUTHORITATIVE.


## Evidence / Source Basis

Primary evidence: SRC-QPMS-4CH1 — the run's pack of official extractions (77 bounded line-window excerpts across the 2019-2023 session files; marking text cited verbatim). No examiner reports consumed; no specimen material cited;

## Limitations / Coverage Gaps

Quality patterns are anchored on the pack's 2019-2023 session windows; the pattern inventory
is a demonstrated floor rather than a census. Graphical tolerance claims are
anchored on one grid item. No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-005 (BL-008 pass 5) from the run's evidence
pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 bound all citations
to pack excerpts. Deepened under SIB-CHEMISTRY_4CH1-RUN-018 (D3 tranche 2): +3 records (MS-070..072), zero-append mining of the carried RUN-005 pack of record; every quote self-bound to raw excerpt text before the official gate; claim QA re-bound all citations. Research artifact — evidence-backed, not canonical educational truth.
