---
created: 2026-10-23T16:39:11 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-compound-angles/r8648
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-compound-angles
- type/review-question
resource_identity:
  ugm_id: r8648
  station: trigonometry-compound-angles
  station_title: 'Trigonometry: Compound Angles'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8648
  old_site_id: Q36
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
  exam_reference: UCLES A level Further Mathematics 2, QP 187, 1952, Q3
task: T-UGM-IMPORT-5
---

# Can we solve $\cos\theta - \sin (2\theta) + \cos (3\theta) - \sin (4\theta) = 0$?

## Question

Give the general solutions of the following equations

1. \(2\sin 3\theta - 7 \cos 2\theta + \sin \theta + 1 = 0\),

---

1. \(\cos\theta - \sin 2\theta + \cos 3\theta - \sin 4\theta = 0\).

## Suggestion

How might we reduce the number of different multiples of \(\theta\)?

Can we turn the LHS into a function of \(\sin \theta\) alone, or of \(\cos \theta\) alone?

How can we simplify an expression like \(\cos A + \cos B\)? Are there any identities that could help us?

## Solution

We’ll try to write everything in terms of just \(\sin \theta\) (the single \(\sin\theta\) in the LHS points to this). Let \(s = \sin \theta\), and \(c = \cos\theta\).

We could use the double-angle formula \(\cos 2\theta = 1 - 2s^2.\) We’d like to expand \(\sin 3\theta\). Using the angle addition formula,

\[\begin{align*} \sin 3\theta &= c\sin 2\theta + s\cos 2\theta\\ &= 2sc^2 +s(1-2s^2)\\ &= 2s(1-s^2) + s(1-2s^2)\\ &= 3s - 4s^3. \end{align*}\]

The original equation becomes

\[\begin{align*} 2(3s - 4s^3) - 7(1-2s^2) + s +1 &= 0\\ \implies 8s^3 - 14s^2 - 7s + 6 &= 0. \end{align*}\]

When solving a cubic equation, it is often sensible to try simple numbers like \(s= \pm 1, \pm 2\) to find the first factor using the Factor Theorem.

If we try small integers for \(s\), we find that \(8s^3 - 14s^2 - 7s + 6 = 0\) when \(s = 2\), and so by the Factor Theorem, \(s-2\) is a factor. Thus

\[8s^3 - 14s^2 - 7s + 6 = (s-2)(8s^2+2s -3) =(s-2)(4s+3)(2s-1),\]

which is zero when \(s = 2, -\dfrac{3}{4}\) or \(\dfrac{1}{2}\).

We can note that \(\sin \theta = 2\) is impossible.

As the period of

\(\sin\)

is

\(2\pi\)

, and

\(\sin(\theta) = \sin(\pi-\theta)\)

, the remaining solutions are

\[\begin{align*} \theta = \quad & \sin^{-1}\left(\frac 1 2\right) + 2\pi n, \\ \theta = \quad & \pi - \sin^{-1}\left(\frac 1 2\right) + 2\pi n, \\ \theta =\quad & \sin^{-1}\left(- \frac 3 4\right) + 2\pi n, \\ \theta =\quad & \pi-\sin^{-1}\left(- \frac 3 4\right) + 2\pi n \end{align*}\]

where

\(n\)

is an integer. We can simplify to find

\[\begin{align*} \theta =\quad & \dfrac{\pi}{6} +2n\pi, \\ \theta =\quad & \dfrac{5\pi}{6} +2n\pi, \\ \theta =\quad & -\sin^{-1}\left(\frac 3 4\right)+2n\pi, \\ \theta =\quad & \sin^{-1}\left(\frac 3 4\right)+(2n+1)\pi, \end{align*}\]

where in each case \(n\) is any integer.

We might try an approach similar to that above, by writing everything in terms of \(\cos \theta\) and \(\sin \theta\). It’s probably quicker, however, to use the sum-to-product formulae, which help us to combine two \(\sin\) or two \(\cos\) functions.

\[\sin A + \sin B = 2 \sin\left(\frac{A+B} 2\right) \cos\left(\frac{A-B} 2\right)\] and \[\cos A + \cos B = 2 \cos\left(\frac{A+B} 2\right) \cos\left(\frac{A-B} 2\right).\]

We can derive these simply from

\[\begin{align*} \sin(X\pm Y) &= \sin(X)\cos(Y) \pm \cos(X)\sin(Y),\\ \cos(X\pm Y) &= \cos(X)\cos(Y) \mp \sin(X)\sin(Y) \end{align*}\]

Applying these to this part of the question we obtain

\[\cos \theta + \cos 3\theta = 2 \cos 2\theta \cos \theta , \qquad \sin 2\theta + \sin 4\theta = 2 \sin 3\theta \cos \theta\]

and so we need to solve

\[\begin{align*} 2\cos 2\theta \cos \theta - 2\sin3\theta\cos\theta & = 0 \\ \Longleftrightarrow \cos \theta (\cos 2 \theta - \sin 3\theta) & = 0. \end{align*}\]

So our solutions are \(\cos \theta = 0\), which gives \(\theta = \dfrac{\pi}{2} + n\pi\), or are the solutions to \(\cos 2\theta = \sin 3\theta\).

Now

\(\cos 2\theta = 1-2s^2\)

, while (as we showed above)

\(\sin 3\theta = 3s-4s^3\)

, so we need to solve

\[\begin{align*} 1-2s^2&=3s-4s^3\\ \implies 4s^3-2s^2-3s+1&=0\\ \implies (s-1)(4s^2+2s -1)&=0\\ \implies \sin \theta = 1 \quad \text{or} \quad \sin \theta &= \dfrac{-1\pm\sqrt{5}}{4}. \end{align*}\]

So our final solution is

\[\begin{align*} \theta = \quad &\dfrac{\pi}{2} + n\pi\\ \text{or} \quad \theta = \quad &\sin^{-1}\left(\dfrac{-1+ \sqrt{5}}{4}\right) + 2n\pi,\\ \text{or} \quad \theta = \quad &\pi - \sin^{-1}\left(\dfrac{-1+ \sqrt{5}}{4}\right) + 2n\pi, \\ \text{or} \quad \theta = \quad &\sin^{-1}\left(\dfrac{-1- \sqrt{5}}{4}\right) + 2n\pi,\\ \text{or} \quad \theta = \quad &\pi - \sin^{-1}\left(\dfrac{-1- \sqrt{5}}{4}\right) + 2n\pi, \end{align*}\]

where \(n\) is an integer.

Alternatively, we could note that \[\cos \alpha = \cos \beta \implies \alpha = \pm \beta + 2n\pi.\]

We also have (by considering a right-angled triangle where one angle is \(\gamma\)) that \[\sin \gamma = \cos\left(\dfrac{\pi}{2}-\gamma\right).\] This is in fact true for all \(\gamma\).

Thus the equation

\(\cos 2\theta = \sin 3\theta\)

becomes

\[\begin{align*} \cos 2\theta &= \cos \left(\dfrac{\pi}{2}-3\theta \right)\\ \implies 2\theta &= \pm \left(\dfrac{\pi}{2}-3\theta\right) +2n\pi\\ \implies \theta &= \dfrac{\pi}{2} +2n\pi \quad \text{or} \quad \dfrac{\pi}{10} + \dfrac{2n\pi}{5}, \end{align*}\]

and so we have the same answers as before, but this time in an explicit form.

Notice we have inadvertently shown here that \(\sin\left(\dfrac{\pi}{10}\right) = \dfrac{-1+ \sqrt{5}}{4}\).
