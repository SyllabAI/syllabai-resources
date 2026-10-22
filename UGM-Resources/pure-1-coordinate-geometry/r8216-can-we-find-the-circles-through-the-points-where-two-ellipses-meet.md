---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/circles/r8216
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- circles
- type/review-question
resource_identity:
  ugm_id: r8216
  station: circles
  station_title: Circles
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8216
  old_site_id: Q11
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
  exam_reference: UCLES 2002 Q1
task: T-UGM-IMPORT-3
---

# Can we find the circles through the points where two ellipses meet?

## Question

Show that the equation of any circle passing through the points of intersection of the [ellipse](https://undergroundmathematics.org/glossary/ellipse) \[(x + 2)^2 + 2y^2 = 18\] and the ellipse \[9(x - 1)^2 + 16y^2 = 25\] can be written in the form \[x^2 - 2ax + y^2 = 5 - 4a.\]

## Suggestion

Can we sketch the ellipses roughly? In how many points will the two ellipses meet? How can we find these points?

Where will the centres of circles going through the intersection points lie?

Interactive diagram

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/gJ7mVUv9)

The two ellipses appear here in red. A possible circle through their intersections is in blue.

## Solution

To get some sense of what is going on in this question, it is helpful to sketch a graph.

Both ellipses are symmetrical in the \(x\)-axis, since replacing \(y\) with \(-y\) makes no difference to the equations.

The second ellipse is symmetrical in the line \(x=1\), since if we substitute in \(x=1+k\) and \(x=1-k\) into the equation, we obtain the same values for \(y\). Likewise, the first ellipse is symmetrical in \(x = -2\). (For more on this idea, have a look at [Quadratic symmetry](https://undergroundmathematics.org/quadratics/quad-symmetry).)

If we put \(x = 0\), and then \(y = 0\) into each equation, we can find the intercepts with the axes.

Alternatively, we could observe that the centre of the first ellipse lies at \((-2,0)\) and its [semi-axes](https://undergroundmathematics.org/glossary/semi-major-axis) have length \(\sqrt{18}=3\sqrt{2}\) in the \(x\)-direction and \(\sqrt{9}=3\) in the \(y\)-direction. Likewise, the second ellipse has centre \((1,0)\) and semi-axes \(\frac53\) and \(\frac54\).

Either of these approaches gives us enough information to sketch the ellipses.

(Though it is not obvious without a calculator whether \(-2+3\sqrt{2}<\frac83\) or not, the question does tell us that the ellipses intersect. Our calculation of their point of intersection will then prove that they do, indeed, intersect, and it will follow that \(-2+3\sqrt{2}<\frac83\).)

We can now tackle the question asked.

We find the points of intersection of the two ellipses by solving the simultaneous equations \[(x + 2)^2 + 2y^2 = 18\] and \[9(x - 1)^2 + 16y^2 = 25.\]

We can eliminate

\(y\)

by multiplying the first equation by

\(8\)

and subtracting the second equation, giving

\[\begin{align*} && 8(x + 2)^2 - 9(x - 1)^2 &= 144 - 25&&\quad\\ \iff\quad && 8x^2 + 32x + 32 - 9x^2 + 18x - 9 &= 119\\ \iff\quad && x^2 - 50x + 96 &= 0\\ \iff\quad && (x - 2)(x - 48) &= 0. \end{align*}\]

This gives the \(x\)-value of the points of intersection as either \(2\) or \(48\).

It is clear from our sketch that \(x=48\) does not correspond to real points of intersection. (There are, though, [complex](https://undergroundmathematics.org/glossary/complex-number) points of intersection.) So we must have \(x=2\). (We could also find this by substituting \(x=48\) into the equation of the ellipse and discovering that there are no real values of \(y\) corresponding to it.)

Taking

\(x = 2\)

and substituting into the first simultaneous equation, we have

\[\begin{align*} && 16 + 2y^2 &= 18&&\quad\\ \iff\quad&& y^2 &= 1\\ \iff\quad&& y &= \pm1. \end{align*}\]

Hence there are two (real) points of intersection, at \((2,1)\) and \((2,-1)\). (It’s easy to check that these points really do lie on both ellipses).

A circle through both these points has centre \((a,0)\) on the \(x\)-axis, by symmetry.

Then the equation of the circle is \[(x - a)^2 + y^2 = (2-a)^2+1.\] The right-hand side here is the distance of the centre from \((2,1)\), or from \((2,-1)\), squared.

Expanding gives

\[\begin{align*} && x^2 - 2ax + a^2 + y^2 &= 5 - 4a + a^2&&\quad\\ \iff\quad&& x^2 - 2ax + y^2 &= 5 - 4a, \end{align*}\]

as required.

These circles form a system of *coaxal circles*; you might like to explore this concept further.
