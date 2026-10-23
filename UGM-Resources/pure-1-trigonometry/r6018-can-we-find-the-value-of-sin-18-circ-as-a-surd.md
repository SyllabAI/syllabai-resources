---
created: 2026-10-23T16:39:11 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-compound-angles/r6018
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-compound-angles
- type/review-question
resource_identity:
  ugm_id: r6018
  station: trigonometry-compound-angles
  station_title: 'Trigonometry: Compound Angles'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6018
  old_site_id: Q39
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
  exam_reference: UCLES A level Mathematics 1, QP 184, 1953, Q5
task: T-UGM-IMPORT-5
---

# Can we find the value of $\sin 18^\circ$ as a surd?

## Question

1. Show that \(\theta=18^\circ\) satisfies the equation \(\cos 3\theta=\sin 2\theta\). By expressing \(\cos 3\theta\) and \(\sin 2\theta\) in terms of trigonometrical functions of \(\theta\), show that \(\sin 18^\circ\) is a root of the equation \[4x^2+2x-1=0,\] and hence find its value as a surd.

---

1. Find all solutions between \(0^\circ\) and \(360^\circ\) of the equation \[4\tan 2x=\cot x.\]

## Suggestion

If \(\cos\alpha=\sin\beta\), what can we say about \(\alpha\) and \(\beta\)?

By expressing \(\cos 3\theta\) and \(\sin 2\theta\) in terms of trigonometrical functions of \(\theta\), show that \(\sin 18^\circ\) is a root of the equation \[4x^2+2x-1=0...\]

How could we write \(\cos3\theta\) and \(\sin2\theta\) in terms of \(\cos\theta\) and \(\sin\theta\)? Could we say \(\cos(3\theta)=\cos(2\theta+\theta\))?

If you can write \(\sin2\theta-\cos3\theta=0\) in terms of \(\cos\theta\) and \(\sin\theta\), can you see anything that looks similar to \(4x^2+2x-1\)?

… and hence find its value as a surd.

How could we solve a quadratic equation to give an exact solution?

Can we write \(\tan\) and \(\cot\) in terms of \(\cos\) and \(\sin\)?

Can we learn from what we did for the first part?

## Solution

We know that \[\cos(3\times 18^\circ)=\cos 54^\circ=\sin(90^\circ-54^\circ)=\sin 36^\circ=\sin(2 \times 18^\circ).\] So \(\theta=18^\circ\) satisfies \[\cos 3\theta=\sin2\theta.\]

By expressing \(\cos 3\theta\) and \(\sin 2\theta\) in terms of trigonometrical functions of \(\theta\), show that \(\sin 18^\circ\) is a root of the equation \[4x^2+2x-1=0,\] …

We can express both \(\cos3\theta\) and \(\sin2\theta\) in terms of just \(s = \sin\theta\) and \(c = \cos\theta\).

We’ll use the identities \[\sin2\theta=2sc,\] \[\cos2\theta=1-2s^2\] and \[\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta.\]

We have \[\cos3\theta=\cos(2\theta+\theta)=\cos(2\theta) c-\sin(2\theta) s = (1-2s^2)c - 2scs = c(1-4s^2).\]

So if \(\sin2\theta-\cos3\theta=0\), we have \(2sc-c(1-4s^2)=0\), or \(c(4s^2+2s-1)=0.\)

Now we know that \(\sin(18^\circ)\) is a solution to this equation, and so \(\sin(18^\circ)\) is a root of \(4x^2+2x-1=0\), since \(\cos18^\circ\ne0\).

Hence find its value as a surd.

We complete the square in order to find the roots of \(4x^2+2x-1\) in surd form. We have \[4x^2+2x-1=\left(2x+\frac{1}{2}\right)^2-\frac{5}{4}=0,\] so that \[2x+\frac{1}{2}=\pm\frac{\sqrt{5}}{2},\] and we have \[x=\frac{-1\pm\sqrt{5}}{4}.\] Finally, we must choose whether we need a plus or a minus sign to find the root corresponding to \(\sin18^\circ\). We know that \(\sin18^\circ>0\), so we choose the plus sign. So we have that \[\sin18^\circ=\frac{-1+\sqrt{5}}{4}.\]

We play a similar game here to that of the first part of the question. Firstly, we can write \[\tan x=\frac{s}{c}, \quad \cot x=\frac{1}{\tan x}=\frac{c}{s},\] so the equation we need to solve becomes \[4\frac{\sin(2x)}{\cos(2x)}=\frac{c}{s} \implies 4\sin(2x)s-\cos(2x)c=0 \implies 8s^2c-(1-2s^2)c=0 \implies (10s^2-1)c=0.\] So we have that \(\cos x=0\) solves this, which gives us the values \(x=90^\circ, 270^\circ\) between \(0^\circ\) and \(360^\circ\). We also have that \[\sin x=\pm\frac{1}{\sqrt{10}}\] is a solution, so that \(x=\sin^{-1}(\pm1/\sqrt{10})\) are also solutions. To work out how many solutions between \(0^\circ\) and \(360^\circ\), consider

We see that \(\sin x=\pm1/\sqrt{10}\) four times between \(0^\circ\) and \(360^\circ\).

Using a calculator, one finds that \(\sin^{-1}(1/\sqrt{10})=18.4^\circ\) to one decimal place. From the symmetries of sine, we see that the other angles are then \(180^\circ-18.4^\circ=161.6^\circ\), \(180^\circ+18.4^\circ=198.4^\circ\) and \(360^\circ-18.4^\circ=341.6^\circ\), giving us six solutions in total.
