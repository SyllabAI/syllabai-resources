---
created: 2026-10-23T16:39:11 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-compound-angles/r7604
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-compound-angles
- type/review-question
resource_identity:
  ugm_id: r7604
  station: trigonometry-compound-angles
  station_title: 'Trigonometry: Compound Angles'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7604
  old_site_id: Q199
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
  exam_reference: UCLES A level Mathematics A Special paper, QP 9200/0, 1981, Q3
task: T-UGM-IMPORT-5
---

# Can we solve these simultaneous trigonometric equations?

## Question

1. Given that \(x=1+2\cos\theta\), prove that \(x^3-3x^2+1= 2\cos 3\theta-1\). Using this result, or otherwise, find each of the three roots of the equation \(x^3-3x^2+1=0\), giving your answers correct to 3 places of decimals.

---

1. The values of \(x\) and \(y\) satisfy the equations \[\begin{align*} 3\cos^2 x+ 2\cos^2 y&=4,\\ 3\sin 2x-2\sin 2y&=0. \end{align*}\] Find the values of \(\cos 2x\) and \(\cos 2y\). Hence find, to the nearest degree, four pairs of corresponding values of \(x\) and \(y\), all values lying between \(0^\circ\) and \(360^\circ\).

## Solution

Let

\(\sin\theta = s\)

, and

\(\cos\theta = c\)

. Looking at the right hand side of the equation we have, using compound angle formulae,

\[\begin{align*} 2\cos 3\theta -1&=2\cos(2\theta +\theta)-1\\ &=2[\cos(2\theta)c-\sin(2\theta)s] -1\\ &=2[(2c^2 -1)c-2s^2c]-1\\ &=2[2c^3-c-2(1-c^2)c]-1\\ &=8c^3-6c-1.\\ \end{align*}\]

Looking at the left hand side of the equation, and expanding using the binomial theorem,

\[\begin{align*} x^3 &=(1+2c)^3\\ &=1+3(2c)+3(2c)^2+(2c)^3\\ &=8c^3+12c^2+6c+1, \end{align*}\]

and

\[\begin{align*} x^2&=(1+2c)^2\\ &=4c^2+4c+1. \end{align*}\]

So

\[\begin{align*} x^3-3x^2+1&= (8c^3 +12c^2+6c+1) -3(4c^2+4c+1)+1\\ &=8c^3-6c-1. \end{align*}\]

Hence, \(x^3-3x^2+1=2\cos 3\theta -1\).

If we use the first part, and take

\(x=1+2\cos\theta\)

, then the equation

\(x^3-3x^2+1=0\)

becomes

\[\begin{align*} &&2\cos 3\theta-1&=0&&\quad\\ \iff&&\cos 3\theta&=\dfrac{1}{2}\\ \iff&&3\theta&=\dfrac{\pi}{3}+2n\pi\ \text{or} -\dfrac{\pi}{3}+2n\pi\\ \iff&&\theta&=\dfrac{\pi}{9}+\dfrac{2n\pi}{3}\ \text{or} -\dfrac{\pi}{9}+\dfrac{2n\pi}{3} \end{align*}\]

for any integer \(n\).

We can then find \(x\) by working out \(1+2\cos\theta\) for these possible values of \(\theta\).

Note that \(\cos(-A)=\cos A\) for any \(A\), and that \(\cos(A+2n\pi)=\cos A\) for any integer \(n\).

Putting \(n = 0, 1, 2\) here gives \[\cos\dfrac{\pi}{9} \left(= \cos\dfrac{-\pi}{9}\right), \cos\dfrac{7\pi}{9} \left(=\cos\dfrac{11\pi}{9}\right) \quad \text{and} \quad \cos\dfrac{13\pi}{9} \left(=\cos\dfrac{5\pi}{9}\right).\]

Therefore the three roots (it cannot have more) of \(x^3-3x^2+1=0\) are \[1+2\cos\dfrac{\pi}{9}=2.879, 1+2\cos\dfrac{7\pi}{9}=-0.532 \quad \text{and} \quad 1+2\cos\dfrac{13\pi}{9}=0.653,\] all given to 3 decimal places.

