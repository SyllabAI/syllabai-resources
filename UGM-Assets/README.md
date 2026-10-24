# UGM-Assets — Underground Mathematics static-figure corpus

Static figures (PNG/SVG) referenced by the served UGM corpus
(`UGM-Resources/`, 479 resources, CIE 9709 P1 lanes 1–8), imported by task
**`T-UGM-ASSETS-1`** (2026-10-24). Paths mirror the live site exactly:
`<station>/<resource>/images/<file>` — the same relative path the UGM page
HTML references, so provenance is the path.

- **Figure map of record:** `UGM-Resources/figures-map.json` — one row per
  figure occurrence (resource → section → ordinal → asset path + caption).
  275 resources carry 1,233 figure occurrences over 976 unique files
  (37.7 MB). Section anchors are cross-checked against the corpus
  bodies' `##` headings (0 unmatched); ordinals are unique per section.
- **Scope of record — static images only.** GeoGebra interactive embeds and
  printable/component PDFs are NOT part of this import and remain excluded
  (LICENSE-DATA.md, Amendment 2026-10-23 scope note carried forward).
  Assets referenced only by solution/teacher-support variant pages outside
  the corpus sections are likewise excluded.
- **Rights:** © University of Cambridge (Underground Mathematics); sourced
  exam questions © UCLES. Imported under the operator attestation of
  2026-10-24 — see `LICENSE-DATA.md` (Amendment 2026-10-24). No ownership claimed;
  non-commercial educational pilot posture; takedown / correction handling
  as stated in LICENSE-DATA.md (issue or repo-owner contact; prompt removal).
- **Integrity:** per-file SHA-256 identity in `MANIFEST.json` (this
  directory), same law as the text corpus manifest.
- **Serving:** the hub importer (syllabai-v2 `apps/hub/scripts/import_ugm.py`)
  copies referenced files to `apps/hub/public/ugm-assets/` at consume time
  and injects figure references into the served bundle at deterministic
  section positions; the text bodies in `UGM-Resources/` are untouched by
  this task (conversion laws of record preserved byte-exact).
