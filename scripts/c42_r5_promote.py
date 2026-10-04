#!/usr/bin/env python3
"""c42_r5_promote.py — the only writer of scripts/c42_r5_promotions.yaml (the
operator-side §18 apply record for the T-C42 R5 substrate promotion).

The C41 promote convention instantiated for the maths-a chunk substrate
(c13-chunk-convention-1 family):

  * operates on EXACT row identity only — mapping_id + spec_code + note_path
    + chunk_ordinal + heading + chunk_sha256_16, all six fields from the
    landed store; no wildcard, no stratum-level, no code-level promotion;
  * the promotion set is DERIVED, never asserted: anchored rows
    (chunk present AND spec_code resolved) minus the R21 re-gate's REJECT
    rows minus its HOLD rows = 839 - 3 - 4 = 832. Worklist rows (the 23
    unresolved-span + 59 uncovered-SP) and the 3 REJECT / 4 HOLD anchored
    rows are categorically excluded (recorded, never forced);
  * every entry's evidence quote is byte-verified under the c40 norm
    (quote-in-chunk) against a FRESH re-chunking of the corpus before
    anything is written — same discipline as c41_maths_a_promote.py;
  * validated_by: operator (the c11/C41 precedent); AI-name patterns fail
    closed; the human operator's directive is recorded in meta;
  * idempotent: deterministic content, byte-identical re-runs; atomic write.

Usage:
    python3 scripts/c42_r5_promote.py            # build/verify, write
    python3 scripts/c42_r5_promote.py --check    # verify only, no write
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
QUAL = "igcse-maths-a"
STORE = REPO / "graph" / QUAL / "spec_chunk_mappings.yaml"
PROMOTIONS = HERE / "c42_r5_promotions.yaml"
FILL_MD = REPO / "graph/reports/C42_R21_MATHS_A_REGATE_FILL_RECORD.md"
FILL_JSON = REPO / "graph/reports/C42_R21_MATHS_A_REGATE_FILL_RECORD.json"
REGATE_CHECK = REPO / "graph/reports/C42_R21_REGATE_CHECK.json"
VERDICTS = HERE / "c42_r21_review_verdicts.yaml"

TOOL = "scripts/c42_r5_promote.py"
DIRECTIVE = ("Fire r5 — 2026-10-04, discord (gateway trace "
             "ea5e3ae2488d59498dcc801859715415)")
REVIEW_REF = "graph/reports/C42_R21_MATHS_A_REGATE_FILL_RECORD.md"
PROMOTED_DATE = "2026-10-04"
AI_PAT = re.compile(r"glm|super\s*z|gpt|claude|openai|anthropic|\bai\b|llm|agent|model|bot", re.I)

sys.path.insert(0, str(HERE))
import c40_maths_a_chunk_sp_substrate as c40  # noqa: E402


def die(msg: str) -> None:
    print(f"FAIL-CLOSED: {msg}", file=sys.stderr)
    sys.exit(1)


def sha16(data) -> str:
    b = data.encode("utf-8") if isinstance(data, str) else data
    return hashlib.sha256(b).hexdigest()[:16]


def baseline() -> str:
    return subprocess.run(["git", "-C", str(REPO), "rev-parse", "HEAD"],
                          capture_output=True, text=True).stdout.strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="verify preconditions + rebuild in memory; no write")
    args = ap.parse_args()

    # ---- gate-2 evidence preconditions --------------------------------------
    for p in (STORE, FILL_MD, FILL_JSON, REGATE_CHECK, VERDICTS):
        if not p.exists():
            die(f"required artifact missing: {p.relative_to(REPO)}")
    check = json.loads(REGATE_CHECK.read_text(encoding="utf-8"))
    if check.get("all_pass") is not True or check.get("passed") != 13:
        die("C42_R21_REGATE_CHECK.json is not all_pass 13/13 — gate 2 evidence missing")
    fill = json.loads(FILL_JSON.read_text(encoding="utf-8"))
    if fill.get("gate", {}).get("outcome") != "PASS":
        die("R21 fill record gate outcome is not PASS")

    ver = yaml.safe_load(VERDICTS.read_text(encoding="utf-8"))
    verdicts = ver["verdicts"]
    vconf = {m for m, p in verdicts.items() if p["verdict"] == "CONFIRM"}
    vrej = {m for m, p in verdicts.items() if p["verdict"] == "REJECT"}
    vhold = {m for m, p in verdicts.items() if p["verdict"] == "HOLD"}
    if (len(vconf), len(vrej), len(vhold)) != (457, 3, 4):
        die(f"R21 verdict split is not 457/3/4: {(len(vconf), len(vrej), len(vhold))}")

    # ---- store census --------------------------------------------------------
    text = STORE.read_text(encoding="utf-8")
    doc = yaml.safe_load(text)
    rows = {r["mapping_id"]: r for r in doc["rows"]}
    if len(rows) != len(doc["rows"]):
        die("duplicate mapping_id in the store")
    anchored = {mid: r for mid, r in rows.items()
                if r.get("chunk") and r.get("spec_code")}
    worklist = set(rows) - set(anchored)
    if (len(anchored) != 839 or len(rows) != 921
            or doc["meta"]["rows_anchored"] != 839):
        die(f"store census drifted: rows={len(rows)} anchored={len(anchored)} "
            f"(meta says {doc['meta']['rows_anchored']})")
    if any(rows[m].get("validation_status") != "SUGGESTED" for m in rows):
        die("store is not uniformly SUGGESTED — the apply has already run? "
            "(promote operates on the pre-apply store)")
    if not (vrej | vhold) <= set(anchored):
        die("R21 REJECT/HOLD ids outside the anchored surface")
    if (vrej | vhold) & worklist:
        die("R21 REJECT/HOLD ids overlap the worklist class")

    promote_ids = set(anchored) - vrej - vhold
    if len(promote_ids) != 832:
        die(f"promotion arithmetic is not 839 - 3 - 4 = 832 (got {len(promote_ids)})")
    if not vconf <= promote_ids:
        die("R21 CONFIRM ids outside the promotion set")
    if promote_ids & (vrej | vhold | worklist):
        die("promotion set overlaps REJECT/HOLD/worklist")

    # ---- fresh re-chunk once; verify EVERY promoted row mechanically --------
    r = c40.R()
    _, notes = c40.load_corpus(r)
    by_note, _ = c40.span_chunks(notes)
    r.close()
    failed = []
    for mid in sorted(promote_ids):
        row = anchored[mid]
        chs = by_note.get(row["note_path"])
        if not chs:
            failed.append((mid, "note missing from fresh re-chunk"))
            continue
        ch = next((c for c in chs if c["ordinal"] == row["chunk"]["ordinal"]), None)
        probs = []
        if ch is None:
            probs.append("pinned ordinal missing")
        else:
            if c40.sha16(ch["text"]) != row["chunk"]["sha256_16"]:
                probs.append("sha mismatch")
            if ch["heading"] != row["chunk"]["heading"]:
                probs.append("heading mismatch")
            if len(ch["text"]) != row["chunk"]["chars"]:
                probs.append("chars mismatch")
            if c40.norm(row["evidence_quote"]) not in c40.norm(ch["text"]):
                probs.append("quote not contained in chunk")
        if probs:
            failed.append((mid, probs))
    if failed:
        for mid, probs in failed[:10]:
            print(f"  FAIL {mid}: {probs}", file=sys.stderr)
        die(f"mechanical pre-verification failed for {len(failed)} row(s) — nothing written")

    # ---- entries (store row order — deterministic) --------------------------
    entries = []
    for row in doc["rows"]:
        mid = row["mapping_id"]
        if mid not in promote_ids:
            continue
        e = {"row": {
            "mapping_id": mid,
            "spec_code": row["spec_code"],
            "note_path": row["note_path"],
            "chunk_ordinal": row["chunk"]["ordinal"],
            "heading": row["chunk"]["heading"],
            "chunk_sha256_16": row["chunk"]["sha256_16"],
        }}
        if mid in verdicts:  # sampled at R21
            e["verdict"] = verdicts[mid]["verdict"]
            e["verdict_source"] = verdicts[mid]["source"]
        e["validated_by"] = "operator"
        e["validated_date"] = PROMOTED_DATE
        e["review_reference"] = REVIEW_REF
        if AI_PAT.search(e["validated_by"]):
            die(f"attribution gate: {e['validated_by']!r} fails closed")
        entries.append(e)

    n_sampled = sum(1 for e in entries if "verdict" in e)
    meta = {
        "task": "T-C42",
        "stage": "r5-s18-substrate-apply",
        "contract": ("C42_IGCSE_MATHS_A_K2B_REWORK_SCOPE.md §4 R5 + §7 gate 3 — "
                     "SUGGESTED -> HUMAN_VALIDATED via the promotions-file convention "
                     "(the C41 mechanics: exact row identities only, structural diff "
                     "asserts the non-validation delta is zero, two-way audit)"),
        "operator_directive": DIRECTIVE,
        "gate2_evidence": ("graph/reports/C42_R21_MATHS_A_REGATE_FILL_RECORD.md + "
                           "graph/reports/C42_R21_REGATE_CHECK.json (X1-X13 all 13/13 "
                           "PASS) + scripts/c42_r21_review_verdicts.yaml"),
        "round_contract": ("promote = anchored 839 - REJECT 3 - HOLD 4 = 832 "
                           f"({n_sampled} sampled CONFIRM + {len(entries) - n_sampled} "
                           "gate-passed unsampled, every row mechanically re-verified "
                           "at promote and again at apply); the 3 REJECT rows, the 4 "
                           "H3 HOLD rows (per-row operator sign-off owed, none given "
                           "with the directive) and the 82 worklist rows stay SUGGESTED"),
        "baseline": baseline(),
        "tool": TOOL,
        "generated_date": PROMOTED_DATE,
    }
    promo_doc = {"meta": meta, "promotions": entries}

    body = yaml.safe_dump(promo_doc, allow_unicode=True, sort_keys=False, width=100)
    header = (
        "# T-C42 R5 promotion record — operator §18 substrate apply authorizations\n"
        "# (igcse-maths-a 4MA1 chunk substrate). Written ONLY by scripts/c42_r5_promote.py;\n"
        "# hand-editing is forbidden. Exact row identities only (the C41 promote convention).\n"
    )
    new_text = header + body

    if args.check:
        print(f"c42_r5_promote --check: {len(entries)} entries OK "
              f"({n_sampled} sampled CONFIRM + {len(entries) - n_sampled} unsampled); "
              f"all 832 mechanically pre-verified; no write")
        return 0
    if PROMOTIONS.exists():
        old = PROMOTIONS.read_text(encoding="utf-8")
        if old == new_text:
            print(f"c42_r5_promote: promotions file already current "
                  f"({len(entries)} entries) — idempotent no-op")
            return 0
        die("promotions file exists with different content — refusing to overwrite "
            "(the apply record pins its sha; investigate before re-firing)")
    tmp = PROMOTIONS.with_suffix(".yaml.tmp")
    tmp.write_text(new_text, encoding="utf-8")
    tmp.replace(PROMOTIONS)
    print(f"c42_r5_promote: WROTE {PROMOTIONS.relative_to(REPO)} — "
          f"{len(entries)} entries ({n_sampled} sampled CONFIRM + "
          f"{len(entries) - n_sampled} gate-passed unsampled), all pre-verified")
    print(f"  promotions sha256_16 {sha16(new_text)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
