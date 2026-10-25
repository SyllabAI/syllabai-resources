---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-trig-log/rotating-derivatives
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-trig-log
- type/scaffolded-task
resource_identity:
  ugm_id: rotating-derivatives
  station: calculus-trig-log
  station_title: Calculus of Trigonometry & Logarithms
  resource_type_id: 3
  resource_type_label: Scaffolded task
  level: Introducing
  ref: 9337
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-trig-log
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-trig-log
    validation_status: SUGGESTED
  spec_points:
  - code: 3.4.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-12 cross-map (cross-map-p3-differentiation.json
        (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4)
      evidence: the unit-circle velocity vector (-sin t, cos t) assembled from the rotating diagrams -
        the geometric derivation of d/dt(sin t) = cos t and d/dt(cos t) = -sin t, the 3.4.1 standard facts
        (flips the lane-11 non-overlap row of record routed 'P3 3.4 Differentiation')
      rationale: 'Canonical UGM title: Rotating derivatives'
      validation_status: SUGGESTED
    title: use the derivatives of e , ln x , sin x , cos x , tan x , tan x , together with constant multiples,
      sums, differences and composites
  mapped_date: '2026-10-25'
  mapper: cross-map-p3-differentiation.json (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-12
---

# Rotating derivatives

> Excerpt: By considering a particle or point moving around a unit circle, students are asked to interpret diagrams which lead to the derivatives of $\sin t$ and $\cos t$.

## Problem

Particle \(P\) is moving anti-clockwise round a circle of radius \(\quantity{1}{m}\) at speed \(\quantity{1}{m\,s^{-1}}\).

The particle is at point \(A\) when \(t=0\) and its position at time \(\quantity{t}{s}\) is shown in the diagram below.

are given by the rates at which its $$its vector is given by $$\mathbf{v}=\left( \begin{matrix}\dfrac{d}{dt}(\cos t)\\\dfrac{d}{dt}(\sin t)\end{matrix}\right)$$ which it may be more convenient to write as $\mathbf{v}=\left( \dfrac{d}{dt}(\cos t), \dfrac{d}{dt}(\sin t)\right)$.

Combine some of the following diagrams to explain why the velocity vector \(\mathbf{v}\) is \((-\sin t, \cos t)\). You may be able to do this in more than one way. (The diagrams are also provided on [cards](https://undergroundmathematics.org/calculus-trig-log/rotating-derivatives/components/diagrams-cards.pdf).)

- How have you used the fact that \(P\) is moving at unit speed on a unit circle?

- What does this tell you about the derivatives of \(\cos t\) and \(\sin t\)?

Velocity is the rate of change of displacement, so its components are given by the rates at which its \(x\) and \(y\) coordinates are changing with respect to time. Therefore \[\mathbf{v}=\left( \dfrac{dx}{dt}, \dfrac{dy}{dt}\right).\]

<cm-table> <cm-tr> <cm-td><cm-image url="images/coordinatesb.svg" alt-text=" " caption=""/></cm-td><cm-td><cm-image url="images/velocityontangentb.svg" alt-text=" " caption=""/></cm-td><cm-td><cm-image url="images/uppertrianglet.svg" alt-text=" " caption=""/></cm-td> </cm-tr> <cm-tr> <cm-td><cm-image url="images/introduceqb.svg" alt-text=" " caption=""/></cm-td><cm-td><cm-image url="images/qcoordsb.svg" alt-text=" " caption=""/></cm-td><cm-td><cm-image url="images/vlabelled.svg" alt-text=" " caption=""/></cm-td> </cm-tr> </cm-table>

## Suggestion

Particle \(P\) is moving anti-clockwise round a circle of radius \(\quantity{1}{m}\) at speed \(\quantity{1}{m\,s^{-1}}\).

The particle is at point \(A\) when \(t=0\) and its position at time \(\quantity{t}{s}\) is shown in the diagram below.

are given by the rates at which its $$its vector is given by $$\mathbf{v}=\left( \begin{matrix}\dfrac{d}{dt}(\cos t)\\\dfrac{d}{dt}(\sin t)\end{matrix}\right)$$ which it may be more convenient to write as $\mathbf{v}=\left( \dfrac{d}{dt}(\cos t), \dfrac{d}{dt}(\sin t)\right)$.

Combine some of the following diagrams to explain why the velocity vector \(\mathbf{v}\) is \((-\sin t, \cos t)\). You may be able to do this in more than one way.

- How have you used the fact that \(P\) is moving at unit speed on a unit circle?

- What does this tell you about the derivatives of \(\sin t\) and \(\cos t\)?

Here are some questions to ask yourself when looking at the diagrams. (The diagrams with questions are also provided on [cards](https://undergroundmathematics.org/calculus-trig-log/rotating-derivatives/components/suggestion-cards.pdf).)

What is the magnitude and direction of \(\mathbf{v}\)?

Why is \(P\) in this position at time \(\quantity{t}{s}\)?

How are vectors \(\mathbf{v}\) and \(\overrightarrow{OQ}\) related?

How are the two triangles related?

Why is \(\mathbf{v}\) given by the vector shown?

Why are these the coordinates of \(Q\)?

<cm-table> <cm-tr> <cm-td><cm-image url="images/coordinatesb.svg" alt-text=" " caption=""/> Why is $P$ in this position at time $\quantity{t}{s}$? </cm-td> <cm-td><cm-image url="images/velocityontangentb.svg" alt-text=" " caption=""/> What is the magnitude and direction of $\mathbf{v}$? </cm-td> <cm-td><cm-image url="images/uppertrianglet.svg" alt-text=" " caption=""/> How are the two triangles related? </cm-td> </cm-tr> <cm-tr> <cm-td><cm-image url="images/introduceqbs.svg" alt-text=" " caption=""/> How are vectors $\mathbf{v}$ and $\overrightarrow{OQ}$ related? </cm-td> <cm-td><cm-image url="images/qcoordsb.svg" alt-text=" " caption=""/> Why are these the coordinates of $Q$? </cm-td><cm-td><cm-image url="images/vlabelled.svg" alt-text=" " caption=""/> Why is $\mathbf{v}$ given by the vector shown? </cm-td> </cm-tr> </cm-table>

## Things you might have noticed

Particle \(P\) is moving anti-clockwise round a circle of radius \(\quantity{1}{m}\) at speed \(\quantity{1}{m\,s^{-1}}\).

The particle is at point \(A\) when \(t=0\) and its position at time \(\quantity{t}{s}\) is shown in the diagram below.

are given by the rates at which its $$its vector is given by $$\mathbf{v}=\left( \begin{matrix}\dfrac{d}{dt}(\cos t)\\\dfrac{d}{dt}(\sin t)\end{matrix}\right)$$ which it may be more convenient to write as $\mathbf{v}=\left( \dfrac{d}{dt}(\cos t), \dfrac{d}{dt}(\sin t)\right)$.

Combine some of the following diagrams to explain why the velocity vector \(\mathbf{v}\) is \((-\sin t, \cos t)\). You may be able to do this in more than one way.

- How have you used the fact that \(P\) is moving at unit speed on a unit circle?

We’ll use the diagrams with the prompts from the suggestion section.

Why is \(P\) in this position at time \(\quantity{t}{s}\)?

What is the magnitude and direction of \(\mathbf{v}\)?

Why is $P$ in this position at time $\quantity{t}{s}$?

What is the magnitude and direction of $\mathbf{v}$?

\(P\) is moving with speed \(\quantity{1}{m\,s^{-1}}\) round a circle of radius \(\quantity{1}{m}\). Therefore, after time \(\quantity{t}{s}\), it has travelled a distance of \(\quantity{t}{m}\) along a circular arc of radius \(\quantity{1}{m}\). This arc subtends an angle \(\quantity{t}{rads}\) at the centre of the circle, and hence the coordinates of \(P\) at time \(\quantity{t}{s}\).

At any time \(\quantity{t}{s}\) the velocity of \(P\) has magnitude \(\quantity{1}{m\,s^{-1}}\) and is directed along the tangent to the circle at the point \((\cos t, \sin t)\).

There are a couple of ways to approach the rest of the problem. We can think about triangles in the plane, or we can think about transforming vectors.

Using triangles

How are the two triangles related?

Why is \(\mathbf{v}\) given by the vector shown?

<cm-table max-width="600"> <cm-tr> <cm-td><cm-image url="images/uppertrianglet.svg" alt-text=" " caption=""/> How are the two triangles related? </cm-td> <cm-td><cm-image url="images/vlabelled.svg" alt-text=" " caption=""/> Why is $\mathbf{v}$ given by the vector shown? </cm-td> </cm-tr> </cm-table>

Both triangles are right-angled, with one angle \(t\) and hypotenuse \(1\). Therefore they are congruent.

The hypotenuses of the two triangles are perpendicular, so by considering the angles around \(P\) we can see that the sides of the red triangle are parallel to the axes.

The length of the horizontal side of the red triangle is \(\sin t\) and the length of the vertical side is \(\cos t\). It follows that \(\mathbf{v}\) can be expressed as \((-\sin t, \cos t)\), as shown.

- Why is the horizontal component of \(\mathbf{v}\) given by \(-\sin t\) rather than \(\sin t\)?

- What would happen if \(P\) were in a different quadrant?

Transforming vectors

How are vectors \(\mathbf{v}\) and \(\overrightarrow{OQ}\) related?

Why are these the coordinates of \(Q\)?

Why is \(\mathbf{v}\) given by the vector shown?

As \(\angle POQ\) is a right-angle, \(\overrightarrow{OQ}\) is parallel to \(\mathbf{v}\) and they have the same direction. Furthermore, \(\overrightarrow{OQ}\) has length \(\quantity{1}{m}\) and \(\mathbf{v}\) has magnitude \(\quantity{1}{m\,s^{-1}}\), so geometrically \(\overrightarrow{OQ}=\mathbf{v}\). Therefore we can think of \(\mathbf{v}\) as a translation of \(\overrightarrow{OQ}\). We know how to find the coordinates of \(Q\), because it is a point on the circle, so this will help us to express \(\mathbf{v}\) in terms of \(t\).

\(Q\) has coordinates \((\cos (t+\tfrac{\pi}{2}), \sin(t+\tfrac{\pi}{2}))\) because \(OQ\) is a rotation of \(OP\) anticlockwise through \(\quantity{\tfrac{\pi}{2}}{rad}\). Therefore we can write \(\mathbf{v}= (\cos (t+\tfrac{\pi}{2}), \sin(t+\tfrac{\pi}{2}))\).

What does the graph of \(\cos (t+\tfrac{\pi}{2})\) look like? What about the graph of \(\sin(t+\tfrac{\pi}{2})\)?

We chose to separate thinking about triangles from thinking about transforming vectors. You may have used a combination of these approaches. What do the approaches have in common? What different things do they tell you?

In the problem we were told that

Velocity is the rate of change of displacement, so its components are given by the rates at which its \(x\) and \(y\) coordinates are changing with respect to time. Therefore \[\mathbf{v}=\left( \dfrac{dx}{dt}, \dfrac{dy}{dt}\right).\]

The diagrams helped us to establish that at time \(\quantity{t}{s}\), \(x=\cos t\) and \(y=\sin t\) and therefore \(\mathbf{v}=\left( \dfrac{d}{dt}(\cos t), \dfrac{d}{dt}(\sin t)\right)\).

From the diagrams we also saw that \(\mathbf{v}\) can be written as \((-\sin t, \cos t)\). By equating the components in the two expressions for \(\mathbf{v},\) we obtain

\[\frac{d}{dt}(\cos t)= -\sin t \quad \text{and}\quad \frac{d}{dt}(\sin t)=\cos t.\]

But from the diagrams we also saw that \(\mathbf{v}\) could be written as \((\cos (t+\tfrac{\pi}{2}), \sin(t+\tfrac{\pi}{2}))\), which gives a way of thinking about the derivatives of \(\cos t\) and \(\sin t\) as rotations through \(\tfrac{\pi}{2}\),

\[\frac{d}{dt}(\cos t)= \cos \left(t+\frac{\pi}{2}\right) \quad \text{and}\quad \frac{d}{dt}(\sin t)= \sin\left(t+\frac{\pi}{2}\right).\]

What do these ideas tell you about the acceleration of \(P\) at time \(\quantity{t}{s}\)?
