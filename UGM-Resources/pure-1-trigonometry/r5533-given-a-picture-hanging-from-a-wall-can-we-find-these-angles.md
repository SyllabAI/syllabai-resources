---
created: 2026-10-23T16:39:11 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/r5533
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-triangles-to-functions
- type/review-question
resource_identity:
  ugm_id: r5533
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5533
  old_site_id: null
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
  exam_reference: O&C O level MEI Additional Mathematics 1, QP MEI 109, 1974, Q12
task: T-UGM-IMPORT-5
---

# Given a picture hanging from a wall, can we find these angles?

## Question

A rectangular picture of width \(\quantity{32}{cm}\) and height \(\quantity{20}{cm}\) has its lower edge \(AB\) horizontal against a vertical wall. It hangs at an angle of \(15^\circ\) to the wall and may be taken to be of negligible thickness. It is supported by two equal strings \(FD\), \(FC\) of length \(\quantity{20}{cm}\) attached to the upper corners \(C\), \(D\) of the picture and to a point \(F\) on the wall vertically above the centre of \(AB\).

Copy the given sketch, including the projections of \(C\), \(D\) and \(E\), the mid-point of \(CD\), onto the wall at \(X\), \(Y\) and \(Z\) respectively.

Identify in terms of the letters the following angles and calculate them:

1. the angle between the two strings,

---

1. the angle between the string \(DF\) and the wall,

---

1. the angle between the wall and the plane containing both strings.

## Suggestion

Are we certain about our definitions of trigonometric functions? And [Pythagoras’ Theorem](https://undergroundmathematics.org/glossary/pythagoras-theorem)?

Can we look for useful triangles in the diagram where we can apply these rules?

## Solution

A rectangular picture of width \(\quantity{32}{cm}\) and height \(\quantity{20}{cm}\) has its lower edge \(AB\) horizontal against a vertical wall. It hangs at an angle of \(15^\circ\) to the wall and may be taken to be of negligible thickness. It is supported by two equal strings \(FD\), \(FC\) of length \(\quantity{20}{cm}\) attached to the upper corners \(C\), \(D\) of the picture and to a point \(F\) on the wall vertically above the centre of \(AB\).

Copy the given sketch, including the projections of \(C\), \(D\) and \(E\), the mid-point of \(CD\), onto the wall at \(X\), \(Y\) and \(Z\) respectively.

Identify in terms of the letters the following angles and calculate them:

1. the angle between the two strings…

We know the length of two of the sides of the right triangle \(DEF\).

The angle between \(DF\) and \(FE\) is half the angle \(\alpha\) that we need, so we can use the definition of sine to give \[\alpha = 2\sin^{-1} \frac{16}{20} \quad \left(=2\arcsin\frac{16}{20}\right) \quad \approx 106.3^\circ.\]

1. the angle between the string \(DF\) and the wall…

The angle between a line and a plane is given by the angle between the line and its perpendicular projection onto that plane, that is, the angle between the line \(DF\) and \(FY\).

So looking at the triangle \(AYD\), we can use the definition of cosine to find the length of \(YD\) as

\[20 \cos 15^\circ \approx \quantity{5.2}{cm}.\]

We can now obtain the angle \(\beta\) from the triangle \(FDY\) with help of the definition of the tangent, giving \[\beta = \tan^{-1} (\cos 15^\circ) \quad (=\arctan(\cos15^\circ)) \quad \approx 14.5^\circ.\]

Let’s call the angle between the plane of the strings and the wall \(\gamma\), which is given by the angle between the lines \(FZ\) and \(FE\).

Looking at the triangle \(EFZ\), we can calculate the length of \(EF\) with help of Pythagoras as \(\sqrt{20^2-16^2} = 12\).

We also know that \(EZ\) has the same length as \(DY\), which we have already calculated. Finally we use the definition of sine again to obtain \[\gamma = \sin^{-1} \frac{20 \cos 15^\circ}{12} \quad \left(=\arcsin\frac{20 \cos 15^\circ}{12}\right) \quad \approx 25.6^\circ.\]
