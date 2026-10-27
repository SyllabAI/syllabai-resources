---
sib_protocol: SIB-1.0
artifact_id: GAP-07
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
  supplementary: true

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

# GAP-07 — Tutor Knowledge Gaps

## Purpose

This artifact audits tutor-facing knowledge coverage for the Pearson Edexcel
International GCSE in Chemistry (4CH1): what the of-record corpus supplies a
tutor — command-word tables, practical-question guidance, topic guides — and
where the tutor's knowledge base has holes. It inventories the tutor surfaces
of record, cross-reads the duplicated ones, and discloses every surface a
tutor would need that the corpus does not carry. Gaps stay disclosed, never
filled.

## Scope

**Covers:** the book's tutor-facing appendices (command words, practical
questions); the board's topic guides and core-practical guide of record; the
command-word duplication between specification and book; and the declared
scope of the book itself as a tutor-planning surface.

**Out of scope:** misconception response content (GAP-04) and research
priorities (GAP-08).

## Executive Summary

The tutor's knowledge base of record is anchored by the book's own appendices
— a full command-word table and a guide to practical questions — and by the
board's teaching-and-learning corpus: exactly two topic guides (chemical
bonding and chemical equilibria) plus the core-practical guide. The audit
finds the command-word machinery duplicated across specification and book with
compatible definitions, a declared book scope that spans two specifications
(Chemistry and Science Double Award), and a topic-guide corpus that covers two
of the book's four units — the clearest tutor-knowledge gap of record. The
core-practical guide enters the pack only through its solubility page, so
practical-by-practical tutor coverage is disclosed as unaudited beyond it.

## Main Analysis

### GAP-037 — The book's tutor-facing appendices are a two-part apparatus: command words and a practical-questions guide

**Claim:** the book of record closes with two tutor-facing appendices — a
command-word table defining the assessment vocabulary and a guide to
practical questions — and both are written in examination-facing language, so
a tutor's core briefing surfaces exist inside the book itself.
**Evidence:** the course-structure table lists "APPENDIX B: COMMAND WORDS |
321" and "APPENDIX C: A GUIDE TO PRACTICAL QUESTIONS | 322" (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 8); Appendix C opens "This
appendix is designed to help you better understand the practical work in your
study, and also to give you guidance on how to answer the practical-based
questions in your International GCSE Chemistry papers" (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 1075). Temporal scope:
CURRENT — AUTHORITATIVE.

### GAP-038 — The command-word machinery is duplicated between specification Appendix 5 and book Appendix B, and the definitions agree where the pack permits comparison

**Claim:** the specification's command-word taxonomy and the book's command
word appendix carry compatible definitions — Describe, Calculate, Deduce
appear in both — which gives tutors a cross-check surface; the audit finds no
contradiction of record but also no adjudicated reconciliation table, which
stays disclosed as unverified beyond the quoted overlaps.
**Evidence:** the specification's Appendix 5 reads "The following table lists
the command words used in the external assessments" with "Describe To give an
account of something. Statements in the response need to be developed, as they
are often linked" and "Deduce Draw/reach conclusion(s) from the information
provided" (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p51); the book's Appendix
B defines "Describe | Give an account of something. Statements in the response
need to be developed, as they are often linked, but do not need to include a
justification or reason." and "Deduce | Draw/reach conclusion(s) from the
information provided." (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 1071). Temporal scope:
CURRENT — AUTHORITATIVE.

### GAP-039 — The book's command-word table carries rows the specification page of record does not show, extending the tutor's briefing surface

**Claim:** the book's Appendix B includes rows — Estimate, Evaluate,
State-what-is-meant-by, Suggest, verb-preceded commands and multiple-choice
wording — that the specification's Appendix 5 page of record does not print
in this pack, so the book is the richer command-word surface of record and
the pack cannot verify whether the specification carries those rows elsewhere.
**Evidence:** the book defines "Estimate | Find an approximate value, number
or quantity from a diagram/given data or through a calculation." and
"Evaluate | Review information (e.g. data, methods) then bring it together to
form a conclusion" (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 1072), plus "Suggest |
Use your knowledge to propose a solution to a problem in a novel context." and
the multiple-choice row "What, why | Direct command words used for
multiple-choice questions." (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 1074); the specification
page of record prints its table without those rows visible (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p51). Temporal scope:
CURRENT — AUTHORITATIVE.

### GAP-040 — The topic-guide corpus of record covers two of the book's four units, which is the clearest tutor-knowledge gap of record

