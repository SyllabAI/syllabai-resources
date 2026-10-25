---
created: 2026-10-25T19:03:34 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-trig-log/r7616
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-trig-log
- type/review-question
resource_identity:
  ugm_id: r7616
  station: calculus-trig-log
  station_title: "Calculus of Trigonometry & Logarithms"
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7616
  old_site_id: "Q166"
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
  - code: 3.3.1
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-11 cross-map (cross-map-p3-trigonometry.json (P3c lane 11) @ syllabai-experimental 4dbd50d5)"
      evidence: "the sign of (\u222bcos)(\u222bsin over [\u03c0,2\u03c0])(\u222bdx/cos3x over [0,\u03c0/8]) decided from the properties of the six functions: sin negative on [\u03c0,2\u03c0] and 1/cos3x positive and finite on the range (cos3x\u2265cos(3\u03c0/8)>0) - properties and graphs for angles of any magnitude, no computation needed"
      rationale: "Canonical UGM title: Is this product of integrals positive or negative?"
      validation_status: SUGGESTED
    title: "understand the relationship of the secant, cosecant and cotangent functions to cosine, sine and tangent, and use properties and graphs of all six trigonometric functions for angles of any magnitude"
  mapped_date: '2026-10-25'
  mapper: cross-map-p3-trigonometry.json (P3c lane 11) @ syllabai-experimental 4dbd50d5
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-11
---

# Is this product of integrals positive or negative?

## Question

Let \[T=\left( \int _{-\pi/2}^{\pi/2}\cos x\,dx\right)\times \left(\int_\pi ^{2\pi} \sin x\,dx\right) \times \left(\int_0^{\pi/8}\frac{dx}{\cos 3x}\right).\] Which of the following is true?

1. \(T=0\);

---

1. \(T<0\);

---

1. \(T>0\);

---

1. \(T\) is not defined.

## Suggestion

Note that the third integral, \(\displaystyle \int_0^{\pi/8}\frac{dx}{\cos 3x}\), means the same as \[\int_0^{\pi/8}\frac{1}{\cos 3x}\,dx.\]

Do we need to work out the exact values of each of the integrals? What is the important thing to know?

## Solution

Let \[T=\left( \int _{-\pi/2}^{\pi/2}\cos x\,dx\right)\times\left(\int_\pi ^{2\pi} \sin x\,dx\right) \times\left(\int_0^{\pi/8}\frac{dx}{\cos 3x}\right).\] Which of the following is true?

1. \(T=0\);

---

1. \(T<0\);

---

1. \(T>0\);

---

1. \(T\) is not defined.

We are not asked to work out the exact value of \(T\), only to determine whether it is positive, negative or zero (if it is defined).

*It might not be defined if there is a vertical asymptote in the region where we are integrating. We note that \(\dfrac{1}{\cos 3x}\) can be infinite for some values of \(x\).*

So we only need to determine the sign for each of the three integrals involved in the product.

Consider the first integral, \[\int_{-\pi/2}^{\pi/2}\cos x\,dx.\] The graph of \(y=\cos x\) looks like this:

So the integral from \(x=-\pi/2\) to \(x=\pi/2\) is positive, as the graph all lies above the \(x\)-axis in this range.

Then for the second, \[\int_\pi^{2\pi}\sin x\,dx.\] The graph of \(y=\sin x\) looks like this:

Between \(x=\pi\) and \(x=2\pi\), this graph lies entirely below the \(x\)-axis, so this integral is negative.

For the third integral, \[\int_0^{\pi/8}\frac{dx}{\cos 3x}\] we will need to consider the graph of \(y=\cos 3x\), which is the graph of \(y=\cos x\) stretched by a scale factor of \(\frac{1}{3}\) in the \(x\)-direction.

*Now \(\frac{1}{\cos 3x}\) is infinite at \(x=\pi/6\), but \(x=\pi/8<\pi/6\), and so there are no vertical asymptotes in the region where we are integrating.*

This graph is positive between \(x=0\) and \(x=\pi/8\), so between \(x=0\) and \(x=\pi/8<\pi/6\), we see that \(\dfrac{1}{\cos 3x}\) is positive. Thus this third integral is positive.

Finally, we can combine the three integrals. Since two of them are positive and one is negative, their product must be negative.

The answer is therefore (b), \(T<0\).
