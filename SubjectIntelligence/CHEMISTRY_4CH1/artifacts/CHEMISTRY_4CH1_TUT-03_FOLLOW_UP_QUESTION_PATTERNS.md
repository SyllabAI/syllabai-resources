---
sib_protocol: SIB-1.0
artifact_id: TUT-03
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

status: GENERATED
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

# TUT-03 — Follow-Up Question Patterns

## Purpose

This artifact maps how the 4CH1 course escalates its demands: the
learning-objective ladder each chapter opens with, how the book's own question
batteries turn those objectives into follow-up work, and how the specification's
command-word taxonomy grades the verbs a student must respond to. A tutor can
use this to place any student on the ladder and choose the next rung. Every
claim is carried on a bounded, locator-addressed excerpt from this artifact's
own evidence pack.

## Scope

**Covers:** the learning-objective openings (their verb vocabulary and
chemistry-only marking); the objective-to-question conversion in the
calculations chapters; the specification's command-word definitions; and the
application-battery pattern at chapter ends.

**Out of scope:** the board's Socratic questioning guidance for practicals
(TUT-04) and examiner feedback on responses (TUT-07).

## Executive Summary

Each chapter opens with "LEARNING OBJECTIVES" phrased in a small verb set —
Know, Understand, Be able to calculate, Describe, Write — with chemistry-only
material explicitly flagged. The question batteries then convert those
objectives into drills, and the drills escalate from course- rehearsed reactions
to unfamiliar reactions where information is supplied. The specification's
command-word taxonomy supplies the assessment-side grading of the same verbs:
Calculate demands working, Comment on demands judgement, Deduce demands
conclusions from given information. The tutor's follow-up sequencing should run
know → calculate → explain → deduce.

## Main Analysis

### TUT-013 — Chapters open with an objectives ladder built on a small verb set

**Claim:** the book's chapter openings state learning objectives in a
consistent verb ladder — Understand, Know, Be able to calculate — so a tutor can
read a chapter's demand level from its objectives page alone.
**Evidence:** the states-of-matter objectives open with "Understand the three
states of matter in terms of the arrangement, movement and energy of the
particles", move to "Know what is meant by the terms: solvent, solute,
solution, saturated solution" and include the chemistry-only item "Know what is
meant by the term solubility in the units g per 100 g of solvent."
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 21).
The atomic-structure objectives include "Be able to calculate the relative
atomic mass of an element (Aᵣ) from isotopic abundances"
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 86).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-014 — Objectives distinguish rehearsed content from unfamiliar applications in the same breath

**Claim:** the equation-writing objective explicitly spans two rungs — reactions
studied in the course and unfamiliar reactions with supplied information — so
the tutor's follow-up pattern is fixed by the objective itself: first rehearse,
then transfer.
**Evidence:** the chapter 5 objectives require "Write word equations and
balanced chemical equations (including state symbols):" "for reactions studied
in this course" and "for unfamiliar reactions where suitable information is
provided", alongside "Calculate percentage yield" and "Practical: Know how to
determine the formula of a metal oxide by combustion (e.g. magnesium oxide) or
by reduction (e.g. copper(Il) oxide)" (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 135). Temporal scope:
CURRENT — AUTHORITATIVE.

### TUT-015 — The question batteries convert objectives into graded drills on the same verbs

**Claim:** the chapter batteries mirror the objectives verb-for-verb — the
write-equations objective becomes the "Balance the following equations:" drill
across eleven items from Fe + HCl to C₈H₁₈ — so follow-up work can be picked
straight from the battery at the matching rung.
**Evidence:** the chapter 5 battery question 1 asks to "Balance the following
equations:" across items including "Fe + HCl → FeCl₂ + H₂" and "C₈H₁₈ + O₂ →
CO₂ + H₂O", then question 2 continues "Calculate the relative formula masses of
the following compounds:" (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 229). Temporal scope:
CURRENT — AUTHORITATIVE.

### TUT-016 — Follow-ups embed worked method so the next question tests transfer, not method discovery

**Claim:** the concentration battery embeds a fully worked volume calculation
before its drill questions, converting the follow-up demand from "find a method"
to "apply this method to new numbers" — the book's own model of scaffolding.
**Evidence:** the chapter 6 battery carries the worked reasoning "You will need
25.0 cm³ of the sodium hydrogencarbonate solution to neutralise the
hydrochloric acid." before setting the molar-volume drill with the convention
"In questions 1 to 4, take the molar volume to be 24 dm³ (24 000 cm³) at rtp."
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 259).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-017 — The specification's command-word taxonomy grades the verbs the batteries train

**Claim:** the assessment-side ladder is the specification's command-word
taxonomy: Calculate is "Obtain a numerical answer, showing relevant working.",
Comment on "Requires the synthesis of a number of variables from
data/information to form a judgement.", and Deduce is "Draw/reach conclusion(s)
from the information provided." — a tutor hearing a student's target grade can
map it onto these verbs.
**Evidence:** the specification's Appendix 5 table defines "Calculate |
Obtain a numerical answer, showing relevant working.", "Comment on | Requires
the synthesis of a number of variables from data/information to form a
judgement." and "Deduce | Draw/reach conclusion(s) from the information
provided." (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p51). Temporal scope:
CURRENT — AUTHORITATIVE.

### TUT-018 — Chapter-end batteries escalate to rule application across whole substance lists

**Claim:** the electrolysis battery shows the top rung of the follow-up
pattern: one rule set applied serially across eight substances spanning molten
and aqueous cases, followed by half-equation writing and an observation scenario
— the form a tutor should use to test whether rules are portable.
**Evidence:** question 1 asks to "State what is formed at the cathode and at the
anode during the electrolysis of the following substances." across "Molten
lead(II) bromide" to "Sodiumhydroxide solution", and question 2 escalates to
"Copy and complete the following half-equations for reaction at the anode or
cathode, and state whether each involves oxidation or reduction."
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 393).
The electrolysis objectives frame the same demand: "Write ionic half-equations
representing the reactions at the electrodes during electrolysis and understand
why these reactions are classified as oxidation or reduction"
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 354).
Temporal scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-BOOK-4CH1-SB1 (the parse v3 corpus — chapter 1, 3, 5, 6
and 10 learning-objective pages and the matching question batteries) and
SRC-SPEC-4CH1 (Appendix 5 command-word taxonomy page). Supplementary: SRC-TL-4CH1
(topic-guide cover page) and SRC-ER-4CH1 (June 2019 1C report cover page) are
held as single-page identity-presence entries and consumed for no claim here.
All excerpts are bounded with locators preserved; caps enforced by the pack
builder.

## Limitations / Coverage Gaps

The pack window holds the first 48 objectives-and-questions excerpts in book
order, concentrated in Units 1 and 2; Unit 3 and Unit 4 objective pages are
outside the window and no claim is made about their ladder. The command-word
page is held once and quotes the taxonomy's first entries; the full taxonomy
continues beyond the 1,600-character excerpt cap. Unit-question synoptics are
covered in TUT-02's pack and are not re-claimed here. No canonical planes were
written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-008 (BL-008 pass 8) from this artifact's
evidence pack alone; validator of record tools/sib @ 357ace0a; claim QA binds
every citation to a pack excerpt. Research artifact — evidence-backed, not
canonical educational truth.
