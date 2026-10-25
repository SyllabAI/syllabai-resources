---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/r9413
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/review-question
resource_identity:
  ugm_id: r9413
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9413
  old_site_id: Q1032
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
      evidence: normal to x = n cos t - cos nt, y = n sin t - sin nt proved as x cos((n+1)t/2) + y sin((n+1)t/2)
        = (n-1) cos((n-1)t/2) - the chain-rule composites cos nt, sin nt inside the parametric derivative
        (flips the lane-11 non-overlap row of record routed 'P3 3.4 Differentiation')
      rationale: 'Canonical UGM title: Can we show that these normals intersect on this circle?'
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

# Can we show that these normals intersect on this circle?

## Question

Prove that the equation of the normal at a point of the curve \[x=n\cos t-\cos nt,\qquad y=n\sin t-\sin nt,\] where \(n\) is an integer greater than unity, is \[x\cos \frac{n+1}{2}t + y\sin \frac{n+1}{2}t=(n-1)\cos \frac{n-1}{2}t.\] Show that, if \(n\) is an even integer, the normals at the points \(t\) and \(t+\pi\) are perpendicular and intersect on the circle \[x^2+y^2=(n-1)^2.\]

## Suggestion

How do we calculate the gradient when \(x\) and \(y\) are given parametrically? How do we then calculate the gradient of the normal?

The equation we are aiming for is written in terms of

\(\dfrac{n\pm 1}{2}t\)

which suggests that the following identities might be useful:

\[\begin{align*} \sin a-\sin b&= 2\sin\left(\frac{a-b}{2}\right)\cos\left(\frac{a+b}{2}\right)\\ \cos a-\cos b&= 2\sin\left(\frac{a+b}{2}\right)\sin\left(\frac{b-a}{2}\right) \\ \cos a \cos b&= \frac{1}{2}\cos(a-b)+\frac{1}{2}\cos(a+b) \\ \sin a \sin b&= \frac{1}{2}\cos (a-b) -\frac{1}{2}\cos(a+b) \end{align*}\]

This applet illustrates what is described here. Use the sliders to vary \(t\) and try different values of \(n\).

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/NBCpEbbu/width/800/height/600/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/NBCpEbbu)

How would we show that two lines are perpendicular?

You might find it helpful to define a shorthand such as \(A=\dfrac{n+1}{2}t\) and \(P=\dfrac{n+1}{2}\pi\).

We could write down the equations of the two normals from the first part of the question. What might we need to do to them to get them in the form of the required circle equation?

## Solution

