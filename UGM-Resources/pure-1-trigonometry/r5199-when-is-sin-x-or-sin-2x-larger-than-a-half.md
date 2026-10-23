---
created: 2026-10-23T16:39:10 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/r5199
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-triangles-to-functions
- type/review-question
resource_identity:
  ugm_id: r5199
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5199
  old_site_id: Q131
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: trigonometry-triangles-to-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: trigonometry-triangles-to-functions
    validation_status: SUGGESTED
  spec_points:
  - code: 1.5.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-5 cross-map (cross-map-trigonometry.json (P3c
        lane 5) @ syllabai-experimental 75f1cfb8)
      evidence: fraction of 0≤x≤2π for which sin x ≥ 1/2 and sin 2x ≥ 1/2 — graph reading plus solution
        sets
      rationale: 'Canonical UGM title: “When is $\sin x$ or $\sin 2x$ larger than a half?”; exam provenance:
        Oxford University Mathematics Aptitude Test, 2011, Q1D'
      validation_status: SUGGESTED
    title: sketch and use graphs of the sine, cosine and Including e.g. tangent functions (for angles
      of any size, and using either degrees or radians)
  - code: 1.5.5
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-5 cross-map (cross-map-trigonometry.json (P3c
        lane 5) @ syllabai-experimental 75f1cfb8)
      evidence: fraction of 0≤x≤2π for which sin x ≥ 1/2 and sin 2x ≥ 1/2 — graph reading plus solution
        sets
      rationale: 'Canonical UGM title: “When is $\sin x$ or $\sin 2x$ larger than a half?”; exam provenance:
        Oxford University Mathematics Aptitude Test, 2011, Q1D'
      validation_status: SUGGESTED
    title: find all the solutions of simple trigonometrical equations lying in a specified interval (general
      forms of solution are not included).
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, 2011, Q1D
task: T-UGM-IMPORT-5
---

# When is $\sin x$ or $\sin 2x$ larger than a half?

## Question

The fraction of the interval \(0\leq x \leq 2\pi\), for which one (or both) of the inequalities \[\sin x \geq\frac{1}{2}, \qquad \sin 2x \geq \frac{1}{2}\] is true, equals

1. \(\dfrac{1}{3}\);

---

1. \(\dfrac{13}{24}\);

---

1. \(\dfrac{7}{12}\);

---

1. \(\dfrac{5}{8}\).

## Solution

The fraction of the interval \(0\leq x \leq 2\pi\), for which one (or both) of the inequalities \[\sin x \geq\frac{1}{2}, \qquad \sin 2x \geq \frac{1}{2}\] is true, equals

1. \(\frac{1}{3}\);

---

1. \(\frac{13}{24}\);

---

1. \(\frac{7}{12}\);

---

1. \(\frac{5}{8}\).

In the range \(0\leq x\leq2\pi\) we have \(\sin x\geq\dfrac{1}{2}\) if and only if \(\dfrac{\pi}{6}\leq x \leq \dfrac{5\pi}{6},\)

and \(\sin 2x\geq\dfrac{1}{2}\) if and only if \[\dfrac{\pi}{12}\leq x \leq \dfrac{5\pi}{12}\quad \text{or} \quad \dfrac{13\pi}{12} \leq x \leq \dfrac{17\pi}{12}.\]

So at least one of the inequalities holds for \(\dfrac{\pi}{12}\leq x \leq \dfrac{5\pi}{6}\) and \(\dfrac{13\pi}{12}\leq x \leq \dfrac{17\pi}{12}\).

The first of these intervals has length \(\dfrac{9\pi}{12}\) and the second has length \(\dfrac{4\pi}{12}\).

Therefore the fraction of the interval \(0\leq x \leq 2\pi\), for which one (or both) of the inequalities is true, is \(\dfrac{13\pi}{12}\) out of \(2\pi\), which is \(\dfrac{13}{24}\). Hence, the solution is (b).