It’s worth trying to get everything in terms of \(\cos 2 x\) and \(\cos 2 y\) first.

We know that \(\cos 2x=2\cos^2 x-1\); rearranging this gives \(\cos^2 x=\dfrac{1}{2}(1+\cos 2x)\).

So we can rewrite our first equation as

\[\begin{align*} &3\cos^2 x+2\cos^2 y=4\\ \iff\quad &\tfrac{3}{2}(1+\cos 2x)+\tfrac{2}{2}(1+\cos 2y)=4\\ \iff\quad &3\cos 2x+2\cos 2y =3. \end{align*}\]

Now looking at our second equation, we aim to change every

\(\sin\)

to a

\(\cos\)

. Rearranging and squaring both sides, we have

\[9\sin^2 2x=4\sin^2 2y\]

Using the identity

\(\cos^2 \theta +\sin^2 \theta=1\)

gives

\[\begin{align*} & 9(1-\cos^2 2x)=4(1-\cos^2 2y)\\ \iff\quad & 9\cos^2 2x-4\cos^2 2y=5\\ \iff\quad & (3\cos 2x-2\cos 2y)(3\cos2x+2\cos 2y)=5. \end{align*}\]

Now substituting in \(3\cos 2x+2\cos 2y=3\) gives \[3\cos 2x-2\cos 2y=\frac{5}{3}.\]

We now have two linear simultaneous equations in \(\cos 2x\) and \(\cos 2y\). Adding them to eliminate \(\cos 2y\) gives \[6\cos 2x=\frac{14}{3}\] so \(\cos 2x=\frac{7}{9}\).

Substituting into either of our simultaneous equations then gives \(\cos 2y=\dfrac{1}{3}\).

Using the \(\cos^{-1}\) function on a calculator gives \(2x=38.94^\circ\) (to four significant figures).

Thus the general solution is \(2x=-38.94 + 360n\), or \(2x=38.94+360n\).

This gives the four solutions (all to three significant figures) for \(x\) between \(0^\circ\) and \(360^\circ\): \[x=19.5^\circ, 161^\circ, 199^\circ, 341^\circ.\]

Using a similar method to solve \(\cos 2y=\dfrac{1}{3}\) gives (all to three significant figures): \[y=35.3^\circ, 145^\circ, 215^\circ, 325^\circ.\]

We now need to pair the \(x\) values with the corresponding \(y\)-values.

The first equation is equivalent to \(3\cos 2x+2\cos 2y=3\), and we know the values of \(\cos 2x\) and \(\cos 2y\), so this will not help us further.

However, we squared the second equation (thus introducing extra roots), so if we return to the original here, it should tell us more.

So we have \(\sin 2y=\dfrac{3}{2}\sin 2x\).

When \(x=19.5\), \(\sin 2y=\dfrac{3}{2}\sin 2x=0.943\), so \(2y=70.5\) or \(109\) or \(431\) or \(469\), giving \(y=35.3\), \(54.7\), \(215\) or \(235\).

Comparing these with our list of possible values of \(y\) from \(\cos 2y=\dfrac{1}{3}\) shows that \(y=35.3\) or \(215\) in this case.

Likewise, when \(x=161^\circ\), \(\sin 2y=\dfrac{3}{2}\sin 2x=-0.943\), so \(2y=251\) or \(289\) or \(611\) or \(649\), giving \(y=125\) or \(145\) or \(305\) or \(325\).

Thus, comparing with the possible \(y\) values gives \(y=145\) or \(325\) in this case.

In the third case, when \(x=199\), we have \(\sin 2y=0.943\) again, so \(y=35.3\) or \(215\).

Likewise, in the final case, when \(x=341\), we have \(\sin 2y=-0.943\) again, so \(y=145\) or \(325\).

Thus there are in total eight possible pairs of \((x,y)\) values: to the nearest degree, these are:

\[(19^\circ, 35^\circ), (19^\circ, 215^\circ), (161^\circ, 145^\circ), (161^\circ, 325^\circ), (199^\circ, 35^\circ), (199^\circ, 215^\circ), (341^\circ, 145^\circ), (341^\circ, 325^\circ).\]
