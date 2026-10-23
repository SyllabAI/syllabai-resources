---
created: 2026-10-23T16:39:10 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-compound-angles/r7021
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-compound-angles
- type/review-question
resource_identity:
  ugm_id: r7021
  station: trigonometry-compound-angles
  station_title: 'Trigonometry: Compound Angles'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7021
  old_site_id: Q53
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
  spec_points:
  - code: 1.5.2
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-5 cross-map (cross-map-trigonometry.json (P3c
        lane 5) @ syllabai-experimental 75f1cfb8)
      evidence: 'regular pentagon projection: cos(π/5) − cos(2π/5) = 1/2 — exact-value derivation beyond
        the standard 30/45/60 set (extension recorded)'
      rationale: 'Canonical UGM title: “Using angles in a pentagon...”; exam provenance: UCLES A level
        Mathematics 1, QP 180, 1954, Q9'
      validation_status: SUGGESTED
    title: use the exact values of the sine, cosine and tangent of 30 °, 45 °, 60 °, and related angles
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Mathematics 1, QP 180, 1954, Q9
task: T-UGM-IMPORT-5
---

# Using angles in a pentagon...

## Question

\(ABCDE\) is a regular pentagon. By projecting the broken line \(AED\) on the line \(AB\), or otherwise, show that \[\cos\dfrac{\pi}{5}-\cos\dfrac{2\pi}{5}=\frac{1}{2}.\]

Hence, or otherwise, show that \(\cos\dfrac{\pi}{5} = \dfrac{\sqrt{5}+1}{4}\).

Show further that \(\cos\dfrac{3\pi}{5} = -\dfrac{\sqrt{5}-1}{4}\).

## Suggestion

\(ABCDE\) is a regular pentagon. By projecting the broken line \(AED\) on the line \(AB\), or otherwise, show that \[\cos\dfrac{\pi}{5}-\cos\dfrac{2\pi}{5}=\dfrac{1}{2}.\]

Let’s assume that the side lengths of the pentagon are \(1\).

Can we draw a large, clear diagram of the pentagon \(ABCDE\), with \(AB\) horizontally at the bottom?

What are the angles inside a regular pentagon, in radians?

If we now drop perpendiculars from \(D\) and \(E\) to the horizontal, can we start to find lengths and angles?

Using the first part, are there any trigonometrical identities we could use? To get this just in terms of \(\cos\dfrac{\pi}{5}\)?

What’s the sum of \(\dfrac{3\pi}{5}\) and \(\dfrac{2\pi}{5}\)? How does this connect \(\cos\dfrac{3\pi}{5}\) and \(\cos\dfrac{2\pi}{5}\)?

## Solution

\(ABCDE\) is a regular pentagon. By projecting the broken line \(AED\) on the line \(AB\), or otherwise, show that \[\cos\frac{\pi}{5}-\cos\frac{2\pi}{5}=\frac{1}{2}.\]

**Method 1**

The sum of angles inside a \(n\)-sided polygon is \((n-2)\pi\), so each angle inside our regular pentagon is \(\dfrac{3\pi}{5}\). For simplicity we choose each side to be of length \(1\).

Let

\(D'\)

and

\(E'\)

be the points

\(D\)

and

\(E\)

projected onto the line

\(AB\)

as shown. Since

\(ABCDE\)

is a regular pentagon,

\[D'A =\frac{1}{2}.\]

From the right-angled triangle

\(AEE'\)

we see that

\[AE' =\cos\frac{2\pi}{5},\]

and from the triangle

\(DPE\)

we find that

\[D'E' = PE =\cos\frac{\pi}{5}.\]

Since

\[D'E' = D'A + AE',\]

we get the result

\[\begin{equation*} \cos\frac{\pi}{5}-\cos\frac{2\pi}{5}=\frac{1}{2}. \qquad \label{eq:star}\tag{$*$} \end{equation*}\]

**Method 2**

The question says ‘or otherwise’, so we’re free to pick another method if we wish.

The regular pentagon is intimately connected with \(\phi\), the Golden Ratio \(= 1.61803...\), which is the positive solution to \(x^2 - x - 1 = 0\).

Using the Cosine Rule in \(ABD\) one way, \(\cos \dfrac{2\pi}{5} = \dfrac{1}{2\phi}\). Using the Cosine Rule in \(ABD\) another way, \(\cos \dfrac{\pi}{5} = \dfrac{2\phi^2-1}{2\phi^2}\).

Thus \[\cos\dfrac{\pi}{5}-\cos\dfrac{2\pi}{5} = \dfrac{2\phi^2-1}{2\phi^2}- \dfrac{1}{2\phi} = \dfrac{2\phi^2-1}{2\phi^2}- \dfrac{\phi}{2\phi^2}= \dfrac{2\phi^2-\phi-1}{2\phi^2} = \dfrac{\phi^2}{2\phi^2} = \dfrac{1}{2}.\]

Let

\[\gamma=\cos\frac{\pi}{5}.\]

Using the cosine double angle formula

\[\cos 2\theta=2\cos^2\theta-1\]

with

\(\theta=\dfrac{\pi}{5},\)

we can use

\(\eqref{eq:star}\)

to get

\[\begin{align*} \gamma-(2\gamma^2-1) &= \frac{1}{2} \\ \iff \quad 4\gamma^2-2\gamma-1 &= 0. \end{align*}\]

We then use the quadratic formula to solve for \(\gamma\): we have \[\gamma = \cos\frac{\pi}{5}=\frac{2\pm\sqrt{4-4\times 4\times (-1)}}{2\times 4}=\frac{1\pm\sqrt{5}}{4}.\] We know that \(\dfrac{\pi}{5} < \dfrac{\pi}{2}\) so \(\cos\dfrac{\pi}{5}>0\) and thus we choose the positive root: \[\cos\frac{\pi}{5}=\frac{1+\sqrt{5}}{4}.\]

We use the fact that \[\cos(\pi-\theta)=-\cos\theta,\] which we can see from the diagram.

This gives

\[\cos\frac{3\pi}{5}=-\cos\frac{2\pi}{5}\]

so

\[\begin{align*} \cos\frac{3\pi}{5} &= -\cos\frac{2\pi}{5}=\frac{1}{2}-\cos\frac{\pi}{5}\\ &= \frac{2-(\sqrt{5}+1)}{4}=-\frac{\sqrt{5}-1}{4} \end{align*}\]

as required.
