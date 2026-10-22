---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/circles/r7816
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- circles
- type/review-question
resource_identity:
  ugm_id: r7816
  station: circles
  station_title: Circles
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7816
  old_site_id: Q4028
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
  exam_reference: UCLES 1976 Q8
task: T-UGM-IMPORT-3
---

# Can we find the ratio of the areas of these two sectors?

## Question

The figure shows two circles, centres \(O\) and \(C\), radii \(r_1\) and \(r_2\), which touch externally at \(P\). Given that \(A\hat{O}P=\dfrac{\pi}{4}\) radians, \(B\hat{C}P = \dfrac{\pi}{3}\) radians and \(AB\) is parallel to \(OPC\), show that \(\dfrac{r_1}{r_2} = \dfrac{\sqrt{6}}{2}\). Hence find the ratio of the areas of the sectors \(OAP\), \(CBP\).

## Suggestion

Could we create some right-angled triangles within the figure, and use trigonometric functions here?

What’s the formula for the area of a sector?

## Solution

Dropping perpendiculars from \(A\) and \(B\) gives us the above diagram. Thus we have

\[r_1 \sin \dfrac{\pi}{4} = AD= BE = r_2 \sin \frac{\pi}{3}.\]

And so we have \[\dfrac{r_1}{r_2} = \dfrac{\sin \dfrac{\pi}{3}}{\sin \dfrac{\pi}{4}} = \dfrac{\left(\dfrac{\sqrt{3}}{2}\right)}{\left(\dfrac{1}{\sqrt{2}}\right)} = \dfrac{\sqrt{6}}{2}.\]

The area of a sector containing an angle

\(\theta\)

and with radius

\(r\)

is

\(\dfrac{1}{2}r^2 \theta\)

. So

\[\begin{align*} A_1 &=\dfrac{1}{2}r_1^2 \times \dfrac{\pi}{4}=\dfrac{\pi r_1^2}{8},\\ A_2 &=\dfrac{1}{2}r_2^2 \times \dfrac{\pi}{3}=\dfrac{\pi r_2^2}{6}.\\ \end{align*}\]

Hence \[\frac{A_1}{A_2} = \dfrac{6}{8} \left( \dfrac{r_1}{r_2} \right)^2 = \dfrac{9}{8}.\]
