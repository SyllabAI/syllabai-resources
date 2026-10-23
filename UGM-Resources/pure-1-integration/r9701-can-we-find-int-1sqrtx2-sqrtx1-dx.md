---
created: 2026-10-24T04:45:46 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/r9701
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/review-question
resource_identity:
  ugm_id: r9701
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9701
  old_site_id: None
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
  spec_points:
  - code: 1.8.1
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-8 cross-map (cross-map-integration.json (P3c lane 8) @ syllabai-experimental c04abfbd)"
      evidence: "part (i) rationalises 1/(sqrt(x+2)-sqrt(x+1)) into sqrt(x+2)+sqrt(x+1) and integrates the (x+c)^(1/2) terms — canonical (ax+b)^n antiderivatives; the surrounding parts (trig substitution, partial fractions) are P3-dressed and the lane-6 routing named 1.8 Integration as the home"
      rationale: "Canonical UGM title: \"Can we find $\\int 1/(\\sqrt{x+2} - \\sqrt{x+1}) dx$?\"; exam provenance: UCLES A level Mathematics B Special paper, QP 9202/0, 1981, Q3"
      validation_status: SUGGESTED
    title: "understand integration as the reverse process of differentiation, and integrate ( ax + b ) (for any rational n except –1), together with constant multiples, sums and differences"
  mapped_date: '2026-10-24'
  mapper: cross-map-integration.json (P3c lane 8) @ syllabai-experimental c04abfbd
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "UCLES A level Mathematics B Special paper, QP 9202/0, 1981, Q3"
task: T-UGM-IMPORT-8
---

# Can we find $\int 1/(\sqrt{x+2} - \sqrt{x+1}) dx$?

## Question

1. By using the substitution \(x = \cos \theta\), or otherwise, evaluate \[\begin{equation*} \int_0^1 \frac{1}{(1-x)^{1/2}(1+x)^{3/2}} \:dx. \end{equation*}\]

---

1. Find \[\begin{align*} \text{(i)}\; &\int \frac{1}{\sqrt{x+2} - \sqrt{x+1}} \:dx, \\ \text{(ii)}\; &\int \frac{x}{(x+1)(x+2)^2} \:dx. \end{align*}\]

## Solution

If

\(x = \cos \theta\)

, then

\(dx = -\sin \theta \:d\theta\)

, and so

\[\begin{align*} \int_0^1 \frac{1}{(1-x)^{1/2}(1+x)^{3/2}} \:dx &= \int_{\pi/2}^0 \frac{-\sin \theta}{(1 - \cos \theta)^{1/2}(1 + \cos \theta)^{3/2}} \:d\theta \\ &= \int_0^{\pi/2} \frac{\sin \theta}{(1 - \cos \theta)^{1/2}(1 + \cos \theta)^{3/2}} \:d\theta \\ &= \int_0^{\pi/2} \frac{\sin \theta}{(1 - \cos \theta)^{1/2}(1 + \cos \theta)^{1/2}(1 + \cos \theta)} \:d\theta \\ &= \int_0^{\pi/2} \frac{\sin \theta}{(1 - \cos^2 \theta)^{1/2}(1 + \cos \theta)} \:d\theta \\ &= \int_0^{\pi/2} \frac{d\theta}{1 + \cos \theta}. \end{align*}\]

From the

double angle formula for cosine

, we have that

\[\begin{equation*} \cos \theta = \cos^2 \frac{\theta}{2} - \sin^2 \frac{\theta}{2} = 2 \cos^2 \frac{\theta}{2} - 1 \implies 1 + \cos \theta = 2 \cos^2 \frac{\theta}{2}. \end{equation*}\]

Hence,

\[\begin{align*} \int_0^{\pi/2} \frac{d\theta}{1 + \cos \theta} &= \frac{1}{2} \int_0^{\pi/2} \sec^2 \frac{\theta}{2} \:d\theta\\ &=\left[\tan \dfrac{\theta}{2}\right]_0^{\pi/2}\\ &= \tan \frac{\pi}{4} - \tan 0 = 1. \end{align*}\]

1. Find \[\begin{align*} \text{(i)}\; &\int \frac{1}{\sqrt{x+2} - \sqrt{x+1}} \:dx, \\ \end{align*}\]

Rationalising the denominator, we have that

\[\begin{align*} \int \frac{1}{\sqrt{x+2} - \sqrt{x+1}} \:dx &= \int \frac{\sqrt{x+2} + \sqrt{x+1}}{(\sqrt{x+2} - \sqrt{x+1})(\sqrt{x+2} + \sqrt{x+1})} \:dx \\ &= \int \frac{\sqrt{x+2} + \sqrt{x+1}}{(x+2) - (x+1)} \:dx \\ &= \int \sqrt{x+2} + \sqrt{x+1} \:dx \\ &= \frac{(x+2)^{3/2}}{\frac{3}{2}} + \frac{(x+1)^{3/2}}{\frac{3}{2}} + c \\ &= \frac{2}{3} \left( (x+2)^{3/2} + (x+1)^{3/2} \right) + c \end{align*}\]

where \(c\) is a constant of integration.

\[\begin{align*} \text{(ii)}\; &\int \frac{x}{(x+1)(x+2)^2} \:dx. \end{align*}\]

We can attempt to rewrite the integrand using partial fractions: that is, we would hope that there are constants

\(A\)

,

\(B\)

, and

\(C\)

such that

\[\begin{equation*} \frac{x}{(x+1)(x+2)^2} = \frac{A}{x+1} + \frac{B}{x+2} +\frac{C}{(x+2)^2}= \frac{A(x+2)^2 + B(x+1)(x+2)+C(x+1)}{(x+1)(x+2)^2}. \end{equation*}\]

Thus \(x = A(x+2)^2 + B(x+1)(x+2)+C(x+1)\) for all values of \(x\).

Putting \(x = -1\), we have \(A = -1\), while putting \(x = -2\) gives \(C=2\) and putting \(x = 0\) yields \(B = 1\).

As a result,

\[\begin{align*} \frac{x}{(x+1)(x+2)^2} &= \frac{1}{x+2} + \frac{2}{(x+2)^2} - \frac{1}{x+1} \end{align*}\]

and so

\[\begin{align*} \int \frac{x}{(x+1)(x+2)^2} \:dx &= \int \frac{1}{x+2} + \frac{2}{(x+2)^2} - \frac{1}{x+1} \:dx \\ &= \ln\big\vert x+2\big\vert - \frac{2}{x+2} - \ln\big\vert x+1\big\vert + c \end{align*}\]

where \(c\) is a constant of integration.
