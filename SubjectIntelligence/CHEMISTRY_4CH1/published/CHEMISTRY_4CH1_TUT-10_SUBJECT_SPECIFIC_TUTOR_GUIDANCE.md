---
sib_protocol: SIB-1.0
artifact_id: TUT-10
artifact_version: 1.1
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
generated_at: 2026-10-30

provenance:
  source_manifest: "SRC-BOOK-4CH1-SB1"
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-021"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "bc4740884"
    syllabai_resources: "7352d2eab0bc822a8273d8dadfbeaefe3faf45d2"
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

### TUT-088 — The practical-questions appendix teaches the explain-grammar: precaution plus priced reason

**Claim:** The book's guide to practical questions turns the safety-precaution demand into a grammar lesson: eye protection alone is never the answer, the word explain in the question stem means a reason must accompany the precaution, and the mark tariff tells the student how many information pieces are owed. The appendix's own table makes the pricing explicit — each precaution row carries its marks twice, one for the action and one for the because-clause — so the tutor can train safety answers as two-column habit rather than improvisation.
**Evidence:** the stem and its lesson: "Apart from wearing eye protection, explain a safety precaution that you would need to take in doing this experiment. (2marks)" followed by "Notice the word 'explain' in the last sentence. 'Explain' means that, as well as giving a precaution, you have to give a reason for it. Look at the number of marks available. If there is more than 1 mark, you have to give more than one piece of information." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 1077); the priced table: "Do the experiment in a fume cupboard (1) because chlorine is poisonous (1)" (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 1078).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-089 — Anomaly discipline runs end-to-end: ignore on the graph, and name a mechanism — clumsiness is not an answer

**Claim:** The book and the board's terminology guide agree on how anomalies must be handled, and each polices a different half of it. The book's appendix rules the drawing side: the anomalous point is excluded from the best-fit line completely, and the cause-hunt must be specific — a concrete experimental fault is demanded, with human error named as the non-answer. The terminology guide rules the attribution side: exam questions always require a specific identified error, so blame cannot be parked on the experimenter's clumsiness. Together they give the tutor a two-part training drill: mechanically exclude the point, then supply a mechanism precise enough to have produced it.
**Evidence:** the drawing rule: "You might be asked to explain what might have caused it. When you are drawing your straight line or curve, you ignore the anomalous point completely." with the specificity demand: "It isn't enough to say simply that 'wrong measurements were taken or human error', you have to be much more specific, for example 'too much calcium carbonate was added by mistake, and that produced more carbon dioxide than expected'." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 1090); the attribution rule: "exam questions always require a specific error to be identified – errors and anomalies should not simply be attributed to avoidable clumsiness on the part of the experimenter!" (SRC-TL-4CH1, practical-terminology-in-int-gcse-science.pdf p7).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-090 — The graph-language ladder grades descriptions from proportional through linear to merely positive

**Claim:** The appendix builds a graded vocabulary for describing graphs and shows the exam cost of each rung: the loose as-one-increases-so-does-the-other sentence is rejected because a curve would satisfy it too; directly proportional is defined operationally through doubling and tripling and reserved for straight lines through the origin; a straight line missing the origin must be called linear instead; and the equivalence of proportional with directly proportional is stated outright. For the tutor this is the exact marking ladder for graph-description answers, teachable as three sentences the student can rehearse.
**Evidence:** the rejected rung: "The correct expression is that 'the volume of carbon dioxide is directly proportional to the mass of calcium carbonate used'. If you just say that 'as the mass of calcium carbonate increases, the volume of carbon dioxide increases', that isn't precise enough, and you may not get the full mark. That faulty statement could equally well describe a curve." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 1097); the operational definition: "The phrase directly proportional means if you double the mass of calcium carbonate, the volume of carbon dioxide produced will double as well." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 1097); the fallback rung and the equivalence: "If a straight line does not pass through the origin, you should say there is a linear relationship between the two variables." and "The words proportional and directly proportional mean the same thing, there is no difference between them." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 1097).
Temporal scope: CURRENT — AUTHORITATIVE.
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
canonical educational truth. Deepened under SIB-CHEMISTRY_4CH1-RUN-021 (D3 REQUIRED-core depth pass, tranche 5: TUT): +3 records (TUT-088..TUT-090), zero-append mining of the carried pack of record on the OCR text-of-record basis resolved by operator ruling (gate_resolution_sb1_ebook.json); every quote self-bound to raw excerpt text before the official gate; claim QA re-bound all citations.
