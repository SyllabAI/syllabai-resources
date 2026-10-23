---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/r5345
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/review-question
resource_identity:
  ugm_id: r5345
  station: sequences
  station_title: Sequences
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5345
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: sequences
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: sequences
    validation_status: SUGGESTED
  spec_points:
  - code: 1.6.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: a_4, a_8, a_16 of an AP are consecutive GP terms; show a_3, a_6, a_12 too — nth-term
        formulae of AP and GP interplay
      rationale: 'Canonical UGM title: "If AP terms $a_4,a_8, a_{16}$ are in GP, are $a_3, a_6, a_{12}$
        in GP too?"; exam provenance: UCLES O level Additional Mathematics 1, 1963, Q5(ii)'
      validation_status: SUGGESTED
    title: use the formulae for the n th term and for the Including knowledge that numbers sum of the
      first n terms to solve problems involving arithmetic or geometric progressions equivalent).
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES O level Additional Mathematics 1, 1963, Q5(ii)
task: T-UGM-IMPORT-6
---

# If AP terms $a_4,a_8, a_{16}$ are in GP, are $a_3, a_6, a_{12}$ in GP too?

## Question

The fourth, eighth and sixteenth terms of an arithmetic progression are consecutive terms of a geometric progression. Show that the third, sixth and twelfth terms of the arithmetic progression are also consecutive terms of a geometric progression.

## Solution

Let the first term of the arithmetic progression be \(a=a_1\) and the common difference be \(d\). Then the fourth, eighth and sixteenth terms are \[a_4=a+3d,\, a_8=a+7d,\, a_{16}=a+15d.\] Since they are consecutive terms of an arithmetic progression, we must have that \[\frac{a_8}{a_4}=r=\frac{a_{16}}{a_8},\] where \(r\) is the common ratio of the geometric progression. Therefore \[\frac{a+7d}{a+3d}=\frac{a+15d}{a+7d},\] and therefore \[(a+7d)^2=(a+15d)(a+3d).\] Multiplying out the brackets, we find that \[a^2+14da+49d^2=a^2+18da+45d^2,\] and rearranging we find that \[4d^2-4da=0.\] Therefore \[4d(d-a)=0.\] If \(d=0\) then \(a_n=a\) for all \(n\). Therefore \(a_3=a_6=a_{12}\), which is part of a geometric progression with common ratio \(1\).

If \(d=a\), then \[a_3=a+2d=3d,\, a_6=a+5d=6d,\, a_{12}=a+11d=12d,\] which is part of a geometric progression with common ratio \(2\).
