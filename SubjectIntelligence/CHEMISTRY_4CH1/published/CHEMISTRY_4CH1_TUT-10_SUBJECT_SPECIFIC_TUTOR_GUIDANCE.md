---
sib_protocol: SIB-1.0
artifact_id: TUT-10
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
  supplementary: true

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

# TUT-10 — Subject-Specific Tutor Guidance

## Purpose

This artifact consolidates the guidance a 4CH1 tutor needs that is specific to
this subject's assessment culture: the command-word vocabulary the papers use,
the measuring-precision discipline the book's practical appendix teaches, the
board's practical-terminology law (variables, concordance, error attribution),
the mathematical conventions, and the book's own revision advice. Every claim is
carried on a bounded, locator-addressed excerpt from this artifact's own
evidence pack.

## Scope

**Covers:** the book's command-word appendix and the specification's taxonomy;
apparatus choice and burette discipline; reading and recording precision;
reliability and concordance; the fair-test law and precise-variable wording;
the significant-figures convention; and the past-papers-plus-reports revision
strategy.

**Out of scope:** the Socratic practical prompts (TUT-04) and the paper model
(TUT-01, TUT-07).

## Executive Summary

4CH1 tutoring has a precision culture of its own: command words grade the
response type (Calculate demands working; Suggest means a novel-context
proposal); apparatus choice is a marks question (never a beaker for volume);
readings go to half the smallest division and are recorded with trailing zeros
(11.00 cm³, not 11); reliability means repeat-and-check-concordance with titres
within 0.20 cm³; the fair-test law fixes every variable but one; and the word
"amount" is banned in method descriptions. The book's own closing advice is the
strategy: work the recent past papers, mark against published mark schemes, and
read the Examiners' Reports for the practical questions.

## Main Analysis

### TUT-055 — Command words are the tutor's marking vocabulary, published identically by book and board

**Claim:** the book's appendix carries the same command-word taxonomy the
specification publishes — Calculate ("Obtain a numerical answer, showing
relevant working."), Comment on ("Requires the synthesis of a number of
variables from data/information to form a judgement."), Deduce ("Draw/reach
conclusion(s) from the information provided.") — so tutor feedback can use the
board's own definitions.
**Evidence:** the book's appendix table defines "Calculate | Obtain a numerical
answer, showing relevant working.", "Comment on | Requires the synthesis of a
number of variables from data/information to form a judgement." and "Deduce |
Draw/reach conclusion(s) from the information provided."
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 1071);
the specification's Appendix 5 carries the same taxonomy with "Suggest | Use
your knowledge to propose a solution to a problem in a novel context."
(SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p51). Temporal scope:
CURRENT — AUTHORITATIVE.

### TUT-056 — Apparatus choice is an examinable decision with a hard ban

**Claim:** the book's practical appendix turns equipment selection into a rule
set — volume choices span cylinders, burettes, pipettes and gas syringes, a
burette reads to 0.05 cm³, and "you will never use a beaker or a conical flask
to measure the volume of a liquid."
**Evidence:** the appendix states "When it comes to volumes, however, you are
faced with a number of choices of equipment: measuring cylinders of various
sizes, burettes, pipettes and gas syringes. It is important to pick the right
item." (SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line
1079) and "The most common size of burette will measure variable volumes up to
50 cm³, and you can take measurements to the nearest 0.05 cm³. Note you will
never use a beaker or a conical flask to measure the volume of a liquid. They
are too imprecise!" (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 1081). Temporal scope:
CURRENT — AUTHORITATIVE.

### TUT-057 — Readings are taken to half the smallest division and recorded with the precision shown

**Claim:** the book sets the reading law ("Edexcel examiners expect you to read
a scale to a precision of half the smallest divisions marked on whatever piece
of apparatus you are using") and the recording law (a burette reading on the
11 cm³ line is written "11.00 cm³") — the twin disciplines behind most
practical-question marks.
**Evidence:** the appendix states "Edexcel examiners expect you to read a scale
to a precision of half the smallest divisions marked on whatever piece of
apparatus you are using." (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 1083); "if a burette
reading falls exactly on the 11 cm³ line, you should still record it as 11.00
cm³because it was possible to read it to 0.05 cm³"
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 1084).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-058 — Reliability means repeat, check concordance, and discard the outlier set

