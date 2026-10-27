---
sib_protocol: SIB-1.0
artifact_id: CUR-07
artifact_version: 1.1
subject: Chemistry
qualification: International GCSE
specification: 4CH1
curriculum_version: "2017"

research_family: curriculum_intelligence
applicability: REQUIRED

temporal_scope:
  current: true
  legacy: false

source_scope:
  specification: true
  textbook: false
  question_papers: false
  mark_schemes: false
  examiner_reports: false
  supplementary: true

status: GENERATED
generated_by: zai_agent
generated_at: 2026-10-27

provenance:
  source_manifest: "SRC-SPEC-4CH1"
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-015"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "2cb92fe5f56d22f1b231c129a7e0dbc27bf86007"
    syllabai_resources: "d9c944362529a1ef4db481a349a0f33f1f6daf31"
---

# CUR-07 — Terminology & Definitions

## Purpose

This artifact is the terminology law of the CHEMISTRY_4CH1 curriculum intelligence: the
assessment command-word taxonomy of record — all 25 command words with their official
definitions, verbatim — plus the interpretation layer that connects those definitions
to the demand classes CUR-02 classified. Command words are the contract between a
question and a learner: they fix what kind of response earns marks, and every
assessment-facing family (ASM archetypes, MS mark-scheme logic, TUT feedback) inherits
its response-grading vocabulary from this taxonomy. It is a research artifact grounded
on the run's evidence pack; the canonical planes remain authoritative and read-only to
this pipeline.

## Scope

**Covers:** the complete command-word taxonomy of record — 25 words in three
categories (23 main, 1 verb-preceding-command-word, 1 multiple-choice-questions), with
the official definitions verbatim from the validated graph store and the
specification's own Appendix 5 (printed pages 45-46); the functional interpretation of
the taxonomy in four demand tiers (recall, reasoning, quantitative/production,
evaluation); and the bridge to the KNOW_TERM demand class of CUR-02. Temporal scope is
CURRENT — AUTHORITATIVE; no legacy material is used or cited.

