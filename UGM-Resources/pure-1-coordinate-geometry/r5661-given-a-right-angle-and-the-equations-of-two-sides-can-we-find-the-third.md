---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/geometry-of-equations/r5661
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- geometry-of-equations
- type/review-question
resource_identity:
  ugm_id: r5661
  station: geometry-of-equations
  station_title: Geometry of Equations
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5661
  old_site_id: Q4062
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: geometry-of-equations
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: geometry-of-equations
    validation_status: SUGGESTED
  spec_points:
  - code: 1.3.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'two side equations given, third side from the perpendicular gradient through the given vertex.'
      rationale: 'Canonical UGM title: “Given a right angle and the equations of two sides, can we find the third?”; exam provenance: UCLES 1979 Q5'
      validation_status: SUGGESTED
    title: find the equation of a straight line given e.g. given two points, or one point and the gradient. sufficient information
  - code: 1.3.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'two side equations given, third side from the perpendicular gradient through the given vertex.'
      rationale: 'Canonical UGM title: “Given a right angle and the equations of two sides, can we find the third?”; exam provenance: UCLES 1979 Q5'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1979 Q5
task: T-UGM-IMPORT-3
---

# Given a right angle and the equations of two sides, can we find the third?

## Question

In the triangle \(ABC\) the equations of two of the sides are \(2y=x+2\) and \(y=2x-2\). Given that \(A\) is the point \((4,3)\) and that \(A\hat{B}C\) is \(90^\circ\), find the equation of the third side.

## Suggestion

How could we find out which of those sides goes through \(A\)?

## Solution

Our best starting plan is to draw a diagram.

The point \(A\) must be on either \(y = 2x-2\), or \(2y = x + 2\), and we can see by substituting in that \(A\) is on the second of these but not the first.

So the first line (\(y=2x-2\)) must give the side \(BC\), so \(B\) lies on this line. We are also told that the angle at \(B\) is a right angle.

We can now sketch our diagram. (At this stage, we have not worked out whether \(2y=x+2\) passes through \(B\) or not.)

Now the gradient of \(BC\) is \(2\), so the gradient of \(AB\) is \(-\frac12\), since \(AB\) is perpendicular to \(BC\). Since the line \(AB\) passes through \(A(4,3)\), it follows that it has equation \(y-3=-\frac12(x-4)\) (using the general formula \(y-y_1=m(x-x_1)\)), which rearranges to \(y=-\frac12x+5\) or \(x+2y=10\). This is the equation of the third side.

It also follows that \(2y=x+2\) is the line \(AC\) (since it has gradient \(+\frac12\), so is not perpendicular to \(BC\)). This would allow us to work out the coordinates of \(C\), though we are not asked to find these.
