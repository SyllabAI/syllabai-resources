---
created: 2026-10-23T16:39:10 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/r8330
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-triangles-to-functions
- type/review-question
resource_identity:
  ugm_id: r8330
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8330
  old_site_id: Q186
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
  - code: 1.5.2
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-5 cross-map (cross-map-trigonometry.json (P3c
        lane 5) @ syllabai-experimental 75f1cfb8)
      evidence: 'equilateral triangle on a circle of circumference 10: area via (1/2)r^2 sin(2π/3) with
        exact sin(2π/3)=√3/2'
      rationale: 'Canonical UGM title: “Which of these area and perimeter statements is true?”; exam provenance:
        Oxford University Mathematics Aptitude Test, 2012, Q1I'
      validation_status: SUGGESTED
    title: use the exact values of the sine, cosine and tangent of 30 °, 45 °, 60 °, and related angles
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, 2012, Q1I
task: T-UGM-IMPORT-5
---

# Which of these area and perimeter statements is true?

## Question

The vertices of an equilateral triangle are labelled \(X\), \(Y\) and \(Z\). The points \(X\), \(Y\) and \(Z\) lie on a circle of circumference \(10\) units. Let \(P\) and \(A\) be the numerical values of the triangle’s perimeter and area, respectively. Which of the following is true?

1. \(\dfrac{A}{P}=\dfrac{5}{4\pi}\);

---

1. \(P<A\);

---

1. \(\dfrac{P}{A}=\dfrac{10}{3\pi}\);

---

1. \(P^2\) is rational.

## Suggestion

Can we draw a diagram? What is the radius of the circle?

## Solution

Since the circumference \(C=2\pi r=10\), we have \(r=\dfrac{5}{\pi}\).

We know that the area of a triangle \(ABC\) is \(\dfrac{1}{2}ab\sin C\). Using this,the area of the smaller triangle shown in the diagram is \[\frac{1}{2}r^2\sin\left( \frac{2\pi}{3}\right)=\left(\dfrac{5}{\pi}\right)^2\frac{\sqrt3}{4} =\dfrac{25\sqrt{3}}{4\pi^2},\] since \(\sin\left( \dfrac{2\pi}{3}\right)=\dfrac{\sqrt{3}}{2}\).

Thus the area of the whole equilateral triangle is \[A=\dfrac{75\sqrt{3}}{4\pi^2}.\]

To find \(P\), we note that \[\dfrac{1}{2}XZ = r\sin \left(\frac{\pi}{3}\right)=\dfrac{5}{\pi}\frac{\sqrt{3}}{2},\] and hence \[P=\dfrac{15\sqrt{3}}{\pi}.\] Therefore \[\frac{A}{P}=\frac{75\sqrt{3}}{4\pi^2}\frac{\pi}{15\sqrt{3}}=\frac{5}{4\pi}\] so the answer is (a).

To check, it is easy to see that \(P^2\) is irrational, since it involves \(\pi^2\), so (d) is not correct.

Since \(\dfrac{A}{P} = \dfrac{5}{4\pi}, P > A\), so (b) is wrong.

From our work, (c) is clearly wrong.

Alternatively, the cosine rule applied to the smaller triangle could be used to find \(P\): \[P=3\times\sqrt{2\times r^2-2\times r^2\cos \left(\frac{2\pi}{3}\right)},\] which again gives \(P=\dfrac{15\sqrt3}{\pi}\).
