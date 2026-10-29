---
sib_protocol: SIB-1.0
artifact_id: TUT-02
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
  specification: false
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

# TUT-02 — Common Student Questions

## Purpose

This artifact catalogues the question forms 4CH1 students actually meet in the
validated student book of record — the chapter and unit question batteries that
define what "answering chemistry questions" means on this course — so a tutor
can anticipate the question shapes a student will bring and rehearse them
directly. Every claim is carried on a bounded, locator-addressed excerpt from
this artifact's own evidence pack; nothing is asserted beyond the packs.

## Scope

**Covers:** the book's chapter-question batteries and end-of-unit question
batteries in the pack window: their skills tagging, their command-word usage,
and their escalating demand from recall to multi-step calculation.

**Out of scope:** the learning-objective ladder itself (TUT-03), Socratic
question technique from the teaching corpus (TUT-04), and exam-paper feedback
patterns (TUT-07).

## Executive Summary

The book's question batteries are not an afterthought: each battery is tagged
with transferable skills (critical thinking, interpretation, analysis, problem
solving, reasoning), and the questions climb from one-word state names through
classification and explanation to multi-part calculations with follow-through
structure. The pack window shows the pattern across Units 1 and 2: changes of
state, classification of matter, separation methods, equation balancing and
mole calculations, electrolysis products, and synoptic unit questions that
demand explanation, not just recall.

## Main Analysis

### TUT-007 — Chapter questions are explicitly skills-tagged, signalling what each question trains

**Claim:** the book's chapter-question batteries open with explicit skills
tags — critical thinking, interpretation, analysis, problem solving, reasoning —
so a tutor can tell a student not just what a question asks but what skill it
trains.
**Evidence:** the chapter 1 battery opens "CHAPTER QUESTIONS" with the tags
"SKILLS", "CRITICAL THINKING", "INTERPRETATION", "ANALYSIS", "PROBLEM SOLVING"
and "REASONING", before asking "What mass of potassium chloride would crystallise
from the solution in biii if the temperature fell to 10°C?"
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 56).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-008 — Early-course questions pair classification drills with explanation demands

**Claim:** the elements-compounds-mixtures battery combines classify-type
questions with an explanation demand about purity — the recurring pairing a
tutor should expect: name the category, then justify it.
**Evidence:** question 1 asks to "Classify each of the following substances as
an element, compound or mixture:" and question 3 sets the melting-point scenario
where "Substance X melts at 122 °C and substance Y melts between 87and93 °C"
and asks to "Explain which one is the pure substance."
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 83).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-009 — The quantitative chapters drill equation balancing and mole calculations in long graded batteries

**Claim:** the calculations chapters' question batteries are long graded drills
— eleven balancing items spanning simple to complex equations, then blocks of
relative-formula-mass, percentage-composition and mole-conversion calculations —
so a tutor can diagnose exactly which rung a student fails on.
**Evidence:** the chapter 5 battery question 1 asks to "Balance the following
equations:" across items from "Fe + HCl → FeCl₂ + H₂" to "C₈H₁₈ + O₂ → CO₂ +
H₂O", followed by "Calculate the relative formula masses" (question 2),
"Calculate the percentage of nitrogen" (question 3), and mole-to-mass and
mass-to-mole conversions (questions 4 and 5) (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 229). Temporal scope:
CURRENT — AUTHORITATIVE.

### TUT-010 — Solution-volume questions arrive with worked context embedded in the battery

**Claim:** the concentration chapter's battery embeds a fully worked
solution-volume calculation inside the question section itself — modelling the
method before the drill — so the questions that follow are follow-ups to a shown
method, not cold starts.
**Evidence:** the chapter 6 battery opens with the worked reasoning "You will
need 25.0 cm³ of the sodium hydrogencarbonate solution to neutralise the
hydrochloric acid." and then fixes the molar volume convention "In questions 1
to 4, take the molar volume to be 24 dm³ (24 000 cm³) at rtp." before question 4
builds a three-step mole-to-volume chain from "0.240g of magnesium is reacted
with an excess of dilute sulfuric acid" (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 259). Temporal scope:
CURRENT — AUTHORITATIVE.

### TUT-011 — Electrolysis questions rehearse rule application across a list of unfamiliar substances

**Claim:** the electrolysis battery's flagship question applies one rule set —
products at each electrode — across eight named substances spanning molten and
aqueous cases, then escalates into half-equations and an observation-based
scenario; a tutor should expect students to stumble on exactly the aqueous-vs-
molten switch.
**Evidence:** question 1 asks to "State what is formed at the cathode and at the
anode during the electrolysis of the following substances." from "Molten
lead(II) bromide" through "Sodiumhydroxide solution", and question 3 follows
with the molten-potassium-iodide scenario asking "Explain why the bulb didn't
come on until the potassium iodide melted."
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 393).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-012 — Unit-level questions are synoptic and demand explanation in terms of structure and bonding

**Claim:** the end-of-unit batteries mix definition questions, quantitative
items marked with their mark tariffs, and structure-bonding explanations — the
register a tutor should treat as the course's real assessment voice.
**Evidence:** the Unit 1 battery asks to "Explain what you understand by the
term 'relative atomic mass' of an element." then sets the bromine-isotope
calculation with "Give your answer to 2 decimal places." and the diamond/
graphite/fullerene explanations including "Explain why graphite conducts
electricity. (2)" (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 396). Temporal scope:
CURRENT — AUTHORITATIVE.

