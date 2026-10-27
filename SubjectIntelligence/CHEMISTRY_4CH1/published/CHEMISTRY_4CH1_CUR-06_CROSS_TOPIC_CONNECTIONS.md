---
sib_protocol: SIB-1.0
artifact_id: CUR-06
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

# lifecycle: GENERATED -> QA_PASSED -> STAGED
status: PUBLISHED
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

# CUR-06 — Cross-Topic Connections

## Purpose

This artifact is the cross-topic synthesis of the CHEMISTRY_4CH1 curriculum intelligence:
where the four official topics exchange content — which later topics consume which
earlier foundations, which foundations are silently re-used across the qualification,
and where the of-record graph is structurally silent. The official specification
presents chemistry content as four parallel topics (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p15); learning
does not respect that presentation, and neither does the validated concept graph. This
artifact reads the graph's cross-topic edges honestly — including the important
negative result at the statement grain — and states the consumption contract for
sequencing consumers. It is a research artifact; canonical planes remain authoritative
and read-only to this pipeline.

## Scope

**Covers:** the genuine cross-topic concept edges of the validated graph (24 edges of
record whose endpoints anchor to different topics; RUN-COMPUTED: census.json,
concept_edges.genuine_cross_topic_edges.count), with 26 in-pack REQUIRES_PREREQUISITE
windows and 17 PART_OF windows situating the bridge concepts in their official
statements; the point-edge store's zero-cross-topic boundary at statement grain
(RUN-COMPUTED: census.json, point_edges.cross_topic_point_edges) — with in-pack shape
samples); and the didactic reading of the resulting pattern. Temporal scope is CURRENT
— AUTHORITATIVE; no legacy material is used or cited.

**Does not cover:** intra-topic sequence law (CUR-05's ground), the official topic
definitions themselves (CUR-01), or any claim that topic boundaries should be
re-drawn — the four-topic structure is official; this artifact maps the traffic
across it.

## Executive Summary

- At the official statement grain, the ratified point-edge store contains ZERO
  cross-topic edges: all 35 rows are intra-topic (RUN-COMPUTED: census.json,
  point_edges.cross_topic_point_edges). Cross-topic connectivity of record exists
  only at the concept grain.
- At the concept grain, 24 genuine cross-topic REQUIRES_PREREQUISITE edges of record
  connect the four topics (RUN-COMPUTED: census.json,
  concept_edges.genuine_cross_topic_edges.count); the in-pack windows instantiate the
  pattern from every topic pair.
- The dominant pattern is S1-as-foundation: S2 ion tests and Group 1/7 reactivity
  require S1's ion-charge rules and electronic configuration; S3 bond-energy
  calculation requires S1's covalent bond; S4 crude oil and ethanol manufacture
  require S1's mixture and fractional distillation concepts
  (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 7939-7953); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 10023-10037); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 8146-8160); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 8861-8875); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 8918-8932).
- The dependencies are not strictly forward in topic order: two edges run S2→S3
  (combustion requiring exothermic/endothermic; extraction method requiring the
  reactivity-order concept), which the official S1→S4 topic presentation does not
  advertise (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 8546-8560); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 9864-9878); (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p15).

## Main Analysis

### CUR-031 — Two grains, two answers: the method of this artifact

Cross-topic connectivity must be read at the grain the stores actually encode. At the
specification-point grain, the ratified store of record is entirely intra-topic: 35
edges, 0 crossing topic boundaries (RUN-COMPUTED: census.json,
point_edges.cross_topic_point_edges), with the in-pack shape samples showing the
row anatomy (p:1.19 REQUIRES_PREREQUISITE p:1.18 and siblings — all within-topic
pairs) (SRC-GRAPH-4CH1, graph/igcse-chemistry/point_edges.yaml lines 32-46); (SRC-GRAPH-4CH1, graph/igcse-chemistry/point_edges.yaml lines 152-166). At the concept
grain, the graph DOES cross topics: 24 genuine cross-topic edges — defined as edges
whose two endpoints anchor to spec points of different topics — all of relation
REQUIRES_PREREQUISITE (RUN-COMPUTED: census.json,
concept_edges.genuine_cross_topic_edges.count;
census.json, concept_edges.genuine_cross_topic_edges.by_relation). Both results are
reported, not reconciled away: the statement-grain silence means the official
specification never makes a cross-topic dependency explicit as statement wording,
while the concept grain records where understanding must actually transfer. The
PART_OF windows ground every named bridge concept back into its official statements
(anion tests → 2.48, bond-energy calculation → 3.7C, carboxylic-acid reactions →
4.36C, combustion in oxygen → 2.11, crude oil → 4.7, electrolysis → 1.58C via its
node, extraction method → 2.23C, G1 reactivity → 2.4C) (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 944-958); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 1355-1369); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 1484-1498); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 1927-1941); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 2412-2426); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 3686-3700); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 4025-4039).

