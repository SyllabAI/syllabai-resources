---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r7978
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r7978
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7978
  old_site_id: Q30
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: counting-and-binomials
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: counting-and-binomials
    validation_status: SUGGESTED
  spec_points:
  - code: 1.6.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: expand (x-y)^6 by the binomial theorem and evaluate (19 3/4)^6 to the nearest thousand
        — canonical (a-b)^n numerical question
      rationale: 'Canonical UGM title: "Can we use a binomial expansion to evaluate $\left(19\tfrac{3}{4}\right)^6$?";
        exam provenance: UCLES A level Mathematics 1, 1951, Q3'
      validation_status: SUGGESTED
    title: use the expansion of ( a + b ) , where n is a positive integer
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Mathematics 1, 1951, Q3
task: T-UGM-IMPORT-6
---

# Can we use a binomial expansion to evaluate $\left(19\tfrac{3}{4}\right)^6$?

## Question

Expand \((x-y)^6\) by the binomial theorem and use the result to evaluate \(\left(19\tfrac{3}{4}\right)^6\) correct to the nearest thousand.

[*Try to do this without touching your calculator!*]

## Suggestion

Expand \((x-y)^6\) by the binomial theorem…

Could we write out the expansion using the binomial formula? (We’ll need to be careful with the signs…)

Would the appropriate line of Pascal’s triangle help?

…and use the result to evaluate \(\left(19\tfrac{3}{4}\right)^6\) correct to the nearest thousand.

Can we choose sensible values for \(x\) and \(y\) such that \(x-y=19\tfrac{3}{4}\), making the calculations of \(x^n\) and \(y^n\) relatively easy?

Since we only need to know the result to the nearest thousand, can we ignore some terms of the expansion?

## Solution

Expand \((x-y)^6\) by the binomial theorem…

Using the binomial theorem, we have \[(a+b)^n=\sum\limits_{k=0}^n \binom{n}{k}a^{n-k}b^k.\] Substituting in the values \(n=6\), \(a=x\) and \(b=-y\), we get

\[\begin{align*} (x-y)^6 &= \binom{6}{0}x^6(-y)^0+\binom{6}{1}x^5(-y)^1+\binom{6}{2}x^4(-y)^2+\binom{6}{3}x^3(-y)^3 \\ &\quad + \binom{6}{4}x^2(-y)^4+\binom{6}{5}x^1(-y)^5+\binom{6}{6}x^0(-y)^6 \\ &= x^6(-y)^0 + \frac{6}{1} x^5(-y)^1 + \frac{6 \cdot 5}{2 \cdot 1} x^4(-y)^2 + \frac{6 \cdot 5 \cdot 4}{3 \cdot 2 \cdot 1} x^3(-y)^3 \\ &\quad + \frac{6 \cdot 5}{2 \cdot 1} x^2(-y)^4 + \frac{6}{1} x^1(-y)^5 + x^0(-y)^6 \\ &=x^6 -6x^5y+15x^4y^2-20x^3y^3+15x^2y^4-6xy^5+y^6 . \end{align*}\]

Alternatively we can use the fact that the 6th line of Pascal’s triangle is \(1\), \(6\), \(15\), \(20\), \(15\), \(6\), \(1\) and just write the final result down, being careful with signs. (If you do this, it’s a good idea to state that you’ve used the \(6^{\textrm{th}}\) line of Pascal’s triangle.)

…and use the result to evaluate \(\left(19\tfrac{3}{4}\right)^6\) correct to the nearest thousand.

Using

\(x=20\)

and

\(y=\frac{1}{4}\)

, we can substitute into the binomial expansion to get

\[\begin{align*} \left(19\tfrac{3}{4}\right)^6 & = 20^6 - 6 \times 20^5 \times \frac{1}{4} + 15 \times 20^4 \times \left(\frac{1}{4}\right)^2 - 20 \times 20^3 \times \left(\frac{1}{4}\right)^3 \\ &\qquad \qquad +\, 15 \times 20^2 \times \left(\frac{1}{4}\right)^4 - 6 \times 20 \times \left(\frac{1}{4}\right)^5 + \left(\frac{1}{4}\right)^6. \end{align*}\]

We need this result *to the nearest thousand,* so we can save ourselves some work and ignore the very last term straight away.

We can then work backwards through the terms, calculating their rough size to see whether we can ignore them in the approximation.

It’s helpful to write numbers in their prime factorisation (to help with cancelling) or in powers of \(10\) so we can keep tabs on how big the terms are.

- \(\left(\dfrac{1}{4}\right)^6 = 2^{-12}\) — ignore

- \(6\times 20\times \left(\dfrac{1}{4}\right)^5 = 3\times 10 \times 2^{-8}=\dfrac{30}{256}\) — ignore

- \(15\times 20^2 \times \left(\dfrac{1}{4}\right)^4 =3\times 5 \times 10^2 \times 2^{-6}=\dfrac{1500}{64}\) — ignore

- \(20^4\times \left(\dfrac{1}{4}\right)^3 = 10^4\times 2^{-2}=\dfrac{10000}{4}=2500\) — keep this.

The last three terms must be included in the approximation.

- \(15\times 20^4\times \left(\dfrac{1}{4}\right)^2 = 3\times 5 \times 10^4=150\,000\)

- \(6\times 20^5 \times \dfrac{1}{4} = 2^4\times 3\times 10^5=4\,800\,000\)

- \(20^6 = 2^6 \times 10^6=64\,000\,000\).

So to the nearest thousand,

\[\begin{align*} (19\tfrac{3}{4})^6 &\approx 64\,000\,000-4\,800\,000+150\,000-2500= 59\,347\,500 \\ &\approx 59\,348\,000. \end{align*}\]

The next term, \(\dfrac{1500}{64}\), is positive, so we definitely need to round up.

A computer tells us that the exact answer is \[\left(19\tfrac{3}{4}\right)^6=59\,347\,523.320556640625.\] It is interesting to note that including one more term would have given us the answer correct to the nearest whole number.
