---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r7972
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r7972
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7972
  old_site_id: Q3036
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
  - code: 1.1.3
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: Reconstruct a quadratic from two known values.
      rationale: 'Canonical UGM title: “If we know two values satisfying a quadratic, can we find the
        quadratic?”; exam provenance: O&C (Oxford & Cambridge SEG) 1972 Q3(i)'
      validation_status: SUGGESTED
    title: solve quadratic equations, and quadratic By factorising, completing the square and using the
      inequalities, in one unknown formula.
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: O&C (Oxford & Cambridge SEG) 1972 Q3(i)
task: T-UGM-IMPORT-1
---

# If we know two values satisfying a quadratic, can we find the quadratic?

## Question

If \(x^2 = ax + b\) has solutions \(x = -2\) and \(x = 4\), find the values of \(a\) and \(b\).

## Solution

By substituting in the values

\(x = -2\)

and

\(x = 4\)

, we know that

\[\begin{align*} 4 &= -2a + b, \\ 16 &= 4a + b. \end{align*}\]

We can solve these equations simultaneously: subtracting the first from the second to eliminate \(b\) gives \[12=6a,\] so \(a=2\). Substituting this into the first equation then gives \(b=4+2a=8\).

Finally, we can check our working using the second equation: \(4a+b=4\times2+8=16\), as we required.

Alternatively, we can say \(x^2-ax-b=(x+2)(x-4)\) for all \(x\).

Multiplying out and comparing coefficients gives \(a = 2, b = 8\), as before.
