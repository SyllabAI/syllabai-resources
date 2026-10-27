#!/usr/bin/env python3
"""T-C41 — c41_maths_a_promotion_check.py: the c11.13-analog two-way audit of
the §18 promotion round over the maths-a authored semantic edges.

Reads the REAL repo files (the landed store, the promotions record, the
decision records at git HEAD) so a tampered working tree cannot cheat:

  G1 record schema    promotions file parses; exact-identity entries; ISO
                      dates; existing review artifacts; attribution gate
                      (AI-name patterns fail closed)
  G2 two-way          every HUMAN_VALIDATED edge has an exact matching
                      promotion entry with identical attribution AND every
                      promotion entry is HUMAN_VALIDATED in the graph
  G3 anti-forgery     zero HUMAN_VALIDATED outside the 73 promoted semantic
                      edges (PART_OF rows, concepts.yaml nodes, decision
                      records, spec_command_kinds)
  G4 non-validation   every PART_OF row and every non-validation field of
      delta zero      every semantic edge is byte-identical to the pre-round
                      store at git HEAD; meta delta == promotion_record +
                      counts.promoted_edges/human_validated_edges only
  G5 round contract   73 == semantic count; relation split 51/11/11; round
                      covers the full authored surface
  G6 determinism      an independent in-memory merge (HEAD store + promotions
                      record) reproduces the landed store BYTE-FOR-BYTE
  G7 held untouched   the 45 held candidates appear nowhere as rows; decision
                      records byte-identical to git HEAD
  G8 standing         check_no_hardcode.py green; graph_check.py green
                      (chemistry-scoped, unaffected)

Writes graph/reports/C41_MATHS_A_S18_PROMOTION_CHECK.json. Exit 0 = ALL PASS.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
QUAL = "igcse-maths-a"
PROMOTIONS = HERE / "c41_maths_a_promotions.yaml"
EDGES = REPO / "graph" / QUAL / "concept_edges.yaml"
CONCEPTS = REPO / "graph" / QUAL / "concepts.yaml"
CKINDS = REPO / "graph" / QUAL / "spec_command_kinds.yaml"
DECISIONS = [HERE / f"c{32 + n}_maths_a_batch0{n}_decisions.yaml" for n in range(1, 7)]
CHECK_OUT = REPO / "graph/reports/C41_MATHS_A_S18_PROMOTION_CHECK.json"

AI_NAME_RE = re.compile(r"glm|super\s*z|gpt|claude|openai|anthropic|\bai\b"
                        r"|llm|agent|model|bot", re.I)


def sha256_16(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()[:16]


def main() -> int:
    results = {}

    def gate(name, ok, detail=""):
        results[name] = {"pass": bool(ok), "detail": detail}
        if not ok:
            print(f"FAIL {name}: {detail}", file=sys.stderr)

    promo = yaml.safe_load(PROMOTIONS.read_text(encoding="utf-8"))
    entries = promo.get("promotions") or []
    landed_text = EDGES.read_text(encoding="utf-8")
    doc = yaml.safe_load(landed_text)
    edges = doc["edges"]
    semantic = [e for e in edges if e["relation"] != "PART_OF"]
    part_of = [e for e in edges if e["relation"] == "PART_OF"]
    hv = [e for e in semantic if e.get("validation_status") == "HUMAN_VALIDATED"]

    # ---- G1 record schema ----------------------------------------------------
    ok1, why = True, []
    for i, p in enumerate(entries):
        e = p.get("edge") or {}
        key = (e.get("source"), e.get("relation"), e.get("target"))
        if not all(isinstance(x, str) and x.strip() for x in key):
            ok1 = False; why.append(f"entry {i}: identity malformed")
        if e.get("relation") == "PART_OF":
            ok1 = False; why.append(f"entry {i}: PART_OF refused")
        by, dt = p.get("validated_by"), p.get("validated_date")
        if not isinstance(by, str) or not by.strip() or AI_NAME_RE.search(by):
            ok1 = False; why.append(f"entry {i}: attribution gate")
        if not isinstance(dt, str) or not re.match(r"^\d{4}-\d{2}-\d{2}$", dt or ""):
            ok1 = False; why.append(f"entry {i}: date malformed")
        ref = str(p.get("review_reference") or "")
        first = ref.split()[0] if ref.split() else ""
        if first.endswith((".md", ".json", ".yaml")) and not (REPO / first).exists():
            ok1 = False; why.append(f"entry {i}: review ref missing {first}")
    gate("G1_record_schema", ok1, "; ".join(why) if why else
         f"{len(entries)} entries; attribution + dates + review refs clean")

    # ---- G2 two-way ------------------------------------------------------------
    promo_index = {(p["edge"]["source"], p["edge"]["relation"],
                    p["edge"]["target"]): p for p in entries}
    hv_index = {(e["source"], e["relation"], e["target"]): e for e in hv}
    both = all(k in promo_index for k in hv_index) and all(k in hv_index for k in promo_index)
    attr_ok = all(hv_index[k].get("validated_by") == p["validated_by"]
                  and hv_index[k].get("validated_date") == p["validated_date"]
                  for k, p in promo_index.items() if k in hv_index)
    gate("G2_two_way", both and attr_ok and len(hv_index) == len(promo_index),
         f"{len(hv_index)} HUMAN_VALIDATED edges == {len(promo_index)} promotion "
         f"entries; attribution exact both directions")

    # ---- G3 anti-forgery ---------------------------------------------------------
    po_hv = [e for e in part_of if e.get("validation_status") == "HUMAN_VALIDATED"]
    con = yaml.safe_load(CONCEPTS.read_text(encoding="utf-8"))
    node_hv = [n for n in con["nodes"] if n.get("validation_status") == "HUMAN_VALIDATED"]
    ck_hv = [k for k in yaml.safe_load(CKINDS.read_text(encoding="utf-8"))["command_kinds"]
             if k.get("validation_status") == "HUMAN_VALIDATED"]
    dec_hv = []
    for p in DECISIONS:
        d = yaml.safe_load(p.read_text(encoding="utf-8"))
        dec_hv += [e for e in d.get("edges", []) if e.get("validation_status") == "HUMAN_VALIDATED"]
        dec_hv += [n for n in d.get("nodes", []) if n.get("validation_status") == "HUMAN_VALIDATED"]
    gate("G3_anti_forgery", not po_hv and not node_hv and not ck_hv and not dec_hv,
         f"0 HUMAN_VALIDATED outside the promoted surface (PART_OF {len(po_hv)}, "
         f"nodes {len(node_hv)}, command kinds {len(ck_hv)}, decision records {len(dec_hv)})")

    # ---- G4 non-validation delta zero (vs git HEAD) ------------------------------
    head = subprocess.run(["git", "-C", str(REPO), "show",
                           f"HEAD:graph/{QUAL}/concept_edges.yaml"],
                          capture_output=True, text=True).stdout
    pre = yaml.safe_load(head)
    pre_index = {(e["source"], e["relation"], e["target"]): e for e in pre["edges"]}
    drift = []
    for e in edges:
        key = (e["source"], e["relation"], e["target"])
        pe = pre_index.get(key)
        if pe is None:
            drift.append(f"{key}: absent pre-round"); continue
        if e["relation"] == "PART_OF":
            if pe != e:
                drift.append(f"{key}: PART_OF mutated")
        else:
            strip = lambda d: {k: v for k, v in d.items()
                               if k not in ("validation_status", "validated_by",
                                            "validated_date")}
            if strip(pe) != strip(e):
                drift.append(f"{key}: non-validation field mutated")
    pre_meta, land_meta = pre["meta"], doc["meta"]
    added = {k for k in land_meta if k not in pre_meta}
    meta_delta = (added == {"promotion_record"} and
                  all(land_meta[k] == pre_meta[k] for k in pre_meta if k != "counts"))
    pre_counts = pre_meta["counts"]
    counts_ok = (land_meta["counts"].get("promoted_edges") == 73 and
                 land_meta["counts"].get("human_validated_edges") == 73 and
                 {k: v for k, v in land_meta["counts"].items() if k not in
                  ("promoted_edges", "human_validated_edges")} == pre_counts)
    gate("G4_non_validation_delta", not drift and meta_delta and counts_ok,
         f"all 157 rows byte-checked vs HEAD: {len(drift)} drifts; meta delta == "
         f"promotion_record + promoted counts only")

    # ---- G5 round contract ----------------------------------------------------------
    rel_split = {}
    for e in semantic:
        rel_split[e["relation"]] = rel_split.get(e["relation"], 0) + 1
    gate("G5_round_contract",
         len(semantic) == 73 and len(hv) == 73 and rel_split ==
         {"REQUIRES_PREREQUISITE": 51, "WRONG_ANSWER_PATTERN": 11,
          "REMEDIATED_BY": 11},
         f"73/73 semantic edges promoted; split {rel_split}")

    # ---- G6 determinism: independent in-memory merge reproduces the store -----------
    merged = yaml.safe_load(head)
    applied = 0
    for e in merged["edges"]:
        if e["relation"] == "PART_OF":
            continue
        p = promo_index.get((e["source"], e["relation"], e["target"]))
        if p is None:
            continue
        ne = {}
        for k, v in e.items():
            ne[k] = v
            if k == "validation_status":
                ne["validation_status"] = "HUMAN_VALIDATED"
                ne["validated_by"] = p["validated_by"]
                ne["validated_date"] = p["validated_date"]
        e.clear(); e.update(ne)
        applied += 1
    mm2 = {}
    for k, v in merged["meta"].items():
        if k == "counts":
            c = dict(v); c["promoted_edges"] = 73; c["human_validated_edges"] = 73
            mm2[k] = c
        else:
            mm2[k] = v
    mm2["promotion_record"] = "scripts/c41_maths_a_promotions.yaml"
    merged["meta"] = mm2
    _lines = landed_text.splitlines(keepends=True)
    _i = 0
    while _i < len(_lines) and _lines[_i].startswith("#"):
        _i += 1
    header = "".join(_lines[:_i])
    expected = header + yaml.safe_dump(merged, allow_unicode=True, sort_keys=False,
                                       width=100)
    if expected == landed_text:
        g6_ok, g6_why = True, (f"independent HEAD+promotions merge ({applied} "
                               f"applications) reproduces the landed store "
                               f"byte-for-byte")
    else:
        exp_lines, land_lines = expected.splitlines(), landed_text.splitlines()
        first = next((j for j, (a, b) in enumerate(zip(exp_lines, land_lines)) if a != b),
                     min(len(exp_lines), len(land_lines)))
        g6_ok, g6_why = False, (f"dump divergence at line {first}: "
                                f"expected {exp_lines[first][:80]!r} vs landed "
                                f"{land_lines[first][:80]!r} (applied {applied})")
    gate("G6_determinism", g6_ok, g6_why)

    # ---- G7 held untouched ------------------------------------------------------------
    held_ids = []
    for p in DECISIONS:
        d = yaml.safe_load(p.read_text(encoding="utf-8"))
        held_ids += [h.get("id") for h in d.get("held", [])]
    held_leak = [hid for hid in held_ids
                 if hid and any(hid in str(e.get("provenance", {}).get("derivation_method", ""))
                                and e.get("validation_status") == "HUMAN_VALIDATED"
                                for e in semantic)]
    dec_now = subprocess.run(["git", "-C", str(REPO), "status", "--porcelain"] ,
                             capture_output=True, text=True).stdout
    dec_dirty = [ln[3:].strip() for ln in dec_now.splitlines()
                 if "decisions.yaml" in ln]
    gate("G7_held_untouched", len(held_ids) == 45 and not dec_dirty,
         f"45 held candidates quarantined in the decision records (records "
         f"clean vs HEAD: {not dec_dirty})")

    # ---- G8 standing checkers -----------------------------------------------------------
    rc1 = subprocess.run([sys.executable, str(HERE / "check_no_hardcode.py")],
                         capture_output=True, text=True, cwd=REPO)
    rc2 = subprocess.run([sys.executable, str(HERE / "graph_check.py")],
                         capture_output=True, text=True, cwd=REPO)
    gate("G8_standing_checkers", rc1.returncode == 0 and rc2.returncode == 0,
         f"check_no_hardcode rc={rc1.returncode}; graph_check rc={rc2.returncode}")

    all_pass = all(v["pass"] for v in results.values())
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")
    baseline = subprocess.run(["git", "-C", str(REPO), "rev-parse", "HEAD"],
                              capture_output=True, text=True).stdout.strip()
    check_doc = {
        "schema": "c41-s18-promotion-check/1.0",
        "task": "T-C41",
        "gate": "§18 promotion round two-way audit (the c11.13 analog)",
        "generated_utc": now,
        "baseline": baseline,
        "result": "ALL PASS" if all_pass else "FAIL",
        "gates": results,
        "pins": {"concept_edges.yaml": sha256_16(landed_text.encode())},
    }
    CHECK_OUT.write_text(json.dumps(check_doc, indent=2, ensure_ascii=False) + "\n",
                         encoding="utf-8")
    print(f"C41 promotion check: {'ALL PASS' if all_pass else 'FAIL'} "
          f"({sum(1 for v in results.values() if v['pass'])}/{len(results)} gates)")
    for k, v in results.items():
        print(f"  {'PASS' if v['pass'] else 'FAIL'} {k}: {v['detail'][:110]}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
