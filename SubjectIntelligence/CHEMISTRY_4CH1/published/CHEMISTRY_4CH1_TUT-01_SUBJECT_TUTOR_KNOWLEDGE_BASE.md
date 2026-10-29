---
sib_protocol: SIB-1.0
artifact_id: TUT-01
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
  supplementary: false

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

### TUT-061 — The book polices formula notation and the implied-charge convention a tutor must enforce

**Claim:** The book's KEY POINT apparatus does not just present formulas — it polices how they are written and read. Brackets are taught as a misreading-prevention device with a worked counter-example showing exactly how a bracketless formula miscounts atoms, and the implied-charge convention is stated as a rule with its exception valve: charges may be written when a point requires it, but they are present whether written or not. A tutor grading formula writing is therefore enforcing the book's own two-part convention, not a private preference.
**Evidence:** the bracket rule is taught with its failure mode: "If you didn't write the brackets, the formula would look like this: BaNO32. That would read as 1 barium, 1 nitrogen and 32 oxygens!" (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 285); the charge convention is stated with its exception valve: "It is sometimes written Na+Cl- if you are trying to make a particular point, but for most purposes the charges are left out. In an ionic compound, the charges are there, whether you write them or not." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 289).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-062 — Stability is taught as an energy ladder with the book's own everyday anchor

**Claim:** The book gives the tutor a complete explanatory model for stability before energetics is ever formalised: lower energy means more stable, reactions happen so that substances become more stable, and bond formation releases energy because the product sits lower on that ladder. The model is anchored to a deliberately everyday image — a dropped book falling to the floor — so the tutor can re-ground any abstract stability argument in the book's own analogy. The energetics chapter then re-uses the same ladder at reaction grain: stability names the relative energies of reactants and products, and the more energy a chemical has the less stable it is.
**Evidence:** the bonding chapter states the ladder: "Generally, the lower the energy something has, the more stable it is. Chemical reactions usually occur so that something becomes more stable." and anchors it: "Think about holding a book: if you let go of the book, it will fall to the floor, where it has less (potential) energy, therefore it becomes more stable. When bonds form energy is given out and so the substance formed has less energy, therefore it is more stable." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 309); the energetics chapter re-states it at reaction grain: "The term stability is usually used to describe the relative energies of the reactants and the products in a chemical reaction. The more energy a chemical has, the less stable it is." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 719).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-063 — The book grades its own graphs and calorimetry compromises: method-law a tutor can mark against

**Claim:** Two pieces of method-law are printed in the book's own voice and give the tutor grading criteria that are not examiner-invented. First, a drawing rule: smooth curves are reserved for continuous independent variables, and discrete variables — carbon atoms come only in whole numbers — must be plotted as points, with the book ridiculing the 1.64-carbon alcohol to make the violation visible. Second, a compromise rule: the calorimetry heating-time choice has no ideal answer, because a larger temperature rise magnifies heat losses while a smaller one magnifies reading errors — so the tutor teaches a managed trade-off, not a correct answer. The quantitative chain underneath is likewise defined in-book, specific heat capacity per gram per degree with water's 4.18 J/g/°C as the standing value.
**Evidence:** the drawing rule: "A smooth curve should only be used for a continuous independent variable, one which can take any value. There is no such thing as an alcohol with 0.5 or 1.64 carbon atoms! The number of carbon atoms is a non-continuous variable because it can only take whole number values." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 739); the compromise rule: "There's no ideal answer to this. The higher the temperature the water reaches, the greater the heat losses during the experiment. On the other hand, if you just increase the temperature of the water by a small amount, errors in reading the thermometer or in finding the mass change of the alcohol become too significant." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 731); the quantitative chain: "The specific heat capacity of a substance is defined as the amount of heat needed to raise the temperature of 1 gram of a substance by 1 °C." and "For water, the value is 4.18 J/g/°C (joules per gram per degree Celsius)." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 728).
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
canonical educational truth. Deepened under SIB-CHEMISTRY_4CH1-RUN-021 (D3 REQUIRED-core depth pass, tranche 5: TUT): +3 records (TUT-061..TUT-063), zero-append mining of the carried pack of record on the OCR text-of-record basis resolved by operator ruling (gate_resolution_sb1_ebook.json); every quote self-bound to raw excerpt text before the official gate; claim QA re-bound all citations.
