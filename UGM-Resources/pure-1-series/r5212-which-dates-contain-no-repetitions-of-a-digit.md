---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r5212
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r5212
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5212
  old_site_id: Q152
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
  exam_reference: Oxford University Mathematics Aptitude Test, 2010, Q5
task: T-UGM-IMPORT-6
---

# Which dates contain no repetitions of a digit?

## Question

This question concerns calendar dates of the form \[d_1d_2/m_1m_2/y_1y_2y_3y_4\] in the order day/month/year.

The question specifically concerns those dates which contain no repetitions of a digit. For example, the date \(23/05/1967\) is such a date but \(07/12/1974\) is not such a date as both \(1=m_1=y_1\) and \(7=d_2=y_3\) are repeated digits.

We will use the Gregorian Calendar throughout (this is the calendar system that is standard throughout most of the world; see below.)

1. Show that there is no date with no repetition of digits in the years from \(2000\) to \(2099\).

---

1. What was the last date before today, \(03/11/2010\), with no repetition of digits? Explain your answer.

---

1. When will the next such date be? Explain your answer.

---

1. How many such dates were there in years from \(1900\) to \(1999\)? Explain your answer.

[The Gregorian Calendar uses 12 months, which have, respectively, \(31\), \(28\) or \(29\), \(31\), \(30, 31, 30, 31, 31, 30, 31, 30\) and \(31\) days. The second month (February) has \(28\) days in years that are not divisible by \(4\), or that are divisible by \(100\) but not \(400\) (such as \(1900\)); it has \(29\) days in the other years (leap years).]

## Suggestion

This question concerns calendar dates of the form \[d_1d_2/m_1m_2/y_1y_2y_3y_4\] in the order day/month/year.

The question specifically concerns those dates which contain no repetitions of a digit. For example, the date \(23/05/1967\) is such date but \(07/12/1974\) is not such a date as both \(1=m_1=y_1\) and \(7=d_2=y_3\) are repeated digits.

We will use the Gregorian Calendar throughout (this is the calendar system that is standard throughout most of the world; see below.)

Which digits are already in use?

## Solution

This question concerns calendar dates of the form \[d_1d_2/m_1m_2/y_1y_2y_3y_4\] in the order day/month/year.

The question specifically concerns those dates which contain no repetitions of a digit. For example, the date \(23/05/1967\) is such date but \(07/12/1974\) is not such a date as both \(1=m_1=y_1\) and \(7=d_2=y_3\) are repeated digits.

We will use the Gregorian Calendar throughout (this is the calendar system that is standard throughout most of the world; see below.)

Any date which has a year from \(2000\) to \(2099\) will have \(y_1=2\) and \(y_2=0\).

Therefore, \(m_1\) cannot be \(0\), so \(m_1=1\).

Since there are only \(12\) months, \(m_2\) can be only \(0\), \(1\) or \(2\), but any of these values will lead to repetitions.

Hence, there is no date with no repetition of digits in the years from \(2000\) to \(2099\).

We should aim for dates of the form \(d_1d_2/m_1m_2/19y_3y_4\), since we already know that there is no date from \(2000\) to \(2099\) that will work.

Also, since we want the last day, we should find the biggest values possible, starting with the year. The greatest value for a year with no repeated digits is \(1987\).

Now we aim to find the greatest possible value for the month. Since \(10\),\(11\) and \(12\) will all lead to repeated digit \(1\), this is \(06\).

For the day, we cannot use \(0\) and \(1\) and so the day cannot be \(30\) or \(31\). So the biggest day with no repeated values is \(25\).

Hence the last date before \(03/11/2010\) with no repetition of digits is \(25/06/1987\).

To find the next such date after \(03/11/2010\) we aim to choose the smallest values for day, year and month, starting with the year.

Since every date from \(2000\) to \(2099\) repeats digits, the date we seek should be of the form \(d_1d_2/m_1m_2/2y_2y_3y_4\), with \(y_2>0\).

If \(y_2=1\), then, in order to avoid repetitions, \(m_1=0\) and \(d_1=3\).

But then we will have no possible value for \(d_2\), as we cannot use \(0\) or \(1\).

So \(y_2\) cannot be \(1\). Moreover, by the same argument, \(y_3\) and \(y_4\) should also be different from \(1\).

The next possible value is \(y_2=3\). Since we want the minimum value of \(y_1y_2y_3y_4\), and we cannot use \(1\) or \(0\), \(y_1y_2y_3y_4=2345\).

So the minimum value of the month that we can choose is \(06\), and the minimum one for the day is \(17\).

Therefore the next date with no repeated digits is \(17/06/2345\).

Since we want years from \(1900\) to \(1999\), \(y_1=1\) and \(y_2=9\).

Also, \(m_1=0\), as it cannot be \(1\). Since we have used \(1\) and \(0\), and the only days starting with \(3\) are \(30\) and \(31\), which cannot be used, \(d_1=2\).

For the other positions, namely, \(d_2\), \(m_2\), \(y_3\) and \(y_4\), we can choose any of the \(6\) digits that remain unused.

So we have \(6\) ways of choosing \(d_2\), \(5\) ways of choosing \(m_2\) (as it should be different from \(d_2\)), \(4\) ways of choosing \(y_3\) and \(3\) ways of choosing \(y_4\).

Hence, there are \(6\times5\times4\times3=360\) such dates in the years from \(1900\) to \(1999\).
