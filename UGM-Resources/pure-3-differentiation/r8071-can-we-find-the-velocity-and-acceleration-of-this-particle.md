---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-trig-log/r8071
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-trig-log
- type/review-question
resource_identity:
  ugm_id: r8071
  station: calculus-trig-log
  station_title: Calculus of Trigonometry & Logarithms
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8071
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
  - code: 3.4.1
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-12 cross-map (cross-map-p3-differentiation.json
        (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4)
      evidence: v = ds/dt and a = dv/dt for s = 12 sin(3t/2) - the 3.4.1 composite derivative of sin(3t/2)
        by the chain rule is the load-bearing computation (mechanics clothing); the remaining parts are
        1.5 trig equations
      rationale: 'Canonical UGM title: Can we find the velocity and acceleration of this particle?'
      validation_status: SUGGESTED
    title: use the derivatives of e , ln x , sin x , cos x , tan x , tan x , together with constant multiples,
      sums, differences and composites
  mapped_date: '2026-10-25'
  mapper: cross-map-p3-differentiation.json (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-12
---

# Can we find the velocity and acceleration of this particle?

## Question

A particle \(P\) moves in a straight line so that, after \(t\) seconds, its distance, \(s\) metres, from a fixed point \(O\) is given by the equation. \[s=12\sin\left(\frac{3}{2}t\right)\] Determine

1. expressions for the velocity and acceleration of \(P\) in terms of \(t\),

---

1. the time at which \(P\) first returns to \(O\),

---

1. the maximum distance of \(P\) from \(O\) during the motion,

---

1. the velocity of \(P\) when \(s=6\).

## Solution

The velocity of the particle is the rate of change of its displacement from

\(O\)

. So we can differentiate the given function with respect to time.

\[\begin{align*} v&=\frac{ds}{dt}=\frac{3}{2}\times12\cos\left(\frac{3}{2}t\right) \\ &=18\cos\left(\frac{3}{2}t\right) \end{align*}\]

We can differentiate this function now to give us an expression for the acceleration.

\[\begin{align*} a&=\frac{dv}{dt}=-\frac{3}{2}\times18\sin\left(\frac{3}{2}t\right) \\ &=-27\sin\left(\frac{3}{2}t\right) \end{align*}\]

The graph of \(s\) is a sine wave that has been stretched horizontally by a factor of \(\frac{2}{3}\). A graph of \(\sin t\) would meet the axis at \(t=\pi\) so this graph will meet the axis at \[t=\pi\times\frac{2}{3}\] The particle first returns to \(0\) at \(t=\frac{2}{3}\pi\approx\quantity{2.1}{s}\).

The graph has been stretched vertically so that it has an amplitude of \(12\). The maximum distance from \(O\) is equal to \(\quantity{12}{m}\).

We can substitute this value into the given equation giving us

\[\begin{align*} 6&=12\sin\left(\frac{3}{2}t\right) \\ \implies\quad \sin\left(\frac{3}{2}t\right)&=\frac{1}{2} \end{align*}\]

Using this standard triangle we can see that if \(\sin\left(\frac{3}{2}t\right)=\frac{1}{2}\) then \(\cos\left(\frac{3}{2}t\right)=\frac{\sqrt{3}}{2}\). Therefore using the expression from part (1) we can calculate the velocity as \[v=18\cos\left(\frac{3}{2}t\right)=18\frac{\sqrt{3}}{2}=9\sqrt{3}\approx\quantity{15.6}{m\,s^{-1}}.\]
