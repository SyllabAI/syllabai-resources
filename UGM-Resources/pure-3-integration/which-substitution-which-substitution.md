---
created: 2026-10-26T02:40:04 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/which-substitution
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/rich-example
resource_identity:
  ugm_id: which-substitution
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 2
  resource_type_label: Rich example
  level: Developing
  ref: 6297
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
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-13 cross-map (cross-map-p3-integration.json
        (P3c lane 13) @ syllabai-experimental 21845f3)
      evidence: INT 1/sqrt(1-x^2) dx via x = sin theta and x = cos theta giving apparently different answers
        reconciled by the constant - the substitution-mechanics + constant-of-integration reasoning; the
        arcsin integrand is beyond the 3.5 list and disclosed (the recorded in-spec skill is the substitution
        technique itself)
      rationale: 'Canonical UGM title: Which substitution?'
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

# Which substitution?

> Excerpt: Students are asked to do the same integral twice, using a different substitution each time. The problem highlights that you can arrive at different answers because of this, and asks students to think about how the two answers are related.

## Problem

\(\displaystyle{\int \dfrac{1}{\sqrt{1-x^2}} \, dx}\) can be integrated by using a substitution. What answer do you get if you use

1. \(x = \sin \theta\)?

---

1. \(x = \cos \theta\)?

Do they both give the correct answer? If so, why?

## Solution

1. If \(x = \sin \theta\), then \(\dfrac{dx}{d\theta} = \cos \theta\), meaning we can write \(dx = \cos \theta \ d\theta\). Substituting this into the integral we get

\[\begin{align*} \int \dfrac{1}{\sqrt{1-x^2}} \, dx &= \int \dfrac{1}{\sqrt{1-\sin^2 \theta}} \ \cos \theta \, d\theta\\ &= \int \dfrac{1}{\cos \theta} \ \cos \theta \, d\theta \\ &= \int 1 \, d\theta \\ &= \theta + c. \end{align*}\]

As \(x = \sin \theta\), then \(\theta = \arcsin x\), so the answer in terms of \(x\) is \[\displaystyle{\int \dfrac{1}{\sqrt{1-x^2}} \, dx = \arcsin x + c}.\]

Remember that [inverse trigonometric functions](https://undergroundmathematics.org/glossary/inverse-trigonometric-function) can be written in two different ways. For example \(\arcsin\) and \(\sin^{-1}\).

1. This time \(x = \cos \theta\), so \(\dfrac{dx}{d\theta} = -\sin \theta\). Writing \(dx = -\sin \theta \ d\theta\) gives us

\[\begin{align*} \int \dfrac{1}{\sqrt{1-x^2}} \, dx &= \int \dfrac{1}{\sqrt{1-\cos^2 \theta}} \cdot (-\sin \theta) \, d\theta\\ &= \int -1 \, d\theta \\ &= -\theta + c. \end{align*}\]

As \(x = \cos \theta\), \(\theta = \arccos x\), so this time we get the answer \[\displaystyle{\int \dfrac{1}{\sqrt{1-x^2}} \, dx = -\arccos x + c}.\]

| The fact that the answers are both inverse trigonometric functions suggests there is a relationship between them. The easiest way to think about their differences and similarities is to sketch the graphs of both functions. We see that \(y = -\arccos x\) is the same shape as \(y = \arcsin x\) , the only difference being a translation of \(\frac{π}{2}\) along the \(y\) axis. This difference can be accounted for by the constants of integration. |  |
|---|---|

We could also think about this algebraically. If we let \(y = \arcsin x\), then \(\sin y = x.\) As \(\sin y = \cos(\frac{\pi}{2} - y)\) we can write

\[\begin{align*} &&\cos\left(\frac{\pi}{2} - y\right) &= x \\ \iff&& \frac{\pi}{2} - y &= \arccos x \\ \iff&& \frac{\pi}{2} - \arcsin x &= \arccos x. \end{align*}\]

The second line of this argument will not always follow on from the first, as it depends on the range of values for \(y\). Can you see why it is valid in this case?

This method also shows that the values of \(\arcsin x\) and \(-\arccos x\) differ by \(\frac{\pi}{2},\) or in fact, that \(\arcsin x + \arccos x = \frac{\pi}{2}.\)

**Reflection**

Does having a different antiderivative function affect the solution to a definite integral? Remember, \[\int_a^b f(x) \, dx = F(b) - F(a).\]

It is useful to realise that there can be more than one form of answer to an integral. This happens particularly when using trigonometric substitutions as there are so many ways that different functions can be written in terms of each other.
