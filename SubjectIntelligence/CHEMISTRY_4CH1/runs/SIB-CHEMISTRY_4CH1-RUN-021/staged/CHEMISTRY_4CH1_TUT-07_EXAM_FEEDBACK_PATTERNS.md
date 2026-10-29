---
sib_protocol: SIB-1.0
artifact_id: TUT-07
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
  textbook: false
  question_papers: false
  mark_schemes: false
  examiner_reports: true
  supplementary: true

status: GENERATED
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

# TUT-07 — Exam Feedback Patterns

## Purpose

This artifact extracts the feedback patterns the 4CH1 assessment system itself
models for tutors: how the issuing body's exemplar commentaries explain why
responses earn or lose marks, and how the examiners' reports phrase their
advice. A tutor can mirror these forms when feeding back on a student's written
work. Every claim is carried on a bounded, locator-addressed excerpt from this
artifact's own evidence pack.

## Scope

**Covers:** the exemplar commentary's feedback forms for the rates question
(responses A-H) and the crude-oil question; the polymer-plotting feedback pair;
the examiners' report advice on wording and presentation; and the assessment
objective weightings that tell a tutor where feedback effort pays.

**Out of scope:** misconception diagnosis (TUT-06) and the book-side hint
system (TUT-05).

## Executive Summary

The exemplar commentaries give a tutor the examiner's exact grammar: what was
missing ("no specific mention of this, so the mark... cannot be awarded"), what
wording was wrong ("The gas does not evaporate; it escapes."), and what
precision a comparative demand requires ("stating that the acid has a high
concentration is not sufficient"). The examiners' reports compress the same
discipline into advice ("It must be heat or thermal energy to gain the mark.")
and presentation guidance. The assessment objectives set the proportions: AO1
and AO2 at 38-42% each, AO3 at 19-21%, so feedback on application and analysis
carries as much weight as knowledge recall.

## Main Analysis

### TUT-037 — The examiners grade against assessment objectives whose weightings tell a tutor where feedback pays

**Claim:** the qualification's assessment objectives weight knowledge (AO1) at
38-42%, application and analysis (AO2) at 38-42%, and experimental skills (AO3)
at 19-21% — so a tutor's feedback time should be split accordingly across
recall, application and practical-data skills.
**Evidence:** the specification's assessment-objectives table lists "AO1
Knowledge and understanding of chemistry 38–42%", "AO2 Application of knowledge
and understanding, analysis and evaluation of chemistry 38 42%" and "AO3
Experimental skills, analysis and evaluation of data and methods in chemistry
19–21%" (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p35). Temporal scope:
CURRENT — AUTHORITATIVE.

### TUT-038 — The commentary's core feedback move is naming the missing marking point, not restating the answer

**Claim:** the exemplar commentaries award and refuse marks by naming exact
missing elements — for the crude-oil distillation response the mark was refused
because "there was no specific mention of this" for the vaporised crude oil —
the feedback form a tutor should copy: point to the absent statement.
**Evidence:** the commentary records "Although the answer implied that the crude
oil vapour is put into the column, there was no specific mention of this, so the
mark for bullet point 2 cannot be awarded." and for the empirical formula
"An empirical formula should not show any functional groups that may be
present." (SRC-TL-4CH1,
teaching-and-learning-materials/international-gcse-chemistry-exemplars-commentary.pdf
p28). Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-039 — Comparative demands are marked strictly: high is not higher

**Claim:** the rates-question commentaries define the comparative standard:
stating a high concentration "is not sufficient" without the comparison, and a
collision frequency "must be higher" — feedback that teaches students to answer
the comparison actually asked.
**Evidence:** the commentary states "A comparison of the two concentrations of
acid is required, so stating that the acid has a high concentration is not
sufficient." (SRC-TL-4CH1,
teaching-and-learning-materials/international-gcse-chemistry-exemplars-commentary.pdf
p10); on collisions, "It is important to make a comparison between the
frequencies of successful collisions. To state that there will now be a high
frequency of collisions is not sufficient; it must be higher."
(SRC-TL-4CH1,
teaching-and-learning-materials/international-gcse-chemistry-exemplars-commentary.pdf
p12). Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-040 — Graph language is feedback-marked: origin-passing lines mean proportionality

