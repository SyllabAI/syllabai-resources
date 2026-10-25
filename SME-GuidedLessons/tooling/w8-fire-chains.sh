#!/bin/bash
# w8-fire-chains.sh — WAVE-8 chain ignition (corrected invocation pattern, native).
# Per note: start -> phase P1 unflagged -> phase P2..P8 --assist -> export, one
# single-shell invocation per note. 19 events per log; assistedPhases = P1..P7;
# P0 closes unflagged; single export; zero pauses.
set -e
export WAVE1_RUNS_DIR=/home/z/my-project/.tmp/wave8/runs
export WAVE1_DL_DIR=/home/z/my-project/download/wave8
RUN=/home/z/my-project/scripts/wave1-run.js
TMP=/home/z/my-project/.tmp/wave8
mkdir -p "$WAVE1_RUNS_DIR" "$WAVE1_DL_DIR"

NOTES="rn_x5m8QBWxtKvxQ9sx rn_w25KHshCMNQWwftj rn_dgVRCKCwn4rTGxGZ rn_HNXFQt7vM32g6PMv rn_KTZjJ7sPdDt4tkTH rn_6478QfpYNQDjZSvt rn_XJ8qXfzZJJFKXHnF rn_Zh6Pw56rjdMkPCD4 rn_tvwj4VZ6yFscPJfD rn_y85XYRv5QfgZFQxv rn_H6ZVkxvdNgYDvfFb rn_3wZh9qRT7qFJn9QW rn_t68QRDhwR6r5gxYX rn_DRQXrcSrmgQ7jcbZ"

n=0
for id in $NOTES; do
  n=$((n+1))
  echo "== CHAIN $n/14: $id =="
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
echo "ALL 14 CHAINS FIRED"
