---
sib_protocol: SIB-1.0
artifact_id: GAP-01
artifact_version: 1.0
subject: Chemistry
qualification: International GCSE
specification: 4CH1
curriculum_version: "2017"

research_family: gap_intelligence
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
generated_at: 2026-10-26

provenance:
  source_manifest: "SRC-SPEC-4CH1"
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-009"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "2cb92fe5f56d22f1b231c129a7e0dbc27bf86007"
    syllabai_resources: "6ef8c89291a6662f11fc6dc5ada151c47b172075"
---

# GAP-01 — Curriculum Coverage Gaps

## Purpose

This artifact audits where the validated student book of record and the
current specification of record align — and where they do not — for the
Pearson Edexcel International GCSE in Chemistry (4CH1). It maps the
specification's four-topic architecture and its chemistry-only machinery
against the book's unit, chapter and chunk-level coverage, and discloses every
coverage asymmetry the evidence packs can actually support. Every claim is
carried on a bounded, locator-addressed excerpt from this artifact's own
evidence pack; gaps that the pack cannot verify are disclosed as unverified,
never filled by invention. Canonical planes are untouched.

## Scope

**Covers:** the four-topic specification map versus the book's four-unit
spine; the specification's C-suffix (chemistry-only) statements versus the
book's CHEMISTRY ONLY flags at chapter and chunk level; and the sub-topic
granularity of each topic as printed on the specification pages of record.

**Out of scope:** assessment-model coverage (GAP-03), misconception feedback
coverage (GAP-04), and tutor-facing resource gaps (GAP-07).

## Executive Summary

The specification of record divides the chemistry content into four topics —
Principles of chemistry, Inorganic chemistry, Physical chemistry and Organic
chemistry — and the student book mirrors that architecture with four units
opening at pages 2, 122, 206 and 254. The audit finds the book's CHEMISTRY
ONLY machinery working at two levels, chapter flags in the course structure
and in-chunk markers on solubility content, and finds both levels consistent
with the specification's C-suffix statements where the packs permit a direct
comparison. The audit also discloses what it cannot see: the specification
pages carrying the statement-level detail for three topic-1 sub-topics are
outside this artifact's pack, so those chapter-to-statement mappings are
recorded as unverified rather than asserted.

## Main Analysis

### GAP-001 — The four-topic specification map is mirrored by the book's four-unit spine, with different granularity

**Claim:** the specification's chemistry-content map divides the qualification
into four numbered topics, and the student book mirrors that architecture as
four units with printed page openings, but the two sides partition content at
different granularity — the specification prints sub-topic lists per topic
while the book prints 29 numbered chapters across the four units.
**Evidence:** the book's course-structure table lists "UNIT 1: PRINCIPLES OF
CHEMISTRY" at page 2, "UNIT 2: INORGANIC CHEMISTRY" at 122, "UNIT 3: PHYSICAL
CHEMISTRY" at 206 and "UNIT 4: ORGANIC CHEMISTRY" at 254, followed by appendices
and a glossary (SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl
line 8); the specification's topic pages open with sub-topic lists — Topic 1
"Principles of chemistry" with sub-topics "(a) States of matter" through "(i)
Electrolysis" (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf
p17), Topic 2 "Inorganic chemistry" with sub-topics "(a) Group 1 (alkali
metals) – lithium, sodium and potassium" through "(h) Chemical tests"
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p22), Topic
3 with "(a) Energetics", "(b) Rates of reaction", "(c) Reversible reactions and
equilibria" and Topic 4 with "(a) Introduction" through "(h) Synthetic
polymers" (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p29). Coverage gap
disclosed: the specification does not print a chapter-level partition, and the
book does not print sub-topic labels, so sub-topic-to-chapter mapping must be
inferred — it is disclosed here as inferred, not verified. Temporal scope:
CURRENT — AUTHORITATIVE.

### GAP-002 — Chemistry-only content is flagged on both sides, and the flags agree where the pack permits comparison

**Claim:** the specification reserves C-suffix statement numbers for
chemistry-only content, and the book carries CHEMISTRY ONLY flags at both
chapter and chunk level; for solubility, the two machineries describe the same
content.
**Evidence:** the specification's Topic 1 page carries C-suffixed statements —
"1.5C know what is meant by the term solubility in the units g per 100 g of
solvent", "1.6C understand how to plot and interpret solubility curves" and
"1.7C practical: investigate the solubility of a solid in water at a specific
temperature" (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p17); the book's course
structure flags "5 | CHEMICAL FORMULAE, EQUATIONS AND CALCULATIONS PART 1 |
CHEMISTRY ONLY", "9 | METALLIC BONDING | CHEMISTRY ONLY" and "10 ELECTROLYSIS |
CHEMISTRY ONLY" (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 9); and the book's
States-of-matter chapter marks its solubility definition CHEMISTRY ONLY —
"the mass of solute which must dissolve in 100g of solvent at that temperature
to form a saturated solution" (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 43). Temporal scope:
CURRENT — AUTHORITATIVE.

### GAP-003 — The book's solubility question battery operationalizes the specification's C-suffixed solubility statements

**Claim:** the book's chemistry-only solubility material does not stop at
definitions; its question battery drills exactly the skills the specification's
C-suffixed statements 1.6C and 1.7C demand — plotting and interpreting
solubility curves and investigating solubility at specific temperatures —
so no curriculum coverage gap exists for these statements.
**Evidence:** the book's chemistry-only question set asks the student to "Use
these figures to plot a solubility curve, with the temperature on the
horizontal axis and the solubility on the vertical one", to "Determine the
maximum mass of sodium chlorate that will dissolve in 40g of water at 30 °C"
and to find "at what temperature would crystals first appear in the solution"
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 59);
this sits against the specification's "1.6C understand how to plot and
interpret solubility curves" and "1.7C practical: investigate the solubility
of a solid in water at a specific temperature" (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p17). Temporal scope:
CURRENT — AUTHORITATIVE.

