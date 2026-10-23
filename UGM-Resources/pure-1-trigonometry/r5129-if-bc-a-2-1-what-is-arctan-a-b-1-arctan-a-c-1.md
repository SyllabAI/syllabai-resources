---
created: 2026-10-23T16:39:11 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-compound-angles/r5129
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-compound-angles
- type/review-question
resource_identity:
  ugm_id: r5129
  station: trigonometry-compound-angles
  station_title: 'Trigonometry: Compound Angles'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5129
  old_site_id: Q66
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: trigonometry-compound-angles
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: trigonometry-compound-angles
    validation_status: SUGGESTED
  spec_points: []
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md rule
    3: coverage is never manufactured)'
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES STEP Mathematics II, 2005, Q4
task: T-UGM-IMPORT-5
---

# If $bc=a^2+1$,  what is $\arctan[(a+b)^{-1}]+\arctan[(a+c)^{-1}]$?

## Question

The positive numbers \(a\), \(b\) and \(c\) satisfy \(bc=a^2+1\). Prove that \[\arctan\left(\frac{1}{a+b}\right)+\arctan\left(\frac{1}{a+c}\right)=\arctan\left(\frac{1}{a}\right).\] The positive numbers \(p\), \(q\), \(r\), \(s\), \(t\), \(u\) and \(v\) satisfy \[st=(p+q)^2+1, \qquad uv=(p+r)^2+1, \qquad qr=p^2+1.\] Prove that

\[\begin{align*} \arctan\left(\frac{1}{p+q+s}\right)&+\arctan\left(\frac{1}{p+q+t}\right)+\arctan\left(\frac{1}{p+r+u}\right)\\ &+\arctan\left(\frac{1}{p+r+v}\right)=\arctan\left(\frac{1}{p}\right). \end{align*}\]

Hence show that \[\arctan\left(\frac{1}{13}\right)+\arctan\left(\frac{1}{21}\right)+\arctan\left(\frac{1}{82}\right)+\arctan\left(\frac{1}{187}\right)=\arctan\left(\frac{1}{7}\right).\]

## Suggestion

Do we know what \(\tan(A+B)\) is?

Could we use \(P=\arctan\left(\dfrac{1}{a+b}\right) \implies \tan P=\dfrac{1}{a+b}\)?

Can we simplify the LHS of the first equation with this?

Can we use the first part of the question? Could we use it twice?

Can we use simultaneous equations to find suitable values for the various letters?

## Solution

Let

\[\begin{align*} P &= \arctan\left(\frac{1}{a+b}\right) \quad &&\Longrightarrow \quad& \tan P&=\frac{1}{a+b}\\ Q &= \arctan\left(\frac{1}{a+c}\right) \quad &&\Longrightarrow \quad& \tan Q&=\frac{1}{a+c} \\ R &= \arctan\left(\frac{1}{a}\right) \quad &&\Longrightarrow \quad& \tan R&=\frac{1}{a} \end{align*}\]

Note that since \(a, b\) and \(c\) are all positive numbers, \(P\), \(Q\) and \(R\) all lie between \(0\) and \(\dfrac{\pi}{2}\).

Then we wish to show that \(P+Q=R\), which is equivalent to showing that \(\tan(P+Q)=\tan R\) (since \(0 < P+Q < \pi\)).

Using the compound angle formula, we also know that

\[\tan(P+Q)=\frac{\tan P + \tan Q}{1-\tan P\tan Q}.\]

So we find that

\[\begin{align*} \tan(P+Q) &= \dfrac{\dfrac{1}{a+b}+\dfrac{1}{a+c}}{1-\dfrac{1}{(a+b)(a+c)}} \\ &= \dfrac{\Bigl(\dfrac{2a+b+c}{(a+b)(a+c)}\Bigr)}{\Bigl(\dfrac{a^2+ab+ac+bc-1}{(a+b)(a+c)}\Bigr)} \\ &= \dfrac{2a+b+c}{a^2+ab+ac+bc-1} \\ &= \dfrac{2a+b+c}{a^2+ab+ac+(a^2+1)-1}\quad\text{as $bc=a^2+1$}\\ &= \dfrac{2a+b+c}{2a^2+ab+ac}\\ &= \dfrac{2a+b+c}{a(2a+b+c)}\\ &= \dfrac{1}{a}\\ &= \tan R, \end{align*}\]

so we are done.

Since \(qr=p^2+1\), we can say immediately from the first part that

\[\arctan\left(\frac{1}{p+q}\right)+\arctan\left(\frac{1}{p+r}\right)=\arctan\left(\frac{1}{p}\right).\]

Now using the first part on the first term on the LHS (since \(st=(p+q)^2+1\)), and on the second term also (since \(uv=(p+r)^2+1\)), we have

\[\arctan\left(\frac{1}{p+q+s}\right)+\arctan\left(\frac{1}{p+q+t}\right)+\arctan\left(\frac{1}{p+r+u}\right) +\arctan\left(\frac{1}{p+r+v}\right)=\arctan\left(\frac{1}{p}\right).\]

We are looking for values of \(p\), \(q\), \(r\), \(s\), \(t\), \(u\) and \(v\) so that the above result takes this form.

We’ll begin by taking

\(p=7\)

(to make the right hand side work) and then look for solutions consistent with this. We have the equations

\[\begin{align*} 7+q+s &= 13 \qquad& \Longrightarrow&\quad& q+s &= 6\\ 7+q+t &= 21 \qquad& \Longrightarrow&\quad& q+t &= 14\\ 7+r+u &= 82 \qquad& \Longrightarrow&\quad& r+u &= 75\\ 7+r+v &= 187 \qquad& \Longrightarrow&\quad& r+v &= 180 \end{align*}\]

and

\[\begin{align*} st &= (7+q)^2+1\\ uv &= (7+r)^2+1\\ qr &= 7^2+1=50. \end{align*}\]

Using the first two of these we find

\(s=6-q\)

and

\(t=14-q\)

, and we can then substitute this into

\(st=(7+q)^2+1\)

to eliminate

\(s\)

and

\(t\)

, deducing

\[\begin{align*} &&(6-q)(14-q)&=(q+7)^2+1&&\quad\\ &\Longrightarrow \quad& 84-20q+q^2&=q^2+14q+50\\ &\Longrightarrow \quad& 34q&=34\\ &\Longrightarrow \quad& q&=1. \end{align*}\]

It then follows that \(s=5\), \(t=13\) and \(r=50\) since \(qr=50\). Using this value for \(r\) we also find that \(u=25\) and \(v=130\).

We must also double-check that all seven equations are consistent by subsituting into the equation we didn’t use:

\(uv = (p+r)^2+1\)

. This equation is satisfied, as

\[uv=25\times130 = 3250\quad\text{and}\quad (p+r)^2+1 = 57^2+1 = 3249+1=3250.\]

So

\[\begin{align*} p&=7,& q&=1,& r&=50,& s&=5,\\ t&=13,& u&=25,& v&=130 \end{align*}\]

gives us \[\arctan\left(\frac{1}{13}\right)+\arctan\left(\frac{1}{21}\right)+\arctan\left(\frac{1}{82}\right)+\arctan\left(\frac{1}{187}\right)=\arctan\left(\frac{1}{7}\right).\]
