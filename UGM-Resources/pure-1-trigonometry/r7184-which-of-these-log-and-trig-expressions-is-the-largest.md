---
created: 2026-10-23T16:39:10 (UTC +06:00)
source: https://undergroundmathematics.org/exp-and-log/r7184
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- exp-and-log
- type/review-question
resource_identity:
  ugm_id: r7184
  station: exp-and-log
  station_title: Exponentials & Logarithms
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7184
  old_site_id: Q168
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: exp-and-log
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: exp-and-log
    validation_status: SUGGESTED
  spec_points:
  - code: 1.5.1
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-5 cross-map (cross-map-trigonometry.json (P3c
        lane 5) @ syllabai-experimental 75f1cfb8)
      evidence: largest of tan(5π/4), sin^2(5π/4), log values — tan's period π and sin(π−x)=sinx symmetry
        with exact values; the log comparison rides 2.2 — recorded
      rationale: 'Canonical UGM title: “Which of these log and trig expressions is the largest?”; exam
        provenance: Oxford University Mathematics Aptitude Test, Specimen 2, Q1C'
      validation_status: SUGGESTED
    title: sketch and use graphs of the sine, cosine and Including e.g. tangent functions (for angles
      of any size, and using either degrees or radians)
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, Specimen 2, Q1C
task: T-UGM-IMPORT-5
---

# Which of these log and trig expressions is the largest?

## Question

Which of the following numbers is largest in value? (All angles are given in radians.)

1. \(\tan\left(\frac{5\pi}{4}\right)\),

---

1. \(\sin^2 \left(\frac{5\pi}{4}\right)\),

---

1. \(\log_{10} \left(\frac{5\pi}{4}\right)\),

---

1. \(\log_2 \left(\frac{5\pi}{4}\right)\).

## Suggestion

Which of the terms can we evaluate exactly? How do the other terms compare?

## Solution

Let’s consider the numbers in order.

a: Using the fact that \(\tan\) has period \(\pi\), we have \[\tan \left(\frac{5\pi}{4}\right)=\tan\left(\pi + \frac{\pi}{4}\right) = \tan \left(\frac{\pi}{4}\right)=1 .\]

b: Since

\(\sin(\pi - x) = \sin(x)\)

, we have

\[\begin{align*} \sin\left(\frac{5\pi}{4}\right)&=\sin\left(\pi-\frac{5\pi}{4}\right)\\ &=\sin\left(\frac{-\pi}{4}\right)\\ &=-\sin\left(\frac{\pi}{4}\right) = \frac{-1}{\sqrt{2}}\\ \implies \sin^2 \left(\frac{5\pi}{4}\right)&=\frac{1}{2} . \end{align*}\]

c: Now, since \(\pi<4\), we know that \(\frac{5\pi}{4}<5\) and so clearly \(\frac{5\pi}{4}<10\). Therefore, \[\log_{10}\left(\frac{5\pi}{4}\right)<1 .\]

d: Similarly, \(\pi>3 \implies \frac{5\pi}{4}>\frac{15}{4}>2\). Hence, \[\log_{2}\left(\frac{5\pi}{4}\right)>1.\] So this expression has the largest value of the four.

The answer is (d).
