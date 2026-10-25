---
created: 2026-10-24T22:06:39 (UTC +06:00)
source: https://undergroundmathematics.org/exp-and-log/r9747
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- exp-and-log
- type/review-question
resource_identity:
  ugm_id: r9747
  station: exp-and-log
  station_title: Exponentials & Logarithms
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9747
  old_site_id: "Q1002"
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
      evidence: "'by taking logs, or otherwise, show that 5x10^47 < 3^100 < 6x10^47' and read off the first digit of 3^100; prior routing of record: lane-5 '2.2 Logarithmic and exponential functions'"
      rationale: "Canonical UGM title: Can we use $\\log_{10}$ to find the first digit of $3^{100}$?"
      validation_status: SUGGESTED
    title: "use logarithms to solve equations and e.g. inequalities in which the unknown appears in indices"
  mapped_date: '2026-10-25'
  mapper: cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "UCLES STEP Mathematics I, 2000, Q1"
  task: T-UGM-IMPORT-10
---

# Can we use $\log_{10}$ to find the first digit of $3^{100}$?

## Question

To nine decimal places, \(\log_{10}2=0.301029996\) and \(\log_{10}3=0.477121255\).

1. Calculate \(\log_{10}5\) and \(\log_{10}6\) to three decimal places. By taking logs, or otherwise, show that \[5\times 10^{47}<3^{100}<6\times 10^{47}.\]

Hence write down the first digit of \(3^{100}\).

1. Find the first digit of each of the following numbers: \(2^{1000}\); \(2^{10\,000}\); and \(2^{100\, 000}\).

## Solution

The laws of logs tell us that

\[\begin{align*} \log_{10}(ab)&=\log_{10}a+\log_{10}b, \\ \log_{10}(a^b)&=b\log_{10}a, \end{align*}\]

and combining the two we have that \[\log_{10}\left(\frac{a}{b}\right)=\log_{10}(ab^{-1})=\log_{10}a+\log_{10}b^{-1}=\log_{10}a-\log_{10}b.\]

Recall that \(\log_{10}10=1\), by definition. We have that \[\log_{10}5=\log_{10}\left(\frac{10}{2}\right)=\log_{10}10-\log_{10}2=1-0.301029996=0.699\] to three decimal places.

Similarly, we have that \[\log_{10}6=\log_{10}(3\times 2)=\log_{10}3+\log_{10}2=0.477121255+0.301029996=0.778\] to three decimal places.

Now we wish to show that \[5\times 10^{47}<3^{100}<6\times 10^{47}.\] We can calculate that \[\log_{10}(5\times 10^{47})=\log_{10}5+47\log_{10}10=0.699+47=47.699.\] Further, we have \[\log_{10}3^{100}=100\log_{10}3=47.712,\] to three decimal places. Finally, we find that \[\log_{10}(6\times 10^{47})=\log_{10}6+47\log_{10}10=0.778+47=47.778.\] Combining these, we have that \[\log_{10}(5\times 10^{47})<\log_{10}3^{100}<\log_{10}(6\times 10^{47}).\] Therefore \[10^{\log_{10}(5\times 10^{47})}<10^{\log_{10}3^{100}}<10^{\log_{10}(6\times 10^{47})},\] which is the same as \[5\times 10^{47}<3^{100}<6\times 10^{47}.\] From this we can see that \(5\) with \(47\) zeroes \(<3^{100}<\) \(6\) with \(47\) zeroes. This means that the first digit of \(3^{100}\) must be \(5\).

To nine decimal places, \(\log_{10}2=0.301029996\) and \(\log_{10}3=0.477121255\).

1. Find the first digit of each of the following numbers: \(2^{1000}\); \(2^{10\,000}\); and \(2^{100\, 000}\).

To answer this part we mimic the technique of the last part of part (i). That is, we find an integer \(n\) which satisfies \[n\times10^{m}<2^{1000}<(n+1)\times 10^m\] or \[\log_{10}(n\times10^{m})<\log_{10}2^{1000}<\log_{10}((n+1)\times 10^m),\] which tells us that the first digit of \(2^{1000}\) is \(n\). We have that \[\log_{10} 2^{1000}=1000\log_{10}2=301.29996.\] We know that \[\log_{10}10^{301}=301,\] so we need to check \[\log_{10}(2\times 10^{301})=\log_{10}2+301=301.301.\] Therefore \[1\times10^{301}<2^{1000}<2\times10^{301}.\] So the first digit of \(2^{1000}\) is \(1\).

Again, we study \[\log_{10}2^{10\,000}=10\,000\log_{10}2=3010.29996.\] This is again close to \(\log_{10}10^{3010}\), so we check \[\log_{10}(2\times 10^{3010})=\log_{10}2+3010=3010.301.\] So \[10^{3010}<2^{10\,000}<2\times10^{3010},\] which tells us that the first digit of \(2^{10\, 000}\) is \(1\).

Finally, we have that \[\log_{10}2^{100\,000}=100\,000\log_{10}2=30102.9996.\] This is very close to \(30103\), so let’s check \[\log_{10}(9\times 10^{30102})=\log_{10}3^2+30102=2\log_{10}3+30102=30102.9542.\] So we have that \[9\times 10^{30102}<2^{100\,000}<10^{30103},\] and so the first digit of \(2^{100\,000}\) is \(9\).

This is related to Benford’s Law, which states that the fractional part of the logarithm of random data is uniformly distributed between 0 and 1.

So, for instance, in a set of figures taken from real life, 1 is by far the most common first digit.

This has a neat application in fraud detection, in that most people ignore Benford’s Law when making up figures, and create their first digits in equal numbers.
