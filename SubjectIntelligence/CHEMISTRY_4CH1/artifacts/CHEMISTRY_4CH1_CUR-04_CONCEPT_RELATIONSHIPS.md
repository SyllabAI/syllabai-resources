---
sib_protocol: SIB-1.0
artifact_id: CUR-04
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

# CUR-04 — Concept Relationships

## Purpose

This artifact is the relationship layer of the CHEMISTRY_4CH1 concept store: the edge
vocabulary through which concepts, misconceptions and specification points connect.
CUR-03 described what the nodes are; CUR-04 describes how they link — composition
(PART_OF), dependency (REQUIRES_PREREQUISITE), explanation (EXPLAINED_BY), association
(RELATED_TO), confusion (COMMONLY_CONFUSED_WITH), error modeling (MISCONCEPTION_OF and
WRONG_ANSWER_PATTERN) and remediation (REMEDIATED_BY) — with in-pack exemplars for
every kind, the direction conventions, and the per-edge provenance law. Every
downstream family that sequences learning (CUR-05 prerequisites), diagnoses errors
(MIS) or plans remediation (TUT/PED) consumes the relationships classified here. It is
a research artifact grounded on the run's evidence pack; the canonical planes remain
authoritative and read-only to this pipeline.

## Scope

**Covers:** the concept-edge store's eight-relation vocabulary as declared in its meta
block and observed across 59 in-pack edge windows spanning all eight kinds; the edge
record shape (source, relation, target, role, evidence, per-edge provenance); the
direction conventions; and the validation-tier distribution across the 488 edges of
record. Temporal scope is CURRENT — AUTHORITATIVE; no legacy material is used or
cited.

**Does not cover:** the spec-point-grain prerequisite store (CUR-05's ground), the
cross-topic synthesis (CUR-06), or node definitions themselves (CUR-03). Evidence
quotes embedded in edge rows reference external note corpora that are not resolved
sources of this library; they are recorded as the edges' own pointers, and no claim
here grounds on their content independently.

## Executive Summary

- The edge vocabulary of record has eight relations: PART_OF (211 edges),
  REQUIRES_PREREQUISITE (209), REMEDIATED_BY (26), WRONG_ANSWER_PATTERN (24),
  EXPLAINED_BY (12), RELATED_TO (2), COMMONLY_CONFUSED_WITH (2), MISCONCEPTION_OF (2)
  — the store meta declares the V2 enum plus the frozen "triple distinction" of
  COMMONLY_CONFUSED_WITH, WRONG_ANSWER_PATTERN and MISCONCEPTION_OF
  (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 254-268) (RUN-COMPUTED: census.json, concept_edges.relation_distribution).
- Every edge carries evidence rows (kind NOTE or MARK_SCHEME with file + quote) and a
  per-edge provenance block (tier, model_version, extraction_pass)
  (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 13354-13368).
- Validation tiers across the store: HUMAN_VALIDATED 389, SUGGESTED 97,
  REVIEW_REQUIRED 2 of 488 edges (RUN-COMPUTED: census.json,
  concept_edges.validation_distribution); the meta gate remains operator-only.
- The error-modeling triple is operational in-pack: a misconception node links to the
  concept it misunderstands (MISCONCEPTION_OF), to the answer pattern examiners
  penalise (WRONG_ANSWER_PATTERN, mark-scheme-grounded), and to the concept that
  repairs it (REMEDIATED_BY) (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 13499-13513); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 13549-13563); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 14150-14164).

## Main Analysis

### CUR-017 — The eight-relation vocabulary of record

The store's meta block declares the edge vocabulary: "V2 knowledge_edges enum +
COMMONLY_CONFUSED_WITH + WRONG_ANSWER_PATTERN (frozen §8A.11 triple distinction; V2
projection documented in C11_ARCHITECTURE.md §13)" (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 254-268).
The enum's live values are PART_OF, REQUIRES_PREREQUISITE, RELATED_TO,
MISCONCEPTION_OF, EXPLAINED_BY, REMEDIATED_BY (the V2 knowledge_edges set), extended
by COMMONLY_CONFUSED_WITH and WRONG_ANSWER_PATTERN. The store realizes all eight:
211 PART_OF, 209 REQUIRES_PREREQUISITE, 26 REMEDIATED_BY, 24 WRONG_ANSWER_PATTERN,
12 EXPLAINED_BY, 2 each of RELATED_TO, COMMONLY_CONFUSED_WITH and MISCONCEPTION_OF —
488 edges in total (RUN-COMPUTED: census.json, concept_edges.relation_distribution;
census.json, concept_edges.edges). The in-pack exemplars below instantiate every
kind. The "triple distinction" language matters for downstream consumers: confusing a
learner error (WRONG_ANSWER_PATTERN), a misconception's object (MISCONCEPTION_OF) and
a benign confusion pair (COMMONLY_CONFUSED_WITH) is exactly the modeling mistake the
frozen distinction exists to prevent.

