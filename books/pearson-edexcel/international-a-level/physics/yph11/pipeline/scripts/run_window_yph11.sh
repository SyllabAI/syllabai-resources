#!/bin/bash
# One foreground window of the YPH11 SB1 Docling grind, resume-safe.
# Usage: bash run_window_yph11.sh FROM TO
# The Bash tool kills batches at 10 min; each window must fit with margin.
# Pages already checkpointed are skipped by docling_full_yph11.py itself.
set -u
cd /home/z/my-project
export DOCLING_ARTIFACTS_PATH=/home/z/my-project/data/models
export YPH11_OFFSET=11
LOG=/home/z/my-project/data/yph11_sb1/parse.log
mkdir -p /home/z/my-project/data/yph11_sb1
FROM=${1:?from}; TO=${2:?to}
echo "=== window $FROM-$TO start $(date +%H:%M:%S) ===" >> $LOG
timeout 560 python3 scripts/docling_full_yph11.py "$FROM" "$TO" >> $LOG 2>&1
RC=$?
DONE=$(ls /home/z/my-project/data/yph11_sb1/docling_pages/ 2>/dev/null | wc -l)
echo "=== window $FROM-$TO rc=$RC total=$DONE/225 $(date +%H:%M:%S) ===" >> $LOG
echo "[window $FROM-$TO rc=$RC done=$DONE/225]"
