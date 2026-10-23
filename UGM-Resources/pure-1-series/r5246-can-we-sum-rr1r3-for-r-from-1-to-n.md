---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r5246
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r5246
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5246
  old_site_id: Q124
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
  spec_points: []
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md
    rule 3: coverage is never manufactured)'
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Further Mathematics Scholarship paper, 1952, Q3
task: T-UGM-IMPORT-6
---

# Can we sum $r(r+1)(r+3)$ for $r$ from $1$ to $n$?

## Question

Evaluate:

1. \(\sum_{r=1}^{n}r(r+1)(r+3)\);

---

1. \(\sum_{r=1}^n \dfrac{1}{r(r+1)(r+3)}\).

## Suggestion

Evaluate:

1. \(\sum_{r=1}^n \dfrac{1}{r(r+1)(r+3)}\).

How can we rewrite \(\dfrac{1}{r(r+1)(r+3)}\) in a way that might be useful? Could we use partial fractions?

Or alternatively, if we write the numerator as \(r+1-r\), can we now split the fraction into two fractions which both have terms that cancel?

## Solution

We multiply the brackets out, giving

\[\begin{align*} \sum_{r=1}^{n}r(r+1)(r+3) &= \sum_{r=1}^{n}(r^3+4r^2+3r) \\ &= \sum_{r=1}^{n}r^3+4\sum_{r=1}^{n}r^2+3\sum_{r=1}^{n}r. \end{align*}\]

Since we know \[\sum_{r=1}^{n}r^3=\frac{n^2(n+1)^2}{4}, \sum_{r=1}^{n}r^2=\frac{n(n+1)(2n+1)}{6}, \sum_{r=1}^{n}r=\frac{n(n+1)}{2},\] we see that \[\sum_{r=1}^{n}r(r+1)(r+3)=\frac{n^2(n+1)^2}{4}+4\frac{n(n+1)(2n+1)}{6}+3\frac{n(n+1)}{2},\] so \[\sum_{r=1}^{n}r(r+1)(r+3)=\frac{3n^2(n+1)^2+8n(n+1)(2n+1)+18n(n+1)}{12}.\]

We can now take out the common factor

\(n(n+1)\)

, to get

\[\begin{align*} \sum_{r=1}^{n}r(r+1)(r+3) &= \frac{n(n+1)[3n(n+1)+8(2n+1)+18]}{12} \\ &= \frac{n(n+1)(3n^2+19n+26)}{12} \\ &= \frac{n(n+1)(n+2)(3n+13)}{12}. \end{align*}\]

This looks like a

telescoping sum

; our only problem is that we have three numbers in the denominator. We can deal with that by rewriting the

\(1\)

in the numerator as

\(r+1-r\)

, so

\[\begin{align*} \sum_{r=1}^n \frac{1}{r(r+1)(r+3)} &= \sum_{r=1}^n\left( \frac{r+1}{r(r+1)(r+3)}-\frac{r}{r(r+1)(r+3)}\right) \\ &= \sum_{r=1}^n \frac{1}{r(r+3)}-\sum_{r=1}^n \frac{1}{(r+1)(r+3)}. \end{align*}\]

Now we will compute the two sums separately. For the first one, we have

\[\begin{align*} \sum_{r=1}^{n} \frac{1}{r(r+3)} &= \frac{1}{3}\sum_{r=1}^n \frac{r+3-r}{r(r+3)} \\ &= \frac{1}{3} \sum_{r=1}^{n}\left(\frac{1}{r}-\frac{1}{r+3}\right). \end{align*}\]

Since

\[\sum_{r=1}^{n}\frac{1}{r+3}=\sum_{r=4}^{n+3}\frac{1}{r},\]

we have

\[\begin{align*} \sum_{r=1}^{n} \frac{1}{r(r+3)} &= \frac{1}{3}\left(\sum_{r=1}^{n}\frac{1}{r}-\sum_{r=4}^{n+3}\frac{1}{r}\right) \\ &= \frac{1}{3}\left(1+\frac{1}{2}+\frac{1}{3}+\sum_{r=4}^{n}\frac{1}{r}-\sum_{r=4}^{n}\frac{1}{r}-\frac{1}{n+1}-\frac{1}{n+2}-\frac{1}{n+3}\right) \\ &= \frac{1}{3}\left(1+\frac{1}{2}+\frac{1}{3}-\frac{1}{n+1}-\frac{1}{n+2}-\frac{1}{n+3}\right). \end{align*}\]

For the second one we will try a similar approach. We have \[\sum_{r=1}^n \frac{1}{(r+1)(r+3)} = \frac{1}{2}\sum_{r=1}^{n}\frac{(r+3)-(r+1)}{(r+1)(r+3)}=\frac{1}{2}\sum_{r=1}^{n}\left(\frac{1}{r+1}-\frac{1}{r+3}\right).\] Similarly to before, we have \[\sum_{r=1}^n \frac{1}{(r+1)(r+3)}=\frac{1}{2}\left(\frac{1}{2}+\frac{1}{3}-\frac{1}{n+2}-\frac{1}{n+3}\right).\]

By combining the results for the two sums, we get

\[\begin{align*} &\sum_{r=1}^n \frac{1}{r(r+1)(r+3)} \\ & \qquad = \frac{1}{3}\left(1+\frac{1}{2}+\frac{1}{3}-\frac{1}{n+1}-\frac{1}{n+2}-\frac{1}{n+3}\right)-\frac{1}{2}\left(\frac{1}{2}+\frac{1}{3}-\frac{1}{n+2}-\frac{1}{n+3}\right) \\ & \qquad = \frac{1}{3}+\frac{1}{6}+\frac{1}{9}-\frac{1}{4}-\frac{1}{6}-\frac{1}{3(n+1)}+\left(\frac{1}{n+2}+\frac{1}{n+3}\right)\left(\frac{1}{2}-\frac{1}{3}\right) \\ & \qquad = \frac{7}{36}-\frac{1}{3(n+1)}+\frac{2n+5}{6(n+2)(n+3)} \\ & \qquad = \frac{7}{36}+\frac{(2n+5)(n+1)-2(n+2)(n+3)}{6(n+1)(n+2)(n+3)} \\ & \qquad = \frac{7}{36}-\frac{3n+7}{6(n+1)(n+2)(n+3)}. \end{align*}\]

We could alternatively write \(\dfrac{1}{r(r+1)(r+3)} = \dfrac{A}{r}+\dfrac{B}{r+1}+\dfrac{C}{r+3}\). Finding the constants in the usual way gives \[\dfrac{1}{r(r+1)(r+3)} = \dfrac{1/3}{r}-\dfrac{1/2}{r+1}+\dfrac{1/6}{r+3}.\] Note that \(\dfrac{1}{3}-\dfrac{1}{2}+\dfrac{1}{6} = 0\), which means that most of the terms cancel (as before). This leaves us with \[\sum_{r=1}^n \frac{1}{r(r+1)(r+3)} = \dfrac{11}{18}-\dfrac{5}{12}-\dfrac{1}{2(n+1)}+\dfrac{1}{6}\left(\dfrac{1}{n+1}+\dfrac{1}{n+2} + \dfrac{1}{n+3}\right)\] \[= \frac{7}{36}-\frac{3n+7}{6(n+1)(n+2)(n+3)}.\]

Check: when \(n = 2\), LHS \(= \dfrac{1}{8}+ \dfrac{1}{30}=\dfrac{19}{120}\), and RHS \(= \dfrac{7}{36}-\dfrac{13}{360} = \dfrac{19}{120}\).
