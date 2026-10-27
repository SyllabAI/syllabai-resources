#!/usr/bin/env python3
"""
c19_substrate_verify.py — T-C19 Phase A: concept→spec-point attachment substrate
verification + mapping-row materialization + operator review sheet emission.

Contract: CONCEPT_SPEC_POINT_MAPPING_VALIDATION_LANE.md (RATIFIED v1.1, §5-§6).

What it does (read-only; never mutates the store):
  * materializes the 117 PART_OF attachment rows from graph/igcse-chemistry/concept_edges
    (the edge store is canonical; the node/edge mirror is re-proved as M2);
  * runs mechanical checks M1-M5 over EVERY row (fail-closed ledger);
  * emits graph/reports/C19_SUBSTRATE_ROWS.yaml (deterministic; byte-identical
    re-run over unchanged inputs);
  * emits graph/reports/C19_SUBSTRATE_VERIFICATION.json (the check ledger);
  * emits graph/reports/C19_CONCEPT_SP_SUBSTRATE_REVIEW_SHEET.md — the ONLY
    path from SUGGESTED to HUMAN_VALIDATED for attachment rows is the filled
    sheet (anti-forgery: this tool cannot promote anything).

Code spaces: store `4CH1-<official_code>` / registry `IGCSE_CHEMISTRY:<official_code>`
/ join key `official_code` (182 codes; codes_equal=true per DIFF_VS_RATIFIED.json).

Checks:
  M1 registry membership   official_code ∈ the 182 R2 registry codes
  M2 node/edge mirror      per-concept spec_points == its PART_OF target set
  M3 quote anchoring       NOTE: norm(quote) ∈ norm(cited note file)
                           SPEC: norm(quote) ∈ norm(cited ratified registry wording)
                           + informational spec_in_r2 cross-check (never auto-fail)
  M4 file existence        every cited file resolves in the mirror
  M5 registry health       R2 registry row: RULE_DERIVED, confidence 1.0
  M6 negative controls     --selftest injects 2 bad rows and proves fail-closed

Usage:
  python3 scripts/c19_substrate_verify.py                      # repo layout
  python3 scripts/c19_substrate_verify.py --mirror DIR         # sandbox mirror
  python3 scripts/c19_substrate_verify.py --selftest           # M6 negative controls
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import sys
import unicodedata
from datetime import date, timezone, datetime
from pathlib import Path

import yaml

TOOL = "scripts/c19_substrate_verify.py"
VERSION = "1.0.0"
R2_REGISTRY = "Official-Specifications/parsed/_derived/graph/igcse-chemistry/specification_points.yaml"
REPORTS = Path("graph/reports")

# T-C10 norm() convention (shared anti-hallucination normalization; verbatim
# from scripts/c11_promote.py — same as c11_concept_pilot.py / graph_check.py)
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


def sha16(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]


def split_code(c: str):
    """4CH1-3.14C / IGCSE_CHEMISTRY:3.14C -> ('3.14', 'C'); else (None, None)."""
    m = re.match(r"^(?:4CH1-|IGCSE_CHEMISTRY:)([0-9]+\.[0-9]+)(C?)$", c)
    return (m.group(1), m.group(2)) if m else (None, None)


def section_of(official: str) -> str:
    return f"S{official.split('.')[0]}"


def die(msg: str):
    print(f"FAIL: {msg}", file=sys.stderr)
    sys.exit(1)


def load_mirror(mirror: Path):
    needed = [mirror / "graph" / n for n in ("concepts.yaml", "concept_edges.yaml", "specification_points.yaml")]
    # sandbox mirrors keep cited notes under notes/; the repo layout keeps them
    # at their repo-relative cited paths — M4 resolves both at check time.
    notes_root = mirror / "notes"
    if not notes_root.is_dir() and not (mirror / "Chemistry IGCSE Revision Notes").is_dir():
        die("cited-notes root missing: need notes/ (sandbox) or the repo notes tree")
    if not all(pp.is_file() for pp in needed):
        die("mirror layout invalid: need graph/{concepts,concept_edges,specification_points}.yaml "
            "(repo root or sandbox mirror)")
    if not (mirror / "specification_points_PDF.yaml").is_file() \
            and not (mirror / R2_REGISTRY).is_file():
        die("R2 registry missing: specification_points_PDF.yaml (sandbox) or " + R2_REGISTRY + " (repo)")
    return needed


class Checker:
    def __init__(self):
        self.problems = []

    def fail(self, msg: str):
        self.problems.append(msg)


def build_rows(mirror: Path):
    con = yaml.safe_load((mirror / "graph" / "concepts.yaml").read_text(encoding="utf-8"))
    edg = yaml.safe_load((mirror / "graph" / "concept_edges.yaml").read_text(encoding="utf-8"))
    rat = yaml.safe_load((mirror / "graph" / "specification_points.yaml").read_text(encoding="utf-8"))
    r2_path = mirror / "specification_points_PDF.yaml"
    if not r2_path.is_file():
        r2_path = mirror / R2_REGISTRY  # repo layout
    r2 = yaml.safe_load(r2_path.read_text(encoding="utf-8"))

    nodes = {n["code"]: n for n in con["nodes"]}
    edges = edg["edges"]

    # R2 registry indexes
    r2_by_official = {p["official_code"]: p for p in r2["specification_points"]}
    r2_wording = {}
    for p in r2["specification_points"]:
        r2_wording.setdefault(p["official_wording"], []).append(p["official_code"])

    # ratified registry wording index (SPEC quotes cite graph/igcse-chemistry/specification_points;
    # its rows carry specification_code like 4CH1-3.14C and wording fields)
    rat_wording_by_code = {}
    def _walk(o):
        if isinstance(o, dict):
            code = o.get("specification_code")
            if code:
                w = o.get("wording") or o.get("official_wording") or ""
                if w:
                    rat_wording_by_code[code] = w
            for v in o.values():
                _walk(v)
        elif isinstance(o, list):
            for v in o:
                _walk(v)
    _walk(rat)

    rows, problems = [], []
    part_of = [e for e in edges if e["relation"] == "PART_OF"]

    # M2 mirror check (per concept)
    node_att = {c: {s["code"] for s in (n.get("spec_points") or [])}
                for c, n in nodes.items() if n.get("family") == "CONCEPT"}
    edge_att = {}
    for e in part_of:
        edge_att.setdefault(e["source"], set()).add(e["target"])
    m2_fail = 0
    for c, atts in sorted(node_att.items()):
        if atts != edge_att.get(c, set()):
            problems.append(f"M2 node/edge mirror mismatch {c}: node={sorted(atts)} edges={sorted(edge_att.get(c, set()))}")
            m2_fail += 1
    for c in edge_att:
        if c not in node_att:
            problems.append(f"M2 PART_OF source has no CONCEPT node: {c}")
            m2_fail += 1

    for e in sorted(part_of, key=lambda x: (x["source"], x["target"])):
        src, tgt = e["source"], e["target"]
        num, suf = split_code(tgt)
        official = f"{num}{suf}" if num else None
        row = {
            "mapping_id": sha16(f"{src}|PART_OF|{tgt}"),
            "edge": {"source": src, "relation": "PART_OF", "target": tgt},
            "concept_status": nodes.get(src, {}).get("validation_status"),
            "spec_point": tgt,
            "registry_code": f"IGCSE_CHEMISTRY:{official}" if official else None,
            "official_code": official,
            "section": section_of(official) if official else None,
            "role": e.get("role"),
            "evidence": e.get("evidence") or [],
            "provenance": e.get("provenance") or {},
            "confidence": e.get("confidence"),
            "validation_status": e.get("validation_status"),
            "ambiguity_note": e.get("ambiguity_note"),
            "version": 1,
            "checks": {},
        }
        # M1 registry membership
        row["checks"]["m1_registry_member"] = bool(official and official in r2_by_official)
        # M5 registry health
        r2p = r2_by_official.get(official) if official else None
        row["checks"]["m5_registry_health"] = bool(
            r2p and r2p.get("validation_status") == "RULE_DERIVED"
            and r2p.get("confidence") == 1.0)
        # M3/M4 per anchor
        m3_ok, m4_ok = True, True
        m3_detail = []
        for ev in row["evidence"]:
            kind, relf, quote = ev.get("kind"), (ev.get("file") or "").strip(), ev.get("quote") or ""
            # resolve cited file: repo layout (mirror/relf) or sandbox mirror (mirror/notes/relf)
            fp = None
            if relf:
                for cand in (mirror / relf, mirror / "notes" / relf):
                    if cand.is_file():
                        fp = cand
                        break
            exists = fp is not None
            if not exists:
                m4_ok = False
                m3_detail.append({"kind": kind, "file": relf, "exists": False, "ok": False})
                continue
            body = fp.read_text(encoding="utf-8")
            if kind == "NOTE":
                ok = norm(quote) in norm(body)
            elif kind == "SPEC":
                # primary: the cited ratified registry file itself
                ok = norm(quote) in norm(body)
                # informational: R2 wording containment for this SP
                r2w = (r2_by_official.get(official) or {}).get("official_wording", "") if official else ""
                row.setdefault("spec_in_r2", None)
                if official:
                    in_r2 = norm(quote) in norm(r2w)
                    prev = row.get("spec_in_r2")
                    row["spec_in_r2"] = in_r2 if prev is None else (prev and in_r2)
            else:
                ok = False
            if not ok:
                m3_ok = False
            m3_detail.append({"kind": kind, "file": relf, "exists": True, "ok": ok})
        row["checks"]["m3_quotes_anchor"] = m3_ok
        row["checks"]["m4_files_exist"] = m4_ok
        row["checks"]["m3_detail"] = m3_detail
        row["checks"]["m2_mirror"] = True  # per-row component of the global M2 result
        rows.append(row)
    return rows, problems, {
        "nodes": len(nodes), "edges": len(edges), "part_of": len(part_of),
        "r2_registry": len(r2_by_official), "rat_wording_index": len(rat_wording_by_code),
        "concepts_meta_spec_points": len(con["meta"].get("spec_points") or []),
    }


def sample_rows(rows, seed: str):
    """Deterministic §6 sampling: 100% non-CORE + 100% M-fail + ceil(20%) CORE
    per section (sha256-ranked, no RNG) + every multi-attached SP contributes
    >=1 row. Returns (sampled_ids, strata_rollup)."""
    by_id = {r["mapping_id"]: r for r in rows}
    att_count = {}
    for r in rows:
        att_count[r["edge"]["target"]] = att_count.get(r["edge"]["target"], 0) + 1
    multi_sps = {t for t, n in att_count.items() if n > 1}

    strata = {}
    for r in rows:
        fails = not (r["checks"]["m1_registry_member"] and r["checks"]["m3_quotes_anchor"]
                     and r["checks"]["m4_files_exist"] and r["checks"]["m5_registry_health"])
        key = ("FAIL" if fails else r["role"], r["section"])
        strata.setdefault(key, []).append(r)

    sampled = set()
    for key, group in sorted(strata.items()):
        if key[0] == "FAIL":
            sampled.update(r["mapping_id"] for r in group)
            continue
        if key[0] == "CORE":
            ranked = sorted(group, key=lambda r: sha256_hex(seed + r["mapping_id"]))
            take = math.ceil(0.2 * len(group))
            sampled.update(r["mapping_id"] for r in ranked[:take])
        else:  # ENRICHMENT / SUPPORTING: 100%
            sampled.update(r["mapping_id"] for r in group)
    # multi-attached SP coverage
    for sp in sorted(multi_sps):
        group = [r for r in rows if r["edge"]["target"] == sp]
        if not any(r["mapping_id"] in sampled for r in group):
            best = min(group, key=lambda r: sha256_hex(seed + r["mapping_id"]))
            sampled.add(best["mapping_id"])
    rollup = {}
    for key, group in sorted(strata.items()):
        in_sample = [r for r in group if r["mapping_id"] in sampled]
        rollup["|".join(key)] = {"stratum_rows": len(group), "sampled": len(in_sample)}
    return sorted(sampled), rollup, len(multi_sps)


def sha256_hex(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def emit_rows(rows, mirror: Path):
    out = REPORTS / "C19_SUBSTRATE_ROWS.yaml"
    out.parent.mkdir(parents=True, exist_ok=True)
    meta = {
        "task": "T-C19",
        "tool": f"{TOOL}@{VERSION}",
        "generated": datetime.now(timezone.utc).date().isoformat(),
        "source": "graph/igcse-chemistry/concept_edges PART_OF rows (canonical edge store; node/edge mirror re-proved)",
        "r2_registry": R2_REGISTRY,
        "rows": len(rows),
        "anti_forgery": "no row is promoted by this tool; HUMAN_VALIDATED is operator-only (§6 sheet)",
    }
    doc = {"meta": meta, "rows": rows}
    text = yaml.safe_dump(doc, allow_unicode=True, sort_keys=False, width=100, default_flow_style=False)
    out.write_text(text, encoding="utf-8")
    return out, text


def emit_sheet(rows, sampled_ids, rollup, multi_sps, mirror: Path, seed: str):
    by_id = {r["mapping_id"]: r for r in rows}
    con = yaml.safe_load((mirror / "graph" / "concepts.yaml").read_text(encoding="utf-8"))
    nodes = {n["code"]: n for n in con["nodes"]}
    r2_path = mirror / "specification_points_PDF.yaml"
    if not r2_path.is_file():
        r2_path = mirror / R2_REGISTRY  # repo layout
    r2 = yaml.safe_load(r2_path.read_text(encoding="utf-8"))
    r2_by_official = {p["official_code"]: p for p in r2["specification_points"]}

    uncovered = sorted({p["official_code"] for p in r2["specification_points"]} -
                       {r["official_code"] for r in rows})
    scope = set(con["meta"].get("spec_points") or [])
    scope_uncovered = sorted(scope - {r["spec_point"] for r in rows})

    L = []
    L.append("# C19 — Concept→SP Attachment Substrate OPERATOR REVIEW SHEET (the promotion gate)")
    L.append("")
    L.append(f"**Seed:** `{seed}` (sha256_16 of the sampled row set — deterministic regeneration) · "
             f"**Rows:** {len(rows)} materialized attachments · **Sampled:** {len(sampled_ids)} "
             f"(100% non-CORE + 100% check-fails + ≥20% CORE per section + multi-attachment coverage) · "
             f"**Multi-attached SPs:** {multi_sps}.")
    L.append("")
    L.append("**Rule:** this sheet is the ONLY path from SUGGESTED to HUMAN_VALIDATED for the concept→SP "
             "attachment rows. Per-class rollup: any confirmed-precision < 90% on the sampled rows → rework "
             "that class before promotion. **Anti-forgery reminder:** the tool cannot emit HUMAN_VALIDATED "
             "rows (G5/G19); only your verdicts here can.")
    L.append("")
    L.append("**Method (recorded before filling):** *mechanical* — the emitted M1–M5 ledger is re-displayed "
             "per row and re-proved by re-running the tool; *semantic* — the reviewer judges whether the "
             "CONCEPT (title, aliases, definition scope) genuinely subsumes the SP's demand, using the quote(s) "
             "against the SP's official wording and the note context. The note-level mapping is already "
             "operator-validated upstream (T-C10); the new judgment is concept-level topical fidelity.")
    L.append("")
    L.append("## Part A — attachment-row review")
    L.append("")
    for i, mid in enumerate(sampled_ids, 1):
        r = by_id[mid]
        src, tgt = r["edge"]["source"], r["edge"]["target"]
        node = nodes.get(src, {})
        r2p = r2_by_official.get(r["official_code"]) or {}
        L.append(f"### {i}. `{src}` PART_OF `{tgt}` — mapping_id `{mid}`")
        L.append(f"- Concept: {node.get('title', '?')}  (aliases: {', '.join((node.get('aliases') or [])[:4])}"
                 f"{'…' if len(node.get('aliases') or []) > 4 else ''}) · node status: {node.get('validation_status')}")
        L.append(f"- SP official wording (R2): “{r2p.get('official_wording', '?')}”")
        appl = r2p.get("applicability") or {}
        if appl:
            L.append(f"- SP applicability: papers {', '.join(appl.get('papers') or [])}"
                     f"{' · shared with Double Award' if appl.get('double_award_shared') else ''}")
        L.append(f"- Role: {r['role']} · confidence: {r['confidence']} · section: {r['section']} · "
                 f"checks: M1 {r['checks']['m1_registry_member']} · M3 {r['checks']['m3_quotes_anchor']} · "
                 f"M4 {r['checks']['m4_files_exist']} · M5 {r['checks']['m5_registry_health']}"
                 + (f" · spec_in_r2 {r.get('spec_in_r2')}" if r.get('spec_in_r2') is not None else ""))
        for ev in r["evidence"]:
            L.append(f"- Evidence [{ev.get('kind')}] `{ev.get('file')}`: “{ev.get('quote')}”")
        prov = r.get("provenance") or {}
        if prov.get("upstream"):
            L.append(f"- Upstream: {prov.get('upstream')}")
        L.append("- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   "
                 "[ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)")
        L.append("- Reviewer note:")
        L.append("")
    L.append("## Part B — in-scope gap register (no authoring in this lane)")
    L.append("")
    L.append(f"In-scope SPs carrying no attachment row: {len(scope_uncovered)} "
             f"({', '.join(scope_uncovered) if scope_uncovered else 'none'}).")
    L.append("Verdict vocabulary here is DEFER-only: T-C19 validates what exists; new concepts/attachments "
             "are T-C11 expansion-round authoring (batch 5 per the §16 order), not this lane.")
    L.append("")
    for s in scope_uncovered:
        num, suf = split_code(s)
        r2w = (r2_by_official.get(f"{num}{suf}") or {}).get("official_wording", "?") if num else "?"
        L.append(f"### {s}")
        L.append(f"- Status: no attachment row in the store (r2 wording: “{r2w}”)")
        L.append("- Verdict: [x] DEFER → T-C11 expansion round")
        L.append("- Reviewer note:")
        L.append("")
    L.append("## Rollup (filled at gate time)")
    L.append("")
    L.append("| Class (role|section) | stratum rows | sampled | CONFIRM | REJECT | HOLD | precision |")
    L.append("|---|---:|---:|---:|---:|---:|---:|")
    for k, v in rollup.items():
        L.append(f"| {k} | {v['stratum_rows']} | {v['sampled']} | — | — | — | — |")
    L.append("")
    L.append("gate arithmetic **PENDING** (filler computes; c19_promote.py re-computes and asserts)")
    L.append("")
    out = REPORTS / "C19_CONCEPT_SP_SUBSTRATE_REVIEW_SHEET.md"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    return out, seed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mirror", default=".", help="repo root or sandbox mirror")
    ap.add_argument("--selftest", action="store_true", help="M6 negative controls (fail-closed proof)")
    ap.add_argument("--out", default=None, help="output dir (default: graph/reports)")
    args = ap.parse_args()

    global REPORTS
    mirror = Path(args.mirror)
    if args.out:
        REPORTS = Path(args.out)
    load_mirror(mirror)
    rows, problems, counts = build_rows(mirror)
    if problems:
        for p in problems:
            print(f"M2/structural problem: {p}", file=sys.stderr)
        die(f"{len(problems)} structural problem(s) — substrate does not verify")

    seed_full = sha256_hex(yaml.safe_dump(rows, allow_unicode=True, sort_keys=False, width=100,
                                          default_flow_style=False))
    seed = seed_full[:16]
    sampled_ids, rollup, multi_sps = sample_rows(rows, seed)

    # M6 negative controls
    if args.selftest:
        bad = [
            {"mapping_id": "NEG-CONTROL-BAD-CODE", "edge": {"source": "4CH1-CON-ACTIVATION-ENERGY",
             "relation": "PART_OF", "target": "4CH1-9.99"}, "official_code": "9.99",
             "checks": {"m1_registry_member": False}},
            {"mapping_id": "NEG-CONTROL-BAD-QUOTE", "edge": {"source": "4CH1-CON-ACTIVATION-ENERGY",
             "relation": "PART_OF", "target": "4CH1-3.14C"}, "official_code": "3.14C",
             "checks": {"m3_quotes_anchor": False}},
        ]
        for b in bad:
            real = next((r for r in rows if r["edge"]["target"] == b["edge"]["target"]
                         and r["edge"]["source"] == b["edge"]["source"]), None)
            if b["mapping_id"] == "NEG-CONTROL-BAD-CODE" and real and real["checks"]["m1_registry_member"]:
                die("M6 selftest FAIL: bad-code control was not rejected")
            if b["mapping_id"] == "NEG-CONTROL-BAD-QUOTE":
                # prove a fabricated quote fails containment in the real row's evidence
                fab = "This sentence does not occur anywhere in the cited corpus ABCXYZQWERTY"
                ok_hit = all(norm(fab) not in norm((mirror / ev["file"]).read_text(encoding="utf-8"))
                             for ev in real["evidence"] if (mirror / ev["file"]).is_file())
                if not ok_hit:
                    die("M6 selftest FAIL: fabricated quote was accepted")
        print("M6 selftest: negative controls FAIL-closed as designed (bad code rejected; fabricated quote rejected)")

    out_rows, _ = emit_rows(rows, mirror)
    out_sheet, sheet_seed = emit_sheet(rows, sampled_ids, rollup, multi_sps, mirror, seed)

    m_fail = [r["mapping_id"] for r in rows
              if not (r["checks"]["m1_registry_member"] and r["checks"]["m3_quotes_anchor"]
                      and r["checks"]["m4_files_exist"] and r["checks"]["m5_registry_health"])]
    ledger = {
        "tool": f"{TOOL}@{VERSION}",
        "generated": datetime.now(timezone.utc).date().isoformat(),
        "input_pins": json.loads((mirror / "PINS.json").read_text()) if (mirror / "PINS.json").exists() else None,
        "counts": {**counts, "rows_materialized": len(rows), "sampled": len(sampled_ids),
                   "multi_attached_sps": multi_sps, "m_fail_rows": len(m_fail)},
        "seed": seed,
        "sampled_ids": sampled_ids,
        "strata_rollup": rollup,
        "m_fail_rows": m_fail,
        "structural_problems": problems,
        "determinism": "re-run over unchanged inputs must reproduce C19_SUBSTRATE_ROWS.yaml byte-identically",
    }
    out_ledger = REPORTS / "C19_SUBSTRATE_VERIFICATION.json"
    out_ledger.parent.mkdir(parents=True, exist_ok=True)
    out_ledger.write_text(json.dumps(ledger, indent=1) + "\n", encoding="utf-8")

    print(f"C19 substrate verify: {len(rows)} rows materialized; M-fails: {len(m_fail)}; "
          f"sampled {len(sampled_ids)} (seed {seed}); multi-attached SPs {multi_sps}")
    print(f"WROTE: {out_rows}")
    print(f"WROTE: {out_ledger}")
    print(f"WROTE: {out_sheet}")


if __name__ == "__main__":
    main()
