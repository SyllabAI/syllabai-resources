#!/usr/bin/env python3
"""c42_r5_promotion_apply.py — the gated merge point for the T-C42 R5 §18
substrate apply (operator gate 3): SUGGESTED -> HUMAN_VALIDATED over the
maths-a chunk substrate, exactly the rows the R21 re-gate sheet authorizes.

The C41 apply convention (c41_maths_a_promotion_apply.py, G13 convention)
fused with the C13 apply discipline (c13_apply_promotion.py steps A-F),
instantiated for the c40-chunk-convention-1 store so the landed c40 generator
and its records stay byte-untouched:

  A. gate-2 evidence asserts: the R21 fill record/check/verdicts carry the
     exact PASS arithmetic (457/3/4, per-class 92.5%/100%/100% >= 90%,
     Part B 82/82 decided, mechanical 464/464);
  B. reproduction proof: the c40 substrate tool re-runs twice (G7) and its
     emission is BYTE-IDENTICAL to the input store — any corpus/tool/store
     drift aborts before any flip;
  C. mechanical re-verification (G4-at-apply) of EVERY promoted row against
     a fresh re-chunking: quote-in-chunk under the shared norm(), chunk
     sha256_16/heading/chars agreement, spec_code inside the ratified 188;
  D. promotion-set integrity: the entries cover EXACTLY anchored 839 -
     REJECT 3 - HOLD 4 = 832 (the R21 sheet's authorized surface: its 457
     sampled CONFIRM rows + its 375 gate-passed unsampled rows); REJECT,
     HOLD and worklist rows are categorically excluded — any overlap fails;
  E. apply: flips ONLY validation_status (+ a per-row promotion block, the
     C13 row shape); meta gains the promotion fields; the header's status
     line is re-dated. A structural diff over all 921 rows asserts the
     non-validation delta is exactly zero;
  F. self-verification: census + round-trip stability; re-run fails closed
     (the store already carries promotion_record).

Validated_by is 'operator' everywhere (the c11/C41 anti-forgery precedent);
AI-name patterns fail closed. The human operator's directive is recorded in
the promotions file and both apply records.

Usage:
    python3 scripts/c42_r5_promotion_apply.py --dry-run
    python3 scripts/c42_r5_promotion_apply.py
"""
from __future__ import annotations

import argparse
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
STORE = REPO / "graph" / QUAL / "spec_chunk_mappings.yaml"
PROMOTIONS = HERE / "c42_r5_promotions.yaml"
FILL_MD = REPO / "graph/reports/C42_R21_MATHS_A_REGATE_FILL_RECORD.md"
FILL_JSON = REPO / "graph/reports/C42_R21_MATHS_A_REGATE_FILL_RECORD.json"
REGATE_CHECK = REPO / "graph/reports/C42_R21_REGATE_CHECK.json"
VERDICTS = HERE / "c42_r21_review_verdicts.yaml"
REC_JSON = REPO / "graph/reports/C42_R5_APPLY_RECORD.json"
REC_MD = REPO / "graph/reports/C42_R5_APPLY_RECORD.md"

TOOL = "scripts/c42_r5_promotion_apply.py"
APPLY_VERSION = "1.0.0"
PROMOTED_DATE = "2026-10-04"
DIRECTIVE = ("Fire r5 — 2026-10-04, discord (gateway trace "
             "ea5e3ae2488d59498dcc801859715415)")
GATE_LABEL = ("c42-r21-regate@b17e3712 (Part A 457 CONFIRM / 3 REJECT / 4 HOLD, "
              "per-class 92.5% / 100% / 100% >= 90%; Part B 82/82 decided; "
              "mechanical 464/464)")
AI_PAT = re.compile(r"glm|super\s*z|gpt|claude|openai|anthropic|\bai\b|llm|agent|model|bot", re.I)

