---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/circles/r9452
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- circles
- type/review-question
resource_identity:
  ugm_id: r9452
  station: circles
  station_title: Circles
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9452
  old_site_id: Q151
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
      evidence: 'Closest points between (x-5)^2+(y-4)^2=4 and (x-1)^2+(y-1)^2=1 — centre/radius plus the distance-between-centres reading.'
      rationale: 'Canonical UGM title: “Which point on the first circle is closest to the second?”; exam provenance: Oxford (MAT) 2007 Q1D'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford (MAT) 2007 Q1D
task: T-UGM-IMPORT-3
---

# Which point on the first circle is closest to the second?

## Question

The point on the circle \[(x-5)^2+(y-4)^2=4\] which is closest to the circle \[(x-1)^2+(y-1)^2=1\] is

1. \((3.4,2.8)\),

---

1. \((3,4)\),

---

1. \((5,2)\),

---

1. \((3.8,2.4)\).

## Solution

Here is a diagram of the circles:

**Approach 1**

The right-angle triangle with the circle centres at two of its vertices has sides of length \(3\) and \(4\). Its hypotenuse is therefore of length \(5\).

Using similar triangles, we have \(\dfrac{3}{5}=\dfrac{a}{4}=\dfrac{b}{3}\). Thus \(a = 2.4, b = 1.8\), and the point on the first circle closest to the second is \((3.4,2.8)\). The answer is (a).

**Approach 2**

The vector joining \((5,4)\) and \((1,1)\), the centres of the circles, is \(\begin{pmatrix}-4\\-3\end{pmatrix}\). The length of this vector is \(\sqrt{(-4)^2+(-3)^2}=5\).

The first circle has radius \(2\), and so the point on this closest to the second is \(\dfrac{2}{5}\)ths of the way along this vector. Hence we can calculate the point: \[\begin{pmatrix}5\\4\end{pmatrix} + \frac{2}{5}\begin{pmatrix}-4\\-3\end{pmatrix} = \begin{pmatrix}5\\4\end{pmatrix} + \begin{pmatrix}-1.6\\-1.2\end{pmatrix} = \begin{pmatrix}3.4\\2.8\end{pmatrix}.\]

Therefore the answer is (a).
