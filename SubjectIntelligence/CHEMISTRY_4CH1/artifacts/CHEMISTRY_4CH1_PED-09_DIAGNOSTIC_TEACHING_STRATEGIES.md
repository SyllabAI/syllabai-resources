---
sib_protocol: SIB-1.0
artifact_id: PED-09
artifact_version: 1.0
subject: Chemistry
qualification: International GCSE
specification: 4CH1
curriculum_version: "2017"

research_family: learning_pedagogy_intelligence
applicability: REQUIRED

temporal_scope:
  current: true
  legacy: false

source_scope:
  specification: true
  textbook: true
  question_papers: false
  mark_schemes: false
  examiner_reports: true
  supplementary: true

status: GENERATED
generated_by: zai_agent
generated_at: 2026-10-26

provenance:
  source_manifest: "SRC-BOOK-4CH1-SB1"
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

# PED-09 — Diagnostic Teaching Strategies

## Purpose

This artifact catalogues the diagnostic-teaching machinery of record for 4CH1:
the book's named common mistakes with their corrective checks, confusable-pair
warnings, exam-wording precision diagnostics (SRC-BOOK-4CH1-SB1), the examiner
reports' verified standing confusions and partial-credit patterns
(SRC-ER-4CH1), and the research-informed diagnosis-and-repair route the
publisher's topic guides model for the hardest topics (SRC-TL-4CH1). Claims
ride only on this artifact's own bounded pack excerpts. Canonical planes are
untouched.

## Scope

**Covers:** named common mistakes with checks; confusable-pair diagnostics;
exam-wording precision warnings; examiner-verified confusions and credit
patterns; research-informed diagnosis-to-route modelling; diagnostic apparatus
(precautions, readings, graphs).

**Out of scope:** misconception taxonomy breadth (MIS family) and calculation
method detail (PRO family).

## Executive Summary

Diagnosis in the evidence of record is proactive: the book names its own
predictable failure points in the learner's voice — a common mistake is
announced before it is made, with the check that catches it attached
(charge-check on half-equations). Confusable pairs are flagged as such
(sulfate/sulfide endings, isomer/isotope, ethane/ethene), and exam-language
precision is policed with explicit bans (write displaces bromine, not bromide;
colourless, not clear; constant, not equal). The examiner reports confirm the
highest-value diagnoses from the marking side — standing confusions between the
two water tests, the recurring branched-polymer drawing difficulty, wrong-term
mark loss — and show partial-credit patterns. The topic guides model the full
diagnostic loop for the hardest topic: name the difficulty, ground it in
research, then route to the repair instrument.

## Main Analysis

### PED-056 — Named common mistakes with corrective checks

**Claim:** the book announces predictable mistakes as mistakes, in the learner's
voice, and attaches the check that catches each one.
**Evidence:** a moles-calculation hint warns that "A common mistake is to
multiply" by the wrong quantity when finding a mass from moles
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 214); the
half-equation hint warns that a common mistake puts "the electrons on the wrong
side" and prescribes the charge check that catches it (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 368). Temporal scope: CURRENT —
AUTHORITATIVE.

### PED-057 — Confusable-pair diagnostics

**Claim:** confusable pairs are flagged as confusable at the point of use, with
the disambiguation rule attached.
**Evidence:** formula writing is diagnosed directly: "Not looking carefully at
word endings is one of the most common mistakes students make" followed by the
sulfate/sulfide warning "CONFUSING ENDINGS! Don't confuse ions such as sulfate
and sulfide" (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line
284, line 286); the organic chapter warns "Don't confuse the word isomer with
isotope" with the distinction restated (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 894); naming precision extends to
single letters — "even one different letter in the name can matter" between
ethane and ethene (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 319); symbol case is diagnosed the
same way — "the first is a capital letter and the second must be lower case"
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 94). Temporal
scope: CURRENT — AUTHORITATIVE.

### PED-058 — Exam-wording precision diagnostics

**Claim:** the book polices exam language explicitly, banning the near-synonym
that loses the mark.
**Evidence:** displacement wording is fixed in advance: "you must write
'chlorine displaces bromine' not 'chlorine displaces bromide'"
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 446); the
bromine-water result bans the wrong adjective — "the final mixture is
colourless and not clear. Do not use the word clear" (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 965); equilibrium wording is
fenced — "the concentrations of the reactants and products at equilibrium are
constant" rather than equal (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 833). Temporal scope: CURRENT —
AUTHORITATIVE.

