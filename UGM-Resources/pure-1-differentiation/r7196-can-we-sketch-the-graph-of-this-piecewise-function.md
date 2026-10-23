---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-meets-functions/r7196
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-meets-functions
- type/review-question
resource_identity:
  ugm_id: r7196
  station: calculus-meets-functions
  station_title: Calculus meets Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7196
  old_site_id: Q112
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-meets-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-meets-functions
    validation_status: SUGGESTED
  spec_points:
  - code: 1.7.2
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: piecewise sketch with a turning point from the quadratic piece — differentiation drives
        the labelled sketch
      rationale: 'Canonical UGM title: "Can we sketch the graph of this piecewise function?"; exam provenance:
        Oxford University Mathematics Aptitude Test, None, Q3'
      validation_status: SUGGESTED
    title: use the derivative of x (for any rational n ), together with constant multiples, sums and
      differences of functions, and of composite functions using the chain rule
  - code: 1.7.4
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: piecewise sketch with a turning point from the quadratic piece — differentiation drives
        the labelled sketch
      rationale: 'Canonical UGM title: "Can we sketch the graph of this piecewise function?"; exam provenance:
        Oxford University Mathematics Aptitude Test, None, Q3'
      validation_status: SUGGESTED
    title: locate stationary points and determine their nature, and use information about stationary
      points in sketching graphs.
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, None, Q3
task: T-UGM-IMPORT-7
---

# Can we sketch the graph of this piecewise function?

## Question

Let \[\quad f(x) = \begin{cases}x+1 & \text{for } 0 \leq x \le 1; \\ 2x^2-6x+6 & \text{for } 1 \leq x \le 2. \end{cases}\]

1. Sketch a graph of \(y=f(x)\) for \(0 \le x \le 2\), labelling any turning points and the values attained at \(x=0\), \(1\), \(2\).

---

1. For \(1 \le t \le 2\), define \[g(t) = \int_{t-1}^{t} f(x) \ dx.\] Express \(g(t)\) as a cubic in \(t\).

---

1. Calculate and factorise \(g'(t)\).

---

1. What are the minimum and maximum values of \(g(t)\) for \(t\) in the range \(1 \le t \le 2\)?

## Suggestion

Are there any turning points for \(f(x)\)?

1. For \(1 \le t \le 2\), define \[g(t) = \int_{t-1}^{t} f(x) \:dx.\] Express \(g(t)\) as a cubic in \(t\).

Can we helpfully split \(g(t)\) into two integrals?

What happens if we differentiate \(g(t)\)?

Where could \(g(t)\) attain its minimum and maximum values?

## Solution

There is no turning point in the interval \(0 \le x \le 1\). To find any turning points in the interval \(1 \le x \le 2\), we first differentiate \(f(x)\) in this interval to get \[f'(x) = 4x - 6.\] Setting \(f'(x)=0\) gives \(x=\dfrac{3}{2}\), so there is just one turning point, at \(\left(\dfrac{3}{2},\dfrac{3}{2}\right)\).

We also have \[f(0) = 1; \quad f(1) = 2; \quad f(2) = 2.\]

We could alternatively find the turning point for the quadratic section by completing the square. We have \(2x^2-6x+6= 2(x - 3/2)^2 + 3/2\).

1. For \(1 \le t \le 2\), define \[g(t) = \int_{t-1}^{t} f(x) \:dx.\] Express \(g(t)\) as a cubic in \(t\).

As

\(0 \le t-1 \le 1 \leq t\)

, we can split the integral at

\(x=1\)

. We have

\[\begin{align*} g(t) &= \int_{t-1}^{1} x+1 \:dx + \int_{1}^{t} 2x^2 - 6x + 6 \:dx \\ &= \left[\dfrac{x^2}{2}+x\right]_{t-1}^{1} + \left[\dfrac{2x^3}{3} - 3x^2 + 6x \right]_{1}^{t} \\ &= \dfrac{2t^3}{3} - \dfrac{7t^2}{2} + 6t - \dfrac{5}{3}. \end{align*}\]

Note \(\displaystyle\int_{t-1}^{1} x+1 \:dx = \left[\dfrac{x^2}{2}+x\right]_{t-1}^{1}= \left[\dfrac{(x+1)^2}{2}\right]_{t-1}^{1}\).

We have

\[\begin{align*} g'(t) &= 2t^2 - 7t + 6 \\ &= (2t-3)(t-2). \end{align*}\]

The minimum and maximum values will occur either at the end points (\(t=1\) or \(t=2\)) or at the turning points.

The turning points occur when \(g'(t)=0\), which is when \(t=\dfrac{3}{2}\) or \(t=2\).

We have

\[\begin{align*} g(1) &= \dfrac{3}{2} = \dfrac{36}{24}; \\ g\left(\dfrac{3}{2}\right) &= \dfrac{41}{24}; \\ g(2) &= \dfrac{5}{3} = \dfrac{40}{24}. \end{align*}\]

So the maximum occurs at \(t=\dfrac{3}{2}\) with value \(\dfrac{41}{24}\), and the minimum is at \(t=1\) with value \(\dfrac{3}{2}\).
