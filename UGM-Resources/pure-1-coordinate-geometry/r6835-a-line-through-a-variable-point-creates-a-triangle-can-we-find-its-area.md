---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/geometry-of-equations/r6835
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- geometry-of-equations
- type/review-question
resource_identity:
  ugm_id: r6835
  station: geometry-of-equations
  station_title: Geometry of Equations
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6835
  old_site_id: Q3013
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
      evidence: 'Line with gradient -2 through (2t,t) enclosing area 4 with the axes — the 1.3.1 statement verbatim plus intercept reading.'
      rationale: 'Canonical UGM title: “A line through a variable point creates a triangle; can we find its area?”; exam provenance: UCLES 1980 Q1'
      validation_status: SUGGESTED
    title: find the equation of a straight line given e.g. given two points, or one point and the gradient. sufficient information
  - code: 1.3.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'Line with gradient -2 through (2t,t) enclosing area 4 with the axes — the 1.3.1 statement verbatim plus intercept reading.'
      rationale: 'Canonical UGM title: “A line through a variable point creates a triangle; can we find its area?”; exam provenance: UCLES 1980 Q1'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1980 Q1
task: T-UGM-IMPORT-3
---

# A line through a variable point creates a triangle; can we find its area?

## Question

Find

1. the equation of the line with gradient \(-2\) which passes through the point \((2t,t)\),

---

1. the values of \(t\) for which the area enclosed by this line and the coordinate axes is \(4\) square units.

## Interactive diagram

Can we achieve an area of \(4\) by varying \(t\)?

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/kyKuAya5)

## Solution

Using the general formula \(y-y_1=m(x-x_1)\), the equation is \(y-t=-2(x-2t)\), which rearranges to give \(y=-2x+5t\) or \(2x+y=5t\).

Find

1. the values of \(t\) for which the area enclosed by this line and the coordinate axes is \(4\) square units.

We begin by finding the points where this line intersects the axes.

When \(x=0\), \(y=5t\), and when \(y=0\), \(x=\frac52 t\), so the points of intersection are \((0,5t)\) and \((\frac52 t,0)\). A sketch of the situation looks like this; we have drawn two sketches, one for the case \(t>0\) and the other for the case \(t<0\).

The region enclosed by the line and the coordinate axes is a right-angled triangle, so its area is given by \[\text{area} = \frac{1}{2} \times \frac{5}{2}t \times 5t = \frac{25}{4}t^2.\]

We are asked to find the values of \(t\) for which this area equals \(4\), so we need \[\frac{25}{4}t^2 = 4.\] This gives \(t^2=\frac{16}{25}\) and so \(t = \pm \frac{4}{5}\).

We have not been quite precise in this argument. The area is \(\frac{1}{2} \times \frac{5}{2}t \times 5t=\frac{25}{4}t^2\) when \(t\) is positive, but when \(t\) is negative, the side lengths (which must be positive) are \(-\frac52 t\) and \(-5t\), so the area is then \(\frac{1}{2} \times \bigl(-\frac{5}{2}t\bigr) \times (-5t)\). However, this still multiplies to give \(\frac{25}{4}t^2\), so our final answer is correct, as can also been seen by the symmetry of the situation.
