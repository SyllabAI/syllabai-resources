---
sib_protocol: SIB-1.0
artifact_id: ASM-03
artifact_version: 1.0
subject: Chemistry
qualification: International GCSE
specification: 4CH1
curriculum_version: "2017"

research_family: assessment_intelligence
applicability: REQUIRED

temporal_scope:
  current: true
  legacy: false

source_scope:
  specification: true
  textbook: false
  question_papers: true
  mark_schemes: true
  examiner_reports: false
  supplementary: true

# lifecycle: GENERATED -> QA_PASSED -> STAGED
status: PUBLISHED
generated_by: zai_agent
generated_at: 2026-10-26

provenance:
  source_manifest: "SRC-QPMS-4CH1"
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-005"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "f61a5bafe6cacdf538e5e06d86f818e7737cbfe3"
    syllabai_resources: "367b5d61cd5f1ab115f9947ba2981f08389540ee"
---

# ASM-03 — Question Archetypes

## Purpose

This artifact names the recurring question archetypes of the 4CH1 papers as they appear
in the official exam corpus of record (SRC-QPMS-4CH1): the stable stem-forms candidates
meet on every sitting, each anchored to one worked instance from the parsed papers with
its embedded mark-scheme behaviour. Where ASM-02 classified item classes by response
format, this artifact classifies by what the question makes the candidate DO. Every
archetype claim is carried on a bounded, locator-addressed excerpt from the run's
evidence pack. Research artifact for teaching and revision design; canonical planes are
read-only here and nothing was written to them.

## Scope

**Covers:** six archetypes — selection items; definition/recall stems; linked
explanations; practical description/test items; multi-step calculations; and
construction/drawing items (equations, formulae, graphs, diagrams).

**Grounding:** SRC-QPMS-4CH1 (official paper extractions with embedded mark-scheme
text — the 2019-06 1C and 2C papers of the pack supply the anchors, with the
interleaved 2020-01 paper confirming recurrence).

**Out of scope:** command-word frequency (ASM-04), mark tariffs (ASM-05), examiner
sentiment (EXM family).

## Executive Summary

Six archetypes cover the overwhelming majority of observable 4CH1 items. Selection
items ask candidates to pick a letter, statement or option; recall items ask for a
definition or a name; the signature reasoning archetype is the linked explanation whose
mark scheme names two or three points M1/M2/M3; practical items ask candidates to
describe a test or an experimental step, anchored to core-practical knowledge;
calculations are multi-step working problems printed with answer lines and Mr values;
and construction items ask candidates to complete or draw equations, displayed
formulae, energy diagrams and curves of best fit. Each archetype carries a
characteristic mark-scheme shape, which makes archetype recognition a teachable exam
skill in its own right.

## Main Analysis

### ASM-013 — The selection archetype: pick the letter, statement or row

**Claim:** selection items ask the candidate to identify rather than produce — picking
an option, a letter from a diagram, or a statement.
**Evidence:** an opening MCQ asks "Which statement explains this observation?"
(SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 11-25) and a Periodic-Table item
asks "Give the letter from the diagram that represents a noble gas." (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 100-114).
**Design reading:** selection items are 1-mark diagnostics with low answer-production
load, used by the papers as fast on-ramps inside larger questions.
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-014 — The recall/definition archetype: state what is meant by

**Claim:** definition items use a stable "state what is meant by / state the meaning
of" stem form and are marked against a tight accepted-answer set.
**Evidence:** "State what is meant by the term isomers." with mark scheme "M1
(compounds/molecules) with the same ... molecular formula" , and "State the meaning of the term ionic
bond." (SRC-QPMS-4CH1, 2020-01/4CH1-1C/questions.md lines 274-288).
**Design reading:** the mark scheme's OWTTE ("or words to that effect") machinery
around these stems rewards precise technical vocabulary — exactly the terminology
work the MIS/EXP families support.
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-015 — The linked-explanation archetype: M1/M2/M3 chains

