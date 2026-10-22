---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/circles/r7937
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- circles
- type/review-question
resource_identity:
  ugm_id: r7937
  station: circles
  station_title: Circles
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7937
  old_site_id: Q3028
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
  exam_reference: UCLES 1970 Q2
task: T-UGM-IMPORT-3
---

# What area do these intersecting circles share?

## Question

Two equal circles, each of radius \(\quantity{10}{cm}\), have centres at \(A\) and \(B\) respectively and the length of \(AB\) is \(\quantity{17.4}{cm}\). The circles intersect at \(C\) and \(D\). Find

1. the angle \(CBA\) and express it in radians correct to three significant figures,

---

1. the area of the minor sector \(BCD\),

---

1. the area common to both circles.

## Solution

The line segment \(CD\) is the perpendicular bisector of \(AB\), and so we have the following right-angled triangle.

Thus, \[\cos \theta = \frac{\text{adjacent}}{\text{hypotenuse}} = \frac{\quantity{8.7}{cm}}{\quantity{10}{cm}} = 0.87\] and so \[\theta = \arccos(0.87) = \text{$0.51559\!\ldots$ radians}\] which, to three significant figures, is \(0.516\) radians.

By symmetry, \(\theta = \angle CBA = \angle DBA\), and so \[\angle DBC = \angle DBA + \angle CBA = 2\theta = 2 \arccos(0.87).\]

The area of a sector of radius \(r\) and enclosed angle \(\theta\) (in radians) is \(\dfrac{1}{2}r^2\theta\), so the area of the sector \(CDB\) is \(\dfrac{1}{2}10^2(2 \arccos(0.87)) = 51.559...,\)

which to \(3\)sf is \(\quantity{51.6}{cm^2}.\)

By symmetry, the area common to both circles is twice the area of this shaded region, and the area of this shaded region is equal to \[\text{area of the minor sector $BCD$} - \text{area of $\triangle BCD$}.\]

The area of a triangle is \(\dfrac{1}{2}ab \sin C\), so the triangle \(BCD\) has area \(\dfrac{1}{2}100 \sin (2\arccos(0.87))=42.895...\)

Thus the area of the shaded region is \(51.559... - 42.895... = 8.664...,\) and so the area shared between the circles is (\(3\)sf) \(\quantity{17.3}{cm^2}.\)
