---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/geometry-of-equations/r7320
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- geometry-of-equations
- type/review-question
resource_identity:
  ugm_id: r7320
  station: geometry-of-equations
  station_title: Geometry of Equations
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7320
  old_site_id: Q4024
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
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'Shade (x-2)(y+3)>=0 and x^2+y^2<=25, find p with (3,p) in both — circle-equation graph reading plus inequality-region extension (recorded medium).'
      rationale: 'Canonical UGM title: “Can we illustrate this pair of inequalities on a graph?”; exam provenance: O&C (Oxford & Cambridge SEG) 1964 Q5'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: O&C (Oxford & Cambridge SEG) 1964 Q5
task: T-UGM-IMPORT-3
---

# Can we illustrate this pair of inequalities on a graph?

## Question

Describe and indicate by shading, on the usual axes, the set of points \(S_1\) defined by \((x-2)(y+3) \geq 0\). \(S_2\) is the set of points defined by \(x^2+ y^2 \leq 25\). Find the range of values of \(p\) if the point \((3, p) \in S_1 \cap S_2\).

[*Editorial Note: Here by \((3, p) \in S_1 \cap S_2\), we mean that the point \((3,p)\) is contained in both \(S_1\) and \(S_2\).*]

## Suggestion

What might the boundary of \(S_1\) look like? If we know the boundary of a region, trying a few examples can often help us to see which side of the boundary is the required region.

\(S_2\) is the set of points defined by \(x^2 + y^2 \leq 25\). Find the range of values of \(p\) if the point \((3, p) \in S_1 \cap S_2\).

Sketching the region \(S_2\) on the same axes may well help here.

## Solution

The boundary of the region is given by \((x-2)(y+3)=0\), so either \(x=2\) or \(y=-3\). So \(S_2\) is bounded by two straight lines.

We have \((x-2)(y+3) \geq 0\) when either \(x-2\geq 0\) and \(y+3 \geq 0\), or \(x-2\leq 0\) and \(y+3 \leq 0\). Alternatively, we could pick a point in each of the four regions formed by the two straight lines to determine whether or not it is in \(S_1\). For example, \((0,0)\) has \((0-2)(0+3)=-2<0\), so the origin does not lie in \(S_1\).

Using either approach, we deduce that \(S_1\) is the shaded region in this diagram:

The boundary of the region (the lines \(x = 2\) and \(y = -3\)) is included in \(S_1\).

\(S_2\) is the set of points defined by \(x^2 + y^2 \leq 25\). Find the range of values of \(p\) if the point \((3, p) \in S_1 \cap S_2\).

The set \(S_2\) is the interior and boundary of a circle centred on the origin with radius \(5\).

Thus the intersection of \(S_1\) and \(S_2\) (the points in both \(S_1\) and \(S_2\)) is the area of overlap:

Thus the range of values of \(p\) if the point \((3, p) \in S_1 \cap S_2\) is given by the \(y\)-coordinates of the points in the intersection of the overlap region with the line \(x = 3\):

It’s easy to see that the line \(x=3\) leaves the overlap region at \((3,4)\) (since this is on the circle) and at \((3,-3)\) (which is on the line \(y=-3\)), and both of these points are included, so \(-3 \leq p \leq 4\).