FILL_SNIPPETS = (
    "| A total | 464 | 457 | 3 | 4 | 98.5% |",
    "| A stratum exact (score == 1.0) | 94 | 87 | 3 | 4 | 92.5% |",
    "| A stratum partial (score < 1.0) | 238 | 238 | 0 | 0 | 100.0% |",
    "| A stratum none (score n/a) | 132 | 132 | 0 | 0 | 100.0% |",
    "| B (worklist re-decided) | 82 | 82 DEFER | | | 82/82 decided |",
    "**Gate outcome: PASS",
    "**464/464 PASS**.",
)

HEADER_LINE_OLD = ("# All rows SUGGESTED / RULE_DERIVED; HUMAN_VALIDATED is "
                   "operator-only via the C40 review sheet.\n")
HEADER_LINE_NEW = ("# T-C42 R5 §18 apply (2026-10-04, operator gate 3): 832 anchored "
                   "rows HUMAN_VALIDATED (839 - 3 REJECT - 4 H3 HOLD); the worklist "
                   "rows stay SUGGESTED; provenance tiers unchanged (RULE_DERIVED).\n")


def die(msg: str) -> None:
    print(f"FAIL-CLOSED: {msg}", file=sys.stderr)
    sys.exit(1)


def sha16(data) -> str:
    b = data.encode("utf-8") if isinstance(data, str) else data
    return hashlib.sha256(b).hexdigest()[:16]


def baseline() -> str:
    return subprocess.run(["git", "-C", str(REPO), "rev-parse", "HEAD"],
                          capture_output=True, text=True).stdout.strip()


