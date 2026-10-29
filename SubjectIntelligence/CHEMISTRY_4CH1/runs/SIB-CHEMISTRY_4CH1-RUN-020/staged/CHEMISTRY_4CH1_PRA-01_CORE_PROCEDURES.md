---
sib_protocol: SIB-1.0
artifact_id: PRA-01
artifact_version: 1.1
subject: Chemistry
qualification: International GCSE
specification: 4CH1
curriculum_version: "2017"

research_family: practical_procedural_intelligence
applicability: REQUIRED

temporal_scope:
  current: true
  legacy: false

source_scope:
  specification: true
  textbook: true
  question_papers: true
  mark_schemes: true
  examiner_reports: false
  supplementary: false

# lifecycle: GENERATED -> QA_PASSED -> STAGED
status: PUBLISHED
generated_by: zai_agent
generated_at: 2026-10-29

provenance:
  source_manifest: "SRC-TL-4CH1"
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-020"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "f39fc0fde3ee12f97efa5c031e16c17c25243fd5"
    syllabai_resources: "923232c73d9ac7dca748b29ccca1c8067ba741aa"
---

# PRA-01 — Core Procedures

## Purpose

This artifact catalogues the core practical procedures of record for 4CH1 at
three grains: the specification's own designated practical statements
(SRC-SPEC-4CH1), the core-practicals guide's spec-coded procedures with
teaching-grade notes and expected results (SRC-TL-4CH1), and the student book's
PRACTICAL procedure boxes (SRC-BOOK-4CH1-SB1), with the exam face of those
procedures taken from the official question corpus (SRC-QPMS-4CH1). Claims ride
only on this artifact's own bounded pack excerpts. Canonical planes are
untouched.

## Scope

**Covers:** specification-designated practicals; spec-coded core practicals;
in-book procedure boxes; acceptable-variant teaching notes; quantified expected
results; procedural safety notes; practical demand as examined.

**Out of scope:** technique vocabulary detail (PRA-02), error analysis
(PRA-04), and method selection (PRA-05).

## Executive Summary

The core procedures exist in three aligned layers. The specification itself
designates procedures as statements — practical: investigate reactions between
dilute acids and metals; describe experiments to investigate rate factors. The
core-practicals guide binds each investigation to its specification code (Core
practical 2: Chromatography at 1.13) and arms it with teaching notes: the best
half-equations to hand students for aqueous electrolysis, acceptable variants
for strong acid or alkali, and quantified expected results (ammonium chloride at
0.0500 mol in 90.0 g of water producing about −1.8 °C, worked through Q = mcΔT).
The book carries the same procedures as PRACTICAL boxes with safety notes baked
in. The question corpus shows the exam face: describe-the-test and prepare-a-sample
items drawn from these same procedures.
The deepened records extend the family's exam-face claim into result-processing law: the book's own chromatography analysis routine (spot matching by travelled distance, centre-of-spot measurement, the Rf ratio with its 0-to-1 sanity envelope and its solvent-and-paper validity conditions), the solubility procedure's quantified processing route (mass scaling to the 100 g convention, the general solubility equation, and the always-quote-a-temperature discipline), and the apparatus pragmatics — a non-critical supply voltage and the expected-volume caveat where chlorine dissolves — that pre-arm observation judgement inside the electrolysis procedures themselves.

## Main Analysis

### PRA-001 — The specification designates procedures as content

**Claim:** practical procedures are specification content in their own right —
stated as practical or describe-experiments statements with codes.
**Evidence:** the inorganic section states "2.21 practical: investigate
reactions between dilute hydrochloric and sulfuric acids and metals" naming
magnesium, zinc and iron (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p 24); the physical section
states "3.9 describe experiments to investigate the effects of changes in
surface area of a solid, concentration of a solution, temperature and the use of
a catalyst on the rate of a reaction" (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p 28).
**Specification Points:** 2.21, 3.9
Temporal scope: CURRENT — AUTHORITATIVE.