**Claim:** the teaching-and-learning corpus of record carries exactly two
chemistry topic guides — Chemical bonding and Chemical equilibria — against
the book's four-unit architecture, so a tutor seeking board-level topic
guidance for inorganic or organic chemistry has no of-record surface, a gap
this artifact discloses rather than substitutes for.
**Evidence:** the two guides identify themselves on their covers — "TOPIC
GUIDE: Chemical bonding Pearson Edexcel International GCSE in Chemistry (4CH1)
and Science (4SD0 and 4SS0) First teaching 2017" and "TOPIC GUIDE: Chemical
equilibria Pearson Edexcel International GCSE in Chemistry (4CH1) and Science
(4SD0 and 4SS0) First teaching 2017" (SRC-TL-4CH1,
Chemical-bonding---FINAL.pdf p1; Chemical-equilibrium---FINAL.pdf p1); the
book's four units are "UNIT 1: PRINCIPLES OF CHEMISTRY", "UNIT 2: INORGANIC
CHEMISTRY", "UNIT 3: PHYSICAL CHEMISTRY" and "UNIT 4: ORGANIC CHEMISTRY"
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 8).
Temporal scope: CURRENT — AUTHORITATIVE.

### GAP-041 — The core-practical guide supplies per-practical tutor coaching — questions to ask, skills, maths links — but enters this pack only for solubility

**Claim:** the board's core-practical guide provides a per-practical tutoring
template — "Questions you could ask to enhance learning", skills covered,
maths skills and alternative experiments — and the pack exhibits that template
for the solubility practical only, so the template's coverage of the other
core practicals is disclosed as unaudited rather than confirmed.
**Evidence:** the solubility page of record reads "Questions you could ask to
enhance learning and focus your students on important aspects of the
practical: • Why does increasing the temperature usually affect the solubility
of solids?" and lists "Skills that are covered in the practical: • Measuring
mass • Use of a Bunsen burner" with "Maths skills: 1A Recognise and use
numbers in decimal form" (SRC-TL-4CH1,
biology-chemistry-physics-core-practical-guide.pdf p73); the book's Appendix C
safety page pairs with it — "The obvious precaution is to wear eye
protection." with the mark-earning "explain" requirement spelled out
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 1077).
Temporal scope: CURRENT — AUTHORITATIVE.

### GAP-042 — The book declares a two-specification scope, so tutor planning must split Chemistry-only from Double Award content — and the book claims the split apparatus

**Claim:** the book of record declares itself written for two specifications —
the Chemistry specification and the Science Double Award specification — and
states that it "clearly indicates which content is in the Chemistry
examination", so tutor knowledge must include the split discipline; the audit
records the declared apparatus but does not audit the split page-by-page,
which stays disclosed as unaudited.
**Evidence:** the book states "This book is written for students following
the Pearson Edexcel International GCSE (9-1) Chemistry specification and the
Edexcel International GCSE (9–1) Science Double Award specification" and "The
book clearly indicates which content is in the Chemistry examination"
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 11);
it also declares its EAL grading and command-word support — "The language
throughout this textbook is graded for speakers of English as an additional
language (EAL)" and "A list of command words, also at the back of the book"
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 11);
the examiner-report presence source identifies as "Examiners' Report June 2019
IGCSE Chemistry 4CH1 1C" (SRC-ER-4CH1, 2019-06/4CH1-1C/er.pdf p1). Temporal
scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-BOOK-4CH1-SB1 (the book's appendices of record — course
structure, About-this-book, command-word appendix and practical-questions
guide) and SRC-SPEC-4CH1 (the command-word taxonomy page, p51, and the
suggested-practicals appendix, p53). Supplementary: SRC-TL-4CH1 (the two topic
guide covers and the core-practical guide's solubility page) is cited;
SRC-ER-4CH1, SRC-ROOT-BOOK-COPIES-4CH1 and SRC-SAMS-4CH1 ride as one-page
identity-presence entries. All excerpts are bounded with locators preserved;
caps enforced by the pack builder.

## Limitations / Coverage Gaps

The core-practical guide enters this pack at its solubility page only, so the
per-practical tutoring template is evidenced once; the other practicals'
pages are unaudited here. The specification page of record shows its
command-word table without the rows the book carries; whether the
specification prints those rows on an unheld page is disclosed as unverified.
No claim is made about tutor surfaces outside the cited pages.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-009 (BL-009 pass 9) from this artifact's
evidence pack alone; validator of record tools/sib @ 357ace0a; claim QA binds
every citation to a pack excerpt. Research artifact — evidence-backed, not
canonical educational truth.
