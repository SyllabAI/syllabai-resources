---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-trig-log/estimating-gradients
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-trig-log
- type/problem-requiring-decisions
- level/introducing
resource_identity:
  ugm_id: estimating-gradients
  station: calculus-trig-log
  station_title: Calculus of Trigonometry & Logarithms
  resource_type_id: 6
  resource_type_label: Problem requiring decisions
  level: Introducing
  ref: 5303
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-trig-log
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-trig-log
    validation_status: SUGGESTED
  spec_points:
  - code: 1.7.1
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: estimate the gradient of y=sin x at three points from tangent lines, then sketch the
        derivative — the gradient-of-a-curve skill in a trig setting; no trig derivatives required
      rationale: 'Canonical UGM title: "Estimating gradients"'
      validation_status: SUGGESTED
    title: understand the gradient of a curve at a point as the limit of the gradients of a suitable
      sequence of chords, and use the notations d y , and d y f ′ ( x ) , f ″( x ) , 2 for first and
      second derivatives
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-7
assets:
- path: https://undergroundmathematics.org/calculus-trig-log/estimating-gradients/assets/student-worksheet.pdf
  kind: printable
- path: https://undergroundmathematics.org/calculus-trig-log/estimating-gradients/download/teacher-notes.pdf
  kind: printable
---

# Estimating gradients

> Excerpt: Students are asked to estimate the gradient of a sine graph at three different points. Can they then sketch the graph of the derivative?

## Problem

Estimate the gradient of \(f(x) = \sin x\) at the points A, B and C.

Suggestion

We could draw tangent lines at A, B and C. How would this help?

## Things you might have noticed

If we draw in a tangent line at A, we will see that the gradient is, or is close to, zero.

At B we have to do a little more work. If we draw a tangent line, then we can form a right-angled triangle to help us estimate a gradient.

Why has a triangle of this size been chosen? Does it make our estimation easier?

We know the maxima and minima of a sine graph are \(1\) and \(-1\), so we could estimate the vertical height of the triangle as about 3. The base of the triangle goes from the \(x\) value of the maximum to the \(x\) value of the minimum. What is this distance?

This will depend on the scale we have imagined on the \(x\) axis. Have we thought in radians or degrees? In radians the distance between the maximum and minimum point is \(\pi\), and in degrees it is \(180^{\circ}\). This gives us two very different possible values for the gradient.

Can you produce a sketch of the gradient function of \(f(x) = \sin x\) when

1. \(x\) is in radians?

---

1. \(x\) is in degrees?

1. Depending on the accuracy of the method used, in radians we should get gradients of approximately \(0\), \(-1\) and \(0.7\) at points A, B and C. We can use the values and the symmetry of the function \(\sin x\), to work out the gradient at some other points, before sketching a graph. What function does the sketch look like?

---

1. In degrees, the gradient at A is still zero, but is much smaller at B and C: around \(0.017\) at B, and around \(0.012\) at C. How is this gradient function similar to the function in radians? What is the link between them?

**Thinking about radians and degrees**

| Radians | Degrees |
|---|---|
|  |  |

Although it is hard to see when the \(y\) axes both have the same scale, the gradient functions both have the same features. Why must this be the case?

In radians, the gradient function looks like a \(\cos\) graph, and in fact it is. If \(f(x) = \sin x\) then \(f'(x) = \cos x\) when \(x\) is in radians. To think more about why this is true, see [Rotating derivatives](https://undergroundmathematics.org/calculus-trig-log/rotating-derivatives).

In degrees, when we enlarge the scale of the \(y\)-axis then we see the familiar shape appearing.

The gradient function of \(f(x) = \sin x\) is \(f'(x) = a\cos x\), where \(a\) is a value (quite a lot) smaller than \(1\). To think about what the value of \(a\) might be, consider how you would transform a sine graph with period of \(2\pi\) to a graph with period of \(360^{\circ}\).

It is important to reflect on the fact that the derivative of sine depends on the what unit our angles are in. We have seen that in degrees we get an additional scale factor appearing in the derivative which does not appear in radians. This is why when we do calculus with trigonometric functions we use radians and not degrees.
