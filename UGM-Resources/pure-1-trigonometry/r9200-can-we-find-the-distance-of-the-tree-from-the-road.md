---
created: 2026-10-23T16:39:11 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/r9200
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-triangles-to-functions
- type/review-question
resource_identity:
  ugm_id: r9200
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9200
  old_site_id: Q1040
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
  exam_reference: UCLES O level Additional Mathematics 1, QP 471/1, 1969, Q3(i)
task: T-UGM-IMPORT-5
---

# Can we find the distance of the tree from the road?

## Question

A road runs from \(A\) due East to \(B\), \(500\) yd. distant. The bearings of a tree from \(A\) and \(B\) are \(048^\circ\) and \(296^\circ\) respectively. Find the distance, correct to the nearest yard, of the tree from the road.

## Solution

In our diagram, \(h\) represents the perpendicular distance of the tree from the road and \(x\) is the distance from the foot of the perpendicular to \(A\).

From the left hand triangle, we find that

\[\begin{equation}\label{eq:1} \tan 42^\circ=\frac{h}{x}, \end{equation}\]

and from the right hand triangle,

\[\begin{equation}\label{eq:2} \tan 26^\circ=\frac{h}{500-x}. \end{equation}\]

Rearranging equation \(\eqref{eq:1}\), we find that \(x=\dfrac{h}{\tan 42^\circ}\). Substituting this into \(\eqref{eq:2}\), we find that \[\tan 26^\circ=\frac{h}{500-\dfrac{h}{\tan 42^\circ}}.\] Rearranging, we find that \[h\left(1+\frac{\tan 26^\circ}{\tan 42^\circ}\right)=500\tan 26^\circ,\] and so \[h=\frac{500\tan 26^\circ}{1+\dfrac{\tan26^\circ}{\tan42^\circ}}.\]

This gives us that \(h=158\) yd. to the nearest yard.
