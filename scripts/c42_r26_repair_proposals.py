#!/usr/bin/env python3
"""c42_r26_repair_proposals.py — T-C42 R26 deterministic PROPOSAL-ONLY scorer.

The R26 lane is the SEVENTH R1-shaped repair round of the C42 K2-B rework loop
(scope §7: "the rework lane repeats R1-shaped rounds only by explicit operator
instruction"), fired by the operator directive "(a) an R26-shaped repair over
the 4-row inventory" (2026-10-04, zai-web, gateway trace 1a10641c64283c99) —
option (a) of the R25 re-gate record's next-decision menu, named verbatim. It
runs over the R25 re-gate's defect inventory — the 4 fresh REJECT rows of
scripts/c42_r25_fresh_verdicts.yaml.

THE R26 NOVELTY — THE FIRST REPAIR ROUND OVER THE PROMOTED SURFACE: the R25
gate PASSED (exact 88/94 = 93.62% / partial 100% / none 100%, zero movement)
but its re-seeded draw surfaced 4 fresh REJECT rows, and ALL FOUR sit on the
R5-promoted 832-row HUMAN_VALIDATED surface (each pinned in
scripts/c42_r5_promotions.yaml with its then-code 2.2F / 1.1G / 5.1D / 3.3F).
Per the anti-forgery rule this round MOVES ZERO STORE BYTES; the adjudications
land only as next-re-build-facing records (the override map + a promotions
amendment, consumed fail-closed at the R28-shaped lane).

Surfaces (derived deterministically from the R25 fresh verdict record):
  surface 1 — the id-level rows (root is the note-level class): NONE this
              round. All 4 R25 REJECT roots are section-level scope
              differences (limit-scope / adjacent-surface classes) and all 4
              note-level joins STAND on the R25 evidence + this round's note
              censuses (types-of-number via its multiples/factors/primes ords;
              introduction-to-vectors via its add/subtract ords;
              drawing-straight-line-graphs via its ax+by=c ord and the
              conversion-graphs rows; factorising-by-grouping — see the
              verdict record's census remark for the honest scoping note) —
              so there is no id-level anchor to score and NO resolution-file
              amendment this round (the R14/R18/R22 shape).
  surface 2 — the section-level rows: 4 rows; candidates for the section
              chunk's true code scored from the chunk heading + the fresh
              verdict's own note against the ratified 188 — BOTH tier
              wordings (the R1 standing instruction): per candidate we score
              the store's operative wording AND the C30 tier-dedupe ledger's
              foundation.text (where the code is a shared-tier row) and rank
              by the better of the two, recording both. The row's CURRENT
              code is additionally scored and recorded separately (the R18
              absence-finding convention) — for the 2.2F grouping row the
              packet documents whether anything in the ratified 188 beats
              the row's own (rejected) code. PROPOSAL-ONLY — the top-1s are
              deliberately published as noisy (the R14/R18 scorer-artifact
              precedent); the operator verdict round decides.
  surface 3 — the heading-only class: the 4 H3 HOLD rows on the live store
              (1.7B / 6.3J / 3.3F / 2.2C — the R5-apply hold set, unchanged
              through R25) are LISTED as continuity inventory under the
              STANDING convention c42-heading-only-convention-1 — no scorer
              candidates, no new decision this round. They ride a future
              round only with the operator's explicit per-row sign-off (plus
              the convention decision itself), or stay SUGGESTED.
  residual  — continuity only: the C32 §3 residual stays KEPT UNRESOLVED per
              its R1 adjudication (re-affirmed at R6, R10, R14, R18, R22);
              no new scoring.

Scoring: 0.5*difflib(name, wording) + 0.5*token-jaccard(name, wording)
+ 0.10 section-prior when the note's corpus tree section matches the code's
spec section (the C32 residual-scorer convention, unchanged). PMT is not a
source; top-1 candidates are deliberately published as noisy — they bound
nothing; the operator verdict round decides.

Writes graph/reports/C42_R26_REPAIR_PROPOSALS.json; prints a compact table.
"""
import difflib
import json
import re
import unicodedata
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "graph/reports/C42_R26_REPAIR_PROPOSALS.json"
R25_FRESH = REPO / "scripts/c42_r25_fresh_verdicts.yaml"
STORE = REPO / "graph/igcse-maths-a/spec_chunk_mappings.yaml"
REGISTRY = REPO / "graph/igcse-maths-a/specification_points.yaml"
LEDGER = REPO / "graph/reports/C30_MATHS_A_TIER_DEDUPE_LEDGER.json"
PROMOTIONS = REPO / "scripts/c42_r5_promotions.yaml"
DIRECTIVE = ("(a) an R26-shaped repair over the 4-row inventory "
             "(2026-10-04, zai-web, gateway trace 1a10641c64283c99)")

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
    fresh = yaml.safe_load(R25_FRESH.read_text(encoding="utf-8"))
    store = yaml.safe_load(STORE.read_text(encoding="utf-8"))
    reg = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    points = {p["code"]: p for p in reg["specification_points"]}
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    led_rows = {r["official_code"]: r for r in ledger["rows"]}
    promo = yaml.safe_load(PROMOTIONS.read_text(encoding="utf-8"))
    promo_pins = {e["row"]["mapping_id"]: e["row"] for e in promo["promotions"]}

    verdicts = fresh["verdicts"]
    rejects = {m: p for m, p in verdicts.items() if p.get("verdict") == "REJECT"}
    rows_by_id = {r["mapping_id"]: r for r in store["rows"]}

    # ---- surface 1: id-level (note-level-class roots) ------------------------
    # The R25 review record's root fields are pointers ("recorded in note");
    # the class evidence is the fresh verdicts' own notes. None of the 4 is
    # the id-level class (a note-level join defect) — all 4 are section-level
    # scope differences. Asserted here, fail-closed, from the fresh notes.
    surface1 = [m for m in sorted(rejects)
                if "note-level" in (rejects[m].get("note") or "").lower()]

    # ---- surface 2: section-level rows ----------------------------------------
    surface2 = []
    for mid, p in sorted(rejects.items()):
        srow = rows_by_id[mid]
        chunk_ord = srow["chunk"]["ordinal"]
        heading = srow["chunk"]["heading"]
        note_path = srow["note_path"]
        current = srow["spec_code"]
        pin = promo_pins.get(mid)
        if pin is None:
            raise SystemExit(f"FAIL-CLOSED: {mid} is not a promoted row — the "
                             "R26 inventory is expected to sit on the R5 "
                             "promoted surface")
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
        # the R18 absence-finding convention: score the row's own code too
        cur_bare = current.split("-", 1)[1]
        cur_wordings = [points[current].get("official_wording") or ""]
        cur_led = led_rows.get(cur_bare)
        if cur_led:
            cur_wordings.append(cur_led["foundation"]["text"])
        cur_best, cur_w = 0.0, ""
        for w in cur_wordings:
            sc = score(name_text, w, cur_bare.startswith(tree_sec + "."))
            if sc > cur_best:
                cur_best, cur_w = sc, w
        top_excl = cands[0]["code"] if cands else None
        top_incl = max([(cur_best, current), (cands[0]["score"], cands[0]["code"])]
                       if cands else [(cur_best, current)])[1]
        surface2.append({
            "mapping_id": mid,
            "note_path": note_path,
            "chunk_ordinal": chunk_ord,
            "heading": heading,
            "current_code": current,
            "promoted_pin_code": pin.get("spec_code"),
            "promoted_pin_matches_store": pin.get("spec_code") == current,
            "root": (p.get("note") or "")[:400],
            "top_candidates_excluding_current": cands[:5],
            "current_code_score": {"code": current, "score": cur_best,
                                   "wording": cur_w},
            "top1_including_current": {"code": top_incl},
            "top1_excluding_current": {"code": top_excl},
        })

    # ---- surface 3: the H3 continuity inventory (the live store hold set) ------
    h3_ids = ["1dfc65df88b35d69", "2d44bcf00f589c18",
              "91a5080f8b390de6", "56905a113334dcd1"]
    surface3 = []
    for mid in h3_ids:
        r = rows_by_id[mid]
        surface3.append({
            "mapping_id": mid,
            "spec_code": r.get("spec_code"),
            "note_path": r.get("note_path"),
            "chunk_ordinal": (r.get("chunk") or {}).get("ordinal"),
            "heading": (r.get("chunk") or {}).get("heading"),
            "validation_status": r.get("validation_status"),
            "disposition": ("rides a future round only with the operator's "
                            "explicit per-row sign-off (plus the convention "
                            "decision itself), or stays SUGGESTED — the R21 "
                            "disposition, unchanged through R25"),
        })

    out = {
        "schema": "syllabai.c42-r26-repair-proposals/1.0",
        "task": "T-C42 / R26 (the seventh R1-shaped repair round, over the "
                "R25 4-row defect inventory — the FIRST over the promoted "
                "surface)",
        "directive": DIRECTIVE,
        "method": ("0.5*difflib(name, wording) + 0.5*token-jaccard + 0.10 "
                   "section-prior, scored against BOTH tier wordings (store "
                   "operative + C30 ledger foundation.text where the code is "
                   "a shared-tier row, better-of-two recorded); name_text = "
                   "chunk heading + evidence note (surface 2); the current "
                   "code is scored and recorded separately per the R18 "
                   "absence-finding convention; PROPOSAL-ONLY — binds "
                   "nothing; top-1 candidates are deliberately published as "
                   "noisy; PMT excluded as source; the operator verdict "
                   "round decides. Surface 1 is EMPTY this round (no "
                   "note-level-class root — all four note-level joins STAND, "
                   "so there is no id-level anchor and NO resolution-file "
                   "amendment). Surface 3 (the 4 H3 HOLD rows) is LISTED not "
                   "scored — they ride the STANDING convention "
                   "c42-heading-only-convention-1 with the R21 disposition "
                   "unchanged; see graph/reports/C42_R10_HEADING_ONLY_CONVENTION.md"),
        "store_context": ("the R5 §18 apply has landed and was re-applied "
                          "byte-stably at R24 (832 anchored rows "
                          "HUMAN_VALIDATED, sha16 9bad739bd79e5899); ALL 4 "
                          "R25 REJECT rows sit on that promoted surface "
                          "(pinned with their then-codes) — this round moves "
                          "ZERO store bytes; the adjudications land as "
                          "next-re-build-facing records (the override map "
                          "scripts/c42_section_overrides_r26.yaml + the "
                          "promotions amendment "
                          "scripts/c42_r26_promotions_amendment.yaml) "
                          "consumed fail-closed at the R28-shaped lane"),
        "surface1_id_level": surface1,
        "surface2_section_level": surface2,
        "surface3_heading_only_h3_continuity": surface3,
        "residual": ("the C32 §3 residual stays KEPT UNRESOLVED per its R1 "
                     "adjudication (re-affirmed at R6, R10, R14, R18, R22); "
                     "the 81 worklist rows stand as re-decided at R25 (81/81 "
                     "DEFER)"),
    }
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    print(f"c42_r26_repair_proposals: WROTE {OUT.relative_to(REPO)} "
          f"(surface1={len(surface1)}, surface2={len(surface2)}, "
          f"H3-continuity={len(surface3)})")
    for row in surface2:
        t1 = row["top1_excluding_current"]["code"]
        t1s = (row["top_candidates_excluding_current"] or [{}])[0].get("score")
        cur = row["current_code_score"]
        print(f"  {row['mapping_id']} {row['current_code']} ord "
              f"{row['chunk_ordinal']} — top-1 excl (noisy): {t1} @ {t1s} | "
              f"current scored: {cur['code']} @ {cur['score']}")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