### CUR-018 — PART_OF: concept-to-specification composition

At concept grain, PART_OF attaches a concept to the specification point it composes:
exemplar 4CH1-CON-ANION-TESTS PART_OF 4CH1-2.48 with role CORE, evidenced by note
rows ("Negatively charged non-metal ions are known as anions") (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 944-958). This is the edge-side view of the node anchoring CUR-011 described:
211 PART_OF edges wire the 167 concept nodes into the official statement space
(RUN-COMPUTED: census.json, concept_edges.relation_distribution; census.json,
structure_edges.relation_distribution) for the topic/subtopic composition grain.
Consumers should read PART_OF as the membership relation that keeps concept-level
content legally traceable to official wording — a concept with no PART_OF path to a
specification point would be off-curriculum by construction.

### CUR-019 — REQUIRES_PREREQUISITE between concepts, and its direction

REQUIRES_PREREQUISITE is the largest semantic relation (209 edges; RUN-COMPUTED:
census.json, concept_edges.relation_distribution). The direction convention is
V2-native: the source requires the target — exemplar 4CH1-CON-ANION-TESTS
REQUIRES_PREREQUISITE 4CH1-CON-GAS-TESTS, evidenced by the limewater-step note ("Bubble
the gas released through limewater"), because the carbonate test is a gas test applied
within it (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 7909-7923). The same source-node exemplar set shows
cross-topic dependencies (anion tests requiring ion-charge rules from S1) that CUR-06
synthesizes; this record fixes the relation's LOCAL meaning: an ordered didactic
dependency between two concepts, direction from the dependent to the prerequisite.
Any sequencing consumer (CUR-05, PED, TUT) must preserve this direction when
projecting edges into teaching order.

### CUR-020 — EXPLAINED_BY and RELATED_TO: explanation and association

EXPLAINED_BY links a phenomenon-level concept to the concept that explains it:
exemplar 4CH1-CON-AIR-COMPOSITION EXPLAINED_BY 4CH1-CON-O2-PERCENT-DETERMINATION,
evidenced by the practical note ("percentage of oxygen = 19.7%") (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 13028-13042). RELATED_TO records a weaker, non-hierarchical association:
exemplar 4CH1-CON-DIAMOND-GRAPHITE RELATED_TO 4CH1-CON-SIMPLE-MOLECULAR, with its
per-edge provenance visible in-window (tier AI_SUGGESTED, model_version "GLM (Super Z
agent, z.ai)", extraction_pass c11-s16-batch-3, derivation RELATED_RESIDUAL)
(SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 13354-13368). Both relations are sparse by design (12 and 2
edges of record; RUN-COMPUTED: census.json, concept_edges.relation_distribution) —
the store prefers explicit dependency and error relations over loose association, and
downstream consumers should treat RELATED_TO as texture, never as sequencing
evidence.

### CUR-021 — The confusion layer: COMMONLY_CONFUSED_WITH and MISCONCEPTION_OF

COMMONLY_CONFUSED_WITH pairs concepts that learners interchangeably muddle without
either being wrong: exemplar 4CH1-CON-ATOMIC-NUMBER COMMONLY_CONFUSED_WITH
4CH1-CON-MASS-NUMBER, evidenced by the note ("Both the atomic number and the mass
number are given on the Periodic Table, but it can be easy to confuse them")
(SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 13428-13442). MISCONCEPTION_OF instead anchors an error node
to the correct concept it distorts: exemplar 4CH1-MIS-EQ-SUBSCRIPT MISCONCEPTION_OF
4CH1-CON-EQ-SYMBOL, evidenced by the balancing note ("A common mistake when balancing
symbol equations is to add, change or remove small numbers in the chemical formula of
a substance") (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 13499-13513). The two relations encode
different pedagogy: confusion pairs call for contrast teaching; misconception links
call for error diagnosis against a fixed correct referent. Both are sparse in the
store of record (2 edges each; RUN-COMPUTED: census.json,
concept_edges.relation_distribution) — the bulk of the error model lives in the
WRONG_ANSWER_PATTERN relation below.

### CUR-022 — The error-to-remediation loop: WRONG_ANSWER_PATTERN and REMEDIATED_BY

The store's heaviest error relations both center on misconception nodes. WRONG_ANSWER_PATTERN
(24 edges) links an error node to the concept whose questions expose it: exemplar
4CH1-MIS-BOND-ENERGY-COUNT WRONG_ANSWER_PATTERN 4CH1-CON-BOND-ENERGY-CALC, evidenced
by a MARK_SCHEME row ("Deduct 1 mark for each mistake") and the teaching note ("Don't forget to take into account the balancing numbers when working out how many of each type of bond is being broken/formed") (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 13549-13563). REMEDIATED_BY (26 edges) links the same error node to the concept or
content that repairs it: exemplar 4CH1-MIS-BOND-ENERGY-COUNT REMEDIATED_BY
4CH1-CON-BOND-ENERGY-CALC, evidenced by the method note ("it is helpful to write down
a displayed formula equation for the reaction before identifying the type and number
of bonds") (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 14150-14164). Read together, the two relations are
the store's remediation loop: error → the assessment surface where it costs marks →
the content that fixes it. This loop is the natural consumption contract for the MIS
family (diagnosis) and the TUT/PED families (intervention), and it is why those
families should key on misconception node codes rather than free-text error labels.

### CUR-023 — Per-edge provenance and the validation-tier distribution

Every in-pack edge window carries a per-edge provenance block — tier, model_version,
extraction_pass — alongside evidence rows typed NOTE or MARK_SCHEME (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 13354-13368); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 13428-13442). The store-wide tier
distribution is 389 HUMAN_VALIDATED, 97 SUGGESTED and 2 REVIEW_REQUIRED across the
488 edges (RUN-COMPUTED: census.json, concept_edges.validation_distribution), while
the node store stands entirely at AI_SUGGESTED with an operator-only promotion gate
(SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 251-265). The interpretation law for downstream families:
relationship DATA may be consumed at its declared tier (HUMAN_VALIDATED edges are the
dependable spine for sequencing; SUGGESTED edges are research texture), and the 2
REVIEW_REQUIRED edges are disclosed as explicitly unreviewed — any consumer touching
them must re-disclose that status rather than silently treating them as validated.

## Evidence / Source Basis

- **CURRENT — AUTHORITATIVE:** SRC-SPEC-4CH1 — official specification PDF, Issue 3
  (page 15, topic structure context), sha1 of record
  3ad641b7c60b314fa3b10680feda30bf56280a53, verified at run preflight.
- **CURRENT — AUTHORITATIVE:** SRC-GRAPH-4CH1 — validated curriculum graph:
  concept_edges.yaml (488 edges, 8-relation vocabulary, per-edge provenance),
  concepts.yaml (meta block: provenance law, edge vocabulary declaration), verified
  at run preflight. Read-only plane for this pipeline. Edge evidence rows referencing
  external note/mark-scheme files are pointers; those files are not resolved sources
  of this library.
- **CURRENT — AUTHORITATIVE / SUPPLEMENTARY:** SRC-TL-4CH1 — Getting Started Guide
  (page 3) as identity/context row.
- **CURRENT — ASSESSMENT EVIDENCE (specimen):** SRC-SAMS-4CH1 — page 1 identity-only
  row.
- **RUN-COMPUTED:** census.json — deterministic counts over the graph stores of
  record; verified by the run's evidence-claim QA.

## Limitations / Coverage Gaps

- The pack carries 59 edge windows of 488 edges of record (covering all eight
  relation kinds with at least one exemplar each); kind-level counts rest on the
  RUN-COMPUTED census.
- REMEDIATED_BY is sampled thinly in-pack (1 of 26); its loop-law claim rests on the
  exemplar plus the census count, not on exhaustive excerpt coverage.
- The store's derivation methods (e.g. RELATED_RESIDUAL) are recorded per edge in the
  store itself; this artifact reports them as declared, without re-adjudicating.
- Edge evidence quotes referencing external files (revision notes, mark-scheme
  extracts under scripts/c11_evidence/) are pointers recorded by the store; their
  parent corpora are not resolved sources of this library.
- The 2 REVIEW_REQUIRED edges are disclosed as unreviewed; no record here consumes
  them as validated content.

## Research Status

status: GENERATED (research artifact; not educational truth, not canonical curriculum
truth). Generated by the SIB-GEN batch run SIB-CHEMISTRY_4CH1-RUN-002 under the
provider-neutral pipeline (BL-008 wave 1, protocol §4 pass 2), grounded exclusively on
the run's CUR-04 evidence pack (pack sha256 of record in the run manifest) plus the
run's deterministic census annex. Current/legacy separation: fully CURRENT; no legacy
claims. Determinism: content fingerprint of this artifact is recorded in the run
manifest; regeneration produces a new artifact_version.
