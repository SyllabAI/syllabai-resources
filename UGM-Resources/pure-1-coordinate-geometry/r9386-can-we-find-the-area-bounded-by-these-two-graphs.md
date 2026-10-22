---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/circles/r9386
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- circles
- type/review-question
resource_identity:
  ugm_id: r9386
  station: circles
  station_title: Circles
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9386
  old_site_id: Q243
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
  spec_points:
  - code: 1.3.2
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'Area between y=sqrt(2-x^2) (upper semicircle) and a line — circle-graph reading plus line form; the area evaluation rides 1.4 radians (recorded medium).'
      rationale: 'Canonical UGM title: “Can we find the area bounded by these two graphs?”; exam provenance: Oxford (MAT) 2013 Q1H'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford (MAT) 2013 Q1H
task: T-UGM-IMPORT-3
---

# Can we find the area bounded by these two graphs?

## Question

The area bounded by the graphs \[y=\sqrt{2-x^2} \qquad \text{and} \qquad x+\left(\sqrt{2}-1\right)y=\sqrt{2}\] equals

1. \(\dfrac{\sin{\sqrt{2}}}{\sqrt{2}}\);

---

1. \(\dfrac{\pi}{4}-\dfrac{1}{\sqrt{2}}\);

---

1. \(\dfrac{\pi}{2\sqrt{2}}\);

---

1. \(\dfrac{\pi^2}{6}\).

## Suggestion

Could we start by sketching the graphs of our two functions?

How do we calculate the area of the required shape? Could we write it as the difference of two other areas?

What would we expect our answer to look like? Do some of the options in the list seem more likely than others?

## Solution

The equation \(y=\sqrt{2-x^2}\) can be squared to get \(y^2=2-x^2\), or \(x^2+y^2=2\). This is a circle centred at the origin with radius \(\sqrt{2}\).

The original equation, though, is \(y=\sqrt{\vphantom{x^2}\cdots}\), which is never negative, so we actually only have the semicircle with \(y\ge0\).

The graph of \(x+\left(\sqrt{2}-1\right)y=\sqrt{2}\) is a straight line which intersects the \(y\)-axis at \(\left(0, 2+\sqrt{2}\right)\), and the \(x\)-axis at \(\left(\sqrt{2},0\right)\), which is on the circumference of the circle.

We can now sketch these two graphs.

To find the other point of intersection, we substitute \(x=\sqrt{2}-\left(\sqrt{2}-1\right)y\) into the equation of the circle, to get \[\begin{gathered} \left(\sqrt{2}-\left(\sqrt{2}-1\right)y\right)^2+y^2=2\\ \implies\quad 2-2\sqrt{2}\left(\sqrt{2}-1\right)y+\left(\sqrt{2}-1\right)^2y^2+y^2=2\\ \implies\quad 2-\left(4-2\sqrt{2}\right)y+\left(3-2\sqrt{2}\right)y^2+y^2=2\\ \implies\quad -\left(4-2\sqrt{2}\right)y+\left(4-2\sqrt{2}\right)y^2=0\\ \implies\quad \left(4-2\sqrt{2}\right)y(-1+y)=0. \end{gathered}\] So \(y=0\) (the intersection we already know about) or \(y=1\).

Alternatively, substituting \(y=\sqrt{2-x^2}\) into the equation of the line gives a shorter solution if we notice that \(2-x^2 = \left(\sqrt{2}-x\right)\left(\sqrt{2}+x\right)\).

So the line intersects this semicircle at \(\left(\sqrt{2},0\right)\) and \((1,1)\).

The sector has an angle of \(45^\circ=\dfrac{\pi}{4}\). The simplest way to calculate the area of this segment is to work out the area of \(\frac{1}{8}\) of the circle, and then subtract the triangle which has base \(\sqrt{2}\) and height \(1\).

So the area is \[\frac{1}{8} \times 2\pi - \frac{1}{2} \times \sqrt{2} \times 1 = \frac{\pi}{4} - \frac{1}{\sqrt{2}}\]

and the answer is (b).

Once we know that the area we seek is the difference between the area of a sector of a circle and the area of a triangle, does one of the answers pick itself?
