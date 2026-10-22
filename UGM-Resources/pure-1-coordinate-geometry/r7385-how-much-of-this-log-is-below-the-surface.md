---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/circles/r7385
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- circles
- type/review-question
resource_identity:
  ugm_id: r7385
  station: circles
  station_title: Circles
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7385
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
  exam_reference: UCLES 1986 Q15
task: T-UGM-IMPORT-3
---

# How much of this log is below the surface?

## Question

The figure shows the circular cross-section of a uniform log of radius \(\quantity{40}{cm}\) floating in water. The points \(A\) and \(B\) are on the surface and the highest point \(X\) is \(\quantity{8}{cm}\) above the surface.

Show that \(\widehat{AOB}\) is approximately \(1.29\) radians.

Calculate

1. the length of the arc \(AXB\),

---

1. the area of the cross-section below the surface,

---

1. the percentage of the volume of the log below the surface.

## Solution

Let \(M\) be the point on \(AB\) vertically below \(X\). The length \(OX\) is \(40\) and \(MX\) is \(8\), so \(OM\) is \(\quantity{32}{cm}\).

We’ll compute the angle \(\alpha\), shown here, using its cosine.

We find \[\alpha = \cos^{-1}\left(\frac{32}{40}\right) \approx 0.6435... \text{ radians.}\]

Since the angle \(\widehat{AOB}\) is \(2 \alpha\), we have \(\widehat{AOB} \approx 1.2870... = 1.29\) radians (3sf).

The length of the arc is \(s = r\theta\). In our case, \(s \approx 40 \times 1.287 = \quantity{51.5}{cm}\) (3sf).

Let’s call the area of the cross-section below the surface \(S\). We can calculate it as the sum of the triangle \(OAB\) and the major sector \(OAB\).

The area of the triangle is \(\frac{1}{2}a b \sin C = \frac{1}{2} 40^2\sin1.287 \approx 768.0\).

The area of the sector is \(\frac{1}{2}r^2\theta = \frac{1}{2} 40^2(2\pi-1.287) \approx 3997.0\).

So we have \(S\approx768.0+3997.0 = 4765.0 = \quantity{4770}{cm^2}\) (3sf). To calculate $S$, we need to compute the area of the circle segment shown in red below. <cm-image url="images/shadedarea.png" alt-text="shaded circle segment" /> This is approximately the area of the sector $OAXB$ minus the area of triangle $OAB$, which is $$\frac{40^2}{2}(1.287 - \sin(1.287)) \approx 261.6.$$ Given that the whole circle has an area of $40^2\pi \approx \quantity{5026.6}{cm^2}$, $S \approx 5026.6-261.6 = 4765.0=\quantity{4770}{cm^2}$ (3sf).

The percentage of the volume of the log below the surface is the same as the percentage of the area of the cross-section below the surface.

This is \(\dfrac{4765.0}{\pi 40^2}\times100 \approx 94.80 = 94.8\%\) (3sf).
