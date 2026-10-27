#!/usr/bin/env python3
"""T-SME-11 — build spec_point_resolution.json for the 10 new lanes.

Initial pass = tiered auto-join resolution, honest by construction:
  - T1_verbatim / T2_near / T3_section_anchored and unflagged S1_name_match
    from spec_point_map.json -> resolved (tier kept, method records the
    auto-join lineage; no operator verdicts have been authored yet)
  - flagged mappings (S2_name_ambiguous, T4_fuzzy) -> unresolved with the
    flag as reason (no-guess discipline: ambiguous joins stay uncoded)
  - unmapped entries -> unresolved with the mapper's reason

Fail-closed: every official_id/code pair is checked against the qual's
canonical registry before a resolution is written; any mismatch hard-fails.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

BASE = Path("/home/z/my-project/download/syllabai-resources")
EQ = BASE / "SME-ExamQuestion"
PARSED = BASE / "Official-Specifications" / "parsed"
NOW = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

LANES = {
    "igcse-english-language-a-16-paper-1-non-fiction-texts-and-transactional-writing": "igcse-english-language-a",
    "igcse-english-language-a-16-paper-2-poetry-and-prose-texts-and-imaginative-writing": "igcse-english-language-a",
    "igcse-english-language-a-16-paper-3-coursework": "igcse-english-language-a",
    "igcse-maths-b-16": "igcse-maths-b",
    "igcse-science-double-award-modular-24-biology-unit-1": "igcse-science-double-award-modular",
    "igcse-science-double-award-modular-24-biology-unit-2": "igcse-science-double-award-modular",
    "igcse-science-double-award-modular-24-chemistry-unit-1": "igcse-science-double-award-modular",
    "igcse-science-double-award-modular-24-chemistry-unit-2": "igcse-science-double-award-modular",
    "igcse-science-double-award-modular-24-physics-unit-1": "igcse-science-double-award-modular",
    "igcse-science-double-award-modular-24-physics-unit-2": "igcse-science-double-award-modular",
}

RESOLVED_TIERS = {"T1_verbatim", "T2_near", "T3_section_anchored"}
METHOD = ("tiered auto-join initial pass (T-SME-11; map_spec_points.py "
          "T1-T4/S1-S2; SME-authorized corpus; PMT excluded as source); "
          "operator verdict rounds pending")
VALIDATION = ("AI_VALIDATED (operator-delegated chain; T-SME-11 initial "
              "tiered auto-join from the harvested SME index against the "
              "canonical parsed registry; ambiguous and weak joins left "
              "unresolved by design)")


def registry_index(qual: str) -> tuple[dict, dict]:
    sp = json.loads((PARSED / qual / "spec_points.json").read_text())
    pts = sp["spec_points"]
    by_id = {p["id"]: p for p in pts}
    by_code = {}
    for p in pts:
        by_code.setdefault(p.get("official_code"), p)
    return by_id, by_code


def part_refs(course: str) -> dict[str, int]:
    refs: dict[str, int] = {}
    for tj in sorted((EQ / course).glob("*/*/topic.json")):
        t = json.loads(tj.read_text())
        for q in t.get("questions") or []:
            for p in q.get("parts") or []:
                for sid in p.get("spec_point_ids") or []:
                    refs[sid] = refs.get(sid, 0) + 1
    return refs


def apply_lane(course: str, qual: str) -> dict:
    mp = json.loads((EQ / course / "spec_point_map.json").read_text())
    idx = json.loads((EQ / course / "spec_point_index.json").read_text())
    entries = idx["spec_points"]
    by_id_reg, by_code_reg = registry_index(qual)
    refs = part_refs(course)

    resolved_rows, unresolved_ids = [], []
    mappings = mp.get("mappings") or {}
    unmapped = {u["spcpt_id"]: u for u in mp.get("unmapped") or []}
    flag_by_id = {f["spcpt_id"]: f for f in mp.get("flags") or []}

    for sid, entry in sorted(entries.items()):
        m = mappings.get(sid)
        row = {
            "id": sid,
            "sme_name": entry.get("name") or "",
            "sme_definition": entry.get("definition") or "",
            "referenced_by_parts": refs.get(sid, 0),
        }
        if m and not m.get("flag") and (m["tier"] in RESOLVED_TIERS
                                        or m["tier"] == "S1_name_match"):
            reg = by_id_reg.get(m["official_id"])
            if reg is None:
                sys.exit(f"FAIL {course}: {sid} -> official_id "
                         f"{m['official_id']} not in registry")
            # quals with synthesized ids (english_lit family) print no
            # statement codes — the convention is the official_id suffix
            code = (reg.get("official_code")
                    or reg["id"].rsplit(":", 1)[-1])
            if code != (m.get("official_code")
                        or (m.get("official_id") or "").rsplit(":", 1)[-1]):
                sys.exit(f"FAIL {course}: {sid} code mismatch "
                         f"{m.get('official_code')} vs registry {code}")
            row.update({
                "resolved_code": code,
                "official_id": m["official_id"],
                "official_wording": reg.get("text") or "",
                "tier": m["tier"],
                "unit": m.get("unit"),
                "score": m.get("score"),
                "method": METHOD,
            })
            resolved_rows.append(row)
        elif m and m.get("flag"):
            row.update({"resolved_code": None,
                        "reason": f"flagged: {m['flag']}"})
            unresolved_ids.append(sid)
            resolved_rows.append(row)
        else:
            reason = (unmapped.get(sid) or {}).get("reason") or "unmapped by auto-join"
            row.update({"resolved_code": None,
                        "reason": reason})
            unresolved_ids.append(sid)
            resolved_rows.append(row)

    doc = {
        "schema": "syllabai.sme-spec-point-resolution/1.0",
        "generated_utc": NOW,
        "validation": VALIDATION,
        "counts": {"ids": len(entries),
                   "resolved": len(entries) - len(unresolved_ids),
                   "unresolved": len(unresolved_ids)},
        "unresolved_allowlist_note": ("parts whose ids are all unresolved "
                                      "stay uncoded by design (no-guess "
                                      "discipline)"),
        "resolved": resolved_rows,
    }
    (EQ / course / "spec_point_resolution.json").write_text(
        json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")

    # manifest bookkeeping (same block the t_spec appliers maintain)
    man_path = EQ / course / "manifest.json"
    man = json.loads(man_path.read_text())
    man["spec_point_resolution"] = {
        "counts": {"parts_with_codes": sum(1 for r in resolved_rows
                                           if r.get("resolved_code")),
                   "parts_left_uncoded_no_guess_tail": len(unresolved_ids),
                   "parts_total": len(entries)},
        "pipeline": ["scripts/t_sme_11_apply.py",
                     "scripts/map_spec_points.py",
                     "scripts/sme_spcpt_harvest_all.py"],
        "updated_utc": NOW,
    }
    man_path.write_text(json.dumps(man, ensure_ascii=False, indent=1),
                        encoding="utf-8")
    print(f"[{course}] ids={len(entries)} resolved="
          f"{len(entries) - len(unresolved_ids)} unresolved="
          f"{len(unresolved_ids)}")
    return doc["counts"]


def apply_part_codes(course: str) -> tuple[int, int]:
    """Write spec_point_codes onto topic.json parts from the resolution
    sidecar (idempotent). Parts whose ids are all unresolved stay uncoded
    (the no-guess allowlist)."""
    res = json.loads((EQ / course / "spec_point_resolution.json").read_text())
    id2code = {r["id"]: r.get("resolved_code") for r in res["resolved"]}
    n_parts = n_coded = 0
    for tj in sorted((EQ / course).glob("*/*/topic.json")):
        t = json.loads(tj.read_text())
        changed = False
        for q in t.get("questions") or []:
            for p in q.get("parts") or []:
                n_parts += 1
                sids = p.get("spec_point_ids") or []
                codes = sorted({id2code[s] for s in sids if id2code.get(s)})
                if codes:
                    n_coded += 1
                if p.get("spec_point_codes") != codes:
                    p["spec_point_codes"] = codes
                    changed = True
        if changed:
            tj.write_text(json.dumps(t, ensure_ascii=False, indent=1),
                          encoding="utf-8")
    return n_parts, n_coded


def main() -> int:
    total_r = total_u = 0
    for course, qual in sorted(LANES.items()):
        c = apply_lane(course, qual)
        total_r += c["resolved"]
        total_u += c["unresolved"]
        n_parts, n_coded = apply_part_codes(course)
        if n_parts:
            print(f"  [{course}] parts {n_parts} coded {n_coded}")
    print(f"TOTAL resolved {total_r} unresolved {total_u} "
          f"across {len(LANES)} lanes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
