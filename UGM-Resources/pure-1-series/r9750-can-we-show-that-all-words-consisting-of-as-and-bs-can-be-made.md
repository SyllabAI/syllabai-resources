---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r9750
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r9750
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9750
  old_site_id: Q1056
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
  exam_reference: Oxford University Mathematics Aptitude Test, 2013, Q7
task: T-UGM-IMPORT-6
---

# Can we show that all words consisting of $A$s and $B$s can be made?

## Question

\(\textbf{AB}\)-words are “words” formed from the letters \(\textbf{A}\) and \(\textbf{B}\) according to certain rules. The rules are applied starting with the empty word, containing no letters. The basic rules are:

1. If the current word is \(x\), then it can be replaced with the word that starts with \(\textbf{A}\), followed by \(x\) and ending with \(\textbf{B}\), written \(\textbf{A} x\textbf{B}\).

---

1. If the current word ends with \(\textbf{B}\), the final \(\textbf{B}\) can be removed.

1. Show how the word \(\textbf{AAAB}\) can be produced.

---

1. Describe precisely all the words that can be produced with these two rules. Justify your answer. You might like to write \(\textbf{A}^i\) for the word containing just \(i\) consecutive copies of \(\textbf{A}\), and similarly for \(\textbf{B}\); for example \(\textbf{A}^3 \textbf{B}^2 = \textbf{AAABB}\).

We now add a third rule:

1. Reverse the word, and replace every \(\textbf{A}\) by \(\textbf{B}\), and every \(\textbf{B}\) by \(\textbf{A}\).

For example, applying this rule to \(\textbf{AAAB}\) would give \(\textbf{ABBB}\).

1. Describe precisely all the words that can be produced with these three rules. Justify your answer.

Finally, we add a fourth rule.

1. Reverse the word.

1. Show that every word consisting of \(\textbf{A}\)s and \(\textbf{B}\)s can be formed using these four rules. Hint: show how, if we have produced the word \(w\), we can produce (a) the word \(\textbf{A}w\), and (b) the word \(\textbf{B}w\); hence deduce the result.

## Suggestion

\(\textbf{AB}\)-words are “words” formed from the letters \(\textbf{A}\) and \(\textbf{B}\) according to certain rules. The rules are applied starting with the empty word, containing no letters. The basic rules are:

1. If the current word is \(x\), then it can be replaced with the word that starts with \(\textbf{A}\), followed by \(x\) and ending with \(\textbf{B}\), written \(\textbf{A} x\textbf{B}\).

---

1. If the current word ends with \(\textbf{B}\), the final \(\textbf{B}\) can be removed.

…

1. Describe precisely all the words that can be produced with these two rules. Justify your answer. You might like to write \(\textbf{A}^i\) for the word containing just \(i\) consecutive copies of \(\textbf{A}\), and similarly for \(\textbf{B}\); for example \(\textbf{A}^3 \textbf{B}^2 = \textbf{AAABB}\).

If we start with \(\textbf{A}^i\textbf{B}^j\), what effect does Rule (1) have? What about Rule (2)?

1. Reverse the word, and replace every \(\textbf{A}\) by \(\textbf{B}\), and every \(\textbf{B}\) by \(\textbf{A}\).

---

1. Reverse the word.

1. Show that every word consisting of \(\textbf{A}\)s and \(\textbf{B}\)s can be formed using these four rules. Hint: show how, if we have produced the word \(w\), we can produce (a) the word \(\textbf{A}w\), and (b) the word \(\textbf{B}w\); hence deduce the result.

Why does creating \(\textbf{A}w\) and \(\textbf{B}w\) from \(w\) solve the problem?

What effect does combining Rule (3) and Rule (4) into a single rule have?

## Solution

Apply Rule (1) three times to get \(\textbf{AAABBB}\), and then apply Rule (2) twice to give \(\textbf{AAAB}\).

Applying Rule (1) \(i\) times will produce the word \(\textbf{A}^i \textbf{B}^i\). We can then remove any number of the \(\textbf{B}\)s by applying Rule (2). These two rules cannot produce any word containing a \(\textbf{B}\) before an \(\textbf{A}\).

So we can produce any word of the form \(\textbf{A}^i \textbf{B}^j\) where \(i \ge j \ge 0\).

Rule (3) still keeps all the \(\textbf{A}\)s before all the \(\textbf{B}\)s. But now we can produce any word of the form \(\textbf{A}^i \textbf{B}^j\) with \(i \ge 0\) and \(j \ge 0\).

For \(i \ge j\), apply the rules exactly as in (ii) above. For \(j>i\), apply Rule (1) \(j\) times and Rule (2) \(j-i\) times, and then apply Rule (3) once.

1. By first applying Rule (1) to \(w\) we get \(\textbf{A} w \textbf{B}\), and then applying Rule (2) we get \(\textbf{A}w\).

---

1. Let \(\overline{x}\) be the word produced by replacing all the \(\textbf{A}\)s in \(x\) with \(\textbf{B}\)s and replacing all \(\textbf{B}\)s with \(\textbf{A}\)s. Now we can produce \(\overline{w}\) by applying Rule (3) followed by Rule (4) to \(w\). Then we can use Rule (1) and then Rule (2) to get \(\textbf{A} \overline{w}\). Now we can use Rules (3) and (4) again to get \(\overline{\textbf{A} \overline{w}} = \textbf{B}w\).

As we now have ways of adding \(\textbf{A}\) or \(\textbf{B}\) to the start of a word, we can produce any word consisting of \(\textbf{A}\)s and \(\textbf{B}\)s from these four rules starting with the empty word.
