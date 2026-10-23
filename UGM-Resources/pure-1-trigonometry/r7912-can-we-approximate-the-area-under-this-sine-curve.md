---
created: 2026-10-23T16:39:10 (UTC +06:00)
source: https://undergroundmathematics.org/introducing-calculus/r7912
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- introducing-calculus
- type/review-question
resource_identity:
  ugm_id: r7912
  station: introducing-calculus
  station_title: Introducing Calculus
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7912
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: introducing-calculus
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: introducing-calculus
    validation_status: SUGGESTED
  spec_points:
  - code: 1.5.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-5 cross-map (cross-map-trigonometry.json (P3c
        lane 5) @ syllabai-experimental 75f1cfb8)
      evidence: plot y = sin x at π/6 intervals using exact values (1/2, √3/2, 1), then trapezium-area
        approximation of ∫sin — the area work rides 1.8 (recorded)
      rationale: 'Canonical UGM title: “Can we approximate the area under this sine curve?”; exam provenance:
        O&C O level SMP Additional Mathematics 1, QP SMP 117, 1975, Q11'
      validation_status: SUGGESTED
    title: sketch and use graphs of the sine, cosine and Including e.g. tangent functions (for angles
      of any size, and using either degrees or radians)
  - code: 1.5.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-5 cross-map (cross-map-trigonometry.json (P3c
        lane 5) @ syllabai-experimental 75f1cfb8)
      evidence: plot y = sin x at π/6 intervals using exact values (1/2, √3/2, 1), then trapezium-area
        approximation of ∫sin — the area work rides 1.8 (recorded)
      rationale: 'Canonical UGM title: “Can we approximate the area under this sine curve?”; exam provenance:
        O&C O level SMP Additional Mathematics 1, QP SMP 117, 1975, Q11'
      validation_status: SUGGESTED
    title: use the exact values of the sine, cosine and tangent of 30 °, 45 °, 60 °, and related angles
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: O&C O level SMP Additional Mathematics 1, QP SMP 117, 1975, Q11
task: T-UGM-IMPORT-5
---

# Can we approximate the area under this sine curve?

## Question

Draw the graph of \(y = \sin x\) for \(0 \leq x \leq \pi\), plotting points with \(x\)-coordinates at intervals of \(\dfrac{\pi}{6}\), and labelling them \(O, A, B, C, D, E, F\) successively.

Calculate the area of the polygon \(OABCDEF\) by dividing it into strips parallel to the \(y\)-axis, or otherwise. Hence give an approximation to \[\int_0^{\pi/2}\sin x \:dx.\]

## Solution

We start by making a table of values.

The values of \(\sin x\) we seek are given by examining these triangles;

| \(x\) | \(0\) | \(\pi/6\) | \(2\pi/6\) | \(3\pi/6\) | \(4\pi/6\) | \(5\pi/6\) | \(6\pi/6\) |
|---|---|---|---|---|---|---|---|
| \(\sin x\) | \(0\) | \(1/2\) | \(\sqrt{3}/2\) | \(1\) | \(\sqrt{3}/2\) | \(1/2\) | \(0\) |

We can now plot these seven points to give us an approximation to the required graph.

If we divide the polygon as suggested, we get two triangles and four trapezia. Notice that the shape is symmetrical, so we can just calculate the areas of one triangle and two trapezia and double the result.

\[\begin{align*} \text{Area}_1 &= \frac{1}{2}\times\frac{\pi}{6}\times\frac{1}{2} = \frac{\pi}{24} \\ \text{Area}_2 &= \frac{1}{2}\times\frac{\pi}{6}\times\left(\frac{1}{2}+\frac{\sqrt{3}}{2}\right) = \frac{\pi}{24}(1+\sqrt{3}) \\ \text{Area}_3 &= \frac{1}{2}\times\frac{\pi}{6}\times\left(\frac{\sqrt{3}}{2}+1\right) = \frac{\pi}{24}(\sqrt{3}+2) \\ \implies\quad\text{Area}_{\text{half}} &= \frac{\pi}{24}(4+2\sqrt{3}) \end{align*}\]

So the area of the whole polygon is \(\dfrac{\pi}{6}(2+\sqrt{3}) = 1.954\) (\(4\) s.f.).

The value of the integral we are to approximate is the area under the curve as far as its maximum point. This is approximately the same as half the area of the polygon, \(0.977\) (\(3\) s.f.). From the diagram we can see that this is a slight underestimate.

Using calculus, it is possible to calculate the required integral exactly, as \(-\cos (\pi/2) - (-\cos 0) = 1\).
