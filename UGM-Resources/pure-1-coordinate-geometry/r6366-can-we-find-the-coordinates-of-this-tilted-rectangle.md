---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/geometry-of-equations/r6366
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- geometry-of-equations
- type/review-question
resource_identity:
  ugm_id: r6366
  station: geometry-of-equations
  station_title: Geometry of Equations
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6366
  old_site_id: Q1068
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
      evidence: 'perpendicular line through B, vertex coordinates by intersection solving — line equations end to end.'
      rationale: 'Canonical UGM title: “Can we find the coordinates of this tilted rectangle?”; exam provenance: UCLES 1986 Q10'
      validation_status: SUGGESTED
    title: find the equation of a straight line given e.g. given two points, or one point and the gradient. sufficient information
  - code: 1.3.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'perpendicular line through B, vertex coordinates by intersection solving — line equations end to end.'
      rationale: 'Canonical UGM title: “Can we find the coordinates of this tilted rectangle?”; exam provenance: UCLES 1986 Q10'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1986 Q10
task: T-UGM-IMPORT-3
---

# Can we find the coordinates of this tilted rectangle?

## Question

In the rectangle \(ABCD\), \(A\) and \(B\) are the points \((4,2)\) and \((2,8)\) respectively.

Given that the equation \(AC\) is \(y=x-2\), find

1. the equation of \(BC\),

---

1. the coordinates of \(C\),

---

1. the coordinates of \(D\),

---

1. the area of the rectangle \(ABCD\).

*This question needs an exact method that goes beyond accurate drawing.*

## Suggestion

In the rectangle \(ABCD\), \(A\) and \(B\) are the points \((4,2)\) and \((2,8)\) respectively.

*This question needs an exact method that goes beyond accurate drawing.*

Given that the equation \(AC\) is \(y=x-2\), find

1. the equation of \(BC\),

If we know that \(BC\) is perpendicular to \(AB\), what can we say about the gradients of these lines?

We know the equations of \(BC\) and \(AC\) now…

How do we calculate the area of a rectangle?

## Solution

In the rectangle \(ABCD\), \(A\) and \(B\) are the points \((4,2)\) and \((2,8)\) respectively.

*This question needs an exact method that goes beyond accurate drawing.*

Given that the equation \(AC\) is \(y=x-2\), find

1. the equation of \(BC\),

The gradient of \(AB\) is \(\dfrac{8-2}{2-4} = - 3\). The gradient of the perpendicular line \(BC\) is thus \(\dfrac {1}{3}\).

Since we know that the line passes through \(B(2,8)\), the equation of \(BC\) is given by \[y-8 = \frac{1}{3}(x-2)\] which we can rearrange as \(y = \dfrac{1}{3}x+\dfrac{22}{3}\) or \(3y=x+22\).

We know that

\(BC\)

and

\(AC\)

meet at

\(C\)

. We can calculate their intersection point by setting their equations equal to each other (solving their equations simultaneously). We then have

\[\begin{align*} &&x-2&= \frac{1}{3}x+\frac{22}{3}&&\quad\\ \iff\quad&& \frac{2}{3}x&=\frac{28}{3}\\ \iff\quad&& x&=14. \end{align*}\]

The corresponding \(y\) value is then \(y=14-2=12\), so \(C\) has coordinates \((14,12)\).

Going from \(B\) to \(C\) is the same translation as going from \(A\) to \(D\). (In terms of vectors, \(\overrightarrow{BC}=\overrightarrow{AD}\).) To get from \(B (2,8)\) to \(C (14,12)\), we move \(12\) units to the right and \(4\) units up.

So if we start at \(A (4,2)\) and move \(12\) units to the right and \(4\) units up, we arrive at \(D(16,6)\).

The length of the side

\(AB\)

can be calculated using Pythagoras’ theorem, giving

\[\begin{align*} AB &= \sqrt{(x_A-x_B)^2+(y_A-y_B)^2}\\ &= \sqrt{(2)^2+(-6)^2}\\ &= \sqrt{40}\\ &= 2\sqrt{10}. \end{align*}\]

In the same way we can find

\(BC\)

:

\[\begin{align*} BC &= \sqrt{(x_B-x_C)^2+(y_B-y_C)^2} \\ &= \sqrt{(-12)^2+(-4)^2} \\ &=\sqrt{160}\\ &= 4\sqrt{10}. \end{align*}\]

If we multiply the two side lengths of our rectangle, we find its area. We therefore have

\[\begin{align*} \text{area} &=AB \times BC \\ &= 2\sqrt{10} \times 4\sqrt{10} \\ &= 8\times10 \\ &= 80. \end{align*}\]

Here you can see a complete sketch of the rectangle.
