---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/r6820
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/review-question
resource_identity:
  ugm_id: r6820
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6820
  old_site_id: Q1035
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
  - code: 1.7.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: minimise A^2 = 9V^2/(16x^2) + x^4 for the pyramid face — negative-power and quartic
        derivatives with a prove-the-minimum clause
      rationale: 'Canonical UGM title: "When is the area of a face of this pyramid a minimum?"; exam
        provenance: UCLES A level Mathematics 2 and Pure Mathematics 2, 1964, Q7'
      validation_status: SUGGESTED
    title: use the derivative of x (for any rational n ), together with constant multiples, sums and
      differences of functions, and of composite functions using the chain rule
  - code: 1.7.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: minimise A^2 = 9V^2/(16x^2) + x^4 for the pyramid face — negative-power and quartic
        derivatives with a prove-the-minimum clause
      rationale: 'Canonical UGM title: "When is the area of a face of this pyramid a minimum?"; exam
        provenance: UCLES A level Mathematics 2 and Pure Mathematics 2, 1964, Q7'
      validation_status: SUGGESTED
    title: locate stationary points and determine their nature, and use information about stationary
      points in sketching graphs.
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Mathematics 2 and Pure Mathematics 2, 1964, Q7
task: T-UGM-IMPORT-7
---

# When is the area of a face of this pyramid a minimum?

## Question

A pyramid of given volume \(V\) stands on a horizontal square base of edge \(2x\), and its vertex is vertically above the centre of the base. Show that the area \(A\) of a sloping triangular face is given by \[A^2=\frac{9V^2}{16x^2}+x^4,\] and prove that, as \(x\) varies, \(A\) is least when the face is equilateral.

## Suggestion

What is the formula for the volume of a pyramid?

Sketch a square based pyramid and label its height \(h\). Can we now find the area of one of the triangular faces?

Can we create any right-angled triangles where we can use Pythagoras?

…and prove that, as \(x\) varies, \(A\) is least when the face is equilateral.

Is minimising \(A^2\) the same as minimising \(A\)? How could we go about minimising \(A^2(x)\)?

Where is the stationary point of \(A^2?\)

How do we know the stationary point we’ve found is a minimum?

Can we show that for this value of \(x\) we have equilateral faces?

## Solution

A pyramid of given volume \(V\) stands on a horizontal square base of edge \(2x\), and its vertex is vertically above the centre of the base. Show that the area \(A\) of a sloping triangular face is given by \[A^2=\dfrac{9V^2}{16x^2}+x^4,\]

The volume \(V\) of a square based pyramid is \[V=\dfrac{1}{3}bh,\] where \(b\) is the area of the base and \(h\) is the height.

Where does this formula come from?

To see where this formula comes from (it holds for pyramids with any base, and cones too) consider a unit cube:

Now draw in the four diagonals from each of the pairs of opposite corners like this:

This makes six identical square based pyramids from each of the faces:

Each pyramid has a base of area one and is of height \(1/2\). Each one must also have a volume of \(1/6\), which is \(\dfrac{1}{3}bh\).

We can extend this for cubes of a different side length, and cuboids.

Our pyramid looks like this:

So we have \[V=\frac{1}{3}(2x)^2h.\]

We need to find the area of a sloping triangular face (which will be the same for all four faces, since the vertex is directly above the centre of the base).

For this, we need the height \(y\) of the face, which is related to \(h\) and \(x\) via \[y^2=h^2+x^2,\] which we can see from taking a vertical cross-section of the pyramid.

The area of the face is \(A=\frac{1}{2}(2x)y=xy\).

Therefore, \[A^2=x^2y^2=x^2(h^2+x^2)=x^2\left(\left(\frac{3V}{4x^2}\right)^2+x^2\right)=x^2\left(\frac{9V^2}{16x^4}+x^2\right)=\frac{9V^2}{16x^2}+x^4,\] as required.

…and prove that, as \(x\) varies, \(A\) is least when the face is equilateral.

We can say that \(A\) has a turning point if and only if \(A^2\) does, since we know \(A\) is positive and \(y=x^2\) is an increasing function for \(x > 0\).

If you know the Chain Rule for differentiating, you might think about \(\dfrac{d(A^2)}{dx} = 2A\dfrac{dA}{dx}\).

So considering \[\frac{d(A^2)}{dx}=4x^3+\frac{9V}{16}\frac{-2}{x^3}=4x^3-\frac{9V^2}{8x^3},\] we find stationary points when \(\dfrac{d(A^2)}{dx}=0.\) \[\Longrightarrow \qquad 4x^3-\frac{9V^2}{8x^3}=0 \qquad \Longrightarrow \qquad 32x^6=9V^2.\] There will be two real roots of this equation, one negative (which doesn’t interest us) and one positive, so there is one stationary point in the \(x>0\) region.

We know \[\frac{d(A^2)}{dx}=\frac{32x^6 - 9V^2}{8x^3},\] so if \(x\) increases slightly from \(\left(\dfrac{9V^2}{32}\right)^\frac{1}{6}\), then \(x^6\) increases slightly from \(\dfrac{9V^2}{32}\), (since \(y = x^6\) is an increasing function for \(x > 0\)), which tells us that the gradient of \(y = A^2\) is positive. Similarly if \(x\) decreases slightly from \(\left(\dfrac{9V^2}{32}\right)^\frac{1}{6}\), the gradient is negative.

So our single stationary point for \(x > 0\) must be a local minimum, and we know that \(A^2\) (and hence \(A\)) is minimized when \(x^6=\dfrac{9V^2}{32}\).

Now \(h^2 = \dfrac{9V^2}{16x^4}=\dfrac{9V^2}{32x^6}2x^2\), and so if \(x^6 = \dfrac{9V^2}{32}\), then \(h^2 = 2x^2\), and \(y^2 = x^2 + h^2 = 3x^2\).

So \(y = \sqrt{3}x\), and each face must be an equilateral triangle.
