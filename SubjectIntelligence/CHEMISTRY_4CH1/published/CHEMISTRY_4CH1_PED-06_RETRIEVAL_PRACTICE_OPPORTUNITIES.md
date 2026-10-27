---
sib_protocol: SIB-1.0
artifact_id: PED-06
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
  examiner_reports: false
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

# PED-06 — Retrieval Practice Opportunities

## Purpose

This artifact catalogues the retrieval-practice machinery embedded in the 4CH1
materials of record: REMINDER and Remember-hint boxes that force recall of prior
chapters (SRC-BOOK-4CH1-SB1), mnemonic retrieval scaffolds, completion-style
retrieval items in the unit question banks, forward pointers that prime upcoming
retrieval, confusion-flagged re-teaching moments, and the research-informed
strategy guides that repair retrieval where it fails (SRC-TL-4CH1). Claims ride
only on this artifact's own bounded pack excerpts. Canonical planes are untouched.

## Scope

**Covers:** cross-chapter REMINDER boxes with page pointers; Remember-hint
density and exam-scope retrieval relief; letter and word mnemonics;
completion-style bank items; forward-pointer priming; confusion-flagged re-teach;
topic-guide retrieval repair.

**Out of scope:** practice-question structure (PED-05) and prerequisite mapping
(PED-02).

## Executive Summary

Retrieval practice in the evidence of record is built into the page furniture of
the book rather than bolted on. REMINDER boxes send the learner back to named
chapters and pages to re-derive what a later topic assumes; HINT boxes open with
Remember and either restore a fact or deliberately relieve the learner of it when
the exam supplies the value. Mnemonics (PANiC, AN OX RED CAT, MASH) compress
confusable polarities into retrievable strings. Unit banks include
completion-style items that are pure retrieval (supplying the missing periodic-table
terms). Forward pointers prime future retrieval by naming where a thread returns.
Where the book itself flags a point as confusing — hydrogen chloride versus
hydrochloric acid — it stops and re-teaches, and the publisher's topic guides
supply research-informed prompt instruments for exactly such failure points.

## Main Analysis

### PED-035 — REMINDER boxes force cross-chapter recall with pointers

**Claim:** REMINDER boxes are the book's spaced-retrieval device: they name the
earlier chapter (and page) where the assumed knowledge lives and send the learner
back to it.
**Evidence:** the isotopes section prompts "Remember that isotopes are atoms of
the same element, but with different masses" and points to the explaining chapter
and page (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 148);
the Group 1 chapter's hydroxide work tells learners "You might need to remind
yourself why the formula is MOH" via Chapter 7 (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 415). Temporal scope: CURRENT —
AUTHORITATIVE.

### PED-036 — Remember-hints restore — or deliberately relieve — memory load

**Claim:** Remember-hints either restore a needed fact or explicitly relieve the
learner of memorising what the exam will supply, tuning retrieval demand to
assessment reality.
**Evidence:** a relative-atomic-mass hint states "you do not have to calculate
the relative atomic masses" because "they will always be given to you in an exam"
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 154); a
proton-number hint opens "Remember that the number of protons is the same as the
atomic number" (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line
100). Temporal scope: CURRENT — AUTHORITATIVE.

### PED-037 — Mnemonics as compressed retrieval strings

**Claim:** the book compresses confusable electrode and salt polarities into
named mnemonics the learner can retrieve under pressure.
**Evidence:** electrolysis polarity is anchored as "Remember PANiC: positive
anode, negative (is) cathode" (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 356); electrode reaction polarity
offers "A way of remembering this is AN OX RED CAT or AN OILRIG CAT"
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 369); the
metal-plus-acid salt rule closes with "You can remember this using the mnemonic
MASH" (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 523).
Temporal scope: CURRENT — AUTHORITATIVE.

### PED-038 — Point-of-use remember-demands as retrieval triggers

**Claim:** beyond reminder boxes, the book issues explicit remember-demands at
the exact point where the fact is needed — retrieval triggered by use, not by
schedule.
**Evidence:** the formula-writing section states "You will have to remember
this" for the nitrate ion charge before the crossing-over worked example
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 288); the
weighted-average KEY POINT opens "Remember, to work out a weighted average"
with the inputs required (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 150). Temporal scope: CURRENT —
AUTHORITATIVE.

### PED-039 — Forward pointers prime upcoming retrieval

**Claim:** the book primes future retrieval by naming, in advance, where a thread
returns — a spacing signal for the learner's own planning.
**Evidence:** the periodic-table section tells learners that "Chapter 4 deals in
detail with what you need to know" later in the course (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 103); electrolysis announces that
oxidation and reduction return "in Chapter 14" (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 367); the empirical-formula section
notes learners will realise the wider use of examples "in Unit 4" organic
chemistry (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 200).
Temporal scope: CURRENT — AUTHORITATIVE.

### PED-040 — Confusion-flagged re-teaching moments

**Claim:** where material is predictably confusable the book flags the confusion
explicitly and re-teaches the distinction in place.
**Evidence:** the halogens chapter pauses on "This is something that can be
confusing" — hydrogen chloride the gas versus hydrochloric acid in solution
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 440).
Temporal scope: CURRENT — AUTHORITATIVE.

### PED-041 — Topic guides as research-informed retrieval repair

**Claim:** where retrieval routinely fails — bonding being the publisher's named
case — the teaching corpus supplies research-informed prompt instruments rather
than more repetition.
**Evidence:** the bonding guide names the topic as hard because it demands
"abstract, theoretical ideas" applied to macroscopic observations and builds its
strategy on observed learning (SRC-TL-4CH1, Chemical-bonding---FINAL.pdf p 2);
it then routes teachers to the Royal Society of Chemistry prompt-sheet series as
the repair instrument (SRC-TL-4CH1, Chemical-bonding---FINAL.pdf p 3).
Temporal scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-BOOK-4CH1-SB1 (REMINDER/HINT/KEY POINT chunks, unit-bank
completion items at line+chunk-id locators). Supplementary: SRC-TL-4CH1 topic
guides and Getting Started Guide pages with the identity-pinned scheme of work;
SRC-SME-NOTES-4CH1 moles note; SRC-SPEC-4CH1 command-word pages held for context;
SRC-ER-4CH1 and SRC-ER-4CH0-LEGACY as identity-presence pages only, consumed for
no claim here. Bounded excerpts with locators preserved; caps enforced by the
pack builder.

## Limitations / Coverage Gaps

The retrieval devices catalogued are those in this pack's query windows; the
full REMINDER/HINT inventory across all 29 chapters is neither enumerated nor
denied. Mnemonic coverage is limited to the three the window captured. The
scheme of work remains a DOCX identity entry; its internal retrieval
opportunities are not text-claimable here. OCR-era quirks are quoted as parsed or
paraphrased, never repaired. The legacy examiner-report entry is present for
identity only; no legacy claim is made. No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-006 (BL-008 pass 6) from this artifact's
evidence pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 binds
every citation to a pack excerpt. Research artifact — evidence-backed, not
canonical educational truth.
