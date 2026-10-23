---
created: 2026-10-23T16:39:10 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/r5497
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-triangles-to-functions
- type/review-question
resource_identity:
  ugm_id: r5497
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5497
  old_site_id: Q164
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
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-5 cross-map (cross-map-trigonometry.json (P3c
        lane 5) @ syllabai-experimental 75f1cfb8)
      evidence: 'circle-with-tangent diagram: choose the correct relation among cos α = sin(β+γ) etc.
        — complementary-angle structure read from a diagram'
      rationale: 'Canonical UGM title: “How are these three angles connected?”; exam provenance: Oxford
        University Mathematics Aptitude Test, 2011, Q1E'
      validation_status: SUGGESTED
    title: sketch and use graphs of the sine, cosine and Including e.g. tangent functions (for angles
      of any size, and using either degrees or radians)
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, 2011, Q1E
task: T-UGM-IMPORT-5
---

# How are these three angles connected?

## Question

*[Choose the one correct answer and explain your reasoning.]*

The circle in the diagram has centre \(C\). Three angles \(\alpha, \beta, \gamma\) are also indicated.

The angles \(\alpha,\beta, \gamma\) are related by the equation:

1. \(\cos \alpha = \sin (\beta + \gamma)\),

---

1. \(\sin \beta = \sin \alpha \sin \gamma\),

---

1. \(\sin \beta (1 − \cos \alpha) = \sin \gamma\),

---

1. \(\sin (\alpha + \beta) = \cos \gamma \sin \alpha\).

## Solution

Let’s give the vertices in the diagram some names. We’ll call the vertex of angles \(\alpha\) and \(\beta\), \(A\), and the vertex of angle \(\gamma\), B.

We’ll also draw in the radius between C and the tangent - they’ll be perpendicular at the point of contact. We’ll call this point \(D\).

By looking at the right-angled triangle \(ACD\), we can see that the length of \(AC = x = \dfrac{r}{\sin \alpha}\), so \(r = x\sin\alpha\).

Now we can apply the sine rule to the triangle \(ABC\) to give \[\frac{\sin \beta}{r}=\frac{\sin \gamma}{x},\] so \[x\sin\beta = r\sin\gamma \implies x\sin\beta = x\sin\alpha\sin\gamma.\]

So on cancelling \(x\) we have \[\sin \beta = \sin \alpha \sin \gamma,\] and the answer is (b).
