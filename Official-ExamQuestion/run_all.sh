#!/usr/bin/env bash
# ADR-037 full-corpus runner + canary verification.
# Usage:   bash Official-ExamQuestion/run_all.sh
# Env:     SKIP_FETCH=1     skip staging inputs (assume already downloaded/extracted)
#          EXAMQ_PAPERS     paper variants to run (default "1C 2C"; F34)
set -uo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"                 # .../syllabai-resources/Official-ExamQuestion
RES="$(cd "$ROOT/.." && pwd)"                          # .../syllabai-resources
UP="${EXAMQ_UPLOAD_DIR:-/home/z/my-project/upload}"    # staging area for inputs (see AGENTS.md)
mkdir -p "$UP"
GHTOKEN="${GHTOKEN:-}"
PAPERS="${EXAMQ_PAPERS:-1C 2C}"                        # F34: paper variants (1C=110 marks, 2C=70)
BASEURL="https://raw.githubusercontent.com/SyllabAI/syllabai-pastpapers/main/past-papers/pearson-edexcel/international-gcse/chemistry/4ch1/past-papers"

# Bootstrap the series index when absent (LEDGER F16): one contents-API call on
# the 4CH1 series directory. The recursive git/trees API TRUNCATES on large
# repos (~39k entries observed) and can silently omit subtrees — never rely on it.
if [ ! -s "$UP/pp-tree.json" ]; then
  echo "bootstrapping pp-tree.json (series enumeration via contents API)"
  GHTOKEN="$GHTOKEN" python3 - "$UP/pp-tree.json" <<'PY'
import json, os, subprocess, sys
out = sys.argv[1]
tok = os.environ.get("GHTOKEN", "")
url = ("https://api.github.com/repos/SyllabAI/syllabai-pastpapers/contents/"
       "past-papers/pearson-edexcel/international-gcse/chemistry/4ch1/past-papers?ref=main")
cmd = ["curl", "-s"]
if tok: cmd += ["-H", f"Authorization: token {tok}"]
cmd += [url]
entries = json.loads(subprocess.run(cmd, capture_output=True, text=True, timeout=60).stdout or "null")
if not isinstance(entries, list):
    sys.exit("F16 bootstrap failed: contents API did not return a directory list (auth? repo moved?)")
series = sorted(e["name"] for e in entries if e.get("type") == "dir")
pre = "past-papers/pearson-edexcel/international-gcse/chemistry/4ch1/past-papers"
tree = []
for s in series:
    for paper in ("1C", "2C", "1CR", "2CR"):   # F34 + the F-178 R-variant tranches
        tree.append({"path": f"{pre}/{s}/4CH1-{paper}/qp.pdf"})
json.dump({"tree": tree,
           "note": "synthesized series index via contents API (git/trees recursive truncates; F16; papers per F34)"},
          open(out, "w"))
print("  series enumerated:", len(series))
PY
fi

SERIES=$(python3 - <<'PY'
import json, re, os
p = os.environ.get("EXAMQ_UPLOAD_DIR", "/home/z/my-project/upload") + "/pp-tree.json"
t = json.load(open(p))
pat = re.compile(r"4ch1/past-papers/([^/]+)/4CH1-[0-9][A-Z]R?/qp\.pdf$")
print(" ".join(sorted({m.group(1) for e in t["tree"] if (m := pat.search(e.get("path", "")))})))
PY
)
[ -n "$SERIES" ] || { echo "cannot enumerate series (pp-tree.json missing)"; exit 1; }
echo "series: $SERIES"
echo "papers: $PAPERS"

for S in $SERIES; do
  for PAPER in $PAPERS; do
    if [ "${SKIP_FETCH:-0}" != "1" ]; then
      D="$BASEURL/$S/4CH1-$PAPER"
      for f in manifest.yaml qp.pdf ms.pdf; do
        case "$f" in
          manifest.yaml) out="$UP/manifest-$S-$PAPER.yaml";;
          qp.pdf)        out="$UP/official-4CH1-$PAPER-$S-qp.pdf";;
          ms.pdf)        out="$UP/official-4CH1-$PAPER-$S-ms.pdf";;
        esac
        if [ ! -s "$out" ]; then
          code=$(curl -s -L -w '%{http_code}' ${GHTOKEN:+-H "Authorization: token $GHTOKEN"} "$D/$f" -o "$out")
          [ "$code" = "200" ] || { echo "FETCH-FAIL $S/4CH1-$PAPER/$f HTTP $code"; exit 1; }
        fi
      done
      [ -s "$UP/official-$S-$PAPER-qp.txt" ] || pdftotext -layout "$UP/official-4CH1-$PAPER-$S-qp.pdf" "$UP/official-$S-$PAPER-qp.txt" 2>/dev/null
      [ -s "$UP/official-$S-$PAPER-ms.txt" ] || pdftotext -layout "$UP/official-4CH1-$PAPER-$S-ms.pdf" "$UP/official-$S-$PAPER-ms.txt" 2>/dev/null
    fi
    echo "--- run $S / 4CH1-$PAPER"
    python3 "$RES/scripts/official_examq_extract.py" --series "$S" --paper "$PAPER" >/dev/null || { echo "RUN-FAIL $S/$PAPER"; exit 1; }
  done
done

# cross-diff where the repo has a parsed layer (1C dirs only today; F34), then the aggregate report
for S in 2024-06 2025-06 2026-06; do
  [ -s "$UP/parsed-$S-questions.json" ] || \
    curl -s -L ${GHTOKEN:+-H "Authorization: token $GHTOKEN"} \
      "$BASEURL/$S/4CH1-1C/parsed/questions.json" -o "$UP/parsed-$S-questions.json"
done
python3 "$RES/scripts/cross_diff_parsed.py" --paper 1C || exit 1
python3 "$RES/scripts/make_multiseries_report.py" || exit 1

# gate: every canary must hold before this corpus is shippable
python3 "$ROOT/check_canaries.py" || { echo "CANARIES FAILED — corpus NOT shippable"; exit 1; }
echo "run_all complete: corpus regenerated, report refreshed, canaries hold."
