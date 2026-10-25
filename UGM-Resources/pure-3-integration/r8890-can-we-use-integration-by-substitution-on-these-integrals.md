---
created: 2026-10-26T02:40:04 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/r8890
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/review-question
resource_identity:
  ugm_id: r8890
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8890
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
      evidence: INT_0^(1/2) x/(1-x^2)^2 dx by the GIVEN substitution u = 1 - x^2 with limit transformation,
        then INT sin theta/cos^3 theta dtheta by u = cos theta or the tan sec^2 rewrite - the exact CIE
        'use a given substitution' task (flips the lane-12 non-overlap row of record routed 'P3 3.5 Integration')
      rationale: 'Canonical UGM title: Can we use integration by substitution on these integrals?'
      validation_status: SUGGESTED
    title: use a given substitution to simplify and evaluate e.g. to integrate either a definite or an
      indefinite integral.
  mapped_date: '2026-10-26'
  mapper: cross-map-p3-integration.json (P3c lane 13) @ syllabai-experimental 21845f3
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-13
---

# Can we use integration by substitution on these integrals?

## Question

1. By using the substitution \(u = 1 - x^2\), or otherwise, evaluate \[\begin{equation*} \int_0^{\frac{1}{2}} \frac{x}{(1-x^2)^2} \:dx. \end{equation*}\]

---

1. Evaluate \[\begin{equation*} \int_0^{\pi/6} \frac{\sin \theta \:d\theta}{\cos^3 \theta}. \end{equation*}\]

## Solution

If we take

\(u = 1 - x^2\)

, then

\[\begin{equation*} \frac{du}{dx} = -2x \implies du = -2x \:dx \end{equation*}\]

and therefore, by substitution,

\[\begin{align*} \int_0^{\frac{1}{2}} \frac{x}{(1-x^2)^2} \:dx = \int_{1-0}^{1-\left(\frac{1}{2}\right)^2} \frac{du}{-2u^2} &= \frac{1}{2} \int_{\frac{3}{4}}^1 \frac{du}{u^2} \\ &= \frac{1}{2} \left[ \frac{u^{-1}}{-1} \right]_{\frac{3}{4}}^1 \\ &= -\frac{1}{2} \left( 1 - \frac{4}{3} \right) \\ &= \frac{1}{6}. \end{align*}\]

Note how we can make an integral look simpler by factoring out constants, including negatives which we can take care of by swapping the limits over.

In part (i) the \(x^2\) in the substitution dealt with the \(x\) in the numerator. In the same way here we don’t need to worry about the \(\sin \theta\) if we have \(\cos \theta\) in the substitution—we can be confident it will get sorted out along the way.

Take

\(u = \cos \theta\)

, so that

\[\begin{equation*} \frac{du}{d\theta} = -\sin \theta \implies du = - \sin \theta \:d\theta. \end{equation*}\]

By substitution, then,

\[\begin{align*} \int_0^{\pi/6} \frac{\sin \theta \:d\theta}{\cos^3 \theta} = \int_{\cos 0}^{\cos \frac{\pi}{6}} \frac{-du}{u^3} &= - \left[ \frac{u^{-2}}{-2} \right]_1^{\sqrt{3}/2} \\ &= \frac{1}{2} \left( \left( \frac{2}{\sqrt{3}} \right)^2 - 1 \right) \\ &= \frac{1}{6}. \end{align*}\]
