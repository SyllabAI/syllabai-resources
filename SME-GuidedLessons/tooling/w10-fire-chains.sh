#!/bin/bash
# w10-fire-chains.sh — WAVE-10 chain ignition (corrected invocation pattern, native).
# Per note: start -> phase P1 unflagged -> phase P2..P8 --assist -> export, one
# single-shell invocation per note. 19 events per log; assistedPhases = P1..P7;
# P0 closes unflagged; single export; zero pauses. The FINAL wave: 8 notes.
set -e
export WAVE1_RUNS_DIR=/home/z/my-project/.tmp/wave10/runs
export WAVE1_DL_DIR=/home/z/my-project/download/wave10
RUN=/home/z/my-project/scripts/wave1-run.js
TMP=/home/z/my-project/.tmp/wave10
mkdir -p "$WAVE1_RUNS_DIR" "$WAVE1_DL_DIR"

NOTES="rn_8T5GfPn2q7sY2YCh rn_ncFJkGhXFsKrkNkH rn_2z53qk2CdWrVVc7V rn_BBGMYy3Yx9Nm4GV3 rn_BDkhS5vQpRd4hvwf rn_7ZMc3T3J4SJXfNdR rn_bvyrkKqRBMKCRzHM rn_bGgYrQXP2tqrYwdV"

n=0
for id in $NOTES; do
  n=$((n+1))
  echo "== CHAIN $n/8: $id =="
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
echo "ALL 8 CHAINS FIRED"
