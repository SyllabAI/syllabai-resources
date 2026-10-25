---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/r5990
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/review-question
resource_identity:
  ugm_id: r5990
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5990
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
  - code: 3.4.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-12 cross-map (cross-map-p3-differentiation.json
        (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4)
      evidence: chain rule on sin^4 x, cos^2 x, cos^4 x gives d/dx = 0 identically - the expression is
        the constant 1; the deduction task on the 3.4.1 composite derivatives
      rationale: 'Canonical UGM title: What happens when we differentiate $\sin^4x + 2 \cos^2x - \cos^4x$?'
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

# What happens when we differentiate $\sin^4x + 2 \cos^2x - \cos^4x$?

## Question

Verify that the differential coefficient with respect to

\(x\)

of

\[\begin{equation*} \sin^4 x + 2 \cos^2 x - \cos^4 x \end{equation*}\]

is equal to \(0\) for all values of \(x\). What deduction can be made from this result?

*[By ‘the differential coefficient’, the question means ‘the derivative’.]*

## Solution

By the

chain rule

, we have that

\[\begin{equation*} \frac{d}{dx} \sin^4 x = 4 \sin^3 x \frac{d}{dx} \sin x = 4 \sin^3 x \cos x \end{equation*}\]

and

\[\begin{equation*} \frac{d}{dx} \cos^2 x = 2 \cos x \frac{d}{dx} \cos x = -2 \cos x \sin x \end{equation*}\]

and

\[\begin{equation*} \frac{d}{dx} \cos^4 x = 4 \cos^3 x \frac{d}{dx} \cos x = - 4 \cos^3 x \sin x. \end{equation*}\]

Therefore

\[\begin{align*} \frac{d}{dx} \left( \sin^4 x + 2 \cos^2 x - \cos^4 x \right) &= \frac{d}{dx} \sin^4 x + 2 \frac{d}{dx} \cos^2 x - \frac{d}{dx} \cos^4 x \\ &= 4 \sin^3 x \cos x - 4 \cos x \sin x + 4 \cos^3 x \sin x \\ &= 4 \sin x \cos x \left( \sin^2 x + \cos^2 x - 1 \right) \\ &= 0, \end{align*}\]

as required.

We can use \(c\) for \(\cos x\) and \(s\) for \(\sin x\) in the above to simplify things (not forgetting that \(s^2 + c^2 = 1\)).

We can conclude from this that

\[\begin{equation*} \sin^4 x + 2 \cos^2 x - \cos^4 x \end{equation*}\]

is constant for every value of \(x\). By substituting \(x = 0\) into the above, this constant must equal \(0 + 2 - 1 = 1\).

Alternatively, we can say

\[\begin{align*} \sin^4 x + 2 \cos^2 x - \cos^4 x &= s^4-c^4+2c^2\\ &= (s^2+c^2)(s^2-c^2)+2c^2 \\ &= s^2 -c^2 + 2c^2\\ &= s^2 + c^2 =1. \end{align*}\]
