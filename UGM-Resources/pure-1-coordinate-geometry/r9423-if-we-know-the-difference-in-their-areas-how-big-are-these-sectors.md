---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/circles/r9423
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- circles
- type/review-question
resource_identity:
  ugm_id: r9423
  station: circles
  station_title: Circles
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9423
  old_site_id: Q4061
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
  exam_reference: UCLES 1979 Q4
task: T-UGM-IMPORT-3
---

# If we know the difference in their areas, how big are these sectors?

## Question

The figure shows two sectors in which \(AB\), \(CD\) are arcs of concentric circles, centre \(O\) and radii \(\quantity{2k}{cm}\) and \(\quantity{3k}{cm}\) respectively. \(A\hat{O}B\) is \(\frac{3}{4}\) radian and the area \(ABDC\) is \(\quantity{30}{cm^2}\). Find

1. the value of \(k\),

---

1. the difference between the lengths of the arcs \(AB\) and \(CD\).

## Suggestion

What are the areas of the two sectors in terms of \(k\)? Is there a formula we could use?

Is there a similar formula to help with finding arc lengths?

## Solution

The figure shows two sectors in which \(AB\), \(CD\) are arcs of concentric circles, centre \(O\) and radii \(\quantity{2k}{cm}\) and \(\quantity{3k}{cm}\) respectively. The angle \(A\hat{O}B\) is \(\dfrac{3}{4}\) radian and the area \(ABDC\) is \(\quantity{30}{cm^2}\). Find

1. the value of \(k\),

The area of a sector with radius \(r\) containing an angle \(\theta\) is \(A=\dfrac{1}{2}r^2\theta\). Hence the difference in the sector areas \(30 = \dfrac{1}{2}(3k)^2\dfrac{3}{4} - \dfrac{1}{2}(2k)^2\dfrac{3}{4}\).

Solving this for \(k\) gives \(k=4\).

Find

1. the difference between the lengths of the arcs \(AB\) and \(CD\).

The length of an arc of radius \(r\) and given by an angle \(\theta\) is \(r\theta\). Hence the difference between arc \(AB\) and arc \(CD\) is \(12\times\dfrac{3}{4} - 8\times\dfrac{3}{4} = \quantity{3}{cm}\).
