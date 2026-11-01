#!/usr/bin/env bash
# YCH11 SB1 polish lane — L-024/R-013 re-seed law, executable form.
# Re-seed BEFORE EVERY merge invocation (the merge is not idempotent):
#   1. corpus  <- .pristine           (merge clobbers text_original on re-run)
#   2. report  <- landed parse_report (merge preserves existing keys; a fresh
#      workspace report would drop by_design_gaps — CONT-V2-5 lesson)
#   3. baseline<- landed corpus       (three-way reconciliation net-new input)
# Usage: source your env surface first, then run this script. Idempotent.
set -euo pipefail
LANE="${YCH11_LANE:?YCH11_LANE must point at the ych11 lane dir (…/chemistry/ych11)}"
CORPUS="${YCH11_CORPUS:?}"
PRISTINE="${YCH11_PRISTINE:?}"
REPORT="${YCH11_REPORT:?}"
WS="$(dirname "$CORPUS")"
mkdir -p "$WS"
cp "$PRISTINE" "$CORPUS"
cp "$LANE/parsed/parse_report_v1.json" "$REPORT"
cp "$LANE/parsed/edexcel_ial_chemistry_ych11_sb1_chunks_v1.jsonl" "$WS/baseline_landed_v1.jsonl"
echo "RESEED OK: corpus+report+baseline re-seeded ($LANE -> $WS)"
