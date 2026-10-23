---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/r9905
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/review-question
resource_identity:
  ugm_id: r9905
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9905
  old_site_id: null
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
  - code: 1.7.2
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: pyramid frame maximum volume — V^2 differentiable as a polynomial avoiding the product
        rule; stationary-point nature checked
      rationale: 'Canonical UGM title: "When is the volume of this pyramid a maximum?"; exam provenance:
        UCLES A level Pure Mathematics Special paper, 1980, Q9'
      validation_status: SUGGESTED
    title: use the derivative of x (for any rational n ), together with constant multiples, sums and
      differences of functions, and of composite functions using the chain rule
  - code: 1.7.4
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: pyramid frame maximum volume — V^2 differentiable as a polynomial avoiding the product
        rule; stationary-point nature checked
      rationale: 'Canonical UGM title: "When is the volume of this pyramid a maximum?"; exam provenance:
        UCLES A level Pure Mathematics Special paper, 1980, Q9'
      validation_status: SUGGESTED
    title: locate stationary points and determine their nature, and use information about stationary
      points in sketching graphs.
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Pure Mathematics Special paper, 1980, Q9
task: T-UGM-IMPORT-7
---

# When is the volume of this pyramid a maximum?

## Question

A right square pyramidal frame is formed from a rod of length \(4a\) by dividing the rod into eight pieces, four being of length \(x\) (to make the edges of the square base) and the other four of length \(a - x\) (to make the sloping edges). The rods are jointed together without wastage. If the volume of the pyramid is \(V\), and \(x\) may vary, show that \(\dfrac{dV}{dx} = 0\) when \(x = 0\) and when \[3x^2 - 10ax + 4a^2 = 0.\]

Show that, when \(x\) is equal to the smaller of the two roots of this equation,

1. a real pyramid can be formed,

---

1. \(V\) has a maximum value.

## Solution

The volume \(V\) of a right square pyramid is given by the equation \[V = \frac{1}{3} \times \text{area of the base} \times \text{height}.\] As the square base comprises four rods, each of length \(x\), the area of the base is \(x^2\). For the height, consider the following image.

We wish to calculate

\(h\)

. By

Pythagoras’s theorem

, we have

\[\begin{align*} h^2 + \left( \frac{x}{\sqrt{2}} \right)^2 = (a - x)^2 &\implies h^2 = a^2 - 2ax + x^2 - \frac{x^2}{2} \\ &\implies h = \sqrt{a^2 - 2ax + \frac{x^2}{2}}. \end{align*}\]

Thus, we have that

\[\begin{align*} V &= \frac{1}{3} \times x^2 \times \sqrt{a^2 - 2ax + \frac{x^2}{2}} \\ &= \frac{1}{3} \sqrt{ a^2x^4 - 2ax^5 + \frac{x^6}{2} }. \end{align*}\]

By the

chain rule

,

\[\begin{align*} \frac{dV}{dx} &= \frac{1}{6} \left( a^2x^4 - 2ax^5 + \frac{x^6}{2} \right)^{-1/2} \times \left( 4a^2 x^3 - 10ax^4 + 3x^5 \right) \\ &= \frac{x^3(3x^2 - 10ax + 4a^2)}{6\sqrt{a^2x^4 - 2ax^5 + \frac{x^6}{2}}} \\ &= \frac{x(3x^2 - 10ax + 4a^2)}{6\sqrt{a^2 - 2ax + \frac{x^2}{2}}}. \end{align*}\]

So we can see that, \(\dfrac{dV}{dx} = 0\) when \(x = 0\) or \(3x^2 - 10ax + 4a^2 = 0\).

Strictly, we should be concerned about the cases when the denominator is close to zero because then our expression is ill-defined. But note that \(\sqrt{a^2 - 2ax + \frac{x^2}{2}}\) is the height of the pyramid, and as this approaches zero the volume will be changing rapidly so we can be sure that \(\dfrac{dV}{dx} \neq 0\) at this point.

From the [quadratic formula](https://undergroundmathematics.org/glossary/quadratic-equation-solution), \[3x^2 - 10ax + 4a^2 = 0 \iff x = \frac{10a \pm \sqrt{100a^2 - 48a^2}}{6} = \frac{10 \pm \sqrt{52}}{6} a = \frac{5 \pm \sqrt{13}}{3} a.\]

The smaller of these roots is \(x=\dfrac{5 - \sqrt{13}}{3} a\).

In order to form a real pyramid, \(x\) must be between \(0\) and \(a\). Also, the sloping diagonal, \(a-x\), must be longer than the semi-diagonal of the base, \(\dfrac{x}{\sqrt{2}}\).

Since

\(5>\sqrt{13}\)

, we know that

\(x\)

is positive. We also require

\[\begin{align*} a-x &> \frac{x}{\sqrt{2}} \\ \iff\quad x\left(1+\frac{1}{\sqrt{2}}\right) &< a \\ \iff\quad x &< \left(2-\sqrt{2}\right)a \end{align*}\]

Comparing these surd expressions directly is tricky, so let’s use a calculator to check. \[\dfrac{5 - \sqrt{13}}{3} \approx 0.465 \quad\text{and}\quad 2-\sqrt{2} \approx 0.586\] so the diagonal condition is satisfied and we do have a real pyramid.

As \(x \to 0\), the square base goes to a point and the volume of the pyramid shrinks to zero.

As \(x \to \left(2-\sqrt{2}\right)a\), the sloping diagonal becomes the same length as the semi-diagonal of the base. The height and therefore the volume of the pyramid shrinks to zero.

In between these values, a real pyramid exists and \(V\) is positive.

We know that in this range, we have a single stationary point, which must therefore be a maximum.

Another way to check that the volume is maximised at this value is to compute the second derivative, and to verify that it is negative at this value, but this would be demanding…

Note that the question doesn’t ask us to calculate the maximum value of \(V\) in terms of \(a\), but it’s not hard to do with a calculator – we find \(V_{max} \approx 0.0304a^3\).

Graph of \(V\) against \(x\) for the case \(a=1\)
