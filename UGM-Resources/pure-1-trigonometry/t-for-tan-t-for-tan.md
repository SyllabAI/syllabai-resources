---
created: 2026-10-23T16:39:11 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-compound-angles/t-for-tan
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-compound-angles
- type/building-blocks
- level/developing
resource_identity:
  ugm_id: t-for-tan
  station: trigonometry-compound-angles
  station_title: 'Trigonometry: Compound Angles'
  resource_type_id: 1
  resource_type_label: Building blocks
  level: Developing
  ref: 8131
  old_site_id: G5_RT2_1
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
  exam_reference: Based on this
task: T-UGM-IMPORT-5
assets:
- path: https://undergroundmathematics.org/trigonometry-compound-angles/t-for-tan/download/teacher-notes.pdf
  kind: printable
---

# $t$ for $\tan$

> Excerpt: This resource gives students a simple diagram which they can use to deduce the double angle formulae in terms of $\tan \theta$.

## Problem

If we write \(t = \tan \theta\), then the following equations are true.

\[\begin{align*} \tan 2\theta &= \frac{2t}{1-t^2}, \\ \sin 2\theta &= \frac{2t}{1+t^2}, \\ \cos 2\theta &= \frac{1-t^2}{1+t^2}. \end{align*}\]

Can you use this diagram to obtain these formulae?

For what range of values of \(\theta\) does this argument work?

## Suggestion

What lengths and angles might be useful to us here? Can you find the missing lengths and angles in terms of \(t\)?

Which angle is \(2\theta\)?

The relationships are shown using a triangle. Are there any values of \(\theta\) for which the diagram does not work? Can you adapt it?

## Solution

We have various interesting triangles to consider in this diagram. Let’s study them to see which lengths and angles we can find. In order to talk about the triangle, it will be convenient to label the important points.

In triangle \(ABC\), since \(B\) is the right angle, \(\tan \theta = \tfrac{AB}{BC}\). Since we are told that \(\tan \theta = t\) and \(BC=2\) we get length \(AB=2t\).

Let’s say that \(AD\) has length \(x\).

We see that we have a triangle with two angles that are both \(\theta\), namely triangle \(ADC\), so this is an isosceles triangle, and so \(DC\) also has length \(x\).

Now \(BD\) has length \(2 - x\).

Triangle \(ABD\) is right-angled, and so we can apply [Pythagoras’s theorem](https://undergroundmathematics.org/glossary/pythagoras-theorem): we have \(x^2 = (2-x)^2 + 4t^2\). Rearranging this gives \(0 = 4 - 4x + 4t^2\), and so \(x = 1 + t^2\).

We now know that \(AD = DC = 1 + t^2\), and \(BD = 2 - (1 + t^2) = 1 - t^2\).

Are there any angles in the diagram that might be \(2\theta\)?

\(\angle ADC = 180 - 2\theta\), so \(\angle BDA = 2\theta\).

We are now well placed to consider the trig functions applied to \(2\theta\), because not only do we have a triangle that contains this angle, but we have a *right-angled* triangle containing the angle (namely triangle \(ABD\)). So let’s focus on that triangle.

Considering the right-angled triangle \(ABD\), we see that \[\sin 2\theta = \frac{2t}{1+t^2},\] \[\cos 2\theta = \frac{1-t^2}{1+t^2},\] and \[\tan 2\theta = \frac{2t}{1-t^2}.\]

#### Alternative approach

If we know the equations that we are aiming to derive, then we can take a slightly different approach, although this one is a bit more subtle and needs quite a lot of care in order to avoid a circular argument!

As in the last approach, we establish that one of the angles (not the right angle) is $\theta$ and the adjacent side (not the hypotenuse) has length $2$, so the opposite side must have length $2t$ since we are told that $\tan \theta = t$. There is another very obvious right-angled triangle in the diagram, namely $ABD$. We might hope that it will turn out that $\angle BDA$ is $2\theta$, as that would leave us in good shape to find sine, cosine and tangent of $2\theta$. Given the equations we hope to derive, that would suggest that the hypotenuse should have length $1 + t^2$ and the remaining side length $1 - t^2$. By the converse of Pythagoras's theorem, we see that $1 - t^2$, $2t$ and $1 + t^2$ are indeed the side lengths of a right-angled triangle (since $(1-t^2)^2 + (2t)^2 = (1 + t^2)^2$).

If \(0^{\circ} < \theta < 45^{\circ}\), then we can draw the diagram given in the question and the argument goes through.

If \(\theta = 45^{\circ}\), then the argument degenerates: point \(D\) is the same as point \(B\), we have \(t = 1\), and \(\tan 2\theta\) is not defined anyway.

If \(45^{\circ} < \theta < 90^{\circ}\), then point \(D\) lies outside the triangle. Does the argument still work?

We can sketch triangle \(ACB\) so that \(\angle C=\theta\) where \(45^{\circ} < \theta < 90^{\circ}\) and \(\angle B = 90^{\circ}\). If \(\angle CAD=\theta\) and \(C, B\) and \(D\) are on a straight line, it puts \(D\) outside triangle \(ACB\). Can we now use a similar process to above?

Do any lengths keep the same algebraic values?

The angle in triangle \(BDA\) is now \(180^\circ -2\theta\). How can we use our knowledge of the functions to relate the trigonometric ratios of these angles to \(\sin {2\theta}\), \(\cos {2\theta}\), \(\tan {2\theta}?\)
