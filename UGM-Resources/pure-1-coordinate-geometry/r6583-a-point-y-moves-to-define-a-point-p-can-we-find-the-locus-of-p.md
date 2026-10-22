---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/geometry-of-equations/r6583
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- geometry-of-equations
- type/review-question
resource_identity:
  ugm_id: r6583
  station: geometry-of-equations
  station_title: Geometry of Equations
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6583
  old_site_id: None
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
      evidence: 'perpendicular through Y meets the x-axis at Q, P the midpoint — line equations from geometric conditions, locus equation from coordinates.'
      rationale: 'Canonical UGM title: “A point $Y$ moves to define a point $P$ — can we find the locus of $P\,$?”; exam provenance: O&C (Oxford & Cambridge SEG) 1957 Q6'
      validation_status: SUGGESTED
    title: find the equation of a straight line given e.g. given two points, or one point and the gradient. sufficient information
  - code: 1.3.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'perpendicular through Y meets the x-axis at Q, P the midpoint — line equations from geometric conditions, locus equation from coordinates.'
      rationale: 'Canonical UGM title: “A point $Y$ moves to define a point $P$ — can we find the locus of $P\,$?”; exam provenance: O&C (Oxford & Cambridge SEG) 1957 Q6'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: O&C (Oxford & Cambridge SEG) 1957 Q6
task: T-UGM-IMPORT-3
---

# A point $Y$ moves to define a point $P$ — can we find the locus of $P\,$?

## Question

\(X\) is a fixed point \((3,0)\), \(Y\) is the point \((0,a)\). A line is drawn through \(Y\) and perpendicular to \(XY\), meeting the \(x\)-axis at \(Q\). On this line a point \(P\) is taken so that \(Y\) is the mid-point of \(QP\). Find the coordinates of \(P\).

Find the equation of the locus of \(P\) for varying values of \(a\).

## Suggestion

There is a lot of information here given in a verbal form. It is always useful to sketch the situation to make sense of what is being asked.

How are the coordinates of \(P\) related to each other?

## Solution

We begin by sketching a graph of the situation.

Our strategy is now clear: we will find the gradient of the line \(XY\), and so be able to work out the gradient of \(PQ\). This will allow us to find the equation of \(PQ\), and hence the coordinates of \(Q\). Since \(Y\) is the midpoint of \(PQ\), we will then be able to find the coordinates of \(P\).

The gradient of the line segment \(XY\) is \[\frac{a-0}{0-3} = -\frac{a}{3}.\] Provided that \(a \ne 0\), the equation of any line perpendicular to \(XY\) must therefore have a gradient equal to \(\dfrac{3}{a}\). (We will deal with \(a=0\) later on as a special case.)

So the equation of the line with gradient \(\dfrac{3}{a}\) that passes through \(Y(0,a)\) is \[y = \dfrac{3}{a} x + a,\] since the \(y\)-intercept is \(a\).

The point where this line intersects the \(x\)-axis (\(y=0\)) has \(x\)-coordinate \(-\dfrac{a^2}{3}\), so the point \(Q\) has coordinates \(\left( -\dfrac{a^2}{3}, 0 \right)\).

To get from \(Q\) to \(Y\) we go \(\dfrac{a^2}{3}\) to the right, then \(a\) up, so we need to repeat this to get to \(P\), which is therefore the point \(\left(\dfrac{a^2}{3}, 2a \right)\).

It is also clear from the sketch that the \(x\)-coordinates of \(P\) and \(Q\) are negatives of each other, and that the \(y\)-coordinate of \(Q\) is twice the \(y\)-coordinate of \(Y\).

In the case that \(a = 0\), the points \(Y, Q\) and \(P\) coincide at the origin. So for all values of \(a\), the point \(P\) can be expressed as \(\left( \dfrac{a^2}{3}, 2a \right)\).

Is this still true if \(a<0\)?

We need to determine the locus of the point \(P\left( \dfrac{a^2}{3}, 2a \right)\) as \(a\) varies.

If \(x = \dfrac{a^2}{3}\) and \(y = 2a\), then \(a = y/2\), giving \(x = \dfrac{(y/2)^2}{3}\). Rearranging yields \(y^2 = 12x\), which is the equation of a parabola which is symmetrical about the \(x\)-axis.

This GeoGebra applet can help us to see what is going on.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/mEYhGwbz)
