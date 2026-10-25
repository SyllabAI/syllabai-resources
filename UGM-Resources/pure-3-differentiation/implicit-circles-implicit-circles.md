---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/implicit-circles
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/many-ways-problem
resource_identity:
  ugm_id: implicit-circles
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 4
  resource_type_label: Many ways problem
  level: Introducing
  ref: 5027
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
      evidence: gradient of x^2 + y^2 = 4 at three points and at a general point - implicit differentiation
        dy/dx = -x/y with the radius-gradient alternative, the canonical 3.4.3 implicit introduction
      rationale: 'Canonical UGM title: Implicit circles'
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

# Implicit circles

> Excerpt: Students are asked to find the gradient of three points on the graph of a circle, thinking about different ways to solve this problem. The specific problem is then generalised as a way of introducing implicit differentiation.

## Problem

Find the gradient of the curve \(x^2+y^2=4\) at the following three points.

What is the derivative, \(\dfrac{dy}{dx}\), at a general point on the curve?

Next step

What is the derivative at a general point on *this* curve?

Can you use the same methods as above?

## Things you might have done

There are different ways we could think about finding the gradient of a circle at a point.

Geometric approach

| The gradient of the curve is the same as the gradient of the tangent at that point, and we know that the tangent to a circle is perpendicular to the radius. The radius through \(\left(\sqrt{2},\sqrt{2}\right)\) is part of the line \(y=x\) . So the tangent is the line \(y=-x+c\) . We don’t need to find \(c\) as we just want the gradient, which is \(-1\) . |  |
|---|---|
| We don’t need to find the equations of the radius and tangent, we can just think about their gradients. At the point \(\left(-\sqrt{3},1\right)\) the gradients are \[m_\text{radius} = \dfrac{1}{-\sqrt{3}} \text{ and } m_\text{tangent} = \dfrac{\sqrt{3}}{1}.\] |  |

Differentiation

We could differentiate the equation of our curve to find the gradient at \(x = \frac{1}{2}\).

The difficulty is that we do not have an equation in the form \(y = f(x)\). Can we rearrange it?

\[\begin{align*} x^2+y^2 &= 4 \\ y^2 &= 4 - x^2 \\ y &= \pm\sqrt{4-x^2} \end{align*}\]

This final line causes problems as there are two options for the square root. How might we proceed from here?

