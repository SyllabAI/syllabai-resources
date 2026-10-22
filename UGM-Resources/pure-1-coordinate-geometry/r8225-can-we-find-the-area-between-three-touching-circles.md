---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/circles/r8225
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- circles
- type/review-question
resource_identity:
  ugm_id: r8225
  station: circles
  station_title: Circles
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8225
  old_site_id: Q4005
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
  exam_reference: UCLES 1954 Q7
task: T-UGM-IMPORT-3
---

# Can we find the area between three touching circles?

## Question

Two circles of radius \(\quantity{3}{in.}\) touch each other, and a third circle of radius \(\quantity{2}{in.}\) touches each of them externally. Find the area contained between the three circles.

## Suggestion

If we draw a picture, can we spot a triangle that might help us find the required area?

## Solution

The part of the diagram shaded in red is the area we need to find. We’ll find the area of the triangle, and subtract the areas of the sectors of the three circles.

We need to find the height of the triangle and the angle \(\alpha\). We can see that (working in radians) \(\beta= \pi - 2 \alpha\).

Using Pythagoras’ theorem, we see that \[h=\sqrt{5^2-3^2}=\sqrt{25-9}=\sqrt{16}=4.\] So the area of the triangle is \[\frac{1}{2}\times 6\times 4=\quantity{12}{in.^2}\] By trigonometry, it is clear that \[\cos\alpha=\frac{3}{5}, \quad \sin\alpha=\frac{4}{5}.\]

Let’s compute the areas of the sectors. The area of a sector (working in radians) of radius \(r\) and enclosing an angle \(\theta\) is \(\dfrac{1}{2}r^2\theta\).

Thus the sectors with radius three each have area

\[\frac{1}{2}\times 3^2 \times \alpha =\frac{9}{2}\arccos(0.6),\]

and the sector with radius

\(2\)

has area

\[\frac{1}{2}\times 2^2 \times (\pi-2\arccos(0.6)) = 2\pi - 4\arccos(0.6).\]

Thus the red area is

\[\begin{align*} \text{area of triangle}-2\times \text{area of big sector}- \text{area of small sector} \\ =\quantity{12-5\arccos(0.6)-2\pi}{in.^2} \approx \quantity{1.08}{in.^2} \end{align*}\]