**Claim:** the book defines reliable results as "in close agreement, but not
necessarily the same", prescribes the repeat-and-check response to reliability
questions, and the board's terminology guide fixes the operational concordance
band for chemistry titres — within 0.20 cm³.
**Evidence:** the appendix states "Reliable results are those that are in close
agreement, but not necessarily the same." and "If you are asked how you would
improve the reliability of a set of results, say that you would repeat the
experiment (possibly more than once), and check the new results for consistency
with the old results." (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 1088); the board's guide
states "readings which achieve a particular level of precision are described as
concordant (for International GCSE Chemistry, this is typically titre values
within 0.20 cm3 of each other)." (SRC-TL-4CH1,
teaching-and-learning-materials/practical-terminology-in-int-gcse-science.pdf
p5). Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-059 — The fair-test law and the banned word: variable precision is itself mark-bearing

**Claim:** the board's terminology guide defines the fair test (all variables
controlled except the independent variable) and the book enforces the precision
of wording — "Avoid the word 'amount' entirely." — plus the mark arithmetic
"one mark equals one piece of information".
**Evidence:** the guide states "An investigation where variables that may affect
the outcome are all controlled – except the independent variable – is referred
to as a fair test." (SRC-TL-4CH1,
teaching-and-learning-materials/practical-terminology-in-int-gcse-science.pdf
p4); the book states "Don't use vague expressions like 'I would change the
amount of hydrogen peroxide.' Avoid the word 'amount' entirely." and "as a
general rule, one mark equals one piece of information"
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 1102);
the fair-test holding law follows: whatever is changed "must be the only thing
which changes from one experiment to the next."
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 1103).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-060 — The subject's own revision strategy: recent past papers, mark schemes, and the Examiners' Reports

**Claim:** the book closes its practical appendix with the revision strategy a
tutor should endorse — work the most recent past papers, check against published
mark schemes, and read the Examiners' Reports, "particularly useful for these
practical-based questions" — while the significant-figures convention sets the
numeric ceiling for every calculated answer.
**Evidence:** the appendix states "The very best way of revising for the exam at
the end of your course is to work through past papers set by your examiners."
and "The Examiners' Reports are particularly useful for these practical-based
questions, where what the examiners are looking for isn't always obvious."
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 1104);
the numeric convention: "You shouldn't quote an answer to more significant
figures than the least precise piece of information you are using in the
calculation." (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 1100). Temporal scope:
CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-BOOK-4CH1-SB1 (the parse v3 corpus — the book's Appendix B
command-word table and Appendix C practical-questions guide) and SRC-SPEC-4CH1
(Appendix 5 command-word taxonomy and Appendix 6 suggested practical
investigations). Supplementary: SRC-TL-4CH1 (the board's practical-terminology
guide — planning, measurement, concordance and error pages — and the maths
skills guide's rounding pages, the latter held as texture for the numeric
conventions). SRC-ER-4CH1 (June 2019 1C report cover page) is held as a
single-page identity-presence entry and consumed for no claim. All excerpts are
bounded with locators preserved; caps enforced by the pack builder.

## Limitations / Coverage Gaps

The pack holds the book's two practical-appendix bands and the board
terminology guide at four of its eight pages; the guide's graph-drawing appendix
is outside the window. The maths skills guide is held at three pages and used as
corroborating texture only — the numerical-skills syllabus is the specification
Appendix 4's territory, outside this pack. The suggested-practicals appendix
page is packed and cited for no record here (the practical corpus is the PRA
family's). No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-008 (BL-008 pass 8) from this artifact's
evidence pack alone; validator of record tools/sib @ 357ace0a; claim QA binds
every citation to a pack excerpt. Research artifact — evidence-backed, not
canonical educational truth.
