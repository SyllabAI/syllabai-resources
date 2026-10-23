---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/introducing-calculus/r7250
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- introducing-calculus
- type/review-question
resource_identity:
  ugm_id: r7250
  station: introducing-calculus
  station_title: Introducing Calculus
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7250
  old_site_id: Q4015
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
  exam_reference: UCLES O level Mathematics Syllabus D Paper 1, 1982, Q29
task: T-UGM-IMPORT-7
---

# Can we calculate the total time taken for this car journey?

## Question

The diagram shows a speed-time graph of a car.

1. Calculate the acceleration of the car during the first \(20\) seconds.

---

1. Calculate the distance the car travels from rest before it begins to decelerate.

---

1. Given that the car decelerates at \(\quantity{0.5} {m/s^2}\), calculate the total time taken for the journey.

## Suggestion

The diagram shows a speed-time graph of a car.

Which part of the above graph represents the acceleration of the car?

How is the distance the car travels represented?

Can we find the equations of the straight line parts of the graph?

How can you use this to compute the total time taken for the journey?

## Solution

The acceleration at any point is given by the gradient of the line, so the acceleration is constant on each section.

The gradient for the first section is \(\dfrac{15}{20}=0.75\), and so the acceleration of the car during the first \(20\) seconds is \(\quantity{0.75} {m/s^2}\).

The distance the car travels is given by the area below the graph up to \(t = 70s\).

We’ll split this area into two pieces, the left hand side triangle (the distance the car travels during the first 20 seconds), and the rectangle for \(20s \leq t \leq 70s\).

The base of the triangle is \(20\) and the height is \(15\), and so the area of the triangle is given by \(\dfrac{20 \times 15}{2} = 150\).

The rectangle has sides of lengths \(15\) and \(70-20 = 50\) and so has an area of \(15 \times 50 = 750.\)

Therefore, the total distance the car travels before it begins to decelerate is \(150 + 750 = \quantity{900}{m}\).

We’ll describe the deceleration of the car as a linear function, or the equation of a straight line, and then compute the \(t\)-intercept.

The general form for a linear function is \(y = ax + b\), where \(a\) is the slope of the function and \(b\) is the \(y\)-intercept.

We already know that the gradient of the graph is \(-0.5\), so the function is of the form \[y = -0.5x + b.\]

The graph passes through the point \((70, 15)\), so the function has to satisfy \(15 = -0.5 \times 70 + b\), which yields \(b = 50\).

The function describing the graph for \(t \geq 70\) is therefore given by \[v = -0.5t + 50.\]

The \(t\)-intercept is the solution to \(0 = -0.5t + 50\), which gives \(t = 100\). Therefore, the total time taken for the journey is \(\quantity{100}{s}\).
