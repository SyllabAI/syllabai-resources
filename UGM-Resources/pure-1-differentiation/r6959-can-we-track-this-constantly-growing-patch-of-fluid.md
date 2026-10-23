---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/r6959
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/review-question
resource_identity:
  ugm_id: r6959
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6959
  old_site_id: null
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
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: 'circular patch growing at 5 cm^2/s: dA/dt = (dA/dr)(dr/dt) chain-rule rate for the
        radius'
      rationale: 'Canonical UGM title: "Can we track this constantly growing patch of fluid?"; exam
        provenance: UCLES AO level Additional Mathematics 1, 1979, Q8'
      validation_status: SUGGESTED
    title: apply differentiation to gradients, tangents and normals, increasing and decreasing functions
      and rates of change
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES AO level Additional Mathematics 1, 1979, Q8
task: T-UGM-IMPORT-7
---

# Can we track this constantly growing patch of fluid?

## Question

A viscous liquid is poured on a flat surface. It forms a circular patch which grows at a steady rate of \(\quantity{5}{cm^2/s}\). Find, in terms of \(\pi\),

1. the radius of the patch 20 seconds after pouring has commenced.

---

1. the rate of increase of the radius at this instant.

## Solution

The area \(A\) of the patch is a function of time such that\[\dfrac{dA}{dt}=5 \implies A = 5t,\]

since \(A = 0\) when \(t = 0\).

We also know that at any given time, the area of a circle is connected to its radius via \[A=\pi r^2.\]

If we combine both equations, eliminating A and solving for \(r\), we find\[r=\sqrt{\frac{5t}{\pi}}, \text{or} \: r=\left(\sqrt{\frac{5}{\pi}}\right)t^{\frac {1}{2}}\]

and hence at \(t=20\),

\[r=\frac{10}{\sqrt{\pi}}.\]

Differentiating our expression for \(r\) gives \[\frac{dr}{dt} = \frac{1}{2}\sqrt{\frac{5}{\pi}}t^{-\frac{1}{2}}=\frac{1}{2}\sqrt{\frac{5}{\pi t}},\] and hence we find at a time of 20 seconds an increase of

\[\frac{dr}{dt} = \frac{1}{4\sqrt{\pi}}.\]

Alternatively here we could use the [Chain Rule](https://undergroundmathematics.org/glossary/chain-rule) to say \(\dfrac{dA}{dt}=\dfrac{dA}{dr}\times\dfrac{dr}{dt}\). We know \(\dfrac{dA}{dt}=5\) and can easily find \(\dfrac{dA}{dr} = 2\pi r\).

Thus \(\dfrac{dr}{dt} = \dfrac{5}{2\pi r}\). So when \(t = 20\), \(\dfrac{dr}{dt}= \dfrac{5}{2\pi \frac{10}{\sqrt{\pi}}} = \dfrac{1}{4\sqrt{\pi}}\), as before.
