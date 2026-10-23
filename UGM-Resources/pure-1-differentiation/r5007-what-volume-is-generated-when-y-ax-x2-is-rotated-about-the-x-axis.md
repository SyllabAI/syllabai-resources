---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/r5007
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/review-question
resource_identity:
  ugm_id: r5007
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5007
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-of-powers
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-of-powers
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
  exam_reference: O&C O level Additional Mathematics 2, 1972, Q8
task: T-UGM-IMPORT-7
---

# What volume is generated when $y = ax - x^2$ is rotated about the x-axis?

## Question

The curve \(y = ax - x^2\) cuts the \(x\)-axis at the points \((0,0)\) and \((a,0)\). The area enclosed between the curve and the \(x\)-axis is \(36\) square units. Calculate the value of \(a\).

With this value of \(a\) find, as a multiple of \(\pi\), the volume obtained when the above area is rotated through \(4\) right angles about the \(x\)-axis.

## Solution

From what is given in the question, the area enclosed between the curve and the

\(x\)

-axis is

\[\begin{equation*} 36 = \int_0^a ax - x^2 \:dx = \left[ \frac{ax^2}{2} - \frac{x^3}{3} \right]_0^a = \frac{a^3}{2} - \frac{a^3}{3} = \frac{a^3}{6}. \end{equation*}\]

Thus, \(a^3 = 216\) and so \(a = 6\).

If we have a curve

\(y = f(x)\)

with

\(p \le x \le q\)

and

\(f(x) \ge 0\)

, then the volume enclosed by the surface of revolution obtained by rotating the curve around the

\(x\)

-axis is given by

\[\begin{equation*} \int_{p}^{q} \pi f(x)^2 \:dx. \end{equation*}\]

How does this arise? We can approximate the enclosed solid with a series of cylinders of thickness

\(\delta x\)

(corresponding to a small increase in

\(x\)

) and radius

\(f(x)\)

(corresponding to the height of the function). The volume of the approximation is

\[\begin{equation*} \sum \pi f(x)^2 \delta x \xrightarrow{\delta x \to 0} \int_{p}^{q} \pi f(x)^2 \:dx. \end{equation*}\]

In our case, then, the volume required is

\[\begin{align*} \int_0^6 \pi \left( 6x - x^2 \right)^2 \:dx &= \pi \int_0^6 x^2 (6-x)^2 \:dx \\ &= \pi \int_0^6 x^2 (36 - 12x + x^2) \:dx \\ &= \pi \int_0^6 36x^2 - 12x^3 + x^4 \:dx \\ &= \pi \left[ 12x^3 - 3x^4 + \frac{x^5}{5} \right]_0^6 \\ &= \pi \left( 12 \times 6^3 - 3 \times 6^4 + \frac{6^5}{5} \right) \\ &= \pi \left( \left( 2 - 3 + \frac{6}{5} \right) 6^4 \right) \\ &= \frac{6^4}{5} \pi \\ &= \frac{1296}{5} \pi. \end{align*}\]
