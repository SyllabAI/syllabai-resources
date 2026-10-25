#!/usr/bin/env bash
# ADR-037 full-corpus runner + canary verification, as a leg-structured battery
# (LEDGER F63; culture: Official-ExamQuestion/RECEIPTS-AND-BATTERIES.md).
# Usage:   bash Official-ExamQuestion/run_all.sh
# Env:     SKIP_FETCH=1     skip staging inputs (assume already downloaded/extracted)
#          EXAMQ_PAPERS     paper variants to run (default "1C 2C"; F34)
#          EXAMQ_RECEIPT_DIR  where battery receipts land (default <kit>/receipts, gitignored)
set -uo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"                 # .../syllabai-resources/Official-ExamQuestion
RES="$(cd "$ROOT/.." && pwd)"                          # .../syllabai-resources
UP="${EXAMQ_UPLOAD_DIR:-/home/z/my-project/upload}"    # staging area for inputs (see AGENTS.md)
mkdir -p "$UP"
GHTOKEN="${GHTOKEN:-}"
PAPERS="${EXAMQ_PAPERS:-1C 2C}"                        # F34: paper variants (1C=110 marks, 2C=70)
BASEURL="https://raw.githubusercontent.com/SyllabAI/syllabai-pastpapers/main/past-papers/pearson-edexcel/international-gcse/chemistry/4ch1/past-papers"

# --- battery receipt infrastructure (F63): evidence or it didn't happen ------
RECEIPT_DIR="${EXAMQ_RECEIPT_DIR:-$ROOT/receipts}"
mkdir -p "$RECEIPT_DIR" || exit 1
RECEIPT_LEGS="$RECEIPT_DIR/.battery-legs-$$"
RECEIPT_OUT="$RECEIPT_DIR/battery-$(date -u +%Y%m%dT%H%M%SZ)-$$.json"
BATTERY_STARTED=$(date -u +%Y-%m-%dT%H:%M:%SZ)
: > "$RECEIPT_LEGS"
trap 'rm -f "$RECEIPT_LEGS"' EXIT
BATTERY_NAME=""; BATTERY_T0=0
battery_begin() { BATTERY_NAME="$1"; BATTERY_T0=$(date +%s); echo "=== leg: $BATTERY_NAME"; }
battery_end() {  # records name|exit|seconds; passes the leg's exit through
  local rc="$1"
  printf '%s|%s|%s\n' "$BATTERY_NAME" "$rc" "$(( $(date +%s) - BATTERY_T0 ))" >> "$RECEIPT_LEGS"
  return "$rc"
}
finish_receipt() {  # legs must already be recorded; the pass bit is computed from them
  python3 - "$RECEIPT_LEGS" "$RECEIPT_OUT" "$BATTERY_STARTED" "$RES" "$PAPERS" "$SERIES" <<'PY'
import datetime, json, os, subprocess, sys
legs_path, out, started, res, papers, series = sys.argv[1:7]
legs = []
for line in open(legs_path):
    name, rc, secs = line.rstrip("\n").split("|")
    legs.append({"name": name, "exit": int(rc), "seconds": int(secs)})
def git(*a):
    try:
        return subprocess.run(["git", "-C", res, *a], capture_output=True, text=True, timeout=15).stdout.strip()
    except Exception:
        return ""
head = git("rev-parse", "--short", "HEAD") or None
dirty = bool(git("status", "--porcelain", "--", "Official-ExamQuestion").strip()) if head else None
n_pass = sum(1 for l in legs if l["exit"] == 0)
receipt = {
    "battery": "Official-ExamQuestion run_all battery (ADR-037 corpus)",
    "receipt_schema": "syllabai.examq-battery-receipt/0.1",
    "started_utc": started,
    "finished_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "git_head": head,
    "git_dirty": dirty,
    "papers": papers,
    "series_count": len(series.split()),
    "env": {"SKIP_FETCH": os.environ.get("SKIP_FETCH", "0"),
            "EXAMQ_UPLOAD_DIR": os.environ.get("EXAMQ_UPLOAD_DIR", "/home/z/my-project/upload")},
    "legs": legs,
    "summary": f"{n_pass}/{len(legs)} PASS",
    "pass": bool(legs) and all(l["exit"] == 0 for l in legs),
}
json.dump(receipt, open(out, "w"), indent=2)
print(f"battery receipt: {out}  [{receipt['summary']}]")
PY
}

