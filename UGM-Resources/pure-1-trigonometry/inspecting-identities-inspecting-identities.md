---
created: 2026-10-23T16:39:11 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-compound-angles/inspecting-identities
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-compound-angles
- type/many-ways-problem
- level/developing
resource_identity:
  ugm_id: inspecting-identities
  station: trigonometry-compound-angles
  station_title: 'Trigonometry: Compound Angles'
  resource_type_id: 4
  resource_type_label: Many ways problem
  level: Developing
  ref: 8935
  old_site_id: G5_RT6_1
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
task: T-UGM-IMPORT-5
assets:
- path: https://undergroundmathematics.org/trigonometry-compound-angles/inspecting-identities/download/teacher-notes.pdf
  kind: printable
---

# Inspecting identities

> Excerpt: In this resource, students are asked to use the half-angle formulae to help them sketch graphs of  $y=\cos^2{\frac{\theta}{2}}$ and $y=\sin^{2}\frac{\theta}{2}$.

## Problem

Take a look at these identities.

\[\cos^2 \frac{\theta}{2} \equiv \frac{1}{2}(1+\cos \theta) \quad \quad \quad \sin^2 \frac{\theta}{2} \equiv \frac{1}{2}(1-\cos \theta)\]

How could you use these identities to help you sketch graphs of \(y=\cos^2 \frac{\theta}{2}\) and \(y=\sin^2 \frac{\theta}{2}\)?

The resource [Proving half-angle formulae](https://undergroundmathematics.org/trigonometry-compound-angles/proving-half-angle-formulae) looks at a way to prove these identities geometrically.

## Things you might have noticed

These ideas may help you to sketch the graphs of \(y=\cos^2 \frac{\theta}{2}\) and \(y=\sin^2 \frac{\theta}{2}\)

- As the left-hand side is a square in each case, we know the right hand sides must be zero or positive. This is fine, because \(-1\leq \cos \theta \leq 1\), so \(1+\cos \theta\) will be at least \(0\) and at most \(2\). Similarly, \(1-\cos \theta\) must be between \(0\) and \(2\).

- The right-hand sides of the identities are the same except for a minus sign, so we’d expect the behaviour of the two functions to be very similar, but the maximum and minimum values will occur at different values of \(\theta\). For example, \(\frac{1}{2}(1+\cos \theta)\) will be \(1\) when \(\theta = \dotsc ,-4\pi, -2\pi, 0, 2\pi,4\pi, \dotsc\) (i.e. at even multiples of \(\pi\)) whereas \(\frac{1}{2}(1-\cos \theta)\) will be \(1\) when \(\theta = \dotsc,-5\pi, -3\pi, -\pi, \pi, 3\pi,5\pi, \dotsc\) (i.e. at odd multiples of \(\pi\)).

- The right-hand side of each identity only involves \(\cos \theta\) and constants, so the graphs of \(y=\cos^2 \frac{\theta}{2}\) and \(y=\sin^2 \frac{\theta}{2}\) can be thought of as transformations of a \(y=\cos \theta\) graph. Which transformations are involved in each case? What is the frequency of \(y=\cos^2 \frac{\theta}{2}\) and \(y=\sin^2 \frac{\theta}{2}\)?

- Again, from the right-hand side, the identities tell us that \(\cos^2 \frac{\theta}{2}\) is the mean of \(1\) and \(\cos \theta\) and \(\sin^2 \frac{\theta}{2}\) is the mean of \(1\) and \(-\cos \theta\). What does this tell you about the graph of \(y= \cos^2 \frac{\theta}{2}\) in relation to the graphs of \(y=1\) and \(y=\cos \theta\)?

Graphs

Here are the graphs of \(y=\cos^2 \frac{\theta}{2}\) and \(y= \cos \theta\).

Here are the graphs of \(y=\sin^2 \frac{\theta}{2}\) and \(y=\cos \theta\).
