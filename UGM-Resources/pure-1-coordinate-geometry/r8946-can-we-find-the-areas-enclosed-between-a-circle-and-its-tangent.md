---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/circles/r8946
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- circles
- type/review-question
resource_identity:
  ugm_id: r8946
  station: circles
  station_title: Circles
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8946
  old_site_id: Q1055
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
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'tangent-line equation and areas A(theta), B(theta) — the line/tangent parts are 1.3.2; the area parts ride trig/radians (recorded medium).'
      rationale: 'Canonical UGM title: “Can we find the areas enclosed between a circle and its tangent?”; exam provenance: Oxford (MAT) 2007 Q4'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford (MAT) 2007 Q4
task: T-UGM-IMPORT-3
---

# Can we find the areas enclosed between a circle and its tangent?

## Question

In the diagram below is sketched the circle with centre \((1,1)\) and radius \(1\) and a line \(L\). The line \(L\) is tangential to the circle at \(Q\). Further, \(L\) meets the \(y\)-axis at \(R\), and the \(x\)-axis at \(P\) in such a way that the angle \(OPQ\) equals \(\theta\) where \(0<\theta<\dfrac{\pi}{2}\).

1. Show that the co-ordinates of \(Q\) are \[(1+ \sin \theta, 1 + \cos \theta),\] and that the gradient of \(PQR\) is \(- \tan \theta\). Write down the equation of the line \(PQR\) and so find the co-ordinates of \(P\).

---

1. The region bounded by the circle, the \(x\)-axis and \(PQ\) has area \(A(\theta)\); the region bounded by the circle, the \(y\)-axis and \(QR\) has area \(B(\theta)\). (See diagram.) Explain why \[A(\theta) = B\left(\dfrac{\pi}{2} - \theta\right)\] for any \(\theta\). Calculate \(A\left(\dfrac{\pi}{4}\right)\).

---

1. Show that \[A \left(\dfrac{\pi}{3} \right) = \sqrt{3} - \dfrac{\pi}{3}.\]

## Suggestion

Could we add the radius of the circle which meets the tangent to the diagram? What angles do we know now?

If we draw two diagrams, one with angle \(\theta\) at \(P\), and the other with angle \(\left(\dfrac{\pi}{2} - \theta\right)\) at \(P\), then what do we notice?

Interactive diagram

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/Dd5JWgdE)

The angle \(\angle OPQ=\theta\) can be varied using the slider.

The values of \(A(\theta)\) and \(B(\theta)\) are indicated by the height of the bars on the right.

Could we sketch a new diagram with \(\theta=\dfrac{\pi}{4}\)? Can we calculate the length \(OP\)?

1. Show that \[A \left(\frac{\pi}{3} \right) = \sqrt{3} - \frac{\pi}{3}.\]

Could we sketch a new diagram with \(\theta=\dfrac{\pi}{3}\)?

Maybe \(A \left(\dfrac{\pi}{3} \right)\) could be found by finding the area of two right-angled triangles and subtracting part of the area of the circle?

## Solution

We know the centre of the circle is at \((1,1)\).

From the diagram, we can see that to get from the centre, \(C\), to the point \(Q\) we must travel “\(\sin\theta\)” horizontally and “\(\cos\theta\)” vertically, so

\[Q= \quad (1 + \sin\theta, 1 + \cos\theta).\]

If we now let the length of

\(PQR = \ell\)

, then

\[\begin{align*} \text{gradient of } PQR &= \frac{\text{change in }y}{\text{change in }x} \\ &= \frac{-\ell\sin\theta}{\ell\cos\theta} \\ &= - \tan\theta, \qquad \text{as required.} \end{align*}\]

Alternatively, we could find the gradient of the radius to \(Q\) and (because we know the radius and tangent are perpendicular) we can then find the gradient of the tangent \(PQR\).

The gradient of \(CQ\) is \(\dfrac{\cos\theta}{\sin\theta}\) (the change in \(y\) values \(\div\) the change in \(x\) values). The product of perpendicular gradients is \(-1\).

The tangent

\(PQR\)

is perpendicular to the radius, therefore:

\[\begin{align*} \frac{\cos\theta}{\sin\theta} \times m &= -1, \\ \implies m &= -\frac{\sin\theta}{\cos\theta} \\ &= - \tan\theta, \qquad \text{as required.} \end{align*}\]

The line \(PQR\) has gradient \(-\tan\theta\) and goes through the point \((1 + \sin\theta, 1 + \cos\theta)\), and so has equation

\[y - (1 + \cos\theta) = -\tan\theta (x - (1 + \sin\theta)).\]

We’re not asked to give the equation of the line in any particular form, so we can leave it as is.

At the point

\(P\)

we know

\(y=0\)

. Substituting this value into the equation of the line we find

\[\begin{align*} -(1 + \cos\theta) &= -\tan\theta (x - (1 + \sin\theta)) \\ \implies 1 + \cos\theta &= \tan\theta (x - (1 + \sin\theta)) \\ \implies \frac{1 + \cos\theta}{\tan\theta} &= x - (1 + \sin\theta) \\ \implies x &= 1 + \sin\theta + \frac{1 + \cos\theta}{\tan\theta}. \end{align*}\]

We could, if desired, simplify this answer:

