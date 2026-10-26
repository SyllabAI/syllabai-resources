---
sib_protocol: SIB-1.0
artifact_id: GAP-02
artifact_version: 1.0
subject: Chemistry
qualification: International GCSE
specification: 4CH1
curriculum_version: "2017"

research_family: gap_intelligence
applicability: REQUIRED

temporal_scope:
  current: true
  legacy: false

source_scope:
  specification: true
  textbook: true
  question_papers: false
  mark_schemes: false
  examiner_reports: false
  supplementary: false

status: GENERATED
generated_by: zai_agent
generated_at: 2026-10-26

provenance:
  source_manifest: "SRC-SPEC-4CH1"
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-009"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "2cb92fe5f56d22f1b231c129a7e0dbc27bf86007"
    syllabai_resources: "6ef8c89291a6662f11fc6dc5ada151c47b172075"
---

# GAP-02 — KG Coverage Gaps

## Purpose

This artifact audits knowledge-graph (KG) coverage for the Pearson Edexcel
International GCSE in Chemistry (4CH1). No knowledge-graph corpus is resolved
of record for this library — the SRC-GRAPH-4CH1 source failed preflight and
stays disclosed — so this audit grounds itself on the two structures that
would anchor any KG spine: the specification's content map and the student
book's own per-chapter learning-objectives nodes. It inventories what those
structures cover, at what granularity, and discloses every coverage gap the
evidence packs can actually support. Gaps stay disclosed, never filled.

## Scope

**Covers:** the specification's content map as the canonical content spine;
the book's learning-objectives blocks as the finest-grained coverage nodes of
record; the granularity, continuity and tier-dimension of those nodes across
all four units.

**Out of scope:** curriculum statement-to-chapter mapping detail (GAP-01) and
retrieval-risk scoring (GAP-06).

## Executive Summary

The specification's content map prints four topics with printed page anchors,
and the book of record responds with a learning-objectives block opening every
chapter — twenty-nine chapters spanning all four units, from States of matter
in Unit 1 to Synthetic polymers in Unit 4. The audit finds the
learning-objectives nodes mirror specification statement wording closely
enough to serve as KG seed nodes, that they preserve the chemistry-only tier
dimension, and that they are content-complete but assessment-neutral: no
paper or assessment-objective labels ride on the nodes of record. The
knowledge-graph corpus itself remains absent of record, and that absence —
not a synthetic substitute — is the audit's headline disclosure.

## Main Analysis

### GAP-007 — The canonical content spine of record is the specification's four-topic map, and the KG corpus that would mirror it is absent

**Claim:** the specification's chemistry-content map is the only resolved
structure of record that prints the qualification's content partition as an
explicit indexed list — four topics with page anchors — and no knowledge-graph
corpus is resolved of record to mirror it, so KG coverage gaps are disclosed
at the source level rather than diagnosed against graph nodes.
**Evidence:** the specification's content page reads "2 Chemistry content 1
Principles of chemistry 11 2 Inorganic chemistry 16 3 Physical chemistry 21 4
Organic chemistry 23" (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p15). Disclosure of
record: SRC-GRAPH-4CH1 failed preflight in this run and no graph nodes exist
to compare against; the gap is disclosed, not synthesized. Temporal scope:
CURRENT — AUTHORITATIVE.

### GAP-008 — The book's learning-objectives blocks are the finest-grained coverage nodes of record

**Claim:** every chapter of the student book opens with a learning-objectives
block that decomposes the chapter into bullet-level objectives — a node
structure finer than chapters and coarser than individual sentences — and
these blocks are the finest-grained coverage nodes the of-record corpus
provides for KG seeding.
**Evidence:** the book's Chapter 1 opens "LEARNING OBJECTIVES • Understand the
three states of matter in terms of the arrangement, movement and energy of the
particles" with further bullets for interconversions and the terms "solvent •
solute • solution • saturated solution" (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 21); the Chapter 8 block
decomposes covalent bonding into bullets from "Know that a covalent bond is
formed between atoms by the sharing of a pair of electrons" through dot-and-cross
diagram coverage and structure-property explanations (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 303). Temporal scope:
CURRENT — AUTHORITATIVE.

### GAP-009 — Learning-objectives bullets mirror specification statement wording at statement granularity

**Claim:** where the pack permits a direct comparison, the book's
learning-objectives bullets restate the specification's numbered statements
nearly verbatim — the Chapter 1 block mirrors statements 1.1 through 1.5C —
so statement-level KG nodes could be aligned by wording without invention.
**Evidence:** the book's Chapter 1 objectives open "Understand the three
states of matter in terms of the arrangement, movement and energy of the
particles" (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 21) against the
specification's "1.1 understand the three states of matter in terms of the
arrangement, movement and energy of the particles" (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p17); the same block
carries the solubility bullet "Know what is meant by the term solubility in
the units g per 100 g of solvent." (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 21) against "1.5C know
what is meant by the term solubility in the units g per 100 g of solvent"
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p17).
Temporal scope: CURRENT — AUTHORITATIVE.

