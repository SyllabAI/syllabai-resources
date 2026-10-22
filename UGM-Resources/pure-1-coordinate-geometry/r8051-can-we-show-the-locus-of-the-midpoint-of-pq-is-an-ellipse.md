---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/circles/r8051
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- circles
- type/review-question
resource_identity:
  ugm_id: r8051
  station: circles
  station_title: Circles
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8051
  old_site_id: None
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
  exam_reference: UCLES 1972 Q8
task: T-UGM-IMPORT-3
---

# Can we show the locus of the midpoint of $PQ$ is an ellipse?

## Question

The points \(P\) and \(Q\) on the ellipse

\[\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1\]

have coordinates \((a\cos\theta, b\sin \theta)\) and \((-a\sin\theta, b\cos\theta)\) respectively. Show that, if \(O\) is the origin,

1. \(OP^2+OQ^2 = a^2 + b^2\),

---

1. the area of triangle \(OPQ\) is \(\dfrac{1}{2}ab\),

---

1. the midpoint of \(PQ\) always lies on the curve whose equation is

\[\dfrac{2x^2}{a^2}+\dfrac{2y^2}{b^2}=1.\]

## Suggestion

Could we start by sketching the graph and marking the points \(P\) and \(Q\)?

When finding the area of the triangle \(OPQ\), are there any other areas we could find more easily that could help us?

## Solution

Let \(c = \cos \theta\) and \(s = \sin \theta\), and so \(c^2 + s^2 = 1.\)

Thus \(OP^2+OQ^2 = (ac-0)^2 + (bs-0)^2 + (-as-0)^2 + (bc-0)^2 =a^2(c^2+s^2) + b^2(s^2+c^2) = a^2 + b^2\).

The area of triangle \(OPQ\) is the area of the rectangle in the diagram with three right-angled triangles subtracted.

So the area of triangle \(OPQ\) is

\[(ac+as)(bs)-(0.5ac\times bs)-(0.5as\times bc) -0.5(ac+as)(bs-bc)\]

\[= abcs+abs^2-0.5abcs-0.5abcs -0.5abcs+0.5abcs -0.5abs^2 +0.5abc^2\]

\[= \dfrac{ab}{2}.\]

We have here chosen the case when \(b\sin \theta > b\cos\theta\), but this method will deal with all possible cases.

The midpoint of \(PQ\) is the point \((\dfrac{ac-as}{2}, \dfrac{bc+bs}{2}) =(x,y).\)

Thus \(\dfrac{2x}{a}= c-s, \dfrac{2y}{b} = c+s.\) Squaring each equation and then adding them gives

\[\dfrac{4x^2}{a^2}+\dfrac{4y^2}{b^2} =2,\]

and so the midpoint of \(PQ\) has the locus

\[\dfrac{2x^2}{a^2}+\dfrac{2y^2}{b^2}=1.\]

We can see the locus traced out by \(A\) in the GeoGebra applet below.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/V4NGQ3KP)
