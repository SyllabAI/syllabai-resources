---
created: 2026-10-23T16:39:11 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-compound-angles/r5723
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-compound-angles
- type/review-question
resource_identity:
  ugm_id: r5723
  station: trigonometry-compound-angles
  station_title: 'Trigonometry: Compound Angles'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5723
  old_site_id: Q3009
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
  exam_reference: UCLES AO level Additional Mathematics 2, QP 8175/2, 1983, Q14
task: T-UGM-IMPORT-5
---

# Can we solve these trig equations for $x, y$ and $z$?

## Question

Find all the angles between \(0^\circ\) and \(180^\circ\) which satisfy the equations

1. \(\tan (x + 60^\circ) = 1\),

---

1. \(8 \sin y + 3 \sec y = 0\),

---

1. \(3 \sin^2 z - 8 \sin z \cos z - 3 \cos^2 z = 0\).

## Solution

Let’s find the general solution. We know that \(\arctan{1} = 45 ^\circ\), so \[x+60=45+180n \implies x = -15 + 180n.\]

Recall that the function \(\tan x\) is periodic with period \(180^\circ\).

Thus the only solution in our range is \(165^\circ\).

By definition,

\(\sec\)

is the reciprocal of

\(\cos\)

. By multiplying through by

\(\cos y\)

and rearranging, we have

\[\begin{equation}\label{eq:pt-2-equiv-form-1} 8 \cos y \sin y = -3. \end{equation}\]

Note \(\cos y \neq 0\), since then \(\sec y\) would be undefined.

Now \(2\sin y\cos y = \sin(2y)\), and so on rearranging, our equation becomes \[\sin(2y) = -\frac{3}{4}.\]

So the general solution here is \(2y = -48.6 + 360n\), or \(228.6+360n\).

This is since \(228.6 = 180 - (-48.6)\).

This implies \(y = -24.3 + 180n\), or \(114.3 + 180n\), and so the solutions in our range are \(114.3^\circ\) and \(155.7^\circ\).

Could \(\cos z\) be \(0\) here? This would mean that for the equation to hold, \(\sin z = 0\). But \(\cos z\) and \(\sin z\) are never zero together, so \(\cos z\) cannot be zero if the equation holds.

So we can divide the equation by \(\cos^2 z\), giving us \(3 \tan^2 z - 8 \tan z - 3 = 0\), which becomes \((3\tan z + 1)(\tan z -3) = 0\).

So \(\tan z = -\dfrac{1}{3}\) or \(\tan z = 3\), and \(z = -18.4 + 180n\) or \(71.6 + 180n\).

Thus the two solutions in our range are \(71.6^\circ\) and \(161.6^\circ\).

Alternatively, we could factorise the original expression, \[3 \sin^2 z - 8 \sin z \cos z - 3 \cos^2 z =(3\sin z+\cos z)(\sin z-3\cos z)\] with the same result.