### PRA-002 — Core practicals are bound to their specification codes

**Claim:** the core-practicals guide makes each procedure addressable by binding
it to its specification code as a numbered core practical.
**Evidence:** the separation section heads "Core practical 2: Chromatography"
and states "Core practical: Investigate paper chromatography using inks/food
colourings" against code 1.13, with the surrounding separation-technique
statements 1.10-1.12 listed alongside (SRC-TL-4CH1,
biology-chemistry-physics-core-practical-guide.pdf p 75).
**Specification Points:** 1.10, 1.13
Temporal scope: CURRENT — AUTHORITATIVE.

### PRA-003 — The book carries procedures as PRACTICAL boxes

**Claim:** the student book instantiates the procedures as stepwise PRACTICAL
boxes with concrete quantities and conditions.
**Evidence:** the solubility box runs "A procedure we can use to measure the
solubility of potassium nitrate in water at 40°C" (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 46); the chromatography box
investigates dye composition on paper (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 78); the titration section defines
the technique as finding how much of one solution reacts with a set volume of
another (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 255);
the aqueous-electrolysis box investigates sodium chloride solution
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 373).
Temporal scope: CURRENT — AUTHORITATIVE.

### PRA-004 — Teaching-grade notes carry acceptable variants

**Claim:** the core-practicals guide arms procedures with acceptable variants and
the exact teaching forms, so procedure judgement is prepared before the lab.
**Evidence:** the electrolysis guidance lists "The best ionic half-equations to
give to the students are:" for hydrogen at the cathode and oxygen at the anode,
and marks alternatives as "Acceptable if strong acid is electrolysed" or strong
alkali (SRC-TL-4CH1, biology-chemistry-physics-core-practical-guide.pdf p 89);
it also anticipates the chlorine-dissolves complication and redirects the test
to the solution above the anode (SRC-TL-4CH1,
biology-chemistry-physics-core-practical-guide.pdf p 89). Temporal scope:
CURRENT — AUTHORITATIVE.

### PRA-005 — Expected results are quantified in the guidance

**Claim:** the guide quantifies expected outcomes — masses, moles, temperature
changes — and hands over the processing route, and it pre-plans the rates
investigation's control compromises.
**Evidence:** the calorimetry page specifies ammonium chloride at 2.67 g
(0.0500 mol) in 90.0 g of water producing about −1.8 °C, then works Q = mcΔT and
ΔH = −Q ÷ n (SRC-TL-4CH1,
biology-chemistry-physics-core-practical-guide.pdf p 115); the rates page states
"It is impossible to maintain an exactly constant surface area" and prescribes
the same mass, number and similar size of chips as the partial control, with
acid concentrations determined by trial in advance (SRC-TL-4CH1,
biology-chemistry-physics-core-practical-guide.pdf p 129). Temporal scope:
CURRENT — AUTHORITATIVE.

### PRA-006 — Procedures carry in-book safety notes

**Claim:** safety instructions are embedded in the procedure boxes themselves,
tied to the specific hazard of the step.
**Evidence:** the solubility procedure's safety note reads "Wear eye protection
and heat gently to avoid burns" from spitting hot solid (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 45); the chlorine electrolysis note
instructs "Do not smell the chlorine, especially if you have asthma" and to
switch the current off once chlorine is detected (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 371). Temporal scope: CURRENT —
AUTHORITATIVE.

### PRA-007 — The exam face of the procedures

**Claim:** the official question corpus examines these procedures as describe and
prepare items drawn directly from the practical statements.
**Evidence:** a water-test item asks "Describe how anhydrous copper(II) sulfate
is used to test for water" with a linked mark scheme (SRC-QPMS-4CH1,
2019-06/4CH1-1C/questions.md lines 868-882); a preparation item asks the student
to "obtain a pure, dry sample of hydrated copper(II) sulfate crystals from the
filtrate" at five marks (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines
1221-1235). Temporal scope: CURRENT — AUTHORITATIVE.

