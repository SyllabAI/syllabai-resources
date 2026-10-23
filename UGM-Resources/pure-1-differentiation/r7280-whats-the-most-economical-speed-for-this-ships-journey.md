---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/r7280
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/review-question
resource_identity:
  ugm_id: r7280
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7280
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-of-powers
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-of-powers
    validation_status: SUGGESTED
  spec_points:
  - code: 1.7.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: 'most economical ship speed: 2400(150/v + 8v/3) minimised — v^-1 + v derivative with
        a nature check'
      rationale: 'Canonical UGM title: "What''s the most economical speed for this ship''s journey?";
        exam provenance: O&C O level MEI Additional Mathematics 1, 1974, Q8'
      validation_status: SUGGESTED
    title: use the derivative of x (for any rational n ), together with constant multiples, sums and
      differences of functions, and of composite functions using the chain rule
  - code: 1.7.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: 'most economical ship speed: 2400(150/v + 8v/3) minimised — v^-1 + v derivative with
        a nature check'
      rationale: 'Canonical UGM title: "What''s the most economical speed for this ship''s journey?";
        exam provenance: O&C O level MEI Additional Mathematics 1, 1974, Q8'
      validation_status: SUGGESTED
    title: locate stationary points and determine their nature, and use information about stationary
      points in sketching graphs.
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: O&C O level MEI Additional Mathematics 1, 1974, Q8
task: T-UGM-IMPORT-7
---

# What's the most economical speed for this ship's journey?

## Question

The cost of running a cargo ship is \(£150\) a day for wages and other crew expenses and \(£\dfrac{8v^2}{3}\) a day for fuel and maintenance, where \(v\) is the steady speed in \(\quantity{}{km/h}\). Find in terms of \(v\) how many days a voyage of \(\quantity{2400}{km}\) takes and hence obtain a formula for the total cost of the whole voyage.

Deduce by calculus methods the most economical speed and the least total cost of the whole voyage.

## Solution

If \(v\) is the steady speed of the ship, it takes time \(t=\dfrac{s}{v}\) to travel a distance \(s\).

In our case, we have \(s=\quantity{2400}{km}\), and hence the voyage takes \(\dfrac{2400}{v}\) hours, or \(\dfrac{100}{v}\) days.

The cost per day is

\(150+\dfrac{8v^2}{3}\)

so the total cost of the voyage is

\[\begin{equation*} \left(150+\dfrac{8v^2}{3}\right)\frac{100}{v} = \frac{15\,000}{v} + \frac{800v}{3}. \end{equation*}\]

The most economical speed reduces the total cost of the voyage to a minimum. First we find the derivative of the cost function:

\[\frac{d}{dv} \left( \frac{15\,000}{v} + \frac{800v}{3} \right) = -\frac{15\,000}{v^2}+ \frac{800}{3}.\]

Setting this equal to zero and solving for \(v\),

\[\begin{align*} -\frac{15\,000}{v^2}+ \frac{800}{3} &= 0\\ -15\,000 + \frac{800v^2}{3} &= 0\\ v^2 &= \frac{450}{8}\\ v &= \pm \sqrt{\frac{450}{8}} = \pm \frac{15}{2}. \end{align*}\]

The speed \(v\) has to be positive, so \(v = \quantity{\dfrac{15}{2}}{km/h}\) is the most economical speed.

At this speed the cost of the voyage is \(\dfrac{15\,000}{15/2} + \dfrac{800\times15/2}{3} = £4\,000\).

To check this is the minimum rather than the maximum cost, we can compare the cost at a different speed such as

\(v=\quantity{5}{km/h}\)

.

\[\begin{align*} \text{Cost} &= \frac{15\,000}{5} + \frac{800\times5}{3}\\ &= 3\,000+\frac{4\,000}{3}\\ &> 4\,000 \end{align*}\]

So the \(£4\,000\) is indeed the minimum cost.

Alternatively, we could evaluate the second derivative at \(v=\dfrac{15}{2}\).
