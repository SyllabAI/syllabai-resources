---
sib_protocol: SIB-1.0
artifact_id: CUR-03
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

# CUR-03 — Concept Taxonomy

## Purpose

This artifact is the taxonomy of the CHEMISTRY_4CH1 concept store: what a concept node
IS in the validated concept graph, what families of nodes exist, how nodes anchor to
specification points, what the alias vocabulary carries, and — critically — what
provenance tier the store's own meta block declares for this content. CUR-01 fixed the
qualification skeleton and CUR-02 fixed the demand grammar of the specification
statements; CUR-03 describes the mid-grain layer between them: the 193 concept and
misconception nodes through which explanation, remediation and tutoring content can be
indexed. It is a research artifact grounded on the run's evidence pack; the canonical
knowledge graph of SyllabAI remains authoritative, and this pipeline treats it
read-only.

## Scope

**Covers:** the concept store's node taxonomy (node code space, family split between
CONCEPT and MISCONCEPTION, title/alias structure, spec-point anchoring with the CORE
role), the store's own published census (193 nodes: 167 concepts, 26 misconceptions;
211 PART_OF edges, 277 semantic edges), the provenance-tier law declared in the
store's meta block (AI_SUGGESTED default, operator-only HUMAN_VALIDATED gate), and
in-pack exemplars spanning all four topics. Temporal scope is CURRENT — AUTHORITATIVE;
no legacy material is used or cited.

**Does not cover:** the edge semantics between concepts (CUR-04), prerequisite
structure (CUR-05), cross-topic connectivity (CUR-06), or any claim that the concept
store IS the canonical knowledge graph. The store's embedded evidence quotes reference
external note corpora that are NOT among this library's resolved sources; those
reference pointers are recorded as pointers, and no claim here grounds on their
content.

## Executive Summary

- The concept store holds 193 nodes — 167 CONCEPT and 26 MISCONCEPTION — per its own
  meta census (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 251-265), matching the run census (RUN-COMPUTED:
  census.json, concepts.nodes).
- Every concept node carries a code in the store's own namespace (4CH1-CON-* /
  4CH1-MIS-*), a title, an alias list, and one or more spec-point anchors with role
  CORE (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 263-277).
- The store declares provenance_default: AI_SUGGESTED with an operator-only
  validation gate — "no promotion from generation; HUMAN_VALIDATED is operator-only"
  (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 251-265). This artifact therefore treats every node as
  research content, never as validated curriculum truth.
- The MISCONCEPTION family nodes are pattern-classified (in-pack exemplars all carry
  pattern_class: WRONG_ANSWER_PATTERN) and ground on mark-scheme evidence rows
  (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 7542-7556); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 7591-7605).

## Main Analysis

### CUR-010 — The node taxonomy: what a concept node is

A concept node is a machine-readable unit of subject understanding with five
load-bearing fields: a code in the store's namespace, a family (CONCEPT or
MISCONCEPTION), a title stating the concept's content in one sentence, an alias list,
and spec-point anchors (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 263-277). The exemplar node
4CH1-CON-ACID-ALKALI-IONS shows the shape completely: family CONCEPT, title "Acids as
hydrogen-ion sources and alkalis as hydroxide-ion sources in aqueous solution", three
aliases ("hydrogen ions in solution", "hydroxide ions in solution", "what makes a
solution acidic or alkaline"), anchored at 4CH1-2.31 with role CORE
(SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 263-277). Node codes are stable identifiers (4CH1-CON-* for
concepts, 4CH1-MIS-* for misconceptions), and each node carries creation metadata and
a damage_flags field (empty in all in-pack exemplars) (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 360-374); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 860-874). The store's own meta block publishes its
census: 193 nodes, 167 concepts, 26 misconceptions, 211 PART_OF edges and 277
semantic edges (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 251-265) — the same totals the run census
computes over the store (RUN-COMPUTED: census.json, concepts.nodes;
census.json, concept_edges.edges).

### CUR-011 — Concepts are specification-anchored, not free-floating

