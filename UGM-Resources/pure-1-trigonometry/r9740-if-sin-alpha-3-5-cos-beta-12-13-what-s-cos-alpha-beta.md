---
created: 2026-10-23T16:39:11 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-compound-angles/r9740
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-compound-angles
- type/review-question
resource_identity:
  ugm_id: r9740
  station: trigonometry-compound-angles
  station_title: 'Trigonometry: Compound Angles'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9740
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: trigonometry-compound-angles
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: trigonometry-compound-angles
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
  exam_reference: UCLES A level Mathematics B 1, QP 9202/1, 1980, Q4(a)
task: T-UGM-IMPORT-5
---

# If $\sin \alpha = 3/5, \cos \beta = 12/13$, what's $\cos(\alpha + \beta)$?

## Question

Given that \(\sin \alpha = \tfrac{3}{5}\) and \(\cos \beta = \tfrac{12}{13}\), prove that one possible value of \(\cos(\alpha + \beta)\) is \(\tfrac{33}{65}\) and find all the other possible values.

## Suggestion

Given that \(\sin \alpha = \dfrac{3}{5}\) and \(\cos \beta = \dfrac{12}{13}\), prove that one possible value of \(\cos(\alpha + \beta)\) is \(\dfrac{33}{65}\)…

Could we draw a diagram with right-angle triangles and the angles \(\alpha\), \(\beta\) and \(\alpha+\beta\)?

If two sides of a right-angle triangle are \(3\) and \(5\), what is the third side?

## Solution

Given that \(\sin \alpha = \dfrac{3}{5}\) and \(\cos \beta = \dfrac{12}{13}\), prove that one possible value of \(\cos(\alpha + \beta)\) is \(\tfrac{33}{65}\) and find all the other possible values.

The diagram tells us that \(\cos(\alpha+\beta) = \cos\alpha\cos\beta-\sin\alpha\sin\beta\) for \(\alpha+\beta < 90^\circ\). This is, in fact, true for all angles \(\alpha\) and \(\beta\).

Now \(\cos^2 \theta + \sin^2 \theta = 1\) for all \(\theta\), which means \(\cos \alpha = \pm\dfrac{4}{5}\), and \(\sin \beta = \pm \dfrac{5}{13}\).

Thus \(\cos(\alpha+\beta) = \cos\alpha\cos\beta-\sin\alpha\sin\beta = \pm \dfrac{48}{65}\pm \dfrac{15}{65},\) where the signs are independent of each other.

We therefore have four solutions, \(\cos(\alpha+\beta) = \pm \dfrac{63}{65}\), or \(\pm \dfrac{33}{65}\).
