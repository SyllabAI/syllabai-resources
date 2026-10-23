---
created: 2026-10-23T16:39:10 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/r7973
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-triangles-to-functions
- type/review-question
resource_identity:
  ugm_id: r7973
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7973
  old_site_id: Q32
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
      evidence: how many distinct values among sinα sinβ, sinα cosβ, cosα sinβ, cosα cosβ — ratio definitions
        and ordering
      rationale: 'Canonical UGM title: “Are any of these four trig expressions equal to each other?”;
        exam provenance: UKMT Senior Mathematical Challenge, 2006, Q16'
      validation_status: SUGGESTED
    title: sketch and use graphs of the sine, cosine and Including e.g. tangent functions (for angles
      of any size, and using either degrees or radians)
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UKMT Senior Mathematical Challenge, 2006, Q16
task: T-UGM-IMPORT-5
---

# Are any of these four trig expressions equal to each other?

## Question

If \(\alpha<\beta\), how many different values are there among the following expressions? \[\sin\alpha\sin\beta \quad \sin\alpha\cos\beta \quad \cos\alpha\sin\beta \quad \cos\alpha\cos\beta\]

## Solution

**Method 1**

We have

\[\sin\alpha\sin\beta = \frac{b}{c}\frac{a}{c} = \frac{ab}{c^2},\]

\[\sin\alpha\cos\beta = \frac{b}{c}\frac{b}{c} = \frac{b^2}{c^2},\]

\[\cos\alpha\sin\beta = \frac{a}{c}\frac{a}{c} = \frac{a^2}{c^2},\]

and

\[\cos\alpha\cos\beta = \frac{a}{c}\frac{b}{c} = \frac{ab}{c^2}.\]

Now since \(a > b, a^2 > ab > b^2\), and clearly the expressions take exactly three distinct values.

**Method 2**

We know that \(0<\alpha<45^{\circ}<\beta<90^{\circ}\). Using the properties of \(\cos\) and \(\sin\) (which which are illustrated in the graph above), we have

\[\begin{align} \sin \alpha < \cos \alpha\label{eq:2}\\ \cos \beta < \sin \beta\label{eq:4}\\ \end{align}\]

Now if we start with \(\eqref{eq:4}\) and multiply it by \(\sin\alpha\), we get

\[\sin\alpha\cos \beta < \sin\alpha\sin \beta.\]

If we start with \(\eqref{eq:2}\) and multiply by \(\sin \beta\), we get

\[\sin \beta \sin \alpha <\sin \beta \cos \alpha.\]

Now \(\alpha\) and \(\beta\) are [complementary angles](https://undergroundmathematics.org/glossary/complementary-angle), so we can write

\[\cos\alpha\cos\beta=\cos(90^{\circ}-\beta)\cos(90^{\circ}-\alpha)=\sin\beta\sin\alpha.\]

So we can order the four expressions as

\[\sin\alpha\cos\beta<\sin\alpha\sin\beta=\cos\alpha\cos\beta<\cos\alpha\sin\beta\]

and conclude that we have only three different values.
