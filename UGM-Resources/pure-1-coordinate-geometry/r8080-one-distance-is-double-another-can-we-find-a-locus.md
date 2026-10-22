---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/geometry-of-equations/r8080
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- geometry-of-equations
- type/review-question
resource_identity:
  ugm_id: r8080
  station: geometry-of-equations
  station_title: Geometry of Equations
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8080
  old_site_id: Q1070
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
      evidence: 'PA=2PB with A(0,3), B(0,-3) -> x^2+y^2+10y+9=0 — distance-ratio locus to circle equation; the completing-the-square step rides 1.1.1.'
      rationale: 'Canonical UGM title: “One distance is double another; can we find a locus?”; exam provenance: UCLES 1985 Q16(b)'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1985 Q16(b)
task: T-UGM-IMPORT-3
---

# One distance is double another; can we find a locus?

## Question

Given that \(A\) is the point \((0,3)\) and \(B\) is the point \((0,-3)\), a point \(P(x,y)\) moves so that \(PA=2PB\). Show that the equation of the locus of \(P\) is \[x^2 + y^2 +10y + 9 = 0.\]

## Suggestion

How can we work out the distances \(PA\) and \(PB\) (in terms of \(x\) and \(y\))?

In this applet, changing \(\theta\) will move \(P\), such that \(PA = 2PB\). What shape is the locus of \(P\)?

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/BRGK7Rsj)

## Solution

The point

\(P\)

has the coordinates

\((x,y)\)

, so we can apply Pythagoras’ theorem to find the distances

\[\begin{align*} PA&=\sqrt{x^2 + (y-3)^2}\\ PB&=\sqrt{x^2 + (y+3)^2}, \end{align*}\]

as seen in this sketch:

We can now insert the expressions for \(PA\) and \(PB\) into the constraint \(PA=2PB\), giving \[\sqrt{x^2 + (y-3)^2} = 2\sqrt{x^2 + (y+3)^2}.\]

Next, we square both sides and expand the brackets. We have

\[\begin{align*} &&\sqrt{x^2 + (y-3)^2} &= 2\sqrt{x^2 + (y+3)^2}&&\quad\\ \implies\quad&& x^2 + (y-3)^2 &= 4x^2 + 4(y+3)^2\\ \implies\quad&& x^2 + y^2-6y+9&=4x^2+4y^2+24y+36. \end{align*}\]

Collecting like terms gives \[3x^2 + 3y^2 + 30y + 27 = 0\] which, on dividing by \(3\), gives the equation of the locus of \(P\) in the form requested, namely \(x^2 + y^2 +10y + 9 = 0\).

A more general problem with detailed suggestions and solutions can be found in [The Circle of Apollonius](https://undergroundmathematics.org/geometry-of-equations/the-circle-of-apollonius-coordinate-edition).
