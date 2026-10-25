---
created: 2026-10-24T22:06:39 (UTC +06:00)
source: https://undergroundmathematics.org/exp-and-log/see-the-power
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- exp-and-log
- type/building-blocks
- level/introducing
resource_identity:
  ugm_id: see-the-power
  station: exp-and-log
  station_title: Exponentials & Logarithms
  resource_type_id: 1
  resource_type_label: Building blocks
  level: Introducing
  ref: 5984
  old_site_id: "A4_RT2_4"
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
      evidence: "introduction to logarithms 'without formally defining them or even using the word': powers of ten estimated by inspection and interpolation (sqrt(10)~3.16) - the logarithm-as-index relationship made concrete"
      rationale: "Canonical UGM title: See the power"
      validation_status: SUGGESTED
    title: "understand the relationship between logarithms and indices, and use the laws of logarithms (excluding change of base)"
  mapped_date: '2026-10-25'
  mapper: cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-10
---

# See the power

> Excerpt: This problem is an introduction to logarithms, without formally defining them or even using the word.
Students are asked to estimate the power of ten needed to achieve a given value and hence solve an equation.

## Warm-up

Some equations involving powers or indices can be solved “by inspection” if we are familiar with the powers of common numbers. Try these

1. \(2^x = 16\)

---

1. \(10^x = 0.001\)

---

1. \(5^x = 125\)

---

1. \(\big(\frac{1}{3}\big)^x = 81\)

Check your answers

1. \(x = 4\) because \(16 = 2^4\)

---

1. \(x = -3\) because \(0.001 = \frac{1}{1000} = \frac{1}{10^3}\)

---

1. \(x = 3\)

---

1. \(x = -4\) because \(\big(\frac{1}{3}\big)^{-1} = 3\)

Some other equations look very similar but are not so easy to solve. Think about this one \[10^x = 562\] What could you do to find an approximate answer? How accurate could you make your estimate?

Suggestion

What are \(10^2\) and \(10^3\)? Can you state upper and lower bounds for the value of \(x\)?

How can you narrow down the range of possible values?

## Problem

Think about the function \(y=10^x\). Every time we increase \(x\) by one, we multiply \(y\) by \(10\).

By how much do we multiply \(y\) when we increase \(x\) by \(0.5\)?

Given that \(\sqrt{10}\approx 3.16\) and \(\sqrt[4]{10}\approx 1.78\), complete the table below.

| \(10^0=\) | \(10^{0.25}\approx\) | \(10^{0.5}\approx\) | \(10^{0.75}\approx\) |
|---|---|---|---|
| \(10^1=\) | \(10^{1.25}\approx\) | \(10^{1.5}\approx\) | \(10^{1.75}\approx\) |
| \(10^2=\) | \(10^{2.25}\approx\) | \(10^{2.5}\approx\) | \(10^{2.75}\approx\) |
| \(10^3=\) | \(10^{3.25}\approx\) | \(10^{3.5}\approx\) | \(10^{3.75}\approx\) |

What does the whole number part of the power of ten tell us about the value of \(y\)?

How is this connected with standard form?

Can you now find approximate solutions to the following equations?

1. \(10^x = 21\)

---

1. \(10^x = 5\,000\)

---

1. \(10^x = 562\,000\)

---

1. \(10^x = 0.00178\)

See the resource [1950s calculators](https://undergroundmathematics.org/exp-and-log/calculators1950) for a further exploration of this.

## Solution

To go from \(10^1\) to \(10^2\) we multiply by \(10\). When we add to the power we multiply the expression, so to go from \(10^1\) to \(10^2\) in two equal steps we would add \(0.5\) to the power twice and multiply the expression by the same number twice. The number by which we multiply must therefore be the square root of \(10\), such that \(10^{1+0.5+0.5}=10^1\times\sqrt{10}\times\sqrt{10}=10^2\).

Similarly, to do it in four steps we would have to multiply by the fourth root of \(10\) each time.

The first column of the table is easy to fill in with whole number powers of \(10\), remembering that \(a^0=1\) for any value of \(a\) (with the possible exception of \(a=0\)).

What is \(0^0\)?

Looking at the second row, when we move from \(10^1\) to \(10^{1.25}\) we are increasing the power of \(10\) by \(0.25\), so we multiply by \(\sqrt[4]{10}\approx1.78\). Moving from the first to the third column we are increasing the power by \(0.5\), which means we multiply by \(\sqrt{10}\approx3.16\). Moving from the third to the fourth column we are increasing the power of \(10\) by another \(0.25\), and so we multiply by \(1.78\).

Here is a completed table.

| \(10^0=1\) | \(10^{0.25}\approx1.78\) | \(10^{0.5}\approx3.16\) | \(10^{0.75}\approx5.62\) |
|---|---|---|---|
| \(10^1=10\) | \(10^{1.25}\approx17.8\) | \(10^{1.5}\approx31.6\) | \(10^{1.75}\approx56.2\) |
| \(10^2=100\) | \(10^{2.25}\approx178\) | \(10^{2.5}\approx316\) | \(10^{2.75}\approx562\) |
| \(10^3=1\,000\) | \(10^{3.25}\approx1\,780\) | \(10^{3.5}\approx3\,160\) | \(10^{3.75}\approx5\,620\) |

It is clear from the table that the whole number part of the power tells us how many digits will be in the whole number part of the value of the expression. For instance, \(10^{2.\text{anything}}\) will have three digits before the decimal point. This is a feature of powers of ten, which works because our counting system uses base-\(10\) numbers.

[Hexadecimal](https://undergroundmathematics.org/glossary/hexadecimal) is a counting system that uses base-\(16\) numbers and is especially useful in computer science. Here, the whole number part of \(x\) would tell us the number of digits in the hexadecimal representation of \(16^x\).

We could write \(5\,620\) in standard form as \(5.62\times10^3\). This \(3\) tells us the number has four digits, which is also what the \(3\)s in the last row of our table tell us.

Approximate solutions to the first two can be found by looking in the table above. Since \(21\) is between \(17.8\) and \(31.6\), \(x\) must be between \(1.25\) and \(1.5\). We could narrow this range by trial and improvement or by plotting a graph.

\(562\,000\) has six digits, so \(x\) must be \(5.\)something. From the right hand column of the table, the decimal part must be \(.75\). This separation of the whole number and decimal parts of the number is what we do when we write the number in standard form: \(562\,000=5.62\times10^5\).

To solve the final equation, it helps to first write the number in standard form: \(0.00178=1.78\times10^{-3}\) so we want \(-3+0.25\).

This gives us a set of approximate solutions as follows:

1. \(x \approx 1.3\)

---

1. \(x \approx 3.7\)

---

1. \(x \approx 5.75\)

---

1. \(x \approx -2.75\)

In each case, the value of \(x\) is the *power to which we have to raise \(10\) in order to get the target number*. This is known as the [logarithm](https://undergroundmathematics.org/glossary/logarithm) of the target number. Specifically it is the “logarithm to base \(10\)”, since we are working with powers of \(10\). You can check your answers using the \(\log\) or \(\log_{10}\) key on your calculator.