**Claim:** the commentaries repeatedly correct graph descriptions to the
examinable phrase — a line through the origin requires "directly proportional",
not "as one increases so does the other" — a pattern a tutor can drill with any
graph question.
**Evidence:** the commentary states "Since the graph line passes through the
origin it is necessary to state that the two variables are directly proportional
to one another, not just that as one increases so does the other."
(SRC-TL-4CH1,
teaching-and-learning-materials/international-gcse-chemistry-exemplars-commentary.pdf
p12), repeating the proportional wording on response D's page
(SRC-TL-4CH1,
teaching-and-learning-materials/international-gcse-chemistry-exemplars-commentary.pdf
p14). Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-041 — The examiners' reports compress feedback into mark-bearing wording rules and presentation advice

**Claim:** the reports phrase feedback as concrete rules — "energy" alone does
not score, "heat or thermal energy" does — alongside presentation advice on
showing methods, giving a tutor ready-made feedback lines.
**Evidence:** the June 2025 report states "A few lost the mark for just saying
that energy was released. It must be heat or thermal energy to gain the mark."
(SRC-ER-4CH1, chemistry/4ch1/past-papers/2025-06/4CH1-2C/er.pdf p6); the June
2022 report's model-answer commentary advises "Consider using bullet points or a
numbered list to show a method clearly." (SRC-ER-4CH1,
chemistry/4ch1/past-papers/2022-06/4CH1-1C/er.pdf p6). Temporal scope:
CURRENT — AUTHORITATIVE.

### TUT-042 — The commentaries name recurring errors explicitly, marking them as common mistakes

**Claim:** the feedback corpus labels recurring errors as common mistakes — the
addition-polymer mislabelling appears identically on two responses' pages — so a
tutor can pre-empt exactly these errors before they cost marks.
**Evidence:** response B's commentary states "It is a common mistake to name an
addition polymer as a saturated compound." (SRC-TL-4CH1,
teaching-and-learning-materials/international-gcse-chemistry-exemplars-commentary.pdf
p82) and response C's commentary repeats the same sentence
(SRC-TL-4CH1,
teaching-and-learning-materials/international-gcse-chemistry-exemplars-commentary.pdf
p83). The June 2019 report likewise names "The most common misapprehensions were
stating bromine as a gas at room temperature and even more thought solid iodine
was purple or brown." (SRC-ER-4CH1,
chemistry/4ch1/past-papers/2019-06/4CH1-2C/er.pdf p6). Temporal scope:
CURRENT — AUTHORITATIVE.

### TUT-079 — The particulate-account chain is the marking currency: what the ions are, what the frequency must do

**Claim:** Two unmined commentary pages carry the same correction chain from opposite ends of a rates question: the acid must be described as ions in dilute solution, the concentration effect must be stated as more particles per unit volume, and the rate consequence must be stated as more successful collisions per unit time — each missing step costing its mark even when the outcome is acknowledged. Alongside sits the design-level insight the candidates missed: the marble-chip mass is irrelevant because the chips are always in excess. The feedback therefore teaches the full explanatory ladder a tutor must drill — model, census, frequency — plus the excess reasoning that explains why one variable drops out of the account entirely.
**Evidence:** the chain: "In dilute solution HCl exists as ions, not molecules. It is also necessary to state that there are more particles/ions in the same volume. The second mark could not be awarded since the candidate did not state that there are more successful collisions per unit time." (SRC-TL-4CH1, international-gcse-chemistry-exemplars-commentary.pdf p8); the same ruling at the weaker response: "In dilute solution HCl exists as ions, not molecules. It is also necessary to state that there are more particles/ions in the same volume." with the identical collision ruling (SRC-TL-4CH1, international-gcse-chemistry-exemplars-commentary.pdf p16); the design insight: "The mass of the marble chips is irrelevant in this experiment since the chips are always in excess." (SRC-TL-4CH1, international-gcse-chemistry-exemplars-commentary.pdf p16).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-080 — The examiner autopsies the misapprehension itself, diagnosing where the wrong model came from

