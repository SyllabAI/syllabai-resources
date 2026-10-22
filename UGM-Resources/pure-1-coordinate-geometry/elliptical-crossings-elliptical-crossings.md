---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/circles/elliptical-crossings
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- circles
- type/package-of-problems
- level/developing
resource_identity:
  ugm_id: elliptical-crossings
  station: circles
  station_title: Circles
  resource_type_id: 5
  resource_type_label: Package of problems
  level: Developing
  ref: 7710
  old_site_id: E1_RT7_7
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
task: T-UGM-IMPORT-3
assets:
- path: https://undergroundmathematics.org/circles/elliptical-crossings/download/teacher-notes.pdf
  kind: printable
---

# Elliptical crossings

> Excerpt: Students are asked to describe the behaviour of the midpoint of the line segment formed by the intersection of a straight line with a particular ellipse.

## Problem

This diagram shows the ellipse with equation \(x^2+4y^2=16\) together with the straight line \(y=x+c\).

The line and ellipse intersect at the points \(A\) and \(B\), and the midpoint of \(AB\) is \(M\).

Find the coordinates of \(M\) for some different values of \(c\).

What do you notice?

Suggestion

What would be a simple value of \(c\) to choose first?

If you have found an \(x\) or \(y\) value, which equation is simplest to use to find the other one?

Remember that the coordinates of \(M\) are the average (mean) of the coordinates of \(A\) and \(B\).

What would happen if you used straight lines of a different gradient instead?

## Things you might have noticed

Let’s say we begin by considering the case where \(c=1\), so we have the two equations \(x^2+4y^2=16\) and \(y=x+1\).

Before we continue, let’s just stop and think. Why did we choose \(c=1\)?

- What does the case where \(c=1\) look like in the diagram?

- What other values of \(c\) could we have chosen?

- Are there any values of \(c\) that you would not choose? Why?

To find the coordinates of

\(A\)

and

\(B\)

, we substitute

\(y=x+1\)

into the quadratic to get

\[x^2+4(x+1)^2=16.\]

If we expand the brackets and rearrange, we get the quadratic

\[\begin{equation}\label{eq:eg} 5x^2+8x-12=0. \end{equation}\]

We can use the formula to find the solutions of this quadratic: they are \[x=\frac{-8\pm\sqrt{8^2+4\times5\times12}}{10}.\] We could simplify this, but instead we notice that these two solutions are the \(x\)-coordinates of \(A\) and \(B\). As the \(x\)-coordinate of \(M\) is the mean of these, we only need to add them together and halve the answer. When we add the two solutions together, the square roots cancel and we are left with \(\frac{-8}{10}+\frac{-8}{10}\). So the \(x\)-coordinate of \(M\) is half of this, which is \(\frac{-8}{10}=-\frac{4}{5}\).

Since \(M\) lies on the straight line \(y=x+1\), it follows that the \(y\)-coordinate of \(M\) is \(-\frac{4}{5}+1=\frac{1}{5}\). Hence \(M\) has coordinates \(\bigl(-\frac{4}{5}, \frac{1}{5}\bigr)\).

We could have been even more sneaky in saving work for ourselves!

If we begin to complete the square for the quadratic in equation \(\eqref{eq:eg}\), we have \[5x^2+8x-12=5\bigl(x^2+\tfrac{8}{5}x\bigr)-12=5\bigl(x+\tfrac{4}{5}\bigr)^2+k\] for some number \(k\). The graph \(y=5x^2+8x-12\) therefore has a line of symmetry \(x=-\frac{4}{5}\) and so the two solutions are symmetrically placed about this \(x\)-value, as shown in this sketch. It follows that their mean is \(-\frac{4}{5}\).

And we could do this algebraically, too. If we write \[5x^2+8x-12=5(x-\alpha)(x-\beta)=5(x^2-(\alpha+\beta)x+\alpha\beta),\] where the solutions (or roots) of the quadratic are \(\alpha\) and \(\beta\), then we see that \(-5(\alpha+\beta)=8\), so the sum of the roots is \(-\frac85\), and their mean is \(-\frac45\).

In the example above, we used \(c=1\) and found that \(M\) had coordinates \(\bigl(-\tfrac{4}{5},\tfrac{1}{5}\bigr)\). When you use other values of \(c\), you may find that the coordinates are also quite simple. There does seem to be an interesting pattern to the coordinates: what happens if you plot them?

What is the locus of \(M\)?

The locus of \(M\)

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/kYKSGF44)

- What is the locus of \(M\) in these cases?

- Can you find a relation between the gradient of the straight lines and the locus of \(M\)?

A partial solution

A straight line through the centre of an ellipse is called a *diameter* of the ellipse.

The diameter \(y=mx\) and the locus of \(M\) are called *conjugate diameters*. There are some fascinating theorems about conjugate diameters of an ellipse, which you might wish to research further.

This problem considered an ellipse. You might find it interesting to compare this with your answer to [Parabella](https://undergroundmathematics.org/quadratics/parabella). You could also try answering the same question for a [hyperbola](https://undergroundmathematics.org/glossary/hyperbola) such as \(x^2-4y^2=16\), which is the other type of [conic section](https://undergroundmathematics.org/glossary/conic). Does that also give a similar answer? If so, why, and if not, why not?

## A certain point of view

This diagram shows the ellipse with equation \(x^2+4y^2=16\) together with the straight line \(y=x+c\).

The line and ellipse intersect at the points \(A\) and \(B\), and the midpoint of \(AB\) is \(M\).

Find the coordinates of \(M\) for some different values of \(c\).

What do you notice?

What is the locus of \(M\) as \(c\) varies?

What would happen if you used straight lines of a different gradient instead?

The ellipse looks like a stretched circle: it is the circle \(x^2+y^2=4\) stretched by a factor of \(2\) in the \(x\)-direction.

What happens to the problem when we undo the stretch, by stretching by a factor of \(\frac12\) in the \(x\)-direction?

Suggestion

- What happens to the straight line \(y=x+c\) when we stretch it by a factor of \(\frac12\) in the \(x\)-direction?

- What happens to the points \(A\), \(B\) and \(M\) when we do this stretch? Is \(M\) still the midpoint of \(AB\) after the stretch?

- Can you use this information to work out the locus of \(M\) in the stretched version as \(c\) changes (without using any equation for the locus that you have already worked out)?

- Can you use your answers to work out the equation of the locus of \(M\) in the original problem?

- What would your answers be if the original straight lines had equations \(y=2x+c\) instead? Or, more generally, \(y=mx+c\) for a fixed value of \(m\)?
