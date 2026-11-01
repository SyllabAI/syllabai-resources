#!/bin/bash
# YCH11 SB1 polish lane env surface — TEMPLATE (repo-resident at the R5
# resumption, T-PARSE-YCH11-1-R5; same parameterized convention as the
# YCH12 SB2 v2 lane, T-PARSE-YCH12-2 / R-013: lane tooling must not live
# only in the sandbox).
# Copy to your sandbox scripts dir, fix the two roots if needed, source it
# before runner/merge/audit/validate/reconcile/reseed.
export YCH11_VERSION=v1
export YCH11_LANE="${YCH11_LANE:-/home/z/my-project/gh_repos/syllabai-resources/books/pearson-edexcel/international-a-level/chemistry/ych11}"
export YCH11_WS="${YCH11_WS:-/home/z/my-project/data/ych11_sb1}"
# grind + merge + audit + validate + reconcile read these
export YCH11_CORPUS="$YCH11_WS/out/edexcel_ial_chemistry_ych11_sb1_chunks_v1.jsonl"
export YCH11_PRISTINE="$YCH11_LANE/parsed/edexcel_ial_chemistry_ych11_sb1_chunks_v1.pristine"
export YCH11_IDS="$YCH11_WS/llm_repair_ids_ych11.json"   # copy from $YCH11_LANE/pipeline/evidence/
export YCH11_REPAIRS="$YCH11_WS/llm_repairs_ych11.jsonl" # copy from evidence/, runner appends here
export YCH11_LOG="$YCH11_WS/llm_repair_ych11.log"
export YCH11_MD="$YCH11_WS/out/full_book_docling.md"
export YCH11_REPORT="$YCH11_WS/out/parse_report_v1.json"
# runner cadence (L-017/L-027: foreground windows only; PROBE_WAIT 45s fits
# more probes into a 10-min window than the original 90s)
export CONC="${CONC:-2}"
export PROBE_WAIT="${PROBE_WAIT:-45}"
# landing: source this, then:  ych11_reseed.sh && merge_llm_ych11.py &&
# YCH11_BASELINE=$YCH11_WS/out/baseline_landed_v1.jsonl ych11_reconcile.py &&
# audit_polish_ych11.py && validate_ych11.py
