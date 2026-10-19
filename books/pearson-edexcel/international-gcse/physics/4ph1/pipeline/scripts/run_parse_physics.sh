#!/bin/bash
# Background grinder: parse all 308 pages in 10-page windows, resume-safe.
export DOCLING_ARTIFACTS_PATH=/home/z/my-project/data/models
LOG=/home/z/my-project/data/physics/parse.log
echo "=== physics parse run started $(date) ===" >> $LOG
for ((s=1; s<=308; s+=10)); do
  e=$((s+9)); if [ $e -gt 308 ]; then e=308; fi
  python3 /home/z/my-project/scripts/docling_full_physics.py $s $e >> $LOG 2>&1
  echo "[window $s-$e loop-continue $(date)]" >> $LOG
done
echo "=== ALL 308 PAGES DONE $(date) ===" >> $LOG
