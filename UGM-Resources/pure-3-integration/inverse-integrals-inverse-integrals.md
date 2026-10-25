---
created: 2026-10-26T02:40:04 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-trig-log/inverse-integrals
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-trig-log
- type/food-for-thought
resource_identity:
  ugm_id: inverse-integrals
  station: calculus-trig-log
  station_title: Calculus of Trigonometry & Logarithms
  resource_type_id: 9
  resource_type_label: Food for thought
  level: Developing
  ref: 7564
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
  - code: 3.5.1
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-13 cross-map (cross-map-p3-integration.json
        (P3c lane 13) @ syllabai-experimental 21845f3)
      evidence: INT_2^3 ln x dx via the inverse-function area argument (no antiderivative taken) - the
        definite integral of the 3.5.1-listed-adjacent ln is the outcome; the non-standard area method
        is disclosed of record (the by-parts route exists in the corpus under lane 8; this resource's
        method is the recorded alternative) (flips the lane-10 non-overlap row of record routed 'P3 3.5
        Integration')
      rationale: 'Canonical UGM title: Inverse integrals'
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

# Inverse integrals

> Excerpt: Students are asked to think about inverse functions in order to find a definite integral involving $\ln x$. Can they find a method to calculate certain integrals without knowing how to integrate the function directly?

## Warm-up

Take a look at these graphs.

Say what you see…

|  |  |
|---|---|

Things to think about

- Is there any information you can add to the graphs?

- What links are there between the two diagrams?

- What shapes can you see in the diagrams? Can you work out their areas?

## Warm-up ideas

Take a look at these graphs.

Say what you see…

|  |  |
|---|---|

Here are some things you might have noticed.

- There are two different graphs: each has a function and two \(x\)-coordinates given. There is an area shaded on each graph but they are in different places. One is between the curve and the \(y\)-axis and the other between the curve and the \(x\)-axis.

- Neither curve has any \(y\)-coordinates labelled so we can add these to the diagram. For \(y = e^x\), the \(y\)-coordinates are \(2\) and \(3\). For \(y = \ln x\) they are \(\ln 2\) and \(\ln 3\). So the same numbers appear in both graphs except the \(x\) and \(y\)-coordinates have swapped over.

- The swapping of coordinates might remind us that there is a relationship between \(e^x\) and \(\ln x\). They are inverse functions of each other, which we can think about graphically as a reflection in \(y = x\).

This symmetry around \(y = x\) is not immediately obvious from the diagrams, as the scaling in the \(x\) and \(y\) directions is different on each sketch. It is important not to make assumptions about shape or symmetry based on sketch graphs.

- There are two rectangles on each graph with areas of \(2 \times \ln 2\) and \(3 \times \ln 3\) respectively. These areas are the same on both graphs as the \(x\) and \(y\) coordinates are reflected in \(y=x\).

What can we say about the curved regions in the diagrams?

- The symmetry of the graphs implies that the two shaded areas are actually identical as they are reflected across \(y=x\). They could be represented by the integral \(\displaystyle{\int_2^{3} \ln x \, dx}\) or the integral \(\displaystyle{\int_2^{3} \ln y \, dy}.\)

Can you see which area is represented by which integral?

- We can also find the area of other regions bounded by the curves. For example, the area A can be represented by the integral
 
 \(\displaystyle{\int_{\ln 2}^{\ln 3} e^x \, dx}.\)

As inverse functions have symmetry around \(y = x\), we know that area A is the same as area B, shaded in the diagram below.

How would we represent B as an integral?

## Problem

|  |  |
|---|---|

Use the diagrams to help you find \(\displaystyle{\int_2^3 \ln x \, dx}\).

Use a similar method to find \(\displaystyle{\int_{\frac{1}{2}}^{\frac{\sqrt3}{2}} \arcsin x \, dx}\).

## Solution

This solution will be based on ideas from the warm-up, so you may wish to look at the [Warm-up ideas](https://undergroundmathematics.org/calculus-trig-log/inverse-integrals/ideas) section if you haven’t already done so.

The integral represents the area of the shaded region under the curve \(y = \ln x\). However, we also know that because these graphs are inverse functions, the shaded region between \(e^x\) and the \(y\)-axis has the same area.

If we don’t know how to integrate \(\ln x\) directly, then we need to use other areas that we do know how to find. We have already calculated the areas of the large rectangle, \(3\ln 3\), and the smaller rectangle, \(2\ln 2\).

Therefore the L-shaped shaded region has area \(3\ln 3 - 2\ln 2\).

The area between the curve, the

\(y\)

-axis,

\(\ln 2\)

and

\(\ln 3\)

is given by the integral

\[\begin{align*} \displaystyle{\int_{\ln 2}^{\ln 3} e^y \, dy} &= \left[e^y \right]_{\ln 2}^{\ln 3} \\ &= 3 - 2 \\ &= 1. \end{align*}\]

Putting all these together means the area represented by

\(\displaystyle{\int_2^3 \ln x \, dx}\)

can be found by

\[\begin{align*} \int_2^3 \ln x \, dx &= 3\ln 3 - 2\ln 2 - \int_{\ln 2}^{\ln 3} e^y \, dy \\ &= 3\ln 3 - 2\ln 2 - 1 \end{align*}\]

The answer can be written in several different forms. If you combined the logarithms you might have ended up with \(\ln \left(\frac{27}{4}\right) - 1\) or \(\ln \left(\frac{27}{4e}\right)\).

Remember [\(\arcsin x\)](https://undergroundmathematics.org/glossary/inverse-trigonometric-function) is the same as \(\sin^{-1} x\).

We could have sketched the graph of \(y= \sin x\) instead and thought about the area between the curve and the \(y\)-axis.

In this case we find

\[\begin{align*} \int_{\frac{1}{2}}^{\frac{\sqrt{3}}{2}} \arcsin x \, dx &= \frac{\pi}{3}\cdot\frac{\sqrt{3}}{2} - \frac{\pi}{6}\cdot\frac{1}{2} - \int_{\frac{\pi}{6}}^{\frac{\pi}{3}} \sin y \, dy \\ &= \frac{\sqrt{3}\pi}{6} - \frac{\pi}{12} + \frac{1-\sqrt{3}}{2} \end{align*}\]

We have seen that we can find the definite integral of any function if it has an inverse function that is easy to integrate.

Is it also possible to work out the indefinite integral? What happens if you think about the integral \[\displaystyle{\int_a^x \ln t \, dt}?\]
