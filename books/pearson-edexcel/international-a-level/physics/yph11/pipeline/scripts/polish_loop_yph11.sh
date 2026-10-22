#!/bin/bash
# Probe-loop wrapper for YPH11 SB1 LLM polish (PM-3 protocol).
set -u
cd /home/z/my-project/scripts
END=$((SECONDS + ${TIMEOUT_S:-470}))
WAIT=${WAIT_BETWEEN:-60}
RESUME=/home/z/my-project/data/llm_repairs_yph11.jsonl
IDS=/home/z/my-project/data/llm_repair_ids_yph11.json
remaining() {
  node -e "
    const fs = require('fs');
    const ids = JSON.parse(fs.readFileSync('$IDS', 'utf-8'));
    const done = new Set();
    if (fs.existsSync('$RESUME')) {
      for (const line of fs.readFileSync('$RESUME', 'utf-8').split('\n')) {
        if (!line.trim()) continue;
        try { const r = JSON.parse(line); if (r.status === 'ok' || r.status === 'rejected') done.add(r.id); } catch {}
      }
    }
    console.log(ids.filter(i => !done.has(i)).length);
  "
}
while [ $SECONDS -lt $END ]; do
  PROBE_MAX=2 PROBE_WAIT=45 CONC=2 node llm_repair_yph11.js 2>&1 | grep -vE "Failed to make API request|^    at |^$" | tail -4
  REM=$(remaining)
  echo "[loop t=${SECONDS}s] remaining todo: $REM"
  if [ "$REM" = "0" ]; then echo "[loop] POLISH COMPLETE"; exit 0; fi
  if [ $((SECONDS + WAIT)) -gt $END ]; then echo "[loop] window end"; exit 0; fi
  sleep $WAIT
done
echo "[loop] batch window ended, resume later"
