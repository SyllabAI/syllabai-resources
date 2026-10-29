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

### TUT-067 — Follow-up chains resolve into printed arithmetic, and boundary markers police the battery

**Claim:** The book's follow-up answers do not stop at method hints — they resolve all the way to the arithmetic, so a student who missed the intermediate step can reconstruct the whole chain from the printed answer. The solubility follow-up tells the reader where to find the 10 °C value, states it, interprets what staying in solution means, and then subtracts on the page; the chemistry-only boundary is likewise printed inside the battery itself, so the tutor knows exactly where the extension content ends. This makes the batteries self-contained tutoring instruments rather than bare exercise lists.
**Evidence:** the resolved chain: "You can use the data in the table to find the solubility at 10°C. This value is 31.2g per 100 g of water. That means that 31.2 g of potassium chloride will stay in solution at 10 °C. Since you started with 51.0g, the rest of it must have formed crystals:" and the printed arithmetic: "mass of crystals = 51.0 – 31.2 g = 19.8g" closing with "19.8g of potassium chloride will crystallise out." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 56); the in-battery boundary marker: "END OF CHEMISTRY ONLY" (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 56).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-068 — Purity and separation follow-ups run from diagnosis to method selection to creative transfer

**Claim:** The early-course follow-ups rehearse a complete diagnostic arc on one idea: purity is diagnosed from melting behaviour (two white powders, one melting at a fixed point, one across a range), separation is then selected per mixture from a menu of methods, and finally the same skill is transferred to a deliberately whimsical problem — recovering diamonds hidden in labelled sugar — which forces the student to re-derive the method rather than recall a page. The learning objectives anchor the arc: the fixed-point purity criterion is printed as an understanding objective, so the tutor can trace every follow-up back to its statement of record.
**Evidence:** the diagnosis: "Substance X melts at 122 °C and substance Y melts between 87and93 °C. Explain which one is the pure substance." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 83); the anchored objective: "Understand that a pure substance has a fixed melting and boiling point, but that a mixture may melt or boil over a range of temperatures" (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 62); the method menu: "State which separation method you would use to carry out the following separations:" (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 83); the transfer problem: "Describe how you would separate all the diamonds from the sugar." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 83).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-069 — The batteries demand trend-based prediction and accept mechanistic plurality in the answers

**Claim:** Two follow-up families extend the pattern drills beyond recall. Prediction items hand the student a trend and an unseen case: Group 1 knowledge must forecast properties of alkali metals beyond those taught, and the alkane general formula must forecast undecane's physical state at room temperature before any combustion equations are written. The cracking follow-up then discloses the answer's own plurality — the molecule might have split quite differently, and many other ways exist — so the tutor can honestly mark a family of acceptable equations rather than one canonical split. Prediction trains forward inference; plurality disclosure trains tolerance of alternative correct mechanisms.
**Evidence:** the trend-transfer demand: "Use knowledge of trends in Group 1 to predict the properties of other alkali metals" (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 407); the unseen-case prediction: "iiWhat physical state (solid, liquid or gas) would you expect undecane to be in at room temperature (25 °C)?" (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 954); the plurality disclosure: "The molecule might have split quite differently. All sorts of reactions are happening in a catalytic cracker." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 935).
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
canonical educational truth. Deepened under SIB-CHEMISTRY_4CH1-RUN-021 (D3 REQUIRED-core depth pass, tranche 5: TUT): +3 records (TUT-067..TUT-069), zero-append mining of the carried pack of record on the OCR text-of-record basis resolved by operator ruling (gate_resolution_sb1_ebook.json); every quote self-bound to raw excerpt text before the official gate; claim QA re-bound all citations.

