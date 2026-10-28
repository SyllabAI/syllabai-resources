# MS-01 — Mark Scheme Structure

## Purpose

This artifact describes the structure of the 4CH1 mark schemes as they exist in the
official exam corpus of record (SRC-QPMS-4CH1): the embedded per-item "Mark scheme
answer" blocks, the answer forms per item class, the accepted-alternative guidance
columns and the machine-gradable mark-point lines. It is the opening artifact of the
Mark Scheme Intelligence (MS) family, grounded on the parsed mark-scheme text
exactly as held — the family law forbids any mark-point inventiveness beyond that
text. Every claim is carried on a bounded, locator-addressed excerpt from the run's
evidence pack. Research artifact; canonical mark_points planes are read-only and
untouched.

## Scope

**Covers:** the per-item block structure; MCQ answer-and-distractor form; mark-point
lines; ACCEPT/ALLOW guidance; answer forms across item classes; conditional guidance
rows.

**Grounding:** SRC-QPMS-4CH1 (the 2019-06 and 2020-01 1C papers of the pack —
mark-scheme text embedded per item in the official extractions).

**Out of scope:** mark-point taxonomy detail (MS-02), alternatives catalogue (MS-04),
mark-loss semantics (MS-05), examiner language inventory (MS-07).

## Executive Summary

The parsed mark schemes are per-item, self-contained blocks: an answer line (the
accepted response, with the MCQ letter where applicable), optional distractor
rationales (why each wrong option is wrong), an ACCEPT/ALLOW guidance column for
equivalent forms, and a machine-gradable mark-point line "- **(1)** ..." per
allocatable mark. The structure is uniform enough to parse mechanically — which is
what the corpus of record already does — and rich enough to carry the marking
nuance (both-must-be-correct conditions, ignore-notes, dependency notes). For
revision design, the block structure means every mark a candidate can earn is
visible in advance, in the board's own words.

## Main Analysis

### MS-001 — The embedded per-item block structure

**Claim:** mark-scheme content lives in per-item blocks headed "**Mark scheme
answer**", directly following each question part in the parsed papers.
**Evidence:** the 2019-06 1C opening part carries its block immediately after the
stem and options (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 19-33), and the
same block law governs the 2020-01 papers (SRC-QPMS-4CH1, 2020-01/4CH1-1C/questions.md lines 16-30).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-002 — The MCQ answer-and-distractor form

**Claim:** MCQ mark schemes print the keyed letter with its content, then give a
rationale for each rejected distractor.
**Evidence:** "> B (the crystal dissolves in water) A is not correct as the crystal
does not condense C is not correct as the crystal does not evaporate D is not
correct as the crystal does not melt" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 19-33); the same form with full-sentence rationales on the appearance item
(SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 38-52).
**Design reading:** the distractor rationales are pre-built misconception feedback —
a teaching asset the MIS family can mine without inventing anything.
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-003 — The mark-point line as the grading unit

**Claim:** each allocatable mark is printed as its own "- **(N)**" line, making the
mark point the machine-gradable unit of the parsed text.
**Evidence:** "- **(1)** Answer B: the crystal dissolves in the water"
(SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 19-33); "- **(1)** T" on the
noble-gas item (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 105-119).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-004 — ACCEPT/ALLOW guidance for equivalent forms

**Claim:** accepted alternatives ride inside the answer line or an adjacent guidance
column (ACCEPT for equivalent forms, ALLOW for permitted variants).
**Evidence:** "argon / helium ACCEPT Ar / He" (SRC-QPMS-4CH1, 2020-01/4CH1-1C/questions.md lines 16-30); "nitrogen ACCEPT N2"
(SRC-QPMS-4CH1, 2020-01/4CH1-1C/questions.md lines 27-41).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-005 — Answer forms across item classes

