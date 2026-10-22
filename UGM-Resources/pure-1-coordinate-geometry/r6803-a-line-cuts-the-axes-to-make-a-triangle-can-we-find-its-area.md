---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/geometry-of-equations/r6803
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- geometry-of-equations
- type/review-question
resource_identity:
  ugm_id: r6803
  station: geometry-of-equations
  station_title: Geometry of Equations
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6803
  old_site_id: Q1071
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
      evidence: 'gradient+point construction, axis intercepts, triangle area.'
      rationale: 'Canonical UGM title: “A line cuts the axes to make a triangle; can we find its area?”; exam provenance: UCLES 1981 Q1'
      validation_status: SUGGESTED
    title: find the equation of a straight line given e.g. given two points, or one point and the gradient. sufficient information
  - code: 1.3.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'gradient+point construction, axis intercepts, triangle area.'
      rationale: 'Canonical UGM title: “A line cuts the axes to make a triangle; can we find its area?”; exam provenance: UCLES 1981 Q1'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1981 Q1
task: T-UGM-IMPORT-3
---

# A line cuts the axes to make a triangle; can we find its area?

## Question

Three points have coordinates \(A(-2, -1)\), \(B(6, 9)\) and \(C(2, -3)\). The line through the midpoint of \(AB\) parallel to \(AC\) meets the \(x\)-axis at \(X\) and the \(y\)-axis at \(Y\). **Calculate** the coordinates of \(X\) and \(Y\). Hence deduce the area of \(\triangle XOY\), where \(O\) is the origin.

## Suggestion

It is always helpful to draw a sketch of a geometric situation.

We are given coordinates of points; how can we use these to find the equation of the new line?

## Solution

We will first find the midpoint of \(AB\); let’s call it \(M\).

The midpoint of \(AB\) has coordinates which are midway between the coordinates of \(A\) and \(B\).

So in general, given two points \(A(x_1, y_1)\) and \(B(x_2, y_2)\), the midpoint has coordinates \(\left(\dfrac{x_1 + x_2}{2}, \dfrac{y_1 + y_2}{2}\right)\).

In this case, therefore, \(M\) has coordinates \(\left(\dfrac{-2 + 6}{2}, \dfrac{-1 + 9}{2}\right) = (2, 4)\).

Another method

We can consider this sketch of the situation:

Now the horizontal distance between \(A\) and \(B\) is \(6 - (-2) = 8\) and the vertical distance between \(A\) and \(B\) is \(9 - (-1) = 10\).

Therefore, the horizontal distance between \(A\) and \(M\) is \(\dfrac{8}{2} = 4\) and the vertical distance between \(A\) and \(M\) is \(\dfrac{10}{2} = 5\).

As the point \(A\) has the coordinates \((-2, -1)\), the midpoint \(M\) is \((-2 + 4, -1 + 5) = (2,4)\).

What is the equation of the line through \(M\) parallel to \(AC\)? We will use the fact that two lines are parallel if and only if they have the same gradient.

The gradient of the line \(AC\) is \(\dfrac{-3-(-1)}{2-(-2)}=\dfrac{-2}{4} = - \dfrac{1}{2}\). So the line through \(M\) parallel to \(AC\) has gradient \(-\dfrac12\).

As it passes through \(M(2,4)\), it therefore has equation \(y-4=-\frac12(x-2)\) (using the general formula \(y-y_1=m(x-x_1)\)), which rearranges to \(y=-\frac12 x+5\).

We now want to find \(X\) and \(Y\), which are the intercepts with the \(x\) and \(y\) axes respectively.

To find \(X(x,0)\), we solve the equation \(0 = -\dfrac{1}{2} x + 5\), and therefore we have \(X=(10, 0)\).

To find \(Y(0,y)\), we solve \(y = -\dfrac{1}{2} \times 0 + 5\), which gives \(y = 5\). Therefore, \(Y\) has coordinates \((5, 0)\).

The triangle \(\triangle XOY\) is right-angled, so its area is given by \(\frac12 OX\times OY=\frac 12\times 10\times 5=25\).
