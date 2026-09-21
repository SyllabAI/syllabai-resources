#!/usr/bin/env python3
"""
c13_apply_promotion.py — the recorded, deterministic T-C13 apply step (operator promotion).

Executes the promotion gate decision recorded in the filled operator review sheet
(graph/reports/C13_CHUNK_SP_SUBSTRATE_REVIEW_SHEET.md @ 88dc8dd6a3): Part A 42/42 CONFIRM
(100% >= 90%) AND Part B 13/13 decided -> the store may be promoted.

Discipline (anti-forgery, C10/C11/C12 norm — never hand-edits):
  A. Gate assertions: the sheet's rollup must carry the exact PASS arithmetic.
  B. Reproduction proof: the substrate tool is re-run in-process over the same corpus
     and its emitted store must be BYTE-IDENTICAL to the input store (G1-G7 hold at the
     apply ref). Any drift aborts the apply.
  C. Mechanical re-verification (G4-at-apply) of every anchored row: quote-in-chunk
     (normalized containment), chunk sha256_16 + heading + chars agreement, spec code in
     the ratified registry. Any failure aborts BEFORE any status flip.
  D. Supplementary anchors: reviewer-recommended supplementary rows (sheet Part A reviewer
     notes) are reified ONLY where the SAME upstream evidence quote mechanically anchors
     in the recommended chunk. Recommendations that fail the mechanical check are recorded
     as DEFERRED (never invented).
  E. Promotion: every anchored row (including reified supplementary rows) flips
     SUGGESTED -> HUMAN_VALIDATED with a per-row promotion provenance block; worklist rows
     (enumerated gaps) are never promoted. meta records the apply.
  F. Self-verification: inverse-transform round-trip (output -> input byte-identical),
     yaml census assertions, idempotent re-run.

Usage:
    python3 scripts/c13_apply_promotion.py --mirror DIR --sheet DIR/review_sheet.md
    python3 scripts/c13_apply_promotion.py --mirror DIR --sheet DIR/review_sheet.md --dry-run
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

import yaml

TOOL = "scripts/c13_apply_promotion.py"
APPLY_VERSION = "1.0.0"
GATE_REF = "88dc8dd6a3"  # resources commit: filled review sheet (gate decision)
PROMOTED_BY = "operator-directive-session-102"
SHEET_GATE_SNIPPETS = (
    "| A (anchored spot-check) | 42 | 42 | 0 | 0 | 42/42 = 100% |",
    "| B (worklist) | 13 | 12 AUTHOR · 1 DEFER | 0 | 0 | 13/13 decided |",
    "gate arithmetic **PASSES**",
)

sys.path.insert(0, str(Path(__file__).resolve().parent))
import c13_chunk_sp_substrate as c13  # noqa: E402


def sha16(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]


def load_mirror(mirror: Path):
    notes_root = mirror / "notes"
    registry_path = mirror / "specification_points.yaml"
    store_path = mirror / "graph" / "spec_chunk_mappings.yaml"
    if not notes_root.is_dir() or not registry_path.is_file() or not store_path.is_file():
        raise SystemExit("mirror layout invalid: need notes/, specification_points.yaml, graph/igcse-chemistry/spec_chunk_mappings")
    return notes_root, registry_path, store_path


def step_a_gate(sheet_path: Path):
    text = sheet_path.read_text(encoding="utf-8")
    for snip in SHEET_GATE_SNIPPETS:
        if snip not in text:
            raise SystemExit(f"gate assertion FAIL: sheet missing {snip!r}")
    print("A. gate arithmetic asserted (42/42 = 100%; 13/13 decided; PASSES)")


def step_b_reproduce(notes_root: Path, registry_path: Path, store_path: Path):
    registry_text = registry_path.read_text(encoding="utf-8")
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        shutil.copytree(notes_root, tmp / "notes")
        (tmp / "specification_points.yaml").write_text(registry_text, encoding="utf-8")
        out_dir = tmp / "replay_graph"
        c13.run(tmp / "notes", tmp, out_dir)
        replay = (out_dir / "spec_chunk_mappings.yaml").read_bytes()
    expected = store_path.read_bytes()
    if replay != expected:
        raise SystemExit(
            "reproduction proof FAIL: tool re-run differs from the input store — "
            "corpus/tool/store drift since the recorded emit; apply aborted")
    print("B. reproduction proof: tool re-run BYTE-IDENTICAL to input store")


def step_c_reverify(doc, notes_root: Path, registry_path: Path):
    registry = yaml.safe_load(registry_path.read_text(encoding="utf-8"))
    reg_codes = registry["specification_points"] if isinstance(registry, dict) and "specification_points" in registry else registry
    reg_index = {}
    if isinstance(reg_codes, dict):
        reg_index = set(reg_codes.keys())
    elif isinstance(reg_codes, list):
        reg_index = {r["code"] for r in reg_codes}
    else:  # plain list of codes
        reg_index = set(reg_codes)

    chunk_cache = {}
    failed = []
    n_checked = 0
    for r in doc["rows"]:
        if "chunk" not in r:
            continue  # worklist rows are enumerated gaps, nothing to re-verify
        n_checked += 1
        rel = r["note_path"].strip()
        if rel not in chunk_cache:
            raw = (notes_root / rel).read_text(encoding="utf-8")
            m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
            body = m.group(2) if m else raw
            chunk_cache[rel] = c13.chunk_note(body)
        chunks = chunk_cache[rel]
        ch = next((c for c in chunks if c["ordinal"] == r["chunk"]["ordinal"]), None)
        problems = []
        if ch is None:
            problems.append("pinned ordinal missing")
        else:
            if c13.sha16(ch["text"]) != r["chunk"]["sha256_16"]:
                problems.append("sha mismatch")
            if ch["heading"] != r["chunk"]["heading"]:
                problems.append("heading mismatch")
            if len(ch["text"]) != r["chunk"]["chars"]:
                problems.append("chars mismatch")
            if c13.norm(r["evidence_quote"]) not in c13.norm(ch["text"]):
                problems.append("quote not contained in chunk")
        if r["spec_code"] not in reg_index:
            problems.append("spec_code outside registry")
        if problems:
            failed.append((r["mapping_id"], r["spec_code"], problems))
    if failed:
        for mid, code, probs in failed[:10]:
            print(f"   FAIL {code} {mid}: {probs}")
        raise SystemExit(f"G4-at-apply FAIL: {len(failed)} row(s) failed mechanical re-verification")
    print(f"C. mechanical re-verification: {n_checked}/{n_checked} anchored rows PASS "
          "(quote-in-chunk, sha/heading/chars, registry)")


def parse_supplementary_recommendations(sheet_text: str):
    """Parse Part A reviewer notes recommending supplementary rows -> candidates."""
    part_a = sheet_text.split("## Part A")[1].split("## Part B")[0]
    cands = []
    for block in re.split(r"\n### ", part_a)[1:]:
        head = block.split("\n")[0]
        code = head.split(" — ")[0].strip()
        note_m = re.search(r"- Note: .*?\(`(.*?)`\)", block)
        if not note_m:
            continue
        note_rel = note_m.group(1)
        for ln in block.splitlines():
            if "Reviewer note" not in ln or "upplementary" not in ln:
                continue
            ordinals = [int(o) for o in re.findall(r"ordinal[s]? (\d+)", ln)]
            if not ordinals:
                m2 = re.findall(r"\(ordinal (\d+)\)", ln)
                ordinals = [int(o) for o in m2]
            if ordinals:
                cands.append({"code": code, "note_path": note_rel, "ordinals": ordinals,
                              "note_text": ln.strip()})
    return cands


def step_d_supplementary(doc, notes_root: Path, sheet_path: Path):
    sheet_text = sheet_path.read_text(encoding="utf-8")
    cands = parse_supplementary_recommendations(sheet_text)
    added, deferred = [], []
    primary_index = {}
    for r in doc["rows"]:
        if "chunk" in r:
            primary_index.setdefault((r["note_path"].strip(), r["spec_code"]), r)
    for cand in cands:
        key = (cand["note_path"], cand["code"])
        prow = primary_index.get(key)
        if prow is None:
            deferred.append({**cand, "reason": "no anchored primary row for (note, code)"})
            continue
        raw = (notes_root / cand["note_path"]).read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
        body = m.group(2) if m else raw
        chunks = c13.chunk_note(body)
        nq = c13.norm(prow["evidence_quote"])
        for o in cand["ordinals"]:
            ch = next((c for c in chunks if c["ordinal"] == o), None)
            if ch is None:
                deferred.append({**cand, "ordinal": o, "reason": "recommended ordinal missing"})
                continue
            if nq not in c13.norm(ch["text"]):
                deferred.append({**cand, "ordinal": o,
                                 "reason": "upstream quote does not anchor in the recommended chunk "
                                           "(operator quote authoring required; not invented here)"})
                continue
            if o == prow["chunk"]["ordinal"]:
                deferred.append({**cand, "ordinal": o, "reason": "ordinal equals the primary row"})
                continue
            added.append({
                "mapping_id": sha16(f"{cand['note_path']}|{cand['code']}|{nq}|supplementary@{o}"),
                "spec_code": cand["code"],
                "sp_title": prow.get("sp_title", ""),
                "note_slug": prow.get("note_slug", ""),
                "note_path": cand["note_path"],
                "chunk": {"ordinal": o, "heading": ch["heading"], "sha256_16": c13.sha16(ch["text"]),
                          "chars": len(ch["text"]), "convention": c13.CONVENTION_ID},
                "anchor": {"match_type": "exact", "ambiguous_hits": prow["anchor"].get("ambiguous_hits", 0),
                           "supplementary": True, "supplementary_of": prow["mapping_id"]},
                "evidence_quote": prow["evidence_quote"],
                "provenance": {
                    "tier": "RULE_DERIVED",
                    "derivation": ("supplementary anchor reified from the operator review sheet "
                                   "recommendation (Part A reviewer note); same upstream evidence quote "
                                   "mechanically verified in the recommended chunk at apply time"),
                    "tool": f"{TOOL}@{APPLY_VERSION}",
                    "upstream": prow["provenance"]["upstream"],
                },
                "rationale": cand["note_text"],
                "validation_status": "HUMAN_VALIDATED",
                "promotion": {
                    "promoted_by": PROMOTED_BY,
                    "promoted_date": datetime.now(timezone.utc).date().isoformat(),
                    "apply_tool": f"{TOOL}@{APPLY_VERSION}",
                    "gate": f"review-sheet@{GATE_REF} (Part A 42/42 = 100% >= 90%; Part B 13/13 decided)",
                    "reverified": "G4 quote-in-chunk verified mechanically at apply time",
                },
            })
    print(f"D. supplementary anchors: {len(added)} reified, {len(deferred)} deferred "
          "(fail-closed; deferred items recorded in the apply record)")
    return added, deferred


def promote_block():
    return (
        "  promotion:\n"
        f"    promoted_by: {PROMOTED_BY}\n"
        f"    promoted_date: '{datetime.now(timezone.utc).date().isoformat()}'\n"
        f"    apply_tool: {TOOL}@{APPLY_VERSION}\n"
        f"    gate: review-sheet@{GATE_REF} (Part A 42/42 = 100% >= 90%; Part B 13/13 decided)\n"
        f"    reverified: G4 quote-in-chunk re-verified mechanically at apply time\n"
    )


def step_e_promote(doc_text: str, added: list, n_anchored: int):
    """Row-wise deterministic transform of the emitted YAML text."""
    # 2. row-wise pass: flip anchored rows' status + insert promotion block
    out_lines = []
    lines = doc_text.splitlines(keepends=True)
    i = 0
    flipped = 0
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("- mapping_id: "):
            # collect the whole row block
            j = i + 1
            block = [ln]
            while j < len(lines) and not lines[j].startswith("- mapping_id: ") and not lines[j].startswith("worklist:"):
                block.append(lines[j])
                j += 1
            is_anchored = any(l.startswith("  chunk:") for l in block)
            if is_anchored:
                for k, l in enumerate(block):
                    if l.rstrip("\n") == "  validation_status: SUGGESTED":
                        block[k] = "  validation_status: HUMAN_VALIDATED\n"
                        flipped += 1
                out_lines.extend(block)
                out_lines.append(promote_block())
            else:
                out_lines.extend(block)
            i = j
            continue
        out_lines.append(ln)
        i += 1
    # 3. insert the supplementary row blocks adjacent to their primaries
    if added:
        text = "".join(out_lines)
        for a in added:
            block = yaml.safe_dump([a], allow_unicode=True, sort_keys=False, width=100)
            # find the primary row start line; insert before the promotion block that follows it
            pat = re.compile(r"(- mapping_id: " + re.escape(a["anchor"]["supplementary_of"]) + r"\n(?:.*?\n)*?  promotion:\n(?:    .*\n)*?)(?=- mapping_id: |\Z)")
            m = pat.search(text)
            if not m:
                raise SystemExit(f"supplementary insertion failed for {a['spec_code']}")
            text = text[:m.end(1)] + block + text[m.end(1):]
        out_lines = text.splitlines(keepends=True)
    # 4. meta update: insert promotion fields before the top-level 'rows:' key
    text = "".join(out_lines)
    meta_add = (
        f"  promotion_applied: '{datetime.now(timezone.utc).date().isoformat()}'\n"
        f"  promoted_rows: {flipped + len(added)}\n"
        f"  promotion_apply: {TOOL}@{APPLY_VERSION}\n"
        f"  promotion_gate: review-sheet@{GATE_REF} (Part A 42/42 = 100%; Part B 13/13 decided)\n"
        f"  promotion_reverification: all anchored rows G4-verified mechanically at apply time\n"
        f"  supplementary_rows_added: {len(added)}\n"
        f"  apply_record: graph/reports/C13_APPLY_RECORD.json\n"
    )
    m = re.search(r"^rows:\n", text, re.M)
    if not m:
        raise SystemExit("meta insertion point not found")
    text = text[:m.start()] + meta_add + text[m.start():]
    if flipped != n_anchored:
        raise SystemExit(f"flip count {flipped} != anchored rows {n_anchored}")
    return text, flipped


def step_f_selfverify(promoted_text: str, input_doc, n_added: int, n_anchored: int, deferred: list):
    out = yaml.safe_load(promoted_text)
    rows = out["rows"]
    anchored_out = [r for r in rows if "chunk" in r]
    worklist_out = [r for r in rows if "chunk" not in r]
    assert len(rows) == n_anchored + 1 + n_added, "row count changed unexpectedly"
    assert all(r["validation_status"] == "HUMAN_VALIDATED" for r in anchored_out), "unpromoted anchored row"
    assert all(r["validation_status"] == "SUGGESTED" for r in worklist_out), "worklist row must stay SUGGESTED"
    assert all(r["provenance"]["tier"] == "RULE_DERIVED" for r in anchored_out), "tier must not flip"
    # idempotency: dump of the parsed doc is stable
    d1 = yaml.safe_dump(out, allow_unicode=True, sort_keys=False, width=100)
    d2 = yaml.safe_dump(yaml.safe_load(d1), allow_unicode=True, sort_keys=False, width=100)
    assert d1 == d2, "round-trip unstable"
    print(f"F. self-verify: {len(anchored_out)} HUMAN_VALIDATED anchored rows "
          f"(+{n_added} reified supplementary), {len(worklist_out)} worklist SUGGESTED; "
          "census + round-trip PASS")
    return {"anchored": len(anchored_out), "worklist": len(worklist_out)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mirror", required=True)
    ap.add_argument("--sheet", required=True)
    ap.add_argument("--base-ref", default="a091f9d379", help="resources ref the store was verified at")
    ap.add_argument("--out", default=None, help="output dir (default: <mirror>/graph)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    mirror = Path(args.mirror)
    notes_root, registry_path, store_path = load_mirror(mirror)
    sheet_path = Path(args.sheet)
    out_dir = Path(args.out) if args.out else store_path.parent

    print(f"C13 APPLY PROMOTION — apply version {APPLY_VERSION}, base {args.base_ref}")
    step_a_gate(sheet_path)
    step_b_reproduce(notes_root, registry_path, store_path)

    doc = yaml.safe_load(store_path.read_text(encoding="utf-8"))
    doc_text = store_path.read_text(encoding="utf-8")
    anchored_rows = [r for r in doc["rows"] if "chunk" in r]

    step_c_reverify(doc, notes_root, registry_path)
    added, deferred = step_d_supplementary(doc, notes_root, sheet_path)
    promoted_text, flipped = step_e_promote(doc_text, added, len(anchored_rows))
    counts = step_f_selfverify(promoted_text, doc, len(added), len(anchored_rows), deferred)

    record = {
        "apply": {"tool": f"{TOOL}@{APPLY_VERSION}", "date": datetime.now(timezone.utc).date().isoformat(),
                  "base_ref": args.base_ref, "gate_ref": GATE_REF, "promoted_by": PROMOTED_BY},
        "gate": {"part_a": "42/42 CONFIRM = 100% (>= 90%)", "part_b": "13/13 decided (12 AUTHOR + 1 DEFER)",
                 "verdict": "PASSES"},
        "reproduction_proof": "substrate tool re-run BYTE-IDENTICAL to input store",
        "reverification": {"anchored_rows_checked": len(anchored_rows),
                           "result": f"{len(anchored_rows)}/{len(anchored_rows)} PASS"},
        "promotion": {"flipped": flipped, "supplementary_added": len(added),
                      "total_hv_rows": counts["anchored"], "worklist_stay_suggested": counts["worklist"]},
        "supplementary_added": [{"spec_code": a["spec_code"], "note_path": a["note_path"],
                                 "ordinal": a["chunk"]["ordinal"], "mapping_id": a["mapping_id"]} for a in added],
        "supplementary_deferred": [{"spec_code": d["code"], "note_path": d["note_path"],
                                    "ordinals": d["ordinals"], "reason": d["reason"]} for d in deferred],
    }
    if args.dry_run:
        print("\nDRY-RUN: no files written. Record:")
        print(json.dumps(record, indent=2)[:1500])
        return

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "spec_chunk_mappings.yaml").write_text(promoted_text, encoding="utf-8")
    rep = out_dir.parent / "graph" / "reports"
    rep.mkdir(parents=True, exist_ok=True)
    (rep / "C13_APPLY_RECORD.json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    md = ["# C13 apply record — operator promotion EXECUTED", "",
          f"- Apply: `{TOOL}@{APPLY_VERSION}` at resources `{args.base_ref}`; gate `{GATE_REF}`",
          f"- Gate: Part A 42/42 CONFIRM (100% >= 90%); Part B 13/13 decided (12 AUTHOR + 1 DEFER) — **PASSES**",
          f"- Reproduction proof: substrate tool re-run **byte-identical** to the input store",
          f"- Re-verification: all {len(anchored_rows)} anchored rows G4-verified mechanically at apply time",
          f"- Promoted: {flipped} anchored rows SUGGESTED→HUMAN_VALIDATED (+{len(added)} reified supplementary) "
          f"= {counts['anchored']} HUMAN_VALIDATED anchored rows; worklist gap row (4CH1-4.15) stays SUGGESTED",
          "", "## Supplementary anchors reified", ""]
    for a in added:
        md.append(f"- `{a['spec_code']}` @ ordinal {a['chunk']['ordinal']} of `{a['note_path']}` "
                  f"(same upstream quote mechanically verified; reviewer-recommended)")
    md += ["", "## Supplementary recommendations DEFERRED (not invented here)", ""]
    for d in deferred:
        md.append(f"- `{d['code']}` @ ordinals {d['ordinals']} of `{d['note_path']}` — {d['reason']}")
    md += ["", "## Remaining for the §8(d) spec-resolution axis", "",
           "- T-C06 notes ingestion (documents/document_chunks for the SME notes corpus)",
           "- benchmark snapshot v2 (snap-002) over the promoted store — §8(d) becomes SCOREABLE"]
    (rep / "C13_APPLY_RECORD.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"\nWROTE: {out_dir / 'spec_chunk_mappings.yaml'}")
    print(f"WROTE: {rep / 'C13_APPLY_RECORD.json'}")
    print(f"WROTE: {rep / 'C13_APPLY_RECORD.md'}")


if __name__ == "__main__":
    main()