\[\begin{align*} x &= 1 + \sin\theta + \frac{1}{\tan\theta} + \frac{\cos\theta}{\tan\theta} \\ &= 1 + \sin\theta + \cot\theta + \frac{\cos^2{\theta}}{\sin\theta} \\ &= 1 + \frac{\sin^2{\theta}}{\sin\theta} + \cot\theta + \frac{\cos^2{\theta}}{\sin\theta} \\ &= 1 + \frac{\left(\sin^2{\theta} + \cos^2{\theta} \right)}{\sin\theta} + \cot\theta \\ &= 1 + \frac{1}{\sin\theta} + \cot\theta \\ &= 1 + \cosec\theta + \cot\theta. \end{align*}\]

If we’d looked at our diagram carefully, we could’ve arrived at the same answer:

Using \(\tan \theta = \dfrac{\text{opposite}}{\text{adjacent}}\), we see \(TP = \dfrac{1 + \cos\theta}{\tan\theta}\), and so

\[x = 1 + \sin\theta + \frac{1 + \cos\theta}{\tan\theta}.\]

Therefore the co-ordinates of \(P\) are \((1 + \cot \theta + \mathrm{cosec \hspace{1mm}} \theta, 0)\).

1. The region bounded by the circle, the \(x\)-axis and \(PQ\) has area \(A(\theta)\); the region bounded by the circle, the \(y\)-axis and \(QR\) has area \(B(\theta)\). (See diagram.) Explain why \[A(\theta) = B\left(\frac{\pi}{2} - \theta\right)\] for any \(\theta\).

Let’s draw two diagrams - one with angle \(\theta\) at \(P\) and the other with angle \(\dfrac{\pi}{2} - \theta\) at \(P\):

We can see simply from the symmetry of the diagrams that \(A(\theta) = B\left(\dfrac{\pi}{2} - \theta\right)\).

To calculate \(A\left(\dfrac{\pi}{4}\right)\), let’s draw the diagram and see if it might help us.

By symmetry, we see that \[A\left(\dfrac{\pi}{4}\right) = B\left(\dfrac{\pi}{4}\right).\]

Next, we need to know the lengths \(OP\) and \(OR\) of the triangle \(OPR\).

Using our final answer from (i), we have

\[\begin{align*} OP &= 1 + \frac{1}{\sin \dfrac{\pi}{4}} + \dfrac{\cos \dfrac{\pi}{4}}{\sin \dfrac{\pi}{4}} \\ &= 1 + \sqrt{2} + 1 \\ &= 2 + \sqrt{2}. \end{align*}\]

Our triangle is isosceles, since both the angle at \(P\) and the angle at \(R\) are \(\dfrac{\pi}{4}\), so we have \(OR = OP\) and \[OR = 2 + \sqrt{2} \qquad \text{also.}\]

Now we can calculate the area of the whole triangle \(OPR\).

The area of triangle

\(OPR\)

is

\[\frac{1}{2}(2 + \sqrt{2})^2\]

which simplifies to

\[\begin{align*} \frac{1}{2} (4& + 4\sqrt{2} + 2) \\ &= \frac{1}{2} (6 + 4\sqrt{2}) \\ &= 3 + 2\sqrt{2}. \end{align*}\]

The shaded area in the diagram below is made up of a square of side length \(1\), and \(\dfrac{3}{4}\) of the circle (of radius \(1\)).

The shaded area is therefore: \[1 \times 1 + \frac{3}{4} \times \pi \times (1)^2 \qquad = \qquad 1 + \frac{3}{4} \pi.\]

The area of \(A\left(\dfrac{\pi}{4}\right)\) can now be found. We have

\[\begin{align*} A\left(\frac{\pi}{4}\right) &= \frac{1}{2} \left(\text{area of triangle }OPR - \text{shaded area} \right) \\ &= \frac{1}{2} \left(3 + 2\sqrt{2} - (1 + \frac{3\pi}{4}) \right) \\ &= \frac{1}{2} \left(2 + 2\sqrt{2} - \frac{3\pi}{4} \right) \\ &= 1 + \sqrt{2} - \frac{3\pi}{8}. \end{align*}\]

1. Show that \[A \left(\frac{\pi}{3} \right) = \sqrt{3} - \frac{\pi}{3}.\]

The length \(SP\) can be found from the triangle \(CSP\): we have

\[\begin{align*} \tan {\frac{\pi}{6}} &= \frac{CS}{SP} \\ \frac{1}{\sqrt{3}} &= \frac{1}{SP} \\ \text{so } \quad SP &= \sqrt{3}. \end{align*}\]

Therefore the area of triangle \(CSP\) is \[\frac{1}{2} \times 1 \times \sqrt{3} \quad = \quad \frac{\sqrt{3}}{2}.\]

By symmetry, the area of triangle \(CQP\) is also \(\dfrac{\sqrt{3}}{2}\).

The area of the sector \(CQS\) is \[\frac{1}{3} \times \pi \times (1)^2 \quad = \quad \frac{1}{3} \pi.\]

Therefore we can now find the area \(A\left(\dfrac{\pi}{3}\right)\): we have

\[\begin{align*} A\left(\frac{\pi}{3}\right) &= \text{area of triangle } CSP + \text{area of triangle } CQP - \text{area of sector } CQS \\ &= \frac{\sqrt{3}}{2} + \frac{\sqrt{3}}{2} - \frac{\pi}{3} \\ &= \sqrt{3} - \frac{\pi}{3}, \qquad \text{as required.} \end{align*}\]
