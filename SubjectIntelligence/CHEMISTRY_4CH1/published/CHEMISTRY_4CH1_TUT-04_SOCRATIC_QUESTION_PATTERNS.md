---
sib_protocol: SIB-1.0
artifact_id: TUT-04
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

# TUT-04 — Socratic Question Patterns

## Purpose

This artifact captures the board's own Socratic questioning repertoire for 4CH1:
the "questions you could ask to enhance learning" prompts the issuing body
publishes for its core practicals, the topic-guide guidance on how to phrase
answerable questions, and the book's chapter batteries as the student-facing
counterpart. A tutor can reuse these patterns verbatim in one-to-one dialogue.
Every claim is carried on a bounded, locator-addressed excerpt from this
artifact's own evidence pack.

## Scope

**Covers:** the core-practical guide's question prompts for solubility,
chromatography, magnesium oxidation, electrolysis and rusting; the equilibrium
topic guide's question-phrasing warning; and the book's chapter-question
dialogue openers.

**Out of scope:** hint formulation (TUT-05) and misconception correction
patterns (TUT-06).

## Executive Summary

The board's teaching corpus models Socratic questioning as short "why" and
"how could you" prompts attached to each core practical — why pencil not ink in
chromatography, why lift the crucible lid, why the solid does not conduct —
each one probing a specific conceptual pitfall in the procedure. The topic
guides add a discipline: on dynamic equilibrium, a question that lets two
competing effects operate uncontrolled is, in the board's own words, impossible
to answer. The pattern set is: procedural-why prompts, prediction prompts with
controlled variables, and evidence-prompts asking how a claim could be shown.

## Main Analysis

### TUT-019 — The board attaches "questions you could ask" prompts directly to its core practicals

**Claim:** the issuing body's core-practical guide pairs each practical with
"Socratic-style" prompts labelled "Questions you could ask to enhance learning
and focus your students on important aspects of the practical:" — a tutor can
lift them verbatim into dialogue.
**Evidence:** the solubility practical page carries the header "Questions you
could ask to enhance learning and focus your students on important aspects of
the practical:" with the prompt "Why does increasing the temperature usually
affect the solubility of solids?" (SRC-TL-4CH1,
teaching-and-learning-materials/biology-chemistry-physics-core-practical-guide.pdf
p73). The rusting page repeats the structure with "Why is it necessary to leave
the test tube angled as shown in the diagram?" and "How could you show that all
the oxygen has reacted (assume the iron wool is in excess)?"
(SRC-TL-4CH1,
teaching-and-learning-materials/biology-chemistry-physics-core-practical-guide.pdf
p94). Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-020 — Chromatography prompts probe the procedure's hidden assumptions one question at a time

**Claim:** the chromatography question set isolates single assumptions per
question — pencil not ink, spots above solvent, mobile versus stationary phase —
demonstrating the pattern of decomposing a technique into its
testable decisions.
**Evidence:** the chromatography page asks "Why is it important to draw the
lines and write labels on the chromatography paper in pencil and not in ink?",
"Why should the spots of ink be above the level of the solvent in the beaker?"
and "Which is the mobile phase? Which is the stationary phase?"
(SRC-TL-4CH1,
teaching-and-learning-materials/biology-chemistry-physics-core-practical-guide.pdf
p77). Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-021 — Procedure-why prompts link method steps to their reasons

**Claim:** the practical question sets bind each operational step to its reason
— why lift the crucible lid, why heat to constant mass — training the
examinable habit of justifying method choices.
**Evidence:** the magnesium-oxidation question page asks "(i) Why is it
necessary to lift the lid from time to time while heating?" and "(ii) Why is it
necessary to repeat the heating until two consecutive masses are the same?"
(SRC-TL-4CH1,
teaching-and-learning-materials/biology-chemistry-physics-core-practical-guide.pdf
p85). Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-022 — Conceptual-why prompts target the electricity-conduction model in electrolysis

**Claim:** the electrolysis question set opens from the conduction model — why
the solid does not conduct — before escalating to half-equations, the exact
ordering a tutor should follow when the student's electrolysis picture is
shaky.
**Evidence:** the electrolysis question page asks "(i) Solid lead (II) bromide
contains ions. Why does solid lead (II) bromide not conduct electricity?"
before part (ii) asks "Why is this reaction described as oxidation?" for the
half-equation "2Br− → Br2 +2e−" (SRC-TL-4CH1,
teaching-and-learning-materials/biology-chemistry-physics-core-practical-guide.pdf
p90). Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-023 — The topic guides police question phrasing: some equilibrium questions are unanswerable as set

**Claim:** the equilibrium topic guide warns that a question allowing two
competing effects to operate uncontrolled "can, in fact, be impossible to do so"
— answer — and shows the repair: re-phrase so one variable is held, the
discipline a tutor should apply when composing or choosing questions.
**Evidence:** the guide states "When setting questions on dynamic equilibrium it
is very important to phrase the question in such a way that it can be answered."
and that "questions that at first sight seem possible to answer can, in fact,
be impossible to do so." because "There are competing effects and qualitative
arguments cannot predict which is the greater." (SRC-TL-4CH1,
teaching-and-learning-materials/Chemical-equilibrium---FINAL.pdf p6). Temporal
scope: CURRENT — AUTHORITATIVE.

### TUT-024 — The book's own batteries supply the student-facing follow-up dialogue

**Claim:** the book's chapter batteries carry the same dialogic register in
written form — prompts that explain a procedure's hidden logic, such as why a
particular acid must be used in the halide test — so tutor and battery can
alternate without register shift.
**Evidence:** the halide-test question explanation states "The acid is added to
react with and remove other anions which might also produce precipitates with
silver nitrate solution" and "You must not use hydrochloric acid (or hydrobromic
acid or hydroiodic acid) as you will be adding halide ions and you are certain
to obtain a precipitate." (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 682). Temporal scope:
CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-TL-4CH1 (the issuing body's core-practical guide —
solubility, chromatography, magnesium, electrolysis and rusting question pages —
and the equilibrium topic guide's question-setting page). The family's
book-grounding primary is carried by SRC-BOOK-4CH1-SB1 (the halide-test
question-battery excerpt). Supplementary: SRC-SPEC-4CH1 (change-summary page)
and SRC-ER-4CH1 (June 2019 1C report cover page) are held as single-page
identity-presence entries and consumed for no claim. All excerpts are bounded
with locators preserved; caps enforced by the pack builder.

## Limitations / Coverage Gaps

The pack holds five of the guide's practical question pages plus the
equilibrium guide's phrasing page; the guide's biology and physics sections and
the remaining chemistry practicals (titration, ester preparation) are outside
the pack and no claim is made about them. The equilibrium guide's worked
re-phrasing is quoted only to the extent the excerpt window carries it. The
book-side dialogue evidence is one battery excerpt; the wider battery form is
catalogued in TUT-02. No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-008 (BL-008 pass 8) from this artifact's
evidence pack alone; validator of record tools/sib @ 357ace0a; claim QA binds
every citation to a pack excerpt. Research artifact — evidence-backed, not
canonical educational truth.
