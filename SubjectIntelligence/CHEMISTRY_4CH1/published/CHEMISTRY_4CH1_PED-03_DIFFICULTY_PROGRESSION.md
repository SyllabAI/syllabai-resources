---
sib_protocol: SIB-1.0
artifact_id: PED-03
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

# lifecycle: GENERATED -> QA_PASSED -> STAGED
status: PUBLISHED
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

# PED-03 — Difficulty Progression

## Purpose

This artifact analyses how difficulty is staged and signposted across the 4CH1
learning materials of record: the student book's explicit difficulty-graded
headers, extension and scope-fencing devices, tier-marked question material, and
skills tags (SRC-BOOK-4CH1-SB1); the Getting Started Guide's planning framing
(SRC-TL-4CH1); and the specification's own progression and prior-learning
statements (SRC-SPEC-4CH1). Claims ride only on this artifact's own bounded pack
excerpts. Canonical planes are untouched.

## Scope

**Covers:** within-chapter difficulty ladders; beyond-the-basics extension
material; explicit out-of-scope fencing; chemistry-only marking on question
material; skills tags on chapter and unit questions; skills-appendix difficulty
grading; spec-level progression and prior-learning framing.

**Out of scope:** prerequisite linkage (PED-02) and problem-solving method
detail (PRO family).

## Executive Summary

Difficulty progression in the evidence of record is signposted, not silent. The
book stages calculations under graded headers (up to an explicit "very slightly
harder" rung), quarantines stretch material in EXTENSION WORK and named
harder-topic sections, and fences scope with explicit you-won't-be-asked
statements so learners know what difficulty is not theirs to carry. Question
material is marked CHEMISTRY ONLY and tagged with the skill it exercises
(problem solving, reasoning, interpretation), and the maths appendix grades its
own demand (drawing smooth curves is named as harder, with the
significant-figures rule supplied as the guardrail). At spec level, progression
is a design commitment: the qualification states what prior learning it builds
on and names the further study its skills support.

## Main Analysis

### PED-014 — Graded difficulty headers on calculations

**Claim:** the book stages calculation difficulty under explicit graded headers
rather than presenting all demands at one level.
**Evidence:** the concentration section runs a follow-on task headed "A VERY
SLIGHTLY HARDER CALCULATION" that converts the acid volume into dm³ before the
concentration step (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 257); the same chapter had earlier
doubled an equation with a stated KEY POINT reason so the arithmetic stays
traceable (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 219).
Temporal scope: CURRENT — AUTHORITATIVE.

### PED-015 — Named beyond-the-basics sections and EXTENSION WORK

**Claim:** stretch material beyond the core demand is quarantined in named
harder-topic sections and EXTENSION WORK boxes, making the core/extension
boundary visible.
**Evidence:** a dot-and-cross section advances under the header "SOME MORE
DIFFICULT MOLECULES WHERE THE CENTRAL ATOM DOES NOT HAVE 8 ELECTRONS IN ITS
OUTER SHELL" (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line
322); the atomic-structure chapter carries an EXTENSION WORK box on the third
shell's true capacity beyond the examinable model (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 113). Temporal scope: CURRENT —
AUTHORITATIVE.

### PED-016 — Explicit scope-fencing of difficulty

**Claim:** the book fences difficulty explicitly, telling learners which
complexity is outside International GCSE demand, and flags where the taught model
is a deliberate simplification.
**Evidence:** the acids chapter fences nitric acid: "Of the common acids in the
lab, nitric acid has much more complex reactions with metals. You won't be asked
about this at International GCSE" (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 599); the ionic-bonding chapter
labels its sodium-chlorine model "This is a simplification!" before noting the
molecular reality (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 267). Temporal scope: CURRENT —
AUTHORITATIVE.

### PED-017 — Tier marking on question material

**Claim:** chapter question material carries explicit CHEMISTRY ONLY marking so
the tier boundary is visible at the item level, not just in the specification.
**Evidence:** the polymers chapter questions include a task headed "CHEMISTRY
ONLY" asking learners to identify a polymer and draw its repeat-unit structures
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 1055).
Temporal scope: CURRENT — AUTHORITATIVE.

### PED-018 — Skills tags signal demand type on questions

**Claim:** chapter and unit questions are tagged with the skill each exercises —
problem solving, reasoning, interpretation, critical thinking — so demand type
accompanies difficulty.
**Evidence:** a catalytic-cracking question is tagged "PROBLEM SOLVING REASONING"
with the instruction to reason about how the molecule might have split
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 935); unit-level
questions carry stacked tags including "SKILLS CRITICALTHINKING" and "PROBLEM
SOLVING SKILLS INTERPRETATION REASONING" (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 1057). Temporal scope: CURRENT —
AUTHORITATIVE.

### PED-019 — The maths appendix grades its own demand

**Claim:** the book's skills appendix grades graph and number demand explicitly
and supplies the guardrail rule for precision.
**Evidence:** the graphs section states that for curved graphs "it is more
difficult to draw a smooth curve than a straight line" while the line rules stay
the same (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 1094);
the significant-figures section instructs that an answer should not carry more
significant figures than the least precise input (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 1100). Temporal scope: CURRENT —
AUTHORITATIVE.

### PED-020 — Spec-level progression and prior-learning framing

**Claim:** the specification frames difficulty progression at design level: it
states the qualification builds on defined prior learning and names the further
study its skills support.
**Evidence:** the spec's recruitment section states the qualification "builds on
the content, knowledge" and understanding brought by learners, with access and
progression free from barriers (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p 40); the
why-choose section names "skills that will support progression to further study
in chemistry and a range of other subjects" (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p 11). Temporal scope:
CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-BOOK-4CH1-SB1 (graded headers, extension boxes,
scope-fencing KEY POINTs, tier-marked and skills-tagged question chunks, maths
appendix chunks at line+chunk-id locators) and SRC-SPEC-4CH1 (progression,
prior-learning, and why-choose pages at page locators). Supplementary:
SRC-TL-4CH1 Getting Started Guide planning pages and the identity-pinned scheme
of work; SRC-SME-NOTES-4CH1 structured notes; SRC-ER-4CH1 and
SRC-ER-4CH0-LEGACY as identity-presence pages only, consumed for no claim here.
Bounded excerpts with locators preserved; caps enforced by the pack builder.

## Limitations / Coverage Gaps

The difficulty devices catalogued are those visible in this pack's query windows;
other graded headers outside the window are neither enumerated nor denied. The
Getting Started Guide's planning pages remain context only — no intra-week
difficulty claim is made from them. OCR-era quirks of the book parse (for
example a doubled equation explained in a KEY POINT, and stacked skills tags
rendered without spaces) are quoted as parsed or paraphrased, never repaired.
The legacy examiner-report entry is present for identity only; no legacy claim
is made. No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-006 (BL-008 pass 6) from this artifact's
evidence pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 binds
every citation to a pack excerpt. Research artifact — evidence-backed, not
canonical educational truth.
