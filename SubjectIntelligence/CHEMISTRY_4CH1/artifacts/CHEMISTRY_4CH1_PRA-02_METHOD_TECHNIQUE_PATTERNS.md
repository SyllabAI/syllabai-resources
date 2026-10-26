---
sib_protocol: SIB-1.0
artifact_id: PRA-02
artifact_version: 1.0
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

status: GENERATED
generated_by: zai_agent
generated_at: 2026-10-26

provenance:
  source_manifest: "SRC-TL-4CH1"
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-006"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "3b6a443d4e3643f461a1cca12c6e1ad47ab6b596"
    syllabai_resources: "8b5a64f1b18724208ff19969b002028d3ed41bed"
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

## Evidence / Source Basis

Primary evidence: SRC-BOOK-4CH1-SB1 (apparatus, conversion, calorimetry and
salt-preparation chunks at line+chunk-id locators) and SRC-TL-4CH1
(core-practicals guide technique pages; practical-terminology guidance).
Supplementary: SRC-SPEC-4CH1 technique statement page; SRC-QPMS-4CH1 held with
one calorimetry item for exam-face context. Bounded excerpts with locators
preserved; caps enforced by the pack builder.

## Limitations / Coverage Gaps

Technique patterns are catalogued from this pack's excerpt windows; other
apparatus conventions outside the windows are neither enumerated nor denied.
OCR-era quirks of the book parse (split words, stray glyphs in a pH extension
note) are quoted as parsed or paraphrased, never repaired. The QPMS item is
cited for demand context only; no mark-point analysis is claimed here (the MS
family owns that layer). No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-006 (BL-008 pass 6) from this artifact's
evidence pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 binds
every citation to a pack excerpt. Research artifact — evidence-backed, not
canonical educational truth.
