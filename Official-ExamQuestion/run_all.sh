#!/usr/bin/env bash
# ADR-037 full-corpus runner + canary verification.
# Usage:   bash Official-ExamQuestion/run_all.sh
# Env:     SKIP_FETCH=1   skip staging inputs (assume already downloaded/extracted)
set -uo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"                 # .../syllabai-resources/Official-ExamQuestion
RES="$(cd "$ROOT/.." && pwd)"                          # .../syllabai-resources
UP=/home/z/my-project/upload                           # staging area for inputs (see AGENTS.md)
GHTOKEN="${GHTOKEN:-}"
BASEURL="https://raw.githubusercontent.com/SyllabAI/syllabai-pastpapers/main/past-papers/pearson-edexcel/international-gcse/chemistry/4ch1/past-papers"

SERIES=$(python3 - <<'PY'
import json, re
t = json.load(open("/home/z/my-project/upload/pp-tree.json"))
pat = re.compile(r"4ch1/past-papers/([^/]+)/4CH1-1C/qp\.pdf$")
print(" ".join(sorted({m.group(1) for e in t["tree"] if (m := pat.search(e.get("path", "")))})))
PY
)
[ -n "$SERIES" ] || { echo "cannot enumerate series (pp-tree.json missing)"; exit 1; }
echo "series: $SERIES"

for S in $SERIES; do
  if [ "${SKIP_FETCH:-0}" != "1" ]; then
    D="$BASEURL/$S/4CH1-1C"
    for f in manifest.yaml qp.pdf ms.pdf; do
      case "$f" in
        manifest.yaml) out="$UP/manifest-$S-1C.yaml";;
        qp.pdf)        out="$UP/official-4CH1-1C-$S-qp.pdf";;
        ms.pdf)        out="$UP/official-4CH1-1C-$S-ms.pdf";;
      esac
      if [ ! -s "$out" ]; then
        code=$(curl -s -L -w '%{http_code}' ${GHTOKEN:+-H "Authorization: token $GHTOKEN"} "$D/$f" -o "$out")
        [ "$code" = "200" ] || { echo "FETCH-FAIL $S/$f HTTP $code"; exit 1; }
      fi
    done
    [ -s "$UP/official-$S-qp.txt" ] || pdftotext -layout "$UP/official-4CH1-1C-$S-qp.pdf" "$UP/official-$S-qp.txt" 2>/dev/null
    [ -s "$UP/official-$S-ms.txt" ] || pdftotext -layout "$UP/official-4CH1-1C-$S-ms.pdf" "$UP/official-$S-ms.txt" 2>/dev/null
  fi
  echo "--- run $S"
  python3 "$RES/scripts/official_examq_extract.py" --series "$S" >/dev/null || { echo "RUN-FAIL $S"; exit 1; }
done

# cross-diff where the repo has a parsed layer, then the aggregate report
for S in 2024-06 2025-06 2026-06; do
  [ -s "$UP/parsed-$S-questions.json" ] || \
    curl -s -L ${GHTOKEN:+-H "Authorization: token $GHTOKEN"} \
      "$BASEURL/$S/4CH1-1C/parsed/questions.json" -o "$UP/parsed-$S-questions.json"
done
python3 "$RES/scripts/cross_diff_parsed.py" || exit 1
python3 "$RES/scripts/make_multiseries_report.py" || exit 1

# gate: every canary must hold before this corpus is shippable
python3 "$ROOT/check_canaries.py" || { echo "CANARIES FAILED — corpus NOT shippable"; exit 1; }
echo "run_all complete: corpus regenerated, report refreshed, canaries hold."
