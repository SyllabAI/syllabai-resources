---
created: 2026-10-23T16:39:11 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/r6049
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-triangles-to-functions
- type/review-question
resource_identity:
  ugm_id: r6049
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6049
  old_site_id: Q1041
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
  exam_reference: UCLES O level Elementary Mathematics Alternative B Paper 2, QP 47, 1954, Q8
task: T-UGM-IMPORT-5
---

# How far are these two ships from the shore?

## Question

Two ships \(P\) and \(Q\) are simultaneously observed from two points \(X\) and \(Y\) on a straight coastline running from west to east. \(P\) is due north of \(X\) and lies on a bearing of \(300^\circ\) from \(Y\). \(Q\) is on a bearing of \(040^\circ\) from \(X\) and on a bearing of \(010^\circ\) from \(Y\). If the distance between \(X\) and \(Y\) is \(4\) miles, calculate the distance of the two ships from the shore.

## Suggestion

A bearing of \(x^\circ\) means that the given direction is obtained by turning through \(x^\circ\) from north in a clockwise direction.

Could we draw a diagram, with all the given angles marked in?

Can we spot any triangles in our diagram that might be useful?

## Solution

Let’s start by drawing a picture.

To find the distance of the ship \(P\) from the shore (labelled \(h\) in the diagram), let’s examine the right-angled triangle \(XPY\).

We can see that angle \(XYP=30^\circ\), and so \[h=4\times \tan 30=\frac{4}{\sqrt{3}}.\]

The distance of \(P\) from the shore is therefore \(\approx \quantity{2.31}{miles}\) (to \(3\)sf).

To find the distance of \(Q\) from the shore, \(d\), we need to work a bit harder. We can see from the diagram that \[d=XQ\times \sin 50,\] so if we can find the length \(XQ\) we are done.

Consider the triangle \(XYQ\). We know all the angles in this triangle and one of the side lengths, so let’s try the [sine rule](https://undergroundmathematics.org/glossary/sine-rule). This gives us that \[\frac{XQ}{\sin 100}=\frac{4}{\sin 30},\] and so \[XQ=\frac{4\sin 100}{\sin 30}=8 \sin 100.\]

Therefore \[d=XQ\sin 50=8\sin100 \sin50.\]

The distance of \(Q\) from the shore is therefore \(\approx \quantity{6.04}{miles}\) (to \(3\)sf).