**Claim:** the papers' signature reasoning archetype asks candidates to link two or
three points, and the mark schemes expose the chain explicitly as M1/M2 (sometimes
M3) with dependency notes.
**Evidence:** "Explain why graphite conducts electricity." is marked "An explanation
that links together the following two points" with "M1 (graphite has) delocalised
electron(s)" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 514-528); the redox
item runs a three-point chain "An explanation that links the following three points"
(SRC-QPMS-4CH1, 2020-01/4CH1-1C/questions.md lines 224-238), as does the
alloy-hardness item "Explain why magnalium is harder than aluminium." (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 275-289).
**Design reading:** every link must be explicit — a candidate who gives the fact
without the because, or vice versa, banks only one of the marks; this is the single
highest-yield writing pattern to drill.
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-016 — The practical/test archetype: describe a test or a step

**Claim:** practical-chemistry items ask candidates to describe a test (with reagent
and observation) or an experimental step, anchored in the core practicals.
**Evidence:** "Describe a test to show that chloroethene is unsaturated." is marked
"M1 add bromine water/solution ... M2 (bromine water/solution) is decolourised/"
(SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 603-617), and the water-test item
"Describe how anhydrous copper(II) sulfate is used to test for water." runs the same
two-point shape (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 868-882).
**Design reading:** the recurring mark shape is reagent-then-observation; the
bromine-water and copper(II)-sulfate tests are the canonical drills.
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-017 — The calculation archetype: multi-step working with printed anchors

**Claim:** calculation items are multi-step working problems with answer lines, Mr
values printed in the stem, and bullet-step mark schemes.
**Evidence:** "Calculate the mass of oxygen required to react with 32 g of methane.
[Mr of methane = 16]" is marked with bullet steps "• calculate moles of methane •
calculate mass of oxygen" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 822-836);
the hydration-number item "Calculate the value of x." runs the same bullet-step law
(SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 1377-1391), and the enthalpy item
demands "Include a sign in your answer." (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 337-351).
**Design reading:** method marks live in the working; a bare correct answer can score
full marks on some items while others require the steps — the mean-time item grants
that "62/62.3 with no working scores 2" (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 163-177), so the drill is to show working anyway.
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-018 — The construction archetype: complete or draw

**Claim:** construction items ask candidates to complete an equation, draw a displayed
formula or diagram, or draw a curve of best fit — production tasks with
shape-of-answer mark schemes.
**Evidence:** "Complete the equation for this reaction. C5H12 + Br2 → +" is marked
"M1 correct formula of organic product" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 786-800); "Draw the displayed formula for another isomer of C5H12" is marked
"M1 correct carbon skeleton, M2 all hydrogen atoms and all bonds shown, M2 dep on
M1" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 771-785); "Draw an energy
level diagram for the reaction" (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 383-397) and "Draw a curve of best fit." (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 1020-1034) complete the set.
**Design reading:** construction marks reward completeness (all atoms, all bonds,
correct sign, correct axis labels), which is a different drilling target from the
linked-writing archetypes.
Temporal scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-QPMS-4CH1 — the run's pack carries the 2019-06 1C and 2C papers
plus the interleaved 2020-01 1C paper as bounded line-window excerpts with line
locators preserved; every archetype anchor above is quoted from those excerpts and
locator-addressed. Supplementary pack sources were not consumed. No examiner-report
evidence is used here (EXM family ground), and no specimen material was cited.

## Limitations / Coverage Gaps

Six archetypes is an observational floor, not a claimed exhaustive partition: rare
forms (e.g. long synthesis chains) may blend several archetypes. Anchors concentrate
on two sessions of one paper family; recurrence across further sessions is asserted
only where the pack shows it. Archetype-to-AO mapping is deliberately omitted — that
inference belongs to a later analysis with ASM-10's coverage ground. No canonical
planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-005 (BL-008 pass 5) from the run's evidence
pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 bound all citations
to pack excerpts. Research artifact — evidence-backed, not canonical educational
truth.