### CUR-032 — S1 as the load-bearing foundation

The heaviest traffic INTO earlier topics targets S1. From S2: the anion-tests and
cation-tests concepts each require the ion-charge-rules concept ("Common ion charges
(group-based and named-ion table, with the deduction rule)", anchored at S1) — writing
ionic equations for precipitate tests is impossible without the charge vocabulary
(SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 7939-7953); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 8383-8397); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 4478-4492); and the Group 1 and Group 7 reactivity concepts
each require electronic configuration of the first 20 elements (1.19, S1) — the
trend explanations ARE configuration arguments (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 10023-10037); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 10200-10214); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 2779-2793). From S2 into
S1 as well: the extraction-method concept requires the electrolysis concept (molten
binary compounds, inert electrodes — 1.58C's ground) (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 9801-9815); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 2733-2747). From S3: bond-energy calculation
requires the covalent-bond concept (shared pair; electrostatic attraction between
shared pair and nuclei) (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 8146-8160); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 2102-2116). From S4: crude oil requires the mixture concept (S1 separation
grain), and the crude-oil-fractions and ethanol-manufacture concepts each require
fractional distillation (the S1 separation technique, anchored at 1.10)
(SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 8861-8875); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 8918-8932); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 9634-9648); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 3597-3611). The didactic conclusion: S1 is
not merely the first topic — it is the service layer every later topic draws on, and
weakness there propagates everywhere.

### CUR-033 — S2 and S3 as mutual suppliers, S4 as the consumer apex

The middle topics both supply and consume. S2 supplies S4 directly: carboxylic-acid
reactions require the S2 acid-reactions concept (metals, bases, carbonates → salts)
(SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 8255-8269); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 360-374); ethanol oxidation
requires the oxidation/reduction-agents concept (2.20's ground) (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 9704-9718); fuels-and-combustion requires the combustion-in-oxygen concept
(2.11) (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 9940-9954); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 1927-1941). But S2
also consumes S3: the combustion-in-oxygen concept requires exothermic/endothermic
classification (3.1's ground), and the extraction-method concept requires the
reactivity-order concept (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 8546-8560); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concepts.yaml lines 3312-3326); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 9864-9878). These S2→S3 edges are the
sequence-relevant surprise: the official topic order lists Inorganic (2) before
Physical (3) (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p15) (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p22) (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p27), yet two S2 application concepts depend on S3's classification vocabulary.
S4 additionally consumes its own topic's chain intra-grain (ethanol manufacture
requires alcohols and cracking; crude-oil fractions require crude oil) — the
in-pack windows record these alongside the cross-topic ones
(SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 9586-9600); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 9610-9624); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 8890-8904).

### CUR-034 — What the bridge set is, and is not, of record

The bridge set of record is exactly the 24 genuine cross-topic concept edges the
census enumerates — every one REQUIRES_PREREQUISITE, zero of any other relation
(RUN-COMPUTED: census.json, concept_edges.genuine_cross_topic_edges.by_relation).
The in-pack exemplar set (14 of the 24 listed in records CUR-032/033) is
representative but not exhaustive; the census annex carries the full edge list with
per-edge source/target topics for exhaustive consumption
(RUN-COMPUTED: census.json, concept_edges.genuine_cross_topic_edges.edges). Three
disciplines follow. First, absence of an edge is not evidence of independence: the
graph records dependencies that were extracted and survived review; undiagnosed
pairs remain open. Second, the bridge edges inherit the concept store's provenance
law — consumers must check each edge's per-edge validation_status before treating it
as sequencing law (the store's tier distribution and operator-only gate are recorded
at CUR-04; RUN-COMPUTED: census.json, concept_edges.validation_distribution). Third,
no bridge edge is a statement-grain fact: the official specification's own structure
(four topics, printed pages 11/16/21/23) is untouched by this analysis
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p15).

### CUR-035 — Didactic reading: a spiral with one documented twist

Read as curriculum design, the bridge set describes a spiral: S1's particle, charge
and separation vocabulary is re-used at S2 (ionic equations, configuration-trend
arguments, electrolysis), S3 (bond energetics) and S4 (separation-led organic
industry); S2's reaction chemistry then feeds S4's functional-group chemistry; and
S3's energetics vocabulary reaches back into S2's applications. The documented twist
is the S2→S3 direction of the two Physical-chemistry dependencies: a center teaching
in strict official topic order would meet combustion-in-oxygen and extraction-method
before the exothermic/endothermic and reactivity-order concepts they require
(SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 8546-8560); (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 9864-9878) (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p15). This artifact does not prescribe re-ordering — scheme-of-work decisions
belong to the operator and the PED family — but it records the dependency-driven
tension so sequencing consumers see it of record rather than discovering it in the
classroom.

