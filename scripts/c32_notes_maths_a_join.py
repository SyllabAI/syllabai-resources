#!/usr/bin/env python3
"""c32_notes_maths_a_join.py — T-C32 (K2-A) Lane A builder for igcse-maths-a.

The operator fired gate K2-A of the C31 K2 scope (graph/reports/
C31_IGCSE_MATHS_A_K2_SCOPE.md §4/§8): build the notes↔SP join for
`igcse-maths-a-18-higher` as a DERIVED-LANE artifact — corpus byte-frozen.

What it does (zero-LLM, deterministic, fail-closed):
  1. Reads the notes corpus manifest + all 191 note JSONs, collecting every
     note's `spec_point_ids` (the 203 `spcpt_*` anchors).
  2. Joins each anchor to the corpus-side resolution substrate
     (SME-ExamQuestion/igcse-maths-a-18-higher/spec_point_resolution.json,
     AI_VALIDATED operator-delegated, T-SPEC-7/8/9/10 rounds) BY ID —
     deterministic id lookup, NO fuzzy matching, NO re-derivation.
  3. Resolved fields (`resolved_code`, `official_id`, `official_wording`,
     `sme_name`, `sme_definition`, `tier`, `method`, `score`, `unit`,
     `referenced_by_parts`) are COPIED 1:1 — provenance preserved exactly,
     nothing downgraded (the sme_notes_chem_join.py verbatim rule).
  4. Validates every mapped code against the ratified K1 store
     (graph/igcse-maths-a/specification_points.yaml): foreign codes are a
     hard failure; per-row wording class recorded (EXACT /
     LEDGER_EXPLAINABLE / DIVERGENT — divergent is recorded, never repaired).
  5. Anything unresolved is RECORDED, never fabricated: the single
     EQ-unresolved anchor keeps status UNRESOLVED and carries PROPOSAL-ONLY
     candidates from a transparent deterministic scorer (difflib ratio +
     token overlap, section-prior boost mirroring the chemistry matcher's
     subsection boost). Proposals bind nothing.
  6. Writes exactly one file:
     Official-Specifications/parsed/_derived/notes-join/igcse-maths-a-18-higher.json
     (the `_derived/` lane is the working precedent for non-canonical
     artifacts; the directory decision is recorded in the C32 lane record).

Byte-freeze guarantees (asserted by scripts/c32_k2a_check.py):
  - SME-RevisionNotes/** and SME-ExamQuestion/**: untouched
  - Official-Specifications/parsed/igcse-maths-a/* canonical bundle: untouched
  - graph/igcse-chemistry/**, graph/igcse-maths-a/**: untouched
  - the only write is the derived artifact above

Usage:
    python3 scripts/c32_notes_maths_a_join.py
    # exits non-zero on any fail-closed condition, writes nothing in that case
"""
from __future__ import annotations

import difflib
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
COURSE = "igcse-maths-a-18-higher"

NOTES_DIR = f"SME-RevisionNotes/{COURSE}"
RESOLUTION = f"SME-ExamQuestion/{COURSE}/spec_point_resolution.json"
SP_STORE = f"graph/{QUAL}/specification_points.yaml"
LEDGER = "graph/reports/C30_MATHS_A_TIER_DEDUPE_LEDGER.json"
OUT = ("Official-Specifications/parsed/_derived/notes-join/"
       "igcse-maths-a-18-higher.json")

# section slug (notes tree) -> ratified section code, for the residual
# proposal's section-prior boost (mirrors the chemistry subsection boost;
# PROPOSAL-ONLY, never applied to resolved rows)
SECTION_SLUGS = {
    "1-numbers-and-the-number-system": "4MA1-S1",
    "2-equations-formulae-and-identities": "4MA1-S2",
    "3-sequences-functions-and-graphs": "4MA1-S3",
    "4-geometry-and-trigonometry": "4MA1-S4",
    "5-vectors-and-transformation-geometry": "4MA1-S5",
    "6-statistics-and-probability": "4MA1-S6",
}


