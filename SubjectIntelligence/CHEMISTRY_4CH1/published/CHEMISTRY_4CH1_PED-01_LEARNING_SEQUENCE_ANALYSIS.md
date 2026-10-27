---
sib_protocol: SIB-1.0
artifact_id: PED-01
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
  specification: false
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
  source_manifest: "SRC-TL-4CH1"
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

# PED-01 — Learning Sequence Analysis

## Purpose

This artifact analyses how learning is sequenced for Edexcel International GCSE
Chemistry (4CH1) as the sequence is actually laid down in the evidence of record:
the four-unit chapter architecture of the validated student-book parse
(SRC-BOOK-4CH1-SB1), the per-chapter learning-objective openers, the official
planning layer (SRC-TL-4CH1), and the spec's own progression statements
(SRC-SPEC-4CH1). Every claim is carried on a bounded, locator-addressed excerpt
from this artifact's own evidence pack; nothing is asserted beyond the packs.
Canonical planes are untouched.

## Scope

**Covers:** the unit/chapter spine and its chapter maps; per-chapter LEARNING
OBJECTIVES openers; the two-part split of the calculations chapter; chemistry-only
strands inside the sequence; the official planning documents and topic-level
teaching guides; externally structured notes that mirror the spec's topic
numbering.

**Out of scope:** prerequisite detail (PED-02), difficulty gradients (PED-03),
and pedagogical strategy inside topics (PED-04).

## Executive Summary

The sequence of record is a four-unit architecture — Principles, Inorganic,
Physical, Organic — each unit opening with a chapter map that lists its chapters
and page anchors. Every chapter then opens with LEARNING OBJECTIVES bullets that
state, before the prose begins, what the chapter must deliver. The sequence is
explicitly staged inside topics as well as between them: the calculations chapter
is split into Part 1 and Part 2 at fixed page anchors, and chemistry-only strands
are interleaved into the unit spine rather than quarantined. At the official
layer, the Getting Started Guide carries a dedicated Planning section and a
scheme of work is held of-record (identity-pinned), while publisher topic guides
supply topic-level teaching sequences. External notes mirror the official topic
numbering and carry spec-point mappings, giving the same sequence a second,
independent structuring.

## Main Analysis

### PED-001 — The four-unit chapter architecture with page-anchored chapter maps

**Claim:** the student book sequences the whole qualification into four units
(Principles, Inorganic, Physical, Organic), each opened by a chapter map listing
its chapters with page anchors.
**Evidence:** the Unit 1 map lists "STATES OF MATTER 3 ELEMENTS, COMPOUNDS AND
MIXTURES 14 ATOMIC STRUCTURE 24 THE PERIODIC TABLE 30" (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 18); the Unit 2 map lists "THE
ALKALI METALS 123 THE HALOGENS 130 GASES IN THE ATMOSPHERE 137 REACTIVITY
SERIES 145" (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line
404); unit divider prose opens Units 3 and 4 (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 709, line 862).
Temporal scope: CURRENT — AUTHORITATIVE.

### PED-002 — Per-chapter learning-objective openers fix the teaching target before prose

**Claim:** each chapter opens with a LEARNING OBJECTIVES block stating the
chapter's assessed outcomes up front, so the sequence is objective-led at chapter
grain.
**Evidence:** the States of Matter opener "LEARNING OBJECTIVES • Understand the
three states of matter in terms of the arrangement, movement and energy of the
particles" (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 21);
the Ionic Bonding opener "LEARNING OBJECTIVES • Understand how ions are formed by
electron loss or gain" (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 264); the same pattern repeats in
the organic chapters (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 976, line 1028).
Temporal scope: CURRENT — AUTHORITATIVE.

### PED-003 — The official planning layer: a dedicated Planning section and a scheme of work of record

**Claim:** the board's own supporting corpus sequences delivery through a Getting
Started Guide whose contents carry a dedicated Planning section, and a scheme of
work is held of-record with pinned identity.
**Evidence:** the Getting Started Guide contents carry a dedicated "Planning" section
navigated from page 21 alongside "Assessment guidance" from page 16
(SRC-TL-4CH1, gstt-int-gcse-chemistry.pdf p 2); the scheme of work is present in
the pack as an identity-pinned entry (SRC-TL-4CH1, identity).
Temporal scope: CURRENT — AUTHORITATIVE.

### PED-004 — Topic-level teaching sequences exist for the known-difficult topics

