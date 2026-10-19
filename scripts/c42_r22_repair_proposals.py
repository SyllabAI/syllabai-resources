#!/usr/bin/env python3
"""c42_r22_repair_proposals.py — T-C42 R22 deterministic PROPOSAL-ONLY scorer.

The R22 lane is the SIXTH R1-shaped repair round of the C42 K2-B rework loop
(scope §7: "the rework lane repeats R1-shaped rounds only by explicit operator
instruction"), fired by the operator directive "R1 shaped repair"
(2026-10-04, discord, gateway trace f63adc3fd5ac8155cf81200804acb165) over
the R21 re-gate's defect inventory — the 3 fresh REJECT rows of
scripts/c42_r21_fresh_verdicts.yaml (the R21 gate PASSED at exact 92.5% /
partial 100% / none 100%; the 3 rejects + 4 H3 holds are the honest residue
the R21 fill record returned to the operator), now carried on the R5-applied
store (832 anchored rows HUMAN_VALIDATED; the 3 REJECT rows stayed SUGGESTED
— they are the only substrate rows this round may concern).

Surfaces (derived deterministically from the R21 fresh verdict record):
  surface 1 — the id-level rows (root contains "note-level"): NONE this
              round. All 3 R21 REJECT roots are section-level classes and all
              3 note-level joins STAND by the R21 evidence itself
              (3d-pythagoras-and-trigonometry via its Pythagoras sections
              ords 0/1/5; difference-of-two-squares via its within-limit
              basic-DOTS sections ord 1; graphical-solutions via its
              lines-based sections ords 0/2/3) — so there is no id-level
              anchor to score and NO resolution-file amendment this round
              (the R14/R18 shape).
  surface 2 — the section-level rows: 3 rows; candidates for the section
              chunk's true code scored from the chunk heading + the fresh
              verdict's own note against the ratified 188 — BOTH tier
              wordings (the R1 standing instruction): per candidate we score
              the store's operative wording AND the C30 tier-dedupe ledger's
              foundation.text (where the code is a shared-tier row) and rank
              by the better of the two, recording both. PROPOSAL-ONLY — the
              top-1s are deliberately published as noisy (the R14/R18
              scorer-artifact precedent); the operator verdict round decides.
  surface 3 — the heading-only class: the 4 fresh H3 HOLD rows on the R21
              sheet (source == heading-only-convention, verdict == HOLD) are
              LISTED as continuity inventory under the STANDING convention
              c42-heading-only-convention-1 — no scorer candidates (a
              heading-only chunk has no content signal to score), no new
              decision this round. They ride a future round only with the
              operator's explicit per-row sign-off (plus the convention
              decision itself), or stay SUGGESTED — the R21 disposition.
  residual  — continuity only: the C32 §3 residual stays KEPT UNRESOLVED per
              its R1 adjudication (re-affirmed at R6, R10, R14 and R18); no
              new scoring.

Scoring: 0.5*difflib(name, wording) + 0.5*token-jaccard(name, wording)
+ 0.10 section-prior when the note's corpus tree section matches the code's
spec section (the C32 residual-scorer convention, unchanged). PMT is not a
source; top-1 candidates are deliberately published as noisy — they bound
nothing; the operator verdict round decides.

Writes graph/reports/C42_R22_REPAIR_PROPOSALS.json; prints a compact table.
"""
import difflib
import json
import re
import unicodedata
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "graph/reports/C42_R22_REPAIR_PROPOSALS.json"
R21_FRESH = REPO / "scripts/c42_r21_fresh_verdicts.yaml"
R21_REVIEW = REPO / "scripts/c42_r21_review_verdicts.yaml"
STORE = REPO / "graph/igcse-maths-a/spec_chunk_mappings.yaml"
REGISTRY = REPO / "graph/igcse-maths-a/specification_points.yaml"
LEDGER = REPO / "graph/reports/C30_MATHS_A_TIER_DEDUPE_LEDGER.json"
DIRECTIVE = ("R1 shaped repair (2026-10-04, discord, gateway trace "
             "f63adc3fd5ac8155cf81200804acb165)")

_TRANS = {ord("‘"): "'", ord("’"): "'", ord("“"): '"', ord("”"): '"',
          ord("–"): "-", ord("—"): "-", ord("″"): '"', ord("′"): "'"}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFC", s)
    s = s.replace("\\", "")
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"[*_`#>]+", "", s)
    s = s.translate(_TRANS)
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def tokens(s: str) -> set:
    return set(t for t in re.split(r"[^a-z0-9]+", norm(s)) if t)


def score(name_text: str, wording: str, section_prior: bool) -> float:
    a, b = norm(name_text), norm(wording)
    s = 0.5 * difflib.SequenceMatcher(None, a, b).ratio() \
        + 0.5 * (len(tokens(a) & tokens(b)) / max(1, len(tokens(a) | tokens(b))))
    if section_prior:
        s += 0.10
    return round(s, 4)


