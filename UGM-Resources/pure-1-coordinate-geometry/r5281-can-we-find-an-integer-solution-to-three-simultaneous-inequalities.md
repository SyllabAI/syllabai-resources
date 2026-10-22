---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/geometry-of-equations/r5281
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- geometry-of-equations
- type/review-question
resource_identity:
  ugm_id: r5281
  station: geometry-of-equations
  station_title: Geometry of Equations
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5281
  old_site_id: Q1016
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
      evidence: 'Three simultaneous linear inequalities deduce bounds on x and y — region reading of boundary lines; linear inequality regions are IGCSE-flavoured extension (rec'
      rationale: 'Canonical UGM title: “Can we find an integer solution to three simultaneous inequalities?”; exam provenance: UCLES 1958 Q1'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1958 Q1
task: T-UGM-IMPORT-3
---

# Can we find an integer solution to three simultaneous inequalities?

## Question

From the inequalities \[y-2x>0,\qquad x+y>3,\qquad 2y-x<5\] deduce that \[\frac{1}{3}< x < \frac{5}{3},\qquad 2< y <\frac{10}{3},\] and hence that the given inequalities cannot be satisfied simultaneously by integral values of \(x\) and \(y\).

[*The phrase ‘integral values’ means the same as ‘integer values’.* ]

## Suggestion

Where do the three lines

\[\begin{align*} y-2x &= 0 \\ x+y &=3 \\ 2y-x &=5 \end{align*}\]

lie in the plane?

On which side of each of these lines does the respective inequality hold?

… and hence that the given inequalities cannot be satisfied simultaneously by integral values of \(x\) and \(y\).

Which integer values of \(x\) and \(y\) do we need to consider?

## Solution

From the inequalities \[y-2x>0,\qquad x+y>3,\qquad 2y-x<5\] deduce that \[\frac{1}{3}< x < \frac{5}{3},\qquad 2< y <\frac{10}{3}\]

Consider the three inequalities in the plane:

- \(y-2x = 0\) crosses the axes at \((0,0)\) and has gradient \(2\) (it rearranges to \(y=2x\)). The region \(y-2x>0\) lies above this line, as it includes the point \((0,1)\).

- \(x+y =3\) crosses the axes at \((0,3)\) and \((3,0)\). The region \(x+y>3\) lies above this line, as it does not include the point \((0,0)\).

- \(2y-x =5\) crosses the axes at \((0,\frac52)\) and \((-5,0)\). The region \(2y-x<5\) lies below this line, as it includes the point \((0,0)\).

We can therefore sketch these three regions in the plane. Here the shaded regions are those which **do not** satisfy the inequality.

We can see from our sketch that there is a small triangular region satisfied by all three inequalities. We determine where each pair of lines intersects in order to determine the coordinates of the vertices of this triangle.

\[\begin{align*} y=2x\quad&\text{and}\quad x+y=3 \quad &\Longrightarrow \quad&& x&=1,& y&=2 \\ y=2x\quad&\text{and}\quad 2y-x=5 \quad &\Longrightarrow \quad&& x&=\tfrac53,& y&=\tfrac{10}{3} \\ x+y=3\quad&\text{and}\quad 2y-x=5 \quad &\Longrightarrow \quad&& x&=\tfrac13,& y&=\tfrac{8}{3} \end{align*}\]

From these we can deduce the minumum and maximum extent of both \(x\) and \(y\): \[\frac{1}{3} < x < \frac{5}{3}, \qquad 2< y < \frac{10}{3},\] as required.

… and hence that the given inequalities cannot be satisfied simultaneously by integral values of \(x\) and \(y\).

The only integer value of \(x\) that satisfies \(\frac{1}{3} < x < \frac{5}{3}\) is \(x=1\).

The only integer value of \(y\) that satisfies \(2< y < \frac{10}{3}\) is \(y=3\).

Does the point

\((1,3)\)

obey all three inequalities simultaneously?

\[\begin{align*} y-2x &> 0: \quad 3-2=1>0 \quad \checkmark \\ x+y &>3: \quad 1+3=4>3 \quad \checkmark \\ 2y-x &<5: \quad 6-1=5 \nless 5 \quad \mathsf{X} \end{align*}\]

Thus there is no integer pair of \(x\) and \(y\) that satisfies all three inequalities simultaneously.
