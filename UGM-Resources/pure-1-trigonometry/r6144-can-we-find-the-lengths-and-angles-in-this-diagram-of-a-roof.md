---
created: 2026-10-23T16:39:11 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/r6144
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-triangles-to-functions
- type/review-question
resource_identity:
  ugm_id: r6144
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6144
  old_site_id: Q4053
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
  exam_reference: UCLES A level Mathematics 1, QP 182, 1952, Q5
task: T-UGM-IMPORT-5
---

# Can we find the lengths and angles in this diagram of a roof?

## Question

In the diagram, which represents the roof of a house, \(ABCD\) is a horizontal rectangle and \(XY\) a line parallel to \(AB\) and \(DC\). \(AB=40'\), \(BC=XY=16'\) and \(AX=BY=CY=DX=17'\). Calculate \((i)\) the height of \(XY\) above the plane \(ABCD\), \((ii)\) the angle of inclination to the horizontal of the face \(AXYB\), and \((iii)\) the angle of inclination to the horizontal of the edge \(AX\).

## Suggestion

In the diagram, which represents the roof of a house, \(ABCD\) is a horizontal rectangle and \(XY\) a line parallel to \(AB\) and \(DC\). \(AB=40'\), \(BC=XY=16'\) and \(AX=BY=CY=DX=17'\). Calculate \((i)\) the height of \(XY\) above the plane \(ABCD\), …

Could we start by drawing a line perpendicular to \(ABCD\) through either \(X\) (or \(Y\))?

How could we calculate its length? Maybe we could construct a triangle containing this side?

… \((ii)\) the angle of inclination to the horizontal of the face \(AXYB\), and \((iii)\) the angle of inclination to the horizontal of the edge \(AX\).

Can we find more right-angled triangles which include one of these angles?

## Solution

We’ll drop the units in all calculations and keep in mind that all lengths are in feet.

In the diagram, which represents the roof of a house, \(ABCD\) is a horizontal rectangle and \(XY\) a line parallel to \(AB\) and \(DC\). \(AB=40'\), \(BC=XY=16'\) and \(AX=BY=CY=DX=17'\). Calculate \((i)\) the height of \(XY\) above the plane \(ABCD\), …

The height we want is \(FY\).

By using

Pythagoras’ theorem

on

\(BGY\)

, we have

\[GY= \sqrt{17^2-8^2}=15.\]

\(8, 15\) and \(17\) is a [Pythagorean triple](https://undergroundmathematics.org/glossary/pythagorean-triple). These often come up in questions about triangles and it can be really helpful to notice them.

Another example is \(3, 4\) and \(5\). Do you know any more?

In right-angled triangle \(GFY\) we have \(GF=12\) and the hypotenuse \(GY=15\) so \(GFY\) is similar to a triangle with sides \(3,4,5\) and thus \(FY=9.\)

If we don’t spot this we could use Pythagoras for a second time.

… \((ii)\) the angle of inclination to the horizontal of the face \(AXYB\), …

The desired angle is \(\angle XHE\). Looking at other lengths in the diagram, we can see that \(\tan(\angle XHE) = \dfrac{9}{8}\), and so \(\angle XHE = 48.3^\circ\).

… and \((iii)\) the angle of inclination to the horizontal of the edge \(AX\).

The desired angle is \(\angle XAE\). We can see that \(\sin(\angle XAE) = \dfrac{9}{17}\), and so \(\angle XAE = 32.0^\circ\).
