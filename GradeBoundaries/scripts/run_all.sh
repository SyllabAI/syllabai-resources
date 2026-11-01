#!/usr/bin/env bash
# GradeBoundaries full pipeline — fail-loud at every gate.
# Run from anywhere; every script resolves its own paths.
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "== [1/6] fetch Pearson (slug-matrix probe)"
python3 "$DIR/fetch_pearson.py" "$@"
echo "== [2/6] fetch CIE (known-ID registry)"
python3 "$DIR/fetch_cie.py" "$@"
echo "== [3/6] parse Pearson (positional)"
python3 "$DIR/parse_pearson.py"
echo "== [4/6] parse CIE"
python3 "$DIR/parse_cie.py"
echo "== [5/6] validate (schema + golden parity + coverage)"
python3 "$DIR/validate.py"
echo "== [6/6] build hub-import bundle"
python3 "$DIR/build_hub_import.py"
echo "ALL GREEN"
