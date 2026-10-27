---
sib_protocol: SIB-1.0
artifact_id: TUT-01
artifact_version: 1.0
subject: Chemistry
qualification: International GCSE
specification: 4CH1
curriculum_version: "2017"

research_family: tutor_intelligence
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

# lifecycle: GENERATED -> QA_PASSED -> STAGED
status: PUBLISHED
generated_by: zai_agent
generated_at: 2026-10-26

provenance:
  source_manifest: "SRC-BOOK-4CH1-SB1"
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-008"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "2cb92fe5f56d22f1b231c129a7e0dbc27bf86007"
    syllabai_resources: "7ff30654d9a256bab02b9371b658ad9b9e589959"
---

# TUT-01 — Subject Tutor Knowledge Base

## Purpose

This artifact defines the knowledge backbone a tutor needs when supporting the
Pearson Edexcel International GCSE in Chemistry (4CH1): how the validated
student book of record organizes the qualification's content, which definitions
anchor the course, and what the two examination papers demand. Every claim is
carried on a bounded, locator-addressed excerpt from this artifact's own
evidence pack; nothing is asserted beyond the packs. Canonical planes are
untouched.

## Scope

**Covers:** the book's four-unit architecture and its appendix infrastructure;
the glossary's definitional spine; key-point treatments of bonding,
energetics and rates; and the current specification's paper model.

**Out of scope:** question patterns (TUT-02, TUT-03), hint strategy detail
(TUT-05), and misconception handling (TUT-06).

## Executive Summary

The student book of record organizes 4CH1 into four units — Principles of
Chemistry, Inorganic Chemistry, Physical Chemistry and Organic Chemistry —
mirroring the specification's four topics, and closes the book with a command-word
appendix, a practical-questions guide and a glossary. A tutor working from this
spine can anchor explanations on the book's own key points, which state the
course's central ideas in teachable form, and can map every lesson onto the
two-paper assessment model the specification defines: Paper 1C at 110 marks and
Paper 2C at 70 marks, 180 in total.

## Main Analysis

### TUT-001 — The book's knowledge architecture is a four-unit spine matching the specification's four topics

**Claim:** the validated student book structures the qualification as four
units — Unit 1: Principles of Chemistry (book page 2), Unit 2: Inorganic
Chemistry (page 122), Unit 3: Physical Chemistry (page 206) and Unit 4: Organic
Chemistry (page 254) — with appendices for the periodic table, command words and
practical questions, plus a glossary; this matches the specification's own
chemistry-content map of four numbered topics.
**Evidence:** the book's course-structure table lists "UNIT 1: PRINCIPLES OF
CHEMISTRY", "UNIT 2: INORGANIC CHEMISTRY", "UNIT 3: PHYSICAL CHEMISTRY" and
"UNIT 4: ORGANIC CHEMISTRY" with "APPENDIX B: COMMAND WORDS" and
"APPENDIX C: A GUIDE TO PRACTICAL QUESTIONS" before the glossary and index
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 8); the
specification's chemistry-content page lists "1 Principles of chemistry 11 2
Inorganic chemistry 16 3 Physical chemistry 21 4 Organic chemistry 23"
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p15).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-002 — The glossary anchors the course's working definitions in one place

**Claim:** the book's glossary supplies compact, teachable definitions for the
course's core vocabulary — from collision theory and electrostatic attraction to
the mole — so a tutor can anchor terminology questions on a single
book-native reference.
**Evidence:** the glossary states collision theory "states that for a reaction
to occur, the reactant particles must collide with each other and the collision
needs to have sufficient energy and the correct orientation"
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 1109);
it defines "electrostatic attraction the force of attraction between something
that is positive and something that is negative" (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 1111); and it defines the
"mole a unit of the amount of a substance" with the Avogadro number of particles
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 1116).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-003 — Bonding knowledge is carried in key points built on electrostatic attraction and ion formation

