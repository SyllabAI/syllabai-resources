---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/combining-functions/r9527
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- combining-functions
- type/review-question
resource_identity:
  ugm_id: r9527
  station: combining-functions
  station_title: Combining Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9527
  old_site_id: Q187
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: combining-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: combining-functions
    validation_status: SUGGESTED
  spec_points:
  - code: 1.2.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: 'Canonical composition builder: fg vs gf order, powers f^i, all forms yielding 4x+4, f^i
        g f^j g^k.'
      rationale: 'Canonical UGM title: “Can we compose two simple functions?”; exam provenance: Oxford
        (MAT) 2012 Q[''Q2'']'
      validation_status: SUGGESTED
    title: identify the range of a given function in simple cases, and find the composition of two given
      functions condition that a composite function
  - code: 1.2.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: 'Canonical composition builder: fg vs gf order, powers f^i, all forms yielding 4x+4, f^i
        g f^j g^k.'
      rationale: 'Canonical UGM title: “Can we compose two simple functions?”; exam provenance: Oxford
        (MAT) 2012 Q[''Q2'']'
      validation_status: SUGGESTED
    title: understand the terms function, domain, range, one-one function, inverse function and composition
      of functions
  mapped_date: '2026-10-23'
  mapper: cross-map-functions.json (P3c) @ syllabai-experimental 4a592ed0
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford (MAT) 2012 Q['Q2']
task: T-UGM-IMPORT-2
assets:
- path: https://undergroundmathematics.org/combining-functions/r9527/images/fg.png
  kind: figure
---

# Can we compose two simple functions?

## Question

Let \[f(x)=x+1\qquad\text{and}\qquad g(x)=2x.\] We will, for example, write \(fg\) to denote the function “perform \(g\) then perform \(f\)” so that \[fg(x)=f(g(x))=2x+1.\] If \(i\geq 0\) is an integer we will, for example, write \(f^i\) to denote the function which performs \(f\) \(i\) times, so that \[f^i(x)=\underbrace{fff......f}_\text{$i\,\text{times}$}(x)=x+i.\]

1. Show that \[f^2g(x)=gf(x).\]
2. Note that \[gf^2g(x)=4x+4.\] Find all the other ways of combining \(f\) and \(g\) that result in the function \(4x+4\).
3. Let \(i,j,k\geq0\) be integers. Determine the function \[f^igf^jgf^k(x).\]
4. Let \(m\geq0\) be an integer. How many different ways of combining the functions \(f\) and \(g\) are there that result in the function \(4x+4m\)?

## Suggestion

Can we use part (iii) of this question here? How many times do we need to do \(g\)? And \(f\)?

## Solution

\[f^2g(x)=f(f(g(x)))=((2x)+1)+1=2x+2=2(x+1)=g(f(x))=gf(x).\]

---

When a question asks for all ways of doing something, or all solutions, we need to find a way to show we haven’t missed any. Also, question parts are often closely related and the earlier parts can be very useful for answering the later parts.

Since we need to make \(4x+4\), we must need two \(g\)s and between one and four \(f\)s in some order. Using the equation from part one, we have \[gf^2g(x)=g(f^2g)(x)=g(gf)(x)=g^2f(x)\] and \[gf^2g(x)=(gf)fg(x)=(f^2g)fg(x)\] which gives \[f^2gfg(x)=f^2(gf)g(x)=f^2(f^2g)g(x)=f^4g^2(x)\] and any more rearrangements would just take us back to one of these options.

Therefore the four possible ways are: \[gf^2g(x),\quad g^2f(x),\quad f^2gfg(x),\quad f^4g^2(x)\] and nothing else.

The four ways are shown in this diagram in green, blue, orange and purple.

> [figure: diagram showing the four paths from x to 4 x plus 4 — `https://undergroundmathematics.org/combining-functions/r9527/images/fg.png`] (image not included in the text import; path of record).

---

From the example in the question, \(f^i(x)=x+i\), so, \[f^igf^jgf^k(x)=2(2(x+k)+j)+i=4x+i+2j+4k\]

---

For any m, there will still only be two \(g\)s.

Thus any function will be of the form \(f^igf^jgf^k(x)\) with integers \(i,j,k\geq 0\) as in part (iii) with \[i+2j+4k=4m\]

### Approach 1

Since \(i,j\geq0\), the value of k is constrained by \(0\leq k\leq m\).

Then, given k, the value of j is constrained by \(0\leq j\leq 2m-2k\), since \(i\geq 0\) and \(i+2j=4m-4k\).

Once

\(j\)

and

\(k\)

are determined,

\[i=4m-4k-2j,\]

so

\(i\)

is also uniquely determined. Therefore the number of possible solutions is:

\[\begin{align*} \sum_{k=0}^m \bigg(\sum_{j=0}^{2m-2k}&1\bigg)\\ &=\sum_{k=0}^m2m-2k+1\\ &=\sum_{k=0}^m(2m+1)-2\sum_{k=0}^mk\\ &=(m+1)(2m+1)-2\times \frac{1}{2} m(m+1)\\ &=(m+1)^2. \end{align*}\]

### Approach 2

So how many ways are there of picking \(i, j\) and \(k\) so that \(i+2j+4k=4m\)? We can draw up a table.

| \(k\) | \(m\) | \(m-1\) | \(m-1\) | \(m-1\) | \(m-2\) | \(m-2\) | \(m-2\) | \(m-2\) | \(m-2\) | \(m-3\) | \(\ldots\) | \(0\) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| \(j\) | \(0\) | \(2\) | \(1\) | \(0\) | \(4\) | \(3\) | \(2\) | \(1\) | \(0\) | \(6\) | \(\ldots\) | \(0\) |
| \(i\) | \(0\) | \(0\) | \(2\) | \(4\) | \(0\) | \(2\) | \(4\) | \(6\) | \(8\) | \(0\) | \(\ldots\) | \(4m\) |

So adding up the possibilities, we have \(1 + 3 + 5 + ... + (2m+1) = (m+1)^2\), since this is an arithmetic series with \(a = 1, d = 2, n = m+1\).
