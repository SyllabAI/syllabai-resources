---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/r6143
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/review-question
resource_identity:
  ugm_id: r6143
  station: sequences
  station_title: Sequences
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6143
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: sequences
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: sequences
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
  exam_reference: UCLES STEP Mathematics I, 2003, Q1
task: T-UGM-IMPORT-6
---

# Find an expression for the sum of $r^2$

## Question

It is given that \(\sum\limits_{r=-1}^n r^2\) can be written in the form \(pn^3+qn^2+rn+s\), where \(p,q,r\) and \(s\) are numbers. By setting \(n=-1,0,1\) and \(2\), obtain four equations that must be satisfied by \(p,q,r\) and \(s\) and hence show that \[\sum_{r=0}^n r^2=\frac{1}{6}n(n+1)(2n+1).\] Given that \(\sum\limits_{r=-2}^n r^3\) can be written in the form \(an^4+bn^3+cn^2+dn+e\), show similarly that \[\sum_{r=0}^n r^3=\frac{1}{4}n^2(n+1)^2.\]

## Solution

There are ways that we could work out that \(\sum\limits_{r=0}^n r^2\) will be a cubic function, even if we didn’t know the result stated above. You might like to look at [Sum estimating](https://undergroundmathematics.org/sequences/sum-estimating) to explore this idea.

Let’s substitute

\(n=-1,0,1\)

and

\(2\)

into the equation

\(\sum_{r=-1}^n r^2=pn^3+qn^2+rn+s.\)

We find

\[\begin{align}\label{1} n=-1 \qquad 1&=-p+q-r+s, \\ \label{2} n=0 \qquad 1&=s, \\ \label{3} n=1 \qquad 2&=p+q+r+s, \\ \label{4} n=2 \qquad 6&= 8p+4q+2r+s. \end{align}\]

Equation

\(\eqref{2}\)

tells us that

\(s=1\)

, and so the other three equations become

\[\begin{align}\label{1pr} -p+q-r&=0, \\ \label{2pr} p+q+r&=1, \\ \label{3pr} 8p+4q+2r&=5. \end{align}\]

Adding equations

\(\eqref{1pr}\)

and

\(\eqref{2pr}\)

, we find that

\[ 2q=1, \]

and so we have that

\[ q=\frac{1}{2}. \]

Substituting this into our equations leaves us with two remaining;

\[\begin{align} \label{1prpr} p+r&=\frac{1}{2}, \\ \label{2prpr} 8p+2r&=3. \end{align}\]

Equation \(\eqref{1prpr}\) tells us that \(r=\dfrac{1}{2}-p\), and substituting this into equation \(\eqref{2prpr}\) tells us that \[8p+2\left(\frac{1}{2}-p\right)=3,\] which we rearrange to find that \[6p=2 \implies p=\frac{1}{3}.\] Therefore \[r=\frac{1}{2}-p=\frac{1}{2}-\frac{1}{3}=\frac{1}{6}.\] We’ve calculated that \[\sum_{r=-1}^n r^2=\frac{1}{3}n^3+\frac{1}{2}n^2+\frac{1}{6}n+1.\] Finally, we write \[\sum_{r=0}^n r^2=\sum_{r=-1}^n r^2-1=\frac{1}{3}n^3+\frac{1}{2}n^2+\frac{1}{6}n=\frac{n}{6}(2n^2+3n+1)=\frac{n}{6}(2n+1)(n+1),\] as required.

Why do you think that the question gave us \(\sum\limits_{r=-1}^n r^2\) and asked us to substitute \(n=-1,0,1\) and \(2\), rather than \(\sum\limits_{r=0}^n r^2\) and \(n=0,1, 2\) and \(3\)?

This time there are five unknowns, so we should substitute

\(n=-2,-1,0,1\)

and

\(2\)

into the equation

\[ \sum_{r=-2}^n r^3=an^4+bn^3+cn^2+dn+e. \]

Doing this yields the equations

\[\begin{align}\label{a1} n=-2 \qquad -8&=16a-8b+4c-2d+e, \\ \label{a2} n=-1 \qquad -9&=a-b+c-d+e, \\ \label{a3} n=0 \qquad -9&=e, \\ \label{a4} n=1 \qquad -8 &=a+b+c+d+e, \\ \label{a5} n=2 \qquad \quad 0&=16a+8b+4c+2d+e. \end{align}\]

Equation

\(\eqref{a4}\)

tells us that

\(e=-9\)

, and so we can substitute this value into the remaining four equations, which gives us

\[\begin{align} \label{b1} 16a-8b+4c-2d&=1, \\ \label{b2} a-b+c-d&=0, \\ \label{b3} a+b+c+d&=1, \\ \label{b4} 16a+8b+4c+2d&=9. \end{align}\]

Examining equations

\(\eqref{b1}\)

and

\(\eqref{b4}\)

we see that they look similar, and so we can add them to find that

\[\begin{equation} 32a+8c=10 \label{c1}. \end{equation}\]

Adding equation

\(\eqref{b2}\)

and

\(\eqref{b3}\)

we have that

\[\begin{equation} 2a+2c=1 \label{c2}. \end{equation}\]

Rearranging this gives

\(2c=1-2a\)

, which we substitute into equation

\(\eqref{c1}\)

to see that

\[ 32a+4(1-2a)=10 \implies 24a=6, \]

or

\[ a=\frac{1}{4} \implies c=\frac{1}{4}. \]

Substituting these values into the equations

\(\eqref{b1}\)

,

\(\eqref{b2}\)

,

\(\eqref{b3}\)

and

\(\eqref{b4}\)

gives us

\[\begin{align}\label{d1} b+d=\frac{1}{2}, \\ \label{d2} 8b+2d=4. \end{align}\]

Equation \(\eqref{d1}\) rearranges to \(d=\frac{1}{2}-b\), which when substituted into equation \(\eqref{d2}\) tells us that \[8b+2\left(\frac{1}{2}-b\right)=4 \implies 6b=3 \implies b=\frac{1}{2}, d=0.\] So we’ve found that \[\sum_{r=-2}^n r^3=\frac{1}{4}n^4+\frac{1}{2}n^3+\frac{1}{4}n^2-9.\] Therefore, \[\sum_{r=0}^n r^3=\sum_{r=-2}^n r^3+9=\frac{1}{4}n^4+\frac{1}{2}n^3+\frac{1}{4}n^2=\frac{n^2}{4}(n^2+2n+1)=\frac{n^2}{4}(n+1)^2,\] as required.
