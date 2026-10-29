---
sib_protocol: SIB-1.0
artifact_id: PED-06
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
  specification: true
  textbook: true
  question_papers: false
  mark_schemes: false
  examiner_reports: false
  supplementary: true

# lifecycle: GENERATED -> QA_PASSED -> STAGED
status: PUBLISHED
generated_by: zai_agent
generated_at: 2026-10-29

provenance:
  source_manifest: "SRC-BOOK-4CH1-SB1"
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
The deepened records extend the retrieval-opportunity claim into summaries, drawing aids, and data provision: the section summary that restates the Group 1 family as a seven-line self-test checklist, the drawing-notation hints that compress the diagram demands (dots versus crosses carrying no physical difference, the carbon-4/hydrogen-1 bonding rule with hydrogens on the outside), and the worked examples that re-supply their own working data so practice lands on the method rather than the lookup.

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

### PED-078 — Section summaries restate the family as a self-test checklist

**Claim:** the book closes its group-chemistry section with a summary that reads as a retrieval checklist — seven stated features the learner can recite and test against.
**Evidence:** the checklist opens on the family and runs from storage to trend: "Group 1 elements:" "are soft with melting points and densities which are very low for metals", "have to be stored out of contact with air or water", "react with water to produce an alkaline solution of the metal hydroxide and hydrogen gas", "increase in reactivity as you go down the group", and "form compounds in which the metal has a 1+ ion" (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 427).
Temporal scope: CURRENT — AUTHORITATIVE.
### PED-079 — Drawing-notation hints compress the diagram retrieval demands

**Claim:** the book pre-empts the notation burdens of diagram work with hints: the dot-and-cross convention is deflated to its real meaning, and the organic drawing rule is compressed into two bond counts plus a placement rule.
**Evidence:** the notation hint removes a false distinction — "there is absolutely no difference between them in reality" — and states what the marks actually carry: "the dots and the crosses simply show that the electrons have come from two different atoms." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 305); the drawing hint compresses the valences — "carbon always forms 4 bonds by sharing 4 electrons, and hydrogen always forms 1 bond by sharing 1 electron." — and fixes the topology: "The hydrogen atoms always go on the outside, never in the middle." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 315).
Temporal scope: CURRENT — AUTHORITATIVE.
### PED-080 — Worked examples re-supply their own working data

**Claim:** the calculation worked examples restate the constants and identities needed at the moment of practice — relative atomic masses, formulae, mole ratios — so the retrieval being exercised is the method, never the lookup.
**Evidence:** the percentage-mass example grants its own data line — "Relative atomic masses: Na = 23, C = 12, O = 16." — before the arithmetic (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 157); the empirical-to-molecular example states the whole task with the mass given — "A compound has the empirical formula CH2. If the relative formula mass is 56, work out the molecular formula." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 201); and the atom-ratio derivation pauses on its own potential confusion — "It is important to remember in this calculation that we are working out how many atoms of copper combine with how many atoms of oxygen" (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 171).
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

This artifact catalogues the retrieval-practice opportunities visible in its pack's excerpt windows; opportunities outside the captured pages/lines are neither enumerated nor denied. The RUN-020 deepening added records only from the held pack surface (zero-append tranche): no windows were appended, so opportunity detail outside the captured surface is neither quoted nor denied. OCR-era quirks of the book parse (the 'divien mn n n s mss' truncation in the atom-ratio window, doubled stamps) are quoted as parsed or paraphrased, never repaired. The bonding topic-guide windows cited by the pre-existing record remain the TL plane of record; no new guide claims were added. No examiner sentiment is synthesized from mark schemes. No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-006 (BL-008 pass 6) from this artifact's evidence pack alone; deepened under SIB-CHEMISTRY_4CH1-RUN-020 (D3 REQUIRED-core depth pass, tranche 4 — PRA+PED, zero-append) with +3 records (PED-078..080) authored only from the held pack excerpts, quotes pre-bound under the markup-transparent self-check; validator of record tools/sib @ 357ace0a; claim QA r3 binds every citation to a pack excerpt. Research artifact — evidence-backed, not canonical educational truth.
