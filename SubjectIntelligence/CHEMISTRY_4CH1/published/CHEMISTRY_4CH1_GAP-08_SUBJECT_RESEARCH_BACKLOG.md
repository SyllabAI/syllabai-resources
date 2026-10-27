---
sib_protocol: SIB-1.0
artifact_id: GAP-08
artifact_version: 1.0
subject: Chemistry
qualification: International GCSE
specification: 4CH1
curriculum_version: "2017"

research_family: gap_intelligence
applicability: REQUIRED

temporal_scope:
  current: true
  legacy: false

source_scope:
  specification: true
  textbook: true
  question_papers: false
  mark_schemes: false
  examiner_reports: true
  supplementary: true

# lifecycle: GENERATED -> QA_PASSED -> STAGED
status: PUBLISHED
generated_by: zai_agent
generated_at: 2026-10-26

provenance:
  source_manifest: "SRC-SPEC-4CH1"
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-009"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "2cb92fe5f56d22f1b231c129a7e0dbc27bf86007"
    syllabai_resources: "6ef8c89291a6662f11fc6dc5ada151c47b172075"
---

# GAP-08 — Subject Research Backlog

## Purpose

This artifact converts the disclosed gaps of the audit passes into a concrete,
prioritized research backlog for the Pearson Edexcel International GCSE in
Chemistry (4CH1). Each backlog item is grounded on a bounded, locator-addressed
excerpt from this artifact's own evidence pack — a change-summary line, an
assessment-objective range, a latest-session examiner report, a
maths-skills demand note, a book hook — and states what research would close
it. Nothing on the backlog is asserted as fact about the course; each item is
a research commitment, not a finding.

## Scope

**Covers:** series-structure research flagged by the Issue 3 change summary;
assessment-objective range reconciliation pending mark-scheme corpora;
command-word drift tracking; numerical-skills demand mapping; misconception
research on the book's open questions; and corpus-completion targets for the
archive of record.

**Out of scope:** the gap findings themselves, which live in GAP-01 through
GAP-07; this artifact only converts them into forward work.

## Executive Summary

The backlog of record has six entries. Two come from the issuing body's own
change-control surface — the November/June series availability amendment and
the command-word taxonomy addition — and both define research that the corpus
of record cannot yet close. Two come from the assessment layer — the
assessment-objective weightings printed as ranges and the absent
mark-scheme corpora that would pin them. One comes from the maths-skills
demand note, and one from the book's own open questions — the hooks where the
book itself signals that the science continues beyond the specification. Each
item names the sources of record it stands on and the acquisition or analysis
that would retire it.

## Main Analysis

### GAP-043 — Backlog: November-series coverage research, flagged by the issuing body's own change summary

**Claim:** the Issue 3 change summary records "Availability of series amended
to November and June" as a specification-level change, and the latest
examiner-report covers of record are June 2025 — so the research task is to
track and acquire the November-series examiner reports as they are issued,
building out the November census that currently exists only from November
2023 of record.
**Evidence:** the change summary of record reads "Availability of series
amended to November and June" (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p3); the latest covers of
record are "Examiners' Report June 2025 Int GCSE Chemistry 4CH1 1C" and
"Examiners' Report June 2025 Int GCSE Chemistry 4CH1 2C" (SRC-ER-4CH1,
2025-06/4CH1-1C/er.pdf p1; 2025-06/4CH1-2C/er.pdf p1). Temporal scope:
CURRENT — AUTHORITATIVE.

### GAP-044 — Backlog: assessment-objective range reconciliation, blocked on absent mark-scheme corpora

**Claim:** the assessment-objective weightings of record are ranges — AO1 and
AO2 at 38–42% each, AO3 at 19–21%, split per paper — and reconciling those
ranges against actual paper demands requires question-paper and mark-scheme
corpora that are absent of record; the research task is the reconciliation
run once those corpora land, not before.
**Evidence:** the assessment-objectives table reads "AO1 Knowledge and
understanding of chemistry 38–42%" with the per-unit split "Chemistry Paper 1
23.2–25.7% 23.2–25.7% 11.6–12.8%" and "Chemistry Paper 2 14.8–16.3%
14.8–16.3% 7.4–8.2%" (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p35); the change summary
notes a further structural item — "Modular International GCSEs added to
forbidden combinations" (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p3) — that the same
future reconciliation should cover. Temporal scope: CURRENT — AUTHORITATIVE.

### GAP-045 — Backlog: command-word taxonomy drift tracking across specification issues

