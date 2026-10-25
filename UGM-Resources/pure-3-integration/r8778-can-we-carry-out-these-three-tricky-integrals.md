---
created: 2026-10-26T02:40:04 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/r8778
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/review-question
resource_identity:
  ugm_id: r8778
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8778
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: chain-rule
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: chain-rule
    validation_status: SUGGESTED
  spec_points:
  - code: 3.5.6
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-13 cross-map (cross-map-p3-integration.json
        (P3c lane 13) @ syllabai-experimental 21845f3)
      evidence: INT x sqrt(2x-1) dx by the substitution u = 2x-1 and INT_0^(pi/4) sec^4 x dx via tan^2
        = sec^2 - 1 (the 3.5.2 relationship reducing it to tan + (tan - x)); the INT 1/sqrt(2x-x^2) card
        requires the arcsin form beyond the 3.5 list and is disclosed of record (flips the lane-11 non-overlap
        row of record routed 'P3 3.5 Integration')
      rationale: 'Canonical UGM title: Can we carry out these three tricky integrals?'
      validation_status: SUGGESTED
    title: use a given substitution to simplify and evaluate e.g. to integrate either a definite or an
      indefinite integral.
  - code: 3.5.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-13 cross-map (cross-map-p3-integration.json
        (P3c lane 13) @ syllabai-experimental 21845f3)
      evidence: INT x sqrt(2x-1) dx by the substitution u = 2x-1 and INT_0^(pi/4) sec^4 x dx via tan^2
        = sec^2 - 1 (the 3.5.2 relationship reducing it to tan + (tan - x)); the INT 1/sqrt(2x-x^2) card
        requires the arcsin form beyond the 3.5 list and is disclosed of record (flips the lane-11 non-overlap
        row of record routed 'P3 3.5 Integration')
      rationale: 'Canonical UGM title: Can we carry out these three tricky integrals?'
      validation_status: SUGGESTED
    title: use trigonometrical relationships in carrying out integration or
  mapped_date: '2026-10-26'
  mapper: cross-map-p3-integration.json (P3c lane 13) @ syllabai-experimental 21845f3
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-13
---

# Can we carry out these three tricky integrals?

## Question

1. Find

1. \(\displaystyle \int x \sqrt{2x-1} \:dx\),

---

1. \(\displaystyle \int \frac{1}{\sqrt{2x - x^2}} \:dx\).

1. Evaluate \(\displaystyle \int_0^{\pi/4} \sec^4 x \:dx\).

## Suggestion

(a)(ii) Find \(\displaystyle \int \frac{1}{\sqrt{2x - x^2}} \:dx\).

Could we try completing the square on the denominator?

What do we get if we differentiate \(\tan x\)?

## Solution

Let

\(u = 2x - 1\)

, so that

\(du = 2 \: dx\)

. Then

\[\begin{align*} \int x \sqrt{2x-1} \:dx = \int \frac{u+1}{2} \sqrt{u} \:\frac{du}{2} &= \frac{1}{4} \int u^{3/2} + u^{1/2} \:du \\ &= \frac{1}{4} \left( \frac{u^{5/2}}{\frac{5}{2}} + \frac{u^{3/2}}{\frac{3}{2}} + C \right) \\ &= \frac{1}{10} u^{5/2} + \frac{1}{6} u^{3/2} + C\\ &= \frac{1}{10} (2x-1)^{5/2} + \frac{1}{6} (2x-1)^{3/2} + C,\\ \end{align*}\]

where \(C\) is a constant of integration.

We can write

\[\begin{equation*} 2x - x^2 = -(x^2 - 2x) = -\left( (x-1)^2 - 1 \right) = 1 - (x-1)^2 \end{equation*}\]

so that

\[\begin{equation*} \int \frac{1}{\sqrt{2x - x^2}} \:dx = \int \frac{1}{\sqrt{1 - (x-1)^2}} \:dx. \end{equation*}\]

Take

\(\sin \theta = x - 1\)

, so that

\(\cos \theta \: d\theta = dx\)

and

\[\begin{align*} \int \frac{1}{\sqrt{1 - (x-1)^2}} \:dx = \int \frac{\cos \theta}{\sqrt{1 - \sin^2 \theta}} \:d\theta &= \int \frac{\cos \theta}{\cos \theta} \:d\theta \\ &= \theta + C \\ &= \sin^{-1} (x-1) + C, \end{align*}\]

where \(C\) is a constant of integration.

We have that

\[\begin{equation*} \tan^2 x + 1 = \sec^2 x. \end{equation*}\]

By the standard result (which can be proved using the

quotient rule

), we have that

\[\begin{equation*} \frac{d}{dx} \tan x = \sec^2 x. \end{equation*}\]

and therefore

\[\begin{equation*} \int \sec^4 x \:dx = \int \sec^2 x \sec^2 x\:dx = \int \sec^2 x\tan^2 x + \sec^2 x \:dx. \end{equation*}\]

The second term we can integrate by the standard result above. For the first term, we substitute \(u=\tan x\) and get \[\int \sec^2 x\tan^2 x\:dx = \int u^2\:du = \frac{\tan^3 x}{3}+C.\] Thus we have \[\int_0^{\pi/4} \sec^4 x \:dx = \left[\frac{\tan^3 x}{3}+\tan x\right]_0^{\pi/4} = \frac{4}{3}.\]