**Claim:** for the topics the publisher itself flags as difficult, the teaching
corpus carries dedicated topic-level sequence guides rather than leaving sequencing
to the book alone.
**Evidence:** the bonding guide opens "Chemical bonding (and related ideas about
chemical stability/reactivity) is acknowledged as being a 'tricky to teach'
topic" and proceeds to structured teaching prompts (SRC-TL-4CH1,
Chemical-bonding---FINAL.pdf p 2); the equilibrium guide likewise opens from a
dedicated teaching-strategy article and builds rule-based examples (SRC-TL-4CH1,
Chemical-equilibrium---FINAL.pdf p 2, p 3).
Temporal scope: CURRENT — AUTHORITATIVE.

### PED-005 — Intra-chapter staging: the calculations chapter is split into two fixed parts

**Claim:** sequencing is staged below chapter grain: the calculations chapter is
delivered in two parts with fixed page anchors, Part 1 on formulae/equations
basics and Part 2 advancing to mole-based and concentration work.
**Evidence:** the Unit 1 chapter map prints "CHEMICAL FORMULAE, EQUATIONS AND
CALCULATIONS PART 1: 38, PART 2: 64" (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 18); the Part 2 opener's objectives
carry the advanced calculations, including "calculations involving amount of
substance, volume and concentration (in mol/dm³) of solution"
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 235).
Temporal scope: CURRENT — AUTHORITATIVE.

### PED-006 — Structured-bonding and electrolysis chapters are sequenced inside the unit spine

**Claim:** the four bonded-structure and electrolysis chapters are sequenced
inside the Unit 1 flow at fixed map positions (Ionic 75, Covalent 85, Metallic
98, Electrolysis 101) rather than being relegated to an appendix, and the
electrolysis chapter's objectives carry the chemistry-only demands (inert
electrodes, ionic half-equations, oxidation/reduction classification).
**Evidence:** the Unit 1 map prints "IONIC BONDING 75 COVALENT BONDING 85
METALLIC BONDING 98 ELECTROLYSIS 101" (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 18); the electrolysis opener's
objectives include describing electrolysis "using inert electrodes, of molten
compounds" and writing "ionic half-equations representing the reactions at the
electrodes" (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line
354); the metallic-bonding opener sits between them at its mapped position
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 344).
Temporal scope: CURRENT — AUTHORITATIVE.

### PED-007 — External revision notes mirror the official topic numbering as a second structuring

**Claim:** the validated external notes corpus independently reproduces the same
sequence, organised under the spec's own topic numbers (1-1 states of matter,
1-5 calculations), with per-note spec-point mappings.
**Evidence:** the moles note is titled "Moles, Mass & RFM" under the 1-5
chemical-formulae topic and binds itself to spec points with typed ids
(SRC-SME-NOTES-4CH1, 1-5-3-moles-mass-and-rfm.md lines 11-25); the
states-of-matter note closes with a summary properties table for the three states
(SRC-SME-NOTES-4CH1, 1-1-1-the-three-states-of-matter.md lines 30-44).
Temporal scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-TL-4CH1 (Getting Started Guide pages; bonding and
equilibrium topic guides; the identity-pinned scheme of work and course planner
entries) and SRC-BOOK-4CH1-SB1 (the validated v3 parse: chapter maps, unit
dividers, and per-chapter learning-objective chunks at line+chunk-id locators).
Supplementary: SRC-SPEC-4CH1 course-introduction pages; SRC-SME-NOTES-4CH1
structured notes; SRC-ER-4CH1 and SRC-ER-4CH0-LEGACY held in the pack as
identity-presence entries only (single pages) and consumed for no claim here.
All excerpts are bounded with locators preserved; caps enforced by the pack
builder.

## Limitations / Coverage Gaps

The scheme of work and course planner are DOCX/PPTX identity entries in this
pack — their internal week-by-week tables are not text-extractable through the
pack builder, so intra-week sequencing inside those documents is neither claimed
nor denied here. The Unit 3 and Unit 4 chapter-map excerpts surface as divider
prose rather than full page-anchored lists in this pack's query windows, so
unit-3/4 chapter order is asserted only at the level the pack shows. OCR-era
text of the book parse carries parse-era rescue disclosures; anomalous spacing
(e.g. "UNIT1") and a garbled electrolysis-objective window (the molten-compounds
parenthetical) are paraphrased, never repaired into quotes. The unit-1 map
excerpt carries no chemistry-only suffixes, so the chemistry-only designation is
asserted only from the electrolysis objectives' content, not from the map line.
No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-006 (BL-008 pass 6) from this artifact's
evidence pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 binds
every citation to a pack excerpt. Research artifact — evidence-backed, not
canonical educational truth.
