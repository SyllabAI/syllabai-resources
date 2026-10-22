---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r5682
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r5682
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5682
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: quadratics
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: quadratics
    validation_status: SUGGESTED
  spec_points:
  - code: 1.1.5
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: Substitution u = sqrt(xy) makes the simultaneous system a hidden quadratic.
      rationale: 'Canonical UGM title: “Can we solve the simultaneous equations $x + y + \sqrt{xy} = 39$
        and $x^2 + y^2 + xy = 741$?”; exam provenance: UCLES 1981 Q4(a)'
      validation_status: SUGGESTED
    title: recognise and solve equations in x which are quadratic in some function of x . tan
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1981 Q4(a)
task: T-UGM-IMPORT-1
---

# Can we solve the simultaneous equations $x + y + \sqrt{xy} = 39$ and $x^2 + y^2 + xy = 741$?

## Question

By substituting

\(x + y = S\)

and

\(xy = P^2\)

, or otherwise, solve the simultaneous equations

\[\begin{align*} x + y + \sqrt{\vphantom{1}xy} &= 39, \\ x^2 + y^2 + xy &= 741. \end{align*}\]

*The expression \(\sqrt{\vphantom{1}xy}\) denotes the positive square root of \(xy\).*

## Solution

Using the suggested substitution, the first equation becomes

\[\begin{equation} S+P=39.\label{eq:1} \end{equation}\]

Also,

\[S^2=x^2+y^2+2xy\]

so the second equation becomes

\[\begin{align} S^2-P^2&=741 \notag \\ (S-P)(S+P)&=741 \notag \\ S-P&=\frac{741}{39}=19. \label{eq:2} \end{align}\]

Solving \(\eqref{eq:1}\) and \(\eqref{eq:2}\) simultaneously, we obtain \(S=29\) and \(P=10\).

Thus \(x + y = 29\) and \(xy = 100\).

Combining these we have

\[\begin{align*} y&=29-x \\ x(29-x)&=100\\ x^2-29x+100&=0 \\ (x-25)(x-4)&=0\\ x&=25\text{ or }4 \end{align*}\]

The original equations are symmetrical in \(x\) and \(y\) so the values of \(x\) and \(y\) are \(25\) and \(4\) in either order.