Every in-pack concept node anchors to at least one specification point with an
explicit role field (CORE in all in-pack exemplars): ACID-ALKALI-IONS → 2.31;
ACID-REACTIONS → 2.37; ANION-TESTS → 2.48; CATION-TESTS → 2.47; COMBUSTION-O2 →
2.11; COVALENT-BOND → 1.44; CRUDE-OIL → 4.7; ELECTROLYSIS → 1.58C;
ELECTRONIC-CONFIGURATION → 1.19; ETHANOL-OXIDATION → 4.31C; EXO-ENDO → 3.1;
FRACTIONAL-DISTILLATION → 1.10; OX-RED-AGENTS → 2.20 (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 263-277); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 360-374); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 860-874); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 1553-1567); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 1869-1883); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 2102-2116); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 2272-2286); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 2733-2747); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 2779-2793); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 3246-3260); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 3312-3326); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 3597-3611); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 5761-5775). The anchors reach across the whole specification: 1.10/1.19/1.44/1.58C in
S1, 2.11/2.20/2.31/2.37/2.47/2.48 in S2, 3.1 in S3, 4.7/4.31C in S4 — the taxonomy's
coverage follows the topics the official content section defines (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p15) (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p17). This anchoring law is what makes the concept store
usable downstream: every explanation, misconception or remediation indexed by a node
inherits a traceable path to official curriculum wording through the anchor.

### CUR-012 — Titles state substance; aliases carry the retrieval vocabulary

Node titles are substantive one-sentence statements of the concept, not labels:
COVALENT-BOND's title embeds the mechanism ("shared pair of electrons; electrostatic
attraction between the shared pair and the nuclei"), ELECTROLYSIS's title carries the
scope ("decomposition by direct current: molten binary compounds and their element
products, using inert electrodes"), ELECTRONIC-CONFIGURATION's title carries both the
content and the consequence ("shells 2, 8, 8; configuration and Periodic Table
position") (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 2102-2116); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 2733-2747); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 2779-2793). Alias lists are learner-language surfaces:
CATION-TESTS aliases include the phenomenology ("Fe2+ pale green precipitate", "Cu2+
blue precipitate", "NH4+ test"), ANION-TESTS aliases include the reagent shorthand
("acidified silver nitrate halide test", "barium chloride sulfate test", "carbonate
limewater test") (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 1553-1567); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 860-874).
Downstream retrieval and tutoring layers should treat aliases as first-class
vocabulary: they are how a learner's phrasing maps onto a canonical node.

### CUR-013 — The MISCONCEPTION family: pattern-classified, mark-scheme-grounded

The store's second node family encodes documented error patterns rather than
understanding. All eight in-pack MISCONCEPTION exemplars carry pattern_class:
WRONG_ANSWER_PATTERN and ground on MARK_SCHEME-kind evidence rows: bond-energy
counting errors ("Deduct 1 mark for each mistake"), the catalystSpeed fallacy ("MAX 1
if any reference to particles gaining energy or moving more quickly"), the cm3→dm3
conversion failure ("an answer of 10(.0) for 1 mark (i.e. failing to divide by
1000)"), the covalent-bonds-broken-on-melting error ("Any reference to bonds between
molecules" is penalised), evaporating-to-dryness ("If evaporated to dryness then award
no marks for whole question"), the CuO colour error ("black"), the neutralisation
endpoint error ("temperature goes down/stops rising/stays constant"), and the J-vs-kJ
enthalpy unit error (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 7542-7556); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 7591-7605); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 7635-7649); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 7673-7687); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 7718-7732); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 7755-7769); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 7795-7809); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 7843-7857). Several nodes also carry
remediation_evidence rows pointing at teaching notes (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 7635-7649); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 7718-7732). The taxonomy consequence: the concept
store already carries an error-model layer alongside its understanding layer, and the
MIS artifact family (misconception atlases etc.) should index through these nodes
rather than re-inventing a parallel error taxonomy. This artifact records the
taxonomy; the evidence quotes' own provenance (embedded mark-scheme extracts and
external note files) belongs to the nodes, and the external files are NOT resolved
sources of this library — their content is cited here only as the nodes' embedded
evidence, never independently.

### CUR-014 — Provenance tier: AI_SUGGESTED by default, operator-gated above

The store's meta block is explicit: provenance_default: AI_SUGGESTED, and the
validation gate is "operator review (pilot: graph/reports/C11_PILOT_REVIEW_SHEET.md;
batch 1: … BATCH1_REVIEW_SHEET.md; batch 2: … BATCH2_REVIEW_SHEET.md) — no promotion
from generation; HUMAN_VALIDATED is operator-only" (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 251-265).
The run census independently confirms the tier distribution: all 193 concept nodes
stand at SUGGESTED, while the edge store mixes HUMAN_VALIDATED (389), SUGGESTED (97)
and REVIEW_REQUIRED (2) tiers (RUN-COMPUTED: census.json, concepts.validation_distribution;
census.json, concept_edges.validation_distribution). The taxonomy consequence is a
hard boundary for every downstream consumer: concept nodes are research scaffolding —
suitable for retrieval, explanation drafting and tutoring texture — but they are not
operator-validated curriculum truth, and no pipeline step may promote them.

