---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/circles/r9045
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- circles
- type/review-question
resource_identity:
  ugm_id: r9045
  station: circles
  station_title: Circles
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9045
  old_site_id: Q59
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: circles
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: circles
    validation_status: SUGGESTED
  spec_points:
  - code: 1.3.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'QP=lambda:1 traces a circle; orthogonal-intersection condition — section formula plus the locus-to-circle family; orthogonality extension.'
      rationale: 'Canonical UGM title: “If $AQ:QP=\lambda:1$, can we show $Q$ lies on a  circle?”; exam provenance: UCLES 1954 Q2'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1954 Q2
task: T-UGM-IMPORT-3
---

# If $AQ:QP=\lambda:1$, can we show $Q$ lies on a  circle?

## Problem

A variable point \(P\) on the circle \(x^2+y^2=a^2\) has coordinates \((a\cos\theta,a\sin\theta)\), and \(A\) is the fixed point \((c,0)\).

If \(Q\) is the point on \(AP\) such that \(AQ:QP=\lambda:1\), find the coordinates of \(Q\), and show that the locus of \(Q\) is another circle. Calculate the coordinates of the centre of this circle and the length of its radius.

Show that the condition for the two circles to intersect at right angles is \(c^2=a^2(1+2\lambda+2\lambda^2)\).

## Suggestion

We can experiment with this GeoGebra applet for this problem.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/F9EgMTvt)

As we move the point \(P\) around its circle, what happens to \(Q\)?

Try with \(A\) in different positions along the axis. What if \(A\) is outside the circle?

You can change the value of \(\lambda\) by sliding \(Q\) along the line.

The point \(Q\) lies some way along the line \(AP\). Can you find the equation of this line?

How could we use the fact \(AQ:QP=\lambda:1\)? Could we find the lengths of the two line segments \(AQ\) and \(QP\)?

Alternatively, is there a way of using \(AQ:QP=\lambda:1\) without knowing the lengths of the line segments?

Could we find the coordinates of \(Q\) as a function of \(\theta\)? (\(\theta\) is defined in the question.)

For the second part, this GeoGebra tool might help.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/Mzjgv5fu)

We can now drag the point \(O_Q\), the centre of the second circle (the point \(A\) is not shown here).

When the two circles intersect at right angles, what can we say about the triangle whose vertices are the centres of the two circles and one of their points of intersection?

## Solution

**Approach 1**

We begin by sketching the circle of radius \(a\) about the origin, the point \(P\) and the point \(A\). We will consider the line \(AP\) and a point \(Q\) such that \(AQ=\lambda QP\).

Here we have drawn the diagram in the case where \(c>a\). Would our answer be any different if we had \(0<c<a\) or \(c<0\)?

Let the co-ordinates of \(Q\) be \((x,y)\) and consider the lengths we know in the following diagram. As we are given co-ordinates, we will add horizontal and vertical lines from \(Q\).

By corresponding angles, the triangles with hypotenuses \(AQ\) and \(QP\) have the same three angles and so are similar. Hence the ratios of the opposite sides, adjacent sides and hypotenuses are equal and so

\[\frac{c-x}{x-a\cos\theta} = \frac{y}{a\sin\theta-y} =\frac{\lambda}{1}.\]

This rearranges to give

\[c-x = \lambda x - \lambda a\cos\theta \qquad \text{and} \qquad y = \lambda a\sin\theta - \lambda y\]

and hence

\[Q=(x,y)=\left(\frac{\lambda a\cos\theta + c}{\lambda+1},\frac{\lambda a\sin\theta}{\lambda+1}\right).\]

We want to show that this sweeps out a circle as \(\theta\) varies from \(0\) to \(2\pi\).

We currently have equations for \(x\) and \(y\) in terms of \(\theta\) and so, to show that this is a circle, we can start by trying to eliminate \(\theta\) and expressing the locus in terms of just \(x\) and \(y\).

The easiest way to do this is to use the identity \(\cos^2 \theta +\sin^2 \theta = 1\). Rearranging our expressions for \(x\) and \(y\) gives that

\[\cos\theta = \left(\frac{\lambda+1}{\lambda a}\right) \left(x - \frac{c}{\lambda+1}\right) \qquad \text{and} \qquad \sin\theta = \left(\frac{\lambda+1}{\lambda a}\right) y.\]

Substituting this in to our identity and dividing through by the common factor gives

\[\left(x - \frac{c}{\lambda+1}\right)^2 + y^2 = \left(\frac{\lambda a}{\lambda+1}\right)^2\]

and so the locus of \(Q\) is a circle with centre \(\left(\dfrac{c}{\lambda+1},0\right)\) and radius \(\dfrac{\lambda a}{\lambda+1}\).

**Approach 2**

Consider the stripped down diagram of the problem.

We let the point \(P\) have position vector \(\mathbf{p}=(a\cos\theta,a\sin\theta)\), \(A\) the vector \(\mathbf{a}=(c,0)\) and the (currently unknown) point \(Q\) the vector \(\mathbf{q}\).

Travelling along the vector from \(A\) to \(P\) we follow the vector equation \[\mathbf{r} = \mathbf{a} + \mu(\mathbf{p} - \mathbf{a}) = \left(\begin{array}{c} c \\ 0 \end{array}\right) + \mu \left(\begin{array}{c} a\cos\theta - c \\ a\sin\theta \end{array}\right),\] where \(0\leq \mu \leq 1\).

It’s given that \(AQ:QP=\lambda:1\), so point \(Q\) is \(\frac{\lambda}{\lambda+1}\) along the line from point \(A\).

Therefore, if we let

\(\mu=\frac{\lambda}{\lambda+1}\)

we will be at point

\(Q\)

so we can then find its coordinates:

\[\mathbf{q}=\left(\begin{array}{c} c \\0 \end{array}\right)+\frac{\lambda}{\lambda+1}\left(\begin{array}{c} a\cos\theta - c \\ a\sin\theta \end{array}\right),\]

so, using the same definition of

\(x\)

and

\(y\)

from before we again find that

\[\begin{align*} x &= c+ \frac{\lambda}{\lambda+1}a\cos\theta - \frac{\lambda c}{\lambda+1}= \frac{c}{\lambda+1} + \frac{\lambda}{\lambda+1}a\cos\theta, \\ y &= \frac{\lambda}{\lambda+1}a\sin\theta \end{align*}\]

so again \[\left(x-\frac{c}{\lambda+1}\right)^2+y^2=\frac{\lambda^2a^2}{(\lambda+1)^2},\]

which leads to the same conclusion.

Show that the condition for the two circles to intersect at right angles is \(\,c^2=a^2(1+2\lambda+2\lambda^2)\).

The two circles intersect at right angles if and only if there is a right-angled triangle formed by the points \(O(0,0)\), \(O_Q\left(\dfrac{c}{\lambda+1},0\right)\) and one of the intersection points, which we will have labelled \(B\).

The triangle \(OBO_Q\) is a right-angled triangle if and only if the lengths of the sides obey [Pythagoras’s theorem](https://undergroundmathematics.org/glossary/pythagoras-theorem): \[a^2+\frac{\lambda^2 a^2}{(\lambda+1)^2}=\frac{c^2}{(\lambda+1)^2}\] \[\iff \quad c^2=a^2(1+2\lambda+2\lambda^2)\] as required.
