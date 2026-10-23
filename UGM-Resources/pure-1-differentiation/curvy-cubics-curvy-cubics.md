---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-meets-functions/curvy-cubics
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-meets-functions
- type/investigation
- level/developing
resource_identity:
  ugm_id: curvy-cubics
  station: calculus-meets-functions
  station_title: Calculus meets Functions
  resource_type_id: 7
  resource_type_label: Investigation
  level: Developing
  ref: 7457
  old_site_id: F5_RT1_1
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-meets-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-meets-functions
    validation_status: SUGGESTED
  spec_points:
  - code: 1.7.2
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: form equations for four sketched cubics — roots plus stationary-point structure; the
        calculus hint for curve C is explicit
      rationale: 'Canonical UGM title: "Curvy cubics"'
      validation_status: SUGGESTED
    title: use the derivative of x (for any rational n ), together with constant multiples, sums and
      differences of functions, and of composite functions using the chain rule
  - code: 1.7.4
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: form equations for four sketched cubics — roots plus stationary-point structure; the
        calculus hint for curve C is explicit
      rationale: 'Canonical UGM title: "Curvy cubics"'
      validation_status: SUGGESTED
    title: locate stationary points and determine their nature, and use information about stationary
      points in sketching graphs.
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-7
assets:
- path: https://undergroundmathematics.org/calculus-meets-functions/curvy-cubics/download/teacher-notes.pdf
  kind: printable
---

# Curvy cubics

> Excerpt: Students are asked to investigate what the equations of four somewhat different cubic functions could be.

## Cubic curves

What gives a cubic curve its curves?

Below are four cubic curves.

Can you form an equation for each?

What does the curve tell you about the properties of the cubic polynomial?

## Curves $A$, $B$ and $D$

How many pieces of information do we need to determine a straight line? How many pieces of information are needed to determine a quadratic? How many pieces of information are we looking for here in order to determine a cubic?

From previous knowledge about curves and their intersections with the \(x\)-axis we can say quite a lot about the form their equations might take.

Curve \(A\)

From looking at curve \(A\), the orange curve, we see it passes through the points \((-2,0)\), \((-1,0)\) and \((1,0)\). Just as we saw in [Can you find… cubic edition](https://undergroundmathematics.org/polynomials/can-you-find-cubic-edition), this means we have an equation for this cubic of the form,

\[y=a(x+2)(x+1)(x-1).\]

We can determine \(a\) by looking at any point on the curve that is not on the \(x\)-axis. In this case we can choose the \(y\)-intercept (when \(x=0\)). This gives \(a=1\).

Here we needed to use four pieces of information to determine an equation of the cubic curve. Do we ever need more than four pieces of information about any cubic to determine an equation for it?

What would the derivative of this function look like and what does that tell us about the shape of the curve?

Curve \(D\)

From our knowledge of roots and transformations of cubic curves, curve \(D\), the black curve, looks like a translation of \(y=x^3\) to \(y=(x-1)^3\).

The equation \(y=(x-1)^3\) looks right but we can test to make sure by substituting \(x=0\) into the equations and locating the \(y\)-intercept of curve \(D\).

What would the derivative of this function look like and what does that tell us about the shape of the curve?

Curve \(B\)

From looking at curve \(B\), the blue curve, it passes through the point \((0,0)\) and touches the \(x\)-axis at \((-1,0)\). Just as we saw in [Can you find… cubic edition](https://undergroundmathematics.org/polynomials/can-you-find-cubic-edition), this means we have an equation for this cubic of the form,

\[y=bx(x+1)^2.\]

We can determine \(b\) by looking at a point on the curve. When \(x=1\), \(y=4\) and so \(b=1\).

What would the derivative of this function look like and what does that tell us about the shape of the curve?

## Curve $C$ - how can calculus help?

Curve \(C\), the red curve, does not look like one of the typical cubic shapes we have seen before. However, it has rotational symmetry about \((0,1)\).

It has some similarities to the curve \(y=x^3+1\) but it does not have the same key feature at \(x=0\).

What are the features of this curve compared to \(y=x^3\) or a translation of it?

A possible response

Curve \(C\) intersects the \(x\)-axis once and the \(y\)-axis at \((0,1)\).

As the value for \(x\) increases, the value for \(y\) increases.

However, it does not appear to have the same shape as the \(y=x^3+1\) curve at the point \((0,1)\).

We could try to form a set of simultaneous equations to find a cubic equation, but would this be an efficient way to find an equation?

**Calculus of curve \(C\)**

The curve has no stationary points.

If a cubic curve given by a function \(y=g(x)\) has no stationary points then what do we know about \(g'(x)\)?

A possible response

We know that the equation \(g'(x)=0\) has no real solutions. Since \(g(x)\) is a cubic function, \(g'(x)\) will be a quadratic expression that forms an equation \(g'(x)=0\) with no real solutions.

So we can use our knowledge of calculus and quadratic equations to help construct a cubic curve with the same properties as curve \(C\).

A possible red curve equation

We know that the quadratic equation \(x^2+1=0\) has no real solutions, so we could take \(g'(x)=x^2+1\).

Using integration we find that \(g(x)=\dfrac{1}{3}x^3+x+k\), where \(k\) is an arbitrary constant.

We could therefore choose \(y=\dfrac{1}{3}x^3+x+1\) as our cubic curve equation, since the curve \(C\) cuts the \(y\)-axis at \(y=1\).

Is this an equation of curve \(C\)? We may need to manipulate \(y=\dfrac{1}{3}x^3+x+1\) so that it goes through the points \((-1,-2)\) and \((1,4)\) as the curve \(C\) does.

Have a look back at where the coefficients for your cubic have come from. Can we alter the coefficients without the argument above breaking down?

After using this resource you could take a look at [Can you find… curvy cubics edition](https://undergroundmathematics.org/calculus-meets-functions/can-you-find-curvy-cubics).
