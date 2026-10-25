---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/product-rule/how-does-your-rectangle-grow
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- product-rule
- type/scaffolded-task
resource_identity:
  ugm_id: how-does-your-rectangle-grow
  station: product-rule
  station_title: Product Rule & Integration by Parts
  resource_type_id: 3
  resource_type_label: Scaffolded task
  level: Introducing
  ref: 8199
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: product-rule
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: product-rule
    validation_status: SUGGESTED
  spec_points:
  - code: 3.4.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-12 cross-map (cross-map-p3-differentiation.json
        (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4)
      evidence: the fixed-height rectangle argument dA/dt = v du/dt extended to both sides varying - the
        visual derivation of the product rule d(uv)/dt = v du/dt + u dv/dt, the 3.4.2 law itself
      rationale: 'Canonical UGM title: How does your rectangle grow?'
      validation_status: SUGGESTED
    title: differentiate products and quotients e.g.
  mapped_date: '2026-10-25'
  mapper: cross-map-p3-differentiation.json (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-12
---

# How does your rectangle grow?

> Excerpt: This two-part task looks at how the rate of change of the area of a rectangle depends on the side lengths. It offers a visual representation of the Product Rule.

## Sideways

This white rectangle has a fixed height, \(v\), and its width \(u\) varies as a function of time, \(t\). We can write the rate of change of the width as \(\dfrac{du}{dt}\) or \(\dot{u}\). You can think of this as the *speed* at which the right hand edge is moving.

| The area of the white rectangle, \(A=\) |  |
|---|---|
| In a short time interval, \(\delta t\) , we can assume that \(\dot{u}\) is roughly constant, so thinking about speed and distance… |  |
| The width increases by a small amount, \(\delta u =\) |  |
| The area increases by the shaded area, \(\delta A =\) |  |
| The rate of change of the area of the rectangle, \(\dfrac{dA}{dt} \approx \dfrac{\delta A}{\delta t} =\) |  |

Example

Our rectangle has height \(v=\quantity{3}{cm}\) and width \(u=\quantity{\left(\frac{1}{2}t^2+1\right)}{cm}\) at time \(\quantity{t}{s}\).

What is the rate of change of area, \(\dfrac{dA}{dt}\), at

1. \(t=0\)?

---

1. \(t=3\)?

## Both ways

This white rectangle has width \(u\) and height \(v\), both of which vary as functions of time, \(t\). We can write the rates of change as \(\dot{u}\) and \(\dot{v}\).

| The area of the white rectangle, \(A=\) |  |
|---|---|
| In a short time interval, \(\delta t\) , we can assume that \(\dot{u}\) and \(\dot{v}\) are roughly constant, so… |  |
| The width increases by \(\delta u =\) |  |
| The height increases by \(\delta v =\) |  |
| The area increases by approximately the shaded area, so \(\delta A \approx\) |  |
| The rate of change of the area of the rectangle, \(\dfrac{dA}{dt} \approx \dfrac{\delta A}{\delta t} \approx\) |  |

Example

Our rectangle has \(v=\quantity{\sqrt{t+1}}{cm}\) and \(u=\quantity{\left(\frac{1}{2}t^2+1\right)}{cm}\) at time \(\quantity{t}{s}\).

What is the rate of change of area, \(\dfrac{dA}{dt}\), at

1. \(t=0\)?

---

1. \(t=3\)?

## Solution

| The area of the white rectangle, \(A=\) | \(u\times v\) |
|---|---|
| In a short time interval, \(\delta t\) , we can assume that \(\dot{u}\) is roughly constant, so thinking about speed and distance… |  |
| The width increases by a small amount, \(\delta u =\) | \(\dot{u}\,\delta t\) |
| The area increases by the shaded area, \(\delta A =\) | \(v\times\dot{u}\,\delta t\) |
| The rate of change of the area of the rectangle, \(\dfrac{dA}{dt} \approx \dfrac{\delta A}{\delta t} =\) | \(v\times\dot{u} = v\dfrac{du}{dt}\) |

Note that \(\frac{\delta A}{\delta t}\) is a fraction whereas \(\frac{dA}{dt}\) is a derivative. They become identical in the limit as \(\delta t\to0\).

Our rectangle has height \(v=\quantity{3}{cm}\) and width \(u=\quantity{\left(\frac{1}{2}t^2+1\right)}{cm}\) at time \(\quantity{t}{s}\).

What is the rate of change of area, \(\dfrac{dA}{dt}\), at

1. \(t=0\)?

---

1. \(t=3\)?

Differentiating, we have \[\frac{du}{dt}=\frac{1}{2}\times2t = t\] so \[\frac{dA}{dt}=v\frac{du}{dt}=3t.\]

At \(t=0\), \(\frac{dA}{dt}=0\).

At \(t=3\), \(\frac{dA}{dt}=\quantity{9}{cm^2\,s^{-1}}\).

This white rectangle has width \(u\) and height \(v\), both of which vary as functions of time, \(t\). We can write the rates of change as \(\dot{u}\) and \(\dot{v}\).

| The area of the white rectangle, \(A=\) | \(u\times v\) |
|---|---|
| In a short time interval, \(\delta t\) , we can assume that \(\dot{u}\) and \(\dot{v}\) are roughly constant, so… |  |
| The width increases by \(\delta u =\) | \(\dot{u}\,\delta t\) |
| The height increases by \(\delta v =\) | \(\dot{v}\,\delta t\) |
| The area increases by approximately the shaded area, so \(\delta A \approx\) | \(v\times\dot{u}\,\delta t+u\times\dot{v}\,\delta t\) |
| The rate of change of the area of the rectangle, \(\dfrac{dA}{dt} \approx \dfrac{\delta A}{\delta t} \approx\) | \(v\times\dot{u}+u\times\dot{v}\) \(= v\dfrac{du}{dt}+u\dfrac{dv}{dt}\) |

Note that in writing down \(\delta A\) we ignored the small white rectangle in the top right-hand corner. Why is it OK to do this?

This result is known as the [Product Rule](https://undergroundmathematics.org/glossary/product-rule) which is often expressed as \[\frac{d}{dx}\big(uv\big)=u\frac{dv}{dx}+v\frac{du}{dx}.\]

Our rectangle has \(v=\quantity{\sqrt{t+1}}{cm}\) and \(u=\quantity{\left(\frac{1}{2}t^2+1\right)}{cm}\) at time \(\quantity{t}{s}\).

What is the rate of change of area, \(\dfrac{dA}{dt}\), at

1. \(t=0\)?

---

1. \(t=3\)?

Differentiating, we have

\[\begin{align*} \frac{dv}{dt} &= \frac{1}{2}(t+1)^{-\frac{1}{2}} \\ \frac{du}{dt} &= t \end{align*}\]

and so \[\frac{dA}{dt} = \left(\frac{1}{2}t^2+1\right)\times\frac{1}{2}(t+1)^{-\frac{1}{2}} + \sqrt{t+1}\times t.\]

At \(t=0\), \(\frac{dA}{dt} = 1\times\frac{1}{2}\times(1)^{-\frac{1}{2}}+0 = \quantity{\frac{1}{2}}{cm^2\,s^{-1}}\).

At \(t=3\), \(\frac{dA}{dt} = \left(\frac{9}{2}+1\right)\times\frac{1}{2}\times(4)^{-\frac{1}{2}}+\sqrt{4}\times 3 = \quantity{7\frac{3}{8}}{cm^2\,s^{-1}}\).
