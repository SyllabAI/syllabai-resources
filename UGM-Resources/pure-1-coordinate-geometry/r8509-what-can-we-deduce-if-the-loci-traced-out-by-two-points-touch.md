---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/circles/r8509
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- circles
- type/review-question
resource_identity:
  ugm_id: r8509
  station: circles
  station_title: Circles
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8509
  old_site_id: Q1006
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
      evidence: 'OP^2=lambda y locus is a circle with centre (0, lambda/2); touching-loci condition — the locus-to-circle derivation family.'
      rationale: 'Canonical UGM title: “What can we deduce if the loci traced out by two points touch?”; exam provenance: UCLES 1955 Q1'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1955 Q1
task: T-UGM-IMPORT-3
---

# What can we deduce if the loci traced out by two points touch?

## Question

A point \(P(x,y)\) moves so that \(OP^2=\lambda y\), where \(O\) is the origin and \(\lambda\) is a constant. Show that the locus of \(P\) is a circle. State the coordinates of the centre of the circle and the length of its radius.

Using the same axes, find the locus of a point \(Q(x',y')\) which moves so that \(QR^2=\lambda' y'\), where \(R\) is the fixed point \((\alpha,0)\) and \(\lambda'\) is a constant.

If the two loci touch each other, and \(\alpha\ne 0\), prove that \(\alpha^2=\lambda\lambda'\).

## Suggestion

Could we sketch the point \(P(x,y)\) and the line \(OP\)?

What’s the formula for the distance between two points?

Could we rearrange this into the standard form for a circle?

Could we draw a picture of this situation?

What’s the distance between the two centres here?

## Interactive graph

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/yvrctBHc)

The red circle here is \(x^2 + y^2 = \lambda y\), while the green circle is \((x-\alpha)^2+y^2=\lambda'y\).

What happens as we vary \(\lambda, \alpha\) and \(\lambda'\)? When do the circles touch?

## Solution

We can apply Pythagoras’ Theorem to find the length

\(OP^2\)

. We have

\[OP^2=x^2+y^2.\]

Now we know that the length

\(OP^2\)

must be equal to

\(\lambda y\)

. We substitute this in and rearrange, giving

\[\begin{align*} OP^2=\lambda y =x^2+y^2 \\ x^2+y^2-\lambda y=0 \\ x^2+\left(y-\dfrac{\lambda}{2}\right)^2-\dfrac{\lambda^2}{4}=0 \\ x^2+\left(y-\dfrac{\lambda}{2}\right)^2=\dfrac{\lambda^2}{4}. \end{align*}\]

This tells us that points \(P(x,y)\) such that \(OP^2=\lambda y\) form a circle, and inspecting the equation above, we see that the circle has centre \(\left(0,\dfrac{\lambda}{2}\right)\) and radius \(\dfrac{\lambda}{2}\).

A point \(Q(x',y')\)

We see the length of the base of the triangle is \(x'-\alpha\), if \(x'>\alpha\), or \(\alpha-x'\) if \(x'<\alpha\).

As squaring both of these quantities gives the same result, we see that

\[\begin{align*} \lambda'y'=QR^2=(x'-\alpha)^2+y'^2 \\ (x'-\alpha)^2+\left(y'-\dfrac{\lambda'}{2}\right)^2=\dfrac{\lambda'^2}{4}, \end{align*}\]

that is, such points lie on the circle with centre \(\left(\alpha,\dfrac{\lambda'}{2}\right)\), with radius \(\dfrac{\lambda'}{2}\).

There is a right-angled triangle here with side lengths that we know.

Using Pythagoras’ theorem, we find

\[\left(\frac{\lambda}{2}+\frac{\lambda'}{2}\right)^2=\alpha^2+\left(\frac{\lambda}{2}-\frac{\lambda'}{2}\right)^2.\]

We could see this as finding (the distance between the centres of the circles\()^2\), using the formula for the distance between two points, which was originally derived from Pythagoras’s theorem.

Expanding the brackets gives

\[\frac{\lambda^2}{4}+\frac{\lambda'^2}{4}+\frac{\lambda\lambda'}{2}=\alpha^2+\frac{\lambda^2}{4}+\frac{\lambda'^2}{4}-\frac{\lambda\lambda'}{2}.\]

Rearranging, we have that

\[\alpha^2=\lambda\lambda'.\]
