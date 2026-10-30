# AUDIT-2026-10-31-f125-part-soup-4ch1 — the part-level soup pass

**Wave:** F125 (operator order: "Proceed with 1CR 8(b)(i) part-level soup pass") ·
exporter v6 (converter unchanged) · branch `t-oeq-partsoup-1/run-001` ·
data cut `4eb72292` (STEM-RESTORE part-level machinery + re-crop + disclosure),
this audit is the docs-of-record companion.

## The order, resolved

The F123 stem-figure pass receipted exactly one residual
(AUDIT-2026-10-30-f123-stemfig-2019-06.md, "Residual observed, NOT changed"):

> **1CR 8(b)(i) part-level grid-axis soup** — "Temperature of reaction mixture
> 25 in °C 0 10 20 30 40 Total volume of acid in cm3" lives in the PART's own
> `problem_md` … Part-level soup is outside the stem-restore machinery; recorded
> here as a candidate for a future part-level soup pass.

F125 adjudicates that residual to zero: the part-level key space
(`Q<n>.<g>(<i>)`) joins STEM-RESTORE.json under the same cut law, the serving
crop is re-cut so it serves what the cut removes, and the 2019-06 slice is now
zero at BOTH layers (group stems F121/F123, part-own text F125).

## The re-crop of record (cut SECOND-gated: the crop serves what the cut removes)

The serving asset `asset_8_b_i_grid` existed since the converter-era auto-crop,
but that crop **clipped the printed y-axis title** ("Temperature of reaction
mixture in °C") — the wave-19/20 law (a cut removes only what the crop serves)
therefore required the re-cut FIRST:

- source: the sha-verified QP of record (`qp_sha256 8df7bd6f8119e396b…`,
  pinned in the 1CR topic.json header), page 19, rendered at 150 dpi;
- eyeballed rect `[143, 192, 507.5, 533.3]` → 39,986 B PNG,
  sha256 `1a44f5c8c3c6ae69d2…` (the committed bytes are the eyeballed candidate,
  byte-verified against the render evidence);
- prior converter-era crop: 32,077 B (retired by this wave);
- the 1CR topic.json asset record gains the of-record shape
  `manual_crop: true` + `review_verdict: "accepted"` (not served fields).

The full printed grid — y-axis title, y-scale 20/25/30, x-scale 0–40, x-axis
title "Total volume of acid in cm3" — is now inside the served crop.

## The verdict of record (STEM-RESTORE.json, part-level key space)

Doctrine extended: **part-level keys `Q<n>.<g>(<i>)`** adjudicate the same
flattened-soup class living in a part's OWN `problem_md` — same cut law (the
cut removes only what a crop of record serves; `served_by` must resolve to a
crop asset of that part), fail-closed verbatim anchors, slice-scoped
consumption (G-E7), and `cropRect` records the eyeballed re-crop box when the
wave re-cropped the serving asset.

The one verdict of record, `2019-06/4CH1-1CR:Q8.b(i)`:

- `verdict: "keep"` — the part's prose is kept; only the flattened axis block
  is cut;
- `dropTail: "Temperature of reaction mixture 25 in °C 0 10 20 30 40 Total
  volume of acid in cm3"` — the grid's y-axis title + y-scale + x-scale +
  x-axis title, flattened by the extraction into one label run;
- `served_by: "asset_8_b_i_grid"` (the re-cropped asset of the same part);
- anchor law: the pre-cut context ends in complete prose ("…Make sure that the
  two lines cross.") — battery-verified unique alignment on the raw corpus
  bytes.

## The exporter (v6)

`scripts/official_examq_export_hub.py` (+153 lines):

- `part_ledger_key()` + `apply_part_cut()` — the F121 group cut law mirrored
  for the part-level space; the group path is byte-identical (proven by the
  battery's group sections and the 567-part G-E7 census below);
- the `export_series` composition hook applies part cuts after the group
  restore (print order: question stem < group stem < figures; part-own text
  cleaned in place);
- **G-E7 extends to the part-level space**: part ledger keys are slice-scoped
  consumed; `served_by` must resolve to a crop asset OF THE PART; the raw
  soup-carrying part text must never reach the served bytes; the cleaned head
  must be served;
- `_CHEM_F125_NOTE_HEAD` chains the F123 note verbatim (the note-of-record
  chain is contiguous F121 → F123 → F125); the manifest note default bumps
  with the wave.

## Proof (all numbers re-proven at this wave's runs, clean tree @ `4eb72292`)

| gate / battery | result |
| --- | --- |
| F121 battery (`scripts/official_examq_f121_tests.py`) | **149/149 PASS** (+24 part-level checks: the part census, the live part anchor law, `apply_part_cut` units, the G-E7 part-level negatives — surviving-cut / served_by / stale-key refusals — and the live 2019-06 1CR 8(b)(i) serving pin: soup cut, cleaned head served, re-cropped grid served, group stem head still served) — `receipts/battery-run.out` |
| strip-law battery | 29/29 green — `receipts/striplaw-run.out` |
| F116 family battery | all checks hold (exit 0) — `receipts/f116-run.out` |
| Gated exporter run (`--expected-deltas` = the F125 disclosure) | G-E3 54 slices / 4,860 marks; G-E2 shapes hold; **G-E1 1 delta == the disclosure exactly** (`official-4ch1-1cr-2019-06` / `offp_2019-06_1cr_8-b-i`, the part-soup class only, new=0/gone=0); G-E1b set-level identity byte-equal 54/54; G-E6 labels 2,607/2,607; G-E4 questions.json byte-identical passthrough (2,605,409 B, 28 SME sets); **G-E7 567 group stems (567 restored, 0 splice-guarded, 46 adjudicated cuts, 48 group keys consumed) + 1 part-level cut on 1 part ledger key** — `receipts/exporter-run.out` |
| Served delta bytes | the soup run removed from the part's OWN problemMd (between the prose and the printed-figure references); the cleaned head ends in prose; BOTH printed figures still served (`asset_8_b_i_results-table` p18 + `asset_8_b_i_grid` p19); every other field of the part byte-identical |
| Counts | unchanged except the one part: 54 sets / 477 questions / 2,607 parts / 4,860 marks / 4,161 markPoints / 491 figure crops / 7 honest stubs |
| Reproducibility | two independent gated runs byte-identical (bundle sha256 `c0864c596ef68976…`) |

Disclosure of record: `scripts/exporter-disclosures/2026-10-31-f125-part-soup-4ch1.json`
(changed = {official-4ch1-1cr-2019-06: [offp_2019-06_1cr_8-b-i]}, new=0/gone=0).
v2 baseline pinned first-hand: the served bundle at v2 main `ec3133e9` is
sha256 `fde66a0e9c07ec74…` — byte-identical to the bundle the wave ran against
(v2 advanced with non-chemistry lanes; the chemistry plane was untouched).

## The residual plane after F125

- The 2019-06 slice is now zero at both layers: every printed figure of the
  slice is served by a crop of record, and no flattened label run survives in
  any served stem — group or part-own.
- The part-level machinery is the repeatable shape for any future slice: the
  doctrine, the exporter law, the battery sections and the G-E7 extension are
  generic; F125 instantiated them on exactly one adjudicated verdict.
- No new residuals were observed in this pass (the pass examined the one
  queued residual; the battery's live part census pins 1 part-level key —
  the corpus-wide part-level census is exactly the adjudicated set).