def main() -> int:
    fresh = yaml.safe_load(R21_FRESH.read_text(encoding="utf-8"))
    review = yaml.safe_load(R21_REVIEW.read_text(encoding="utf-8"))
    store = yaml.safe_load(STORE.read_text(encoding="utf-8"))
    reg = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    points = {p["code"]: p for p in reg["specification_points"]}
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    led_rows = {r["official_code"]: r for r in ledger["rows"]}

    verdicts = fresh["verdicts"]
    rejects = {m: p for m, p in verdicts.items() if p.get("verdict") == "REJECT"}
    holds = {m: p for m, p in review["verdicts"].items()
             if p.get("verdict") == "HOLD"}
    rows_by_id = {r["mapping_id"]: r for r in store["rows"]}

    # ---- surface 1: id-level (note-level-class roots) ------------------------
    surface1 = []
    for mid, p in sorted(rejects.items()):
        root = (p.get("root") or "")
        if "note-level" in (review["verdicts"].get(mid, {}).get("root") or root).lower():
            surface1.append(mid)
    # verified against the full R21 review record roots, not assumed
    surface1 = [m for m in sorted(rejects)
                if "note-level" in (review["verdicts"][m].get("root") or "").lower()]

    # ---- surface 2: section-level rows ----------------------------------------
    surface2 = []
    for mid, p in sorted(rejects.items()):
        srow = rows_by_id[mid]
        chunk_ord = srow["chunk"]["ordinal"]
        heading = srow["chunk"]["heading"]
        note_path = srow["note_path"]
        current = srow["spec_code"]
        tree_sec = note_path.split("/")[1].split("-")[0]  # "4-geometry-..." -> "4"
        name_text = heading + " " + (p.get("note") or "")
        cands = []
        for code, pt in points.items():
            if code == current:
                continue
            bare = code.split("-", 1)[1]
            wordings = [pt.get("official_wording") or ""]
            led = led_rows.get(bare)
            if led:
                wordings.append(led["foundation"]["text"])
            best, best_w = 0.0, ""
            for w in wordings:
                sc = score(name_text, w, bare.startswith(tree_sec + "."))
                if sc > best:
                    best, best_w = sc, w
            cands.append({"code": code, "score": best, "wording": best_w,
                          "in_c30_ledger": led is not None})
        cands.sort(key=lambda c: (-c["score"], c["code"]))
        surface2.append({
            "mapping_id": mid,
            "note_path": note_path,
            "chunk_ordinal": chunk_ord,
            "heading": heading,
            "current_code": current,
            "root": review["verdicts"][mid].get("root") or p.get("root"),
            "fill_note": (p.get("note") or "")[:400],
            "top_candidates": cands[:5],
        })

    # ---- surface 3: the H3 continuity inventory --------------------------------
    surface3 = []
    for mid, p in sorted(holds.items()):
        surface3.append({
            "mapping_id": mid, "spec_code": p.get("spec_code"),
            "note_path": p.get("note_path"),
            "chunk_ordinal": p.get("chunk_ordinal"),
            "heading": p.get("heading"),
            "convention_branch": p.get("convention_branch"),
            "disposition": ("rides a future round only with the operator's "
                            "explicit per-row sign-off (plus the convention "
                            "decision itself), or stays SUGGESTED — the R21 "
                            "disposition, unchanged"),
        })

    out = {
        "schema": "syllabai.c42-r22-repair-proposals/1.0",
        "task": "T-C42 / R22 (the sixth R1-shaped repair round, over the R21 "
                "3-row defect inventory)",
        "directive": DIRECTIVE,
        "method": ("0.5*difflib(name, wording) + 0.5*token-jaccard + 0.10 "
                   "section-prior, scored against BOTH tier wordings (store "
                   "operative + C30 ledger foundation.text where the code is a "
                   "shared-tier row, better-of-two recorded); name_text = chunk "
                   "heading + evidence note (surface 2); PROPOSAL-ONLY — binds "
                   "nothing; top-1 candidates are deliberately published as "
                   "noisy; PMT excluded as source; the operator verdict round "
                   "decides. Surface 1 is EMPTY this round (no note-level-class "
                   "root — all three note-level joins STAND on the R21 "
                   "evidence, so there is no id-level anchor and NO "
                   "resolution-file amendment). Surface 3 (the 4 H3 HOLD rows) "
                   "is LISTED not scored — they ride the STANDING convention "
                   "c42-heading-only-convention-1 with the R21 disposition "
                   "unchanged; see graph/reports/C42_R10_HEADING_ONLY_CONVENTION.md"),
        "store_context": ("the R5 §18 apply has landed (832 anchored rows "
                          "HUMAN_VALIDATED); the 3 REJECT rows stayed SUGGESTED "
                          "and are the only rows this round may concern — no "
                          "promoted row is in any repair surface"),
        "surface1_id_level": surface1,
        "surface2_section_level": surface2,
        "surface3_heading_only_h3_continuity": surface3,
        "residual": ("the C32 §3 residual stays KEPT UNRESOLVED per its R1 "
                     "adjudication (re-affirmed at R6, R10, R14, R18); the 82 "
                     "worklist rows stand as re-decided at R21 (82/82 DEFER)"),
    }
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    print(f"c42_r22_repair_proposals: WROTE {OUT.relative_to(REPO)} "
          f"(surface1={len(surface1)}, surface2={len(surface2)}, "
          f"H3-continuity={len(surface3)})")
    for row in surface2:
        top = row["top_candidates"][0] if row["top_candidates"] else None
        print(f"  {row['mapping_id']} {row['current_code']} ord "
              f"{row['chunk_ordinal']} — top-1(noisy): "
              f"{top['code'] if top else '-'} @ {top['score'] if top else '-'}")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