**Claim:** the answer line's form tracks the item class — a lettered key for MCQs, a
word or word/formula pair for identification items, a full equation for equation
items, a bare number or value for calculation results.
**Evidence:** the equation item's answer line reads "> S + O2 → SO2"
(SRC-QPMS-4CH1, 2020-01/4CH1-1C/questions.md lines 49-63) and the MCQ key form is
"> A (3)" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 81-95).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-006 — Conditional guidance rows

**Claim:** guidance rows impose conditions on credit — most commonly that a pair of
answers must both be correct to score.
**Evidence:** "carbon dioxide ACCEPT CO2 If both name and formula given both must be
correct" (SRC-QPMS-4CH1, 2020-01/4CH1-1C/questions.md lines 38-52) — the same
conditional law appears across the atmosphere-gas identification series
(SRC-QPMS-4CH1, 2020-01/4CH1-1C/questions.md lines 16-30).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-049 — Two-level mark accounting: part totals and question totals

**Claim:** the parsed scheme carries its mark budget at two granularities at once — every part header prints its own value in square brackets while every question header prints the question total in parentheses — so the sum of a block's point lines can be reconciled against two printed checkpoints rather than one. The part-level figure governs the block's own point lines; the question-level figure governs the whole run of blocks beneath it. A parser that reads only one level can silently accept a mis-keyed total.
**Evidence:** "### 3(d)(ii) [2]" precedes the two-observation part whose point lines follow (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 209-223); the next question header prints "## Question 4 (8 marks)" as the run-level checkpoint (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 228-242).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-050 — Linked-explanation scaffolds announce their point count

**Claim:** the linked-explanation scaffold is a fixed, parseable template — “An explanation that links together the following N points” — whose printed count predicts the number of M-rows that follow, giving a reader the point tally before any row is read. The scaffold is stable across item sizes: the two-point and three-point forms differ only in the counted number. The same windows bind the rows together with dependency coding, so the scaffold's count, the M-codes and the dependency note are three redundant statements of one structure.
**Evidence:** the two-point form "An explanation that links together the following two points:" opens the chromatography explanation, whose rows carry "M2 DEP on M1" in the same window (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 310-324); the three-point form "An explanation that links together the following three points:" opens the limewater explanation (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 886-900).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-051 — NOTE riders convert point values into conditional ceilings

**Claim:** a NOTE rider re-states the point's award as a conditional ceiling: the printed value holds only while the candidate's method stays inside the named condition, and overreaching methods drop the award to a printed sub-set. The crystallisation item prints the two overreach cases symmetrically — full evaporation by heating, and full evaporation without heating — each with its own reduced award. The ceiling is therefore part of the parsed point, not an external marking convention.
**Evidence:** "NOTE: If the solution is heated to remove all the water then only M1 can be awarded" and, symmetrically, "NOTE If the solution is left to evaporate all the water without heating only 1 mark can be awarded" ride on the crystallisation method point (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 1224-1238).
Temporal scope: CURRENT — AUTHORITATIVE.


## Evidence / Source Basis

Primary evidence: SRC-QPMS-4CH1 — the 2019-06 and 2020-01 1C official extractions
(120 bounded line-window excerpts across the two files, locators preserved; the
mark-scheme text is embedded in the corpus of record and cited verbatim). No
examiner reports were consumed for this artifact; no specimen material was cited;
supplementary pack sources were not consumed for claims.

## Limitations / Coverage Gaps

The structural description covers the pack's two excerpted papers; the corpus's
remaining sessions share the same declared schema (each file's header carries the
official-extraction schema line), but structure drift in later sessions is not
audited here. The artifact describes the parsed text, not the visual layout of the
original PDFs (table grids render as flattened rows in the parse). No canonical
mark_points plane was read or written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-005 (BL-008 pass 5) from the run's evidence
pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 bound all citations
to pack excerpts. Deepened under SIB-CHEMISTRY_4CH1-RUN-018 (D3 tranche 2): +3 records (MS-049..051), zero-append mining of the carried RUN-005 pack of record; every quote self-bound to raw excerpt text before the official gate; claim QA re-bound all citations. Research artifact — evidence-backed, not canonical educational truth.
