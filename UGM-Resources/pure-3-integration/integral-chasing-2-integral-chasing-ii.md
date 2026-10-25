---
created: 2026-10-26T02:40:04 (UTC +06:00)
source: https://undergroundmathematics.org/product-rule/integral-chasing-2
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- product-rule
- type/fluency-exercise
resource_identity:
  ugm_id: integral-chasing-2
  station: product-rule
  station_title: Product Rule & Integration by Parts
  resource_type_id: 8
  resource_type_label: Fluency exercise
  level: Developing
  ref: 7874
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: product-rule
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: product-rule
    validation_status: SUGGESTED
  spec_points:
  - code: 3.5.5
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-13 cross-map (cross-map-p3-integration.json
        (P3c lane 13) @ syllabai-experimental 21845f3)
      evidence: 'four missing-number definite integrals: INT axe^(2x) and INT x^2 sin cx by parts (3.5.5,
        twice), INT 1/(3x) = ln (3.5.1), INT cx/sqrt(25-x^2) by the substitution reading (3.5.6) - the
        technique-selection fluency showcase (flips the lane-11 non-overlap row of record routed ''P3
        3.5 Integration'')'
      rationale: 'Canonical UGM title: Integral chasing II'
      validation_status: SUGGESTED
    title: recognise when an integrand can usefully be e.g. integration of regarded as a product, and
      use integration by parts
  - code: 3.5.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-13 cross-map (cross-map-p3-integration.json
        (P3c lane 13) @ syllabai-experimental 21845f3)
      evidence: 'four missing-number definite integrals: INT axe^(2x) and INT x^2 sin cx by parts (3.5.5,
        twice), INT 1/(3x) = ln (3.5.1), INT cx/sqrt(25-x^2) by the substitution reading (3.5.6) - the
        technique-selection fluency showcase (flips the lane-11 non-overlap row of record routed ''P3
        3.5 Integration'')'
      rationale: 'Canonical UGM title: Integral chasing II'
      validation_status: SUGGESTED
    title: extend the idea of ‘reverse differentiation’ to Including examples such as ax + b 1 include
      the integration of e , , ax + b sin( ax + b ) , cos( ax + b ) , sec ( ax + b ) and 2 2 x + a
  - code: 3.5.6
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-13 cross-map (cross-map-p3-integration.json
        (P3c lane 13) @ syllabai-experimental 21845f3)
      evidence: 'four missing-number definite integrals: INT axe^(2x) and INT x^2 sin cx by parts (3.5.5,
        twice), INT 1/(3x) = ln (3.5.1), INT cx/sqrt(25-x^2) by the substitution reading (3.5.6) - the
        technique-selection fluency showcase (flips the lane-11 non-overlap row of record routed ''P3
        3.5 Integration'')'
      rationale: 'Canonical UGM title: Integral chasing II'
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

# Integral chasing II

> Excerpt: This resource is made up of four integrals that require the use of a variety of techniques. Students will have to decide which integration technique to use for each integral and solve them to find the unknowns $a, b, c$ and $d$.

## Problem

Can you find the missing positive numbers \(a\) to \(d\)?

1. \(\displaystyle{\int_1^a \dfrac{1}{3x} \,dx = \ln 2}\)

---

1. \(\displaystyle{\int_0^3 ax e^{2x} \,dx = be^6 + 2}\)

---

1. \(\displaystyle{\int_{1}^{3} \dfrac{cx}{\sqrt{25-x^2}} \,dx = 4\sqrt{6} - 4c}\)

---

1. \(\displaystyle{\int_{\frac{\pi}{2}}^{\frac{b}{a}\pi} x^2\sin cx \,dx = \dfrac{\pi d - \pi^2 + c}{a}}\)

## Solution

We will work through the integrals in order, but they can be tackled in a variety of ways.

\[\begin{align*} \int_1^a \dfrac{1}{3x} \,dx &= \left[\frac{1}{3}\ln(3x)\right]_{1}^{a} \\ &= \frac{1}{3}\big(\ln3a - \ln3\big) \\ &= \frac{1}{3}\ln\left(\frac{3a}{3}\right) \\ &= \ln{a^{\frac{1}{3}}} \end{align*}\]

So \(\ln{a^{\frac{1}{3}}} = \ln2\) which gives us \(a = 8\).

We have treated this integral as \(\displaystyle{\int_1^a \dfrac{1}{(3x)} \,dx}\), but what happens if we think of it as \(\displaystyle{\dfrac{1}{3}\int_1^a \dfrac{1}{x} \,dx}\)? Do both approaches give the same answer?

What method will we use for integrating this? We have a product of two different functions so it looks like integration by parts will be useful. \[\int uv' \, dx = uv - \int u'v \, dx\] Which function will we integrate and which will we differentiate?

Since we know that \(a = 8\), we have two functions, \(8x\) and \(e^{2x}\). We can differentiate both these functions, but \(8x\) will become a constant so let’s take \(u = 8x\) and \(v' = e^{2x}\). That gives us \(u'=8\) and \(v = \frac{1}{2}e^{2x}\). Therefore the integral can be written as:

\[\begin{align*} \int_0^3 8x e^{2x} \,dx &= \left[4xe^{2x}\right]_0^3 - \int_0^3 4e^{2x} \, dx \\ &= \left[4xe^{2x} - 2e^{2x} \right]_0^3 \\ &= (12e^6 - 2e^6) - (0 - 2e^0) \\ &= 10e^6 + 2. \end{align*}\]

Comparing the answers we have \(10e^6+2 = be^6 + 2\), so \(b = 10\).

The function in the numerator is a multiple of the derivative of the function in the square root, so it seems reasonable to think that we should try integration by substitution.

Let \(u = 25-x^2\), then \(du = -2x \ dx\). Some manipulation is required to get the integral in the form we need.

\[\int_{1}^{3} \dfrac{cx}{\sqrt{25-x^2}} \,dx = -\dfrac{c}{2} \int_{1}^{3} \dfrac{-2x}{\sqrt{25-x^2}} \, dx\]

Now we can make the substitution.

\[\begin{align*} -\dfrac{c}{2} \int_{1}^{3} \dfrac{-2x}{\sqrt{25-x^2}} \, dx &= -\dfrac{c}{2} \int_{u = 24}^{u=16} \dfrac{1}{\sqrt{u}} \, du \\ &= -\dfrac{c}{2} \left[2u^{\frac{1}{2}}\right]_{u=24}^{u=16} \\ &= -c \big(\sqrt{16} - \sqrt{24} \big) \\ &= 2c\sqrt{6} - 4c \end{align*}\]

If we compare this to the answer given we have \(4\sqrt{6} - 4c = 2c\sqrt{6} - 4c\), so \(c = 2\).

When using integration by substitution there is likely to be more than one possible substitution that could be used. What other substitutions could be used here?

As in the second integral we have the product of two unrelated functions so it makes sense to try integration by parts. Which way round should the choices for \(u\) and \(v'\) be?

We start by substituting in the values of \(a, b\) and \(c\).

\[\int_{\frac{\pi}{2}}^{\frac{5}{4}\pi} x^2\sin 2x \,dx\]

If \(u = x^2\) and \(v' = \sin2x\) then we have \(u' = 2x\) and \(v = -\frac{1}{2}\cos2x\).

\[\begin{align*} \int_{\frac{\pi}{2}}^{\frac{5}{4}\pi} x^2\sin 2x \,dx &= \left[-\frac{1}{2}x^2\cos2x\right]_{\frac{\pi}{2}}^{\frac{5}{4}\pi} - \int_{\frac{\pi}{2}}^{\frac{5}{4}\pi} -x\cos2x \, dx \end{align*}\]

Using integration by parts hasn’t reduced this to an integral that we can now solve but it has reduced the polynomial term from \(x^2\) to \(x\).

While we can’t solve this directly, it has got us one step closer. It is now similar to the second integral and we can use integration by parts for a second time where \(u = x\) and \(v'= \cos2x\), and \(u'=1\) and \(v = \frac{1}{2}\sin2x\).

\[\begin{align*} \left[-\frac{1}{2}x^2\cos2x\right]_{\frac{\pi}{2}}^{\frac{5}{4}\pi} + \int_{\frac{\pi}{2}}^{\frac{5}{4}\pi} x\cos2x \, dx &= \left[-\frac{1}{2}x^2\cos2x + \frac{1}{2}x\sin2x\right]_{\frac{\pi}{2}}^{\frac{5}{4}\pi} - \int_{\frac{\pi}{2}}^{\frac{5}{4}\pi} \frac{1}{2}\sin2x \, dx \\ &= \left[-\frac{1}{2}x^2\cos2x + \frac{1}{2}x\sin2x\ + \frac{1}{4}\cos2x\right]_{\frac{\pi}{2}}^{\frac{5}{4}\pi} \end{align*}\]

Before we substitute in the limits it is worth noticing that all our trigonometric functions have an argument of \(2x\). When substituting \(x =\frac{5\pi}{4}\) or \(x = \frac{\pi}{2}\) into the trigonometric functions we will get the following values.

\(\cos(\frac{5\pi}{2}) = 0\)

\(\sin(\frac{5\pi}{2}) = 1\)

\(\sin\pi = 0\)

\(\cos\pi = -1\)

Therefore when we evaluate the expression we get

\[\left(0+\frac{1}{2}\times\dfrac{5\pi}{4}\times1 + 0\right) - \left(-\dfrac{1}{2}\times(\dfrac{\pi}{2})^2\times-1 + 0 + \dfrac{1}{4}\times1\right) = \dfrac{5\pi}{8} - \dfrac{\pi^2}{8} + \dfrac{1}{4}.\]

We can use the answer given in the question to check our values for \(a, b\) and \(c\) and to find the value for \(d\).

\[\begin{align*} \dfrac{\pi d - \pi^2 + c}{a} &= \dfrac{5\pi}{8} - \dfrac{\pi^2}{8} + \dfrac{1}{4} \\ &= \dfrac{5\pi - \pi^2 +2}{8} \end{align*}\]

We can be confident that \(d = 5\) since our values for \(a\) and \(c\) match what we have already found.