### CUR-036 — Boundary discipline: what this analysis does not license

Three boundaries bound every downstream use. First, no re-scoping of official
structure: the specification's four topics and their subtopics remain the official
content map (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p15) (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p17); the bridges are
understanding-level traffic, not an alternative syllabus. Second, no statement-grain
invention: because the ratified point-edge store holds zero cross-topic rows, any
claim that "statement X officially requires statement Y from another topic" is
UNSUPPORTED by the store of record — cross-topic sequencing claims must be made at
the concept grain with their tier disclosed. Third, no silent tier promotion: bridge
edges at SUGGESTED tier are research texture until operator-validated, and the 2
REVIEW_REQUIRED edges of the wider store stay quarantined from sequencing claims
(RUN-COMPUTED: census.json, concept_edges.validation_distribution).

### CUR-037 — Consumption contract for sequencing consumers

Consumers (PED scheme-of-work analysis, TUT tutoring plans, EXP explanation ordering)
should: key bridges by concept code pair, resolved through the PART_OF anchors to
official statements; preserve direction (source requires target — the
fractional-distillation example runs FROM ethanol-manufacture TO the S1 concept, not
the reverse) (SRC-GRAPH-4CH1, graph/igcse-chemistry/concept_edges.yaml lines 9634-9648); check per-edge validation_status
before promotion into teaching-order law; and treat the 24-edge census as the
complete bridge inventory of record for this run, with the census annex's pinned
input digests making the inventory reproducible
(RUN-COMPUTED: census.json, concept_edges.genuine_cross_topic_edges.count;
census.json, concept_edges.genuine_cross_topic_edges.edges). Where a consumer needs
a bridge the graph does not record, the honest output is a disclosed gap — never an
invented edge.

## Evidence / Source Basis

- **CURRENT — AUTHORITATIVE:** SRC-SPEC-4CH1 — official specification PDF, Issue 3
  (pages 15, 17, 22, 27, 29 — the content map and the four topic openings), sha1 of
  record 3ad641b7c60b314fa3b10680feda30bf56280a53, verified at run preflight.
- **CURRENT — AUTHORITATIVE:** SRC-GRAPH-4CH1 — validated curriculum graph:
  concept_edges.yaml (bridge and intra-topic exemplars), concepts.yaml (bridge
  concept definitions), point_edges.yaml (statement-grain shape samples), verified at
  run preflight. Read-only plane for this pipeline. Edge evidence rows referencing
  external note/mark-scheme files are pointers, not resolved sources of this library.
- **CURRENT — AUTHORITATIVE / SUPPLEMENTARY:** SRC-TL-4CH1 — Getting Started Guide
  (page 3) as identity/context row.
- **CURRENT — ASSESSMENT EVIDENCE (specimen):** SRC-SAMS-4CH1 — page 1 identity-only
  row.
- **RUN-COMPUTED:** census.json — deterministic counts over the graph stores of
  record (including the genuine-cross-topic edge list); verified by the run's
  evidence-claim QA.

## Limitations / Coverage Gaps

- Cross-topic connectivity of record exists ONLY at the concept grain; the official
  statement-grain store is silent (zero rows), so statement-level cross-topic claims
  are unsupported by construction.
- The concept graph's cross-topic edges carry the concept store's provenance tiers;
  in-pack windows show per-edge provenance for some exemplars only — consumers must
  read the store for per-edge status.
- The in-pack exemplar set covers 26 of the 488 concept edges; the full 24-edge
  bridge inventory rests on the RUN-COMPUTED census (inputs pinned, reproducible).
- Whether the 24 bridges are exhaustive of true cross-topic dependency is unknown by
  the store's own provenance law; unlisted pairs are undiagnosed, not disproven.
- No scheme-of-work text was extracted in this run (DOCX identity-only rows), so the
  board's own sequencing intent is not groundable here — the tension noted in CUR-035
  is the graph's testimony, not the board's.

## Research Status

status: GENERATED (research artifact; not educational truth, not canonical curriculum
truth). Generated by the SIB-GEN batch run SIB-CHEMISTRY_4CH1-RUN-002 under the
provider-neutral pipeline (BL-008 wave 1, protocol §4 pass 2), grounded exclusively on
the run's CUR-06 evidence pack (pack sha256 of record in the run manifest) plus the
run's deterministic census annex. Current/legacy separation: fully CURRENT; no legacy
claims. Determinism: content fingerprint of this artifact is recorded in the run
manifest; regeneration produces a new artifact_version.
