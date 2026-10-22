---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/circles/r7979
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- circles
- type/review-question
resource_identity:
  ugm_id: r7979
  station: circles
  station_title: Circles
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7979
  old_site_id: Q222
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: circles
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: circles
    validation_status: SUGGESTED
  spec_points: []
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md rule 3: coverage is never manufactured)'
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford (MAT) 2012 Q4
task: T-UGM-IMPORT-3
---

# When does a circle touch a parabola twice?

## Question

The diagram below shows the parabola \(y=x^2\) and a circle with centre \((0,2)\) just ‘resting’ on the parabola. By ‘resting’ we mean that the circle and parabola are tangential to each other at the points \(A\) and \(B\).

1. Let \((x,y)\) be a point on the parabola such that \(x \ne 0\). Show that the gradient of the line joining this point to the centre of the circle is given by \[\frac{x^2-2}{x}.\]

---

1. With the help of the result from the first part, or otherwise, show that the coordinates of \(B\) are given by \[\left(\sqrt{\frac{3}{2}},\frac{3}{2} \right).\]

---

1. Show that the area of the sector of the circle enclosed by the radius to \(A\), the minor arc \(AB\) and the radius to \(B\) is equal to \[\frac{7}{4} \cos^{-1} \left( \frac{1}{\sqrt{7}} \right) .\]

---

1. Suppose now that a circle with centre \((0,a)\) is resting on the parabola, where \(a > 0\). Find the range of values of \(a\) for which the circle and parabola touch at two distinct points.

---

1. Let \(r\) be the radius of a circle with centre \((0,a)\) that is resting on the parabola. Express \(a\) as a function of \(r\), distinguishing between the cases in which the circle is, and is not, in contact with the vertex of the parabola.

## Suggestion

What is the condition for a circle to be tangent to a line?

## Solution

The line segment joining the point \((x,x^2)\) and the centre of the circle \(C=(0,2)\) will have gradient \[\frac{x^2 - 2}{x - 0} = \frac{x^2 - 2}{x}.\] (Note that \(x \ne 0\), so we are not dividing by zero.)

For the circle to be tangent to the parabola at \(B\), the radius through \(B\) and the tangent to the parabola at \(B\) must be perpendicular.

Suppose \(B\) has coordinates \((b,b^2)\). Then the gradient of the parabola (and circle) at \(B\) is equal to \(2b\) (by differentiating the equation \(y=x^2\)).

We know the gradient of the radius through \(B\) from part (i), so we must have \[\frac{b^2 - 2}{b} =\frac{-1}{2b}\] (as perpendicular gradients multiply to \(-1\), which is the same as saying that one is the negative reciprocal of the other).

We can solve this by multiplying by \(2b\) to get \[2b^2 - 4 = -1,\] so \(b=\pm\sqrt{\dfrac{3}{2}}\). Since we must have \(b>0\) (from the diagram), we obtain \(b=\sqrt{\dfrac{3}{2}}\) and \(b^2 = \dfrac{3}{2}\), as required.

We draw on a right-angled triangle to help us here:

The square of the radius \(CB\) is \[r^2=\left(\sqrt{\frac{3}{2}}\right)^2+\left(\frac{3}{2}-2\right)^2= \frac{7}{4}\] and so the area of the circle is \(\pi r^2 = \dfrac{7}{4} \pi\).

The angle \(\theta\) is given by \[\cos\theta=\frac{2-\frac{3}{2}}{\sqrt{\frac{7}{4}}}=\frac{\frac{1}{2}}{\frac{1}{2}\sqrt{7}}=\frac{1}{\sqrt{7}}\] so \(\theta=\cos^{-1}(1/\sqrt{7})\).

The area of the sector is given by \(\dfrac{1}{2}r^2(2\theta)\), as the angle \(\angle ACB\) is \(2\theta\) by symmetry. Using our value of \(r^2\), we get \[\text{area}=\frac{1}{2}\times\frac{7}{4}\times2\cos^{-1}\left(\frac{1}{\sqrt{7}}\right)=\frac{7}{4}\cos^{-1}\left(\frac{1}{\sqrt{7}}\right)\] as required.

We now need to think about a new diagram:

We consider an equation similar to that in part (ii), except with \(2\) replaced with a more general \(a\): \[\frac{b^2 - a}{b} =\frac{-1}{2b}.\] The solutions of this equation will be the intersections of the circle and parabola, and they will have the same gradient at these points, so the two will just touch.

We multiply by \(b\) and rearrange the equation to get \[b^2=a-\frac{1}{2},\] which has two distinct real solutions if and only if \(a>\dfrac{1}{2}\).

If \(0<a\le \dfrac{1}{2}\), then we know from part (iv) that the circle is resting on the vertex of the parabola, since it does not touch it in two places. In this case, it is clear that as the circle passes through \((0,0)\) and has its centre at \((0,a)\), its radius must be \(a\), so \(a=r\).

If

\(a>\dfrac{1}{2}\)

, then there are two distinct points of contact, and we have

\[r^2=b^2+(b^2-a)^2,\]

where

\(b\)

is given by the formula in part (iv):

\[b^2=a-\frac{1}{2}.\]

Substituting this in, we find that

\[\begin{align*} r^2&{}=\left(a-\frac{1}{2}\right)+\left(a-\frac{1}{2}-a\right)^2\\ &{}=a-\frac{1}{2}+\frac{1}{4}\\ &{}=a-\frac{1}{4} \end{align*}\]

so that \[a=r^2+\frac{1}{4}.\]

As a check, when \(r=\dfrac{1}{2}\), which is the boundary between the two cases, the second formula gives \[a=\frac{1}{4}+\frac{1}{4}=\frac{1}{2}=r,\] which is the same answer as given by the first formula.
