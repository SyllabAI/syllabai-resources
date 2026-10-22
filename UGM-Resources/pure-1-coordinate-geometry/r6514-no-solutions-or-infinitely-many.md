---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/geometry-of-equations/r6514
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- geometry-of-equations
- type/review-question
resource_identity:
  ugm_id: r6514
  station: geometry-of-equations
  station_title: Geometry of Equations
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6514
  old_site_id: Q3010
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
      evidence: 'Value of k giving infinitely-many/no solutions of a linear pair — degenerate systems read as coincident/parallel lines (KQ64).'
      rationale: 'Canonical UGM title: “No solutions, or infinitely many?”; exam provenance: UCLES 1983 Q30b'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1983 Q30b
task: T-UGM-IMPORT-3
---

# No solutions, or infinitely many?

## Question

Find the value of

\(k\)

for which the simultaneous equations

\[\begin{align*} 2x - ky &= 1 \\ (k+3)x - 9y &= k \end{align*}\]

have

1. an infinite number of solutions,

---

1. no solutions.

## Solution

**Approach 1: using algebra**

From the first equation, we can write

\[\begin{equation}\label{eq:eq-for-x-in-terms-of-k-and-y} x = \frac{1+ky}{2} \end{equation}\]

and substitute this into the second equation, which yields the equation \[(k+3) \frac{1+ky}{2} - 9y = k.\] After multiplying this through by \(2\) and rearranging, we have that \[\left( (k+3)k - 18 \right) y + (k+3) - 2k = 0.\] Expanding this leads us to the equation \[\left( k^2 + 3k - 18 \right) y + 3 - k = 0.\] The quadratic coefficient for \(y\) can be factored, giving the equation \[(k+6)(k-3)y + 3-k = 0.\]

So \((k+6)(k-3)y-(k-3)=0\), and factorising, we have

\[\begin{equation}\label{eq:linear-equation-in-y-and-k} (k-3)((k+6)y-1)=0. \end{equation}\]

Thus \(k = 3\), or \((k+6)y-1=0\).

There are three cases to consider:

**Case 1: \(k \ne 3\) and \(k \ne -6\)**

In this case, we have a unique solution, namely, \[y = \frac{1}{k+6} \quad\text{and}\quad x = \frac{(k+6) + k}{2(k+6)} = \frac{k+3}{k+6}.\]

**Case 2: \(k = 3\)**

If \(k = 3\), equation \(\eqref{eq:linear-equation-in-y-and-k}\) is true for *any* choice of \(y\), and any choice of \(y\) gives a unique value of \(x\) (namely, that given obtained from equation \(\eqref{eq:eq-for-x-in-terms-of-k-and-y}\)). Thus there are infinitely many solutions \((x,y)\).

**Case 3: \(k = -6\)**

In this case, equation \(\eqref{eq:linear-equation-in-y-and-k}\) can never hold, as it leads to the contradictory statement that \(9 = 0\). There are therefore no solutions.

**Approach 2: Using coordinate geometry**

Each of the two equations can be considered as the equation of a straight line.

In general, these two lines will meet in one point.

But if their gradients are equal, then they either have no solutions (if the lines are distinct and parallel) or infinitely many (if the lines coincide).

What are their gradients? The line \(2x - ky = 1\) has gradient \(\dfrac{2}{k}\) (if \(k \neq 0\), and is vertical if \(k=0\)) and \((k+3)x - 9y = k\) has gradient \(\dfrac{k+3}{9}\).

Their gradients are equal if \(\dfrac{2}{k} = \dfrac{k+3}{9}\), where \(k\ne0\), which rearranges to \(k^2 + 3k -18 = 0\). (If \(k=0\), the second line has gradient \(\frac13\), which is not vertical, so the lines are not parallel.)

This factorises to \((k+6)(k-3)=0\), so their gradients are equal when \(k = 3\) and when \(k=-6\).

If \(k = 3,\) then the original equations are \(2x-3y=1\), and \(6x-9y=3\), which coincide, and so there are infinitely many solutions \((x,y)\).

If \(k = -6\), then the original equations become \(2x+6y=1\), or \(x + 3y = 0.5\), and \(-3x-9y=-6\), or \(x+3y =2\). In this case the lines are parallel and distinct, so there are no solutions.

This GeoGebra applet helps us to see what is happening.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/yVzFMKhU)