# Bootstrap the series index when absent (LEDGER F16): one contents-API call on
# the 4CH1 series directory. The recursive git/trees API TRUNCATES on large
# repos (~39k entries observed) and can silently omit subtrees — never rely on it.
battery_begin "bootstrap-series-index"
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
[ -n "$SERIES" ] || { echo "cannot enumerate series (pp-tree.json missing)"; battery_end 1; finish_receipt; exit 1; }
echo "series: $SERIES"
echo "papers: $PAPERS"
battery_end 0

battery_begin "convert-corpus"
convert_corpus() {
for S in $SERIES; do
  for PAPER in $PAPERS; do
    # F-178: the R papers exist for exactly 11 of the 16 series (2021-06/2021-11/
    # 2023-11/2024-11/2025-11 never printed a 1CR/2CR; 2020-06 never ran). Skip
    # combos the registry of record does not expect instead of crashing in G0.
    if ! python3 -c "
import sys
sys.path.insert(0, '$RES/scripts')
from official_examq_extract import EXPECT_QUESTIONS
sys.exit(0 if EXPECT_QUESTIONS['$PAPER'].get('$S') else 1)"; then
      echo "skip $S/4CH1-$PAPER (paper never printed — F-178 registry)"; continue
    fi
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
          [ "$code" = "200" ] || { echo "FETCH-FAIL $S/4CH1-$PAPER/$f HTTP $code"; return 1; }
        fi
      done
      [ -s "$UP/official-$S-$PAPER-qp.txt" ] || pdftotext -layout "$UP/official-4CH1-$PAPER-$S-qp.pdf" "$UP/official-$S-$PAPER-qp.txt" 2>/dev/null
      [ -s "$UP/official-$S-$PAPER-ms.txt" ] || pdftotext -layout "$UP/official-4CH1-$PAPER-$S-ms.pdf" "$UP/official-$S-$PAPER-ms.txt" 2>/dev/null
    fi
    echo "--- run $S / 4CH1-$PAPER"
    python3 "$RES/scripts/official_examq_extract.py" --series "$S" --paper "$PAPER" >/dev/null || { echo "RUN-FAIL $S/$PAPER"; return 1; }
  done
done
}
convert_corpus; rc=$?
battery_end "$rc" || { finish_receipt; exit 1; }

battery_begin "cross-diff"
# cross-diff where the repo has a parsed layer (1C dirs only today; F34)
for S in 2024-06 2025-06 2026-06; do
  [ -s "$UP/parsed-$S-questions.json" ] || \
    curl -s -L ${GHTOKEN:+-H "Authorization: token $GHTOKEN"} \
      "$BASEURL/$S/4CH1-1C/parsed/questions.json" -o "$UP/parsed-$S-questions.json"
done
python3 "$RES/scripts/cross_diff_parsed.py" --paper 1C
battery_end $? || { finish_receipt; exit 1; }

battery_begin "cross-diff-2C"
# 2C independent-parse cross-diff (wave-26): the repo's 2C parsed layer covers all
# 16 sittings (pastpapers PR #3 + the pre-existing 2024-06/2026-06). Files are
# namespaced parsed-2C-$S-questions.json so they cannot clobber the 1C layer.
for S in 2019-06 2020-01 2020-11 2021-01 2021-06 2021-11 2022-01 2022-06 2023-01 \
         2023-06 2023-11 2024-06 2024-11 2025-06 2025-11 2026-06; do
  [ -s "$UP/parsed-2C-$S-questions.json" ] || \
    curl -s -L ${GHTOKEN:+-H "Authorization: token $GHTOKEN"} \
      "$BASEURL/$S/4CH1-2C/parsed/questions.json" -o "$UP/parsed-2C-$S-questions.json"
done
python3 "$RES/scripts/cross_diff_parsed.py" --paper 2C
battery_end $? || { finish_receipt; exit 1; }

battery_begin "cross-diff-2CR"
# 2CR independent-parse cross-diff (wave-27): the repo's 2CR parsed layer covers
# all 11 sittings (pastpapers PR #4 + the pre-existing 2026-06). Files are
# namespaced parsed-2CR-$S-questions.json so they cannot clobber the other layers.
for S in 2019-06 2020-01 2020-11 2021-01 2022-01 2022-06 2023-01 2023-06 \
         2024-06 2025-06 2026-06; do
  [ -s "$UP/parsed-2CR-$S-questions.json" ] || \
    curl -s -L ${GHTOKEN:+-H "Authorization: token $GHTOKEN"} \
      "$BASEURL/$S/4CH1-2CR/parsed/questions.json" -o "$UP/parsed-2CR-$S-questions.json"