Given that we have a specific point, \(\left(\frac{1}{2}, -\frac{\sqrt{15}}{2}\right)\), we know we want the negative square root as our value of \(y\) is negative. Therefore we could differentiate \(y = -\sqrt{4-x^2}\) using the [chain rule](https://undergroundmathematics.org/glossary/chain-rule) to get \[\dfrac{dy}{dx} = -\frac{1}{2} (4-x^2)^{-1/2} \cdot(-2x) = \frac{x}{\sqrt{4-x^2}}.\] At \(x = \frac{1}{2}\) this gives us a gradient of \(\frac{1}{\sqrt{15}}\).

Notice that our expression for \(\frac{dy}{dx}\) is undefined for \(x=\pm 2\) and for \(\big|x\big|>2\). But here we are only interested in \(x = \frac{1}{2}\).

What is the derivative at a general point on the curve?

Again, we can tackle this in a number of different ways.

Geometric approach

We see that the gradient of the radius at \((x,y)\) is \(\dfrac{y}{x}\).

As the tangent is perpendicular to the radius, the gradient of the curve at that point will be \(\dfrac{-1}{y/x}\) or \(-\dfrac{x}{y}\).

Would it matter if our point was in a different quadrant?

Rearranging the equation

If we rearrange the equation, we get \(y = \pm\sqrt{4-x^2}\) as above. The two cases make this slightly awkward, but we can treat them separately.

If \(y = +\sqrt{4-x^2}\) then using the chain rule we have \[\frac{dy}{dx}=\frac{\frac{1}{2}}{\sqrt{4-x^2}}(-2x) = \frac{\frac{1}{2}(-2x)}{y} = -\frac{x}{y}.\]

Whereas, if \(y = -\sqrt{4-x^2}\) we have \[\frac{dy}{dx}=-\frac{\frac{1}{2}}{\sqrt{4-x^2}}(-2x) = \frac{\frac{1}{2}(-2x)}{y} = -\frac{x}{y}.\]

So for each case we get the same result as above.

Notice that something strange happens in between the two cases, at \(y=0\).

Differentiating directly

What happens if instead we differentiate the original equation \(x^2 + y^2 = 4\) directly?

Differentiating both sides we get \[\dfrac{d}{dx}\left(x^2+y^2 \right) = \dfrac{d}{dx}\left(4\right)\] which is the same as \[\dfrac{d}{dx}\left(x^2\right) + \dfrac{d}{dx}\left(y^2\right) = \dfrac{d}{dx}\left(4\right)\] and therefore \[2x + \dfrac{d}{dx}\left(y^2\right) = 0.\]

This in itself is not very helpful, but if we define \(u=y^2\) we can then use the chain rule. \[\dfrac{d}{dx}\left(y^2\right) = \frac{du}{dx} = \frac{du}{dy}\cdot\frac{dy}{dx} = 2y\frac{dy}{dx}\] This *is* useful because now we have an expression involving the gradient of the curve.

This works because, even though we could not write \(y\) as a function of \(x\), if you look at just the part of the curve near a given point, \(y\) and \(u\) *are* functions of \(x\) and the gradients do have sensible meanings.

<cm-chalk> We can differentiate the $x^2$ and the $4$, but how do we differentiate the $y^2$ term with respect to $x$? </cm-chalk> Although we can't write $x^2 + y^2 = 4$ explicitly in the form $y = f(x)$, $y$ is still related to $x$. This is what is called an <cm-glossary text="implicit equation" reference="implicit-equation" />. We can think of $y$ as a function of $x$ that is unknown. That means the $y^2$ term can be thought of as some function of $x$ squared, i.e. $[f(x)]^2$. This is a composite function in $x$ that can be differentiated by the chain rule. Differentiating $[f(x)]^2$ using the chain rule gives us $2f(x)\cdot f'(x)$. If we use the notation of $y^2$ we would write the derivative as $2y \cdot \dfrac{dy}{dx}$. <cm-chalk> Can you see that these two different ways of writing the derivative are the same? </cm-chalk>

What we have done is called *implicit differentiation* and means that when we differentiate \(x^2 + y^2 = 4\) we get

\[2x + 2y\dfrac{dy}{dx} = 0.\]

We can now rearrange to find \(\dfrac{dy}{dx} = -\dfrac{x}{y}\), the same as we had from the other approaches.

You might notice that the gradient function is in terms of both \(x\) and \(y\). This makes sense because for each value of \(x\), there may be two points on the curve, each of which has a different \(y\) and different gradient.

You might check this result by substituting the coordinates given earlier to make sure we get the same gradients.

What happens when \(y = 0\)? What does this mean geometrically on the circle?

In this case, we had a choice of three methods, but for many other curves the first two approaches do not work and implicit differentiation becomes a valuable tool.

The first approach above relied on the geometry of the circle. It used the fact that a tangent to a circle is at right-angles to the radius. Is this true for an ellipse? Imagine your ellipse as a circle that has been stretched in one direction. What happens to the angle between the tangent and the radius?

Here we will differentiate implicitly.

\[\begin{align*} \dfrac{d}{dx}\left(9x^2 + 16y^2 \right) &= \dfrac{d}{dx}(144) \\ 18x + 32y\frac{dy}{dx} &= 0 \end{align*}\]

We can rearrange to find the gradient.

\[\begin{align*} \dfrac{dy}{dx} &= -\dfrac{18x}{32y} \\ &= -\dfrac{9x}{16y} \end{align*}\]
