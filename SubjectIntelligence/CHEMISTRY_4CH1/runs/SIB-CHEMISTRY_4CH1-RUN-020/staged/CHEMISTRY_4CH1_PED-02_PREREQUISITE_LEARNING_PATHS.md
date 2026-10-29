---
sib_protocol: SIB-1.0
artifact_id: PED-02
artifact_version: 1.1
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
generated_at: 2026-10-29

provenance:
  source_manifest: "SRC-TL-4CH1"
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-020"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "f39fc0fde3ee12f97efa5c031e16c17c25243fd5"
    syllabai_resources: "923232c73d9ac7dca748b29ccca1c8067ba741aa"
---

# PED-02 — Prerequisite Learning Paths

## Purpose

This artifact maps the prerequisite-learning paths visible in the pass-6 evidence
of record: the student book's explicit prior-knowledge recall hooks
(SRC-BOOK-4CH1-SB1), the publisher's prerequisite-repair instruments for the
known-difficult topics (SRC-TL-4CH1 topic guides), and the notes corpus's
spec-point-level prerequisite bindings (SRC-SME-NOTES-4CH1). Claims are carried
only on this artifact's own bounded, locator-addressed pack excerpts. Canonical
planes are untouched.

## Scope

**Covers:** in-text "already met / already seen" recall hooks; section-internal
scaffolds that reuse earlier constructions; research-informed prerequisite repair
for bonding and equilibrium; spec-point-level prerequisite mapping in external
notes; the official planning package that frames prerequisite planning.

**Out of scope:** chapter ordering itself (PED-01) and difficulty staging
(PED-03).

## Executive Summary

Prerequisite handling in the evidence of record is explicit rather than implicit:
the book stops to re-anchor prior knowledge with KEY POINT recall hooks ("You
have already met...") and reuses earlier constructions (block diagrams) with a
stated pedagogical rationale. For the two topics the publisher itself flags as
hard, the teaching corpus ships dedicated prerequisite-repair instruments —
prompt-sheet strategies for bonding built on classroom research, and a
rule-application path for equilibrium built on a published critique of how the
topic is usually taught. At finer grain, the validated notes corpus binds each
note to its spec points, making the prerequisite chain checkable at note level.
The deepened records extend the prerequisite-path claim into its literacy and derivation layers: the book's back-matter command-word table that fixes what Explain, Justify and Plot demand before any answer is attempted, the hydroxonium KEY POINT that hangs new content on a named earlier construction, and the notes' molar-mass derivation chain that walks mole, relative atomic mass and the water arithmetic as one connected path.

## Main Analysis

### PED-008 — Explicit prior-knowledge recall hooks in the book prose

**Claim:** the book marks prerequisite re-anchoring explicitly with KEY POINT
recall hooks that name what the learner has met before, rather than assuming it
silently.
**Evidence:** the salts chapter states "You have already met the ammonium" ion
and introduces its water-side counterpart alongside it, telling learners they do
not have to remember the new name (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 637). Temporal scope: CURRENT —
AUTHORITATIVE.

### PED-009 — Section-internal reuse of earlier constructions with stated rationale

**Claim:** later sections explicitly rebuild on constructions met earlier in the
same section, and the book states the pedagogical reason for the reuse.
**Evidence:** the polymers section recalls that "We have already seen one block
diagram at the beginning of this section" and argues the diagram "is a useful way
of learning this because you can use the box to represent any hydrocarbon chain"
before instantiating it with hexane-1,6-dioic acid and ethane-1,2-diol
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 1050).
Temporal scope: CURRENT — AUTHORITATIVE.

### PED-010 — Bonding prerequisite repair built on classroom research

