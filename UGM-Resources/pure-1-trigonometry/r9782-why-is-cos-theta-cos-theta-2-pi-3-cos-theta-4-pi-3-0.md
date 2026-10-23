---
created: 2026-10-23T16:39:11 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-compound-angles/r9782
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-compound-angles
- type/review-question
resource_identity:
  ugm_id: r9782
  station: trigonometry-compound-angles
  station_title: 'Trigonometry: Compound Angles'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9782
  old_site_id: Q43
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
  exam_reference: UCLES A level Mathematics 1, QP 186, 1951, Q6
task: T-UGM-IMPORT-5
---

# Why is $\cos \theta + \cos (\theta + 2\pi/3) + \cos(\theta + 4\pi/3)=0$?

## Question

1. Prove that \[\cos(A+B)=\cos A\cos B - \sin A\sin B,\] where the angles \(A\), \(B\) and \(A+B\) are all acute.

---

1. By projecting the sides of an equilateral triangle onto a certain line, prove that \[\cos \theta + \cos \left(\theta + \frac{2\pi}{3}\right) + \cos\left(\theta+\frac{4\pi}{3}\right)=0\] and find the value of the expression \[\sin \theta + \sin \left(\theta + \frac{2\pi}{3}\right) + \sin\left(\theta+\frac{4\pi}{3}\right).\]

## Suggestion

There is a standard geometric proof of this formula using the unit circle. If you haven’t come across it before, you may like to have a look at the diagram hidden below.

A useful diagram

What lengths can you calculate, in terms of \(\alpha\) and \(\beta\)?

Could we draw an equilateral triangle at an angle \(\theta\) to the horizontal? What angles do we know? What horizontal lengths can we deduce?

To find the value of the \(\sin\) sum, what vertical lengths can we deduce?

## Solution

We’ll use \(\alpha\) and \(\beta\) to represent the angles, and capital letters to represent points on the diagram. So we are trying to prove that

\[\cos(\alpha+\beta) = \cos \alpha \cos \beta - \sin \alpha \sin \beta.\]

The circle drawn has radius \(1\) (it’s a unit circle). From triangle \(OCD\), we see that \(\quad OD = \cos(\alpha+\beta)\).

From triangle \(OFC\), we know \(\quad CF = \sin \beta \quad\) and \(\quad OF = \cos \beta.\)

From triangle \(CFG\), \[\sin \alpha = \frac{FG}{FC} \quad \Longrightarrow \quad FG = \sin \alpha \sin \beta.\]

From triangle \(OEF\), \[\cos \alpha = \frac{OE}{OF} \quad \Longrightarrow \quad OE = \cos \alpha \cos \beta.\]

As \(FG\) is equal in length to \(DE\), we have

\[\begin{align*} OE &= OD + DE \\ &= OD + FG. \\ \end{align*}\]

Therefore \(\cos \alpha \cos \beta = \cos(\alpha+\beta) + \sin \alpha \sin \beta,\) so \(\cos(\alpha+\beta) = \cos \alpha \cos \beta - \sin \alpha \sin \beta,\) as required.

The restriction to acute angles is actually unnecessary - this works for all angles.

Let’s start by drawing an equilateral triangle inside a unit circle, at an angle \(\theta\) to the horizontal.

We can quickly identify (using parallel lines and angles in triangles) that \[\angle BAD = \theta + \frac{2 \pi}{3} \qquad \text{and} \qquad \angle CBO \text{ (reflex)} = \theta + \frac{4 \pi}{3}.\]

Thinking about the unit circle, we can see (by considering the diagrams below) that

If we take \(\psi = \theta + \dfrac{2 \pi}{3}\), we see that

\[\cos \left(\theta + \dfrac{2\pi}{3} \right) = \overrightarrow{AM} \equiv \overrightarrow{A'B'},\]

and taking \(\phi = \theta + \dfrac{4\pi}{3}\), we have

\[\cos \left(\theta + \dfrac{4\pi}{3} \right) = \overrightarrow{B'O}.\]

Therefore

\[\cos \theta + \cos \left(\theta + \frac{2\pi}{3} \right) + \cos \left(\theta + \frac{4\pi}{3} \right) = \overrightarrow{OA'} + \overrightarrow{A'B'} + \overrightarrow{B'O}.\]

(i.e. we move from \(O\) to \(A'\), return to \(B'\) and then back to \(O\)).

Therefore the total displacement is zero, and so \[\cos \theta + \cos \left(\theta + \frac{2\pi}{3}\right) + \cos\left(\theta+\frac{4\pi}{3}\right)=0.\]

…and find the value of the expression \[\sin \theta + \sin \left(\theta + \frac{2\pi}{3}\right) + \sin\left(\theta+\frac{4\pi}{3}\right).\]

The sum for \(\sin\) can similarly be found by projecting the sides of an equilateral triangle onto the \(y\)-axis.

We can think again about the unit circle and how we find the sine of different angles:

Let \(\psi = \theta + \dfrac{2\pi}{3}\) and \(\phi = \theta + \dfrac{4\pi}{3}\). From our diagram above, we get

\[\begin{align*} \sin \theta + \sin \left(\theta + \frac{2\pi}{3} \right) + &\sin \left(\theta + \frac{4\pi}{3} \right) \\ &= \overrightarrow{A'A} + \overrightarrow{MB} + \overrightarrow{BB'} \\ &= \overrightarrow{B'M} + \overrightarrow{MB} + \overrightarrow{BB'} \\ &= 0. \end{align*}\]

Suppose we are allowed to use any method for the last two parts. If we know about complex numbers, they can be tackled more quickly. Let $w = \cos\theta + i\sin\theta$. Then if $k = e^{2\pi/3}$, we have $$w+kw+k^2w = \cos \theta + \cos \left(\theta + \frac{2\pi}{3}\right) + \cos\left(\theta+\frac{4\pi}{3}\right)+i(\sin \theta + \sin \left(\theta + \frac{2\pi}{3}\right) + \sin\left(\theta+\frac{4\pi}{3}\right)).$$ But we know $k^3 = 1$, so $k^3 -1 = (k-1)(k^2+k+1) =0$. Since $k \neq 1$, we have $k^2+k+1 = 0$, and so $$\cos \theta + \cos \left(\theta + \frac{2\pi}{3}\right) + \cos\left(\theta+\frac{4\pi}{3}\right)+i(\sin \theta + \sin \left(\theta + \frac{2\pi}{3}\right) + \sin\left(\theta+\frac{4\pi}{3}\right))=0,$$ which gives us both our results.
