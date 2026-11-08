#!/usr/bin/env python3
"""T-MG-QB-3 run-001 — patch the MG-QuestionBank README coverage row and append
the LEDGER.md wave entry. Writes QB-README.new.md + LEDGER.new.md into WORK."""
import os

WORK = "/home/z/my-project/mg_work"

# ---------- README ----------
readme = open(f"{WORK}/QB-README.cur.md").read()

old_row = ("| `as-level-maths-edexcel`, `a-level-maths-edexcel`, other boards | — | — | — | "
           "later runs under `T-MG-QB-*`; mode presence re-verified at run-000 of each |")
new_rows = (
    "| `a-level-maths-edexcel` | 44 chapters (Year 1 `as-*` ×24 + Year 2 `a-level-*` ×20) "
    "over 245 subtopics | 44 (per-chapter question sets — the site's A-Level question resource) | 44 | "
    "extracted by `T-MG-QB-3/run-001`; 913 questions / 5,323 printed marks; segmented by printed "
    "total lines (numbers embedded in display-math make leading anchors unreliable here); "
    "3 source total-line typos + 1 printed numbering gap recorded; 9 question PDFs via the site's "
    "own asset-host naming convention (page publishes answers only; HEAD-200 verified); "
    "`as-level-maths-edexcel` intentionally **not** extracted separately — its 24 chapters are "
    "slug-identical to this lane's Year-1 half (same source sets; dedup decision in manifest) |")
assert old_row in readme, "README coverage row drifted"
readme = readme.replace(old_row, new_rows)

old_gov = ("- Extraction scripts live in `../scripts/` as `mg_*.py` (`mg_flight_decode.py`, "
           "`mg_fetch_catalog.py`, `mg_probe_pdf.py`, `mg_qb_extract.py`, `mg_manifest.py`, "
           "`mg_upload.py`).")
new_gov = ("- Extraction scripts live in `../scripts/` as `mg_*.py` (`mg_flight_decode.py`, "
           "`mg_fetch_catalog.py`, `mg_probe_pdf.py`, `mg_qb_extract.py`, `mg_manifest.py`, "
           "`mg_upload.py`; QB-2: `mg_qb2_*.py`; QB-3: `mg_qb3_*.py`, plus the shared "
           "`gh_api.py` Git-Data-API helper).")
assert old_gov in readme, "README governance line drifted"
readme = readme.replace(old_gov, new_gov)
open(f"{WORK}/QB-README.new.md", "w").write(readme)

# ---------- LEDGER ----------
ledger = open(f"{WORK}/LEDGER.cur.md").read().rstrip() + "\n"
wave = """

## Wave 27 — MG-QuestionBank's third lane: the MathsGenie A-Level Maths (Edexcel, 9MA0) chapter question-set bank (T-MG-QB-3 run-001; branch t-mg-qb-3/run-001)

The question bank reaches A-Level: `MG-QuestionBank/a-level-maths-edexcel` carries **44 of 44 chapters /
913 questions / 5,323 printed marks** with worked-solution scans 44/44, zero PDFs stored (~47 MB,
1,952 files). The lane's granularity of record is the **per-chapter question set** — the new-site lane
(`mathsgenie.co.uk/a-level/maths/edexcel`, 44 chapters over 245 subtopics, re-decoded live and
chapter-identical to `T-MG-VERIFY-1` run-000) publishes no per-subtopic question PDFs (subtopic pages
are video/lesson; the new-site subtopic question bank is an interactive client-side feature,
link-of-record), so the question resources join 44/44 by chapter title to the old-site delivery
(`old.mathsgenie.co.uk/newalevel.php` → `a-level-*-questions-*.php`, asset host
`old-asset.mathsgenie.co.uk/alevel/`). **`as-level-maths-edexcel` is intentionally not extracted**: its
24 chapters verified slug-identical to this lane's Year-1 half (same source sets) — dedup decision
recorded in the manifest, never silently dropped.

Extraction needed its own parser law. A-Level sets embed question numbers inside display-math blocks
(verified visually: one question's "5" renders inside the fragment "2 + 10 5", another's after a
fraction numerator), so the QB-1/2 leading-number anchor law is unreliable here; instead every question
prints a right-aligned "(Total for question N is M marks)" boundary line, and the lane is segmented by
consecutive total lines in spatial order, the line travelling with its crop. The marks law extends
accordingly: marks come from printed total lines only — the "(N marks)" pattern of QB-1/2 does not
occur in this lane; nothing inferred. The numbering law keeps the printed number as identity: three
source total-line typos (graphs-transformations Q22 printed "2", sequences-and-series Q9 printed "2",
the-normal-distribution Q2 printed "1") are position-derived and flagged `printed_as`; one printed
numbering gap (exponentials-and-logarithms skips 19) is kept as printed. Ground-truth fixes made
in-run and disclosed: the singular "(Total for question N is 1 mark)" lines (six chapters would have
lost questions to a plural-only regex); and 9 question-set pages that publish only the answers link —
their sibling question PDFs follow the site's own asset-host naming convention, were HEAD-200-verified
at run time, and are included with explicit discovery provenance (all 9 initially mis-read as
image-only sets because the scanned answers PDF sat in the question slot of an interim catalog;
re-classified before any corpus landing). Premium-gated entries: 0 (the old-site sets are all free).
Past-paper / predicted-paper / mini-test banks remain excluded per the operator decision of
2026-11-07; old-spec C1–C4/S1/M1 materials are a different qualification generation and out of the lane
of record. Receipt: `MG-QuestionBank/T-MG-QB-3-run-001-RECEIPT.json`; scripts land as
`scripts/mg_qb3_*.py` (+ the shared `scripts/gh_api.py` helper) with run evidence under
`scripts/mg_qb3_run001/`.
"""
open(f"{WORK}/LEDGER.new.md", "w").write(ledger + wave)
print("QB-README.new.md + LEDGER.new.md written")
print("README rows now:", sum(1 for l in readme.splitlines() if l.startswith("| `") and "topics" not in l and "|---" not in l))