**Claim:** The examiner's report on the halogen-states question does not merely record that answers were wrong — it names the two most common misapprehensions (bromine as a gas, solid iodine as purple or brown) and then diagnoses their probable origin: the candidates were likely recalling iodine vapour or iodine solution, the two forms in which that element is most often seen. The same report autopsies the decimal-place losses with a reading-compliance reading: some candidates rounded to the periodic-table value rather than the demanded one decimal place, perhaps because they did not read the whole question, and the mark is lost even though the method was correct. Feedback at this grain tells the tutor what to re-teach and what habit to train, separately.
**Evidence:** the autopsy: "The most common misapprehensions were stating bromine as a gas at room temperature and even more thought solid iodine was purple or brown. These candidates may have been thinking about iodine vapour or iodine solution." (SRC-ER-4CH1, 2019-06/4CH1-2C/er.pdf p6); the reading diagnosis: "Some candidates failed to give their answer to 1 decimal place as required, perhaps showing they did not read the whole question." and the cost: "Unfortunately they have not then given the final answer to the required one decimal place so do not gain the third mark." (SRC-ER-4CH1, 2019-06/4CH1-2C/er.pdf p6).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-081 — Named common mistakes repeat verbatim across responses, and definition-completeness is marked atomically

**Claim:** The commentary's common-mistake sentence for addition polymers is printed twice, once under each of two different student responses earning 5/6 and 6/6 — the repetition itself is evidence that the commentary treats it as a standing pattern, not a one-off remark. The crude-oil exemplar page adds the atomic accounting grain: a mark is lost simply because the answer never states that a hydrocarbon contains only carbon and hydrogen atoms, and a dot-and-cross loses its mark for missing lone pairs even when the bonding pair is right. The tutor learns that definitional completeness and lone-pair discipline are individually priced marks, auditable from the feedback alone.
**Evidence:** the repeated pattern: "It is a common mistake to name an addition polymer as a saturated compound." as printed under both Student Response B (5/6) and Student Response C (6/6) (SRC-TL-4CH1, international-gcse-chemistry-exemplars-commentary.pdf p82 and p83); the atomic accounting: "One mark lost because the answer does not state that only carbon and hydrogen atoms are present in a hydrocarbon." and the lone-pair ruling: "Lone pairs on the chlorine atom missing." (SRC-TL-4CH1, international-gcse-chemistry-exemplars-commentary.pdf p28).
Temporal scope: CURRENT — AUTHORITATIVE.
## Evidence / Source Basis

Supplementary evidence carries this family: SRC-TL-4CH1 (the issuing body's
exemplar student answers with examiner commentary — the rates-question response
pages, the crude-oil response page, and the polymer response pair) and SRC-ER-4CH1
(June 2025 2C, June 2022 1C and June 2019 2C report pages). Primary family
grounding is supplied by SRC-SPEC-4CH1 (the assessment-objectives page); the
student book of record is held in the pack as identity-presence entries (the
image-only scan and the parse corpus without planned excerpts) and consumed for
no claim. All excerpts are bounded with locators preserved; caps enforced by the
pack builder.

## Limitations / Coverage Gaps

The pack holds eight exemplar-commentary pages of the booklet's 89 and three
report pages of the 24 reports of record; the 2024-06 1C report is excluded of
record (garbled text layer, the exclusion established at RUN-005). Feedback
patterns for calculation questions and six-mark responses generally are outside
the packed windows. The AO weighting table's per-paper breakdown is packed but
only the headline weightings are claimed. No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-008 (BL-008 pass 8) from this artifact's
evidence pack alone; validator of record tools/sib @ 357ace0a; claim QA binds
every citation to a pack excerpt. Research artifact — evidence-backed, not
canonical educational truth. Deepened under SIB-CHEMISTRY_4CH1-RUN-021 (D3 REQUIRED-core depth pass, tranche 5: TUT): +3 records (TUT-079..TUT-081), zero-append mining of the carried pack of record on the OCR text-of-record basis resolved by operator ruling (gate_resolution_sb1_ebook.json); every quote self-bound to raw excerpt text before the official gate; claim QA re-bound all citations.
