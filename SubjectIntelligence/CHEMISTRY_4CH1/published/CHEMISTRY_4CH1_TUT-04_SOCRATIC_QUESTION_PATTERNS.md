---
sib_protocol: SIB-1.0
artifact_id: TUT-04
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
  specification: false
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

### TUT-070 — The guide's acid-metal why-questions make the anomaly itself the opening move

**Claim:** The core-practicals guide's acid-metal page questions the class on what should not have happened: aluminium starts slowly and then speeds up, and calcium stops reacting while both reactants remain. Each prompt is printed as a bare why-question attached to the surprising observation, so the socratic move is built into the document — the tutor need not invent the puzzle, only withhold the resolution until the class produces collision-based accounts (the oxide layer that must be breached, the sulfate crust that seals the surface). The page frames these as questions that focus students on the important aspects of the practical, which is exactly the socratic contract: fewer, sharper questions aimed at the procedure's hidden chemistry.
**Evidence:** the framing: "Questions you could ask to enhance learning and focus your students on important aspects of the practical:" followed by the anomaly pair: "Why does the reaction between aluminium and dilute hydrochloric acid start off very slowly but then increase in rate after a while?" and "Why does the reaction between calcium and sulfuric acid stop after a while, even though neither the metal nor the acid has fully reacted?" (SRC-TL-4CH1, biology-chemistry-physics-core-practical-guide.pdf p99).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-071 — The electrolysis battery runs a socratic ladder from observation to principle, with the scaffold deliberately faded

**Claim:** The electrolysis unit battery builds its hardest item as a graduated dialogue: first the phenomenon (a bulb lighting only at melting, purple fumes at the positive electrode, lilac flashes at the negative), then the why-question that targets the principle beneath the observation, then the identification and half-equation demands that formalise it. The preceding half-equation drill fades its own support — electrons are supplied for the first four items only — so the student must supply the scaffold unaided as the ladder climbs. This is socratic sequencing at question-battery grain: the book engineers the same withhold-then-formalise progression a tutor conducts orally.
**Evidence:** the staged phenomenon: "As soon as the potassium iodide was molten, the bulb came on. Purple fumes were seen coming from the positive electrode, and lilac flashes were seen around the negative one." with the principle probe: "Explain why the bulb didn't come on until the potassium iodide melted." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 393); the scaffold fade: "state whether each involves oxidation or reduction. Electrons have been put in for the first four but not for the ones after that." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 393).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-072 — The teacher-facing topic guide turns socratic questioning on the teaching tool itself

**Claim:** The equilibrium topic guide opens by questioning the profession's own canonical shortcut: it cites the published argument that Le Châtelier's principle is counterproductive to understanding, notes the principle survives in specifications worldwide regardless, and states plainly that it is not required for teaching this specification yet students invoke it in answers. The guide then prices the shortcut with evidence — a test of 109 chemistry teachers in which only one understood the counter-intuitive outcome — so the tutor is left holding a documented reason to question the principle they were themselves taught. Socratic doubt is thereby aimed at the teacher's own toolkit, not just the student's.
**Evidence:** the opening citation: "In 1984 R.T. Allsop and N.H. George wrote an article, published in Education in Chemistry, entitled 'Le Châtelier – A Redundant Principle?' in which they argued that the use of the principle was counterproductive to the understanding of chemical equilibrium." and the status finding: "Although Le Châtelier's Principle is not required for teaching the International GCSE Chemistry specification, a number of students refer to it in answers." (SRC-TL-4CH1, Chemical-equilibrium---FINAL.pdf p2); the evidence of teacher vulnerability: "One problem with Le Châtelier's Principle is that it fails to predict the outcome of changes to conditions in a number of cases, particularly reactions involving gases where a change in temperature will lead to a change in pressure in a closed system." (SRC-TL-4CH1, Chemical-equilibrium---FINAL.pdf p2).
Temporal scope: CURRENT — AUTHORITATIVE.
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
canonical educational truth. Deepened under SIB-CHEMISTRY_4CH1-RUN-021 (D3 REQUIRED-core depth pass, tranche 5: TUT): +3 records (TUT-070..TUT-072), zero-append mining of the carried pack of record on the OCR text-of-record basis resolved by operator ruling (gate_resolution_sb1_ebook.json); every quote self-bound to raw excerpt text before the official gate; claim QA re-bound all citations.