class R:
    """disk-first / git-fallback reader over ONE persistent cat-file batch."""

    def __init__(self):
        self.methods: dict[str, str] = {}
        self._cache: dict[str, bytes] = {}
        self._proc = None

    def _show(self, rel: str) -> bytes:
        if self._proc is None:
            self._proc = subprocess.Popen(
                ["git", "-C", str(REPO), "cat-file", "--batch"],
                stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        self._proc.stdin.write(f"HEAD:{rel}\n".encode())
        self._proc.stdin.flush()
        parts = self._proc.stdout.readline().decode().split()
        if len(parts) < 3 or parts[1] == "missing":
            raise FileNotFoundError(rel)
        body = self._proc.stdout.read(int(parts[2]))
        self._proc.stdout.read(1)
        return body

    def close(self):
        if self._proc is not None:
            try:
                self._proc.stdin.close()
                self._proc.terminate()
            except Exception:
                pass
            self._proc = None

    def read_bytes(self, rel: str) -> bytes:
        if rel not in self._cache:
            p = REPO / rel
            if p.is_file():
                self.methods[rel] = "disk"
                self._cache[rel] = p.read_bytes()
            else:
                self.methods[rel] = "git-show"
                self._cache[rel] = self._show(rel)
        return self._cache[rel]

    def read_json(self, rel: str):
        return json.loads(self.read_bytes(rel).decode("utf-8"))

    def read_yaml(self, rel: str):
        return yaml.safe_load(self.read_bytes(rel).decode("utf-8"))


def sha16(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()[:16]


def norm(s: str) -> str:
    return " ".join(re.findall(r"[a-z0-9]+", (s or "").lower()))


def fail(msg: str) -> None:
    print(f"FAIL-CLOSED: {msg}", file=sys.stderr)
    sys.exit(1)


def rows_of(d: dict, candidates: list[str]) -> list:
    for k in candidates:
        v = d.get(k)
        if isinstance(v, list) and v and isinstance(v[0], dict):
            return v
    fail(f"no row list among {candidates} in SP store")


def main() -> int:
    r = R()
    inputs = {}

    # ---- inputs + immutable input pins -------------------------------------
    resolution = r.read_json(RESOLUTION)
    nm = r.read_json(f"{NOTES_DIR}/manifest.json")
    sp = r.read_yaml(SP_STORE)
    ledger = r.read_json(LEDGER).get("rows") or []

    res_sha = sha16(r.read_bytes(RESOLUTION))
    nm_sha = sha16(r.read_bytes(f"{NOTES_DIR}/manifest.json"))
    sp_sha = sha16(r.read_bytes(SP_STORE))
    ledger_sha = sha16(r.read_bytes(LEDGER))
    inputs = {
        "notes_manifest": {"path": f"{NOTES_DIR}/manifest.json",
                           "sha256_16": nm_sha},
        "resolution": {"path": RESOLUTION, "sha256_16": res_sha},
        "spec_points_store": {"path": SP_STORE, "sha256_16": sp_sha},
        "tier_dedupe_ledger": {"path": LEDGER, "sha256_16": ledger_sha},
    }

    # ---- ratified store index ----------------------------------------------
    sp_rows = rows_of(sp, ["specification_points", "rows", "points"])
    by_code = {row["official_code"]: row for row in sp_rows}
    order = {row["official_code"]: row["global_order"] for row in sp_rows}
    ledger_map = {x["official_code"]: x for x in ledger}

    # ---- resolution index ---------------------------------------------------
    res_rows = resolution.get("resolved") or []
    res_map = {x["id"]: x for x in res_rows}
    n_ids = len(res_rows)
    n_resolved = sum(1 for x in res_rows if x.get("resolved_code"))

    # ---- walk the notes (all pages, fail on any miss) -----------------------
    pages = nm.get("pages") or []
    if nm.get("course_slug") != COURSE:
        fail(f"manifest course_slug {nm.get('course_slug')!r} != {COURSE!r}")
    anchors: list[dict] = []
    for p in pages:
        rel = f"{NOTES_DIR}/{p['path']}"
        note = r.read_json(rel)
        ids = note.get("spec_point_ids") or []
        for aid in ids:
            anchors.append({
                "anchor_id": str(aid),
                "note_path": p["path"],
                "rn_id": p.get("rn_id") or note.get("note_id"),
                "note_title": note.get("title") or note.get("page_title"),
            })
    if len(anchors) != 203 or len({a['anchor_id'] for a in anchors}) != 203:
        fail(f"anchor census drifted: {len(anchors)} anchors, "
             f"{len({a['anchor_id'] for a in anchors})} distinct (expected 203/203)")

    # ---- deterministic id-lookup join ---------------------------------------
    joins, unresolved = [], []
    for a in sorted(anchors, key=lambda x: (x["note_path"], x["anchor_id"])):
        row = res_map.get(a["anchor_id"])
        if row is None:
            unresolved.append({**a, "status": "UNRESOLVED — RECORDED, NEVER FABRICATED",
                               "reason": "id absent from the resolution substrate",
                               "disposition_proposals": []})
            continue
        if not row.get("resolved_code"):
            unresolved.append({**a, "status": "UNRESOLVED — RECORDED, NEVER FABRICATED",
                               "reason": "EQ substrate row has no resolved_code",
                               "sme_name": row.get("sme_name"),
                               "disposition_proposals": []})
            continue
        code = row["resolved_code"]
        store_row = by_code.get(code)
        if store_row is None:
            fail(f"foreign official_code {code!r} for {a['anchor_id']} "
                 f"(not in the canonical 188) — never fabricate")
        rw, sw = " ".join((row.get("official_wording") or "").split()), \
            " ".join((store_row.get("official_wording") or "").split())
        if rw == sw:
            wc = "EXACT"
        else:
            lrow = ledger_map.get(code)
            wc = "LEDGER_EXPLAINABLE" if lrow and \
                rw == " ".join(lrow["foundation"]["text"].split()) and \
                sw == " ".join(lrow["higher"]["text"].split()) else "DIVERGENT"
        joins.append({
            "anchor_id": a["anchor_id"],
            "note_path": a["note_path"],
            "rn_id": a["rn_id"],
            "note_title": a["note_title"],
            "resolved_code": code,
            "store_row_code": store_row["code"],
            "store_global_order": store_row["global_order"],
            "official_id": row.get("official_id"),
            "official_wording": row.get("official_wording"),
            "sme_name": row.get("sme_name"),
            "sme_definition": row.get("sme_definition"),
            "tier": row.get("tier"),
            "method": row.get("method"),
            "score": row.get("score"),
            "unit": row.get("unit"),
            "referenced_by_parts": row.get("referenced_by_parts"),
            "wording_check": wc,
            "provenance": {
                "join_method": "deterministic id lookup; fields copied 1:1 from "
                               f"{RESOLUTION}@{res_sha}",
                "copied_1to1": True,
                "fuzzy_matching_used": False,
            },
        })

    # ---- residual proposal scorer (PROPOSAL-ONLY, binds nothing) ------------
    for u in unresolved:
        if not u.get("sme_name"):
            continue
        # section prior from the MANIFEST path (uniform string shape
        # 'notes/<section-slug>/<topic>/<leaf>.json'); the note JSON's own
        # `path` field is a structured dict and not used here
        seg = u["note_path"].split("/")
        section = SECTION_SLUGS.get(seg[1]) \
            if len(seg) > 2 and seg[0] == "notes" else None
        q = norm(u["sme_name"])
        qtok = set(q.split())
        cands = []
        for row in sp_rows:
            w = norm(row.get("official_wording") or "")
            if not w:
                continue
            ratio = difflib.SequenceMatcher(None, q, w).ratio()
            ov = len(qtok & set(w.split())) / max(len(qtok), 1)
            boost = 0.10 if section and row.get("section") == section else 0.0
            cands.append({
                "official_code": row["official_code"],
                "store_row_code": row["code"],
                "official_wording": row.get("official_wording"),
                "score": round(0.5 * ratio + 0.5 * ov + boost, 4),
                "components": {"difflib_ratio": round(ratio, 4),
                               "token_overlap": round(ov, 4),
                               "section_prior_boost": boost},
            })
        cands.sort(key=lambda c: -c["score"])
        margin = round(cands[0]["score"] - cands[1]["score"], 4) \
            if len(cands) > 1 else None
        u["disposition_proposals"] = [{
            "method": "PROPOSAL-ONLY deterministic scorer: 0.5*difflib(name, "
                      "wording) + 0.5*token_overlap (+0.10 section prior from "
                      f"the note's own tree section {section}); mirrors the "
                      "chemistry matcher's subsection boost; the operator "
                      "adjudicates — nothing here resolves the anchor",
            "top_candidates": cands[:5],
            "top_score_margin": margin,
        }]

    # ---- census -------------------------------------------------------------
    distinct_codes = sorted({j["resolved_code"] for j in joins})
    tier_split, anchor_tier_split = {}, {}
    for j in joins:
        t = (by_code[j["resolved_code"]].get("applicability") or {}).get("tier")
        anchor_tier_split[t] = anchor_tier_split.get(t, 0) + 1
    for code in distinct_codes:
        t = (by_code[code].get("applicability") or {}).get("tier")
        tier_split[t] = tier_split.get(t, 0) + 1
    wc_census = {}
    for j in joins:
        wc_census[j["wording_check"]] = wc_census.get(j["wording_check"], 0) + 1

    doc = {
        "schema": "syllabai.notes-spec-point-join/1.0",
        "task": "T-C32 (K2-A Lane A build, igcse-maths-a)",
        "generated_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "generator": "scripts/c32_notes_maths_a_join.py",
        "lane": "A (T-C10-pattern note-level mapping) of the C28 §6-K2 sequence",
        "inputs": inputs,
        "validation_tier": (
            "INHERITED: AI_VALIDATED (operator-delegated chain; T-SPEC-7/8/9/10 "
            "operator-verdict rounds 2026-09-19, PMT excluded as source) on the "
            "resolution substrate; JOIN: deterministic id lookup, machine-gated "
            "by c32_k2a_check.py; NO HUMAN_VALIDATED claim is made by this "
            "artifact — an operator spot-check round can upgrade the tier on "
            "record via a dated addendum"),
        "counts": {
            "notes_pages": len(pages),
            "anchors_total": len(anchors),
            "anchors_distinct": len({a["anchor_id"] for a in anchors}),
            "joined": len(joins),
            "unresolved_recorded": len(unresolved),
            "ids_absent_from_resolution": sum(
                1 for u in unresolved if "absent" in u["reason"]),
            "distinct_official_codes": len(distinct_codes),
            "coverage_of_188": f"{len(distinct_codes)}/188",
            "coverage_by_applicability_tier": tier_split,
            "anchors_by_applicability_tier": anchor_tier_split,
            "foreign_codes": 0,
            "wording_check_census": wc_census,
        },
        "ordering": "joins sorted by (store global_order of resolved_code, "
                    "note_path, anchor_id); unresolved sorted by (note_path, "
                    "anchor_id) — presentation only, no field re-derived",
        "residual_rule": "RECORDED, never fabricated: unresolved anchors carry "
                         "PROPOSAL-ONLY candidates and stay unresolved until "
                         "the operator adjudicates",
        "joins": sorted(joins, key=lambda j: (j["store_global_order"],
                                              j["note_path"], j["anchor_id"])),
        "unresolved": unresolved,
    }

    # ---- fail-closed postconditions -----------------------------------------
    c = doc["counts"]
    if not (c["joined"] == 202 and c["unresolved_recorded"] == 1
            and c["anchors_total"] == 203 and c["foreign_codes"] == 0):
        fail(f"postcondition drift: {json.dumps(c)}")
    if len(doc["joins"]) + len(doc["unresolved"]) != 203:
        fail("join+unresolved != anchors")

    out = REPO / OUT
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    r.close()
    print(f"wrote {OUT} ({out.stat().st_size} bytes)")
    print(f"counts: {json.dumps(c)}")
    print(f"residual: {u['anchor_id']} proposals={len(u['disposition_proposals'][0]['top_candidates']) if u.get('disposition_proposals') else 0}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
