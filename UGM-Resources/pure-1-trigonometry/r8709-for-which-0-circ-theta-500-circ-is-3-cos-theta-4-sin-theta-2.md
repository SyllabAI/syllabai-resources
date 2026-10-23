---
created: 2026-10-23T16:39:11 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-compound-angles/r8709
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-compound-angles
- type/review-question
resource_identity:
  ugm_id: r8709
  station: trigonometry-compound-angles
  station_title: 'Trigonometry: Compound Angles'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8709
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: trigonometry-compound-angles
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: trigonometry-compound-angles
    validation_status: SUGGESTED
  spec_points: []
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md rule
    3: coverage is never manufactured)'
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: O&C O level SMP Additional Mathematics 2, QP SMP 118, 1975, Q4
task: T-UGM-IMPORT-5
---

# For which $0^\circ < \theta < 500^\circ$ is $3\cos \theta + 4\sin \theta > 2$?

## Question

\(3\cos \theta + 4\sin \theta\) may be written in the form \(r\cos(\theta - \alpha)\), where \(r > 0\).

1. Calculate the value of \(r\), and show that one value of \(\alpha\) is approximately \(53.1^\circ\).

---

1. Hence show that one solution of \(3\cos \theta + 4\sin \theta = 2\) is approximately \(120^\circ\).

---

1. State all the other solutions for \(0^\circ \leq \theta \leq 500^\circ.\)

---

1. Hence give the positive values of \(\theta\) less than \(500^\circ\) for which \(3\cos \theta + 4\sin \theta > 2\).

## Suggestion

Can we expand the expression \(\cos(\theta - \alpha)\)?

Can we use the result from part (a)?

How many solutions do you expect in the interval \(0\leq\theta<360^\circ\)?

How can we locate further solutions?

A sketch graph of \(y = 3\cos \theta + 4\sin \theta\) might be helpful. What happens at each of the solutions found in part (c)?

## Solution

We have the compound angle identity, \[\cos (\theta -\alpha) = \cos\theta\cos\alpha+\sin\theta\sin\alpha.\]

Thus \[r\cos (\theta -\alpha) = (r\cos\alpha)\cos\theta+(r\sin\alpha)\sin\theta.\]

Comparing this with \(3\cos \theta + 4\sin \theta\) gives us that \[r\cos\alpha = 3, r\sin\alpha = 4.\]

Squaring and adding these two equations gives us that \(r^2 = 25\), so \(r = 5\).

Dividing the two equations gives us that \(\tan \alpha = \dfrac{4}{3}\), and one solution of this is \(\alpha \approx 53.1^\circ\).

Using the results above, we can write the equation as \(5\cos(\theta - 53.1^\circ) = 2.\) Two of the solutions to this are \[\theta - 53.1^\circ = \cos^{-1} 0.4 \quad\implies\quad \theta \approx 119.5^\circ\] and \[\theta - 53.1^\circ = -\cos^{-1} 0.4 \quad\implies\quad \theta \approx -13.3^\circ.\]

Thus \(120^\circ\) is an approximate solution to the equation.

As well as the above solutions, we can find others by adding integer multiples of \(360^\circ\). We find that \(119.5^\circ\), \(346.7^\circ\) and \(479.5^\circ\) are all the solutions within the given range.

A graph of the function \(y=3\cos \theta + 4\sin \theta\) looks like this.

Note that the function switches between being above and below \(y=2\) at each of the intersections found in part (c). When \(\theta = 0\), the function is greater than \(2\).

This must mean that \(3\cos \theta + 4\sin \theta > 2\) on the intervals \(0 < \theta < 119.5^\circ\) and \(346.7^\circ < \theta < 479.5^\circ\).
