---
sib_protocol: SIB-1.0
artifact_id: PRA-02
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

# PRA-02 — Method/Technique Patterns

## Purpose

This artifact catalogues the method and technique patterns of record for 4CH1
practical work: the apparatus-handling micro-decisions the book teaches
(condenser feed direction, burette reading conventions), the measurement and
conversion habits, the core-practicals guide's technique micro-notes
(SRC-TL-4CH1), the spec's technique-statements demand (SRC-SPEC-4CH1), and the
repeating method families (calorimetry trio, salt-preparation split) that make
techniques transferable (SRC-BOOK-4CH1-SB1). Claims ride only on this artifact's
own bounded pack excerpts. Canonical planes are untouched.

## Scope

**Covers:** apparatus-handling patterns; burette and condenser technique
conventions; volume conversion habits; technique micro-notes from the official
guide; the calorimetry method family; the salt-preparation technique split by
solubility class; terminology-guide apparatus band.

**Out of scope:** which procedures are core (PRA-01) and error analysis
(PRA-04).

## Executive Summary

Technique in the evidence of record is taught as pattern, not as one-off
instructions. Apparatus micro-decisions come with reasons — water enters the
condenser at the lower end so the jacket stays full; burette numbers increase
downward and readings go to two decimal places with the trailing 0/5 rule.
Volume habits are explicit (divide by 1000 before concentration work) and
setups carry permitted variants (acid and alkali can swap places with the alkali
in the burette). Above the micro-level sit two repeating method families: the
calorimetry trio (combustion, displacement, dissolving) shares the
polystyrene-cup pattern with swapped contents, and salt preparation splits by
solubility — excess-solid-and-filter for soluble salts, precipitation for
insoluble ones. The official terminology guide's apparatus and measurement bands
give the technique vocabulary, and the spec demands the techniques themselves as
statements.
The deepened records extend the technique claim into its governance layer: the titration procedure's volumetric recording law (top-to-bottom burette scale, 0.05 cm3 resolution written to two decimal places, and the one-drop precision ceiling), the combustion-calorimetry procedure's own error budget and version-tolerance trade-off, and the board's terminology guidance, which governs practical vocabulary by contextual use rather than formal definition and states the exam's evaluative intent outright.

## Main Analysis

### PRA-008 — Apparatus-handling patterns come with reasons

**Claim:** apparatus technique is taught as decision-plus-reason, not rule alone.
**Evidence:** the distillation section explains that "water is always fed into
the condenser at the lower end" so the jacket fills better and stays full if
flow stops (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line
74); the burette section fixes the reading convention — numbers increase top to
bottom, readings to two decimal places, with the trailing digit 0 on the line
and 5 between lines (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 586). Temporal scope: CURRENT —
AUTHORITATIVE.

### PRA-009 — Measurement conversion habits and permitted setup variants

**Claim:** technique patterns include unit conversion habits and permitted
reversals of apparatus roles.
**Evidence:** the titration hints instruct to "divide the volume by 1000 to
convert" to dm³ for concentration work and note "The acid and alkali can also be
added the other way round, with the alkali in the burette"
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 254).
Temporal scope: CURRENT — AUTHORITATIVE.

### PRA-010 — The official guide's technique micro-notes

**Claim:** the core-practicals guide supplies technique micro-decisions and
learning-focused questioning at the point of use.
**Evidence:** the chromatography page notes "The filter paper can be supported
by placing it on top of a beaker" (SRC-TL-4CH1,
biology-chemistry-physics-core-practical-guide.pdf p 76) and pairs the
technique with "Questions you could ask to enhance learning" prompts
(SRC-TL-4CH1, biology-chemistry-physics-core-practical-guide.pdf p 77); the
terminology guide's contents band the technique vocabulary from using apparatus
through making measurements to presenting and analysing data (SRC-TL-4CH1,
practical-terminology-in-int-gcse-science.pdf p 2). Temporal scope: CURRENT —
AUTHORITATIVE.

### PRA-011 — The calorimetry method family

**Claim:** three enthalpy procedures share one method pattern — polystyrene cup
in a beaker, measured transfer, initial temperature, reagent weighed — with
contents swapped per reaction class, and the book states the family's variant
tolerance.
**Evidence:** the combustion procedure burns small alcohols in a spirit burner
heating known water (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 730); the displacement procedure
places "a polystyrene cup in a 250 cm³ glass beaker" with 50 cm³ of 0.200
mol/dm³ copper(II) sulfate and weighed zinc (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 742); the dissolving procedure
repeats the same cup-and-cylinder pattern for ammonium nitrate-class salts
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 748); a KEY
POINT notes other versions may recommend different temperature rises or fixed
heating times (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line
731). Temporal scope: CURRENT — AUTHORITATIVE.

### PRA-012 — The salt-preparation technique split

**Claim:** salt-making technique splits by solubility class: excess
solid-plus-acid with filtration for soluble salts, double decomposition with
precipitate for insoluble ones.
**Evidence:** the copper(II) sulfate procedure heats acid, adds copper(II) oxide
in spatula portions until some remains, then filters the excess
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 617); the
sodium/potassium/ammonium section names the same excess-then-filter method class
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 623); the
insoluble lead(II) sulfate is prepared by mixing two solutions so "A white
precipitate of lead(II) sulfate will form" (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 633). Temporal scope: CURRENT —
AUTHORITATIVE.

