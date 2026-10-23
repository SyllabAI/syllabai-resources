---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r9664
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r9664
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9664
  old_site_id: Q246
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
  exam_reference: Oxford University Mathematics Aptitude Test, None, Q7
task: T-UGM-IMPORT-6
---

# How many rows can we make with these black and white pebbles?

## Question

Suppose you have an unlimited supply of black and white pebbles. There are four ways in which you can put two of them in a row: \(BB\), \(BW\), \(WB\) and \(WW\).

1. Write down the eight different ways in which you can put three pebbles in a row.

---

1. In how many different ways can you put \(N\) pebbles in a row?

Suppose now that you are not allowed to put black pebbles next to each other. There are now only three ways of putting two pebbles in a row, because \(BB\) is forbidden.

1. Write down the five different ways that are still allowed for three pebbles.

Now let \(r_N\) be the number of possible arrangements for \(N\) pebbles in a row, still under the restriction that black pebbles may not be next to each other, so \(r_2 = 3\) and \(r_3 = 5\).

1. Show that for \(N \ge 4\) we have \(r_N = r_{N-1} + r_{N-2}\). Hint: consider separately the case where the last pebble is white, and the case where it is black.

Finally, suppose that we impose the further restriction that the first pebble and the last pebble cannot both be black. Let \(w_N\) be the number of such arrangements for \(N\) pebbles; for example, \(w_3 = 4\), since the configuration \(BWB\) is now forbidden.

1. For \(N \ge 5\), write down a formula for \(w_N\) in terms of the numbers \(r_i\), and explain why it is correct.

## Suggestion

Using the hint: if the last pebble is white, what do we know about the rest of the row?

What do we know if the first pebble is white? If it’s black?

## Solution

The eight ways are \(BBB\), \(BBW\), \(BWB\), \(BWW\), \(WBB\), \(WBW\), \(WWB\), \(WWW\).

For \(N\) pebbles, there are two possibilities for each (black or white), giving \(2^N\) possible ways.

The five ways are \(BWB\), \(BWW\), \(WBW\), \(WWB\), \(WWW\).

Consider a row of \(N\) pebbles which does not contain adjacent black pebbles; there are \(r_N\) such arrangements.

- If the last pebble is \(W\), then the previous pebbles form a row of length \(N-1\) with no adjacent \(B\)s; there are \(r_{N-1}\) such arrangements.

- If the last pebble is \(B\), the previous pebble must be \(W\), and the rest form a row of length \(N-2\) with no adjacent \(B\)s; there are \(r_{N-2}\) such arrangements.

These are all the possible combinations that fit the rule, and so \(r_N = r_{N-1} + r_{N-2}\).

Of the \(w_N\) rows of length \(N\) which follow these rules:

- If the first pebble is \(W\), the rest of the pebbles form a row of length \(N-1\) with no adjacent \(B\)s; there are \(r_{N-1}\) such arrangements.

- If the first pebble is \(B\), the second must be \(W\); also the last pebble must be \(W\). The remaining pebbles form a row of length \(N-3\) with no adjacent \(B\)s; there are \(r_{N-3}\) such arrangements.

These are all the possible combinations that fit the rule, and so \[w_N = r_{N-1} + r_{N-3}.\]

Alternatively, consider all the rows of length \(N\) with no adjacent black pairs. There are \(r_N\) of these.

We now wish to subtract the rows that have a black pebble at each end. These will each have a white pebble alongside.

Remove these four pebbles, and we have a row of length \(N-4\), and there are \(r_{N-4}\) possibilities for this.

So \(w_N = r_N - r_{N-4}\).

We know \(r_N = r_{N-1} + r_{N-2}\), so applying this twice, we have \(w_N = r_{N-1} + r_{N-3}.\)
