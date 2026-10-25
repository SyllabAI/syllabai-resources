---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/parametric-points
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/fluency-exercise
resource_identity:
  ugm_id: parametric-points
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 8
  resource_type_label: Fluency exercise
  level: Developing
  ref: 8891
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: chain-rule
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: chain-rule
    validation_status: SUGGESTED
  spec_points:
  - code: 3.4.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-12 cross-map (cross-map-p3-differentiation.json
        (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4)
      evidence: dy/dx = -(3 cos t)/(2 sin t) for the parametric ellipse, matched to stationary-point locations
        and graphs - the 3.4.3 parametric chain-rule law as the matching tool (flips the lane-11 non-overlap
        row of record routed 'P3 3.4 Differentiation')
      rationale: 'Canonical UGM title: Parametric points'
      validation_status: SUGGESTED
    title: find and use the first derivative of a function e.g. which is defined parametrically or implicitly.
  mapped_date: '2026-10-25'
  mapper: cross-map-p3-differentiation.json (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-12
---

# Parametric points

> Excerpt: Students are asked to match up parametric equations with locations of stationary points and with their graphs. This requires use of the Chain Rule in the context of parametrics. We encounter some interesting looking curves.

## Warm-up

A curve in the \(x-y\) plane is defined parametrically in terms of a parameter \(t\) as \[x=2 \cos t,\quad y=3 \sin t.\]

Find an expression for \(\dfrac{dy}{dx}\) in terms of \(t\).

Answer

\[\begin{align*} x=2\cos t \quad\implies\quad \frac{dx}{dt}&=-2\sin t \\ y=3\sin t \quad\implies\quad \frac{dy}{dt}&=3\cos t \end{align*}\]

Using the [chain rule](https://undergroundmathematics.org/glossary/chain-rule), \[\frac{dy}{dx} = \frac{dy/dt}{dx/dt} = -\frac{3\cos t}{2\sin t}.\]

Hence find the stationary points on the curve.

Are there any values of \(t\) for which \(\dfrac{dy}{dx}\) is undefined? What would that mean?

Answer

At the stationary points,

\(\frac{dy}{dx} = 0\)

which means

\[\begin{equation*} -\frac{3\cos t}{2\sin t} = 0 \quad\implies\quad \cos t=0. \end{equation*}\]

We don’t need to know the values of \(t\); to find \(x\) and \(y\) it is sufficient to know \(\cos t\) and \(\sin t\). When \(\cos t=0\), \(\sin t = 1\) or \(-1\), so substituting we find the stationary points are at \[(0,3)\text{ and }(0,-3).\]

\(\dfrac{dy}{dx}\) is undefined when \(\sin t=0\) which happens at \[(-2,0) \text{ and } (2,0).\] A sketch of the curve should make it clear what is happening here.

## Problem

Here is a set of equations defined parametrically in terms of \(t\).

\[\begin{align*} x &= 1+ 4 \cos t \\ y &= t+ 3 \sin t \end{align*}\]

\[\begin{align*} x &= 2 \cos t \\ y &= \sin 2t \end{align*}\]

\[\begin{align*} x &= t^2 \\ y &= t^3-4t \end{align*}\]

\[\begin{align*} x &= t^2+t+1 \\ y &= 2t^2-2 \end{align*}\]

\[\begin{align*} x &= t^3-t \\ y &= t^3-3t \end{align*}\]

\[\begin{align*} x &= 2+ 3 \cos t \\ y &= 4+ 5 \sin t \end{align*}\]

Using the interactive below or the [printable cards](https://undergroundmathematics.org/chain-rule/parametric-points/components/cards.pdf), match up each equation (blue card) with

- the location of a stationary point on the curve (green card),

- the location of a [critical point](https://undergroundmathematics.org/glossary/critical-point) on the curve where the tangent is vertical (pink card),

- its graph (white card).

*(Note that some of the curves have other stationary points and critical points that do not appear on cards.)*

\[\begin{align*} x &= 2+ 3 \cos t \\ y &= 4+ 5 \sin t \end{align*}\]

\[\begin{align*} x &= t^3-t \\ y &= t^3-3t \end{align*}\]

\[\begin{align*} x &= t^2+t+1 \\ y &= 2t^2-2 \end{align*}\]

\[\begin{align*} x &= t^2 \\ y &= t^3-4t \end{align*}\]

\[\begin{align*} x &= 2 \cos t \\ y &= \sin 2t \end{align*}\]

\[\begin{align*} x &= 1+ 4 \cos t \\ y &= t+ 3 \sin t \end{align*}\]

Stationary point at \[x=1\]

Stationary point at \[x=0\]

Stationary point at \[x=-\frac{1}{3}\]

Stationary point at \[x=\sqrt{2}\]

Stationary point at \[x=2\]

Stationary point at \[x=\frac{4}{3}\]

Critical point at \[(0,0)\]

Critical point at \[(5,4)\]

Critical point at \[\left(\frac{2}{3\sqrt{3}},\frac{8}{3\sqrt{3}}\right)\]

Critical point at \[(2,0)\]

Critical point at \[(5,0)\]

Critical point at \[\left(\frac{3}{4},-\frac{3}{2}\right)\]

## Solution

The first thing you might notice is that three of the equations are based on trigonometric functions while the other three are based on powers of \(t\).

What might that tell us about the kind of curves they represent?

Match up each equation (blue card) with

- the location of a stationary point on the curve (green card),

To find the stationary points on a curve, we want to find \(\frac{dy}{dx}\) and when it is equal to zero.

Taking equation (E1), we have

\[\begin{align*} x = 1+ 4 \cos t&, \quad y = t+ 3 \sin t \\ \implies\quad \frac{dx}{dt} = -4\sin t&, \quad \frac{dy}{dt} = 1+3\cos t. \end{align*}\]

We can combine these using the chain rule.

\[\begin{equation*} \frac{dy}{dx} = \frac{dy/dt}{dx/dt} = \frac{1+3\cos t}{-4\sin t} \end{equation*}\]

This is zero when

\[\begin{equation*} 1+3\cos t = 0 \quad\implies\quad \cos t=-\frac{1}{3}. \end{equation*}\]

Substituting this back into the equation tells us the curve is stationary when

\[\begin{equation*} x = 1+4\left(-\frac{1}{3}\right) = -\frac{1}{3}. \end{equation*}\]

This therefore goes with card (S4).

Note that we quietly ignored the \(\sin t\) in the denominator of \(\frac{dy}{dx}\) when setting it equal to zero. We should really check that the denominator is not zero at the same point as the numerator is zero, because if it were the gradient would be undefined. In this case, that doesn’t happen (\(\sin t\ne0\) when \(\cos t=-1/3\)) so we are OK.

At a critical point the tangent is vertical and \(\frac{dy}{dx}\) is undefined. This will happen when our expression for \(\frac{dy}{dx}\) is a fraction with zero in the denominator and non-zero in the numerator.

Taking equation (E5), we have

\[\begin{align*} x = t^3-t&, \quad y = t^3-3t \\ \implies\quad \frac{dx}{dt} = 3t^2-1&, \quad \frac{dy}{dt} = 3t^2-3. \end{align*}\]

We could combine these to write

\(\frac{dy}{dx}\)

as a fraction, but in fact we are only interested in when

\(\frac{dx}{dt}=0\)

.

As above, we should also check that \(\frac{dy}{dt}\ne 0\) at the same value of \(t\). In this case, they are quadratics in \(t\) differing only by a constant, so they can never be zero at the same time.

So the critical points happen at

\[\begin{align*} 3t^2-1&=0 \quad\implies\quad t=\pm\frac{1}{\sqrt{3}} \\ \implies\quad x&=\pm\left(\frac{1}{3\sqrt{3}}-\frac{1}{\sqrt{3}}\right) = \pm\frac{2}{3\sqrt{3}} \\ \text{and}\quad y&=\pm\left(\frac{1}{3\sqrt{3}}-\frac{3}{\sqrt{3}}\right) = \pm\frac{8}{3\sqrt{3}} \end{align*}\]

This therefore goes with card (V4).

We can use the above features of the curve to work out which of the graphs it goes with. Taking equation (E2) as an example, \[x=2\cos t, \: y=\sin 2t,\] we find it has

- stationary points at \(x=\pm\sqrt{2}\),

- critical points at \((2,0)\) and \((-2,0)\).

Also, since we know the range of the

\(\sin\)

and

\(\cos\)

functions, we can deduce that

\[\begin{equation*} -2\le x\le 2 \quad\text{and}\quad -1\le y\le 1 \end{equation*}\]

so the whole curve must be contained within a rectangle. From these clues, the only graph card it can match is (C2).

If we wanted an extra clue to help identify the graph, we could find the \(x\)-intercepts and/or \(y\)-intercepts. This curve, for instance, has \(x\)-intercepts at \(x=0\) and \(x=\pm2\), which confirms the match with (C2).

Set of matched cards

\[\begin{align*} x &= 1+ 4 \cos t \\ y &= t+ 3 \sin t \end{align*}\]

Stationary point at \[x=-\frac{1}{3}\]

Critical point at \[(5,0)\]

\[\begin{align*} x &= 2 \cos t \\ y &= \sin 2t \end{align*}\]

Stationary point at \[x=\sqrt{2}\]

Critical point at \[(2,0)\]

\[\begin{align*} x &= t^2 \\ y &= t^3-4t \end{align*}\]

Stationary point at \[x=\frac{4}{3}\]

Critical point at \[(0,0)\]

\[\begin{align*} x &= t^2+t+1 \\ y &= 2t^2-2 \end{align*}\]

Stationary point at \[x=1\]

Critical point at \[\left(\frac{3}{4},-\frac{3}{2}\right)\]

\[\begin{align*} x &= t^3-t \\ y &= t^3-3t \end{align*}\]

Stationary point at \[x=0\]

Critical point at \[\left(\frac{2}{3\sqrt{3}},\frac{8}{3\sqrt{3}}\right)\]

\[\begin{align*} x &= 2+ 3 \cos t \\ y &= 4+ 5 \sin t \end{align*}\]

Stationary point at \[x=2\]

Critical point at \[(5,4)\]
