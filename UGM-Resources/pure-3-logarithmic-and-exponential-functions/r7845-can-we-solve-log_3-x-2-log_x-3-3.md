---
created: 2026-10-24T22:06:39 (UTC +06:00)
source: https://undergroundmathematics.org/exp-and-log/r7845
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- exp-and-log
- type/review-question
resource_identity:
  ugm_id: r7845
  station: exp-and-log
  station_title: Exponentials & Logarithms
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7845
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: exp-and-log
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: exp-and-log
    validation_status: SUGGESTED
  spec_points:
  - code: 3.2.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-10 cross-map (cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af)"
      evidence: "log_b a log_c b log_a c = 1 by rewriting as exponentials, then log_3 x + 2 log_x 3 = -3 solved via u = log_3 x"
      rationale: "Canonical UGM title: Can we solve $ \\log_3 x + 2 \\log_x 3 = -3$?"
      validation_status: SUGGESTED
    title: "use logarithms to solve equations and e.g. inequalities in which the unknown appears in indices"
  mapped_date: '2026-10-25'
  mapper: cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "UCLES A level Mathematics A 1, QP 840/1, 1978, Q1"
  task: T-UGM-IMPORT-10
---

# Can we solve $ \log_3 x + 2 \log_x 3 = -3$?

## Question

1. If \(a\), \(b\) and \(c\) are any positive numbers not equal to unity, show that \[\begin{equation*} \log_b a \log_c b \log_a c = 1. \end{equation*}\]

---

1. Find the values of \(x\) which satisfy the equation \[\begin{equation*} \log_3 x + 2 \log_x 3 = -3. \end{equation*}\]

## Suggestion

How can we rewrite the equation \(\log_a b = c\) in a way that does not include logarithms?

## Solution

**Approach 1: Rewriting logarithms as exponentials**

Let \(\log_b a = x\), \(\log_c b = y\), and \(\log_a c = z\) so that, by definition, \(b^x = a\), \(c^y = b\), and \(a^z = c.\)

Thus \(a = b^x = (c^y)^x =c^{xy} = (a^z)^{xy} = a^{xyz}\), which implies that \(xyz = 1\), that is, \(\log_b a \log_c b \log_a c = 1.\)

**Approach 2: Changing the base of logarithms**

If \(\log_ab=c\), then \(a^c=b\). If we now take logs to base \(d \ne 1\), then \[\log_d(a^c) = \log_d b \implies c\log_d a = \log_d b.\]

So we have \[c = \log_a b = \frac{\log_db}{\log_da},\] and thus we can find logs to base \(a\) if we know logs to base \(d \ne 1\).

This means \[\log_ab\log_bc\log_ca = \dfrac{\log_db}{\log_da}\dfrac{\log_dc}{\log_db}\dfrac{\log_da}{\log_dc}=1,\] as required.

The numbers \(a\), \(b\) and \(c\) cannot be 1 since `logs to base 1’ makes no sense.

Can this result be generalised beyond three variables?

**Approach 1: Rewriting logarithms as exponentials**

Let \(\log_3 x = y\) and \(\log_x 3 = z\), so that \(3^y = x\) and \(x^z = 3\). Thus \(3 = x^z = (3^y)^z = 3^{yz}\), which implies that \(yz = 1\).

We also have \(y + 2z = -3\). Solving these two equations simultaneously gives \[(-2z-3)z = 1 \implies 2z^2 + 3z + 1 = 0 \implies (2z+1)(z+1) = 0.\]

Thus \(z = -\dfrac{1}{2}\) or \(-1\), and hence \(x = \dfrac{1}{3}\) or \(\dfrac{1}{9}\).

**Approach 2: Changing the base of logarithms**

From our work on changing bases above, we have \(\log_ab=\dfrac{\log_bb}{\log_ba} = \dfrac{1}{\log_ba}\).

Thus we have

\[\begin{equation*} \log_3 x + 2 \log_x 3 = -3 \iff \log_3 x + \frac{2}{\log_3 x} = -3. \end{equation*}\]

If we take

\(u = \log_3 x \ne 0\)

, this equation is equivalent to

\[\begin{align*} u + \frac{2}{u} = -3 &\iff u^2 + 3u + 2 = 0 \\ &\iff (u+2)(u+1) = 0 \\ &\iff u = -1 \quad\text{or}\quad u = -2 \\ &\iff \log_3 x = -1 \quad\text{or}\quad \log_3 x = -2 \\ &\iff x = \frac{1}{3} \quad\text{or}\quad x = \frac{1}{9}. \end{align*}\]