**Claim:** for bonding — a topic the publisher flags as hard because it demands
abstract, theoretical thinking — the teaching corpus ships structured
prerequisite-repair instruments sourced from classroom research.
**Evidence:** the bonding guide names the difficulty ("abstract, theoretical
ideas that require students to develop and apply increasingly sophisticated
ideas") and grounds its approach in observed learning
(SRC-TL-4CH1, Chemical-bonding---FINAL.pdf p 2); it then points teachers to a
Royal Society of Chemistry prompt-sheet series on chemical stability by Keith
Taber as the repair instrument (SRC-TL-4CH1, Chemical-bonding---FINAL.pdf p 3).
Temporal scope: CURRENT — AUTHORITATIVE.

### PED-011 — Equilibrium prerequisite repair via a rule-application path

**Claim:** the equilibrium topic guide rebuilds the topic's conceptual
prerequisites through an explicit teaching strategy grounded in a published
critique, then drills rule application on worked cases.
**Evidence:** the guide opens from the Allsop and George argument that the usual
principle-first treatment is "counterproductive to the understanding of chemical
equilibrium" (SRC-TL-4CH1, Chemical-equilibrium---FINAL.pdf p 2); it then works
rule-based cases such as the methanol manufacture equilibrium at stated pressure
and temperature (SRC-TL-4CH1, Chemical-equilibrium---FINAL.pdf p 3). Temporal
scope: CURRENT — AUTHORITATIVE.

### PED-012 — Spec-point-level prerequisite binding in the notes corpus

**Claim:** the validated notes corpus binds each revision note to the spec points
it serves, so a learner's prerequisite chain can be checked at note grain.
**Evidence:** the moles note binds itself to the spec point "know that the mole
(mol) is the unit for the amount of a substance" with a typed registry id
(SRC-SME-NOTES-4CH1, 1-5-3-moles-mass-and-rfm.md lines 11-25); the same note
binds its calculations section to the amount-of-substance calculation spec point
(SRC-SME-NOTES-4CH1, 1-5-3-moles-mass-and-rfm.md lines 47-61). Temporal scope:
CURRENT — AUTHORITATIVE.

### PED-013 — The official planning package frames prerequisite planning

**Claim:** the board's own support package frames prerequisite planning as part of
course planning, and ties the qualification's design to progression readiness.
**Evidence:** the Getting Started Guide introduces "Our package of support to help
you plan and implement the specification" including a course planner
(SRC-TL-4CH1, gstt-int-gcse-chemistry.pdf p 4); its key-features section states
the changes are designed to "give them skills that will support progression to
further study" (SRC-TL-4CH1, gstt-int-gcse-chemistry.pdf p 5). Temporal scope:
CURRENT — AUTHORITATIVE.

### PED-066 — The back-matter command-word table is the exam-literacy prerequisite layer

**Claim:** the book's apparatus for prerequisites extends to exam literacy: a command-word table defines, before any content is attempted, what the exam's verbs demand of an answer.
**Evidence:** the table fixes the reasoning verbs — "An explanation requires a justification/ exemplification of a point." — and collapses the recall verbs: "All of these command words are really synonyms." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 1073); Justify is anchored to the answer's own chain — "Give evidence to support (either the statement given in the question or an earlier answer)." — and Plot is specified end-to-end: "Produce a graph by marking points accurately on a grid from data that is provided and then draw a line of best fit through these points." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 1073).
Temporal scope: CURRENT — AUTHORITATIVE.
### PED-067 — The prior-knowledge hook carries new content on its back

**Claim:** the book's recall hooks are not mere signposts: the hydroxonium KEY POINT introduces new chemistry by explicit analogy to the already-met ammonium ion, then immediately lowers the memory burden.
**Evidence:** the hook names the prior construction — "You have already met the ammonium (NH4⁺) ion, which is obtained when H⁺ is added to ammonia (NH₃)." — and rides the analogy straight into new content: "The hydroxonium ion is the equivalent ion for water." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 637); the same window then caps the demand: "You do not have to remember the name hydroxonium ion." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 637).
Temporal scope: CURRENT — AUTHORITATIVE.
### PED-068 — The notes derive molar mass from relative masses as one connected chain

**Claim:** the notes teach molar mass not as a definition to memorise but as a derivation chain from relative atomic masses, with the arithmetic instantiated on named substances.
**Evidence:** the definition lands mid-chain — "The mass of 1 mole of a substance is known as the **molar mass**" — and is immediately tied to the counting argument: "If you had 6.02 x 10<sup>23</sup> atoms of carbon in your hand, that number of carbon atoms would have a mass of 12 g" (SRC-SME-NOTES-4CH1, 1-5-3-moles-mass-and-rfm.md lines 33-47); the chain completes as a rule plus a worked instance — "To find the mass of one mole of a compound, we add up the relative atomic masses" so "So one mole of water would have a mass of (2 x 1) + 16 = 18 g" (SRC-SME-NOTES-4CH1, 1-5-3-moles-mass-and-rfm.md lines 39-53).
Temporal scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-BOOK-4CH1-SB1 (recall-hook and section-reuse chunks at
line+chunk-id locators) and SRC-TL-4CH1 (bonding and equilibrium topic guides;
Getting Started Guide pages; the identity-pinned scheme-of-work entry).
Supplementary: SRC-SME-NOTES-4CH1 spec-point-bound notes; SRC-SPEC-4CH1 held for
course-introduction context; SRC-ER-4CH1 and SRC-ER-4CH0-LEGACY present as
identity-presence pages only, consumed for no claim here. Bounded excerpts with
locators preserved; caps enforced by the pack builder.

## Limitations / Coverage Gaps

This artifact catalogues the prerequisite-learning paths visible in its pack's excerpt windows; paths outside the captured pages/lines are neither enumerated nor denied. The RUN-020 deepening added records only from the held pack surface (zero-append tranche): no windows were appended, so path detail outside the captured surface is neither quoted nor denied. Notes prose is quoted as parsed — the markdown hyperlink markup and OCR-truncated link text ('relative atomic mas') are preserved, never repaired. The legacy ER window (2016 4CH0/4SC0 report page) is present in the pack as an identity-presence entry and is not cited by any record. No examiner sentiment is synthesized from mark schemes. No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-006 (BL-008 pass 6) from this artifact's evidence pack alone; deepened under SIB-CHEMISTRY_4CH1-RUN-020 (D3 REQUIRED-core depth pass, tranche 4 — PRA+PED, zero-append) with +3 records (PED-066..068) authored only from the held pack excerpts, quotes pre-bound under the markup-transparent self-check; validator of record tools/sib @ 357ace0a; claim QA r3 binds every citation to a pack excerpt. Research artifact — evidence-backed, not canonical educational truth.
