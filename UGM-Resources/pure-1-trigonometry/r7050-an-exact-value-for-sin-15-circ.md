---
created: 2026-10-23T16:39:11 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-compound-angles/r7050
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-compound-angles
- type/review-question
resource_identity:
  ugm_id: r7050
  station: trigonometry-compound-angles
  station_title: 'Trigonometry: Compound Angles'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7050
  old_site_id: Q209
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
  exam_reference: Cambridge Colleges Examination for Entrance Scholarships and Exhibitions, Pure Mathematics
    for Candidates in Natural Sciences (Group 4), 1952, Q3
task: T-UGM-IMPORT-5
---

# An exact value for $\sin 15^{\circ}$...

## Question

1. Without using tables, show for \(\theta=15^\circ\) that \(\sin\theta=\dfrac{\sqrt{6}-\sqrt{2}}{4}\), and find the values of \(\cos\theta\) and \(\tan\theta\).

---

1. In the triangle \(ABC\), \(B\) is a right angle and the other angles are such that if a point \(E\) on \(BC\) and between \(B\) and \(C\) is chosen so that \(BE=BA\), then there is a point \(D\) on \(AC\) and between \(A\) and \(C\) such that \(AD=DE=EC\). Find the ratio of \(DC\) to \(AB\).

## Suggestion

For what angles do we know the exact values of \(\sin\theta\)?

What trigonometric formulae might be useful here? How about expanding \(\sin(a-b)\), choosing \(a\) and \(b\) carefully?

## Solution

We will use the identity

\(\sin(x-y) = \sin x \cos y - \sin y \cos x\)

. We have that

\[\begin{align*} \sin 15^\circ=\sin(45-30)^\circ &=\sin45^\circ\cos30^\circ-\cos45^\circ\sin30^\circ \\ &=\frac{1}{\sqrt{2}}\frac{\sqrt{3}}{2}-\frac{1}{\sqrt{2}}\frac{1}{2} \\ &=\frac{\sqrt{2}\sqrt{3}}{2\times 2}-\frac{\sqrt{2}}{2\times 2} \\ &=\frac{\sqrt{6}-\sqrt{2}}{4}. \end{align*}\]

We now have

\[\begin{align*} \cos^2 15^\circ=1-\sin^2 15^\circ &=1-\frac{6+2-2\sqrt{6}\sqrt{2}}{16} \\ &=\frac{8+2\sqrt{12}}{16}\\ &=\frac{6+2+2\sqrt{2}\sqrt{6}}{16} \\ &=\frac{(\sqrt{6}+\sqrt{2})^2}{4^2}, \end{align*}\]

and so, since \(\cos \theta\) is positive between \(0^\circ\) and \(90^\circ\), \[\cos 15^\circ=\frac{\sqrt{6}+\sqrt{2}}{4}.\]

Finally, we have

\[\begin{align*} \tan 15^\circ=\frac{\sin15^\circ}{\cos15^\circ} &=\frac{\sqrt{6}-\sqrt{2}}{\sqrt{6}+\sqrt{2}} \\ &=\frac{(\sqrt{6}-\sqrt{2})^2}{(\sqrt{6}+\sqrt{2})(\sqrt{6}-\sqrt{2})} \\ &=\frac{6+2-2\sqrt{2}\sqrt{6}}{6-2} \\ &=\frac{8-2\sqrt{12}}{4} \\ &=2-\sqrt{3}. \end{align*}\]

First let’s draw what’s happening, filling in the angles by putting in \(a\) for \(ACB\) and \(b\) for \(CAE\).

The angle-sum in triangle \(ABC\) tells us that \(a+b = 45^\circ\). The angle at \(D\) tells us that \(a = 2b\). Solving these equations simultaneously gives \(b = 15^\circ, a = 30^\circ\).

We need the ratio of \(DC\) to \(AB\). Without loss of generality we can put \(CE = 1\), so \(CD = 2 \cos 30^\circ\) and \(EA = 2\cos 15^\circ\).

Now, by Pythagoras, \(AB = \dfrac{2\cos 15^\circ}{\sqrt{2}}\).

Thus

\[\begin{align*} DC:AB &= 2\cos 30^\circ: \dfrac{2\cos 15^\circ}{\sqrt{2}}\\ &= \sqrt{3} : \sqrt{2}\frac{\sqrt{6}+\sqrt{2}}{4} \\ &= 4\sqrt{3} : \sqrt{12}+2 \\ &=2\sqrt{3} : \sqrt{3}+1. \end{align*}\]
