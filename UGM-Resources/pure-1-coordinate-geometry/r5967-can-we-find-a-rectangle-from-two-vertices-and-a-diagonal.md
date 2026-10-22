---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/geometry-of-equations/r5967
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- geometry-of-equations
- type/review-question
resource_identity:
  ugm_id: r5967
  station: geometry-of-equations
  station_title: Geometry of Equations
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5967
  old_site_id: Q4039
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
      evidence: 'line through two points, perpendicular sides, intersection solving.'
      rationale: 'Canonical UGM title: “Can we find a rectangle from two vertices and a diagonal?”; exam provenance: O&C (Oxford & Cambridge SEG) 1973 Q5'
      validation_status: SUGGESTED
    title: find the equation of a straight line given e.g. given two points, or one point and the gradient. sufficient information
  - code: 1.3.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'line through two points, perpendicular sides, intersection solving.'
      rationale: 'Canonical UGM title: “Can we find a rectangle from two vertices and a diagonal?”; exam provenance: O&C (Oxford & Cambridge SEG) 1973 Q5'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: O&C (Oxford & Cambridge SEG) 1973 Q5
task: T-UGM-IMPORT-3
---

# Can we find a rectangle from two vertices and a diagonal?

## Question

The points \(A(1,2)\) and \(B(-2,1)\) are two vertices of a rectangle \(ABCD\). The diagonal \(CA\) [produced](https://undergroundmathematics.org/glossary/produced) passes through the point \((2,9)\). Calculate the coordinates of the vertices \(C\) and \(D\).

## Interactive diagram

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/ttyEt2pq)

In this applet, \(A\) and \(B\) are fixed. You can move \(C\).

## Solution

Let’s draw a diagram to help us visualise the question.

The point \(A\) has coordinates \((1,2)\) and \(B\) has coordinates \((-2,1)\), so the gradient of \(AB\) is \[\frac{\text{change in $y$}}{\text{change in $x$}}=\frac{2-1}{1-(-2)}=\frac{1}{3}.\]

Now we know that the line \(BC\) will be perpendicular to \(AB\), and so will have gradient \(-3\). As it passes through \(B(-2,1)\), it has equation \(y-1=-3(x+2)\) (using the general formula \(y-y_1=m(x-x_1)\)), which we can rearrange to obtain \[y=-3x-5.\]

In order to find \(C\), we must find where \(BC\) intersects the line \(AC\), whose equation we can find since we know two points on it, \((1,2)\) and \((2,9)\). The gradient of this line is then \[\frac{9-2}{2-1}=7,\] and so it has equation \(y-2=7(x-1)\), or \(y=7x-5\).

So to find \(C\) we must find where \(AC\) meets \(BC\), i.e., where \(y=7x-5\) and \(y=-3x-5\) meet. We see that \[7x-5=-3x-5,\] from which we obtain \(x=0\), and so \(C\) is the point \((0,-5)\).

Finally, we need to find the coordinates of \(D\). To get from \(B\) to \(A\), we move right \(3\), up \(1\). So if we go right \(3\), up \(1\) from \(C\), we get to \(D\), which therefore has coordinates \((3, -4)\).

We can think of “to get from \(B\) to \(A\)” as the vector \(\overrightarrow{BA}=\dbinom{3}{1}\), so the final sentence could be rewritten as:

As \(\overrightarrow{BA}=\dbinom{3}{1}\) and \(\overrightarrow{CD}=\overrightarrow{BA}\), we see that \(D\) has coordinates \((3,-4)\).