**Claim:** the Issue 3 change summary records "'Which' added to the command
word taxonomy" as a between-issue change, so command-word definitions drift
across specification issues; the research task is a standing diff of the
specification's command-word table against the book's appendix and against
the prior issue on every future specification update.
**Evidence:** the change summary of record reads "Appendix 5: Command word
taxonomy 46 'Which' added to the command word taxonomy" (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p3); the same summary
carries its own sweep frame — "Summary of changes made between previous issue
and this current issue Page number" (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p3) — that the standing
diff should reproduce on every future issue. Temporal scope:
CURRENT — AUTHORITATIVE.

### GAP-046 — Backlog: numerical-skills demand mapping from the board's maths-demand notes

**Claim:** the board's maths-for-scientists guide of record publishes
per-topic demand notes — stating what all students bring from KS3 and what
only Higher tier covers ("Only Higher tier students learn about upper and
lower bounds, and percentage error") — and the research task is to map those
demand notes onto the book's calculation topics topic-by-topic, a mapping no
of-record source currently supplies.
**Evidence:** the demand note of record reads "All students will have learned
to round to the nearest whole number and 1, 2 or 3 dp by the end of KS3" and
"Only Higher tier students learn about upper and lower bounds, and percentage
error" (SRC-TL-4CH1, maths-for-scientists.pdf p55); the page also fixes the
rounding rule the mapping would audit against — "Look at the digit after the
last one you want to keep. Round up if this digit is 5 or more, round down if
it is 4 or less" (SRC-TL-4CH1, maths-for-scientists.pdf p55). Temporal scope:
CURRENT — AUTHORITATIVE.

### GAP-047 — Backlog: misconception and open-question research seeded by the book's own hooks

**Claim:** the book's did-you-know surface explicitly flags places where the
science is unsettled or terminology is contested — the carbon-dioxide debate
hook and the Group 0/Group 8 labelling hook — and the research task is to
pair each such hook with examiner feedback as sessions accumulate, so
tutor-facing misconception guidance can be evidence-checked rather than
assumed.
**Evidence:** the hooks of record read "DID YOU KNOW? Although most
scientists believe that increases in carbon dioxide will cause devastating
climate change, there are others who reject this." (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 483) and "DID YOU KNOW?
You will sometimes see Group 0 labelled as Group 8. In more advanced Periodic
Tables the groups are numbered from 1 to 18, including the transition metals."
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 110);
the latest examiner-report covers of record against which future feedback
would be paired are the June 2025 reports (SRC-ER-4CH1,
2025-06/4CH1-1C/er.pdf p1). Temporal scope: CURRENT — AUTHORITATIVE.

### GAP-048 — Backlog: corpus completion targets for the archive of record

**Claim:** the archive of record has named completion targets — the eleven
source corpora that failed preflight this run, the 2020 and 2021 examination
sessions, the missing November R-variant reports, and a clean re-scan of the
OCR-garbled June 2024 Paper 1C examiner report — and each acquisition is
research work this program can name but not perform from the packs; all stay
disclosed as absent rather than approximated.
**Evidence:** the latest forward edge of the of-record census is the June
2025 report pair — "Examiners' Report June 2025 Int GCSE Chemistry 4CH1 1C"
and "Examiners' Report June 2025 Int GCSE Chemistry 4CH1 2C" (SRC-ER-4CH1,
2025-06/4CH1-1C/er.pdf p1; 2025-06/4CH1-2C/er.pdf p1) — while the
specification's own change summary frames the series structure the missing
sessions belong to, "Availability of series amended to November and June"
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p3); the
maths-demand and topic-guide surfaces of record (SRC-TL-4CH1,
maths-for-scientists.pdf p55) stand as the model for what acquisition would
add. Temporal scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-SPEC-4CH1 (the Issue 3 change summary, p3, and the
assessment-objectives page, p35) and SRC-BOOK-4CH1-SB1 (the did-you-know hook
surface). Supplementary: SRC-ER-4CH1 (the June 2025 report covers as the
forward edge of the census) and SRC-TL-4CH1 (the maths-for-scientists demand
note, p55) are cited; SRC-ROOT-BOOK-COPIES-4CH1 and SRC-SAMS-4CH1 ride as
one-page identity-presence entries consumed for no claim. All excerpts are
bounded with locators preserved; caps enforced by the pack builder.

## Limitations / Coverage Gaps

Every item on this backlog is a research commitment grounded on quoted
surfaces, not a finding; none of the underlying gaps is closed by this
artifact. The eleven preflight-absent corpora are characterized by their
absence alone — no claim is made about their hypothetical contents. The book's
hook surface is sampled at two chunks of sixteen; the rest are unsampled.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-009 (BL-009 pass 9) from this artifact's
evidence pack alone; validator of record tools/sib @ 357ace0a; claim QA binds
every citation to a pack excerpt. Research artifact — evidence-backed, not
canonical educational truth.
