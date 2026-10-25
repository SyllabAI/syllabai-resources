---
created: 2026-10-26T02:40:04 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-trig-log/r7074
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-trig-log
- type/review-question
resource_identity:
  ugm_id: r7074
  station: calculus-trig-log
  station_title: Calculus of Trigonometry & Logarithms
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7074
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-trig-log
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-trig-log
    validation_status: SUGGESTED
  spec_points:
  - code: 3.5.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-13 cross-map (cross-map-p3-integration.json
        (P3c lane 13) @ syllabai-experimental 21845f3)
      evidence: 'shaded area between y = sin 2x and y = sin x: R = pi/4 - INT sin 2x - INT sin x with
        the standard antiderivatives [-cos x] evaluated (the horizontal-stretch reading of INT sin 2x
        as (1/2)INT sin x of record) - the 3.5.1 composite-standard evaluation is load-bearing; the intersection
        solving is the recorded 3.3.2 skill (flips the lane-11 non-overlap row of record routed ''P3 3.5
        Integration'')'
      rationale: 'Canonical UGM title: Where do the curves $y=\sin 2x$ and $y=\sin x$ cross?'
      validation_status: SUGGESTED
    title: extend the idea of ‘reverse differentiation’ to Including examples such as ax + b 1 include
      the integration of e , , ax + b sin( ax + b ) , cos( ax + b ) , sec ( ax + b ) and 2 2 x + a
  mapped_date: '2026-10-26'
  mapper: cross-map-p3-integration.json (P3c lane 13) @ syllabai-experimental 21845f3
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-13
---

# Where do the curves $y=\sin 2x$ and $y=\sin x$ cross?

## Question

The diagram shows part of the graphs of the curves \(y=\sin 2x\) and \(y=\sin x\).

\(A\) is a maximum point of the curve \(y=\sin 2x\). \(B\) is a maximum point of the curve \(y=\sin x\).

\(C\) is the point of intersection of the curves shown. Find

1. the \(x\) co-ordinate of \(C\),

---

1. the shaded area.

## Solution

To find the \(x\)-coordinate of \(C\), we need to solve the equation \(\sin x = \sin 2x\) in the region \(0 \le x \le \frac{1}{2}\pi\).

Now \(\sin x = \sin 2x \iff \sin x = 2 \sin x \cos x\). We can see that \(\sin x\) is not zero at \(C\), so the solution we seek is \(\cos x = \dfrac{1}{2}\), and so \(x = \dfrac{\pi}{3}\).

Let’s call the shaded area \(R\). To find \(R\), we start with the area of the rectangle spanned by the line \(AB\) and the \(x\)-axis, which is clearly \(\dfrac{\pi}{4}\).

We then subtract the area below the curves \(y=\sin x\) and \(y=\sin 2x\) as shown by the red area and blue area respectively in the diagram. Thus

\[R=\frac{\pi}{4}-\int_{\pi/4}^{\pi/3} \sin 2x\:dx -\int_{\pi/3}^{\pi/2} \sin x\:dx.\]

Now \[\int_{\pi/3}^{\pi/2} \sin x\:dx = \bigl[-\cos x\bigr]_{\pi/3}^{\pi/2} = \dfrac{1}{2}.\]

And thinking about stretching horizontally \[\int_{\pi/4}^{\pi/3}\sin 2x\:dx = \frac{1}{2}\int_{\pi/2}^{2\pi/3}\sin x\:dx = \frac{1}{2}\bigl[-\cos x\bigr]_{\pi/2}^{2\pi/3} = \dfrac{1}{4}.\]

Thus \[R = \dfrac{\pi}{4}-\dfrac{3}{4}.\]