### PRA-013 — Techniques demanded as specification statements

**Claim:** the specification demands the techniques themselves — a describe-them
statement, not only outcomes.
**Evidence:** the separation statement reads "1.10 describe these experimental
techniques for the separation of mixtures" listing simple distillation, fractional
distillation, filtration, crystallisation and paper chromatography
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p 18);
the same statement list heads the guide's chromatography page
(SRC-TL-4CH1, biology-chemistry-physics-core-practical-guide.pdf p 75).
**Specification Points:** 1.10
Temporal scope: CURRENT — AUTHORITATIVE.

### PRA-036 — Burette reading discipline is a stated recording law with a precision ceiling

**Claim:** the titration procedure fixes the volumetric recording law — reading direction, resolution, and the two-decimal-place writing rule — and bounds the technique's inherent precision.
**Evidence:** the reading rule is explicit — "the numbers increase from the top to the bottom: 0 is at the top and 50 is at the bottom" — and the writing rule follows it: "We normally record readings from the burette to the nearest 0.05 cm3", with "The second decimal place is given as '0' if the level of solution is on the line and '5' if it is between the lines." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 586); the recorded table shows the law applied — final 23.85, initial 2.10, volume of alkali added 21.75 cm3 (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 588); the same window bounds the technique itself, since the pH swings drop-to-drop near the endpoint so "the most precise we can be is to know the neutralisation point to within 1 drop" (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 586).
Temporal scope: CURRENT — AUTHORITATIVE.
### PRA-037 — The combustion-calorimetry procedure confesses its own error budget and licenses method variants

**Claim:** the combustion variant of the calorimetry method enumerates its error sources inside the procedure, makes one of them diagnosable in-flight, and tolerates method versions under an explicit trade-off law.
**Evidence:** the error budget is in-procedure — "There are many sources of error in this experiment, in particular large amounts of heat loss." with the routes named: "The warm water gives out heat to the air, heat is lost from the flame, which goes straight into the air rather than into the water" (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 738); incomplete combustion is observable from the apparatus itself — "the flame of the wick is often yellow orange rather than blue, and soot (carbon) is produced at the bottom of the copper can" (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 738); variant tolerance is licensed with its bound: "You may see other versions of this experiment recommending a different temperature rise or suggesting that you heat the water for a fixed number of minutes." while "The higher the temperature the water reaches, the greater the heat losses during the experiment." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 731).
Temporal scope: CURRENT — AUTHORITATIVE.
### PRA-038 — The board governs practical terminology by context, not by definition

**Claim:** technique vocabulary is governed at board level: the terminology guide declines to give formal definitions, illustrates terms inside practical scenarios across four named aspects, and states the exam's evaluative intent outright.
**Evidence:** the guide opens by naming the problem — "The use of terminology within practical and experimental work in science is a complicated issue." and "Definitions of terms can vary between different sources" (SRC-TL-4CH1, practical-terminology-in-int-gcse-science.pdf p 3); it fixes the exam posture: "we are less interested in students learning strict definitions of terms, and more interested in students appreciating" data and methods critically (SRC-TL-4CH1, practical-terminology-in-int-gcse-science.pdf p 3); the planning section carries the variable framework with its payoff — "Controlling variables will improve the validity of the data in an investigation." — and the apparatus section makes selection itself a data-quality decision: "When selecting apparatus, it is important to consider how the choice made can affect the data collected." (SRC-TL-4CH1, practical-terminology-in-int-gcse-science.pdf p 4).
Temporal scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-BOOK-4CH1-SB1 (apparatus, conversion, calorimetry and
salt-preparation chunks at line+chunk-id locators) and SRC-TL-4CH1
(core-practicals guide technique pages; practical-terminology guidance).
Supplementary: SRC-SPEC-4CH1 technique statement page; SRC-QPMS-4CH1 held with
one calorimetry item for exam-face context. Bounded excerpts with locators
preserved; caps enforced by the pack builder.

## Limitations / Coverage Gaps

This artifact catalogues the technique patterns visible in its pack's excerpt windows; techniques outside the captured pages/lines are neither enumerated nor denied. The RUN-020 deepening added records only from the held pack surface (zero-append tranche): no windows were appended, so detail outside the captured surface is neither quoted nor denied. The terminology guidance is quoted as parsed (its source PDF uses contextual illustration rather than definitions, and line-break hyphenation is preserved in the parse). OCR-era quirks of the book parse are quoted as parsed or paraphrased, never repaired. No examiner sentiment is synthesized from mark schemes. No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-006 (BL-008 pass 6) from this artifact's evidence pack alone; deepened under SIB-CHEMISTRY_4CH1-RUN-020 (D3 REQUIRED-core depth pass, tranche 4 — PRA+PED, zero-append) with +3 records (PRA-036..038) authored only from the held pack excerpts, quotes pre-bound under the markup-transparent self-check; validator of record tools/sib @ 357ace0a; claim QA r3 binds every citation to a pack excerpt. Research artifact — evidence-backed, not canonical educational truth.
