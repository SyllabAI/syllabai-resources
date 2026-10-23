---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-meets-functions/r6180
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-meets-functions
- type/review-question
resource_identity:
  ugm_id: r6180
  station: calculus-meets-functions
  station_title: Calculus meets Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6180
  old_site_id: Q255
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-meets-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-meets-functions
    validation_status: SUGGESTED
  spec_points:
  - code: 1.7.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: 'cylindrical tin plus 2 cm-overlap lid from 350*pi cm^2 of metal: maximise the volume
        — canonical CIE P1 optimisation'
      rationale: 'Canonical UGM title: "Can we maximise the volume of this metal tin?"; exam provenance:
        UCLES A level Mathematics A 1, 1980, Q10'
      validation_status: SUGGESTED
    title: use the derivative of x (for any rational n ), together with constant multiples, sums and
      differences of functions, and of composite functions using the chain rule
  - code: 1.7.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: 'cylindrical tin plus 2 cm-overlap lid from 350*pi cm^2 of metal: maximise the volume
        — canonical CIE P1 optimisation'
      rationale: 'Canonical UGM title: "Can we maximise the volume of this metal tin?"; exam provenance:
        UCLES A level Mathematics A 1, 1980, Q10'
      validation_status: SUGGESTED
    title: locate stationary points and determine their nature, and use information about stationary
      points in sketching graphs.
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Mathematics A 1, 1980, Q10
task: T-UGM-IMPORT-7
---

# Can we maximise the volume of this metal tin?

## Question

A cylindrical tin and its tight-fitting cylindrical lid (overlapping the tin by \(\quantity{2}{cm}\)) are to be made from thin sheet metal. When made, the total area of sheet metal used is \(\quantity{350\pi}{cm^2}\). The base radius of the tin is \(\quantity{x}{cm}\) and its height is \(\quantity{y}{cm}\) as shown in the diagram. Show that, neglecting the thickness of the metal, \[x^2+xy+2x=175.\]

Deduce that the volume, \(\quantity{V}{cm^3}\), of the tin is given by \[V= \pi(175x-2x^2-x^3).\]

If \(x\) may vary, find the values of \(x\) and \(y\) for which \(V\) has its maximum value.

## Suggestion

Can you work out the surface area and volume of this tin and lid in terms of \(x\) and \(y\)? Now can you eliminate \(y\)?

## Solution

We know that the surface area of the tin is

\(\quantity{350\pi}{cm^2}\)

. In terms of

\(x\)

and

\(y\)

, the surface area of the tin is:

\[\begin{align*} 350\pi &=\text{area of base} +\text{area of side}+\text{area of side of lid}+\text{area of top of lid} \\ &= \pi x^2+2\pi x y+2\pi x \times2+\pi x^2 \\ &= 2\pi x^2+2\pi xy +4\pi x, \end{align*}\]

and dividing through by

\(2\pi\)

we get

\[\begin{equation}\label{eq:1} 175=x^2+xy+2x. \end{equation}\]

The volume of the tin is \[V= \pi x^2 y.\]

We can eliminate \(y\) by rearranging equation \(\eqref{eq:1}\) to find that \(xy=175-x^2-2x\), and so \[V=\pi x^2 y=\pi x(xy)=\pi x(175-x^2-2x)=\pi(175x-x^3-2x^2).\]

We differentiate \(V\) with respect to \(x\), giving \[\frac{dV}{dx}=\pi(175-3x^2-4x)=0,\] so to find stationary points of \(V\), we must solve \[3x^2+4x-175=0.\]

We can factorise this equation as \((3x+25)(x-7)=0\) (or use the quadratic formula).

Since \(x\) is the radius of the tin, it must be positive, so \(x=7\).

We have that \[\frac{d^2V}{dx^2}=\pi(-6x-4),\] which is negative when \(x\) is positive, so \(x=7\) gives a local maximum for \(V\).

Furthermore, as there are no other stationary points for \(V\) with \(x>0\), this must give the maximum possible value for \(V\) for \(x\ge0\).

We need to find the corresponding \(y.\) We saw in the previous part that \[xy=175-x^2-2x,\] so that \[7y=175-49-14=112,\] and hence \(y=16\).
