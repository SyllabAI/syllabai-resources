---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/powerful-derivatives
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/building-blocks
resource_identity:
  ugm_id: powerful-derivatives
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 1
  resource_type_label: Building blocks
  level: Developing
  ref: 5348
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
      evidence: prove d/dx x^a = a x^(a-1) for real a by writing x^a = e^(a ln x) and chaining the standard
        derivatives - the ln/exponential derivative law of 3.4.1 is the engine (flips the lane-10 non-overlap
        row of record routed 'P3 3.4 Differentiation')
      rationale: 'Canonical UGM title: Powerful derivatives'
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

# Powerful derivatives

> Excerpt: Students are invited to prove that the derivative of $x^a$ is $ax^{a-1}$ for any real value of $a$.

## Problem

In [Binomials are the answer!](https://undergroundmathematics.org/calculus-of-powers/binomials-are-the-answer), we proved that the derivative of \(x^n\) is \(nx^{n-1}\) for any positive integer \(n\).

Using exponentials and/or logarithms, can you now prove that the derivative of \(x^a\) (where \(x>0\) and \(a\) is any real number) is \(ax^{a-1}\)?

## Solution

If we write

\(x=e^{\ln x}\)

, then

\(x^a\)

becomes

\(e^{a\ln x}\)

. If we write

\(u=a\ln x\)

, then we can differentiate this using the chain rule (in the form

\(\frac{dy}{dx}=\frac{dy}{du}\times\frac{du\vphantom{y}}{dx}\)

, with

\(y=e^u\)

):

\[\begin{align*} \frac{d}{dx}(e^{a\ln x})&=\frac{d}{du}(e^u)\times \frac{d}{dx}(a\ln x)\\ &=e^u\times\frac{a}{x}\\ &=e^{a\ln x}\times\frac{a}{x}\\ &=x^a\times\frac{a}{x}\\ &=ax^{a-1} \end{align*}\]

as we wanted.

This idea of writing \(x^a\) as \(e^{a\ln x}\) is actually the simplest and most useful way to define arbitrary powers. If we tried to define powers in a different way, it would turn out to be quite difficult to prove that the derivative of \(x^{\pi}\) is \(\pi x^{\pi-1}\), for example.

You may also have thought of proving this result using the general binomial theorem using a similar approach to that in [Binomials are the answer!](https://undergroundmathematics.org/calculus-of-powers/binomials-are-the-answer), as follows.

The derivative of

\(x^a\)

is the limit of

\(\dfrac{(x+h)^a-x^a}{h}\)

as

\(h\to0\)

. Then using the binomial theorem, we have

\[\begin{align*} (x+h)^a &= x^a\left(1+\frac{h}{x}\right)^a\\ &= x^a\left(1+a\cdot\frac{h}{x}+\frac{a(a-1)}{2}\cdot\left(\frac{h}{a}\right)^2+\cdots\right). \end{align*}\]

Then subtracting \(x^a\) and dividing by \(h\) gives \[\dfrac{(x+h)^a-x^a}{h} = x^a\left(a\cdot\frac{1}{x}+\frac{a(a-1)}{2}\cdot\frac{h}{a^2}+\cdots\right)\] As \(h\to0\), the right hand side tends to \(x^a\cdot\frac{a}{x}=ax^{a-1}\), as required.

It turns out that there is a subtle difficulty with this approach. It uses the general binomial theorem for \((1+x)^a\), but how do we prove that? The usual way to do so is to use [Taylor’s theorem](https://undergroundmathematics.org/glossary/taylor-series), but that requires us to already know the derivative of \(x^a\)…. So this would be a circular argument! But now that we can differentiate \(x^a\) without reference to the binomial theorem, we can use this to prove the general binomial theorem, and all works nicely.
