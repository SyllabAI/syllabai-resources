#!/usr/bin/env bash
# YCH12 SB2 v2 polish lane — L-024/R-013 re-seed law, executable form.
# Re-seed BEFORE EVERY merge invocation (the merge is not idempotent):
#   1. corpus  <- v2 .pristine        (merge clobbers text_original on re-run)
#   2. report  <- landed parse_report (merge preserves existing keys; a fresh
#      workspace report would drop by_design_gaps — CONT-V2-5 lesson)
#   3. baseline<- landed corpus       (three-way reconciliation net-new input)
# Usage: source your env surface first, then run this script. Idempotent.
set -euo pipefail
LANE="${YCH12_LANE:?YCH12_LANE must point at the ych12 lane dir (…/chemistry/ych12)}"
CORPUS="${YCH12_CORPUS:?}"
PRISTINE="${YCH12_PRISTINE:?}"
REPORT="${YCH12_REPORT:?}"
WS="$(dirname "$CORPUS")"
cp "$PRISTINE" "$CORPUS"
cp "$LANE/parsed/parse_report_v2.json" "$REPORT"
cp "$LANE/parsed/edexcel_ial_chemistry_ych12_sb2_chunks_v2.jsonl" "$WS/baseline_landed_v2.jsonl"
echo "RESEED OK: corpus+report+baseline re-seeded ($LANE -> $WS)"