### PRA-033 — The book arms the chromatography procedure with result-processing law

**Claim:** procedure depth extends past execution into interpretation — the book's own analysis routine specifies spot matching, a measurement discipline, and the Rf ratio with its validity conditions.
**Evidence:** the analysis hint instructs "Measure to the centre of the spot." and demonstrates the match law — "The mixture (m) has spots corresponding to dyes d1, d3 and d4." — with a same-coloured dye excluded once it has travelled a different distance (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 81); the ratio carries a hard validity envelope — "An Rf value must be between 0 and 1." with no units — and cross-paper comparison is licensed only under identical conditions: "you can still compare R values as long as you use the same type of paper and the same solvent" (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 82).
Temporal scope: CURRENT — AUTHORITATIVE.
### PRA-034 — The solubility procedure carries its own quantified processing route

**Claim:** the solubility box quantifies the full data path from raw masses to a temperature-pinned solubility value, and ties measurement care to result validity.
**Evidence:** the worked example scales the raw capture — "12.28g of solid is the maximum mass that dissolves in 20.00 g of water" — five-fold to the 100 g convention and states "The solubility of potassium nitrate at 40°C is therefore 61.4g per 100g of water." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 49); the accompanying hint binds discipline to the number — "you must always quote a temperature with a solubility value" — and the gentle-heating instruction is justified by measurement validity: "We heat the solution gently to make sure that none spits out." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 47); curve-reading tasks quantify the same route — "From the graph we can see that the solubility at 40 °C is 40g per 100g of water." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 54).
Temporal scope: CURRENT — AUTHORITATIVE.
### PRA-035 — Apparatus pragmatics and expected-yield caveats ride inside the procedure

**Claim:** the electrolysis procedures carry their apparatus tolerances and expected-observation caveats on the same teaching surface, so the expected result is pre-armed before the lab.
**Evidence:** the apparatus key point fixes nothing arbitrary — "The power supply can be a 6 volt battery or a power pack. It doesn't matter which." and "The voltage isn't critical either." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 358); the aqueous box quantifies the expected volumes and pre-explains the observed shortfall — "We would expect to get the same volume of hydrogen as chlorine." yet "we appear to obtain less chlorine than expected because it is more soluble in water" (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 372).
Temporal scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-SPEC-4CH1 (practical statement pages at page locators),
SRC-TL-4CH1 (core-practicals guide pages: spec-coded procedures, acceptable
variants, quantified results), and SRC-BOOK-4CH1-SB1 (PRACTICAL boxes at
line+chunk-id locators). Supplementary: SRC-QPMS-4CH1 (2019-06 Paper 1C
question items with embedded mark-scheme text). Bounded excerpts with locators
preserved; caps enforced by the pack builder.

## Limitations / Coverage Gaps

This artifact catalogues the procedures visible in its pack's excerpt windows — the full twelve-core-practical roster is indexed in the library's curriculum registry and consumed family-wide; individual procedures outside the windows are neither enumerated nor denied. The RUN-020 deepening added records only from the held pack surface (zero-append tranche): no windows were appended, so processing-law detail outside the captured pages/lines is neither quoted nor denied. OCR-era quirks of the book parse (doubled KEY POINT stamps, half-equation spacing, Rf rendered as R or Rt in places) are quoted as parsed or paraphrased, never repaired. No examiner sentiment is synthesized from mark schemes. No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-006 (BL-008 pass 6) from this artifact's evidence pack alone; deepened under SIB-CHEMISTRY_4CH1-RUN-020 (D3 REQUIRED-core depth pass, tranche 4 — PRA+PED, zero-append) with +3 records (PRA-033..035) authored only from the held pack excerpts, quotes pre-bound under the markup-transparent self-check; validator of record tools/sib @ 357ace0a; claim QA r3 binds every citation to a pack excerpt. Research artifact — evidence-backed, not canonical educational truth.
