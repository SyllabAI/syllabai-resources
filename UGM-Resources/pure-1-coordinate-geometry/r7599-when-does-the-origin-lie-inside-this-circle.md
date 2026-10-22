---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/circles/r7599
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- circles
- type/review-question
resource_identity:
  ugm_id: r7599
  station: circles
  station_title: Circles
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7599
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
  spec_points:
  - code: 1.3.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'The origin lies inside x^2+ax+y^2+by=c precisely when a^2+b^2>4c — completing the square to centre/radius and the inside test; MAT form, exactly the circle skil'
      rationale: 'Canonical UGM title: “When does the origin lie inside this circle?”; exam provenance: Oxford (MAT) 2016 Q1C'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford (MAT) 2016 Q1C
task: T-UGM-IMPORT-3
---

# When does the origin lie inside this circle?

## Question

The origin lies within the circle with equation \[x^2+ax+y^2+by=c\] precisely when

1. \(c > 0\)

---

1. \(a^2 + b^2 > c\)

---

1. \(a^2 + b^2 < c\)

---

1. \(a^2 + b^2 > 4c\)

---

1. \(a^2 + b^2 < 4c\).

## Suggestion

Can we write this equation in the form \((x-p)^2+(x-q)^2=r^2\)?

Which inequality denotes the region that is the inside of this circle?

## Solution

We can write the equation of the circle as

\[\left(x+\dfrac{a}{2}\right)^2 -\left(\dfrac{a}{2}\right)^2+\left(x+\dfrac{b}{2}\right)^2 -\left(\dfrac{b}{2}\right)^2 = c,\]

or

\[\left(x+\dfrac{a}{2}\right)^2 +\left(x+\dfrac{b}{2}\right)^2 = c + \left(\dfrac{a}{2}\right)^2 +\left(\dfrac{b}{2}\right)^2.\]

Thus the region inside the circle is denoted by

\[\left(x+\dfrac{a}{2}\right)^2 +\left(x+\dfrac{b}{2}\right)^2 < c + \left(\dfrac{a}{2}\right)^2 +\left(\dfrac{b}{2}\right)^2.\]

Does \((0,0)\) satisfy this inequality? If and only if

\[\left(0+\dfrac{a}{2}\right)^2 +\left(0+\dfrac{b}{2}\right)^2 < c + \left(\dfrac{a}{2}\right)^2 +\left(\dfrac{b}{2}\right)^2,\]

which is true if and only if \(0 < c\), and the answer is (a).