**Does not cover:** term definitions from subject content (those live in the
specification statements themselves and the concept store — CUR-02/03), how actual
papers deploy the words (ASM/EXM families' ground), or mark-scheme-specific
application rules. The teaching-corpus command-words document is an identity-only row
in this pack; no claim grounds on its internal text.

## Executive Summary

- The taxonomy of record holds exactly 25 command words — 23 category main, 1
  verb-preceding-command-word ("Analyse the data/graph to explain"), 1
  multiple-choice-questions ("What, Why, Which") — defined verbatim in the validated
  store and in the specification's Appendix 5 (SRC-GRAPH-4CH1, graph/igcse-chemistry/command_words.yaml lines 45-59); (SRC-GRAPH-4CH1, graph/igcse-chemistry/command_words.yaml lines 587-601); (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p51) (RUN-COMPUTED: census.json, command_words.entries; census.json, command_words.category_distribution).
- The recall tier is explicit in the official definitions: "Give/State/Name — all of
  these command words are really synonyms. They generally all require recall of one or
  more pieces of information" (SRC-GRAPH-4CH1, graph/igcse-chemistry/command_words.yaml lines 340-354).
- The reasoning tier is anchored by Explain — "The answer must contain some element of
  reasoning/justification" — and by Deduce, Justify, Suggest and Comment on
  (SRC-GRAPH-4CH1, graph/igcse-chemistry/command_words.yaml lines 317-331); (SRC-GRAPH-4CH1, graph/igcse-chemistry/command_words.yaml lines 134-148).
- The quantitative tier is anchored by Calculate ("Obtain a numerical answer, showing
  relevant working") and Determine ("must have an element that is quantitative")
  (SRC-GRAPH-4CH1, graph/igcse-chemistry/command_words.yaml lines 68-82); (SRC-GRAPH-4CH1, graph/igcse-chemistry/command_words.yaml lines 179-193).

## Main Analysis

### CUR-038 — The taxonomy of record: 25 words, three categories, verbatim

The validated command-word store carries 25 entries, each with a code
(4CH1-CW-*), the command word, a category, and the official definition; the store's
own provenance note records that the words and definitions are verbatim from the
canonical PDF-direct parse of appendix pages 51-52, with the category field a ratified
overlay (SRC-GRAPH-4CH1, graph/igcse-chemistry/command_words.yaml lines 45-59) — store meta. The specification PDF confirms the
verbatim source: Appendix 5 "Command word taxonomy" opens at printed page 45 (PDF
page 51) with the same table (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p51). The category census: 23 main
command words, 1 verb-preceding-command-word ("Analyse the data/graph to explain —
examine the data/graph in detail to provide an explanation"), and 1
multiple-choice-questions entry ("What, Why, Which — direct command words used for
multiple-choice questions") (SRC-GRAPH-4CH1, graph/igcse-chemistry/command_words.yaml lines 565-579); (SRC-GRAPH-4CH1, graph/igcse-chemistry/command_words.yaml lines 587-601) (RUN-COMPUTED: census.json, command_words.entries; census.json, command_words.category_distribution). Every definition quoted in this
artifact is verbatim from the store's definition fields; paraphrase is not used
anywhere in this record set, because a paraphrased command-word definition would
silently rewrite the assessment contract.

### CUR-039 — The recall tier: state the fact, nothing more

Four definitions define the recall contract. Give/State/Name: "All of these command
words are really synonyms. They generally all require recall of one or more pieces of
information" (SRC-GRAPH-4CH1, graph/igcse-chemistry/command_words.yaml lines 340-354). Identify: "Usually requires some key
information to be selected from a given stimulus/resource" (SRC-GRAPH-4CH1, graph/igcse-chemistry/command_words.yaml lines 385-399). Predict: "Give an expected result" (SRC-GRAPH-4CH1, graph/igcse-chemistry/command_words.yaml lines 453-467). Show
that: "Verify the statement given in the question" (SRC-GRAPH-4CH1, graph/igcse-chemistry/command_words.yaml lines 475-489).
Two adjacent definitions bound the tier: State what is meant by — "When the meaning of
a term is expected but there are different ways for how these can be described" —
which is definitional recall with wording freedom (SRC-GRAPH-4CH1, graph/igcse-chemistry/command_words.yaml lines 520-534);
and Give a reason/reasons — "When a statement has been made and the requirement is
only to give the reason(s) why" — recall of a cause, not construction of an argument
(SRC-GRAPH-4CH1, graph/igcse-chemistry/command_words.yaml lines 363-377). The interpretation law for downstream families:
these words cap the demanded depth; an ASM archetype that scores a
Give/State/Name item as if it demanded justification has mis-graded the contract.

### CUR-040 — The reasoning tier: justification is the product

Explain anchors the tier: "An explanation requires a justification/exemplification of
a point. The answer must contain some element of reasoning/justification"
(SRC-GRAPH-4CH1, graph/igcse-chemistry/command_words.yaml lines 317-331). Deduce raises the input stakes — "Draw/reach
conclusion(s) from the information provided" — the conclusion must come FROM the
stimulus, not from memory alone (SRC-GRAPH-4CH1, graph/igcse-chemistry/command_words.yaml lines 134-148). Justify: "Give
evidence to support (either the statement given in the question or an earlier
answer)" — evidence-bearing support of a claim already in play (SRC-GRAPH-4CH1, graph/igcse-chemistry/command_words.yaml lines 407-421). Comment on: "Requires the synthesis of a number of variables from
data/information to form a judgement" (SRC-GRAPH-4CH1, graph/igcse-chemistry/command_words.yaml lines 90-104). Suggest:
"Use your knowledge to propose a solution to a problem in a novel context" — the
novelty flag distinguishes it from recall (SRC-GRAPH-4CH1, graph/igcse-chemistry/command_words.yaml lines 543-557). Describe
sits deliberately between the tiers — "To give an account of something. Statements in
the response need to be developed, as they are often linked but do not need to include a justification or reason" — development without justification is the exact boundary between
describe and explain (SRC-GRAPH-4CH1, graph/igcse-chemistry/command_words.yaml lines 156-170). Discuss is the multi-part
member: identify the issue, explore all aspects, then the store's definition
continues in bullet form (SRC-GRAPH-4CH1, graph/igcse-chemistry/command_words.yaml lines 225-239). This tier maps one-to-one
onto CUR-02's UNDERSTAND_RELATION and EXPLAIN_HOW classes — the store's demanded
substances and the official definitions are two views of the same contract.

### CUR-041 — The quantitative and production tier: working, graphs, diagrams

Calculate: "Obtain a numerical answer, showing relevant working" — the working is
part of the demand, not presentation polish (SRC-GRAPH-4CH1, graph/igcse-chemistry/command_words.yaml lines 68-82).
Determine: "The answer must have an element that is quantitative from the stimulus
provided, or must show how the answer can be reached quantitatively" (SRC-GRAPH-4CH1, graph/igcse-chemistry/command_words.yaml lines 179-193). Estimate: "Find an approximate value, number or quantity from a
diagram/given data or through a calculation" (SRC-GRAPH-4CH1, graph/igcse-chemistry/command_words.yaml lines 271-285). The
diagram/graph family splits by precision: Draw — "Produce a diagram either using a
ruler or freehand"; Plot — "Produce a graph by marking points accurately on a grid
from data that is provided and then draw a line of best fit through these points. A
suitable scale and appropriately labelled axes must be included if these are not
provided in the question"; Sketch — "Produce a freehand drawing. For a graph, this
would need a line and labelled axes with important features indicated. The axes are
not scaled" (SRC-GRAPH-4CH1, graph/igcse-chemistry/command_words.yaml lines 249-263); (SRC-GRAPH-4CH1, graph/igcse-chemistry/command_words.yaml lines 429-443); (SRC-GRAPH-4CH1, graph/igcse-chemistry/command_words.yaml lines 497-511). Complete — "Requires the completion of a
table/diagram" — and Add/Label — "Requires the addition or labelling of a stimulus
material given in the question, for example labelling a diagram or adding units to a
table" — complete the production set (SRC-GRAPH-4CH1, graph/igcse-chemistry/command_words.yaml lines 112-126); (SRC-GRAPH-4CH1, graph/igcse-chemistry/command_words.yaml lines 45-59). Design — "Plan or invent a procedure from existing
principles/ideas" — is the constructive member, bridging toward the evaluation tier
(SRC-GRAPH-4CH1, graph/igcse-chemistry/command_words.yaml lines 203-217). These definitions operationalize CUR-02's
REPRESENT_DIAGRAM and CALCULATE classes at exam-facing grain.

### CUR-042 — The evaluation apex and the MCQ tier

Evaluate is the taxonomy's apex: "Review information (e.g. data, methods) then bring
it together to form a conclusion, drawing on evidence including strengths, weaknesses, alternative actions, relevant data or information" — the store's window carries the definition in full, and the official Appendix 5 table is the extraction source of record
(SRC-GRAPH-4CH1, graph/igcse-chemistry/command_words.yaml lines 293-307); (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p51). The store's provenance block records the deterministic Appendix 5 parse (spec_issue 3), so the definition is verifiable against the store window and the official table cited. The multiple-choice tier is its own category, "What, Why, Which": "Direct command words used for multiple-choice questions" — the paper-format signature that
distinguishes MCQ demand grammar from open-response grammar (SRC-GRAPH-4CH1, graph/igcse-chemistry/command_words.yaml lines 587-601). The verb-preceding category member ("Analyse the data/graph to explain")
shows the taxonomy handling compound stems where a processing verb precedes the
command word (SRC-GRAPH-4CH1, graph/igcse-chemistry/command_words.yaml lines 565-579). For ASM archetype work, these three
non-main entries are the formatting signals: an MCQ archetype keys on
What/Why/Which; a data-processing archetype keys on the compound stem.

### CUR-043 — The bridge to the demand classes and the consumption law

The taxonomy connects to CUR-02's class census: KNOW_TERM (60 statements of 181) is
the statement-grain expression of the recall tier; UNDERSTAND_RELATION (45) and
EXPLAIN_HOW (9) express the reasoning tier; CALCULATE (12) and REPRESENT_DIAGRAM
(18) express the quantitative/production tier (RUN-COMPUTED: census.json,
command_kinds.guide_class_distribution). The bridge is lawful but not mechanical:
command words grade QUESTIONS, guide classes classify STATEMENTS — a
UNDERSTAND_RELATION statement can generate a Describe question in one paper and an
Explain question in another, which is precisely the ASM family's measurement to make,
not this artifact's. The consumption law for every downstream family: quote command
words and their definitions verbatim from this taxonomy (or the official appendix);
never re-define a command word in family-local prose; when a question uses a word
outside the 25, that is a finding to disclose, not a definition to invent.

## Evidence / Source Basis

- **CURRENT — AUTHORITATIVE:** SRC-SPEC-4CH1 — official specification PDF, Issue 3
  (Appendix 5 "Command word taxonomy", PDF pages 51-52, printed 45-46), sha1 of
  record 3ad641b7c60b314fa3b10680feda30bf56280a53, verified at run preflight.
- **CURRENT — AUTHORITATIVE:** SRC-GRAPH-4CH1 — validated curriculum graph:
  command_words.yaml (25 entries, definitions verbatim from the canonical PDF-direct
  parse, category ratified overlay), verified at run preflight. Read-only plane for
  this pipeline.
- **CURRENT — AUTHORITATIVE / SUPPLEMENTARY:** SRC-TL-4CH1 — the board's
  command-words teaching document as an identity-only row (DOCX, text not extracted
  in this run).
- **CURRENT — ASSESSMENT EVIDENCE (specimen):** SRC-SAMS-4CH1 — page 1 identity-only
  row.
- **RUN-COMPUTED:** census.json — deterministic counts over the graph stores of
  record; verified by the run's evidence-claim QA.

## Limitations / Coverage Gaps

- The Evaluate definition is truncated at the pack's excerpt cap in the graph-store
  window; the full official sentence is verifiable on the cited appendix page, and
  this artifact quotes only the in-pack portion plus the pointer.
- The taxonomy grades command words as published; how actual sessions deployed them
  (frequency, marks, pairing with contexts) is the ASM/EXM families' ground and is
  deliberately absent here.
- The DOCX teaching-corpus command-words document is identity-only; any difference
  between its guidance and the official definitions is unexamined in this run.
- One category member's name is itself a compound stem ("Analyse the data/graph to
  explain"); consumers keying on single-word lookups must handle compound entries.
- Subject-level terminology (the chemical vocabulary itself) is out of scope: it
  lives in the specification statements and concept nodes (CUR-02/03).

## Research Status

status: GENERATED (research artifact; not educational truth, not canonical curriculum
truth). Generated by the SIB-GEN batch run SIB-CHEMISTRY_4CH1-RUN-002 under the
provider-neutral pipeline (BL-008 wave 1, protocol §4 pass 2), grounded exclusively on
the run's CUR-07 evidence pack (pack sha256 of record in the run manifest) plus the
run's deterministic census annex. Current/legacy separation: fully CURRENT; no legacy
claims. Determinism: content fingerprint of this artifact is recorded in the run
manifest; regeneration produces a new artifact_version.
