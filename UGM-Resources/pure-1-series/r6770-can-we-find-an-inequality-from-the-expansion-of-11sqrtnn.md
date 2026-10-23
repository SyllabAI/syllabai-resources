---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r6770
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r6770
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6770
  old_site_id: Q2003
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
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: first three terms of [1+1/√n]^n truncated to prove an inequality — extension-level application
        of the expansion
      rationale: 'Canonical UGM title: "Can we find an inequality from the expansion of $[ 1+1/\sqrt{n}]^n$?";
        exam provenance: UCLES A level Pure Mathematics 1, 1980, Q5(b)'
      validation_status: SUGGESTED
    title: use the expansion of ( a + b ) , where n is a positive integer
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Pure Mathematics 1, 1980, Q5(b)
task: T-UGM-IMPORT-6
---

# Can we find an inequality from the expansion of $[ 1+1/\sqrt{n}]^n$?

## Question

By considering the first three terms of the binomial expansion of \(\left[ 1+\left(\dfrac{1}{\sqrt{n}}\right) \right]^n\), where \(n\) is an integer greater than \(1\), prove that \[\left[1+\left(\frac{1}{\sqrt{n}}\right)\right]^{n-2} \geq \tfrac{1}{2}n.\]

## Suggestion

Since \(n \geq 2\), we know that our expansion contains at least three terms.

Maybe we can obtain an inequality by throwing away the remaining terms?

What condition do these terms have to satisfy for this to be valid?

But the left-hand side has an exponent of \(n\) instead of \(n-2\). What can we do to fix this?

## Solution

Since \(n \geq 2\), we know that we have at least three terms in the binomial expansion (which in general has \(n+1\) terms).

Furthermore, we know every term is positive, since

\(1\)

and

\(1/\sqrt{n}\)

both are, which means we can truncate the sum to obtain an inequality. Hence

\[\begin{align*} \left[ 1+\frac{1}{\sqrt{n}} \right]^n &= \sum_{k=1}^n {n \choose k}\left(\frac{1}{\sqrt{n}}\right)^k \\ &= 1+n\frac{1}{\sqrt{n}}+\frac{n(n-1)}{2}\left(\frac{1}{\sqrt{n}}\right)^2+\cdots \\ &\geq 1+n\frac{1}{\sqrt{n}}+\frac{n(n-1)}{2}\left(\frac{1}{\sqrt{n}}\right)^2\\ &= 1+\sqrt{n}+\frac{n-1}{2}. \end{align*}\]

This looks promising, but the inequality we are trying to prove has \(n-2\) instead of \(n\) in the exponent on the left hand side.

To fix this, there are (at least) two approaches we can take.

**Approach 1: Divide through by \((1+1/\sqrt{n})^2\)**

The most direct approach is to simply divide both sides of our inequality by \((1+1/\sqrt{n})^2\).

After this, the left hand side is what we want, but the right hand side is a bit of a mess: \[\left[ 1+\frac{1}{\sqrt{n}} \right]^{n-2} \geq \frac{1+\sqrt{n}+\frac{n-1}{2}}{\left(1+\frac{1}{\sqrt{n}}\right)^2}.\]

To clean it up, we simplify the numerator and denominator of the right hand side. The numerator can be written over a common denominator to get

\[1+\sqrt{n}+\frac{n-1}{2}=\frac{1+2\sqrt{n}+n}{2}= \frac{1}{2}(1+\sqrt{n})^2.\]

(For the final step here, we noticed that \(1+2\sqrt{n}+n\) is the square of \(1+\sqrt{n}\).)

Similarly, the denominator can be expanded to get \[\left(1+\frac{1}{\sqrt{n}}\right)^2= \left(\frac{\sqrt{n}+1}{\sqrt{n}}\right)^2= \frac{1}{n}\left(1+\sqrt{n}\right)^2.\]

Substituting these back in we obtain

\[\left[ 1+\frac{1}{\sqrt{n}} \right]^{n-2} \geq \frac{\frac{1}{2}(1+\sqrt{n})^2}{\frac{1}{n}\left(1+\sqrt{n}\right)^2}=\tfrac{1}{2}n.\]

**Approach 2: Manipulate the right hand side to find hidden factors of \((1+1/\sqrt{n})\).**

In this less direct (but essentially equivalent) approach we manipulate the right hand side by looking for factors of \((1+1/\sqrt{n})\) that we can cancel from both sides.

For this it’s handy to note that we can write

\(n-1=(\sqrt{n}+1)(\sqrt{n}-1)\)

. Thus

\[\begin{align*} \left[ 1+\frac{1}{\sqrt{n}} \right]^n &\geq 1+\sqrt{n}+\frac{n-1}{2}. \\ &= 1+\sqrt{n}+\frac{(\sqrt{n}+1)(\sqrt{n}-1)}{2}. \\ &= (1+\sqrt{n})\left(1+\frac{\sqrt{n}-1}{2}\right). \\ &= (1+\sqrt{n})\left(\frac{\sqrt{n}+1}{2}\right). \\ &= \frac{1}{2}(1+\sqrt{n})^2 \\ \end{align*}\]

This still isn’t quite what we want — on the right hand side we have

\((1+\sqrt{n})\)

, when we want

\((1+1/\sqrt{n})\)

— but we can fix this by noting that

\((1+\sqrt{n})=\sqrt{n}(1+1/\sqrt{n})\)

. Thus

\[\begin{align*} \left[ 1+\frac{1}{\sqrt{n}} \right]^n &\geq \frac{1}{2}(1+\sqrt{n})^2 \\ &= \frac{1}{2}n\left[1+\frac{1}{\sqrt{n}}\right]^2, \\ \end{align*}\]

which, after dividing through by \((1+1/\sqrt{n})^2\), implies that \[\left[1+\frac{1}{\sqrt{n}}\right]^{n-2} \geq \frac{1}{2}n,\] as desired.

Is it important that \(n>1\)?

You might like to check if the inequality is true at \(n=1\), or \(n=0\). You might then consider what would happen if \(n\) was allowed to take non-integer real values.

Where do issues arise?

Below we draw the two curves $y = (1+1/\sqrt{x})^{x-2}$ (in green), and $y = x/2$ (in blue). We can see that for $x > 2$ (but not for $0 < x < 2$) the green curve is above the blue one.
