---
created: 2026-10-23T14:47:57 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/r7115
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/review-question
resource_identity:
  ugm_id: r7115
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7115
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: chain-rule
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: chain-rule
    validation_status: SUGGESTED
  spec_points: []
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md rule
    3: coverage is never manufactured)'
  mapped_date: '2026-10-23'
  mapper: cross-map-circular-measure.json (P3c lane 4) @ syllabai-experimental b52cf1bf
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1964 Q5(ii)
task: T-UGM-IMPORT-4
---

# When does this cone have a maximum volume?

## Question

A hollow container is to be made out of a fixed total area \(\pi a^2\) of sheet metal and its shape is to be that of a right circular cone completed by the circular base on which it stands. Find the radius of the base when the container encloses maximum volume.

## Suggestion

Drawing a diagram will probably help.

Can we write down or work out a formula for the surface area of a cone?

Can we derive formulae for the height and volume of the cone from this?

## Solution

The surface area \(A\) of a cone with radius \(r\) and height \(h\) is given by \(A=\pi r^2 + \pi s r\), where \(s=\sqrt{h^2 + r^2}\) is the sloped side of the cone.

The \(\pi r^2\) part comes from the base of the cone. The other part when laid flat is a sector with radius \(s\) and arclength \(2\pi r\).

If the angle in the sector is \(\theta\), then \(s\theta = 2\pi r\). The area of the sector is \(\dfrac{1}{2}s^2 \theta\), which on eliminating \(\theta\) is \(\pi s r\), as above.

We know that this area is \(\pi a^2\), hence

\[\begin{align*} \pi a^2 &= \pi r^2 + \pi s r\\ a^2 -r^2 &= \sqrt{h^2r^2 + r^4}\\ \sqrt{\frac{a^4}{r^2} - 2a^2} &= h. \end{align*}\]

Now the volume of a cone is

\(V=\dfrac{\pi}{3} h r^2\)

, which gives

\[\begin{align*} V=\frac{\pi}{3} \sqrt{a^4r^2 - 2a^2r^4}. \end{align*}\]

To find when the volume is a maximum, we differentiate and set the first derivative equal to zero. We’ll use the substitution

\(u=a^4r^2 - 2a^2r^4\)

and the

Chain Rule

.

\[\begin{align*} V &= \frac{\pi}{3}u^{\frac{1}{2}} \\ \frac{dV}{dr} = \frac{dV}{du}\times\frac{du}{dr} &= \frac{\pi}{6}u^{-\frac{1}{2}}\left(2a^4r-8a^2r^3\right) \\ &= \frac{\pi}{3}\frac{a^4r-4a^2r^3}{\sqrt{a^4r^2-2a^2r^4}} \end{align*}\]

This is zero when

\[\begin{align*} a^4r-4a^2r^3 &= 0\\ a^2r\left(a^2-4r^2\right) &= 0\\ r=0 \text{ or } \frac{a}{2}. \end{align*}\]

Note that we can ignore the negative solution, \(r=-\frac{a}{2}\), because of the physical context of the question.

Finding the second derivative of the volume (to show we have a maximum) would be difficult.

Instead we could argue that \(V=0\) for \(r=0\) and \(r=\dfrac{a}{\sqrt{2}}\), and is positive for all values of \(r\) in between. The turning point at \(r=\dfrac{a}{2}\) must therefore be a maximum.
