---
created: 2026-10-26T04:13:07 (UTC +06:00)
source: https://undergroundmathematics.org/combining-vectors/r6493
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- combining-vectors
- type/review-question
resource_identity:
  ugm_id: r6493
  station: combining-vectors
  station_title: Combining Vectors
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6493
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: combining-vectors
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: combining-vectors
    validation_status: SUGGESTED
  spec_points:
  - code: 3.7.6
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-15 cross-map (cross-map-p3-vectors.json (P3c
        lane 15) @ syllabai-experimental 16c5f80)
      evidence: '''If a i + b j + c k is perpendicular to these vectors, what is a:b:c?'' — the solution
        states the criterion verbatim (''Two vectors are perpendicular exactly if their scalar product
        [is zero]''), sets the component equations, and ''hence find a unit vector which is perpendicular
        to each of the vectors'' — the scalar-product formula AND a unit-vector construction, 3.7.6 verbatim.
        PICK 3.7.6.'
      rationale: 'Canonical UGM title: If $a\mathbf{i}+b\mathbf{j}+c\mathbf{k}$ is perpendicular to these
        vectors, what is $a:b:c$?'
      validation_status: SUGGESTED
    title: use formulae to calculate the scalar product of e.g. finding the angle between two lines, and
      finding two vectors, and use scalar products in problems the foot of the perpendicular from a point
      to a line; involving lines and points. questions may involve 3D objects such as cuboids, tetrahedra
      (pyramids), etc.
  mapped_date: '2026-10-26'
  mapper: cross-map-p3-vectors.json (P3c lane 15) @ syllabai-experimental 16c5f80
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-15
---

# If $a\mathbf{i}+b\mathbf{j}+c\mathbf{k}$ is perpendicular to these vectors, what is $a:b:c$?

## Question

Given that the vector \(a\mathbf{i}+b\mathbf{j}+c\mathbf{k}\) is perpendicular to each of the vectors \(5\mathbf{i}+3\mathbf{j}-4\mathbf{k}\) and \(2\mathbf{i}-\mathbf{j}-6\mathbf{k}\), find the ratios \(a:b:c\). Hence find a unit vector which is perpendicular to each of the vectors \(5\mathbf{i}+3\mathbf{j}-4\mathbf{k}\) and \(2\mathbf{i}-\mathbf{j}-6\mathbf{k}\).

## Solution

Two vectors are perpendicular exactly if their [scalar product](https://undergroundmathematics.org/glossary/dot-product) is equal to zero.

So we know that \((a\mathbf{i}+b\mathbf{j}+c\mathbf{k}).(5\mathbf{i}+3\mathbf{j}-4\mathbf{k})=0\) and \((a\mathbf{i}+b\mathbf{j}+c\mathbf{k}).(2\mathbf{i}-\mathbf{j}-6\mathbf{k})=0\).

Hence we can form the simultaneous equations

\[\begin{align*} 5a+3b-4c &= 0,\\ 2a-b-6c &=0. \end{align*}\]

The second equation tells us \(b=2a-6c\), and substituting into the first equation, we find \(5a+3(2a-6c)-4c = 0\), which tells us \(a=2c\).

Substituting back into the second equation then reveals \(b=-2c\).

Hence \(a\mathbf{i}+b\mathbf{j}+c\mathbf{k} = 2c\mathbf{i}-2c\mathbf{j}+c\mathbf{k}\), and we conclude the desired ratio is \(2:-2:1\).

The vector \(2c\mathbf{i}-2c\mathbf{j}+c\mathbf{k}\) has length \(c\sqrt{2^2+(-2)^2+1^2} = 3c\).

Thus one unit vector in this direction is \(\dfrac{1}{3c}(2c\mathbf{i}-2c\mathbf{j}+c\mathbf{k})=\dfrac{2}{3}\mathbf{i}-\dfrac{2}{3}\mathbf{j}+\dfrac{1}{3}\mathbf{k}\).

The other is \(-\dfrac{2}{3}\mathbf{i}+\dfrac{2}{3}\mathbf{j}-\dfrac{1}{3}\mathbf{k}\).
