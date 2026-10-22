---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/geometry-of-equations/r8449
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- geometry-of-equations
- type/review-question
resource_identity:
  ugm_id: r8449
  station: geometry-of-equations
  station_title: Geometry of Equations
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8449
  old_site_id: Q4002
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
      evidence: 'perpendicular gradients, vertex coordinates by intersection, area.'
      rationale: 'Canonical UGM title: “Can we show this parallelogram is a rectangle?”; exam provenance: UCLES 1989 Q15'
      validation_status: SUGGESTED
    title: find the equation of a straight line given e.g. given two points, or one point and the gradient. sufficient information
  - code: 1.3.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'perpendicular gradients, vertex coordinates by intersection, area.'
      rationale: 'Canonical UGM title: “Can we show this parallelogram is a rectangle?”; exam provenance: UCLES 1989 Q15'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1989 Q15
task: T-UGM-IMPORT-3
---

# Can we show this parallelogram is a rectangle?

## Question

The diagram shows a parallelogram \(ABCD\) with \(A\) and \(C\) on the coordinate axes. The equation of \(AB\) is \(y=2x+1\) and the equation of \(BC\) is \(2y+x=12\).

1. Show that \(ABCD\) is a rectangle.

---

1. Find the coordinates of \(A\), \(B\), \(C\) and \(D\).

---

1. Find the area of \(ABCD\).

## Solution

Since \(ABCD\) is a parallelogram, we just need to check that \(AB\) and \(BC\) are perpendicular.

The equation of \(AB\) is \(y=2x+1\), which has gradient \(2\), and the equation of \(BC\) is \(2y+x=12\), or \(y=6-\frac{1}{2}x\) and so the gradient of \(BC\) is \(-\frac{1}{2}\).

Since \(2\times -\frac{1}{2}=-1\), \(AB\) and \(BC\) are perpendicular. Therefore \(ABCD\) is a rectangle.

Since \(A\) lies on the \(y\)-axis, it lies at the \(y\)-intercept of \(y=2x+1\), which is \(1\). So \(A=(0,1)\).

Next, since \(C\) lies on the \(x\)-axis, which is \(y=0\), we can substitute this in to the equation of \(BC\) to find that \(x=12\), so \(C=(12,0)\).

To find the coordinates of \(B\), we must find where \(AB\) and \(BC\) meet, so we solve the simultaneous equations \(y=2x+1\) and \(2y+x=12\). Substituting the first into the second gives \[2(2x+1)+x=12,\] which gives us \(x=2\), so \(y=5\). Thus \(B=(2,5)\).

Now let’s find the coordinates of \(D\). To get from \(B\) to \(A\), we go left \(2\) and down \(4\), so we must do the same to get from \(C\) to \(D\), and so \(D=(10,-4)\).

In terms of vectors, the last sentence says: \(\overrightarrow{BA}=\overrightarrow{CD}=\dbinom{-2}{-4}\), so \(D=(10,-4)\).

From the sketch, we can see (using Pythagoras’ theorem) that \(AB=\sqrt{2^2+4^2}=\sqrt{20}=2\sqrt{5}\).

Likewise, \(BC=\sqrt{5^2+10^2}=\sqrt{125}=5\sqrt{5}\).

Therefore the area of \(ABCD\) is \(AB\times BC=2\sqrt{5}\times 5\sqrt{5}=50\).
