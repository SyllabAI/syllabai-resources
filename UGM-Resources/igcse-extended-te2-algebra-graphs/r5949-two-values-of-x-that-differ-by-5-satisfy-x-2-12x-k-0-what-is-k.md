---
created: 2026-11-04T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/polynomials/r5949
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- polynomials
- type/review-question
resource_identity:
  ugm_id: r5949
  station: polynomials
  station_title: Polynomials & Rational Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5949
  old_site_id: null
spec_map:
  curriculum_code: CIE-IGCSE-0580-2025
  lane: cie-igcse-maths-25-extended
  board: Cambridge CIE
  syllabus_version: 2025-2027
  subsection: polynomials
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: polynomials
    validation_status: SUGGESTED
  spec_points:
  - code: E2.5.6
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — the 0580 igcse-extended TE2 cross-map (generalisation
        lane 19) (cross-map-0580-te2-algebra-graphs.json @ syllabai-experimental 79088f34)
      evidence: Two values differing by 5 satisfy x^2-12x+k=0 — gentle root-structure solving; E2.5.6
        register.
      rationale: 'Canonical UGM title: “Two values of $x$ that differ by $5$ satisfy $x^2 - 12x + k =
        0$, what is $k$?”; exam provenance: O&C O level Additional Mathematics 2, QP F339, 1957, Q1

        Question reproduced by kind permission of Cambridge Assessment Group Archives. The question remains
        Copyright University of Cambridge Local Examinations Syndicate (“UCLES”),

        All rights reserved

        .'
      validation_status: SUGGESTED
  mapped_date: '2026-11-04'
  mapper: cross-map-0580-te2-algebra-graphs.json (P3c) @ syllabai-experimental 79088f34
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: 'O&C O level Additional Mathematics 2, QP F339, 1957, Q1

    Question reproduced by kind permission of Cambridge Assessment Group Archives. The question remains
    Copyright University of Cambridge Local Examinations Syndicate (“UCLES”),

    All rights reserved

    .'
task: T-UGM-IMPORT-19
---

# Two values of $x$ that differ by $5$ satisfy $x^2 - 12x + k = 0$, what is $k$?

## Question

1. The equation \(x^3 + ax + b = 0\) is satisfied by the values \(x = 1\) and \(x = 2\). Find the values of \(a\) and \(b\); and find also the third value of \(x\).
2. The equation \(x^2 - 12x + k = 0\) is satisfied by two values of \(x\) that differ by \(5\). Find these two values of \(x\), and the value of \(k\).

## Solution

1. The equation \(x^3 + ax + b = 0\) is satisfied by the values \(x = 1\) and \(x = 2\). Find the values of \(a\) and \(b\)…

Since \(x = 1\) satisfies the equation \(x^3 + ax + b = 0\), by substituting in this value we find that \[ 1^3 + a \times 1 + b = 0 \implies a + b = - 1. \]

Likewise, since \(x = 2\) satisfies the equation, we also have that \[ 2^3 + a \times 2 + b = 0 \implies 2a + b = -8. \]

We therefore have a pair of simultaneous equations:

\[\begin{align*} a + b &= -1, \\ 2a + b &= -8. \end{align*}\]

By writing the first equation as

\(a = -1 - b\)

and substituting this value into the second equation, we are led to a single equation in

\(b\)

, namely

\[\begin{align*} 2(-1-b) + b = -8 &\implies -2 - 2b + b = - 8 \\ &\implies b = 6. \end{align*}\]

Consequently, \(a = - 1 - b = -7\), and so the original polynomial is \(x^3 - 7x + 6\).

Check: \(2(-7) + 6 = -8\).

…and find also the third value of \(x\).

Since \(x = 1\) and \(x = 2\) are roots of the polynomial \(x^3 - 7x + 6\), we can write \[ x^3 - 7x + 6 = (x-1)(x-2)(x + \beta) \] for some real constant \(\beta\). Since the constant terms have to match, this implies that \[ 6 = (-1) \times (-2) \times \beta \implies \beta = 3. \] That is, \(x^3 - 7x + 6 = (x-1)(x-2)(x+3)\), and the third (and final) root of the polynomial is \(x = -3\).

Without any loss of generality, we can call the roots \(\gamma\) and \(\gamma + 5\). So

\[\gamma^2 - 12\gamma + k = 0, (\gamma+5)^2 - 12(\gamma+5)+k=0.\]

Subtracting the first equation from the second, we have \(10\gamma -35 = 0\), and so \(\gamma = \dfrac{7}{2}\).

We have \(k = 12\gamma - \gamma^2\), and so \(k = \dfrac{119}{4}.\)
