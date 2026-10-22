---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/combining-functions/r9924
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- combining-functions
- type/review-question
resource_identity:
  ugm_id: r9924
  station: combining-functions
  station_title: Combining Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9924
  old_site_id: Q111
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: combining-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: combining-functions
    validation_status: SUGGESTED
  spec_points: []
  mapped_date: '2026-10-23'
  mapper: cross-map-functions.json (P3c) @ syllabai-experimental 4a592ed0
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md rule
    3: coverage is never manufactured)'
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford (MAT) 2009 Q['Q1E']
task: T-UGM-IMPORT-2
---

# How many solutions does this composite function equation have?

## Question

In the range \(0\leq x < 2\pi\) the equation \[2^{\sin^2(x)} + 2^{\cos^2(x)} =2\]

1. has \(0\) solutions;
2. has \(1\) solution;
3. has \(2\) solutions;
4. holds for all values of \(x\).

## Solution

### Method 1

In the range \(0\leq x < 2\pi\), we have \(0\leq \sin^2 x \leq 1\) and \(0\leq \cos^2 x \leq 1\). So \(1 \leq 2^{\sin^2(x)} \leq 2\) and \(1 \leq 2^{\cos^2(x)} \leq 2\).

This means that the only way the sum \(2^{\sin^2(x)} + 2^{\cos^2(x)}\) can be equal to \(2\) is if both \(2^{\cos^2(x)}\) and \(2^{\sin^2(x)}\) are equal to \(1\), which occurs exactly when \(\cos^2(x) = 0\) and \(\sin^2(x)=0.\)

But in the given range \(\cos^2(x) =0\) at \(x=\frac{\pi}{2}\) and \(x=\frac{3\pi}{2}\) whereas \(\sin^2(x)=0\) at \(x=0\) and \(x=\pi\) (in fact, \(\cos(x)\) and \(\sin(x)\) can *never* be zero together). So there is no common solution.

The answer is a.

### Method 2

Multiply the equation by \(2^{\sin^2(x)}\). This gives us

\[(2^{\sin^2(x)})^2 + 2^{\cos^2(x)+\sin^2(x)} =2(2^{\sin^2(x)})\] or \[(2^{\sin^2(x)})^2 -2(2^{\sin^2(x)}) + 2 = 0.\] We can rewrite this as \[(2^{\sin^2(x)} -1)^2 = -1,\]

which clearly has no real solutions, so the answer is a.
