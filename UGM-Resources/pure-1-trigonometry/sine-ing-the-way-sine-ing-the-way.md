---
created: 2026-10-23T16:39:11 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/sine-ing-the-way
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-triangles-to-functions
- type/scaffolded-task
- level/developing
resource_identity:
  ugm_id: sine-ing-the-way
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 3
  resource_type_label: Scaffolded task
  level: Developing
  ref: 6079
  old_site_id: G1_RT5_1
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: trigonometry-triangles-to-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: trigonometry-triangles-to-functions
    validation_status: SUGGESTED
  spec_points: []
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md rule
    3: coverage is never manufactured)'
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-5
assets:
- path: https://undergroundmathematics.org/trigonometry-triangles-to-functions/sine-ing-the-way/download/teacher-notes.pdf
  kind: printable
---

# Sine-ing the way

> Excerpt: This resource reminds students of their knowledge of angles in circles before leading them through an elegant proof of the Sine Rule which incorporates the use of circle theorems. It also gives an interesting relationship between a triangle and the diameter of its circumcircle.

## Warm-up

Try to label as many angles in the diagram above as you can, using the fewest possible number of unknowns to represent them.

Suggestion

You can label all of the angles using only two different letters.

## Warm-up Solution

Try to label as many angles in the diagram above as you can, using the fewest possible number of unknowns to represent them.

We have two angles at \(B\) and \(C\) that are subtended by the same arc, so the angles at \(B\) and \(C\) must be equal.

Also we have triangle \(ABD\) which has its longest side as the diameter of the circle, meaning angle \(BAD\) is a right-angle.

Just as the angles at \(B\) and \(C\) are the same, then so are the angles \(BAC\) and \(BDC\). If we label our two different angles \(\theta\) and \(\alpha\) then we have the following.

From here we can now write all the angles in terms of \(\theta\) and \(\alpha\) using our knowledge of triangles, to give us;

## Problem

We take a circle and inscribe a triangle in it.

Complete the steps of the table below to find an interesting relationship between the angles and sides of this triangle.

| Diagram | Description |
|---|---|
|  | 1. Add a point \(C'\) on the circumference of the circle, so that \(\angle C'AB\) is a right-angle. 2. What is the relationship between angles \(ACB\) and \(AC'B\) ? 3. What is the length \(C'B\) ? |
|  | 4. Label side \(AB\) as \(c\) . Write a relationship between \(c\) and the angle at \(C'\) . |
|  | 5. Can you therefore write a relationship between \(c\) and the angle at \(C\) ? |
|  | 6. Starting from the original diagram, add a point \(B'\) on the circumference of the circle, so that \(\angle B'CA\) is a right-angle. 7. What is the relationship between angles \(ABC\) and \(AB'C\) ? 8. What is the length \(B'A\) ? |
|  | 9. Label side \(AC\) as \(b\) . Write a relationship between \(b\) and the angle at \(B'\) . |
|  | 10. Therefore write a relationship between \(b\) and the angle at \(B\) . |
|  | 11. In general, what can we now say about the relationship between the sides and angles of a triangle? |

You have proved your statement for this particular triangle, which has its three vertices on the circumference of a circle. Is your statement true for all triangles?

If you are not sure, you might like to look at [Finding circles](https://undergroundmathematics.org/circles/finding-circles).

## Suggestion

If you require help with of the steps, then click on the appropriate button below.

Suggestion for step 2

What do you know about angles on the circumference that are subtended by the same arc? Look back to the warm-up if you are unsure.

Suggestion for step 3

You may need to use other unknowns.

Suggestion for step 4

Suggestion for step 7

## Solution

| Diagram | Description |
|---|---|
|  | 1. Add a point \(C'\) on the circumference of the circle, so that \(\angle C'AB\) is a right-angle. 2. What is the relationship between angles \(ACB\) and \(AC'B\) ? \(\color{blue}{\angle AC'B = \angle ACB}\) \(\color{blue}{\text{as they are angles on the circumference}}\) \(\color{blue}{\text{subtended by the same arc.}}\) 3. What is the length \(C'B\) ? \(\color{blue}{C'B = 2R}\) \(\color{blue}{\text{where }R = \text{radius}.}\) |
|  | 4. Label side \(AB\) as \(c\) . Write a relationship between \(c\) and \(C'\) . \(\color{blue}{\sin{C'} = \dfrac{c}{2R}}\) |
|  | 5. Can you therefore write a relationship between \(c\) and the angle at \(C\) ? \(\color{blue}{\text{As $C = C'$ and $\sin{C'} = \dfrac{c}{2r}$,}}\) \(\color{blue}{\text{then}}\) \(\color{blue}{\sin{C} = \dfrac{c}{2R}}\) . |
|  | 6. Starting from the original diagram, can you add a point \(B'\) on the circumference of the circle, so that \(\angle B'CA\) is a right-angle? 7. What is the relationship between angles \(ABC\) and \(AB'C\) ? \(\color{blue}{\angle CB'A = \angle CBA}\) \(\color{blue}{\text{as before.}}\) 8. What is the length of \(B'A\) ? \(\color{blue}{B'A = 2R}\) |
|  | 9. Label side \(AC\) as \(b\) . Write a relationship between \(b\) and the angle at \(B'\) . \(\color{blue}{\sin{B'} = \dfrac{b}{2R}}\) 10. Therefore write a relationship between \(b\) and the angle at \(B\) . \(\color{blue}{\text{As $B = B'$ and $\sin{B'} = \dfrac{b}{2R}$,}}\) \(\color{blue}{\text{then}}\) \(\color{blue}{\sin{B} = \dfrac{b}{2R}.}\) |

If we did this for a third time, for point \(A\), then we would get

\[\sin{A} = \dfrac{a}{2R}.\]

Did you notice that we didn’t even need to do this for a second time with point \(B\)? We could have chosen to label our triangle in any way we like, so our reasoning from steps one to five is symmetrical for points \(C\), \(B\) and \(A\).

So we now have three statements linking the side of a triangle with its opposite angle:

\[\sin{A} = \dfrac{a}{2R},\] \[\sin{B} = \dfrac{b}{2R},\] \[\sin{C} = \dfrac{c}{2R}.\]

Rearranging these gives us

\[2R = \dfrac{a}{\sin{A}}=\dfrac{b}{\sin{B}}=\dfrac{c}{\sin{C}}.\]

You are probably familiar with most of this statement, and see that we have proved the [sine rule](https://undergroundmathematics.org/glossary/sine-rule). However, the fact that this common ratio also equals \(2r\) may be unfamiliar.

We have uncovered the relationship, \[2R = \dfrac{a}{\sin{A}}=\dfrac{b}{\sin{B}}=\dfrac{c}{\sin{C}},\] where \(r\) is the radius of the circle that passes through the vertices of the triangle.

This relationship is true for all triangles, as we can always draw a circle through the three vertices of a triangle. This is called the *circumcircle* of the triangle, and its centre is known as the *circumcentre* of the triangle. This is one of many different ways to define the centre of a triangle.

In addition to this, if we begin with a fixed circle, then any triangle we inscribe within it will have the property that \(\dfrac{a}{\sin A}=\dotsb=2R\), a fixed number! So this relationship is *invariant*: it holds for all such triangles, regardless of their side lengths or angles, as long as it remains inscribed in our fixed circle.
