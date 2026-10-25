---
created: 2026-10-26T02:40:04 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-trig-log/trigsy-integrals
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-trig-log
- type/many-ways-problem
resource_identity:
  ugm_id: trigsy-integrals
  station: calculus-trig-log
  station_title: Calculus of Trigonometry & Logarithms
  resource_type_id: 4
  resource_type_label: Many ways problem
  level: Developing
  ref: 8150
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
  - code: 3.5.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-13 cross-map (cross-map-p3-integration.json
        (P3c lane 13) @ syllabai-experimental 21845f3)
      evidence: INT cos 2x (3.5.1 composite) and INT sin^2 x by the double-angle identity (the canonical
        3.5.2 trigonometrical-relationship integration), with the arcsin/arccos symmetric-area cards disclosed
        beyond the 3.5 list of record (flips the lane-11 non-overlap row of record routed 'P3 3.5 Integration')
      rationale: 'Canonical UGM title: Trigsy integrals'
      validation_status: SUGGESTED
    title: use trigonometrical relationships in carrying out integration or
  - code: 3.5.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-13 cross-map (cross-map-p3-integration.json
        (P3c lane 13) @ syllabai-experimental 21845f3)
      evidence: INT cos 2x (3.5.1 composite) and INT sin^2 x by the double-angle identity (the canonical
        3.5.2 trigonometrical-relationship integration), with the arcsin/arccos symmetric-area cards disclosed
        beyond the 3.5 list of record (flips the lane-11 non-overlap row of record routed 'P3 3.5 Integration')
      rationale: 'Canonical UGM title: Trigsy integrals'
      validation_status: SUGGESTED
    title: extend the idea of ‘reverse differentiation’ to Including examples such as ax + b 1 include
      the integration of e , , ax + b sin( ax + b ) , cos( ax + b ) , sec ( ax + b ) and 2 2 x + a
  mapped_date: '2026-10-26'
  mapper: cross-map-p3-integration.json (P3c lane 13) @ syllabai-experimental 21845f3
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-13
---

# Trigsy integrals

> Excerpt: Students are asked to think about the different ways they can integrate trigonometric functions such as $\sin ^2 x$ and $\arccos x$ using their knowledge of these functions and basic ideas from calculus. They do not need to have met any trigonometric integration before.

## Problem

In how many different ways can you find answers to the following integrals?

\(\displaystyle {\int_{0}^{\pi} \cos 2x \, dx}\)

\(\displaystyle {\int_{0}}^{\frac{\pi}{2}} \sin^2 x \, dx\)

\(\displaystyle {\int_{-1}^{1}} \arcsin x \, dx\)

\(\displaystyle {\int_{-1}^{1}} \arccos x \, dx\)

## Suggestion

It might be useful to sketch the graphs of the functions to be integrated. You may wish to use graphing software such as [Desmos](https://www.desmos.com/calculator) or [GeoGebra](https://www.geogebra.org/graphing).

Do the functions have any symmetry that can help?

Are there any trigonometric identities you know that involve these functions?

## Things you might have done

Below are some suggested methods for each of the integrals. Did you use any of these ideas? Did you come up with different approaches?

Sketching

When looking at the graph of \(y = \cos 2x\) we see that \(\displaystyle {\int_{0}^{\pi} \cos 2x \, dx} = 0,\) as the shaded areas above and below the \(x\)-axis cancel each other out.

Would your answer differ if the question had asked for the *area* bounded by the curve and the \(x\)-axis between \(0\) and \(\pi\)?

Transforming

If we know how to find \(\int\cos x \, dx\) then we might consider transforming \(\cos 2x\) into \(\cos x\).

The transformation is a stretch, scale factor 2, parallel to the \(x\)-axis. If we think about the integral \(\int_{0}^{\pi} \cos 2x \, dx\) being stretched by a scale factor of 2, then we see that the shaded area will double and the limits of the integral will change. Therefore we can write

\[\displaystyle {\int_{0}^{\pi} \cos 2x \, dx} = \frac{1}{2}\displaystyle {\int_{0}^{2\pi} \cos x \, dx}.\]

Of course in this case the answer is still zero, but would this approach would work no matter what the limits were?

This is a simple example of integration by substitution. Have a look at [Slippery areas](https://undergroundmathematics.org/chain-rule/slippery-areas) for a resource based on these ideas.

Rotational symmetry

Sketching the graph of \(y = \sin^2 x\) helps us to see the symmetry in the function. It is an even function and it also has rotational symmetry around points such as \((\frac{\pi}{4}, \frac{1}{2})\). If we consider the rectangle drawn above, which has an area of \(\frac{\pi}{2} \times 1\) we can say that the area beneath the function is half this value. Therefore \[\displaystyle{\int_{0}^{\frac{\pi}{2}} \sin^2 x \, dx = \frac{\pi}{4}}.\]

How can we convince ourselves that \(y = \sin^2 x\) has rotational symmetry?

Identities

Trigonometric identities give us a way to transform certain functions into others more easily. Identities that involve \(\sin^2 x\) include \(\sin ^2 x + \cos ^2 x = 1\) and \(\cos 2x = 1 - 2\sin ^2 x.\) Since we already know how to integrate \(\cos 2x\) from above, we can write:

\[\displaystyle {\int_{0}}^{\frac{\pi}{2}} \sin^2 x \, dx = \int_{0}^{\frac{\pi}{2}} \frac{1}{2} - \frac{1}{2}\cos 2x \, dx.\]

Since \(\displaystyle {\int_{0}^{\frac{\pi}{2}} \cos 2x \, dx = 0}\), we are left with \(\displaystyle \int_{0}^{\frac{\pi}{2}} \frac{1}{2} \, dx = \frac{\pi}{4}.\)

Sketching

Drawing the graph reminds us that \(\arcsin x\) is an odd function and so \(\displaystyle {\int_{-1}^{1}} \arcsin x \, dx =0.\)

You might also think about the inverse function of \(\arcsin x\) and how that could help you. To explore this idea further, have a look at [Inverse integrals](https://undergroundmathematics.org/calculus-trig-log/inverse-integrals).

Transforming

By drawing \(y = \arcsin x\) and \(y = \arccos x\) on the same graph, we can see that one can be transformed into the other.

From the graph we can write down

\(\arccos x = -\arcsin x + \dfrac{\pi}{2},\)

so

\[\begin{align*} \displaystyle {\int_{-1}^{1}} \arccos x \, dx &= \displaystyle {\int_{-1}^{1}} -\arcsin x + \dfrac{\pi}{2} \, dx \\ &= -\displaystyle {\int_{-1}^{1}} \arcsin x \, dx + \displaystyle{\int_{-1}^{1}} \dfrac{\pi}{2} \, dx \\ &= 0 + \pi \\ &= \pi. \end{align*}\]

Rotational symmetry

The rectangle drawn in diagram above has an area of \(\pi \times 2.\) Since the shaded area is half of the rectangle, we can say that \[\displaystyle {\int_{-1}^{1}} \arccos x \, dx = \pi.\]
