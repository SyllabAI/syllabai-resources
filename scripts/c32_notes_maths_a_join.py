#!/usr/bin/env python3
"""c32_notes_maths_a_join.py — T-C32 (K2-A) Lane A builder for igcse-maths-a.

T-C42 R11 AMENDMENT (2026-10-03, dated per P5 — landed records never edited,
this generator re-pinned again): re-run over the C42-R10-amended resolution
substrate. The R10 verdict round (the scope §7 loop's third R1-shaped round,
graph/reports/C42_R10_RESOLUTION_REPAIR_RECORD.md) re-pointed 2 codes
(Expanding Triple Brackets H-2.2E -> H-2.2A; Simplifying Algebraic Fractions
1.2A -> H-2.2C), adjudicated the related-calculations NOTE-LEVEL join as
STANDING (the ord-2 section alone DEMOTEs to the worklist at R12), recorded 7
section-level REATTRIBUTE + 1 DEMOTE overrides for the R12 substrate build,
and decided c42-heading-only-convention-1. The pinned census therefore stays
198 joined / 5 unresolved (0 anchors cleared this round; both re-pointed codes
were already covered), and the guard below additionally pins the EXACT
codes the two re-pointed joins must now carry — any other drift fails closed.

T-C42 R7 AMENDMENT (2026-10-02, dated per P5 — landed records never edited,
this generator re-pinned again): re-run over the C42-R6-amended resolution
substrate. The R6 verdict round (the scope §7 loop's second R1-shaped round,
graph/reports/C42_R6_RESOLUTION_REPAIR_RECORD.json) re-pointed 8 codes,
cleared 2 further anchors to UNRESOLVED (Problem Solving with Volumes,
Geometrical Proof — no canonical 188 row teaches them; wrong codes removed,
never forced), and recorded 4+2 section-level overrides + 2 subsumed R1
entries for the R8 substrate build. The pinned census therefore moves
200 joined / 3 unresolved -> 198 joined / 5 unresolved, and the guard below
pins the EXACT post-R6 unresolved id set; any other drift fails closed.

T-C42 R2 AMENDMENT (2026-10-02, dated per P5 — landed records never edited,
this generator re-pinned instead): re-run over the C42-R1-amended resolution
substrate. The R1 operator verdict round (gate 1 of the C42 rework scope,
graph/reports/C42_MATHS_A_RESOLUTION_REPAIR_RECORD.json) re-pointed 22 codes,
re-pointed 21+ rows' official_id/official_wording to their Foundation
statements, and CLEARED 2 anchors to UNRESOLVED (Mathematical Symbols,
Problem Solving with Areas — no canonical 188 row teaches them; wrong codes
removed, never forced). The pinned census therefore moves
202 joined / 1 unresolved -> 200 joined / 3 unresolved, and the guard below
pins the EXACT post-R1 unresolved id set; any other drift fails closed.

Original commission: the operator fired gate K2-A of the C31 K2 scope
(graph/reports/C31_IGCSE_MATHS_A_K2_SCOPE.md §4/§8): build the notes↔SP join
for `igcse-maths-a-18-higher` as a DERIVED-LANE artifact — corpus byte-frozen.

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
  5. Anything unresolved is RECORDED, never fabricated: unresolved anchors
     keep status UNRESOLVED and carry PROPOSAL-ONLY candidates from a
     transparent deterministic scorer (difflib ratio + token overlap,
     section-prior boost mirroring the chemistry matcher's subsection boost).
     Proposals bind nothing. Post-R1 the unresolved set is the C31 §3 residual
     plus the 2 anchors cleared UNRESOLVED by the C42 R1 verdict round.
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
        "task": "T-C42 R11: T-C32 (K2-A Lane A) join re-run over the "
                "C42-R10-amended resolution (igcse-maths-a)",
        "generated_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "generator": "scripts/c32_notes_maths_a_join.py",
        "lane": "A (T-C10-pattern note-level mapping) of the C28 §6-K2 sequence",
        "inputs": inputs,
        "validation_tier": (
            "INHERITED: AI_VALIDATED (operator-delegated chain; T-SPEC-7/8/9/10 "
            "operator-verdict rounds 2026-09-19, PMT excluded as source; C42 R1 "
            "operator verdict round 2026-10-02 — 45 id-level repairs, the C32 "
            "residual KEPT UNRESOLVED, 2 anchors cleared; C42 R6 R1-shaped "
            "verdict round over the R4 defect inventory 2026-10-02 — 8 id-level "
            "repairs, 2 anchors cleared, 4+2 section-level dispositions; C42 R10 "
            "R1-shaped verdict round over the R9 defect inventory 2026-10-03 — "
            "2 id-level repairs, the related-calculations note-level join "
            "adjudicated STANDING, 7+1 section-level dispositions incl. the "
            "loop's first DEMOTE, and c42-heading-only-convention-1; see "
            "C42_MATHS_A_RESOLUTION_REPAIR_RECORD.json, "
            "C42_R6_RESOLUTION_REPAIR_RECORD.json and "
            "C42_R10_RESOLUTION_REPAIR_RECORD.md) on the resolution "
            "substrate; JOIN: deterministic id lookup, machine-gated by the C42 "
            "R11 postcondition in this generator (the C40-era c32_k2a_check.py "
            "battery pins its own 2026-09 landing census and is historical); "
            "NO HUMAN_VALIDATED claim is made by this artifact — an operator "
            "spot-check round can upgrade the tier on record via a dated "
            "addendum"),
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
    # T-C42 R11 census (post the C42-R10-amended resolution): 198 joined /
    # 5 unresolved — the R10 round corrected 2 codes and cleared 0 anchors, so
    # the census is UNCHANGED from R7: the C31 §3 residual KEPT UNRESOLVED at
    # R1 + the 2 anchors the R1 round cleared + the 2 anchors the R6 round
    # cleared. Exact id set pinned; anything else fails closed. NEW at R11:
    # the two re-pointed joins must carry EXACTLY the R10-corrected codes
    # (verbatim-landed proof, the R7 battery's W1 analog pinned in-generator).
    R11_UNRESOLVED = {
        "spcpt_QWXhzVp2S3VYZdZc",  # 'Discrete & Continuous Data' — C31 §3 residual
        "spcpt_8Wtthy9gt8B5xsVW",  # 'Mathematical Symbols' — cleared at R1
        "spcpt_3fMGfNtg3hXMg6gC",  # 'Problem Solving with Areas' — cleared at R1
        "spcpt_mVXT4jbXQPrzhHvz",  # 'Problem Solving with Volumes' — cleared at R6
        "spcpt_hK2H8q4Y8NYv833v",  # 'Geometrical Proof' — cleared at R6
    }
    R11_VERBATIM_CODES = {
        # note_path -> the exact store_row_code the R10 round landed (verdict:
        # CORRECT; the related-calculations anchor adjudicated STANDING at 1.8D)
        "notes/2-equations-formulae-and-identities/expanding-brackets/expanding-triple-brackets.json": "4MA1-2.2A",
        "notes/2-equations-formulae-and-identities/algebraic-fractions/algebraic-fractions.json": "4MA1-2.2C",
        "notes/1-numbers-and-the-number-system/number-toolkit/related-calculations.json": "4MA1-1.8D",
    }
    c = doc["counts"]
    got_unres = {u["anchor_id"] for u in doc["unresolved"]}
    if not (c["joined"] == 198 and c["unresolved_recorded"] == 5
            and c["anchors_total"] == 203 and c["foreign_codes"] == 0):
        fail(f"postcondition drift: {json.dumps(c)}")
    if got_unres != R11_UNRESOLVED:
        fail(f"unresolved id set drift: {sorted(got_unres)}")
    for np_, want in R11_VERBATIM_CODES.items():
        got = next((j["store_row_code"] for j in doc["joins"] if j["note_path"] == np_), None)
        if got != want:
            fail(f"R11 verbatim-code pin: {np_} carries {got!r} != {want!r}")
    if len(doc["joins"]) + len(doc["unresolved"]) != 203:
        fail("join+unresolved != anchors")

    out = REPO / OUT
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    r.close()
    print(f"wrote {OUT} ({out.stat().st_size} bytes)")
    print(f"counts: {json.dumps(c)}")
    for u in doc["unresolved"]:
        n_prop = len(u['disposition_proposals'][0]['top_candidates']) \
            if u.get('disposition_proposals') else 0
        print(f"unresolved: {u['anchor_id']} ({u.get('sme_name')!r}) "
              f"proposals={n_prop}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
