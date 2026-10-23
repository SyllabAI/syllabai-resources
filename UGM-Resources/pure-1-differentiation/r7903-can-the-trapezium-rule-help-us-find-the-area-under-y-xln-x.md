---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/introducing-calculus/r7903
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- introducing-calculus
- type/review-question
resource_identity:
  ugm_id: r7903
  station: introducing-calculus
  station_title: Introducing Calculus
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7903
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: introducing-calculus
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: introducing-calculus
    validation_status: SUGGESTED
  spec_points: []
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md
    rule 3: coverage is never manufactured)'
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Further Mathematics 1, 1973, Q6
task: T-UGM-IMPORT-7
---

# Can the trapezium rule help us find the area under $y = x\ln x$?

## Question

The continuous function

\(f\)

maps the real interval

\[\begin{equation*} a \le x \le b \end{equation*}\]

into a subset of the positive real numbers. Derive the trapezium rule for the approximate evaluation of the area under the curve \(y = f(x)\) between \(x=a\) and \(x=b\), using \((n-1)\) points of subdivision at a distance \(h = (b-a)/n\) apart.

Hence obtain an approximation to the integral

\[\begin{equation*} I = \int_3^5 x \ln x \:dx \end{equation*}\]

using the points of subdivision given in the following table:

| \(x\) | \(3.0\) | \(3.5\) | \(4.0\) | \(4.5\) | \(5.0\) |
|---|---|---|---|---|---|
| \(x \ln x\) | \(3.296\) | \(4.385\) | \(5.545\) | \(6.768\) | \(8.047\) |

## Solution

Consider the following diagram.

In this diagram, we start with the graph of \(y = f(x)\) between \(x=a\) and \(x=b\). This is shown in black. Our goal is to approximate the area under this curve; this is the region in blue (and purple, where it overlaps with the red region).

We then fix an integer \(n\), define \(h = (b-a)/n\), and divide the interval \(a \le x \le b\) into \(n\) equal parts (of length \(h\)) by marking the points at \(a+h\), \(a+2h\), and so on. We then draw line segments between \((a,f(a))\) and \((a+h,f(a+h))\); between \((a+h,f(a+h))\) and \((a+2h,f(a+2h))\); and so on. This is the (piecewise linear) curve in dark red.

The trapezium rule says that the area under the red curve (the region in light red; this is a sequence of trapezia) is approximately the same as the area under the original graph, with the approximation becoming more exact as

\(n\)

increases. We will write this symbolically:

\[\begin{align*} &\text{area of the first trapezium} + \text{area of the second trapezium} + \dotsb + \text{area of the last trapezium}\\ &= \frac{f(a) + f(a+h)}{2} h + \frac{f(a+h) + f(a+2h)}{2} h + \dotsb + \frac{f(b-h) + f(b)}{2} h \\ &= \frac{h}{2} \left( f(a) + 2f(a+h) + 2f(a+2h) + \dotsb + 2f(b-h)+ f(b) \right) \\ &\approx \int_a^b f(x) \:dx. \end{align*}\]

In the above,

\(a = 3\)

,

\(b = 5\)

,

\(f(x) = x \ln x\)

, and

\(h = 0.5\)

. Hence,

\[\begin{align*} \int_3^5 x \ln x \:dx &\approx \frac{0.5}{2} \left( f(3) + 2f(3.5) + 2f(4) + 2f(4.5) + f(5) \right) \\ &= \frac{1}{4} \left( 3.296 + 2 \times 4.385 + 2 \times 5.545 + 2 \times 6.768 + 8.047 \right) \\ &= 11.18475\\ &= 11.2 \quad\text{to $3$ s.f.} \end{align*}\]

We can, in fact, integrate \(x \ln x\) exactly using [integration by parts](https://undergroundmathematics.org/glossary/integration-by-parts). We find \(\int_3^5 x \ln x \:dx = 11.17421860\!\ldots\), so the above approximation is not bad.
