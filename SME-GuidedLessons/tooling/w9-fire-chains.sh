#!/bin/bash
# w9-fire-chains.sh — WAVE-9 chain ignition (corrected invocation pattern, native).
# Per note: start -> phase P1 unflagged -> phase P2..P8 --assist -> export, one
# single-shell invocation per note. 19 events per log; assistedPhases = P1..P7;
# P0 closes unflagged; single export; zero pauses.
set -e
export WAVE1_RUNS_DIR=/home/z/my-project/.tmp/wave9/runs
export WAVE1_DL_DIR=/home/z/my-project/download/wave9
RUN=/home/z/my-project/scripts/wave1-run.js
TMP=/home/z/my-project/.tmp/wave9
mkdir -p "$WAVE1_RUNS_DIR" "$WAVE1_DL_DIR"

NOTES="rn_wDdXr5k7gknQ7xJp rn_NdJGQM8BqHmTy7Vg rn_HqqBFgKRHykMMhbB rn_H9chr9BWCfXYW472 rn_V3hNWh6QWrbCRHrX rn_9J7DQhskyxzhd7CP rn_DrqzYWZMScqGrbWT rn_6c2G8nJpFSnQnbcP rn_MmqCNJfWbtYzRVqT rn_H2zGfgH76qYV5cmr rn_DBGf3WVffDBNDp4R rn_2MpXPtNXvn8pQm3r"

n=0
for id in $NOTES; do
  n=$((n+1))
  echo "== CHAIN $n/12: $id =="
  node "$RUN" start "$id" \
    && node "$RUN" phase "$id" P1 \
    && node "$RUN" phase "$id" P2 --assist \
    && node "$RUN" phase "$id" P3 --assist \
    && node "$RUN" phase "$id" P4 --assist \
    && node "$RUN" phase "$id" P5 --assist \
    && node "$RUN" phase "$id" P6 --assist \
    && node "$RUN" phase "$id" P7 --assist \
    && node "$RUN" phase "$id" P8 --assist \
    && node "$RUN" export "$id" "$TMP/layer-$id.json" \
    || { echo "CHAIN FAILED: $id"; exit 1; }
done
echo "ALL 12 CHAINS FIRED"
