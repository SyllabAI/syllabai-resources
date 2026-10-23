---
created: 2026-10-23T16:39:11 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-compound-angles/r8557
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-compound-angles
- type/review-question
resource_identity:
  ugm_id: r8557
  station: trigonometry-compound-angles
  station_title: 'Trigonometry: Compound Angles'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8557
  old_site_id: Q41
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: trigonometry-compound-angles
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: trigonometry-compound-angles
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
  exam_reference: UCLES A level Mathematics 1, QP 184, 1953, Q7
task: T-UGM-IMPORT-5
---

# Can we find the height of a tower using its reflection?

## Question

A tower stands on a river bank. From a point on the other bank directly opposite, and at height \(h\) above the water level, the angle of elevation of the top of the tower is \(\alpha\) and the angle of depression of the reflection of the top in the water is \(\beta\). [It is to be assumed that the water is smooth, so that the reflection of any object in the water will appear to be as far below the surface as the tower is above it.] Prove that the height of the top of the tower above the water is \[h\sin(\alpha+\beta)\cosec(\beta-\alpha),\] and the width of the river is \[2h\cos\alpha\cos\beta\cosec(\beta-\alpha).\]

Find these two distances (to the nearest foot) when \(h=\quantity{15}{ft.}\), \(\alpha=24^\circ\), and \(\beta=31^\circ\).

## Suggestion

Could we draw a helpful diagram including the reflection of the tower?

Let’s call the height of the tower \(t\), and the width of the river \(w\).

Are there any right-angled triangles that could aid us?

The question says that \(\sin(\alpha+\beta)\) and \(\cosec(\beta-\alpha)\) are in the solution – do we know another way of writing these?

## Solution

A tower stands on a river bank. From a point on the other bank directly opposite, and at height \(h\) above the water level, the angle of elevation of the top of the tower is \(\alpha\) and the angle of depression of the reflection of the top in the water is \(\beta\). [It is to be assumed that the water is smooth, so that the reflection of any object in the water will appear to be as far below the surface as the tower is above it.] Prove that the height of the top of the tower above the water is \[h\sin(\alpha+\beta)\cosec(\beta-\alpha),\] and that the width of the river is \[2h\cos\alpha\cos\beta\cosec(\beta-\alpha).\]

The question wants us to find the height of the tower, \(t\), and the width of the river, \(w\). It’s as if someone of height \(h\) is measuring \(\alpha\) and \(\beta\) using a theodolite, and is then using these three values to calculate \(t\) and \(w\). Notice how we deal with the reflection of the tower in our diagram.

We have two right-angled triangles we can work with from the picture. We have

\[\begin{equation} \tan\alpha=\frac{t-h}{w} \label{eq:1}, \end{equation}\]

from the top triangle, and

\[\begin{equation} \tan\beta=\frac{t+h}{w} \label{eq:2}, \end{equation}\]

from the bottom triangle.

We will first find the height of the tower, \(t\). Rearranging \(\eqref{eq:2}\) we find that \[w=\frac{t+h}{\tan\beta}.\]

Substituting this value of

\(w\)

into equation

\(\eqref{eq:1}\)

yields

\[\begin{align*} \tan\alpha&=\frac{(t-h)\tan\beta}{t+h} \\ \implies (t+h)\tan\alpha&=(t-h)\tan\beta \\ \implies (t+h)\sin\alpha\cos\beta&=(t-h)\sin\beta\cos\alpha \\ \implies t&=\frac{-h(\sin\alpha\cos\beta+\sin\beta\cos\alpha)}{\sin\alpha\cos\beta-\sin\beta\cos\alpha}, \\ \implies t&=\frac{h\sin(\alpha+\beta)}{\sin(\beta-\alpha)}=h\sin(\alpha+\beta)\cosec(\beta-\alpha). \end{align*}\]

We have used here that

\[\begin{align*} \tan\theta&=\frac{\sin\theta}{\cos\theta}, \\ \sin(\theta\pm\phi)&=\sin\theta\cos\phi\pm\cos\theta\sin\phi, \text{ and}\\ \cosec\theta&=\frac{1}{\sin\theta}. \end{align*}\]

Now we wish to find the width of the river, \(w\). We now know what \(t\) is, so we have, using our expression for \(w\) above, \[w=\frac{t+h}{\tan\beta}=\frac{h\sin(\alpha+\beta)\cosec(\beta-\alpha)+h}{\tan\beta}.\]

So we must now rearrange this to check that this agrees with the answer in the question. We have

\[\begin{align*} w&=h\left(\frac{\sin(\alpha+\beta)\cos\beta}{\sin{\beta\sin(\beta-\alpha)}}+\frac{\cos\beta}{\sin\beta}\right), \\ &=h\cos\beta\left(\frac{\sin(\alpha+\beta)+\sin(\beta-\alpha)}{\sin\beta\sin(\beta-\alpha)}\right), \\ &=h\cos\beta\left(\frac{2\sin\beta\cos\alpha}{\sin\beta\sin(\beta-\alpha)}\right), \\ &=2h\cos\alpha\cos\beta\cosec(\beta-\alpha), \end{align*}\]

as required.

Alternatively we can use the identity \[\sin\theta+\sin\phi=2\sin\left(\frac{\theta+\phi}{2}\right)\cos\left(\frac{\theta-\phi}{2}\right).\]

We have

\[\begin{align*} t&=\quantity{15\frac{\sin(24+31)}{\sin(31-24)}=15\frac{\sin 55}{\sin 7}=101}{ft.}, \\ w&=30\frac{\cos24 \cos 31}{\sin 7}=\quantity{193}{ft.}, \end{align*}\]

to the nearest foot (using a calculator).

We need to make sure our calculator is in the correct mode (degrees or radians) before making the computation.
