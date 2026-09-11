# RAG / Retrieval Corpus Guidance for SyllabAI

**Status:** Canonical corpus-side guidance for retrieval experiments  
**Date:** 2026-09-12  
**Current pilot:** Pearson Edexcel International GCSE Chemistry 4CH1 (2017 linear)

## Purpose

This repository is the resource corpus, not the Tutor runtime. Its job is to preserve source fidelity, provenance, validation state and useful document structure so the main SyllabAI retrieval engine can consume evidence safely.

Research into RAG_Techniques, LightRAG, RAG-Anything and RAGFlow produced the following corpus rules.

## 1. Never flatten the educational hierarchy

Preserve:

```text
Board
 → Qualification
 → Subject
 → CurriculumVersion
 → Section
 → Topic/SubTopic
 → SpecificationPoint
 → Resource
 → Evidence segment
```

A retrieval chunk is a search representation, not a replacement for this hierarchy.

Do not merge content across unrelated SpecificationPoints merely because semantic chunking says they are similar.

## 2. Retrieval metadata should be rich

Every retrieval-ready resource/evidence object should be able to retain, where available:

- subject;
- qualification;
- specification/curriculum version;
- section/topic/subtopic;
- SpecificationPoint IDs;
- resource identity/version;
- resource type;
- source/provenance;
- validation status;
- page/section/bounding-box location for source documents;
- concept IDs when validated;
- evidence segment identity.

This metadata supports hierarchical filtering, contextual retrieval and explainable citations.

## 3. Contextual retrieval representation

A search representation may prepend structured context, for example:

```text
Subject: International GCSE Chemistry
Specification: Pearson Edexcel 4CH1 2017 linear
Section: Principles of Chemistry
Topic: Chemical Formulae, Equations and Calculations
SpecificationPoint: 1.28
Resource: Save My Exams Revision Note

[original evidence]
```

The contextual representation is derived from canonical metadata. It must never overwrite the original source text.

## 4. HyPE / hypothetical learner questions

Hypothetical questions may be generated for retrieval experiments. They are aliases/proxies only.

```text
Validated resource
  ↓
SpecificationPoint mappings
  ↓
candidate learner questions
  ↓
validation/deduplication
  ↓
retrieval alias
```

Do not use a generated question as evidence. Do not use it to create or expand curriculum truth. Do not infer a SpecificationPoint mapping solely from a generated question.

## 5. Multimodal evidence

Chemistry resources may contain equations, tables, diagrams, apparatus and scanned content. RAG-Anything/MinerU-style extraction may be evaluated as an ingestion aid.

Extraction output is candidate evidence and must retain source location and uncertainty. VLM/OCR output is not authoritative curriculum truth.

Recommended typed evidence where available:

```text
TextSegment
Table
Equation
Figure
Question
MarkPoint
Page
BoundingBox
```

## 6. Segment reconstruction

Retrieval may select a local contiguous segment around a matched evidence span when surrounding explanation is required. Do not modify the canonical source; create a retrieval view that references the original evidence IDs.

This is particularly important for:

- worked calculations;
- multi-step explanations;
- practical procedures;
- tables followed by interpretation;
- diagrams with explanatory prose;
- question + stimulus + sub-question structures.

## 7. Coverage and negative controls

Current validated T-C10/T-C11 state must be respected by retrieval experiments:

- 182 SpecificationPoints exist in the current T-C09 graph;
- 112 revision notes are mapped;
- final note → SpecificationPoint mapping store contains 209 HUMAN_VALIDATED mappings;
- `4CH1-4.15` is intentionally uncovered after semantic review;
- the rejected `4CH1-1.17` mapping must remain rejected;
- T-C11 held/rejected edges must not become retrieval expansion paths unless explicitly promoted through the existing gate.

Retrieval must not manufacture coverage for uncovered curriculum points through semantic similarity, generated aliases or inferred graph edges.

## 8. Source-of-truth rule

The official specification remains the curriculum authority. Validated resource mappings enrich the curriculum; they do not redefine it.

Preferred provenance chain:

```text
Tutor claim
 → evidence segment
 → resource/version
 → SpecificationPoint
 → curriculum/specification source
```

## 9. Corpus changes

When adding or changing corpus material:

1. preserve source identity and provenance;
2. preserve byte/source fidelity where required by the corpus workflow;
3. do not regenerate authoritative front matter from lossy derived data;
4. preserve validation/review state;
5. update retrieval metadata only after canonical content state is stable;
6. rerun corpus QA before using the material in retrieval benchmarks.

## 10. What this repository does not own

This repository does not own:

- learner mastery;
- learner misconceptions;
- retrieval ranking policy;
- Tutor orchestration;
- final educational graph relations;
- LLM truth validation.

Those belong to the main SyllabAI/application architecture.
