#!/bin/bash
# YCH12 SB2 v2 polish lane env surface — TEMPLATE (repo-resident since
# CONT-V2-5 per R-013: lane tooling must not live only in the sandbox).
# Copy to your sandbox scripts dir, fix the two roots if needed, source it
# before runner/merge/audit/validate/reconcile/reseed.
export YCH12_VERSION=v2
export YCH12_LANE="${YCH12_LANE:-/home/z/my-project/gh_repos/syllabai-resources/books/pearson-edexcel/international-a-level/chemistry/ych12}"
export YCH12_WS="${YCH12_WS:-/home/z/my-project/data/ych12_sb2_v2}"
# grind + merge + audit + validate + reconcile read these
export YCH12_CORPUS="$YCH12_WS/out/edexcel_ial_chemistry_ych12_sb2_chunks_v2.jsonl"
export YCH12_PRISTINE="$YCH12_LANE/parsed/edexcel_ial_chemistry_ych12_sb2_chunks_v2.pristine"
export YCH12_IDS="$YCH12_WS/llm_repair_ids_ych12_v2.json"   # copy from $YCH12_LANE/pipeline/evidence/
export YCH12_REPAIRS="$YCH12_WS/llm_repairs_ych12_v2.jsonl" # copy from evidence/, runner appends here
export YCH12_LOG="$YCH12_WS/llm_repair_ych12_v2.log"
export YCH12_MD="$YCH12_WS/out/full_book_docling_v2.md"
export YCH12_REPORT="$YCH12_WS/out/parse_report_v2.json"
# runner cadence (L-017/L-027: foreground windows only; PROBE_WAIT 45s fits
# more probes into a 10-min window than the original 90s)
export CONC="${CONC:-2}"
export PROBE_WAIT="${PROBE_WAIT:-45}"
# landing: source this, then:  ych12_v2_reseed.sh && merge_llm_ych12.py &&
# YCH12_BASELINE=$YCH12_WS/baseline_landed_v2.jsonl ych12_v2_reconcile.py &&
# audit_polish_ych12.py && validate_ych12.py
