---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/circles/r7171
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- circles
- type/review-question
resource_identity:
  ugm_id: r7171
  station: circles
  station_title: Circles
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7171
  old_site_id: Q3022
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: circles
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: circles
    validation_status: SUGGESTED
  spec_points:
  - code: 1.3.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'Line x=3 meets the circle at P and Q; tangents at P and Q and their intersection — line-circle intersection plus tangent equations via the radius-perpendicular '
      rationale: 'Canonical UGM title: “Where do this pair of tangents to a circle meet?”; exam provenance: UCLES 1970 Q8'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1970 Q8
task: T-UGM-IMPORT-3
---

# Where do this pair of tangents to a circle meet?

## Question

The straight line \(x = 3\) intersects the circle \[x^2 + y^2 - 8x - 10y - 9 = 0\] at the points \(P\) and \(Q\).

Calculate

1. the coordinates of \(P\) and \(Q\),

---

1. the equations of the tangents at \(P\) and \(Q\),

---

1. the coordinates of the point of intersection of the tangents.

## Solution

Putting \(x = 3\), the \(y\)-values we need must satisfy the equation \[3^2 + y^2 - 8 \times 3 - 10y - 9 = 0.\] After rearranging this, we have that \[y^2 - 10y - 24 = 0.\] This can be factorised as \[(y + 2)(y - 12) = 0.\] The two solutions to this equation are \(y = 12\) and \(y = -2\) and, therefore, we have that \[P = (3,-2) \quad\text{and}\quad Q = (3,12).\]

It does not matter which way around \(P\) and \(Q\) are.

1. the equations of the tangents at \(P\) and \(Q\),…

The tangent to the circle at \(P\) is perpendicular to the radius \(OP\).

To find the gradient of the radius we need to know the co-ordinates of the centre of the circle. We can find this by putting the equation into completed the square form: \[(x-4)^2 + (y - 5)^2 = 50.\]

We have the co-ordinates of \(O (4, 5)\) and of \(P (3, -2)\) so the gradient of \(OP\) is \(\frac{5 - (-2)}{4 - 3} = 7\), and the gradient of the tangent is \(-\frac{1}{7}\).

Using the coordinates of P gives us an equation for the tangent of \(y + 2 = \frac{1}{7}(x - 3)\) which can be simplified to \(7y = -x - 11\).

We can do the same for \(Q\) to find that the equation of the tangent is \(7y = x+81.\)

The point of intersection \((x,y)\) must satisfy the pair of equations \[7y= -x - 11, 7y = x + 81.\] Thus we need to solve \[-x - 11= x + 81,\] which gives \(x = -46\), from where we find \(y = 5\) (as, with a little thought, we know it has to be).
