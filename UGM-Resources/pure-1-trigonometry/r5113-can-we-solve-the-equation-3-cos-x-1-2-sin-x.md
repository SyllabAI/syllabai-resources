---
created: 2026-10-23T16:39:11 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-compound-angles/r5113
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-compound-angles
- type/review-question
resource_identity:
  ugm_id: r5113
  station: trigonometry-compound-angles
  station_title: 'Trigonometry: Compound Angles'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5113
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
  exam_reference: UCLES A level Mathematics 1, QP 840/1, 1970, Q5(ii)
task: T-UGM-IMPORT-5
---

# Can we solve the equation $3\cos x + 1 = 2\sin x$?

## Question

Find the values of \(x\) between \(0^\circ\) and \(360^\circ\) which satisfy the equation

\[3\cos x + 1 = 2\sin x.\]

## Suggestion

Could we rewrite \(\sin (x-\alpha)\) in a helpful way?

How many solutions would you expect to find in the range?

Can you sketch a graph to illustrate the equation?

## Solution

We can rearrange our equation to \[2\sin x- 3\cos x = 1.\]

Now we can use the

compound angle identity

to rewrite the left hand side as

\[2\sin x- 3\cos x = R\sin(x-\alpha) = R\sin x\cos\alpha - R\cos x\sin\alpha\]

and matching the coefficients tells us we need

\(R\)

and

\(\alpha\)

such that

\[R\cos\alpha=2 \quad\text{and}\quad R\sin\alpha=3.\]

This reduces to

\[\begin{align*} R^2=13 \quad&\text{and}\quad \tan\alpha=\frac{3}{2} \\ \implies\quad R=\sqrt{13} \quad&\text{and}\quad \alpha=56.3^\circ (1 \text{d.p.}) \end{align*}\]

So now our original equation becomes \[\sin(x-56.3^\circ)=\frac{1}{\sqrt{13}}.\]

The general solution to this is \[x=\arcsin\frac{1}{\sqrt{13}}+56.3^\circ \quad\text{or}\quad x=180^\circ - \arcsin\frac{1}{\sqrt{13}}+56.3^\circ\] plus an integer multiple of \(360^\circ\).

Within the required range this gives us \[x=72.4^\circ\quad\text{or}\quad 220.2^\circ (1 \text{d.p.}).\]

Check – if we have access to a graphing program, we can see where the graphs of \(y = 3\cos x + 1\) and \(y = 2\sin x\) intersect.