### GAP-004 — Unit 3 (Physical chemistry) is the thinnest partition on both sides and the book flags no chemistry-only chapter there

**Claim:** the book's Unit 3 spans roughly 48 printed pages across three
chapters (Energetics, Rates of reaction, Reversible reactions and equilibria),
matching the specification's three-sub-topic Topic 3, and — unlike Unit 1 and
Unit 4 — the course-structure rows for Unit 3 chapters carry no CHEMISTRY ONLY
flag, a visible asymmetry the audit records without asserting a cause.
**Evidence:** the book's course-structure rows read "PHYSICAL CHEMISTRY
19ENERGETICS | 207", "20RATES OF REACTION | 227" and "21 REVERSIBLE REACTIONS
AND EQUILIBRIA" at 240, with none of the three rows carrying the CHEMISTRY
ONLY label that rows in Unit 1 and Unit 4 carry, while "26ALCOHOLS | 287
CHEMISTRY ONLY", "27 CARBOXYLIC ACIDS | 293 CHEMISTRY ONLY" and "28ESTERS |
297 CHEMISTRY ONLY" do carry it (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 10); the specification
prints Topic 3 "Physical chemistry" as the shortest sub-topic list, "(a)
Energetics (b) Rates of reaction (c) Reversible reactions and equilibria"
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p27).
Whether topic 3 carries chunk-level chemistry-only markers is outside this
pack and is disclosed as unverified. Temporal scope: CURRENT — AUTHORITATIVE.

### GAP-005 — The organic chemistry-only chapters concentrate on three functional-group chapters whose specification sub-topics sit adjacent to an unflagged polymers chapter

**Claim:** the book flags exactly three Unit-4 chapters CHEMISTRY ONLY —
Alcohols, Carboxylic acids and Esters — while the specification's Topic 4
sub-topic list places "(e) Alcohols (f) Carboxylic acids (g) Esters" before
"(h) Synthetic polymers"; the book leaves its chapter 29 (Synthetic polymers)
row unflagged, and the audit discloses that the pack does not include the
specification pages printing the statement numbers for sub-topics (e)–(h), so
the statement-level correspondence is recorded as unverified.
**Evidence:** the book's Unit 4 course-structure rows show "26ALCOHOLS | 287
CHEMISTRY ONLY", "27 CARBOXYLIC ACIDS | 293 CHEMISTRY ONLY" and "28ESTERS |
297 CHEMISTRY ONLY" followed by an unflagged "29SYNTHETIC POLYMERS | 302"
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 10);
the specification's Topic 4 page lists "The following sub-topics are covered in
this section. (a) Introduction (b) Crude oil (c) Alkanes (d) Alkenes (e)
Alcohols (f) Carboxylic acids (g) Esters (h) Synthetic polymers"
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p29).
Temporal scope: CURRENT — AUTHORITATIVE.

### GAP-006 — The audit's own evidence boundary: three presence-only sources and three unopened specification pages are disclosed, not silently dropped

**Claim:** this audit's pack can resolve six sources of record, of which the
root-level book intake copy, the sample assessment materials and the examiner
reports enter as identity-presence only, and the specification pages 18–20
that print the statement-level detail for Topic 1 sub-topics (b)–(g) are not
in the pack — both facts bound what this artifact may assert about curriculum
coverage.
**Evidence:** the examiner report of record is identified as "Examiners'
Report June 2019 IGCSE Chemistry 4CH1 1C" (SRC-ER-4CH1,
2019-06/4CH1-1C/er.pdf p1); the topic guide of record is identified as
"TOPIC GUIDE: Chemical bonding Pearson Edexcel International GCSE in Chemistry
(4CH1) and Science (4SD0 and 4SS0) First teaching 2017" (SRC-TL-4CH1,
Chemical-bonding---FINAL.pdf p1); the book's States-of-matter chapter pages
that would pair with specification sub-topic (a) are visible of record
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 9),
while sub-topics (b)–(g) statement pages are absent from the pack and stay
disclosed. Temporal scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-SPEC-4CH1 (the current specification's four topic pages —
17, 21, 22, 27 and 29 — carrying the sub-topic lists and the C-suffixed
statement clusters) and SRC-BOOK-4CH1-SB1 (the parse v3 corpus's course
structure, the chemistry-only chapter flags and the solubility band).
Supplementary: SRC-ER-4CH1, SRC-TL-4CH1, SRC-ROOT-BOOK-COPIES-4CH1 and
SRC-SAMS-4CH1 ride as one-page identity-presence entries and are consumed for
identity claims only. All excerpts are bounded with locators preserved; caps
enforced by the pack builder.

## Limitations / Coverage Gaps

The specification pages that print statement-level detail for Topic 1
sub-topics (b)-(g) — pages 18-20 of the of-record PDF — are outside this pack,
so chapter-to-statement mapping beyond the quoted pairs is disclosed as
unverified. The book side is sampled at the course-structure chunk plus two
chemistry-only solubility chunks; no claim is made about chapter interiors.
The chunk-level chemistry-only marker count is a run-census fact, not a
quoted surface, and is not claimed here.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-009 (BL-009 pass 9) from this artifact's
evidence pack alone; validator of record tools/sib @ 357ace0a; claim QA binds
every citation to a pack excerpt. Research artifact — evidence-backed, not
canonical educational truth.