First we need the gradient of the curve and from that the gradient of the normal. We use the [chain rule](https://undergroundmathematics.org/glossary/chain-rule) to differentiate the [parametric equation](https://undergroundmathematics.org/glossary/parametric-equations).

We have that

\[ x=n\cos t-\cos nt, \]

so

\[ \frac{dx}{dt}=-n\sin t+n\sin nt \]

and

\[ y=n\sin t-\sin nt, \]

so

\[ \frac{dy}{dt}=n\cos t-n\cos nt. \]

Now we could find the gradient of the curve since

\[ \frac{dy}{dx}=\frac{dy}{dt}\frac{dt}{dx}=\frac{\frac{dy}{dt}}{\frac{dx}{dt}}. \]

The form for the answer we are trying to prove is quite different, so it’s worth having a think before ploughing on.

We notice that the form of the answer contains arguments of \(\frac{n+1}{2}t\) or \(\frac{nt+t}{2}\) which points us toward the following identities

\[\begin{align} \sin a-\sin b&= 2\sin\left(\frac{a-b}{2}\right)\cos\left(\frac{a+b}{2}\right)\label{trig1} \\ \cos a-\cos b&= 2\sin\left(\frac{a+b}{2}\right)\sin\left(\frac{b-a}{2}\right) \label{trig2} \\ \cos a \cos b&= \frac{1}{2}\cos(a-b)+\frac{1}{2}\cos(a+b) \label{trig3} \\ \sin a \sin b&= \frac{1}{2}\cos (a-b) -\frac{1}{2}\cos(a+b) \label{trig4} \end{align}\]

Alternatively, we could use the more familiar compound angle identities. Then some slightly different algebra would lead to the same result.

Applying identity \(\eqref{trig1}\), we have that \[\frac{dx}{dt}=2n\sin\left(\frac{n-1}{2}t\right)\cos\left(\frac{n+1}{2}t\right).\]

Applying identity \(\eqref{trig2}\) yields \[\frac{dy}{dt}=2n\sin\left(\frac{n+1}{2}t\right)\sin\left(\frac{n-1}{2}t\right).\]

and so

\[ \frac{dy}{dx}=\frac{2n\sin\left(\frac{n+1}{2}t\right)\sin\left(\frac{n-1}{2}t\right)}{2n\sin\left(\frac{n-1}{2}t\right)\cos\left(\frac{n+1}{2}t\right)}=\frac{\sin \left(\frac{n+1}{2}t\right)}{\cos \left(\frac{n+1}{2}t\right)}. \]

Therefore the gradient of the normal to the curve is

\[\begin{equation} -\frac{\cos \left(\frac{n+1}{2}t\right)}{\sin \left(\frac{n+1}{2}t\right)} \label{eq:grad-of-norm} \end{equation}\]

and the normal to the curve has equation

\[ y-\left( n\sin t -\sin nt \right)=-\frac{\cos \left(\frac{n+1}{2}t\right)}{\sin \left(\frac{n+1}{2}t\right)}\bigl(x-\left(n\cos t-\cos nt\right)\bigr). \]

Multiplying by

\(\sin\left(\frac{n+1}{2}t\right)\)

gives

\[ \sin\left(\frac{n+1}{2}t\right)y-\sin\left(\frac{n+1}{2}t\right)\left( n\sin t -\sin nt \right)=\quad \]

\[ \quad-\cos\left(\frac{n+1}{2}t\right)x+\cos\left(\frac{n+1}{2}t\right)\left(n\cos t-\cos nt\right) \]

and rearranging gives us

\[\begin{align*} \sin\left(\frac{n+1}{2}t\right)y+\cos\left(\frac{n+1}{2}t\right)x &= \sin\left(\frac{n+1}{2}t\right)\left( n\sin t -\sin nt \right) \\ &+\cos\left(\frac{n+1}{2}t\right)\left(n\cos t-\cos nt\right). \end{align*}\]

Multiplying out the brackets and applying identities

\(\eqref{trig3}\)

and

\(\eqref{trig4}\)

we find that

\[\begin{align*} \sin\left(\frac{n+1}{2}t\right)y+\cos\left(\frac{n+1}{2}t\right)x&=n\cos t\cos\left(\frac{n+1}{2}t\right)-\cos nt\cos\left(\frac{n+1}{2}t\right)\\ &\quad+n\sin t\sin\left(\frac{n+1}{2}t\right)-\sin nt\sin\left(\frac{n+1}{2}t\right) \\ &=\frac{n}{2}\left[\cos\left(\frac{n-1}{2}t\right)+\cos\left(\frac{n+3}{2}t\right)\right] \\ &\quad -\frac{1}{2}\left[\cos\left(\frac{n-1}{2}t\right)+\cos\left(\frac{3n+1}{2}t\right)\right] \\ &\quad +\frac{n}{2}\left[\cos\left(\frac{n-1}{2}t\right)-\cos\left(\frac{n+3}{2}t\right)\right] \\ &\quad -\frac{1}{2}\left[\cos\left(\frac{n-1}{2}t\right)-\cos\left(\frac{3n+1}{2}t\right)\right] \\ &=(n-1)\cos\left(\frac{n-1}{2}t\right), \end{align*}\]

which is exactly what we wanted.

Show that, if \(n\) is an even integer, the normals at the points \(t\) and \(t+\pi\) are perpendicular…

From \(\eqref{eq:grad-of-norm}\) we have that the gradient of the normal to the curve at \(t\) is \[m_N(t) = -\frac{\cos \left(\frac{n+1}{2}t\right)}{\sin \left(\frac{n+1}{2}t\right)}.\]

Let’s use a shorthand \(A=\dfrac{n+1}{2}t\) and \(P=\dfrac{n+1}{2}\pi\). Then we can write the gradients of the normals at \(t\) and \(t+\pi\) as \[m_N(t) = -\frac{\cos A}{\sin A} \quad\text{and}\quad m_N(t+\pi) = -\frac{\cos (A+P)}{\sin (A+P)}.\]

Multiplying these two gradients together (we hope to get

\(-1\)

) and then using identities

\(\eqref{trig3}\)

and

\(\eqref{trig4}\)

, we have

\[\begin{align*} m_N(t) \times m_N(t+\pi) &= \frac{\cos A \cos (A+P)}{\sin A \sin (A+P)} \\ &= \frac{\cos(-P)+\cos(2A+P)}{\cos(-P)-\cos(2A+P)} \end{align*}\]

Since \(n\) is an even integer, \(P=\frac{\pi}{2}, \frac{3\pi}{2}, \cdots\) so \(\cos(-P) = 0\). The fraction therefore cancels down, the product of the two gradients is indeed \(-1\) and the normals are perpendicular, as required.

The gradient of the curve at $t$ is $$ \tan\left(\frac{n+1}{2}t\right)=T. $$ Therefore, the gradient of the curve at $t+\pi$ is $$ \tan\left(\frac{n+1}{2}(t+\pi)\right). $$ We have that $$ \tan\left(\frac{n+1}{2}t+\frac{n+1}{2}\pi\right)=\frac{T+\tan\left(\frac{n+1}{2}\pi\right)}{1-T\tan\left(\frac{n+1}{2}\pi\right)}. $$

Here we have used the identity $$ \tan(a+b)=\frac{\tan a+\tan b}{1-\tan a\tan b}. $$

Since $n$ is even, we can write $n=2k$, and so we have that $$ \tan\left(\frac{n+1}{2}\pi\right)=\tan \left(k\pi +\frac{\pi}{2}\right)=\infty. $$ So we can write the gradient of the curve at $t+\pi$ as $$ \frac{\frac{T}{\tan\left(\frac{n+1}{2}\pi\right)}+1}{\frac{1}{\tan\left(\frac{n+1}{2}\pi\right)}-T}=-\frac{1}{T}. $$ Therefore the gradients to the curve at $t$ and $t+\pi$ are perpendicular, and therefore so are the normals to the curves.

…and intersect on the circle \[x^2+y^2=(n-1)^2.\]

Using our shorthand

\(A\)

and

\(P\)

from above and also defining

\(B=\dfrac{n-1}{2}t\)

, we can write the equations of the two normals as

\[\begin{align} x\cos A + y\sin A &= (n-1)\cos B \label{eq:n_t}\\ \text{and}\quad x\cos (A+P) + y\sin (A+P) &= (n-1)\cos (B+P-\pi) \label{eq:n_t+pi} \end{align}\]

The form of the equation of the circle we are aiming for implies that we want to square these equations, but first let’s expand the \((A+P)\) expressions.

Using the compound angle identities we have

\[\begin{align*} \cos(A+P) &= \cos A \cos P - \sin A \sin P = - \sin A \sin P \\ \sin(A+P) &= \sin A \cos P + \cos A \sin P = \cos A \sin P \\ \cos(B+P-\pi) &= \cos B \cos (P-\pi) - \sin B \sin(P-\pi) = \sin B \sin P \end{align*}\]

We have used the facts that \(\cos P = \cos(P-\pi)=0\) and \(\sin(P-\pi) = -\sin P\). Notice also that \(\sin P\) is either \(1\) or \(-1\) depending on the value of \(n\).

Equation

\(\eqref{eq:n_t+pi}\)

then becomes

\[\begin{align*} -x\sin A \sin P + y\cos A \sin P &= (n-1)\sin B \sin P \\ \implies\quad -x\sin A + y\cos A &= (n-1)\sin B \end{align*}\]

Squaring this equation and equation

\(\eqref{eq:n_t}\)

then adding the results we get

\[\begin{align*} x^2\sin^2 A + y^2\cos^2A-2xy\sin A\cos A &= (n-1)^2\sin^2 B \\ \text{and}\quad x^2\cos^2 A + y^2\sin^2A+2xy\sin A\cos A &= (n-1)^2\cos^2 B \\ \implies\quad x^2\left(\sin^2A+\cos^2A\right) + y^2\left(\cos^2A+\sin^2A\right) &= (n-1)^2\left(\sin^2B+\cos^2B\right) \\ \implies\quad x^2 + y^2 &= (n-1)^2 \end{align*}\]

as required.

This applet illustrates what is described here. Use the sliders to vary $t$ and try different values of $n$.