### TUT-064 — The book hands the tutor ready-made model-answer chains for structure-property demands

**Claim:** The book's question commentary does not leave structure-property explanations to the tutor's invention — it prints the chains themselves in exam-answer grain. Ionic brittleness is explained as a same-charge collision sequence ending in the crystal splitting itself apart; the water-versus-organic-solvent solubility contrast is stated as a paired rule; and ductility is folded into malleability with an explicit same-explanation identity, so the tutor teaches one laminated-layer mechanism covering both words. These are precisely the sentences a student must reproduce when the exam asks why, and the book supplies them verbatim.
**Evidence:** the brittleness chain: "lonic crystals tend to be brittle. This is because any small distortion of a crystal will bring ions with the same charge alongside each other. Like charges repel and so the crystal splits itself apart." and the solubility pair: "lonic substances tend to be soluble in water. lonic compounds tend to be insoluble in organic solvents." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 299); the ductility identity: "Metals can also be described as ductile. This means that they can be drawn out into wires. The explanation is the same as why they are malleable." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 351).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-065 — The batteries drill data-driven explanation: numbers given, mechanism demanded

**Claim:** The structure-and-bonding batteries systematically pair supplied data with a mechanism demand, which is the exact grammar the exam's explain-with-data items use. The metals question quotes the sea-of-electrons phrase and requires the magnesium electronic configuration to unpack it; a follow-up supplies three consecutive elements' boiling points and demands the trend be explained through electronic configurations and metallic bonding; and the halogen-displacement unit question makes students interrogate the experiment design itself — why the grey cells were never run — before completing the table. A tutor drilling from this book is rehearsing explanation-from-evidence, not recall.
**Evidence:** the phrase-unpacking demand: "A solid metal is often described as having 'a lattice of positive ions in a sea of delocalised electrons'. State the electronic configuration of a magnesium atom and use it to explain what this phrase means." and the data explanation: "The boiling points of sodium, magnesium and aluminium are 890 °C, 1110 °C and 2470 °C, respectively. Explain these values in terms of the electronic configurations of the elements and metallic bonding." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 351); the design interrogation: "Explain why the student did not carry out the experiments shaded in dark grey in the table." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 691); the anomaly hunt: "Explain which student's result is incorrect." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 403).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-066 — The calculation batteries embed yield, excess and approximation honesty in the questions themselves

**Claim:** The unit-question batteries price the honesty concepts inside ordinary mole calculations: a crystallisation experiment states the theoretical 7.61 g and the actual 5.23 g and demands the percentage yield; the pyrite extraction question states the molar-volume assumption in the question stem; and the strontium-hydroxide solubility question ends by declaring its own five-mark answer only approximate — because dissolving changes the volume — and asks for the redesigned experiment that fixes it. The question bank also police reagent choice at the method grain: the halide-test commentary forbids the three acids that would import the very ion being tested for. A tutor therefore teaches yield, excess, assumption-stating and method justification as routine question furniture, not as add-on wisdom.
**Evidence:** the yield drill: "He actually only made 5.23g. Calculate the percentage yield of the student's experiment." and the assumption: "In this question you can assume that the molar volume of any gas at rtp is 24 dm³." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 398); the approximation disclosure: "The calculation used in d gives only an approximate value for the solubility because the volume changes when a substance is dissolved in water." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 400); the reagent prohibition: "You must not use hydrochloric acid (or hydrobromic acid or hydroiodic acid) as you will be adding halide ions and you are certain to obtain a precipitate." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 682).
Temporal scope: CURRENT — AUTHORITATIVE.
## Evidence / Source Basis

Primary evidence: SRC-BOOK-4CH1-SB1 (the parse v3 corpus — the chapter 1, 2, 5,
6, 10 question batteries and the Unit 1 end-of-unit battery). Supplementary:
SRC-SPEC-4CH1 (change-summary page), SRC-TL-4CH1 (topic-guide cover page) and
SRC-ER-4CH1 (June 2019 1C report cover page) are each held as single-page
identity-presence entries and consumed for no claim here. All excerpts are
bounded with locators preserved; caps enforced by the pack builder.

## Limitations / Coverage Gaps

The pack window holds the first 40 question-battery excerpts in book order, so
Units 3 and 4 batteries (energetics, rates, equilibrium, organic) are outside
this pack and no claim is made about their form. Question stems that reference
diagrams or tables are quoted only where the text carries the demand itself;
figure-dependent items are not reconstructed. The mark schemes for these
questions are not part of this pack (answers exist in the book's answer
sections, outside the window). No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-008 (BL-008 pass 8) from this artifact's
evidence pack alone; validator of record tools/sib @ 357ace0a; claim QA binds
every citation to a pack excerpt. Research artifact — evidence-backed, not
canonical educational truth. Deepened under SIB-CHEMISTRY_4CH1-RUN-021 (D3 REQUIRED-core depth pass, tranche 5: TUT): +3 records (TUT-064..TUT-066), zero-append mining of the carried pack of record on the OCR text-of-record basis resolved by operator ruling (gate_resolution_sb1_ebook.json); every quote self-bound to raw excerpt text before the official gate; claim QA re-bound all citations.

