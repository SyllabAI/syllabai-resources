---
created: 2026-10-26T02:40:04 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/r9297
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/review-question
resource_identity:
  ugm_id: r9297
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9297
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: chain-rule
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: chain-rule
    validation_status: SUGGESTED
  spec_points:
  - code: 3.5.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-13 cross-map (cross-map-p3-integration.json
        (P3c lane 13) @ syllabai-experimental 21845f3)
      evidence: tan^4 x = tan^2 x sec^2 x - sec^2 x + 1 shown from tan^2 = sec^2 - 1, then INT_0^(pi/4)
        tan^4 x dx = tan x - x evaluated at pi/4 = 1 - pi/4 - the exact CIE 3.5.2 use-trigonometrical-relationships
        showcase; the chain-rule tan^3 derivative intro is the recorded 3.4.1 clothing (flips the lane-11
        non-overlap row of record routed 'P3 3.5 Integration')
      rationale: 'Canonical UGM title: How could we integrate $\tan^4x$?'
      validation_status: SUGGESTED
    title: use trigonometrical relationships in carrying out integration or
  mapped_date: '2026-10-26'
  mapper: cross-map-p3-integration.json (P3c lane 13) @ syllabai-experimental 21845f3
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-13
---

# How could we integrate $\tan^4x$?

## Question

Given that \(\dfrac{d}{dx}(\tan x)=\sec^2 x,\) differentiate \(\tan^3x\) with respect to \(x\).

Show that \[\tan^4x=\tan^2x \sec^2x- \sec^2x+1\] and hence evaluate \[\int_0^{\pi/4}\tan^4x \, dx.\]

## Solution

Using the chain rule, we have that \[\frac{d}{dx}\tan^3 x = 3 \tan^2 x \times \frac{d}{dx}\tan x= 3\tan^2 x \sec^2x.\]

We can write

\[\begin{align*} \tan^4x&=\tan^2x\tan^2x\\ &=\tan^2x(\sec^2x-1)\\ &=\tan^2x\sec^2x-\tan^2 x\\ &=\tan^2x\sec^2x-(\sec^2x-1)\\ &=\tan^2x\sec^2x-\sec^2x+1. \end{align*}\]

…and hence evaluate \[\int_0^{\pi/4}\tan^4x \, dx.\]

Using the previous parts,

\[\begin{align*} \int_0^{\pi/4} \tan^4x \, dx&= \int_0^{\pi/4}\tan^2x\sec^2x-\sec^2x+1 \, dx \\ &=\left[\frac{1}{3}\tan^3x-\tan x+x\right]^{\pi/4}_0 \\ &=\frac{1}{3}-1+\frac{\pi}{4} \\ &=\frac{\pi}{4}-\frac{2}{3}. \end{align*}\]
