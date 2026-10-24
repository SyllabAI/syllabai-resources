---
created: 2026-10-24T22:06:39 (UTC +06:00)
source: https://undergroundmathematics.org/exp-and-log/r7231
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- exp-and-log
- type/review-question
resource_identity:
  ugm_id: r7231
  station: exp-and-log
  station_title: Exponentials & Logarithms
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7231
  old_site_id: "Q146"
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
  - code: 3.2.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-10 cross-map (cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af)"
      evidence: "largest of log_2 3, log_4 8, log_3 2, log_5 10 - 'if 0 < b < a then log_a b < 1' plus exact values (log_4 8 = 3/2)"
      rationale: "Canonical UGM title: Which is the largest of these four logarithms?"
      validation_status: SUGGESTED
    title: "understand the relationship between logarithms and indices, and use the laws of logarithms (excluding change of base)"
  mapped_date: '2026-10-25'
  mapper: cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "Oxford University Mathematics Aptitude Test, 2010, Q1E"
  task: T-UGM-IMPORT-10
---

# Which is the largest of these four logarithms?

## Question

Which is the largest of the following four numbers?

1. \(\log_2 3\),

---

1. \(\log_4 8\),

---

1. \(\log_3 2\),

---

1. \(\log_5 10\).

## Suggestion

Can we evaluate any of the logarithms exactly?

What do we know about \(\log_a b\) when \(0 < b < a\)?

## Solution

Useful fact; if \(0 < b < a\) then \(\log_ab < 1\), since \(b < a^1\).

Firstly, we notice that \(\log_3 2 <1\), while the other logarithms are greater than one, so (c) cannot be the answer.

Secondly, we might want to calculate some of the logarithms.

Useful fact; suppose we know logs to base \(j\) and want to know logs to base \(k\).

Then if \(\log_kx = y\), we have \(x = k^y\), and taking logs to base \(j, \log_jx = y\log_jk\), so \(y = \log_kx = \dfrac{\log_jx}{\log_jk}\) .

Since both \(4\) and \(8\) are powers of \(2\), \(\log_4 8\) can be easily calculated. \[\log_4 8= \frac{\log_2 8}{\log_2 4}= \frac{3}{2}\]

At this point we will compare \(\log_2 3\) and \(\log_5 10\) with \(\frac{3}{2}\).

The \(\iff\) symbol is really useful. \(A \iff B\) means that \(A\) is true if, and only if, \(B\) is true. Another way to say this is that \(A\) implies \(B\), and \(B\) implies \(A\); \(A\) and \(B\) are always true together, or false together.

We start by supposing \(\log_2 3> \frac{3}{2}\) and follow through the logical implications to see if it is true. \[\log_2 3> \frac{3}{2} \iff 2\log_2 3>3 \iff \log_2 9>3 \iff 9>2^3 \text{, which is true.}\] Therefore, \(\log_2 3>\log_4 8\). Similarly, \[\log_5 10< \frac{3}{2} \iff \log_5 100 < 3\iff 100<5^3\text{, which is true.}\] Hence, \(\log_5 10<\log_4 8\). From the results above, we can conclude that the biggest number is \(\log_2 3\), so the answer is (a).

Alternatively, we could argue we know the biggest is either \(\log_23=x\), or \(\log_510 = y\).

So \(2^x =3\), and since \(2\sqrt2 = 2(1.414...) < 3\), \(x > 1.5\).

But \(5^y = 10\), so \(5^{y-1} = 2\), and since \(\sqrt5 > 2, y-1 < 0.5\), so \(y < 1.5\). So \(x\) is the biggest.
