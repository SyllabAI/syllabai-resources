---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/geometry-of-equations/r5255
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- geometry-of-equations
- type/review-question
resource_identity:
  ugm_id: r5255
  station: geometry-of-equations
  station_title: Geometry of Equations
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5255
  old_site_id: Q4042
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
      evidence: 'Locus of the intersection of x+y=t and y=tx as t varies; intersection coordinates in terms of t; the locus equation rides quadratics.'
      rationale: 'Canonical UGM title: “What''s the locus of the intersection of these variable lines?”; exam provenance: UCLES 1978 Q14'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1978 Q14
task: T-UGM-IMPORT-3
---

# What's the locus of the intersection of these variable lines?

## Question

The line \(x+y=t\) meets the line \(y=tx\) at the point \(P\). Find the coordinates of \(P\) in terms of \(t\). Hence, or otherwise, show that the equation of the locus of \(P\) as \(t\) varies is \(x^2+xy-y=0\). At the point on the locus where \(x=3\), find the value of \(y\) and the value of \(t\).

## Solution

We’d like to find the intersection of the two lines, and we’d like expressions for the

\(x\)

-coordinate and

\(y\)

-coordinate in terms of

\(t\)

. We already have an expression for

\(y\)

in terms of

\(t\)

and

\(x\)

, so the least work for us is to replace the

\(y\)

in

\(x+y=t\)

with

\(y=tx\)

and proceed from there.

\[\begin{align*} &&x+tx&=t,&&\quad \\ \Longrightarrow\quad&& x(1+t)&=t\\ \Longrightarrow\quad&& x&=\frac{t}{1+t}. \end{align*}\]

Can you see why \(t\) cannot be \(-1\)?

Since \(y=tx\), we see that \[y=\frac{t^2}{1+t}.\] Therefore, \[P=\left(\frac{t}{1+t},\frac{t^2}{1+t}\right).\]

Since we would like to end up with an expression in \(x\) and \(y\), let’s try to eliminate \(t\) from \(y=tx\) and \(x+y=t\). This gives us \[y=(x+y)x,\] which when we rearrange, is the equation \[x^2+xy-y=0.\]

Alternatively, we could substitute our coordinates for

\(P\)

into the given equation:

\[\begin{align*} x^2+xy-y&=\left(\frac{t\vphantom{t^2}}{1+t}\right)^2+\left(\frac{t\vphantom{t^2}}{1+t}\right)\left(\frac{t^2}{1+t}\right)-\left(\frac{t^2}{1+t}\right)\\ &=\frac{t^2}{(1+t)^2}+\frac{t^3}{(1+t)^2}-\frac{t^2(1+t)}{(1+t)^2}\\ &=\frac{t^2+t^3-(t^2+t^3)}{(1+t)^2}\\ &=0. \end{align*}\]

To find \(y\), let’s use \(x^2+xy-y=0\). When \(x=3\), this becomes \[9+3y-y=0,\] which means that \[y=-\frac{9}{2}.\] Since \(x+y=t\), we can use \(x=3\) and \(y=-\frac{9}{2}\) to find that \(t=-\frac{3}{2}\).

It’s always worth checking your answer if you have more than one equation that your variables should satisfy. For example, we could check that our values of \(x\), \(y\) and \(t\) satisfy \(y=tx\). We could also have used this equation to determine \(t\), and then used \(x+y=t\) as a check.

The following GeoGebra applet helps us to see what is happening. The blue line is \(y=tx\), the red line is \(x+y=t\). What happens when \(t=-1\)?

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/s4NTW2Sp)
