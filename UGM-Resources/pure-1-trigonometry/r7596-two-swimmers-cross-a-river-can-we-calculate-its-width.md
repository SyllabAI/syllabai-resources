---
created: 2026-10-23T16:39:11 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/r7596
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-triangles-to-functions
- type/review-question
resource_identity:
  ugm_id: r7596
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7596
  old_site_id: Q1072
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: trigonometry-triangles-to-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: trigonometry-triangles-to-functions
    validation_status: SUGGESTED
  spec_points: []
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md rule
    3: coverage is never manufactured)'
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES O level Mathematics Alternative A Arithmetic, QP 411/1, 1960, Q11
task: T-UGM-IMPORT-5
---

# Two swimmers cross a river - can we calculate its width?

## Question

The above figure shows the parallel banks of a straight stretch of river.

Starting from the point \(A\) on a bank, a man swims at an angle of \(40°\) with the bank, reaching a point \(B\) on the opposite bank after swimming \(150\) yd. A second swimmer also leaves the bank at \(A\) but reaches the opposite bank at \(C\). If \(BC = 50\) yd., calculate

1. the width of the river;

---

1. the angle between \(AB\) and \(AC\).

## Solution

Let’s concentrate on the first swimmer.

Now we know in a right-angled triangle \(\sin(\theta) = \dfrac{\text{opposite }}{\text{hypotenuse}}\).

For our triangle we have \(\sin 40 = \dfrac{w}{150}\), where \(w\) is the width of the river, which yields \(w = 150\sin 40 \approx 96.4\) yd.

Now let’s think about the second swimmer.

We need to find the angle \(\alpha\). Now \(AD = 150 \cos 40 + 50\), while \(CD = 150\sin 40\), so \(\tan (40-\alpha) = \dfrac{150\sin 40}{150 \cos 40 + 50}\).

Thus \(\tan (40-\alpha) = 0.584683... \implies 40-\alpha = 30.3141... \implies \alpha \approx 9.69^\circ\).