### PED-059 — Examiner-verified standing confusions and credit patterns

**Claim:** the examiner reports verify which confusions are standing and where
marks concentrate, from the marking side.
**Evidence:** the 2023-06 report records that candidates confuse the two
specified water tests ("The specification contains two tests for water") — one
chemical, one physical (SRC-ER-4CH1, 2023-06/4CH1-1C/er.pdf p 46); it names poly(propene) as
the recurring drawing difficulty because of the side chain
(SRC-ER-4CH1, 2023-06/4CH1-1C/er.pdf p 17); the 2019-06 report shows wrong
terminology costing marks (SRC-ER-4CH1, 2019-06/4CH1-1C/er.pdf p 25) and shows
partial credit earned for a correct colour change on indicator work
(SRC-ER-4CH1, 2019-06/4CH1-1C/er.pdf p 50). Temporal scope: CURRENT —
AUTHORITATIVE.

### PED-060 — Research-informed diagnosis-to-repair route

**Claim:** the publisher's topic guide models the full diagnostic loop for its
hardest topic: name the difficulty, ground it in classroom research, then route
to the repair instrument.
**Evidence:** the bonding guide names bonding as hard because it demands
"abstract, theoretical ideas" and states that "Research has shown that students
commonly" acquire the difficulties (SRC-TL-4CH1, Chemical-bonding---FINAL.pdf
p 2); the guide then moves to the teaching route — introducing specific
molecules and matching bonding types to their atoms (SRC-TL-4CH1,
Chemical-bonding---FINAL.pdf p 8). Temporal scope: CURRENT — AUTHORITATIVE.

### PED-061 — Diagnostic apparatus in the skills appendix

**Claim:** the skills appendix operationalises diagnosis for practical work:
precaution tables, meniscus-reading rules, and graph-construction checks.
**Evidence:** the appendix tabulates other possible precautions with marks
attached (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line
1078); it fixes the reading rule — take the measurement "from the bottom of the
meniscus" (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line
1083); it grounds graph quality in tooling — a very sharp pencil, since "You
can't draw a good graph with a pen" (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 1089). Temporal scope: CURRENT —
AUTHORITATIVE.

### PED-062 — Conceptual diagnosis where the taught principle misleads

**Claim:** where the taught heuristic itself misleads — equilibrium colour
predictions, catalyst language — the book diagnoses the overreach, and the
equilibrium guide rebuilds the topic on rule application.
**Evidence:** the equilibrium chapter warns "Warning! You have to be very
careful here about predicting exactly what colour changes you would see"
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 841) and pins
the catalyst's role to the minimum-energy idea — not all collisions succeed
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 815); the
topic guide rebuilds equilibrium teaching after the published critique that the
principle-first treatment is counterproductive (SRC-TL-4CH1,
Chemical-equilibrium---FINAL.pdf p 2). Temporal scope: CURRENT —
AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-BOOK-4CH1-SB1 (warning, hint, and appendix chunks at
line+chunk-id locators) and SRC-ER-4CH1 (2019-06 and 2023-06 Paper 1C report
pages with session identity preserved via the pack file paths). Supplementary:
SRC-TL-4CH1 bonding/equilibrium topic guides and practical-terminology guidance;
SRC-SPEC-4CH1 command-word pages; SRC-SME-NOTES-4CH1 separation note.
Bounded excerpts with locators preserved; caps enforced by the pack builder.

## Limitations / Coverage Gaps

Diagnostics are catalogued from this pack's query windows; the full warning
inventory across all chapters is neither enumerated nor denied. Examiner
sentiment is cited only from the report pages in this pack, with session
identity carried by the pack file paths; no examiner sentiment is synthesized
from mark schemes. OCR-era quirks (a doubled KEY POINT stamp, garbled
parentheticals) are quoted as parsed or paraphrased, never repaired. The legacy
examiner-report entry is present for identity only; no legacy claim is made. No
canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-006 (BL-008 pass 6) from this artifact's
evidence pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 binds
every citation to a pack excerpt. Research artifact — evidence-backed, not
canonical educational truth.
