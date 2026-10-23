---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r8014
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r8014
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8014
  old_site_id: Q1014
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
      evidence: ΣC(n,r)=2^n, Vandermonde-style ℒ(2n,n) identity and the hockey-stick identity — binomial-theorem
        identities with combinatorial proofs
      rationale: 'Canonical UGM title: "Can we show $\binom{n}{r}=\binom{n-1}{r-1}+\binom{n-2}{r-1}+\binom{n-3}{r-1}+\dotsb+\binom{r-1}{r-1}$?";
        exam provenance: UCLES A level Further Mathematics B Special paper, 1984, Q1'
      validation_status: SUGGESTED
    title: use the expansion of ( a + b ) , where n is a positive integer
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Further Mathematics B Special paper, 1984, Q1
task: T-UGM-IMPORT-6
---

# Can we show $\binom{n}{r}=\binom{n-1}{r-1}+\binom{n-2}{r-1}+\binom{n-3}{r-1}+\dotsb+\binom{r-1}{r-1}$?

## Question

1. Prove that \[\sum_{r=0}^{n}\binom{n}{r}=2^n.\]

---

1. By considering the number of ways of choosing a set of \(n\) people from a set of \(2n\) people, or otherwise, prove that \[\binom{2n}{n}=\binom{n}{0}^2+\binom{n}{1}^2+\dotsb+\binom{n}{n}^2.\]

---

1. Prove that \[\binom{n}{r}=\binom{n-1}{r-1}+\binom{n-1}{r}\] and hence, or otherwise, prove that \[\binom{n}{r}=\binom{n-1}{r-1}+\binom{n-2}{r-1}+\binom{n-3}{r-1}+\dotsb+\binom{r-1}{r-1},\] where \(r\), \(n\) are positive integers with \(1 \leq r \leq n-1\).

## Suggestion

What does the binomial theorem give as the value of \((a+b)^n\)? What about \((1+a)^n\)?

Could we split our group of people into two groups of size \(n\)?

If we take 1 person from the first group, how many people do you have to take from the second to choose \(n\) people overall?

What if we take \(r\) people from the first group?

Could we write down the two factorial representations of \(\dbinom{n-1}{r-1}\) and \(\dbinom{n-1}{r}\)?

Or could we imagine a bag of \(n\) objects, and picking \(r\) from it?

\([...]\) and hence, or otherwise, prove that \[\binom{n}{r}=\binom{n-1}{r-1}+\binom{n-2}{r-1}+\binom{n-3}{r-1}+\dotsb+\binom{r-1}{r-1},\] where \(r\), \(n\) are positive integers with \(1 \leq r \leq n-1\).

We’ve just found an expression for \(\dbinom{n}{r}\) — how is this useful?

## Solution

Using the expression for the [binomial theorem](https://undergroundmathematics.org/glossary/binomial-theorem):

\[(a+b)^n=\sum_{r=0}^{n}\binom{n}{r}a^n\,b^{n-r},\]

if we set \(a=b=1\) then

\[(1+1)^n=2^n=\sum_{r=0}^{n}\binom{n}{r}1^n\,1^{n-r}=\sum_{r=0}^{n}\binom{n}{r},\]

as required.

The expression

\[\binom{n}{r}=\frac{n!}{r!(n-r)!}\]

gives the number of ways of choosing \(r\) objects from a set of \(n\) objects, without replacement.

If we want to choose \(n\) objects from \(2n\) objects, one way of doing this is to line up the \(2n\) objects and simply pick \(n\) objects from them.

The number of ways of doing this is then \(\dbinom{2n}{n}.\)

Alternatively we could split the \(2n\) objects into two equal groups of \(n\) objects, then choose \(r\) objects from the first group and \(n-r\) from the second.

Summing over all the possible values of \(r=\{0,\,1,\,2,\,\dotsb,n\}\) will give the total number of ways of doing this as \[\sum_{r=0}^{n}\binom{n}{r}\binom{n}{n-r}.\]

But we know by symmetry that \(\dbinom{n}{r} = \dbinom{n}{n-r}\), and so we have \[\dbinom{2n}{n} = \sum_{r=0}^{n}\dbinom{n}{r}^2.\]

There are \(\dbinom{n}{r}\) ways of choosing \(r\) people from \(n\) people.

If we now consider one specific person from among the \(n\) people, say James, our set of \(r\) people might include James or not.

If James is included, then there are \(\dbinom{n-1}{r-1}\) ways of choosing the other \(r-1\) people from the remaining \(n-1\) people.

If James is excluded, then there are \(\dbinom{n-1}{r}\) ways of choosing the \(r\) people from the remaining \(n-1\) people.

So there are \(\dbinom{n-1}{r-1}+\dbinom{n-1}{r}\) ways in total of choosing \(r\) people, hence

\[\binom{n-1}{r-1}+\binom{n-1}{r}=\binom{n}{r}.\]

Alternatively, we could start with the right hand side of the given expression. We have

\[\begin{align*} \binom{n-1}{r-1}+\binom{n-1}{r} &= \frac{(n-1)!}{(r-1)!(n-r)!}+ \frac{(n-1)!}{r!(n-r-1)!} \\ &= \frac{r(n-1)!}{r(r-1)!(n-r)!}+ \frac{(n-r)(n-1)!}{r!(n-r)(n-r-1)!} \\ &= \frac{r(n-1)!}{r!(n-r)!}+ \frac{(n-r)(n-1)!}{r!(n-r)!} \\ &= \frac{r(n-1)!+(n-r)(n-1)!}{r!(n-r)!} \\ &= \frac{n(n-1)!}{r!(n-r)!} \\ &= \frac{n!}{r!(n-r)!}=\binom{n}{r}. \end{align*}\]

\([...]\) and hence, or otherwise, prove that \[\binom{n}{r}=\binom{n-1}{r-1}+\binom{n-2}{r-1}+\binom{n-3}{r-1}+\dotsb+\binom{r-1}{r-1},\] where \(r\), \(n\) are positive integers with \(1 \leq r \leq n-1\).

Using the formula above repeatedly, we find

\[\begin{align*} \binom{n}{r} &= \binom{n-1}{r-1}+\binom{n-1}{r} \\ &= \binom{n-1}{r-1}+\left[\binom{n-2}{r-1}+\binom{n-2}{r}\right] \quad \text{etc.} \\ \end{align*}\]

We can see that as this builds up we always have

\(\dbinom{n-a}{r}\)

as the last term, but we want to end with

\(\dbinom{r-1}{r-1}\)

. If we note that

\(\dbinom{r}{r}=\dbinom{r-1}{r-1}=1\)

then we know to continue until

\(n-a=r\)

so

\(a=n-r\)

.

\[\begin{align*} \binom{n}{r} &= \binom{n-1}{r-1}+\binom{n-2}{r-1}+\dotsb+\left[\binom{n-(n-r)}{r-1}+\binom{n-(n-r)}{r}\right] \\ &= \binom{n-1}{r-1}+\binom{n-2}{r-1}+\dotsb+\binom{r}{r-1}+\binom{r}{r} \\ &= \binom{n-1}{r-1}+\binom{n-2}{r-1}+\dotsb+\binom{r}{r-1}+\binom{r-1}{r-1} \end{align*}\]
