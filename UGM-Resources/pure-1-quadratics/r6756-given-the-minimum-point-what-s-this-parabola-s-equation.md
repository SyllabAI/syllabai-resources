---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r6756
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r6756
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6756
  old_site_id: Q2022
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: quadratics
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: quadratics
    validation_status: SUGGESTED
  spec_points:
  - code: 1.1.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: Equation of a parabola from its minimum point — vertex form.
      rationale: 'Canonical UGM title: “Given the minimum point, what''s this parabola''s equation?”;
        exam provenance: UCLES 1958 Q2(i)'
      validation_status: SUGGESTED
    title: carry out the process of completing the square for a quadratic polynomial ax + bx + c and use
      y a completed square form
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1958 Q2(i)
task: T-UGM-IMPORT-1
assets:
- path: https://undergroundmathematics.org/quadratics/r6756/images/r6756.png
  kind: figure
---

# Given the minimum point, what's this parabola's equation?

## Question

The least value of the function \(x^2+px+q\) is \(3\), and this occurs when \(x=-2\). Find the values of \(p\) and \(q\).

## Suggestion

Given

1. the least value of a quadratic function,
2. where it occurs, and
3. the coefficient of \(x^2\),

can we write the function straight down?

If we were asked to sketch the graph, where would the vertex be?

## Solution

By completing the square, we can express any quadratic polynomial in the form \(a(x-r)^2+s\) for some \(a\), \(r\) and \(s\).

From this, if \(a\) is positive, the least value is \(s\), and this occurs when \(x=r\).

For our question, we must have that \[x^2+px+q = (x+2)^2+3 = x^2+4x+7,\] and so, by comparing coefficients, we get \(p=4\) and \(q=7\). A sketch of the curve can be seen below.

> [figure: Graph of the quadratic described above. — `https://undergroundmathematics.org/quadratics/r6756/images/r6756.png`] (image not included in the text import; path of record).
