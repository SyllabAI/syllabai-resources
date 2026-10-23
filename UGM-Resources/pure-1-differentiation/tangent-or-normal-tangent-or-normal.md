---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/tangent-or-normal
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/package-of-problems
- level/developing
resource_identity:
  ugm_id: tangent-or-normal
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 5
  resource_type_label: Package of problems
  level: Developing
  ref: 5249
  old_site_id: C2_RT7_1
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-of-powers
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-of-powers
    validation_status: SUGGESTED
  spec_points:
  - code: 1.7.3
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: match tangent/normal line pairs then recover curves from gradient functions — perpendicular-gradient
        structure (curve recovery carries a recorded 1.8 reverse bearing)
      rationale: 'Canonical UGM title: "Tangent or normal"'
      validation_status: SUGGESTED
    title: apply differentiation to gradients, tangents and normals, increasing and decreasing functions
      and rates of change
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-7
assets:
- path: https://undergroundmathematics.org/calculus-of-powers/tangent-or-normal/components/cards-single.pdf
  kind: printable
- path: https://undergroundmathematics.org/calculus-of-powers/tangent-or-normal/components/cards.pdf
  kind: printable
- path: https://undergroundmathematics.org/calculus-of-powers/tangent-or-normal/download/teacher-notes.pdf
  kind: printable
---

# Tangent or normal

> Excerpt: This structured activity starts with matching straight lines in pairs that could be tangents and normals, and leads on to finding the equations of corresponding curves given a set of gradient functions.

## Warm-up

Below are eight equations of straight line graphs.

- Which lines are perpendicular to each other?

- Can you find the coordinates of the point where each pair of perpendicular lines intersects?

\(y-x-2=0\)

\(y-3x-2=0\)

\(3y+x-6=0\)

\(16y+2x+31=0\)

\(y-8x+6=0\)

\(2y-x-3=0\)

\(y+x+2=0\)

\(y+2x+1=0\)

## Tangent or normal

We have now sorted the straight line equations from the [Warm-up](https://undergroundmathematics.org/calculus-of-powers/tangent-or-normal/) section into pairs of lines which are perpendicular.

- \(2y-x-3=0\) and \(y+2x+1=0\), intersecting at \((-1,1)\)

- \(y-3x-2=0\) and \(3y+x-6=0\), intersecting at \((0,2)\)

- \(y-8x+6=0\) and \(16y+2x+31=0\), intersecting at \(\bigl(\frac{1}{2},-2 \bigr)\)

- \(y+x+2=0\) and \(y-x-2=0\), intersecting at \((-2,0)\)

Each of these pairs of lines are the tangent and normal lines to a different curve at a point. Below are the gradient functions (derivatives) for each of the original curves.

1. \(2x+5\)

---

1. \(15x^2+12x+3\)

---

1. \(\dfrac{-2}{x^2}\)

---

1. \(24x^2-8x+6\)

1. Can you determine which of these gradient functions (derivatives) corresponds to each pair of tangent and normal lines given above?

---

1. For each pair, can you determine which of the straight lines is the tangent and which is the normal?

## Original curves

Now that we have discovered which one of each pair of lines is the tangent line and which is the normal, can we recover the original curve that each gradient function (derivative) came from?

1. \(2x+5\)

---

1. \(15x^2+12x+3\)

---

1. \(\dfrac{-2}{x^2}\)

---

1. \(24x^2-8x+6\)

In each case can you find the equation of the curve which has the given gradient function and the previously matched tangent and normal lines?

## Solution (Tangent or normal)

Let’s take the first pair of lines, \(2y-x-3=0\) and \(y+2x+1=0\). We know that the gradients of the lines are \(\frac{1}{2}\) and \(-2\) respectively and that they intersect at the point \((-1,1)\).

At the point where the tangent and normal intersect, the curve must have the same gradient as the tangent line. So if we substitute \(x=-1\) into each gradient function we should find one with a value of either \(\frac{1}{2}\) or \(-2\).

1. \(2\times (-1)+5=3\)

---

1. \(15\times(-1)^2+12\times(-1)+3=0\)

---

1. \(\dfrac{-2}{(-1)^2}=-2\)

---

1. \(24(-1)^2-8\times(-1)+6=38\)

We can see that gradient function (3) matches, so the line \(y+2x+1=0\) is the tangent line and the other is the normal line at \((-1,1)\) to the curve. The gradient function is \(\dfrac{-2}{x^2}\).

| Normal: \(2y-x-3=0\) | Tangent: \(y+2x+1=0\) | Gradient function (3): \(\dfrac{-2}{x^2}\) |
|---|---|---|

We can follow the same ideas through for the remaining pairs of lines and gradient functions to get.

| Tangent: \(y-3x-2=0\) | Normal: \(3y+x-6=0\) | Gradient function (2): \(15x^2+12x+3\) |
|---|---|---|

| Tangent: \(y-8x+6=0\) | Normal: \(16y+2x+31=0\) | Gradient function (4): \(24x^2-8x+6\) |
|---|---|---|

| Normal: \(y+x+2=0\) | Tangent: \(y-x-2=0\) | Gradient function (1): \(2x+5\) |
|---|---|---|

## Solution (Original curves)

In each case can you find the equation of the curve which has the given gradient function and the previously matched tangent and normal lines?

We know the gradient function for each curve and since we know the point where the tangent and normal lines meet, we know a point on the curve.

If we have a gradient function of \(6x^2\), is it possible to find the original function for the curve?

If we start with a function of \(x\) and differentiate we get the gradient function for that curve. Can we go back?

If we end up with \(6x^2\) we must have started with \(x^3\) as our power of \(x\), but if we differentiate \(x^3\) with respect to \(x\) we get \(3x^2\). Therefore, we could have started with \(2x^3\).

What happens to \(2x^3+4\) when you differentiate with respect to \(x\)?

Let us go back to our first example, pair one. We have matched up the tangent \(y+2x+1=0\) with the normal \(2y-x-3=0\) to the curve with gradient function \(\dfrac{-2}{x^2}\) at the point \((-1,1)\).

If we start with the gradient function, the function for the curve we started with must end up in this form. Since we end up with \(\dfrac{-2}{x^2}\) we should have started with \(2x^{-1}\) for our power of \(x\).

How do we know this? What happens when we differentiate \(x^{-1}\) with respect to \(x\)?

However, we know that constants when differentiated go to zero, so the most general form we could have started with for this function is \(y=\dfrac{2}{x}+c\), where is \(c\) is real number.

How can we find this constant \(c\)?

From our work with the tangent and normal lines, we know a point on the curve (the point where the tangent and normal lines meet), \((-1,1)\).

Therefore, when \(x=-1\), \(y=\dfrac{2}{(-1)}+c=1\) and so \(-2+c=1\), giving \(c=3\). This tells us that the original function we started with is \(y=\dfrac{2}{x}+3\).

We can do the same for each of the pairs of lines and their intersection points giving the original curves as:

1. \(y=x^2+5x+6\) for the gradient function \(2x+5\).

---

1. \(y=5x^3+6x^2+3x+2\) for the gradient function \(15x^2+12x+3\).

---

1. \(y=\dfrac{2}{x}+3\) for the gradient function \(\dfrac{-2}{x^2}\).

---

1. \(y=8x^3-4x^2+6x-5\) for the gradient function \(24x^2-8x+6\).
