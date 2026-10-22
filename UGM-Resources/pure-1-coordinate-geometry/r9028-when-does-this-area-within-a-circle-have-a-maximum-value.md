---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/circles/r9028
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- circles
- type/review-question
resource_identity:
  ugm_id: r9028
  station: circles
  station_title: Circles
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9028
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
  spec_points: []
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md rule 3: coverage is never manufactured)'
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford (MAT) 2012 Q1J
task: T-UGM-IMPORT-3
---

# When does this area within a circle have a maximum value?

## Question

If two chords \(PQ\) and \(PR\) on a circle of radius \(1\) meet in an angle \(\theta\) at \(P\), for example as drawn in the diagram below,

then the largest possible area of the shaded region \(RPQ\) is

1. \(\theta(1 + \cos\dfrac{\theta}{2})\); \(\quad\)\(\quad\)(b) \(\theta + \sin\theta\); \(\quad\)\(\quad\)(c) \(\dfrac{\pi}{2}(1-\cos\theta)\);\(\quad\)\(\quad\) (d) \(\theta\).

## Suggestion

Can we say anything about how the chords must be aligned to make the shaded area a maximum for a given \(\theta\)?

Can we draw the diagram for this maximal situation and, marking in the angles we know, calculate the required area?

## Solution

The shaded area will be a maximum when the diagram is symmetrical.

We can see this as follows; imagine rotating \(PR\) through a small angle \(\alpha\) anticlockwise in the diagram above.

To keep \(\theta\) the same size we need to rotate \(PQ\) through \(\alpha\) also, and since \(PQ\) is longer than \(PR\), this will cut off a greater area than rotating \(PR\) did.

Thus the symmetrical arrangement maximises the shaded area.

So we need to find the shaded area for the situation above.

Remember that the area of a sector enclosing an angle \(\theta\) (in radians) and with radius \(r\) is \(\dfrac{1}{2}r^2 \theta\).

The area of the sector we need is \(\dfrac{1}{2}\times 1^2 \times 2\theta = \theta.\)

Remember that the area of a triangle with sides \(a\) and \(b\) enclosing an angle \(C\) is \(\dfrac{1}{2}ab\sin C\).

The sum of the areas of the two triangles \(POR\) and \(POQ\) is \(2\left[\dfrac{1}{2}\times 1^2 \times \sin (\pi - \theta)\right] = \sin (\pi - \theta)] = \sin \theta.\)

Thus the total shaded area is \(\sin \theta + \theta\), and the answer is (b).
