---
created: 2026-10-25T01:37:17 (UTC +06:00)
source: https://undergroundmathematics.org/polynomials/r6612
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- polynomials
- type/review-question
resource_identity:
  ugm_id: r6612
  station: polynomials
  station_title: Polynomials & Rational Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6612
  old_site_id: "Q86"
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
      confidence: medium
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-9 cross-map (cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb)"
      evidence: "sketch selection via the Factor Theorem: y=x³−x²−x+1=(x+1)(x−1)² cuts at −1 and touches at 1"
      rationale: "Canonical UGM title: Can we sketch the graph $y=x^3-x^2-x+1$?"
      validation_status: SUGGESTED
    title: "use the factor theorem and the remainder theorem"
  mapped_date: '2026-10-25'
  mapper: cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "Oxford University Mathematics Aptitude Test, 2011, Q1A"
  task: T-UGM-IMPORT-9
---

# Can we sketch the graph $y=x^3-x^2-x+1$?

## Question

A sketch of the graph \(y=x^3-x^2-x+1\) appears on which of the following axes?

|  |  |
|---|---|
|  |  |

## Suggestion

What do we know about the shape of the curve from the coefficient of \(x^3\)?

Where does the curve cut the axes?

Can we factorise the polynomial expression?

## Solution

The coefficient of \(x^3\) is positive, so for large \(x\) we get a positive \(y\), in which case (a) cannot be the graph.

When \(x=0\), \(y=1\), so the \(y\)-intercept is \(+1\) and therefore (b) cannot be the graph.

We note that if \(x=1\) then \(y=0\), so the point \((1,0)\) is on the graph, which is not the case for (d).

Hence, the correct answer is (c).

Alternatively, we can factorise the graph into \(y=(x+1)(x-1)^2\), using the Factor Theorem.

This curve cuts the \(x\)-axis at \(-1\), and touches it at \(1\). Hence, the correct answer is (c).
