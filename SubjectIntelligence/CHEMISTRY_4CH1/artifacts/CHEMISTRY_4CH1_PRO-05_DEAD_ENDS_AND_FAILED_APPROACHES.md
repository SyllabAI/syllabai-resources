---
sib_protocol: SIB-1.0
artifact_id: PRO-05
artifact_version: 1.0
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
generated_at: 2026-10-26

provenance:
  source_manifest: "SRC-QPMS-4CH1"
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

# PRO-05 — Dead Ends and Failed Approaches

## Purpose

This artifact catalogues the dead ends and failed approaches of record in 4CH1:
the wrong-answer rationales published inside the official mark schemes' multiple
choice keys, the named fatal dead ends that score zero, the IGNORE/REJECT
fences around near-miss wording, the credited failure analyses of practical
work, the Rf dead end the book disarms in advance, and the teaching-side dead
end the publisher's own topic guide dismantles of SRC-QPMS-4CH1, SRC-BOOK-4CH1-SB1 and SRC-TL-4CH1. Claims ride only on this artifact's own bounded pack excerpts.
Canonical planes are untouched.

## Scope

**Covers:** distractor rationales as published dead ends; zero-score traps;
IGNORE/REJECT wording fences; credited practical failure analyses; the
insoluble-dye dead end; the principle-first equilibrium critique.

**Out of scope:** misconception taxonomy (MIS family) and diagnostic teaching
(PED-09).

## Executive Summary

Dead ends in 4CH1 are not left for learners to discover: the mark schemes
publish them. Every multiple-choice key explains why each wrong option is wrong
("A is not correct as the crystal does not condense"), turning the distractor
set into a catalogue of failed approaches. Some dead ends are named as fatal —
mentioning bond-breaking where intermolecular forces are demanded scores zero.
Near-miss wording is fenced with IGNORE and REJECT classes so the boundary
between almost-right and wrong is explicit. Practical failure modes are
credited analysis targets: gas escaping before the bung is replaced, impure
magnesium with an oxide coating. The book disarms one dead end in advance — a
dye that never leaves the pencil line was never soluble in that solvent — and
the publisher's equilibrium guide names the field's own failed approach
(principle-first teaching) and replaces it with rule application.

## Main Analysis

### PRO-027 — Distractor rationales as published dead ends

**Claim:** the official keys explain every wrong option, publishing the dead
end behind each distractor.
**Evidence:** the dissolving key rules out each option in turn — "A is not
correct as the crystal does not condense", with evaporation and melting ruled
out the same way (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 22-36); the
helium key dismisses colour, solubility and smell as "irrelevant" to the
property that matters (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines
343-357). Temporal scope: CURRENT — AUTHORITATIVE.

### PRO-028 — The named fatal dead end

**Claim:** one reasoning dead end is named as fatal: invoking bond-breaking
where intermolecular forces are the demand scores zero.
**Evidence:** the melting-point explanation scheme warns "Any mention of
covalent bonds/ionic bonds/metallic bonds breaking scores 0 out of 2" while
crediting the intermolecular-forces route (SRC-QPMS-4CH1,
2019-06/4CH1-1C/questions.md lines 726-740). Temporal scope: CURRENT —
AUTHORITATIVE.

### PRO-029 — IGNORE and REJECT fences around near-miss wording

**Claim:** near-miss wording is fenced explicitly — tolerated irrelevances are
IGNOREd, named wrong answers are REJECTed.
**Evidence:** the alkene-test scheme requires decolourised, marks "IGNORE
clear", and REJECTs a named wrong observation (SRC-QPMS-4CH1,
2019-06/4CH1-1C/questions.md lines 611-625); the displacement scheme IGNOREs
references to the magnesium disappearing and to heat (SRC-QPMS-4CH1,
2019-06/4CH1-1C/questions.md lines 464-481); the conductivity scheme IGNOREs
the "sea of electrons" phrasing while crediting delocalised electrons able to
flow (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 521-537). Temporal
scope: CURRENT — AUTHORITATIVE.
### PRO-030 — Practical failure modes as credited analysis

**Claim:** failed practical approaches are examined as credited analysis: the
mark scheme names the classic failure modes of a gas-volume investigation.
**Evidence:** the rate-investigation scheme credits "M1 some gas escapes before
the bung is" replaced and "M2 the magnesium is impure/ the magnesium ribbon has
an oxide coating" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines
1076-1093). Temporal scope: CURRENT — AUTHORITATIVE.

### PRO-031 — The Rf dead end disarmed in advance

**Claim:** the book pre-empts the chromatography dead end — a stationary dye
spot — by stating its cause directly.
**Evidence:** the chromatography KEY POINT states "If the dye does not move
from the pencil line during an experiment, then the dye is not at all soluble in
the solvent you are using" (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 77); the Rf caution adds the
solvent-and-paper dependence that invalidates cross-experiment comparison
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 82).
Temporal scope: CURRENT — AUTHORITATIVE.

### PRO-032 — The teaching-side dead end: principle-first equilibrium

**Claim:** the publisher's own topic guide names a field-level failed approach —
teaching equilibrium through Le Chatelier's principle first — and replaces it
with rule application on worked cases.
**Evidence:** the guide opens from the Allsop and George argument that use of
the principle was "counterproductive to the understanding of chemical
equilibrium" (SRC-TL-4CH1, Chemical-equilibrium---FINAL.pdf p 2); its recovery
route works the rules on stated cases such as the methanol-manufacture
equilibrium (SRC-TL-4CH1, Chemical-equilibrium---FINAL.pdf p 3). Temporal
scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-QPMS-4CH1 (2019-06 Paper 1C key rationales, fences, and
failure-mode marks with paper identity preserved via the pack file path) and
SRC-BOOK-4CH1-SB1 (chromatography dead-end chunks at line+chunk-id locators).
Supplementary: SRC-TL-4CH1 equilibrium topic guide. Bounded excerpts with
locators preserved; caps enforced by the pack builder.

## Limitations / Coverage Gaps

Dead ends are catalogued from this pack's excerpt windows; the full fence
inventory across sessions is neither enumerated nor denied. Mark-scheme
rationales are cited as published key statements only; the MS family owns the
systematic mark-layer analysis, and no mark_points plane data is consumed or
written. No examiner sentiment is synthesized from mark schemes. OCR-era quirks
are quoted as parsed or paraphrased, never repaired. No canonical planes were
written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-006 (BL-008 pass 6) from this artifact's
evidence pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 binds
every citation to a pack excerpt. Research artifact — evidence-backed, not
canonical educational truth.