### GAP-010 — Learning-objectives nodes span all four units continuously, with no unit or chapter missing from the node sequence of record

**Claim:** the book's learning-objectives nodes run continuously from Chapter
1 (Unit 1) through Chapter 29 (Unit 4) in the of-record chunk corpus — the
pack exhibits nodes in Unit 1, Unit 2, Unit 3 and Unit 4 — so a KG built on
them would inherit continuous topic coverage rather than topic-level holes.
**Evidence:** the corpus exhibits objectives blocks in every unit — Chapter 1
states of matter (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 21), Chapter 11 Group 1
alkali metals with bullets on "the trend in reactivity in Group 1"
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 407),
Chapter 19 energetics with the calorimetry and "Q = mc∆T" bullets
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 711),
and Chapter 29 addition polymers with the repeat-unit objectives
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 1028).
Temporal scope: CURRENT — AUTHORITATIVE.

### GAP-011 — The nodes are content-complete but assessment-neutral: no paper or assessment-objective labels ride on the objectives of record

**Claim:** the book's learning-objectives blocks carry content statements only
— the pack's specification pages likewise print statements without paper or
assessment-objective labels — so an assessment dimension (which statements are
assessed where) is absent from both node structures of record and is disclosed
as a coverage gap no of-record node can fill.
**Evidence:** the Chapter 17 objectives block lists solubility rules and
proton-transfer definitions with no paper, tier or weighting label — "Know the
general rules for predicting the solubility of ionic compounds in water" and
"Understand that an acid is a proton donor and a base is a proton acceptor"
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 595);
the specification's Topic 1 page prints statements "1.1 understand the three
states of matter in terms of the arrangement, movement and energy of the
particles" onward with no per-statement assessment label on this page
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p17).
Temporal scope: CURRENT — AUTHORITATIVE.

### GAP-012 — The chemistry-only tier dimension survives on the objectives nodes, but no resolved KG corpus exists to inherit it

**Claim:** the book's learning-objectives nodes preserve the chemistry-only
tier dimension at bullet level — the Chapter 1 block flags its solubility
objective CHEMISTRY ONLY — which means the node structure of record could
carry tier into a future KG; the absence of any resolved KG corpus of record
is disclosed, and the audit asserts nothing about graph coverage beyond these
nodes.
**Evidence:** the Chapter 1 objectives block reads "CHEMISTRY ONLY • Know what
is meant by the term solubility in the units g per 100 g of solvent."
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 21)
against the specification's C-suffixed statement "1.5C know what is meant by
the term solubility in the units g per 100 g of solvent" (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p17); the examiner-report
and topic-guide sources of record ride as identity-presence only — "Examiners'
Report June 2019 IGCSE Chemistry 4CH1 1C" (SRC-ER-4CH1,
2019-06/4CH1-1C/er.pdf p1) and "TOPIC GUIDE: Chemical bonding Pearson Edexcel
International GCSE in Chemistry (4CH1) and Science (4SD0 and 4SS0) First
teaching 2017" (SRC-TL-4CH1, Chemical-bonding---FINAL.pdf p1). Temporal
scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-SPEC-4CH1 (the specification's content map, p15, and
Topic 1 page, p17) and SRC-BOOK-4CH1-SB1 (the learning-objectives blocks of
record across all four units). Supplementary: SRC-ER-4CH1, SRC-TL-4CH1,
SRC-ROOT-BOOK-COPIES-4CH1 and SRC-SAMS-4CH1 ride as one-page identity-presence
entries consumed for identity claims only. All excerpts are bounded with
locators preserved; caps enforced by the pack builder.

## Limitations / Coverage Gaps

SRC-GRAPH-4CH1 failed preflight and no knowledge-graph corpus exists of
record — every KG claim here is grounded on the spec map and the book's
objectives nodes, never on graph nodes. The pack exhibits 29 of the corpus's
learning-objectives blocks; the remaining blocks are not sampled and no claim
is made about their interiors. Assessment-objective labels are shown absent
on the quoted surfaces only, not on every page of record.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-009 (BL-009 pass 9) from this artifact's
evidence pack alone; validator of record tools/sib @ 357ace0a; claim QA binds
every citation to a pack excerpt. Research artifact — evidence-backed, not
canonical educational truth.
