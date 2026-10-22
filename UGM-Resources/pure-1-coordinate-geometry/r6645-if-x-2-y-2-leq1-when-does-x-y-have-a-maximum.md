---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/circles/r6645
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- circles
- type/review-question
resource_identity:
  ugm_id: r6645
  station: circles
  station_title: Circles
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6645
  old_site_id: Q171
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
  exam_reference: Oxford (MAT) 2011 Q4
task: T-UGM-IMPORT-3
---

# If $x^2+y^2\leq1$, when does $x+y$ have a maximum?

## Question

Let \(Q\) denote the quarter-disc of points \((x,y)\) such that \(x\geq 0\), \(y\geq 0\) and \(x^2+y^2\leq1\) as drawn in Figures A and B below.

Figure A

Figure B

1. On the axes in Figure A, sketch the graphs of \[x+y=\frac{1}{2}, \qquad x+y=1, \qquad x+y=\frac{3}{2}.\] What is the largest value of \(x+y\) achieved at points \((x,y)\) in \(Q\)? Justify your answer.

---

1. On the axes in Figure B, sketch the graphs of \[xy=\frac{1}{4}, \qquad xy=1, \qquad xy=2.\] What is the largest value of \(x^2+y^2+4xy\) achieved at points \((x,y)\) in \(Q\)? What is the largest value of \(x^2+y^2-6xy\) achieved at points \((x,y)\) in \(Q\)?

---

1. Describe the curve \[x^2+y^2-4x-2y=k\] where \(k>-5\). What is the smallest value of \(x^2+y^2-4x-2y\) achieved at points \((x,y)\) in \(Q\)?

## Suggestion

What do we observe in Figure A after drawing the three graphs? How are they related?

Is this part of the question similar to the previous part in any way?

How could we use the diagram to solve the problem?

*‘If the largest values of two functions, say \(f\) and \(g\), are \(\alpha\) and \(\beta\), and \(f+g\) can take the value \(\alpha+\beta\), then the largest value of \(f+g\) is \(\alpha+\beta\).’*

Is this logic okay?

What similar statement can we make about the largest value of \(f-g\)?

How else can we write \(x^2+y^2-4x-2y=k\)? What curve does this look like?

## Solution

Figure A

As we can observe, the line \(x+y=k\) will see its largest value for \(k\) when the graph is tangent to \(Q\), that is, when the line is the furthest possible from the origin that still intersects the region.

Hence we want the value of \(k\) such that the pair of simultaneous equations \(x+y=k, x^2+y^2=1\) have a unique solution.

We have \(x^2+(k-x)^2=1\), or \(2x^2-2kx+k^2-1 =0\), which must have a discriminant of zero when viewed as a quadratic in \(x\).

Thus \(4k^2-8(k^2-1)=0\), and so \(k = \sqrt{2}\), and \(x=y=\dfrac{\sqrt2}{2}\). Hence, the largest value of \(x+y\) on \(Q\) is \(\sqrt{2}\).

Figure B

Similarly as above, \(xy\) will achieve its maximum value on \(Q\) when \(x=y=\dfrac{\sqrt2}{2}\), when \(xy\) will be \(\dfrac{1}{2}\).

Since the maximum value of \(x^2+y^2\) in \(Q\) is \(1\), the largest value of \(x^2+y^2+4xy\) on \(Q\) is \(1+4\times \dfrac{1}{2}=3\).

In order to get the largest value of \(x^2+y^2-6xy\) we need the largest value of \(x^2+y^2\), which is \(1\), and the smallest value of \(6xy\), which is \(0\).

So the largest value of \(x^2+y^2-6xy\) on \(Q\) is \(1-0=1\), achieved, for instance, at \(x=1\) and \(y=0\).

The curve’s equation can be rewritten on completing the square as \[(x^2-4x+4)+(y^2-2y+1)=k+5\] which becomes \[(x-2)^2+(y-1)^2=k+5,\] so it describes a circle of centre \((2,1)\) and radius \(\sqrt{k+5}\). So \(k\) is smaller if \((x,y)\) is closer to \((2,1)\).

In order to find the smallest value of \(x^2+y^2-4x-2y\) achieved at points \((x,y)\) in \(Q\), we should find the closest point to \((2,1)\) in \(Q\).

Since \(Q\) is the quadrant of the disc \(x^2+y^2\le 1\) in the positive quadrant of the plane, and \((2,1)\) is in that same quadrant, the closest point can be obtained by drawing the straight line connecting the points \((0,0)\) and \((2,1)\), and finding where this intersects with the circumference of \(Q\).

Therefore the result will be the solution of the simultaneous equations \[x-2y=0 \quad\text{and}\quad x^2+y^2=1.\] By substituting \(x=2y\) into the second equation, we get \[5y^2=1\Longrightarrow y=\frac{1}{\sqrt5},\] so \(x = \dfrac{2}{\sqrt5}\). So the smallest value of \(x^2+y^2-4x-2y\) is \[k=1-4\frac{2}{\sqrt5}-2\frac{1}{\sqrt5}=1-\frac{10}{\sqrt5}=1-2\sqrt5,\] where we have substituted for \(x\) and \(y\) into \(x^2+y^2-4x-2y\), noting as a check that \(x^2+y^2=1\).
