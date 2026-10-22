---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/combining-functions/r9798
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- combining-functions
- type/review-question
resource_identity:
  ugm_id: r9798
  station: combining-functions
  station_title: Combining Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9798
  old_site_id: Q4009
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
  spec_points: []
  mapped_date: '2026-10-23'
  mapper: cross-map-functions.json (P3c) @ syllabai-experimental 4a592ed0
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md rule
    3: coverage is never manufactured)'
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford (MAT) 2013 Q['Q2']
task: T-UGM-IMPORT-2
---

# When does $f$ satisfy the identity $f(t)-f(1-t)=g(t)$?

## Question

1. Let \(k\) be a real number, \(k \ne \pm 1\). The function \(f(t)\) satisfies the identity \[f(t) - kf(1-t)=t\] for all values of \(t\). By replacing \(t\) with \(1-t\), determine \(f(t)\).
2. Consider the new identity \[\begin{equation*} f(t) - f(1-t) = g(t). \hspace{1cm} \label{eq:star}\tag{$*$} \end{equation*}\]

1. Show that no function \(f(t)\) satisfies \(\eqref{eq:star}\) when \(g(t)=t\).
2. What condition must the function \(g(t)\) satisfy for there to be a solution \(f(t)\) to \(\eqref{eq:star}\)?
3. Find a solution \(f(t)\) to \(\eqref{eq:star}\) when \(g(t) = (2t-1)^3\).

## Solution

We have that the function \(f(t)\) satisfies the identity

\[f(t) - kf(1-t)=t,\]

and by replacing \(t\) with \(1-t\) we have

\[f(1-t) -kf(t)=1-t.\]

Rearranging the second identity and substituting into the first gives

\[f(t) - k[kf(t) + 1-t]=t,\]

and solving for \(f(t)\) gives

\[f(t)=\frac{k+(1-k)t}{1-k^2}.\]

1. Consider the new identity \[\begin{equation*} f(t) - f(1-t) = g(t). \label{eq:starrepeat}\tag{$*$} \end{equation*}\]

1. Show that no function \(f(t)\) satisfies \(\eqref{eq:starrepeat}\) when \(g(t)=t\).

Letting \(g(t)=t\) gives

\[f(t) - f(1-t) = t,\]

and replacing \(t\) with \(1-t\) gives

\[f(1-t)-f(t) = 1-t.\]

Summing these two identities gives \(0=1\), which is clearly a contradiction. So there is no function \(f(t)\) that satisfies \(\eqref{eq:starrepeat}\) when \(g(t)=t\).

1. What condition must the function \(g(t)\) satisfy for there to be a solution \(f(t)\) to \(\eqref{eq:starrepeat}\)?

If there is a solution \(f(t)\) to \(\eqref{eq:starrepeat}\) then we have

\[f(t) - f(1-t) = g(t)\]

and

\[f(1-t)-f(t)=g(1-t).\]

Summing these identities gives

\[g(t)+g(1-t)=0,\]

so \(g(t)\) must satisfy this condition for there to be a solution to \(\eqref{eq:starrepeat}\).

1. Find a solution \(f(t)\) to \(\eqref{eq:starrepeat}\) when \(g(t) = (2t-1)^3\).

### Approach 1

Letting \(g(t)=(2t-1)^3\) means we require \[f(t)-f(1-t)=8t^3-12t^2+6t -1.\]

First let’s try \(f_1(t)=t^3\). This gives

\[\begin{align*} f_1(t) - f_1(1-t) & = t^3 - (1-t)^3 \\ & = 2t^3 - 3t^2 + 3t-1.\\ \end{align*}\]

Multiplying by

\(4\)

gives

\[\begin{equation} 4[f_1(t) - f_1(1-t)] = 8t^3 -12t^2 +12t -4 \label{eq4f1} \end{equation}\]

which is close to our required expression.

Now let

\(f_2(t)=t\)

, which gives

\[\begin{equation} f_2(t) - f_2(1-t) = 2t-1. \label{eqf2} \end{equation}\]

Subtracting

\(3\)

times

\(\eqref{eqf2}\)

from

\(\eqref{eq4f1}\)

gives

\[\begin{align*} 4[f_1(t) - f_1(1-t)] -3[f_2(t) - f_2(1-t)] &= 8t^3 -12t^2 +12t -4 -6t+3\\ &= 8t^3 - 12t^2 + 6t - 1 \end{align*}\]

as required. Hence, \[f(t) = 4f_1(t)-3f_2(t) = 4t^3-3t\] is a solution.

This is just one solution; there are infinitely many solutions.

### Approach 2

Trying \(f(t) = at^3+bt^2+ct+d\) seems like a sensible guess. Can we find constants \(a,b,c\) and \(d\) that will work?

We have \(f(t)-f(1-t) = (at^3+bt^2+ct+d) -(a(1-t)^3+b(1-t)^2+c(1-t)+d)\) which on multiplying out gives

\[f(t)-f(1-t)=2at^3 - 3at^2 + (3a + 2b + 2c)t - a - b - c.\]

Now \((2t-1)^3 = 8t^3 - 12t^2 + 6t - 1\), so comparing coefficients, \(a = 4, b=-1, c=-2, d=0\) is a solution that works.