### CUR-015 — Coverage shape: all four topics, unevenly

The in-pack exemplars span all four topics — S1 (separation techniques 1.10, electronic
configuration 1.19, covalent bonding 1.44, electrolysis 1.58C), S2 (combustion in
oxygen 2.11, oxidation/reduction 2.20, acids and alkalis 2.31, acid reactions 2.37,
cation and anion tests 2.47/2.48), S3 (exothermic/endothermic 3.1) and S4 (crude oil
4.7, ethanol oxidation 4.31C) (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 3597-3611); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 2779-2793); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 2102-2116); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 2733-2747); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 1869-1883); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 5761-5775); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 263-277); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 360-374); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 1553-1567); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 860-874); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 3312-3326); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 2272-2286); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 3246-3260). The official topic structure the
anchors hang from is the specification's own four-topic content section
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p15). The exemplar set is deliberately S1/S2-weighted (the store's
file order and the pack's bounded excerpt caps concentrate there), and the run census
carries the full 193-node store for exhaustive coverage questions — this artifact
claims the coverage SHAPE (all four topics present, S1/S2 densest in the sampled
grain), not uniform per-topic node counts.

### CUR-016 — What this taxonomy is not

The concept store is not the canonical knowledge graph. The canonical planes
(SpecPoints, knowledge graph, mastery, assessment identity) remain the authoritative
curriculum truth of SyllabAI; this store is a research-layer index whose own meta
block demotes it to AI_SUGGESTED with an operator-only promotion gate
(SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 251-265). Nothing in this artifact writes to, redefines, or
overrides any canonical plane: the pipeline's relationship to the graph is read-only
anchoring. Consumers should also not confuse node coverage with statement coverage —
193 nodes index the specification's 182 statements plus cross-cutting ideas, but the
mapping is many-to-many (a node anchors to one or more spec points; a spec point may
underlie several nodes), and the authoritative statement list remains the
specification-point store of CUR-02 (RUN-COMPUTED: census.json,
specification_points.total).

## Evidence / Source Basis

- **CURRENT — AUTHORITATIVE:** SRC-SPEC-4CH1 — official specification PDF, Issue 3
  (pages 15, 17 in the evidence pack), sha1 of record
  3ad641b7c60b314fa3b10680feda30bf56280a53, verified at run preflight.
- **CURRENT — AUTHORITATIVE:** SRC-GRAPH-4CH1 — validated curriculum graph:
  concepts.yaml (193 nodes with meta census and provenance law), verified at run
  preflight. Read-only plane for this pipeline. The nodes' embedded evidence rows
  (mark-scheme extracts under scripts/c11_evidence/, external revision-note files)
  are pointers recorded by the store; those files are not resolved sources of this
  library and nothing here grounds on them independently.
- **CURRENT — AUTHORITATIVE / SUPPLEMENTARY:** SRC-TL-4CH1 — Getting Started Guide
  (page 3) as identity/context row.
- **CURRENT — ASSESSMENT EVIDENCE (specimen):** SRC-SAMS-4CH1 — page 1 identity-only
  row; never cited as session evidence.
- **RUN-COMPUTED:** census.json — deterministic counts over the graph stores of
  record; verified by the run's evidence-claim QA.

## Limitations / Coverage Gaps

- The pack carries 24 bounded excerpts of a 193-node store (15 CONCEPT + 8
  MISCONCEPTION + 1 meta); per-topic node counts beyond the sampled grain rest on the
  RUN-COMPUTED census.
- All concept nodes stand at provenance tier SUGGESTED; nothing here is
  operator-validated content, and the operator review sheets referenced by the store's
  meta block are outside this library's resolved sources.
- The MISCONCEPTION nodes' evidence quotes embed mark-scheme text whose parent papers
  are not in this pack; the quotes are recorded as the nodes' own evidence pointers.
- Alias and title fields are store-authored research text, not official wording;
  official wording lives in the specification-point store (CUR-02) and the
  specification PDF.
- No claim is made about node completeness against the specification: the store's own
  census is the coverage of record.

## Research Status

status: GENERATED (research artifact; not educational truth, not canonical curriculum
truth). Generated by the SIB-GEN batch run SIB-CHEMISTRY_4CH1-RUN-002 under the
provider-neutral pipeline (BL-008 wave 1, protocol §4 pass 2), grounded exclusively on
the run's CUR-03 evidence pack (pack sha256 of record in the run manifest) plus the
run's deterministic census annex. Current/legacy separation: fully CURRENT; no legacy
claims. Determinism: content fingerprint of this artifact is recorded in the run
manifest; regeneration produces a new artifact_version.
