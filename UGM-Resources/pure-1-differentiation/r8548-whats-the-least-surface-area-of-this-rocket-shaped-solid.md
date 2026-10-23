---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/r8548
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/review-question
resource_identity:
  ugm_id: r8548
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8548
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-of-powers
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-of-powers
    validation_status: SUGGESTED
  spec_points:
  - code: 1.7.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: 'rocket-shaped solid of fixed volume: least surface area — optimisation with a fractional-power
        slant'
      rationale: 'Canonical UGM title: "What''s the least surface area of this rocket-shaped solid?";
        exam provenance: UCLES A level Pure Mathematics 2, 1973, Q2'
      validation_status: SUGGESTED
    title: use the derivative of x (for any rational n ), together with constant multiples, sums and
      differences of functions, and of composite functions using the chain rule
  - code: 1.7.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: 'rocket-shaped solid of fixed volume: least surface area — optimisation with a fractional-power
        slant'
      rationale: 'Canonical UGM title: "What''s the least surface area of this rocket-shaped solid?";
        exam provenance: UCLES A level Pure Mathematics 2, 1973, Q2'
      validation_status: SUGGESTED
    title: locate stationary points and determine their nature, and use information about stationary
      points in sketching graphs.
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Pure Mathematics 2, 1973, Q2
task: T-UGM-IMPORT-7
---

# What's the least surface area of this rocket-shaped solid?

## Question

A rocket-shaped solid consists of a right circular cylinder of length \(l\) and radius \(r\) attached at one end to the base of a right circular cone of base radius \(r\) and height \(\frac{3}{4}r\). If the total volume of the solid is to be \(\quantity{14\pi}{cm^3}\), find its least possible surface area.

## Solution

The volume of the rocket-shaped solid is the sum of the volumes of the cylinder and the cone.

The volume of the cylinder is \(\pi r^2 l\), and the volume of the cone is \(\frac{1}{3} \pi r^2 \left( \frac{3}{4} r \right)\), or \(\frac{1}{4}\pi r^3\).

From the question, we must have that

\[\begin{equation*} 14\pi = \pi r^2 l + \frac{1}{4}\pi r^3 = \pi r^2 \left( l + \frac{r}{4} \right) \iff l = \frac{14}{r^2} - \frac{r}{4}. \end{equation*}\]

The surface area of the rocket-shaped solid does not include the base of the cone or the top of the cylinder.

The contribution from the cylinder is thus its bottom disc and curved surface, while the contribution from the cone is just its sloped surface.

For the cylinder, the area of the bottom disc is \(\pi r^2\), while the area of the curved surface is \(2\pi r l\), since when uncurled, it’s a rectangle with side lengths \(2\pi r\) and \(l\).

The area of the sloped part of the cone is

\(\pi r\)

times the slope length; by Pythagoras’ theorem, this length is

\[\begin{equation*} \sqrt{ r^2 + \left(\frac{3}{4}r \right)^2 } = \sqrt{ \frac{25}{16} r^2 } = \frac{5}{4} r. \end{equation*}\]

Thus, the surface area equals

\[\begin{align*} S(r)=\pi r^2 + 2 \pi r l + \pi r \frac{5}{4} r &= \pi r^2 \left( 1 + \frac{5}{4} \right) + 2 \pi r \left( \frac{14}{r^2} - \frac{r}{4} \right) \\ &= \frac{9}{4} \pi r^2 + \frac{28\pi}{r} - \frac{\pi}{2} r^2 \\ &= \frac{7}{4} \pi r^2 + \frac{28\pi}{r}. \end{align*}\]

We are to minimise

\(S(r)\)

with respect to

\(r\)

. Differentiating and setting the derivative equal to zero,

\[\begin{equation*} \frac{dS}{dr} = \frac{7}{2} \pi r - \frac{28\pi}{r^2} = 0 \iff r^3 = 8 \iff r = 2. \end{equation*}\]

This is the unique stationary point for \(S(r)\), and it must be a minimum, since \(S(r) \to \infty\) if \(r \to 0\) or \(r \to \infty\).

The least possible surface area is thus

\[\begin{equation*} S(2) = \frac{7}{4} \pi \times 2^2 + \frac{28\pi}{2} = 7\pi + 14\pi = \quantity{21\pi}{cm^2}. \end{equation*}\]
