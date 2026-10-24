---
created: 2026-10-25T01:37:17 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/r8694
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/review-question
resource_identity:
  ugm_id: r8694
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8694
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
  - code: 3.1.5
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-9 cross-map (cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb)"
      evidence: "∫√(x+1)/(x−3)dx via u²=x+1 reduces to polynomial division plus 8/((u−2)(u+2)) split by partial fractions"
      rationale: "Canonical UGM title: How could we integrate $\\tan^3 \\theta$?"
      validation_status: SUGGESTED
    title: "recall an appropriate form for expressing rational functions in partial fractions, and carry out the decomposition, in cases where the denominator is no more complicated than ( ax + b )( cx + d )( ex + f ), ( ax + b )( cx + d )², ( ax + b )( cx² + d )"
  mapped_date: '2026-10-25'
  mapper: cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "UCLES A level Mathematics A 1, QP 840/1, 1973, Q11"
  task: T-UGM-IMPORT-9
---

# How could we integrate $\tan^3 \theta$?

## Question

1. Evaluate \[\begin{equation*} \int_0^{\tfrac{1}{4} \pi} \tan^3 \theta \:d\theta, \end{equation*}\] giving the answer correct to two significant figures.

---

1. By using the substitution \(x+1 = u^2\), or otherwise, find \[\begin{equation*} \int \frac{\sqrt{x+1}}{x-3} \:dx. \end{equation*}\]

## Solution

We can use the identity

\(\sec^2 \theta = \tan^2 \theta + 1\)

to help us:

\[\begin{align*} \int_0^{\tfrac{1}{4} \pi} \tan^3 \theta \:d\theta &= \int_0^{\tfrac{1}{4} \pi} (\tan^2 \theta) \tan \theta \:d\theta\\ &= \int_0^{\tfrac{1}{4} \pi} (\sec^2 \theta-1) \tan \theta \:d\theta\\ &= \int_0^{\tfrac{1}{4} \pi} \sec^2 \theta\tan \theta - \tan \theta \:d\theta\\ \end{align*}\]

So we have two integrals to calculate; the first is

\[\int_0^{\tfrac{1}{4} \pi} \sec^2 \theta\tan \theta \:d\theta\]

We notice that \(\dfrac{d}{d \theta} \tan \theta = \sec^2 \theta\) (this is a standard result). So, letting \(u = \tan \theta\), our integral becomes

\[\int_0^{\tfrac{1}{4} \pi} u \dfrac{du}{d\theta} \:d\theta = \int_0^{\tan \tfrac{\pi}{4}} u \:du = \dfrac{1}{2} \left[\dfrac{u^2}{2}\right]_0^{\tan \tfrac{\pi}{4}} = \dfrac{1}{2} - 0 = \dfrac{1}{2}\]

Our second integral is

\[\int_0^{\tfrac{1}{4} \pi} tan \theta \:d\theta = \int_0^{\tfrac{1}{4} \pi} \dfrac{\sin \theta}{\cos \theta} \:d\theta\]

We can calculate this by writing \(\tan \theta = \dfrac{\sin \theta}{\cos \theta}\), substituting \(v = \cos \theta\), and noticing that \(-\sin \theta \:d\theta = \:dv\), so our integral is in fact

\[\int_0^{\tfrac{1}{4} \pi} \dfrac{-1}{v} \dfrac{\:d v}{\:d \theta} \:d\theta = \int_0^{\cos \tfrac{\pi}{4}} \dfrac{-1}{v} \:dv = - \biggl[ \ln v \biggr]_1^{\cos \tfrac{\pi}{4}} = \biggl[ \ln \dfrac{1}{v} \biggr]_1^{\tfrac{1}{\sqrt 2}} = \ln{\sqrt 2} - \ln 1 = \dfrac{1}{2} \ln 2\]

So our final value for \(\int_0^{\tfrac{1}{4} \pi} \tan^3 \theta \:d\theta\) is

\[\dfrac{1}{2} - \dfrac{1}{2} \ln 2 = 0.1534...\]

which equals

\(0.15\)

to two significant figures.

Alternatively, we can use substitution in a different way. Let

\(u = \tan \theta\)

, so that

\[\begin{equation*} \frac{du}{d\theta} = \sec^2 \theta = 1 + \tan^2 \theta = 1 + u^2 \end{equation*}\]

and hence

\[\begin{align*} \int_0^{\tfrac{1}{4} \pi} \tan^3 \theta \:d\theta = \int_0^1 \frac{u^3}{1 + u^2} \:du &= \int_0^1 \frac{u(1 + u^2)}{1 + u^2} - \frac{u}{1 + u^2} \:du \\ &= \left[ \frac{u^2}{2} \right]_0^1 - \frac{1}{2} \int_0^1 \frac{2u}{1 + u^2} \:du \\ &= \frac{1}{2} - \frac{1}{2} \left[ \log(1 + u^2) \right]_0^1 \\ &= \frac{1}{2} - \frac{\log 2}{2} \\ &= 0.1534\!\ldots \end{align*}\]

which equals \(0.15\) to two significant figures.

Take \(x+1 = u^2\), so that \(x = u^2 - 1\), and \(dx = 2u du\).

Hence,

\[\begin{align*} \int \frac{\sqrt{x+1}}{x-3} \:dx &= \int \frac{u}{u^2-4} 2u\:du \\ &= \int \frac{2u^2 - 8+8}{u^2 - 4} \:du\\ &= \int 2 + \frac{8}{(u-2)(u+2)} \:du. \end{align*}\]

We can use partial fractions,

\[\begin{align*} \frac{8}{(u-2)(u+2)} &= \frac{A}{u-2} + \frac{B}{u+2}\\ \implies\quad 8 &= A(u+2) + B(u-2) \end{align*}\]

and substituting

\(u=\pm 2\)

we find

\(A=2\)

and

\(B=-2\)

. Hence,

\[\begin{align*} \int \frac{\sqrt{x+1}}{x-3} \:dx &= 2u + 2 \int \frac{1}{(u-2)} - \frac{1}{(u+2)} \:du \\ &= 2u + 2 \log(u-2) - 2\log(u+2) + c \\ &= 2\sqrt{x+1} + 2\log(\sqrt{x+1} - 2) - 2\log(\sqrt{x+1} + 2) + c. \end{align*}\]
