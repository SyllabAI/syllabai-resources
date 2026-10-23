---
created: 2026-10-23T16:39:11 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-compound-angles/r6120
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-compound-angles
- type/review-question
resource_identity:
  ugm_id: r6120
  station: trigonometry-compound-angles
  station_title: 'Trigonometry: Compound Angles'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6120
  old_site_id: Q38
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
  exam_reference: UCLES A level Mathematics 1, QP 182, 1952, Q8
task: T-UGM-IMPORT-5
---

# Can we write $\cos \theta - 2 \cos 3 \theta + \cos 5\theta$ using $\sin$?

## Question

1. Prove the identity \[\cos \theta - 2 \cos 3 \theta + \cos 5\theta = 2\sin \theta (\sin 2 \theta - \sin 4 \theta).\]

---

1. Solve the equations  \(\cos 2x = \sin x\), \(3 \sec^2 x = \tan x + 5\)  giving in each case all solutions between \(0^\circ\) and \(360^\circ\).

## Suggestion

Can we combine two \(\cos\) terms using an expression for the difference of two cosines?

We could use this twice here…

Can we write the first equation just in terms of \(\sin x\)?

How can we relate \(\sec^2 x\) to \(\tan x\)?

This would reduce the equations to quadratic ones…

## Solution

We can always write the expressions \(\cos A + \cos B, \cos A - \cos B, \sin A + \sin B\), and \(\sin A - \sin B\) as the product of two \(\sin / \cos\) terms.

This can be immensely useful to us in lots of situations. Here we are interested in \(\cos A - \cos B\).

We begin with \[\cos(X + Y) = \cos X \cos Y - \sin X \sin Y \quad \text{and} \quad \cos(X - Y) = \cos X \cos Y + \sin X \sin Y.\] Adding these equations gives \[\cos (X-Y) - \cos (X+Y) = 2\sin X \sin Y.\] Now setting \(A=X-Y, B=X+Y\) we find \[\cos A - \cos B = 2 \sin \frac{A+B}2 \sin \frac{B-A}2.\]

Applying this to both \(\cos\theta - \cos 3\theta\) and \(\cos 5 \theta - \cos 3\theta\), we see the left-hand side (LHS) is equal to \[2 \sin 2\theta \sin \theta + 2 \sin 4\theta \sin (-2\theta) = 2 \sin \theta(\sin 2\theta - \sin 4 \theta),\] as required.

Alternatively, we can show by expanding that if \(c = \cos\theta, s = \sin\theta\), then \[\cos(3\theta) = 4c^3-3c, \quad \cos(5\theta) = 16c^5-20c^3+5c, \quad \sin(2\theta) = 2sc, \quad \sin(4\theta) = 8sc^3-4sc.\]

Now the LHS is \[c - 2(4c^3-3c)+ 16c^5-20c^3+5c=16c^5-28c^3+12c,\] while the RHS is \[2s(2sc-(8sc^3-4sc)) = 2(1-c^2)(-8c^3+6c) = 16c^5-28c^3+12c,\] which are the same, and so we are done.

1. For the first equation, we use one of the double angle formulae for \(\cos\), that’s \(\cos 2x = 1 - 2\sin^2 x\).

Now everything’s written in terms of \(\sin x\), which makes the equation much simpler.

Writing \(u=\sin x\), we have to solve the equation \(\cos 2x = \sin x,\) which gives \[1 - 2u^2 = u, \quad \text{ or} \quad 2u^2+u-1=0, \quad \text{ or} \quad (2u-1)(u+1)=0,\]
 with solutions \[\sin x = u = \frac{1}{2}, -1.\]

We need all solutions between \(0^\circ\) and \(360^\circ\). These are \[x = 30^\circ, 150^\circ, 270^\circ.\]

It’s helpful to sketch a graph, to check we’ve got all the solutions.

1. For the second, recall the identity \(\tan^2 x + 1 = \sec^2 x\) (given by dividing \(\sin^2 x + \cos^2 x = 1\) by \(\cos^2 x\)).

Define \(v = \tan x\), so we need to solve

\[3 \sec^2 x = \tan x + 5, \quad \text{ or} \quad 3(1+v^2)-v-5=0, \quad \text{ or} \quad 3v^2 -v -2=0.\] This is \((3v+2)(v-1)=0\), so \(v = -\frac {2}{3}, 1\), which (since \(\tan x\) has period \(\pi\)) gives the four solutions \[x = 45^\circ, 225^\circ, 146.3^\circ, 326.3^\circ.\]