def promotion_block() -> dict:
    return {
        "promoted_by": "operator",
        "promoted_date": PROMOTED_DATE,
        "apply_tool": f"{TOOL}@{APPLY_VERSION}",
        "gate": GATE_LABEL,
        "reverified": ("G4 quote-in-chunk + chunk identity verified mechanically "
                       "at apply time"),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    # ---- A. gate-2 evidence -------------------------------------------------
    for p in (STORE, PROMOTIONS, FILL_MD, FILL_JSON, REGATE_CHECK, VERDICTS):
        if not p.exists():
            die(f"required artifact missing: {p.relative_to(REPO)}")
    fill_text = FILL_MD.read_text(encoding="utf-8")
    for snip in FILL_SNIPPETS:
        if snip not in fill_text:
            die(f"gate-2 assert FAIL: fill record missing {snip!r}")
    check = json.loads(REGATE_CHECK.read_text(encoding="utf-8"))
    if check.get("all_pass") is not True or check.get("passed") != 13:
        die("C42_R21_REGATE_CHECK.json is not all_pass 13/13")
    fill = json.loads(FILL_JSON.read_text(encoding="utf-8"))
    if fill.get("gate", {}).get("outcome") != "PASS":
        die("R21 fill gate outcome is not PASS")

    ver = yaml.safe_load(VERDICTS.read_text(encoding="utf-8"))
    verdicts = ver["verdicts"]
    vconf = {m for m, p in verdicts.items() if p["verdict"] == "CONFIRM"}
    vrej = {m for m, p in verdicts.items() if p["verdict"] == "REJECT"}
    vhold = {m for m, p in verdicts.items() if p["verdict"] == "HOLD"}
    g = ver["gate"]
    pa, bs, pb = g["part_a"], g["part_a"]["by_stratum"], g["part_b"]
    if (pa["total"] != {"rows": 464, "confirm": 457, "reject": 3, "hold": 4,
                        "precision": 0.9849}
            or bs["exact"]["precision"] != 0.9255
            or bs["partial"]["precision"] != 1.0 or bs["none"]["precision"] != 1.0
            or pb.get("rows") != 82 or pb.get("decided") is not True
            or pb.get("defer") != 82
            or not pa["classes_pass"]):
        die("R21 verdict-record gate arithmetic does not carry the exact PASS shape")
    if g["rule"] != ("Part A precision >= 90% per class AND every Part B row "
                     "decided AND mechanical layer clean"):
        die("R21 gate rule string drifted")

    # ---- store + promotions --------------------------------------------------
    store_text = STORE.read_text(encoding="utf-8")
    doc = yaml.safe_load(store_text)
    if "promotion_record" in doc["meta"]:
        die("meta already carries promotion_record (re-run guard) — the apply "
            "is idempotent-by-refusal; revert the store first to re-fire")
    lines = store_text.splitlines(keepends=True)
    i = 0
    while i < len(lines) and lines[i].startswith("#"):
        i += 1
    header = "".join(lines[:i])
    if header.count("\n") != 3 or header.splitlines()[2] != HEADER_LINE_OLD.rstrip("\n"):
        die("store header shape unexpected — the status line is not where it is pinned")
    rows = {r["mapping_id"]: r for r in doc["rows"]}
    if len(rows) != len(doc["rows"]):
        die("duplicate mapping_id in the store")
    anchored = {mid: r for mid, r in rows.items()
                if r.get("chunk") and r.get("spec_code")}
    worklist = set(rows) - set(anchored)
    if len(anchored) != 839 or len(rows) != 921 or doc["meta"]["rows_anchored"] != 839:
        die("store census drifted")
    if any(r.get("validation_status") != "SUGGESTED" for r in doc["rows"]):
        die("store is not uniformly SUGGESTED")

    promo = yaml.safe_load(PROMOTIONS.read_text(encoding="utf-8"))
    entries = promo.get("promotions") or []
    if not entries:
        die("promotions file carries zero entries")
    seen = set()
    for n, e in enumerate(entries):
        where = f"promotion[{n}]"
        row = e.get("row") or {}
        mid = row.get("mapping_id")
        if not isinstance(mid, str) or not mid:
            die(f"{where}: exact row identity required (mapping_id missing)")
        if mid in seen:
            die(f"{where}: duplicate promotion for {mid}")
        seen.add(mid)
        by, dt = e.get("validated_by"), e.get("validated_date")
        if by != "operator":
            die(f"{where}: validated_by must be 'operator' (the c11/C41 "
                f"anti-forgery precedent), got {by!r}")
        if AI_PAT.search(by or ""):
            die(f"{where}: attribution gate fails closed")
        if not isinstance(dt, str) or not re.match(r"^\d{4}-\d{2}-\d{2}$", dt):
            die(f"{where}: validated_date must be YYYY-MM-DD, got {dt!r}")
        ref = e.get("review_reference") or ""
        if not ref or not (REPO / ref.split()[0]).exists():
            die(f"{where}: review_reference artifact not found: {ref!r}")
        if "verdict" in e:
            if e["verdict"] != "CONFIRM":
                die(f"{where}: only CONFIRM verdicts may ride the apply "
                    f"(got {e['verdict']!r})")
            if mid not in verdicts:
                die(f"{where}: {mid} claims an R21 verdict but is not in the "
                    f"R21 verdict record")
            if verdicts[mid]["verdict"] != "CONFIRM":
                die(f"{where}: {mid} is not CONFIRM in the R21 verdict record")
            if e.get("verdict_source") != verdicts[mid]["source"]:
                die(f"{where}: {mid} verdict_source drift vs the R21 record")
    # ---- D. round contract ---------------------------------------------------
    promote_set = set(anchored) - vrej - vhold
    if seen != promote_set:
        missing = sorted(promote_set - seen)[:5]
        extra = sorted(seen - promote_set)[:5]
        die(f"round contract violated: entries {len(seen)} vs authorized surface "
            f"{len(promote_set)}; missing {missing}...; extra {extra}... — the R5 "
            f"round is the whole authorized surface (832); partial rounds are a "
            f"different gate")
    if seen & (vrej | vhold | worklist):
        die("promotion set overlaps REJECT/HOLD/worklist")
    if not vconf <= seen:
        die("R21 CONFIRM rows missing from the promotion set")
    n_sampled = sum(1 for e in entries if "verdict" in e)
    if n_sampled != 457:
        die(f"sampled-CONFIRM entries {n_sampled} != 457")

    # ---- B. reproduction proof ----------------------------------------------
    sys.path.insert(0, str(HERE))
    import c40_maths_a_chunk_sp_substrate as c40
    reg = yaml.safe_load((HERE / "graph_paths.yaml").read_text(encoding="utf-8"))
    if len(reg["quals"][QUAL]["stores"]) != 9:
        die("maths-a registry is not the 9-store K2 exit shape")
    d1, d2 = c40.construct(), c40.construct()
    dump_a = yaml.safe_dump(d1, allow_unicode=True, sort_keys=False, width=100)
    dump_b = yaml.safe_dump(d2, allow_unicode=True, sort_keys=False, width=100)
    if dump_a != dump_b:
        die("G7: substrate construction is not deterministic")
    if store_text != header + "\n" + dump_a:
        die("reproduction proof FAIL: c40 tool re-run differs from the input "
            "store — corpus/tool/store drift; apply aborted")

    # ---- C. mechanical re-verification of every promoted row -----------------
    r = c40.R()
    _, notes = c40.load_corpus(r)
    by_note, _ = c40.span_chunks(notes)
    registry = c40.load_registry()
    r.close()
    if len(registry) != 188:
        die(f"registry is not the ratified 188 (got {len(registry)})")
    failed = []
    for mid in sorted(promote_set):
        row = anchored[mid]
        chs = by_note.get(row["note_path"])
        ch = next((c for c in (chs or [])
                   if c["ordinal"] == row["chunk"]["ordinal"]), None)
        probs = []
        if ch is None:
            probs.append("pinned ordinal missing in fresh re-chunk")
        else:
            if c40.sha16(ch["text"]) != row["chunk"]["sha256_16"]:
                probs.append("sha mismatch")
            if ch["heading"] != row["chunk"]["heading"]:
                probs.append("heading mismatch")
            if len(ch["text"]) != row["chunk"]["chars"]:
                probs.append("chars mismatch")
            if c40.norm(row["evidence_quote"]) not in c40.norm(ch["text"]):
                probs.append("quote not contained in chunk")
        if row["spec_code"] not in registry:
            probs.append("spec_code outside the ratified 188")
        if probs:
            failed.append((mid, probs))
    if failed:
        for mid, probs in failed[:10]:
            print(f"  FAIL {mid}: {probs}", file=sys.stderr)
        die(f"G4-at-apply FAIL: {len(failed)} row(s) failed — no status flipped")

    # ---- E. apply (ONLY validation fields move) -------------------------------
    pre_text = store_text
    pre_doc = yaml.safe_load(pre_text)
    new_doc = yaml.safe_load(pre_text)  # fresh parse; rows are dicts
    flipped = 0
    for row in new_doc["rows"]:
        mid = row["mapping_id"]
        if mid not in promote_set:
            continue
        if "promotion" in row or row.get("validation_status") != "SUGGESTED":
            die(f"row {mid} pre-poisoned — refusing")
        row["validation_status"] = "HUMAN_VALIDATED"
        row["promotion"] = promotion_block()
        flipped += 1
    if flipped != len(promote_set):
        die(f"flipped {flipped} != {len(promote_set)}")

    meta = new_doc["meta"]
    meta["promotion_applied"] = PROMOTED_DATE
    meta["promoted_rows"] = flipped
    meta["promotion_record"] = "scripts/c42_r5_promotions.yaml"
    meta["promotion_apply"] = f"{TOOL}@{APPLY_VERSION}"
    meta["promotion_gate"] = GATE_LABEL
    meta["promotion_directive"] = DIRECTIVE
    meta["promotion_reverification"] = ("all 832 promoted rows G4-verified "
                                        "mechanically at apply time")
    meta["apply_record"] = "graph/reports/C42_R5_APPLY_RECORD.json"

    new_header = header.replace(HEADER_LINE_OLD, HEADER_LINE_NEW)
    if new_header == header:
        die("header status-line amendment did not apply")
    new_text = new_header + "\n" + yaml.safe_dump(
        new_doc, allow_unicode=True, sort_keys=False, width=100)

    # structural diff: the non-validation delta is EXACTLY zero
    if len(pre_doc["rows"]) != len(new_doc["rows"]):
        die("row count drift")
    for oe, ne in zip(pre_doc["rows"], new_doc["rows"]):
        mid = ne["mapping_id"]
        if mid in promote_set:
            if {k: v for k, v in oe.items() if k != "validation_status"} != \
               {k: v for k, v in ne.items()
                if k not in ("validation_status", "promotion")}:
                die(f"promoted row carries a non-validation delta: {mid}")
            if ne["promotion"] != promotion_block():
                die(f"promotion block drift on {mid}")
        else:
            if oe != ne:
                die(f"unpromoted row mutated: {mid}")
    om, nm = pre_doc["meta"], new_doc["meta"]
    promo_meta_keys = {"promotion_applied", "promoted_rows", "promotion_record",
                       "promotion_apply", "promotion_gate", "promotion_directive",
                       "promotion_reverification", "apply_record"}
    if {k: v for k, v in om.items()} != {k: v for k, v in nm.items()
                                         if k not in promo_meta_keys}:
        die("meta carries a non-promotion delta")
    if set(nm) - set(om) != promo_meta_keys:
        die("meta promotion-field set drifted")

    # ---- F. self-verify --------------------------------------------------------
    out = yaml.safe_load(new_text)
    orows = out["rows"]
    hv = [x for x in orows if x.get("validation_status") == "HUMAN_VALIDATED"]
    sug_anch = [x for x in orows if x.get("chunk") and x.get("spec_code")
                and x.get("validation_status") == "SUGGESTED"]
    wl = [x for x in orows if not (x.get("chunk") and x.get("spec_code"))]
    if len(hv) != 832 or len(sug_anch) != 7 or len(wl) != 82 or len(orows) != 921:
        die(f"post-apply census wrong: hv={len(hv)} sug_anch={len(sug_anch)} "
            f"wl={len(wl)} rows={len(orows)}")
    if {x["mapping_id"] for x in sug_anch} != (vrej | vhold):
        die("the SUGGESTED anchored residue is not exactly REJECT|HOLD")
    if any(x["provenance"]["tier"] != "RULE_DERIVED" for x in orows):
        die("a provenance tier moved")
    d1t = yaml.safe_dump(out, allow_unicode=True, sort_keys=False, width=100)
    d2t = yaml.safe_dump(yaml.safe_load(d1t), allow_unicode=True,
                         sort_keys=False, width=100)
    if d1t != d2t:
        die("round-trip unstable")

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")
    rec = {
        "schema": "c42-r5-apply-record/1.0",
        "task": "T-C42",
        "stage": "r5-s18-substrate-apply",
        "generated_utc": now,
        "baseline": baseline(),
        "operator_directive": DIRECTIVE,
        "gate": ("C42 rework scope §4 R5 / §7 gate 3 — the §18 substrate apply "
                 "(SUGGESTED -> HUMAN_VALIDATED, exact row identities, "
                 "structural-diff zero on the non-validation delta, two-way audit)"),
        "gate2_evidence": {
            "fill_record": "graph/reports/C42_R21_MATHS_A_REGATE_FILL_RECORD.md",
            "fill_record_sha256_16": sha16(FILL_MD.read_bytes()),
            "regate_check": "graph/reports/C42_R21_REGATE_CHECK.json",
            "regate_check_baseline": check.get("baseline"),
            "regate_check_head": check.get("head"),
            "verdicts": "scripts/c42_r21_review_verdicts.yaml",
            "gate_outcome": "PASS (Part A 457/3/4, exact 92.5% / partial 100% / "
                            "none 100% >= 90%; Part B 82/82 DEFER; mechanical 464/464)",
        },
        "promotion_record": {
            "path": "scripts/c42_r5_promotions.yaml",
            "sha256_16": sha16(PROMOTIONS.read_bytes()),
            "tool": "scripts/c42_r5_promote.py",
            "entries": len(entries),
            "sampled_confirm": n_sampled,
            "gate_passed_unsampled": len(entries) - n_sampled,
        },
        "tool": f"{TOOL}@{APPLY_VERSION}",
        "round": {
            "surface": "the R21-authorized anchored surface of the maths-a chunk "
                       "substrate",
            "store_rows": 921,
            "anchored": 839,
            "promoted": flipped,
            "reject_stay_suggested": sorted(vrej),
            "hold_stay_suggested": sorted(vhold),
            "worklist_stay_suggested": len(worklist),
            "store_sha256_16_pre": sha16(pre_text.encode("utf-8")),
            "store_sha256_16_post": sha16(new_text.encode("utf-8")),
        },
        "reproduction_proof": ("c40 substrate tool re-run twice (G7 deterministic) "
                               "and BYTE-IDENTICAL to the input store "
                               "(header + canonical dump)"),
        "reverification": {
            "rows_checked": flipped,
            "checks": "quote-in-chunk under the shared norm(), chunk sha256_16/"
                      "heading/chars vs a fresh re-chunking, spec_code inside the "
                      "ratified 188",
            "result": f"{flipped}/{flipped} PASS",
        },
        "structural_diff": {
            "rows": 921,
            "rows_changed": flipped,
            "changed_fields": ["validation_status", "promotion (added block)"],
            "unpromoted_rows_mutated": 0,
            "meta_delta": sorted(promo_meta_keys),
            "header_delta": "status line re-dated (line 3), lines 1-2 verbatim",
        },
        "anti_forgery": {
            "validated_by": "operator (the c11/C41 precedent; AI-name patterns "
                            "fail closed in promote and apply)",
            "non_validation_delta": "asserted zero (structural diff over all 921 rows)",
            "provenance_tiers_untouched": True,
            "worklist_never_promoted": True,
            "reject_hold_never_promoted": True,
        },
        "reject_inventory_returns_to_operator": [
            {k: verdicts[m].get(k) for k in ("verdict", "source", "root", "note",
                                             "spec_code", "note_path",
                                             "chunk_ordinal", "heading")}
            for m in sorted(vrej)],
        "hold_inventory_h3_fail_closed": [
            {k: verdicts[m].get(k) for k in ("verdict", "source",
                                             "convention_branch", "note",
                                             "spec_code", "note_path",
                                             "chunk_ordinal", "heading")}
            for m in sorted(vhold)],
        "post_check": "scripts/c42_r5_promotion_check.py",
        "not_done": [
            "no REJECT-row promotion (3 stay SUGGESTED — the fresh defect "
            "inventory returns to the operator, scope §7)",
            "no HOLD-row promotion (4 H3 fail-closed rows ride only with "
            "explicit per-row operator sign-off, none given with the directive)",
            "no worklist promotion (23 unresolved-span incl. the loop's 3 "
            "DEMOVEs + 59 uncovered-SP stay SUGGESTED, recorded never forced)",
            "no provenance-tier or code-attribution change",
            "no Lane C / chemistry / resolution / corpus writes",
        ],
    }

    if args.dry_run:
        print(f"c42_r5_promotion_apply --dry-run: ALL GATES GREEN — "
              f"{flipped} rows would flip HUMAN_VALIDATED; no files written")
        return 0

    STORE.write_text(new_text, encoding="utf-8")

    stores = {p.name: sha16((STORE.parent / p.name).read_bytes())
              for p in sorted(STORE.parent.glob("*.yaml"))}
    rec["store_pins_post"] = stores
    REC_JSON.write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8")
    rej_lines = "\n".join(
        f"- `{verdicts[m]['spec_code']}` — {verdicts[m]['note_path']} ord "
        f"{verdicts[m]['chunk_ordinal']} ({verdicts[m]['heading']})"
        for m in sorted(vrej))
    hold_lines = "\n".join(
        f"- `{verdicts[m]['spec_code']}` — {verdicts[m]['note_path']} ord "
        f"{verdicts[m]['chunk_ordinal']} ({verdicts[m]['heading']})"
        for m in sorted(vhold))
    md = f"""# C42 R5 — §18 Substrate Apply — igcse-maths-a (operator gate 3)

**Generated:** {now}  |  **Baseline:** `{rec['baseline']}`
**Operator directive:** "{DIRECTIVE.split(' — ')[0]}" ({DIRECTIVE.split(' — ')[1]}).
The directive is the operator command the C42 scope's gate 3 requires; the
gate-2 evidence is the R21 re-gate (Part A 457/3/4, per-class 92.5% / 100% /
100% ≥ 90%; Part B 82/82 decided; mechanical 464/464; X1–X13 all 13/13 PASS).

## What this is

The §18 substrate apply of `C42_IGCSE_MATHS_A_K2B_REWORK_SCOPE.md` (§4 R5,
§7 gate 3), executed under the C41 exact-identity mechanics fused with the
C13 apply discipline. **{flipped} anchored rows** (the R21-authorized surface:
839 anchored − 3 REJECT − 4 HOLD = 832 = {n_sampled} sampled CONFIRM +
{len(entries) - n_sampled} gate-passed unsampled) now carry
`validation_status: HUMAN_VALIDATED` + a per-row `promotion:` block in
`graph/igcse-maths-a/spec_chunk_mappings.yaml`. Every promoted row was
mechanically re-verified at apply time against a fresh re-chunking
(quote-in-chunk under the shared norm(), chunk sha256_16/heading/chars,
registry membership). The 3 REJECT rows, the 4 H3 HOLD rows and the 82
worklist rows stay SUGGESTED — recorded, never forced. Provenance tiers
are unchanged (RULE_DERIVED); no code attribution moved.

## Mechanics

- `scripts/c42_r5_promote.py` (the only writer of
  `scripts/c42_r5_promotions.yaml`): exact row identities only
  (mapping_id + spec_code + note_path + ordinal + heading + chunk sha256_16);
  every evidence quote byte-verified under the c40 norm before anything was
  written; attribution gate (AI self-attribution fails closed); idempotent;
  atomic write.
- `{TOOL}@{APPLY_VERSION}` (the gated merge point): gate-2 evidence asserts,
  reproduction proof (c40 tool re-run byte-identical to the input store),
  G4-at-apply re-verification of all {flipped} rows, round contract
  ({flipped}/{flipped}), and a rewrite of ONLY the validation fields — a
  structural diff over all 921 rows asserts the non-validation delta is
  exactly zero; meta gains the promotion fields; the header status line is
  re-dated (lines 1–2 verbatim).
- `scripts/c42_r5_promotion_check.py` (the c11.13 analog): two-way
  store ⟷ promotions-record audit against the real repo files, with the
  structural re-proof against the pinned baseline blob.

## Anti-forgery posture

- The promotions record carries `validated_by: operator` (the c11 precedent);
  AI-name patterns fail closed in both tools.
- The store carries HUMAN_VALIDATED only on exact row identities with a
  matching promotion entry and exact attribution (the promotion check
  enforces this continuously).
- Zero silent promotion, zero silent repair: the loop's discipline holds at
  the apply — the REJECT/HOLD/worklist surfaces are recorded verbatim below.

## Remaining defect inventory (returns to the operator — scope §7)

REJECT rows (stay SUGGESTED):
{rej_lines}

HOLD rows (c42-heading-only-convention-1 H3 fail-closed — ride a future
round only with explicit per-row operator sign-off; stay SUGGESTED):
{hold_lines}

## Pins

| Artifact | sha256_16 |
|---|---|
| `spec_chunk_mappings.yaml` (pre-apply) | `{rec['round']['store_sha256_16_pre']}` |
| `spec_chunk_mappings.yaml` (post-apply) | `{rec['round']['store_sha256_16_post']}` |
| `c42_r5_promotions.yaml` | `{rec['promotion_record']['sha256_16']}` |
| `specification_points.yaml` (untouched) | `{stores['specification_points.yaml']}` |
| `concepts.yaml` (untouched) | `{stores['concepts.yaml']}` |
| `concept_edges.yaml` (untouched) | `{stores['concept_edges.yaml']}` |
"""
    REC_MD.write_text(md + "\n", encoding="utf-8")

    print(f"c42_r5_promotion_apply: APPLIED — {flipped} rows HUMAN_VALIDATED "
          f"(3 REJECT + 4 HOLD + {len(worklist)} worklist stay SUGGESTED)")
    print(f"  store sha256_16 {rec['round']['store_sha256_16_post']} "
          f"(pre {rec['round']['store_sha256_16_pre']})")
    print(f"  WROTE {REC_JSON.relative_to(REPO)}")
    print(f"  WROTE {REC_MD.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
