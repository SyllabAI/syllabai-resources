#!/bin/bash
# wave6-chain.sh — fire one note's chain native (corrected invocation pattern, first native
# full use at wave-4; one single-shell invocation per note).
# Usage: bash scripts/wave6-chain.sh <noteId>
set -e
N="$1"
export WAVE1_RUNS_DIR=/home/z/my-project/.tmp/wave6/runs
export WAVE1_DL_DIR=/home/z/my-project/download/wave6
L=/home/z/my-project/.tmp/wave6/layer-$N.json
node /home/z/my-project/scripts/wave1-run.js start "$N"
node /home/z/my-project/scripts/wave1-run.js phase "$N" P1
node /home/z/my-project/scripts/wave1-run.js phase "$N" P2 --assist
node /home/z/my-project/scripts/wave1-run.js phase "$N" P3 --assist
node /home/z/my-project/scripts/wave1-run.js phase "$N" P4 --assist
node /home/z/my-project/scripts/wave1-run.js phase "$N" P5 --assist
node /home/z/my-project/scripts/wave1-run.js phase "$N" P6 --assist
node /home/z/my-project/scripts/wave1-run.js phase "$N" P7 --assist
node /home/z/my-project/scripts/wave1-run.js phase "$N" P8 --assist
node /home/z/my-project/scripts/wave1-run.js export "$N" "$L"
