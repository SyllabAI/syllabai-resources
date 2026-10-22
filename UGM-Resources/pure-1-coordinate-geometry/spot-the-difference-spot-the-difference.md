---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/geometry-of-equations/spot-the-difference
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- geometry-of-equations
- type/building-blocks
- level/developing
resource_identity:
  ugm_id: spot-the-difference
  station: geometry-of-equations
  station_title: Geometry of Equations
  resource_type_id: 1
  resource_type_label: Building blocks
  level: Developing
  ref: 9577
  old_site_id: F1_RT2_1
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
      evidence: 'Factorised equations ((x+y-1)(x^2+y^2)=0) vs their graphs — the graph-equation relationship at degenerate cases (line + point, missing points); implicit cubic v'
      rationale: 'Canonical UGM title: “Spot the difference”'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-3
assets:
- path: https://undergroundmathematics.org/geometry-of-equations/spot-the-difference/download/teacher-notes.pdf
  kind: printable
---

# Spot the difference

> Excerpt: Given six equations appearing as only two straight lines on a graph, can you explain what is going on?

## Problem

We graphed the following three pairs of equations, all on the same axes.

1. \(x + y - 1 = 0\) and \((x + y - 1)(x^2 + y^2) = 0\)

---

1. \(x + y = 0\) and \((x + y)(y^2 + (x+1)^2) = 0\)

---

1. \(x + y = 1\) and \(x^3 + 3xy + y^3 = 1\)

To our surprise, we could only see two lines on the graph.

(You might also like to look at the graphs on [Desmos](https://www.desmos.com/calculator/dt4kjrwmxl).)

What has happened? Can you work out which equations go with which lines? Are there any points missing from the graph? If so, where should they be?

Can you think of any other sets of equations that might fool the computer?

## Solution

A point \((x,y)\) satisfies the equation \(x + y - 1 = 0\) if and only if it lies on the straight line with gradient \(-1\) passing through the point \((0, 1)\), and indeed we see that line on the picture.

A point \((x,y)\) satisfies the equation \((x + y - 1)(x^2 + y^2) = 0\) if and only if \(x + y - 1 = 0\) or \(x^2 + y^2 = 0\). So we get the same straight line as before, together with the solutions to \(x^2 + y^2 = 0\). But \(x^2 \geq 0\) and \(y^2 \geq 0\), so we see that the only solution is \((0,0)\). This shows that the equation \((x + y - 1)(x^2 + y^2) = 0\) corresponds to the straight line with gradient \(-1\) passing through the point \((0,1)\), together with the origin \((0,0)\).

It is rather hard to tell whether the origin is included for this equation in the graph above!

A point \((x,y)\) satisfies the equation \(x + y = 0\) if and only if it lies on the straight line with gradient \(-1\) through the origin, and we see that line on the picture.

A point \((x,y)\) satisfies the equation \((x + y)(y^2 + (x + 1)^2) = 0\) if and only if \(x + y = 0\) or \(y^2 + (x+1)^2 = 0\). So we get the same straight line with gradient \(-1\) through the origin, together with the solutions to \(y^2 + (x+1)^2 = 0\). Rather than multiplying out this expression, we can notice that \(y^2 \geq 0\) and \((x+1)^2 \geq 0\), so the only solution is \(x+1 = 0\) and \(y = 0\). This shows that the equation \((x + y)(y^2 + (x+1)^2) = 0\) corresponds to the straight line with gradient \(-1\) passing through the origin, together with the point \((-1,0)\).

We can rearrange the first equation of the third pair to make it the same as the first equation of the first pair, so we already know the points that satisfy this equation: they are precisely the points on the line with gradient \(-1\) passing through \((0,1)\).

Previously, the second equation in each pair has been in a factorised form, which has meant that we could read off the solutions. Inspired by our success there, we could try to factorise the second equation in the third pair to see whether we can use a similar strategy.

We have \(x^3 + 3xy + y^3 - 1 = (x + y - 1)(x^2 - xy + y^2 + x + y + 1)\), so the point \((x,y)\) satisfies the second equation in the third pair if and only if \((x + y - 1)(x^2 - xy + y^2 + x + y + 1) = 0\). We have already thought about \(x + y - 1 = 0\), so we concentrate on the equation \(x^2 - xy + y^2 + x + y + 1 = 0\).

Again we think about what worked for us last time: it was helpful to write our function as a sum of squares. Let’s see whether we can do the same thing again.

We have \(x^2 - xy + y^2 + x + y + 1 = \frac{1}{2}(x+1)^2 + \frac{1}{2}(y+1)^2 + \frac{1}{2}(x-y)^2\). This is a sum of squares, which are all non-negative, so the only way it can be zero is if every term is zero. This happens if and only if \(x = -1\), \(y = -1\), and \(x = y\).

Alternatively, and especially if we don’t spot how to write the expression as a sum of squares, we could consider it as a quadratic in

\(x\)

and try to solve that. We are interested in the equation

\(x^2 + (1-y)x + (y^2 + y + 1) = 0\)

, and using the quadratic formula we see that this has solutions

\[\begin{align*} x &= \frac{y - 1 \pm \sqrt{(1 - y)^2 - 4(y^2 + y + 1)}}{2} \\ &= \frac{y - 1 \pm \sqrt{-3y^2 - 6y - 3}}{2} \\ &= \frac{y - 1 \pm \sqrt{-3(y+1)^2}}{2}. \end{align*}\]

We are looking for real solutions, so we need the part under the square root to be non-negative, but \(-3(y+1)^2 \leq 0\), with equality if and only if \(y = -1\). So the only way we might get a solution is if \(y = -1\), and we see that this then leads to \(x = -1\).

Fortunately, this agrees with our answer above from considering the expression as a sum of squares!

We have shown that the equation \(x^3 + 3xy + y^3 - 1 = (x + y - 1)(x^2 - xy + y^2 + x + y + 1) = 0\) corresponds to the straight line with gradient \(-1\) passing through the point \((0, 1)\), together with the single point \((-1,-1)\).
