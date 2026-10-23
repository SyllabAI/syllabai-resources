---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/same-different
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/investigation
- level/developing
resource_identity:
  ugm_id: same-different
  station: sequences
  station_title: Sequences
  resource_type_id: 7
  resource_type_label: Investigation
  level: Developing
  ref: 5639
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
task: T-UGM-IMPORT-6
assets:
- path: https://undergroundmathematics.org/sequences/same-different/download/teacher-notes.pdf
  kind: printable
---

# Same or different?

> Excerpt: Students are asked to compare three sums written in sigma notation and asked if they are the same or different. Generalisation is encouraged.

## Problem

What’s the same and what’s different about the following sums?

\(\displaystyle\sum_{r=0}^{n} r^2\)

\(\displaystyle\sum_{r=1}^{n} r^2\)

\(\displaystyle\sum_{r=0}^{n-1} (r+1)^2\)

## Things you might have noticed

If we start by thinking about what is written down then we might notice the following:

- The limits of each sum are different.

- The function being summed is different in (3).

- All the functions are quadratic.

- Sums (2) and (3) have the same number of terms.

Probably the simplest way to notice more is to start writing out the sums.

1. \(\displaystyle\sum_{r=0}^{n} r^2 = 0^2 + 1^2 + 2^2 + \cdots + n^2\)

---

1. \(\displaystyle\sum_{r=1}^{n} r^2 = 1^2 + 2^2 + 3^2 + \cdots + n^2\)

---

1. \(\displaystyle\sum_{r=0}^{n-1} (r+1)^2 = 1^2 + 2^2 + 3^2 + \cdots + n^2\)

We can see that (2) and (3) have exactly the same expansion.

We could think of this as a transformation. The function \(r^2\) has been transformed to \((r+1)^2\), a translation of \(1\) unit, and the limits have been similarly transformed.

Also, despite there being an extra term in (1), because it is \(0\), all three sums are actually the same value. So we could write \[\displaystyle\sum_{r=0}^{n} r^2 = \displaystyle\sum_{r=1}^{n} r^2 = \displaystyle\sum_{r=0}^{n-1} (r+1)^2.\]

How can the limits be changed but the sum remain the same?

How can the function be changed but the sum remain the same?

Can you think of some more examples like this?

What is the difference between these two sums? \[\sum_{r=0}^{n} (r+1)^2 - \sum_{r=0}^{n} r^2\]

Are there any generalisations we can make about summing series?