done
python3 "$RES/scripts/cross_diff_parsed.py" --paper 2CR
battery_end $? || { finish_receipt; exit 1; }

battery_begin "aggregate-report"
python3 "$RES/scripts/make_multiseries_report.py"
battery_end $? || { finish_receipt; exit 1; }

battery_begin "enrich-verify"
# ADR-039 §8 step 3 — verifier promoted corpus-wide at build time (was:
# enrichment-slice scope in wave-21 staging). Every SOLUTION-ENRICH entry is
# in scope (base-ledger = the empty ledger written below). Evidence packs are
# re-staged deterministically from the committed corpus + the archive QP text
# layer (same field contract as the wave-21 packs: stem/groupStems/problem/
# ms/choices/markPoints + qpPages from pdftotext -layout, form-feed split) so
# the promoted census is reproducible from the checkout alone.
EMPTY_LEDGER="$UP/.empty-base-ledger.json"
[ -s "$EMPTY_LEDGER" ] || printf '{"entries": {}}' > "$EMPTY_LEDGER"
echo "--- staging corpus evidence packs (wave-21 field contract)"
python3 - "$UP/evidence" "$ROOT" <<'PY' || { echo "PACK-STAGING FAILED"; battery_end 1; finish_receipt; exit 1; }
import json, sys
from pathlib import Path
evdir = Path(sys.argv[1]); evdir.mkdir(parents=True, exist_ok=True)
out = evdir / "official-examq-packs.jsonl"
root = Path(sys.argv[2])
UP = Path(__import__("os").environ.get("EXAMQ_UPLOAD_DIR", "/home/z/my-project/upload"))
ledger = json.loads((root / "SOLUTION-ENRICH.json").read_text())["entries"]
corpus = {}
for d in sorted((root / "igcse-chemistry-19").iterdir()):
    if not d.is_dir():
        continue
    for pd in sorted(d.iterdir()):
        if not pd.name.startswith("4CH1-"):
            continue
        paper = pd.name.split("-")[1]
        t = json.loads((pd / "topic.json").read_text())
        for q in t["questions"]:
            for p in q["parts"]:
                slug = p["part_number"].replace("(", "-").replace(")", "")
                corpus[f"offp_{d.name}_{paper.lower()}_{slug}"] = (d.name, paper, q, p)
n = 0
with out.open("w") as fh:
    for key in ledger:
        series_paper, slug = key.split(":")
        series, paper = series_paper.rsplit("-", 1)
        part = corpus.get(f"offp_{series}_{paper.lower()}_{slug}")
        if not part:
            continue
        _, _, q, p = part
        qp_txt = UP / f"official-{series}-{paper}-qp.txt"
        pages = qp_txt.read_text(errors="replace").split("\f") if qp_txt.exists() else []
        fh.write(json.dumps({
            "key": key,
            "stem": q.get("stem_md") or "",
            "groupStems": "\n".join((v.get("group_stem_md") or "") for v in (q.get("groups") or {}).values()),
            "problem": p.get("problem_md") or "",
            "ms": p.get("solution_md") or "",
            "choices": p.get("choices") or [],
            "markPoints": [{"text": m.get("text_md") or ""} for m in (p.get("mark_points") or [])],
            "qpPages": pages,
        }, ensure_ascii=False) + "\n")
        n += 1
print(f"  packs staged: {n}/{len(ledger)} -> {out}")
PY
echo "--- corpus-wide enrich verifier (all SOLUTION-ENRICH entries in scope)"
python3 "$RES/scripts/official_examq_enrich_verify.py" \
  --corpus "$ROOT" --ledger "$ROOT/SOLUTION-ENRICH.json" \
  --base-ledger "$EMPTY_LEDGER" --evidence "$UP/evidence" \
  --report "$UP/enrich-verify-report.json" --quiet \
  || { echo "ENRICH-VERIFY FAILED — corpus NOT shippable"; battery_end 1; finish_receipt; exit 1; }
battery_end 0

# gate: every canary must hold before this corpus is shippable
battery_begin "canaries"
python3 "$ROOT/check_canaries.py" || { echo "CANARIES FAILED — corpus NOT shippable"; battery_end 1; finish_receipt; exit 1; }
battery_end 0
finish_receipt
echo "run_all complete: corpus regenerated, report refreshed, enrich-verify clean, canaries hold."
