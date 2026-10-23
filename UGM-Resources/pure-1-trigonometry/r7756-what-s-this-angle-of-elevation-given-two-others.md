---
created: 2026-10-23T16:39:11 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/r7756
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-triangles-to-functions
- type/review-question
resource_identity:
  ugm_id: r7756
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7756
  old_site_id: Q44
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
  spec_points: []
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md rule
    3: coverage is never manufactured)'
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Mathematics 1, QP 186, 1951, Q7
task: T-UGM-IMPORT-5
---

# What's this angle of elevation given two others?

## Question

The angular elevation of the summit of a mountain is measured from three points on a straight level road. From a point due south of the summit the elevation is \(\alpha\), from a point due east of it the elevation is \(\beta\), and from the point of the road nearest to the summit the elevation is \(\gamma\).

If the direction of the road makes angle \(\theta\) east of north, prove that

1. \(\tan\theta=\tan\alpha\cot\beta\)

---

1. \(\tan^2\gamma=\tan^2\alpha+\tan^2\beta\).

Find \(\gamma\), if \(\theta=31^{\circ}\) and \(\alpha=8^{\circ}\).

## Suggestion

Before starting, it’s always a good idea to sketch out the problem. Here, we might do that as if we’re looking down on it. We could define \(h\) as the height of the mountain, and then draw three more triangles with the elevation labelled.

Can you use the three different elevation triangles to get three different expressions for the mountain’s height \(h\)?

Are there any useful trigonometrical identities that we can use?

## Solution

Let us choose the length \(AO\) to be \(1\), without loss of generality. (This says effectively that our angles will be the same whatever \(AO\) is.)

Let the height of the mountain be

\(h\)

. We have three expressions for the height

\(h\)

:

\[\begin{align*} \triangle AOM:\quad h&=\tan\alpha\\ \triangle BOM:\quad h&=\tan\theta\tan\beta\\ \triangle COM:\quad h&=\sin\theta\tan\gamma. \end{align*}\]

Equating \(h\) from triangles \(AOM\) and \(BOM\), we get \[h=\tan\alpha=\tan\theta\tan\beta\] so \[\tan\theta=\tan\alpha\cot\beta\] as required.

We will use here the identity \[1+\cot^2\theta=\cosec^2\theta.\]

We have from the diagrams

1. \(\tan^2 \gamma = \dfrac{h^2}{OC^2}\)

---

1. \(\tan^2\alpha = h^2\)

---

1. \(\tan^2\beta = \dfrac{h^2}{OB^2},\) so

\[\begin{align*} \tan^2\alpha + \tan^2\beta &= h^2 + \dfrac{h^2}{OB^2} \\ &=h^2\left(1 + \dfrac{1}{OB^2}\right)\\ &= h^2(1+\cot^2\theta)\\ &= h^2\cosec^2\theta\\ &= \dfrac{h^2}{\sin^2\theta}\\ &= \tan^2\gamma. \end{align*}\]

We can eliminate \(\beta\) from the results of (i) and (ii) to get \[\tan^2\gamma=\frac{\tan^2\alpha}{\sin^2\theta}.\] Substituting in the values for \(\theta\) and \(\alpha\), we find \(\gamma\approx15.3^\circ\).
