---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/introducing-calculus/r8140
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- introducing-calculus
- type/review-question
resource_identity:
  ugm_id: r8140
  station: introducing-calculus
  station_title: Introducing Calculus
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8140
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
  exam_reference: Oxford University Mathematics Aptitude Test, 2015, Q1F
task: T-UGM-IMPORT-7
---

# Can we apply the trapezium rule to $f(x) = x/2 - \lfloor x/2 \rfloor$?

## Question

For a real number \(x\), we denote by \(\lfloor x \rfloor\) the largest integer less than or equal to \(x\). Let

\[f(x) =\dfrac{x}{2}-\left\lfloor \dfrac{x}{2} \right\rfloor.\]

The smallest number of equal width strips for which the trapezium rule produces an *overestimate* for the integral

\[\int_0^5 f(x) \:dx\]

is

(a) \(2,\quad\) (b) \(3,\quad\) (c) \(4,\quad\) (d) \(5,\quad\) (e) it never produces an overestimate.

## Suggestion

Can we sketch the curve?

Can we add to our sketch what happens if we apply the trapezium rule with 2 strips? With 3? With more?

## Solution

If we sketch the graph for \(0 \leq x \leq 5\), we find that it takes a saw-tooth shape.

It’s easy to calculate the integral; it is the area of the three triangles shown, which is \(\dfrac{9}{4}\).

What happens if we apply the trapezium rule with two strips?

The trapezium rule returns the area of the blue triangle, which is \(\dfrac{5}{4} < \dfrac{9}{4}\), an underestimate.

What happens with three strips?

By the trapezium rule, the shaded area now is \(\dfrac{1}{2}\times\dfrac{5}{3}\left[0+\dfrac{1}{2}+2\left(\dfrac{5}{6}+ \dfrac{2}{3}\right)\right] = \dfrac{105}{36}> \dfrac{9}{4}\), and so the answer is (b).

If we apply the trapezium rule with \(5n\) strips, where \(n\) is a positive integer, the result agrees exactly with the given integral.
