---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/r8404
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/review-question
resource_identity:
  ugm_id: r8404
  station: sequences
  station_title: Sequences
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8404
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
  exam_reference: UCLES A level Pure Mathematics 1, 1973, Q2
task: T-UGM-IMPORT-6
---

# If $x_1 = (x_0 + 2)/(x_0 + 1)$, can we show $\sqrt{2}$ lies between $x_0$ and $x_1$?

## Question

If

\(x_0\)

is any positive rational number and

\[\begin{equation*} x_1 = \frac{x_0 + 2}{x_0 + 1}, \quad x_2 = \frac{x_1 + 2}{x_1 + 1}, \quad x_3 = \frac{x_2 + 2}{x_2 + 1}, \end{equation*}\]

prove that

1. \(\sqrt{2}\) lies between \(x_0\) and \(x_1\), and between \(x_2\) and \(x_3\),

---

1. \(|x_1^2 - 2| < |x_0^2 - 2|\),

---

1. \(|x_2^2 - 2| < \frac{1}{9} |x_0^2 - 2|\).

By taking

\(x_0 = \frac{7}{5}\)

, or otherwise, show that

\[\begin{equation*} \frac{41}{29} < \sqrt{2} < \frac{99}{70}, \end{equation*}\]

and, without using tables, show that each of \(\dfrac{41}{29}\) and \(\dfrac{99}{70}\) differ from \(\sqrt{2}\) by less than \(5 \times 10^{-4}\).

## Suggestion

…without using tables, show that each of \(\dfrac{41}{29}\) and \(\dfrac{99}{70}\) differ from \(\sqrt{2}\) by less than \(5 \times 10^{-4}\).

Without knowing \(\sqrt{2}\), we can’t calculate the distance between \(x_n\) and \(\sqrt{2}\), but what’s the distance between \(x_n\) and \(x_{n+1}\)?

## Solution

We can reason as follows:

\[\begin{align*} x_{n+1} < \sqrt{2} &\iff \frac{x_n + 2}{x_n + 1} < \sqrt{2} \\ &\iff (x_n + 2) < \sqrt{2}(x_n + 1) \\ &\iff (1 - \sqrt{2})x_n < (\sqrt{2} - 2) \\ &\iff x_n > \frac{2 - \sqrt{2}}{\sqrt{2} - 1} = \sqrt{2} \frac{\sqrt{2} - 1}{\sqrt{2} - 1} = \sqrt{2}. \end{align*}\]

Since the same argument applies with \(<\) and \(>\) reversed, we’ve shown that \(x_n\) and \(x_{n+1}\) always lie on opposite sides of \(\sqrt{2}\).

Thus \(x_{0}\) and \(x_1\), and \(x_{2}\) and \(x_3\), always lie on opposite sides of \(\sqrt{2}\).

We can write

\[\begin{align*} |x_1^2 - 2| &= \left| \left( \frac{x_0 + 2}{x_0 + 1} \right)^2 - 2 \right|\\ &= \left| \frac{(x_0 + 2)^2 - 2(x_0 + 1)^2}{(x_0 + 1)^2} \right|\\ &= \frac{|x_0^2 + 4x_0 + 4 - 2x_0^2 - 4x_0 - 2|}{|x_0 + 1|^2} \\ &= \frac{|2 - x_0^2|}{|x_0 + 1|^2} \\ &= \frac{|x_0^2 - 2|}{|x_0 + 1|^2} \\ &< |x_0^2 - 2|. \end{align*}\]

The final inequality follows since \(x_0 + 1 > 1\).

The same method as above shows that

\[\begin{equation*} |x_2^2 - 2| = \frac{|x_1^2 - 2|}{|x_1 + 1|^2} = \frac{|x_0^2 - 2|}{|x_0 + 1|^2 |x_1 + 1|^2}. \end{equation*}\]

We can write

\[\begin{equation*} |x_1 + 1|^2 = \left( \frac{x_0 + 2}{x_0 + 1} + 1 \right)^2 = \frac{(x_0 + 2 + x_0 + 1)^2}{(x_0 + 1)^2} = \frac{(2x_0 + 3)^2}{(x_0 + 1)^2}. \end{equation*}\]

Hence,

\[\begin{equation*} |x_2^2 - 2| = \frac{|x_0^2 - 2|}{|x_0 + 1|^2} \times \frac{(x_0 + 1)^2}{(2x_0 + 3)^2}= \frac{|x_0^2 - 2|}{(2x_0 + 3)^2} < \tfrac{1}{9} |x_0^2 - 2|, \end{equation*}\]

with the inequality holding as \(x_0 > 0\) which implies that \((2x_0+3)^2>9\).

By taking

\(x_0 = \dfrac{7}{5}\)

, or otherwise, show that

\[\begin{equation*} \frac{41}{29} < \sqrt{2} < \frac{99}{70} \end{equation*}\]

From the first part of the question, the iteration goes from one side of

\(\sqrt{2}\)

to the other, and back again, and so on. Since

\(x_0 = 1.4 < \sqrt{2}\)

, we know that

\[\begin{equation*} \sqrt{2} < x_1 = \frac{x_0 + 2}{x_0 + 1} = \frac{7 + 10}{7 + 5} = \frac{17}{12} \end{equation*}\]

and that

\[\begin{equation*} \sqrt{2} > x_2 = \frac{x_1 + 2}{x_1 + 1} = \frac{17 + 24}{17 + 12} = \frac{41}{29} \end{equation*}\]

and, finally, that

\[\begin{equation*} \sqrt{2} < x_3 = \frac{x_2 + 2}{x_2 + 1} = \frac{41 + 58}{41 + 29} = \frac{99}{70}. \end{equation*}\]

…and, without using tables, show that each of \(\dfrac{41}{29}\) and \(\dfrac{99}{70}\) differ from \(\sqrt{2}\) by less than \(5 \times 10^{-4}\).

With

\(x_0 = \dfrac{7}{5}\)

, we saw that

\(x_2 = \dfrac{41}{29}\)

and

\(x_3 = \dfrac{99}{70}\)

. We saw from the very first part of the question that

\(x_2\)

and

\(x_3\)

lie on opposite sides of

\(\sqrt{2}\)

, and so

\[\begin{equation*} |x_2 - \sqrt{2}| < |x_2 - x_3| = \left| \frac{41}{29} - \frac{99}{70} \right| = \left| \frac{41 \times 70 - 99 \times 29}{2030} \right| = \frac{1}{2030} < 5 \times 10^{-4}. \end{equation*}\]

The same inequalities above also apply when \(x_2\) and \(x_3\) are interchanged, which proves the result.

Where did our initial iteration come from? We have

\[\begin{equation*} f(x) = x^2 - 2 = 0 \iff x^2 + x - 2 = x \iff x(x+1) - 2 = x \iff x = \frac{x+2}{x+1} = g(x). \end{equation*}\]

Thus we have in action here the \(x = g(x)\) iteration, or the rearrangement method, where we start with \(f(x) = 0\), and move to \(x = g(x)\).
