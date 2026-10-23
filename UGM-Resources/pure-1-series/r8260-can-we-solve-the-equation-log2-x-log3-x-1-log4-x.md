---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/exp-and-log/r8260
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- exp-and-log
- type/review-question
resource_identity:
  ugm_id: r8260
  station: exp-and-log
  station_title: Exponentials & Logarithms
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8260
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: exp-and-log
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: exp-and-log
    validation_status: SUGGESTED
  spec_points:
  - code: 1.6.3
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: part 1 proves the GP-term log identity via a = AR^{p-1} (part 2 is a log-change-of-base
        equation — exp-and-log bearing)
      rationale: 'Canonical UGM title: "Can we solve the equation $\log_2 x + \log_3 x = 1 + \log_4
        x$?"; exam provenance: UCLES A level Pure Mathematics 1, 1973, Q1'
      validation_status: SUGGESTED
    title: use the formulae for the n th term and for the Including knowledge that numbers sum of the
      first n terms to solve problems involving arithmetic or geometric progressions equivalent).
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Pure Mathematics 1, 1973, Q1
task: T-UGM-IMPORT-6
---

# Can we solve the equation $\log_2 x + \log_3 x = 1 + \log_4 x$?

## Question

1. If \(a\), \(b\), \(c\) are positive and are the \(p\)th, \(q\)th, \(r\)th terms of a geometric progression prove that \[\begin{equation*} (q-r) \log a + (r-p) \log b + (p-q) \log c = 0. \end{equation*}\]

---

1. Solve the equation \(\log_2 x + \log_3 x = 1 + \log_4 x\), giving your answer to three significant figures.

## Suggestion

Typically, we’d use \(a\) for the first term of the geometric progression and \(r\) for the common ratio, but that would be bad here, as \(a\) and \(r\) have already been used in the question…

What are the \(p\)th, \(q\)th and \(r\)th terms of the geometric progression, anyway?

Also note that the question does not specify the base of the logarithms, so presumably this should be true for any base.

Hmm, all of these logs have different bases. That seems very awkward. What can we do to simplify things?

## Solution

If the geometric progression has first term

\(A\)

and common ratio

\(R\)

, then

\[\begin{align*} a &= A R^{p-1},\\ b &= A R^{q-1},\\ c &= A R^{r-1}, \end{align*}\]

where

\(A \ne 0\)

. By taking logarithms (to whichever base we like), we have

\[\begin{align*} \log a &= \log A + (p-1) \log R,\\ \log b &= \log A + (q-1) \log R,\\ \log c &= \log A + (r-1) \log R. \end{align*}\]

Consequently, we can just do lots of algebra to show that the result is true:

\[\begin{align*} &(q-r) \log a + (r-p) \log b + (p-q) \log c \\ &\quad= \bigl( (q-r) + (r-p) + (p-q) \bigr) \log A + \bigl( (q-r)(p-1) + (r-p)(q-1) + (p-q)(r-1) \bigr) \log R \\ &\quad= ( qp - rp -q+r +rq - pq -r+p+ pr - qr -p+q) \log R \\ &\quad= 0. \end{align*}\]

This argument is unenlightening; it gives no idea of why the result should be true. Another way of thinking about it is to observe that

\[\dfrac{b}{a} = R^{q-p}\quad\text{and}\quad \dfrac{c}{a} = R^{r-p}.\]

If we now raise the first of these equations to the power of \(r-p\) and the second to the power of \(q-p\), we find that \[\left(\dfrac{b}{a}\right)^{r-p}=\left(\dfrac{c}{a}\right)^{q-p}.\]

Now taking logs gives \((r-p)(\log b-\log a)=(q-p)(\log c-\log a)\), and rearranging this gives us the required identity.

Let’s rewrite the logarithms, so that they’re all to the same base. We use the [change of base formula](https://undergroundmathematics.org/glossary/logarithm-laws) to do this. (There is more on this topic in [Changing bases](https://undergroundmathematics.org/exp-and-log/changing-bases).) We may as well use base \(10\) for our logarithms, so we have \[\log_a x=\frac{\log_{10} x}{\log_{10} a}.\]

Our equation then becomes \[\frac{\log_{10} x}{\log_{10} 2} + \frac{\log_{10} x}{\log_{10} 3} = 1 + \frac{\log_{10} x}{\log_{10} 4}.\] This is now a linear equation in \(\log_{10} x\), so we can simply rearrange it to solve it: \[\left( \frac{1}{\log_{10} 2} + \frac{1}{\log_{10} 3} - \frac{1}{\log_{10} 4} \right)\log_{10} x = 1\] so that \[\log_{10} x = 1\biggm/\left(\frac{1}{\log_{10} 2} + \frac{1}{\log_{10} 3} - \frac{1}{\log_{10} 4} \right)\approx 0.266\,179\] Exponentiating both sides with base \(10\) gives \[x\approx 10^{0.266\,179}\approx 1.85\] to 3 significant figures.

Alternatively, we can say, let \(\log_2x = a\), \(\log_3x=b\), \(\log_4x=c\), so the equation becomes, \(a + b = 1 + c\).

Now \(\log_4x = c\) implies \(4^c=x = 2^a\), and as \(4^c = 2^{2c}\), we have \(a = 2c\). Thus the equation simplifies to \(b+c=1\).

We have \(x=3^b = 4^c\) and \(b=1-c\), so \(3^{1-c}= 4^c\). Taking logarithms of both sides (to a base of our choice) gives \((1-c)\log 3=c\log 4\), and so \(c = \dfrac{\log 3}{\log 4 + \log 3}\). (A particularly nice base to pick is \(3\), in which case this simplifies to \(\dfrac{1}{\log_3 4+1}\).)

Thus \(x = 4^c = 4^{\log 3/(\log 4 + \log 3)} = 1.85\) to \(3\) significant figures.
