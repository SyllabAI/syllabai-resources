#!/bin/bash
# Probe-loop wrapper for 4BI1 LLM polish (PM-3 protocol).
# Each iteration: 1 lean probe (PROBE_MAX=1 PROBE_WAIT=30). If quota clear,
# the runner processes (CONC=2) until quota-stop/todo-done; if walled, sleep
# WAIT_BETWEEN and retry. Exits when todo=0 or TIMEOUT_S elapsed, so the Bash
# tool's 10-min cap kills nothing mid-write (records append per chunk).
set -u
cd /home/z/my-project/scripts
END=$((SECONDS + ${TIMEOUT_S:-480}))
WAIT=${WAIT_BETWEEN:-90}
RESUME=/home/z/my-project/data/biology/llm_repairs_biology.jsonl
IDS=/home/z/my-project/data/biology/llm_repair_ids_biology.json

remaining() {
  node -e "
const fs=require('fs');
const ids=JSON.parse(fs.readFileSync('$IDS','utf-8'));
const done=new Set();
if(fs.existsSync('$RESUME')){
  for(const l of fs.readFileSync('$RESUME','utf-8').split('\n')){
    if(l.trim()){try{const r=JSON.parse(l);if(r.status==='ok'||r.status==='rejected')done.add(r.id)}catch{}}
  }
}
console.log(ids.filter(i=>!done.has(i)).length);"
}

while [ $SECONDS -lt $END ]; do
  PROBE_MAX=1 PROBE_WAIT=30 CONC=2 node llm_repair_biology.js 2>&1 | grep -vE "Failed to make API request|^    at |^$" | tail -6
  REM=$(remaining)
  echo "[loop t=${SECONDS}s] remaining todo: $REM"
  if [ "$REM" = "0" ]; then echo "[loop] POLISH COMPLETE"; exit 0; fi
  if [ $((SECONDS + WAIT)) -gt $END ]; then echo "[loop] not enough window time left, exiting"; exit 0; fi
  sleep $WAIT
done
echo "[loop] window ended, resume later"
