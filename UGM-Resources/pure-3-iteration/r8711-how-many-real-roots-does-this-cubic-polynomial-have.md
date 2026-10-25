---
created: 2026-10-26T03:35:52 (UTC +06:00)
source: https://undergroundmathematics.org/polynomials/r8711
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- polynomials
- type/review-question
resource_identity:
  ugm_id: r8711
  station: polynomials
  station_title: Polynomials & Rational Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8711
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: polynomials
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: polynomials
    validation_status: SUGGESTED
  spec_points:
  - code: 3.6.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-14 cross-map (cross-map-p3-iteration.json (P3c
        lane 14) @ syllabai-experimental 2d93dd7)
      evidence: 'The purest sign-change search in the corpus: the solution tabulates f(x) across x=-2..6,
        reads three sign changes bracketing three real roots (''one between x=-2 and x=-1; one between
        1 and 2; a third between 5 and 6''), then hones the negative root between -1.3 and -1.2 (f(-1.25)=0.671875>0)
        to conclude x=-1.3 to one decimal place - locating a root by searching for a sign change and refining
        the bracket, the verbatim 3.6.1 skill.'
      rationale: 'Canonical UGM title: How many real roots does this cubic polynomial have?'
      validation_status: SUGGESTED
    title: locate approximately a root of an equation, by means of graphical considerations and/or searching
      for a sign change
  mapped_date: '2026-10-26'
  mapper: cross-map-p3-iteration.json (P3c lane 14) @ syllabai-experimental 2d93dd7
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-14
---

# How many real roots does this cubic polynomial have?

## Question

Show that the equation \(x^3 - 6x^2 + 12 = 0\) has two positive roots and one negative root. Show that the negative root lies between \(-1\) and \(-1.5\) and find it correct to one decimal place.

## Suggestion

If we cannot deduce directly how to factorise a polynomial, do we know a way of honing in on the location of (any) roots?

## Solution

Let \(f(x) = x^3 - 6x^2 + 12\), which is a cubic, and thus has at most three real roots. We can tabulate various values for \(f(x)\).

| \(x\) | \(f(x)\) |
|---|---|
| -2 | -20 |
| -1 | 5 |
| 0 | 12 |
| 1 | 7 |
| 2 | -4 |
| 3 | -15 |
| 4 | -20 |
| 5 | -13 |
| 6 | 12 |

The function \(f(x)\) changes sign three times in the table, so that \(f(x)\) has three real roots, one between \(x = -2\) and \(x = -1\); one between \(x = 1\) and \(x = 2\); and a third between \(x = 5\) and \(x = 6\).

So \(f(x)\) has two positive roots and one negative root.

Show that the negative root lies between \(-1\) and \(-1.5\)…

We saw above that \(f(-1) = 5\). As \(f(-1.5) = -\dfrac{39}{8} < 0\), the negative root must lie between \(x = -1\) and \(x = -1.5\).

…and find it correct to one decimal place.

We can tabulate more values for \(f(x)\).

| \(x\) | \(f(x)\) |
|---|---|
| -1.5 | -4.875 |
| -1.4 | -2.504 |
| -1.3 | -0.337 |
| -1.2 | 1.632 |
| -1.1 | 3.409 |
| -1 | 5.0 |

Thus the negative root lies between \(x = -1.3\) and \(x = -1.2\).

We have \(f(-1.25) = 0.671875 > 0\), and so the root falls between \(x = -1.3\) and \(x = -1.25\), so that, to one decimal place, the negative root is \(x = -1.3\).
