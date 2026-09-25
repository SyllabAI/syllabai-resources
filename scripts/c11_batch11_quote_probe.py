#!/usr/bin/env python3
"""T-C11 session 66 — batch-11 quote probe (fail-closed).

Walks scripts/c11_batch11_decisions.yaml and verifies EVERY evidence quote
(nodes + edges) matches its cited file under the batch-8 G03/c11.4
normalization convention (c11_batch10_quote_probe.py's norm(): NFC, markdown
link-unwrap, HTML tag strip, emphasis strip, dash/quote translation,
whitespace collapse) — the byte-honest anchor convention the quote probe
has enforced since the pilot. Also verifies the 4.15 negative control: no
evidence file reference and no quote may carry a 4.15 anchor. Run BEFORE
the registry grows (the batch-8 pre-verification precedent).
"""
from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
DECISIONS = HERE / "c11_batch11_decisions.yaml"

_TRANS = {ord("–"): "-", ord("—"): "-", ord("″"): '"', ord("′"): "'"}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFC", s)
    s = s.replace("\\", "")
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"[*_`#>]+", "", s)
    s = s.translate(_TRANS)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def main() -> int:
    doc = yaml.safe_load(DECISIONS.read_text(encoding="utf-8"))
    checks = 0
    fails = []
    # node evidence (spec_points attachments + the misconception-class
    # node-level evidence/remediation_evidence)
    for n in doc["nodes"]:
        if n.get("spec_points"):
            for sp in n["spec_points"]:
                for ev in sp["evidence"]:
                    checks += 1
                    p = REPO / ev["file"]
                    if not p.exists():
                        fails.append(f"{n['code']}: missing file {ev['file']}")
                        continue
                    hay = norm(p.read_text(encoding="utf-8"))
                    if norm(ev["quote"]) not in hay:
                        fails.append(f"{n['code']} ({sp['code']}): quote not "
                                     f"verbatim in {ev['file']}: "
                                     f"{ev['quote'][:70]!r}")
                    if "4.15" in ev["file"] or "4.15" in ev["quote"]:
                        fails.append(f"{n['code']}: 4.15 citation leak")
        for group, kind_label in ((n.get("evidence") or [], "node-evidence"),
                                  (n.get("remediation_evidence") or [],
                                   "remediation-evidence")):
            for ev in group:
                checks += 1
                p = REPO / ev["file"]
                if not p.exists():
                    fails.append(f"{n['code']}: missing file {ev['file']}")
                    continue
                hay = norm(p.read_text(encoding="utf-8"))
                if norm(ev["quote"]) not in hay:
                    fails.append(f"{n['code']} ({kind_label}): quote not "
                                 f"verbatim in {ev['file']}: "
                                 f"{ev['quote'][:70]!r}")
                if "4.15" in ev["file"] or "4.15" in ev["quote"]:
                    fails.append(f"{n['code']}: 4.15 citation leak")
    # edge evidence
    for e in doc["edges"]:
        for ev in e["evidence"]:
            checks += 1
            p = REPO / ev["file"]
            if not p.exists():
                fails.append(f"{e['source']}->{e['target']}: missing file "
                             f"{ev['file']}")
                continue
            hay = norm(p.read_text(encoding="utf-8"))
            if norm(ev["quote"]) not in hay:
                fails.append(f"{e['source']}->{e['target']} "
                             f"({e['relation']}): quote not verbatim in "
                             f"{ev['file']}: {ev['quote'][:70]!r}")
            if "4.15" in ev["file"] or "4.15" in ev["quote"]:
                fails.append(f"{e['source']}->{e['target']}: 4.15 leak")
    # no 4.15 citation anywhere in the evidence anchors; the raw record
    # text mentions 4.15 only in the sanctioned meta/provenance prose
    raw = DECISIONS.read_text(encoding="utf-8")
    n415 = raw.count("4.15")
    if n415 > 5:  # the sanctioned meta + provenance-prose mentions only
        fails.append(f"4.15 appears {n415}x in the record (expected <= 5 "
                     f"sanctioned prose mentions)")
    print(f"quote probe: {checks} evidence anchors checked")
    if fails:
        print(f"FAILED: {len(fails)}")
        for f in fails:
            print("  -", f)
        return 1
    print("c11_batch11_quote_probe: ALL PASS — every quote verbatim under "
          "the batch-8 anchor convention; the 4.15 negative control "
          "carries no anchor")
    return 0


if __name__ == "__main__":
    sys.exit(main())
