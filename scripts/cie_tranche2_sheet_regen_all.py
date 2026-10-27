#!/usr/bin/env python3
"""
T-SPECS-CIE-TRANCHE2-R2-SHEETS-1 — the tranche-2 round-2 OPERATOR REVIEW SHEET
regeneration engine: map-universe pools for the whole CIE fleet.

Fires the nextAct lane act of the tranche-2 round-1 receipt of record
(.syllabai/receipts/CIE-INTEGRATION/cie-tranche2-r1-consume-run-001-r0.json):
"sheet regeneration (map-universe pools for all 38 banks) + the ruling-batch
encoding engines on the operator's batches" — on the operator's order
(gateway trace 1a15ffe16e67399d, 2026-10-22, zai-web).

THE MATERIAL FINDING OF RECORD (r1 receipt) is THIS engine's pool law:
  the sidecar-pending universe is NOT the bundle gap universe — the r1
  figures were computed on the SIDECAR codes-empty state; the tranche-2
  sheet program's pools must be derived from the MAP zero-code universe.
  Per bank this engine computes and cross-foots BOTH, and discloses the
  reconciliation (chemistry-25 precedent: map pool 1,342 zero-code parts =
  1,336 declared-carrying (256 sids, the verdict units) + 6 sid-less (the
  tranche-3 class); sidecar pending pool 1,336 — identity proven).

Per bank (the 44 CIE sidecar banks):
  pool_a  — MAP question_part items, codes == [], WITH declaredUnresolved:
            the verdict-program units, keyed by sid (the ruling unit;
            1 pending part may declare several sids; the sid's part_refs
            list every part that declared it)
  pool_b  — MAP zero-code parts WITHOUT declaredUnresolved: sid-less, NOT
            ruleable here (upstream coverage class — the tranche-3 shape);
            disclosed in the header, excluded from rows
  recon   — the sidecar pending pool vs pool_a: sids, part sets, and the
            map-only / sidecar-only part drift, disclosed (never coerced)
  rows    — per sid (sorted): verbatim SME name + definition + subtopic
            slugs (spec_point_index), evidence class (the r1 law unchanged:
            J4_residue / multi_hit / declared_link / record_less / no_match,
            phrase hits token-bounded lane-wide over the parsed registry),
            the MAP-side scoped codes (spcptSubtopicScope, when the map
            declares them), the section-derived candidate points of the
            sid's first section topic (verbatim texts, capped with a
            disclosed truncation flag), home/referencing note refs with
            declared codes, and ruling: PENDING (operator-owned).

Tier law UNCHANGED (ADR-030 + AGENT.md rule 3): the lane never invents;
the operator's ruling is the only authoritative class. A later lane encodes
ruled batches via cie_tranche2_batch_encode.py as V8_name_phrase_verdict /
operator_verdict rows; the 134c gate stays PARKED while the census is
unchanged (r1 receipt nextAct).

Read-only on the corpora and the maps; writes:
  scripts/cie_tranche2_sheets/{bank}.yaml     (per-bank ruling surface)
  scripts/cie_tranche2_sheets/_index.json     (fleet index + sheet sha256s
                                               + substrate pins — the
                                               encoder's staleness guard)
  graph/reports/tranche2-r2/{bank}.md         (the operator reading surface)
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
SL = REPO / "spec-links"
REPORTS = REPO / "graph" / "reports"
OUT_DIR = REPO / "scripts" / "cie_tranche2_sheets"
MD_DIR = REPORTS / "tranche2-r2"

LANE = "T-SPECS-CIE-TRANCHE2-R2-SHEETS-1"
STAMP = "2026-10-22T12:00:00Z"
DIRECTIVE = ("operator order (gateway trace 1a15ffe16e67399d, 2026-10-22, zai-web) — "
             "the tranche-2 r1 receipt's nextAct lane act: sheet regeneration on the "
             "map-universe pools + the ruling-batch encoding engines")
NEW_TIER_DOC = ("V8_name_phrase_verdict / operator_verdict (encoded by "
                "cie_tranche2_batch_encode.py on the operator's ruled batches)")
CAND_CAP = 200  # section-derived candidate cap per sid (disclosed truncation)

MAPS_DIR = Path(os.environ.get(
    "CIE_V2_MAPS",
    "/home/z/my-project/work/syllabai-origin-wt/apps/hub/content-maps"))


def die(msg):
    print(f"ABORT: {msg}", flush=True)
    sys.exit(1)


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "")).strip().lower()


def tokens(s: str):
    return [t for t in re.split(r"[^a-z0-9]+", norm(s)) if t]


def phrase_hits(tt, uni, scope_topic=None):
    L = len(tt)
    if L == 0:
        return []
    hits = []
    for p, tk in uni:
        if scope_topic is not None:
            pid = (p.get("id") or "").split(":")[-1]
            if not pid.startswith(scope_topic + "."):
                continue
        n = len(tk)
        for i in range(n - L + 1):
            if tk[i:i + L] == tt:
                hits.append(p)
                break
    return hits


def registry_points(qual: str):
    man = json.loads((REPO / "Official-Specifications" / "manifest.json").read_text())
    for q in man["qualifications"]:
        if q["slug"] == qual:
            pdf = Path(q["pdf"]).stem
            reg = json.loads(
                (REPO / "Official-Specifications" / "parsed" / qual / f"{pdf}.parsed.json")
                .read_text())
            return reg["spec_points"]
    die(f"qual {qual!r} not in Official-Specifications/manifest.json")


def main() -> int:
    sidecars = sorted(SL.glob("cie-*.json"))
    if len(sidecars) != 44:
        die(f"expected 44 CIE sidecars, found {len(sidecars)}")
    MD_DIR.mkdir(parents=True, exist_ok=True)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    index_banks = []
    fleet = defaultdict(int)

    for sl_path in sidecars:
        bank = sl_path.stem
        side = json.loads(sl_path.read_text())
        map_path = MAPS_DIR / f"{bank}.json"
        if not map_path.exists():
            die(f"map missing for {bank}: {map_path}")
        cmap = json.loads(map_path.read_text())
        spi = json.loads((REPO / "SME-ExamQuestion" / bank / "spec_point_index.json").read_text())
        sp = spi.get("spec_points") or {}
        pts = registry_points(side["registry"]["id"])
        uni = [(p, tokens(p.get("text") or "")) for p in pts]
        spcpt_by_code = {p.get("official_code"): p for p in pts}

        items = side["items"]
        mitems = cmap["items"]

        # ---- pools from the MAP (the material finding's law) ----------------
        pool_a = defaultdict(list)   # sid -> [part iid]
        pool_b = []                  # sid-less zero-code parts
        map_zero = 0
        for iid, it in mitems.items():
            if not isinstance(it, dict) or it.get("kind") != "question_part":
                continue
            if it.get("codes"):
                continue
            map_zero += 1
            du = it.get("declaredUnresolved") or []
            if du:
                for sid in du:
                    pool_a[sid].append(iid)
            else:
                pool_b.append(iid)

        # ---- sidecar pending pool + reconciliation --------------------------
        sc_pending = defaultdict(list)
        for iid, it in items.items():
            if not isinstance(it, dict) or it.get("kind") != "question_part":
                continue
            if it.get("codes"):
                continue
            for sid in it.get("pending") or []:
                sc_pending[sid].append(iid)

        sid_delta = sorted(set(pool_a) - set(sc_pending))
        sc_delta = sorted(set(sc_pending) - set(pool_a))
        part_ref_drift = []
        for sid in sorted(set(pool_a) & set(sc_pending)):
            if sorted(pool_a[sid]) != sorted(sc_pending[sid]):
                part_ref_drift.append({
                    "sid": sid,
                    "map_parts": sorted(pool_a[sid]),
                    "sidecar_parts": sorted(sc_pending[sid]),
                })
        all_map_zero = {p for s, ps in pool_a.items() for p in ps} | set(pool_b)
        all_sc_pend = {p for s, ps in sc_pending.items() for p in ps}
        map_only_zero = sorted(all_map_zero - all_sc_pend)
        pool_a_parts = len(all_map_zero) - len(pool_b)   # distinct declared parts
        pool_a_decls = sum(len(v) for v in pool_a.values())  # part-sid declarations
        sc_parts = len(all_sc_pend)
        sc_decls = sum(len(v) for v in sc_pending.values())
        if map_zero != pool_a_parts + len(pool_b):
            die(f"{bank}: map zero accounting broken: {map_zero} != "
                f"{pool_a_parts} + {len(pool_b)}")
        recon = {
            "law": ("pool_a derives from the MAP zero-code universe (the r1 receipt's "
                    "material finding); the sidecar pending pool is the cross-foot, "
                    "not the pool; parts are DISTINCT items — a part declaring "
                    "several sids appears once here and once per sid row below "
                    "(declarations disclosed separately)"),
            "map_zero_code_parts": map_zero,
            "map_pool_a_parts_distinct": pool_a_parts,
            "map_pool_a_declarations": pool_a_decls,
            "map_pool_a_sids": len(pool_a),
            "map_pool_b_parts_sidless": len(pool_b),
            "sidecar_pending_parts_distinct": sc_parts,
            "sidecar_pending_declarations": sc_decls,
            "sidecar_pending_sids": len(sc_pending),
            "sids_only_in_map": sid_delta,
            "sids_only_in_sidecar": sc_delta,
            "part_ref_drift": part_ref_drift,
            "map_zero_parts_absent_from_sidecar": map_only_zero,
        }

        # ---- coded notes (the declared_link evidence) -----------------------
        coded_notes = {iid: [c.get("official_code") for c in (it.get("codes") or [])]
                       for iid, it in items.items()
                       if isinstance(it, dict) and it.get("kind") == "note" and it.get("codes")}
        map_scope = cmap.get("spcptSubtopicScope") or {}

        # ---- rows ------------------------------------------------------------
        rows = []
        cls_census = defaultdict(int)
        for sid in sorted(pool_a):
            r = sp.get(sid) or {}
            name = (r.get("name") or "").strip()
            subs = r.get("subtopic_slugs") or []
            home_notes = list(r.get("notes") or [])
            part_refs = sorted(pool_a[sid])
            sections = sorted({s for iid in part_refs
                               if isinstance(items.get(iid), dict) and items[iid].get("section")
                               for s in [items[iid].get("section")]} |
                              {items[iid].get("topic") for iid in part_refs
                               if isinstance(items.get(iid), dict) and items[iid].get("topic")})

            cls = "no_match"
            hits_wide = phrase_hits(tokens(name), uni) if name else []
            if not name and not (r.get("definition") or "").strip():
                cls = "record_less"
            elif len(hits_wide) == 1:
                cls = "J4_residue"
            elif len(hits_wide) > 1:
                cls = "multi_hit"
            else:
                for nid in home_notes:
                    if nid in coded_notes:
                        cls = "declared_link"
                        break

            # scoped candidates: (a) the MAP's declared scope codes; (b) the
            # sid's first section topic's parsed points (capped, disclosed)
            scoped_map_codes = sorted((map_scope.get(sid) or {}).get("specPointCodes") or [])
            cands, cand_trunc, cand_total = [], False, 0
            if scoped_map_codes:
                cands = [{"code": c, "id": (spcpt_by_code.get(c) or {}).get("id"),
                          "text": ((spcpt_by_code.get(c) or {}).get("text") or "").strip(),
                          "via": "map:spcptSubtopicScope"}
                         for c in scoped_map_codes if c in spcpt_by_code]
            if not cands and sections:
                m = re.match(r"(\d+)[-_.]", sections[0])
                if m:
                    tno = m.group(1)
                    tp = [p for p in pts
                          if (p.get("id") or "").split(":")[-1].startswith(tno + ".")]
                    cand_total = len(tp)
                    shown = tp[:CAND_CAP]
                    cand_trunc = cand_total > len(shown)
                    cands = [{"code": p.get("official_code"), "id": p.get("id"),
                              "text": (p.get("text") or "").strip(),
                              "via": f"section-topic:{tno}"}
                             for p in shown]

            rows.append({
                "sid": sid,
                "sme_name": name,
                "sme_definition": (r.get("definition") or "").strip(),
                "subtopic_slugs": subs,
                "sections": sections,
                "pending_parts": len(part_refs),
                "part_refs": part_refs,
                "note_refs": sorted(set(home_notes)),
                "cls": cls,
                "wide_phrase_hits": sorted({p.get("official_code") for p in hits_wide}),
                "map_scoped_codes": scoped_map_codes,
                "scoped_candidates": cands,
                "candidates_truncated": cand_trunc,
                "candidates_topic_total": cand_total,
                "declared_note_codes": (coded_notes.get(home_notes[0])
                                        if home_notes and home_notes[0] in coded_notes else None),
                "ruling": "PENDING",
            })
            cls_census[cls] += 1

        sheet = {
            "lane": LANE,
            "generated_utc": STAMP,
            "bank": bank,
            "directive": DIRECTIVE,
            "law": ("operator_verdict is the only authoritative class for the "
                    "no-match pool (ADR-030 + AGENT.md rule 3: no semantic-similarity "
                    "manufacturing); the lane assembles verbatim evidence and scoped "
                    "candidates from the MAP-universe pool (the r1 receipt's material "
                    "finding); the operator rules per sid; ruled batches encode as "
                    "V8_name_phrase_verdict / operator_verdict via "
                    "cie_tranche2_batch_encode.py; the 134c gate stays parked while "
                    "the census is unchanged"),
            "pool_law": ("MAP zero-code universe (r1 receipt materialFinding) — NOT "
                         "the sidecar codes-empty state"),
            "substrate_pins": {
                "map_sha256": sha256_file(map_path),
                "sidecar_sha256": sha256_file(sl_path),
                "spec_point_index_sha256": sha256_file(
                    REPO / "SME-ExamQuestion" / bank / "spec_point_index.json"),
                "registry_qual": side["registry"]["id"],
            },
            "reconciliation": recon,
            "pool": {
                "map_zero_code_parts": map_zero,
                "verdict_units_parts_distinct": pool_a_parts,
                "verdict_unit_declarations": pool_a_decls,
                "distinct_sids": len(rows),
                "sidless_parts_tranche3_class": len(pool_b),
                "class_census": dict(sorted(cls_census.items())),
                "official_points_in_scope": len(pts),
                "candidate_cap": CAND_CAP,
            },
            "ruling_schema_doc": (
                "per sid — anchor: {official_code, official_id} (one or more; "
                "official_id must be the registry pairing of official_code) | "
                "quarantine: no honest anchor from the evidence | defer: {reason}. "
                "Ruled batches land as scripts/cie_tranche2_batches/{batch_id}.yaml "
                "and encode via cie_tranche2_batch_encode.py"),
            "rows": rows,
        }
        out_yaml = OUT_DIR / f"{bank}.yaml"
        out_yaml.write_text(yaml.safe_dump(sheet, sort_keys=False, allow_unicode=True, width=110))

        # ---- markdown render -------------------------------------------------
        lines = [
            f"# T-SPECS-CIE-TRANCHE2-R2-SHEETS-1 — {bank} operator review sheet",
            "",
            f"- Pool (MAP universe): {pool_a_parts} verdict-unit parts "
            f"({pool_a_decls} part-sid declarations) / {len(rows)} distinct sids; "
            f"sid-less (tranche-3 class): {len(pool_b)}",
            f"- Sidecar cross-foot: {sc_parts} pending parts ({sc_decls} declarations) / "
            f"{recon['sidecar_pending_sids']} sids",
            f"- Class census: {dict(sorted(cls_census.items()))}",
            "- Law: the operator rules per sid (anchor / quarantine / defer); the lane never "
            "invents (ADR-030, AGENT.md rule 3). Ruled batches → "
            "scripts/cie_tranche2_batches/{batch_id}.yaml → cie_tranche2_batch_encode.py.",
            "",
        ]
        for section in sorted({s for r in rows for s in r["sections"]}):
            block = [r for r in rows if section in r["sections"]]
            lines.append(f"## {section} — {len(block)} entities")
            for r in sorted(block, key=lambda x: -x["pending_parts"]):
                lines.append(f"### {r['sid']} [{r['cls']}] parts={r['pending_parts']}")
                lines.append(f"- SME name: {r['sme_name']!r}")
                if r["sme_definition"]:
                    lines.append(f"- SME definition: {r['sme_definition'][:300]!r}")
                if r["wide_phrase_hits"]:
                    lines.append(f"- phrase hits: {r['wide_phrase_hits']}")
                if r["map_scoped_codes"]:
                    lines.append(f"- map-scoped codes: {r['map_scoped_codes']}")
                if r["declared_note_codes"]:
                    lines.append(f"- declared home-note codes: {r['declared_note_codes']}")
                lines.append(f"- ruling: **{r['ruling']}**")
                lines.append("")
        (MD_DIR / f"{bank}.md").write_text("\n".join(lines) + "\n")

        index_banks.append({
            "bank": bank,
            "sheet": f"scripts/cie_tranche2_sheets/{bank}.yaml",
            "sheet_sha256": sha256_file(out_yaml),
            "map_pool_a_parts": pool_a_parts,
            "map_pool_a_declarations": pool_a_decls,
            "map_pool_a_sids": recon["map_pool_a_sids"],
            "map_pool_b_sidless": len(pool_b),
            "sidecar_pending_parts": sc_parts,
            "sidecar_pending_declarations": sc_decls,
            "sidecar_pending_sids": recon["sidecar_pending_sids"],
            "class_census": dict(sorted(cls_census.items())),
            "map_zero_code_parts": map_zero,
        })
        fleet["banks"] += 1
        fleet["map_pool_a_parts"] += pool_a_parts
        fleet["map_pool_a_declarations"] += pool_a_decls
        fleet["sids"] += len(rows)
        fleet["sidless"] += len(pool_b)
        fleet["sidecar_pending_parts"] += sc_parts
        fleet["sidecar_pending_declarations"] += sc_decls
        for k, v in cls_census.items():
            fleet[f"cls_{k}"] += v
        print(f"{bank:66s} poolA={pool_a_parts:5d}({pool_a_decls:5d}d)/{len(rows):4d}sids "
              f"sidless={len(pool_b):3d} sidecar={sc_parts:5d}({sc_decls:5d}d) "
              f"classes={dict(sorted(cls_census.items()))}", flush=True)

    index = {
        "lane": LANE,
        "generated_utc": STAMP,
        "directive": DIRECTIVE,
        "tier_doc": NEW_TIER_DOC,
        "pool_law": ("MAP zero-code universe per the tranche-2 r1 receipt's "
                     "materialFinding (cie-tranche2-r1-consume-run-001-r0.json); "
                     "the census receipt's sidecar figures stay historical-of-record"),
        "supersedes": ("scripts/cie_tranche2_chem25_review_sheet.yaml (the r1 head-bank "
                       "sheet, sidecar-pool basis) — kept of record, append-only; the "
                       "chem-25 ruling surface is now this lane's map-universe sheet"),
        "encoder": "scripts/cie_tranche2_batch_encode.py (V8_name_phrase_verdict / operator_verdict)",
        "gate_posture": "the 134c gate stays PARKED while the census is unchanged (r1 nextAct)",
        "fleet": dict(fleet),
        "banks": sorted(index_banks, key=lambda b: (-b["map_pool_a_parts"], b["bank"])),
    }
    # the tranche-3 cross-foot: the census receipt's smeCoverageGap class
    # ("NO sidecar entry, NO smeSpecPointIds") must equal the map's sid-less
    # zero-code class fleet-wide (economics-25 585 / economics-20 119 /
    # geography-20 114 already proven EXACT per bank)
    if fleet["sidless"] != 1203:
        die(f"tranche-3 cross-foot FAILED: fleet sidless {fleet['sidless']} != "
            f"1203 (the census receipt's smeCoverageGap) — reconciliation broken")
    (OUT_DIR / "_index.json").write_text(json.dumps(index, indent=1, ensure_ascii=False) + "\n")

    print(f"\nFLEET: banks={fleet['banks']} poolA_parts={fleet['map_pool_a_parts']} "
          f"decls={fleet['map_pool_a_declarations']} sids={fleet['sids']} "
          f"sidless={fleet['sidless']} (tranche-3 cross-foot EXACT 1203) "
          f"sidecar_parts={fleet['sidecar_pending_parts']}")
    print(f"index: {OUT_DIR / '_index.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
