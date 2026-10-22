---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/geometry-of-equations/r9273
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- geometry-of-equations
- type/review-question
resource_identity:
  ugm_id: r9273
  station: geometry-of-equations
  station_title: Geometry of Equations
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9273
  old_site_id: Q256
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
  - code: 1.3.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'Intersection point of two lines; midpoint of the segment from P perpendicular to y=2x+8 — intersection solving plus perpendicular construction.'
      rationale: 'Canonical UGM title: “Can we find the point midway between an intersection and a line?”; exam provenance: UCLES 1973 Q8'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  - code: 1.3.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'Intersection point of two lines; midpoint of the segment from P perpendicular to y=2x+8 — intersection solving plus perpendicular construction.'
      rationale: 'Canonical UGM title: “Can we find the point midway between an intersection and a line?”; exam provenance: UCLES 1973 Q8'
      validation_status: SUGGESTED
    title: find the equation of a straight line given e.g. given two points, or one point and the gradient. sufficient information
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1973 Q8
task: T-UGM-IMPORT-3
---

# Can we find the point midway between an intersection and a line?

## Question

\(P\) is the point of intersection of the lines \(y+x=1\) and \(3y+2x=1\). Find the co-ordinates of the point midway between \(P\) and the line \(y=2x+8\).

## Suggestion

Have you drawn a diagram yet? If you’re not sure where to start, sketch the three lines.

What is the gradient of a line perpendicular to \(y=2x+8\)? Can you find the equation of the one such line through \(P\)?

## Solution

Let’s first find the coordinates of the point \(P\) by solving the simultaneous equations \(y+x=1\) and \(3y+2x=1\).

We can use substitution: we know that at

\(P\)

,

\(y=1-x\)

, so

\[\begin{align*} &&3(1-x)+2x&=1,&&\quad \\ \implies&&3-3x+2x&=1,&& \\ \implies&&2&=x,&& \end{align*}\]

and so \(P\) is the point \((2,1-2)=(2,-1)\).

Alternatively, we could have used elimination: multiplying

\(y+x=1\)

by

\(2\)

gives the simultaneous equations

\[\begin{align*} 2y+2x&=2\\ 3y+2x&=1. \end{align*}\]

Then either by subtracting these equations or by observation, we see that \(y=-1\), so \(x=2\), and \(P\) is the point \((2,-1)\).

Now let’s draw a diagram showing \(P\) and the line \(y=2x+8\).

If we can find the line perpendicular to \(y=2x+8\) through \(P\), then we can find where these lines intersect, which we shall call \(Q\). We can then compute the coordinates of the point midway between \(Q\) and \(P\), which we shall call \(M\). This point \(M\) is the point the question has asked us to find.

A line perpendicular to \(y=2x+8\) must have gradient \(-\frac12\). Therefore the perpendicular passing through \(P(2,-1)\) has equation \[y+1=-\tfrac{1}{2}(x-2)\] (using the general formula \(y-y_1=m(x-x_1)\)), which we can rearrange to get \(y=-\frac12 x\).

So \(Q\) is the point of intersection of \(y=2x+8\) and \(y=-\frac{1}{2}x\). Solving these simultaneously, we find that \[-\tfrac{1}{2}x=2x+8,\] and so \(\frac{5}{2}x=-8\), giving \(x=-\frac{16}{5}\). Then we calculate \[y=-\frac{1}{2}\times\left(-\frac{16}{5}\right)=\frac{8}{5},\] therefore \(Q\) has coordinates \(\bigl(-\frac{16}{5},\frac{8}{5}\bigr)\).

The coordinates of

\(M\)

are the average (mean) of the coordinates of

\(P\)

and

\(Q\)

. We therefore have

\[\begin{align*} M&=\left(\frac{2+\bigl(-\frac{16}{5}\bigr)}{2},\frac{-1+\frac{8}{5}}{2}\right)\\ &=\left(\frac{\bigl(-\frac{6}{5}\bigr)}{2},\frac{\bigl(\frac{3}{5}\bigr)}{2}\right)\\ &=\left(-\frac{3}{5},\frac{3}{10}\right). \end{align*}\]
