---
created: 2026-10-23T16:39:11 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-compound-angles/r6039
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-compound-angles
- type/review-question
resource_identity:
  ugm_id: r6039
  station: trigonometry-compound-angles
  station_title: 'Trigonometry: Compound Angles'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6039
  old_site_id: Q56
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
  exam_reference: UCLES A level Mathematics Scholarship paper, QP 186, 1953, Q3
task: T-UGM-IMPORT-5
---

# Can we solve $\tan\theta\tan(\theta+\pi/3)=2$?

## Question

Prove that, if \(\tan\theta\tan(\theta+\alpha)=k\), then \[(k+1)\cos(2\theta+\alpha)=(1-k)\cos\alpha.\]

Solve the equation \[\tan\theta\tan(\theta+\pi/3)=2.\]

Discuss the equation \[\tan\theta\tan(\theta+\alpha)+1=0.\]

## Suggestion

Can you think of any formulae relating \(\sin, \tan\) and \(\cos\)?

Can we expand \(\cos A\cos B\)? Or \(\sin A \sin B\)?

If we can’t do the first part, can we still do the second and third parts (using the result from the first part)?

## Solution

We’ll use the identities \(\tan x= \dfrac{\sin x}{\cos x}, 2\sin A\sin B = \cos(A-B) - \cos(A+B), 2\cos A\cos B = \cos(A-B) + \cos(A+B).\)

We have

\[k = \tan \theta \tan(\theta+\alpha)\]

\[=\dfrac{2\sin (\theta+ \alpha)\sin \theta}{2\cos (\theta+\alpha) \cos \theta}.\]

We want an expression with arguments \((2\theta+\alpha)\) and \(\alpha\), and we can note that these are the sum and difference of the arguments we have here.

Recalling the identities above, we get

\[k= \dfrac{\cos \alpha - \cos (2\theta+\alpha)}{\cos \alpha + \cos (2\theta+\alpha)},\]

which we can then multiply out and rearrange to get

\[(k+1)\cos(2\theta+\alpha)=(1-k)\cos\alpha.\]

Even if we can’t do the first part of this question, we can still attempt this part using what we were told in the first part.

We use the first part of the question, with \(k=2\) and \(\alpha=\pi/3\).

Remember that \(\pi/3\) radians is equal to \(60^\circ\).

So what we now solve is the much simpler problem \[3\cos(2\theta+\pi/3)=-\cos(\pi/3),\] that is, \[\cos(2\theta+\pi/3)=-\dfrac{1}{6}.\] So we have (where \(n\) is an integer) \[2\theta + \dfrac{\pi}{3} = \arccos\left(-\dfrac{1}{6}\right)+2n\pi\]

OR

\[2\theta + \dfrac{\pi}{3} =-\arccos\left(-\dfrac{1}{6}\right) + 2n\pi.\]

So the general solution is

\[\theta=\pm \dfrac{1}{2}\arccos\left(-\dfrac{1}{6}\right)-\dfrac{\pi}{6}+n\pi,\]

or

\[\theta = 0.3455...+n \pi, -1.393 + n\pi.\]

This time we put \(k=-1\). We find that, from what we proved in the first part, \[0=2\cos\alpha,\] which tells us that there can only exist a solution if \(\alpha\) satisfies \(\cos\alpha=0\), or \(\alpha = \dfrac{\pi}{2} + n\pi\).

Moreover, when \(\cos\alpha = 0\), the equation is satisfied for ANY \(\theta\).

You could plot the curve \(y=\tan x \tan(x+a)\) in [Desmos](https://www.desmos.com/calculator) to verify this…