**Claim:** the book's ionic-bonding chapter carries its central teaching in
key-point boxes that define electrostatic attraction in plain language and
derive ions from electron transfer — the exact formulation a tutor should reuse
when a student's bonding model needs rebuilding.
**Evidence:** a key point states "Electrostatic attraction simply means that
positively charged particles attract negatively charged particles." and explains
that when a metal combines with a non-metal "an electron is transferred from the
outer shell of the sodium atom to the outer shell of the chlorine atom", forming
ions: "A positive ion is called a cation" and "A negative ion is called an
anion" (SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line
269). A companion key point introduces "isoelectronic, which means 'have the
same number of electrons'" — with the explicit caution that an Fe²⁺ ion is
"definitely not a noble gas structure!" (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 272).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-004 — Energetics knowledge rests on ∆H and bond-energy definitions the book states exactly

**Claim:** the energetics chapter's key points give the tutor the two
definitions that anchor all quantitative energy work — the enthalpy change ∆H
(in kJ/mol, measurable only as a change) and bond energy as the energy to break
one mole of covalent bonds in gaseous molecules.
**Evidence:** a key point states "∆H is pronounced 'delta H'. The Greek letter ∆
is used to mean 'change in'", that "it is not possible to measure how much
enthalpy (H) something has", and that "The units for ∆H can be written as kJ/mol
or kJ mol-1" (SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl
line 718); another defines "Bond energy is defined as the amount of energy
needed to break 1 mole of covalent bonds in gaseous molecules."
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 759).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-005 — The book's rates key point fixes the exact wording tutors must enforce in rate explanations

**Claim:** for rate-of-reaction explanations the book prescribes the wording
discipline tutors should drill: an explanation that cites more collisions must
also include the idea of time.
**Evidence:** a key point on rates states "When explaining this, do not only say
that there are more collisions. You must always include the idea of time. So,
you should say things such as 'the particles collide more frequently or there are
more collisions per second'." (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 797). The same discipline
reappears in examiner reporting on rate questions, where candidates "often lost
marks due to unclear expressions, with many stating that this led to the rate
increasing rather than being greatest at the start" (SRC-ER-4CH1,
chemistry/4ch1/past-papers/2024-11/4CH1-1C/er.pdf p5) — held in this pack as
corroborating texture.
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-006 — The assessment model a tutor must plan around is two untiered papers totalling 180 marks

**Claim:** the current specification defines Paper 1C as a 2-hour written
examination weighted at 61.1% carrying 110 marks, and Paper 2C as a 1-hour and
15-minute examination weighted at 38.9% carrying 70 marks, with both papers
drawing questions from any topic area and Paper 2C alone assessing the bold
(chemistry-only) content.
**Evidence:** the specification's assessment table states for Paper 1C
"Assessed through a 2-hour written examination set and marked by Pearson." and
"The paper is weighted at 61.1% of the qualification." with "110" marks, and for
Paper 2C a "1-hour and 15-minute written examination" weighted at 38.9% with
"70" marks, Paper 2C assessing "all the content, including content that is in
bold and has a 'C' reference"; the page adds "The total number of marks for this
qualification is 180." (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p33). The book's own
front matter carries the matching assessment overview section in its course
structure (SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl
line 8).
Temporal scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-BOOK-4CH1-SB1 (the parse v3 corpus of the student book of
record — course structure, glossary pages, and the bonding, energetics and rates
key points) and SRC-SPEC-4CH1 (the current specification's chemistry-content map
and assessment-information page). Supplementary: SRC-ER-4CH1 held in the pack —
the November 2024 1C report page is quoted once to corroborate the rates wording
discipline, and the June 2019 1C report cover is held as a single-page
identity-presence entry consumed for no claim. SRC-TL-4CH1 is held as a
one-page identity-presence entry and consumed for no claim here. All excerpts
are bounded with locators preserved; caps enforced by the pack builder.

## Limitations / Coverage Gaps

The pack's book window holds 45 excerpts: the course structure, the ionic- and
covalent-bonding key points, the energetics and rates key points, and the
glossary's definitional band — so Unit 2 and Unit 4 content is not sampled here
and no claim is made about it. The glossary window holds the c-to-m alphabetical
band only. The specification is held at two pages (the topic map and the
assessment table); assessment-objective detail and the appendices are outside
this pack. No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-008 (BL-008 pass 8) from this artifact's
evidence pack alone; validator of record tools/sib @ 357ace0a; claim QA binds
every citation to a pack excerpt. Research artifact — evidence-backed, not
canonical educational truth.
