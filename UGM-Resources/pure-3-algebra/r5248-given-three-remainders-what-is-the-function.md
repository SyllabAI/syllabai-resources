---
created: 2026-10-25T01:37:17 (UTC +06:00)
source: https://undergroundmathematics.org/polynomials/r5248
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- polynomials
- type/review-question
resource_identity:
  ugm_id: r5248
  station: polynomials
  station_title: Polynomials & Rational Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5248
  old_site_id: "Q185"
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: polynomials
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: polynomials
    validation_status: SUGGESTED
  spec_points:
  - code: 3.1.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-9 cross-map (cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb)"
      evidence: "remainders 10, 3, 4 under x−1, x−2, x−3 recovered as f(1), f(2), f(3) by the remainder theorem, solving for a, b, c in the nested product form"
      rationale: "Canonical UGM title: Given three remainders, what is the function?"
      validation_status: SUGGESTED
    title: "use the factor theorem and the remainder theorem"
  mapped_date: '2026-10-25'
  mapper: cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "UCLES A level Mathematics 1 and Pure Mathematics 1, QP 417/1 and 447/1, 1964, Q1(ii)"
  task: T-UGM-IMPORT-9
---

# Given three remainders, what is the function?

## Question

A certain function of \(x\) can be expressed in the form \[a+b(x-1)+c(x-1)(x-2)+2(x-1)(x-2)(x-3),\] where \(a\), \(b\), \(c\), are numerical. When the function is divided in turn by \(x-1\), \(x-2\), \(x-3\) the remainders are \(10\), \(3\), \(4\). Calculate the values of \(a\), \(b\), \(c\).

## Solution

Let

\(f(x)\)

denote our function of

\(x\)

. That is,

\[\begin{equation} f(x) = a+b(x-1)+c(x-1)(x-2)+2(x-1)(x-2)(x-3). \label{eq:1} \end{equation}\]

As \(f(x)\) is a polynomial, the [Remainder Theorem](https://undergroundmathematics.org/glossary/remainder-theorem) tells us that the remainder when divided by \((x-a)\) is equal to \(f(a)\). Substituting \(1\), \(2\) and \(3\) into \(\eqref{eq:1}\) in turn, we get that \[f(1) = a,\quad f(2)=a+b \quad \text{and} \quad f(3)=a+2b+2c,\] and so \(a=10\), \(a+b=3\) and \(a+2b+2c=4\).

Solving these equations then gives that \(a=10\), \(b=-7\) and \(c=4\).
