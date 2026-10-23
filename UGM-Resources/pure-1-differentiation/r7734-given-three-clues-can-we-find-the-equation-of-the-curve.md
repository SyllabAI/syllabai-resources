---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/r7734
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/review-question
resource_identity:
  ugm_id: r7734
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7734
  old_site_id: Q3048
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-of-powers
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-of-powers
    validation_status: SUGGESTED
  spec_points:
  - code: 1.7.3
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: curve with gradient ax+b through two points and tangent parallel to y=x — gradient-function
        reconstruction with a tangent condition (the reverse-of-differentiation step carries a recorded
        1.8 bearing)
      rationale: 'Canonical UGM title: "Given three clues, can we find the equation of the curve?";
        exam provenance: O&C O level Additional Mathematics 1, 1968, Q8(i)'
      validation_status: SUGGESTED
    title: apply differentiation to gradients, tangents and normals, increasing and decreasing functions
      and rates of change
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: O&C O level Additional Mathematics 1, 1968, Q8(i)
task: T-UGM-IMPORT-7
---

# Given three clues, can we find the equation of the curve?

## Question

The gradient of a curve is \(ax + b\) at all points, where \(a\) and \(b\) are constants. Find the equation of the curve, given that it passes through the points \((0,4)\) and \((1,3)\), and that the tangent at \((1,3)\) is parallel to the line \(y = x\).

## Solution

Let’s say the equation of the curve is \(y = f(x)\), so \(y' = ax + b\). This means that \[y= \int ax + b \:dx = \frac{ax^2}{2} + bx + c\] for some constant of integration, \(c\). (This is a consequence of the [fundamental theorem of calculus](https://undergroundmathematics.org/glossary/fundamental-theorem-of-calculus).)

As the curve passes through the point \((0,4)\) we know that \[\frac{a \times 0^2}{2} + b \times 0 + c = 4 \implies c = 4,\] and as it passes through the point \((1,3)\), we also have that \[\frac{a \times 1^2}{2} + b \times 1 + c = 3 \implies \frac{a}{2} + b + 4 = 3 \implies a + 2b = -2.\] Now the tangent to the curve at \((1,3)\) is parallel to the line \(y = x\), which has gradient \(1\), so \(a + b = 4\) (since \(y' = ax + b\)).

We therefore have simultaneous equations in

\(a\)

and

\(b\)

, which are

\[\begin{align*} a + 2b &= -2, \\ a + b &= 1. \end{align*}\]

Subtracting, we have \(b = -3\), and hence \(a = 4\). The equation of the curve is therefore \(y = 2x^2 - 3x + 4\).
