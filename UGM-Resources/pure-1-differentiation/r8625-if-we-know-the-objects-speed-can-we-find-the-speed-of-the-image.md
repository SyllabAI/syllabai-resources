---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/r8625
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/review-question
resource_identity:
  ugm_id: r8625
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8625
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: chain-rule
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: chain-rule
    validation_status: SUGGESTED
  spec_points:
  - code: 1.7.3
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: lens-formula related rates — expressible via v=f+f^2(u-f)^-1 and the chain rule (P1-compatible
        route; the recorded solutions often go implicit)
      rationale: 'Canonical UGM title: "If we know the object''s speed, can we find the speed of the
        image?"; exam provenance: UCLES A level Pure Mathematics 2, 1980, Q1(a)'
      validation_status: SUGGESTED
    title: apply differentiation to gradients, tangents and normals, increasing and decreasing functions
      and rates of change
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Pure Mathematics 2, 1980, Q1(a)
task: T-UGM-IMPORT-7
---

# If we know the object's speed, can we find the speed of the image?

## Question

The distances

\(u\)

and

\(v\)

of an object and its image respectively from a lens of focal length

\(f\)

are connected by the formula

\[\begin{equation*} \frac{1}{u} + \frac{1}{v} = \frac{1}{f}. \end{equation*}\]

Determine the speed of the image of an object when the object is \(\quantity{3}{m}\) from a lens of focal length \(\quantity{\dfrac{1}{2}}{m}\) and is moving away from the lens at \(\quantity{5}{m\,s^{-1}}\).

## Solution

We want to find the speed of the image,

\(\dfrac{dv}{dt}\)

, at the moment when

\(u=3\)

and

\(\dfrac{du}{dt}=5\)

. So let’s try implicitly differentiating the formula with respect to

\(t\)

.

\[\begin{align*} u^{-1} + v^{-1} &= 2 \\ \implies\quad -u^{-2}\frac{du}{dt} -v^{-2}\frac{dv}{dt} &= 0 \\ \iff\quad \frac{1}{u^2}\frac{du}{dt} &= -\frac{1}{v^2}\frac{dv}{dt} \end{align*}\]

Substituting in the given values, we have

\[\begin{equation} \frac{dv}{dt} = -\frac{5}{9}v^2. \label{eq:dvdt} \end{equation}\]

Substituting values into the original formula, we have

\[\begin{align*} \frac{1}{3} + \frac{1}{v} &= 2 \\ \implies\quad v^2 &= \frac{9}{25} \end{align*}\]

and combining with

\(\eqref{eq:dvdt}\)

we have

\[\begin{equation*} \frac{dv}{dt} = -\frac{5}{9}\frac{9}{25} = -\frac{1}{5}. \end{equation*}\]

So the speed of the image is \(\quantity{0.2}{m\,s^{-1}}\).

Alternatively, we could have rearranged the given formula as \[v=\frac{u}{2u-1}\] and differentiated using the [quotient rule](https://undergroundmathematics.org/glossary/quotient-rule) to achieve the same result.
