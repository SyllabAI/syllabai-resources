#!/usr/bin/env python3
"""c42_r6_repair_proposals.py — T-C42 R6 deterministic PROPOSAL-ONLY scorer.

The R6 lane is the SECOND R1-shaped verdict round of the C42 K2-B rework loop
(scope §7: "the rework lane repeats R1-shaped rounds only by explicit operator
instruction"), fired by the operator directive "R1-shaped verdict round over
this inventory (then R2/R3/R4 re-run)" (2026-10-02, zai-web) over the R4
re-gate's defect inventory (19 reject rows in scripts/c42_r4_fresh_verdicts.yaml).

Surfaces (derived deterministically from the R4 fresh verdict record):
  surface 1 — the id-level rows (root in {note-level, note-level-class}):
              15 reject rows -> 10 distinct anchors; candidates for the
              corrected code of each note's anchor, scored from the note title
              AND the note's own taught-content signal (its chunk headings)
              against the ratified 188 — BOTH tier wordings (the R1 standing
              instruction): per candidate we score the store's operative
              wording AND the C30 tier-dedupe ledger's foundation.text and
              rank by the better of the two, recording both.
  surface 3 — the section-level rows (root == section-level): 4 rows;
              candidates for the section chunk's true code scored from the
              chunk heading + the fill's own note. The two EXTENSION rows
              (area ord 6, basic-fractions ord 2 — heading-verbatim surfaces
              recorded alongside verdicted siblings, transparently labeled)
              are scored the same way for reviewability.
  residual  — continuity only: the C32 §3 residual stays KEPT UNRESOLVED per
              its R1 adjudication; no new scoring.

Scoring: 0.5*difflib(name, wording) + 0.5*token-jaccard(name, wording)
+ 0.10 section-prior when the note's corpus tree section matches the code's
spec section (the C32 residual-scorer convention, unchanged). PMT is not a
source; top-1 candidates are deliberately published as noisy — they bound
nothing; the operator verdict round decides.

Writes graph/reports/C42_R6_REPAIR_PROPOSALS.json; prints a compact table.
"""
import difflib
import json
import re
import sys
import unicodedata
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "graph/reports/C42_R6_REPAIR_PROPOSALS.json"
R4_FRESH = REPO / "scripts/c42_r4_fresh_verdicts.yaml"

STOP = {"the", "a", "an", "of", "and", "to", "in", "use", "uses", "using",
        "find", "understand", "understanding", "for", "with", "on", "from",
        "how", "do", "i", "what", "is", "are", "their", "your", "it", "s"}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFC", str(s)).lower()
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def toks(s: str):
    return {t for t in norm(s).split() if t not in STOP and len(t) > 1}


def score(name_text: str, wording: str, note_section: str | None, code: str) -> dict:
    nn, wn = norm(name_text), norm(wording)
    nt, wt = toks(name_text), toks(wording)
    d = difflib.SequenceMatcher(None, nn, wn).ratio()
    j = len(nt & wt) / len(nt | wt) if (nt | wt) else 0.0
    boost = 0.0
    if note_section and note_section[0].isdigit() and code.split("-")[1].split(".")[0] == note_section[0]:
        boost = 0.10
    return {"difflib_ratio": round(d, 4), "token_overlap": round(j, 4),
            "section_prior_boost": boost}


def both_tier_candidates(name_text, note_section, points, ledger, k=3):
    """Score every 188 code against BOTH the store wording and the ledger
    foundation.text; rank by the better score; record both."""
    scored = []
    for p in points:
        s_store = score(name_text, p["official_wording"], note_section, p["code"])
        led = ledger.get(p["code"].split("-", 1)[1])
        s_led = score(name_text, led["foundation"]["text"], note_section, p["code"]) if led else None
        best = max(s_store["difflib_ratio"] * 0.5 + s_store["token_overlap"] * 0.5 + s_store["section_prior_boost"],
                   (s_led["difflib_ratio"] * 0.5 + s_led["token_overlap"] * 0.5 + s_led["section_prior_boost"])
                   if s_led else -1.0)
        scored.append({"code": p["code"],
                       "wording_store": p["official_wording"],
                       "wording_ledger": led["foundation"]["text"] if led else None,
                       "score": round(best, 4),
                       "score_store": round(s_store["difflib_ratio"] * 0.5 + s_store["token_overlap"] * 0.5
                                            + s_store["section_prior_boost"], 4),
                       "score_ledger": round(s_led["difflib_ratio"] * 0.5 + s_led["token_overlap"] * 0.5
                                             + s_led["section_prior_boost"], 4) if s_led else None,
                       "tier": (p.get("applicability") or {}).get("tier")
                       if isinstance(p.get("applicability"), dict) else None})
    scored.sort(key=lambda x: -x["score"])
    return scored[:k]


def main() -> int:
    store = yaml.safe_load((REPO / "graph/igcse-maths-a/specification_points.yaml").read_text())
    points = store["specification_points"]
    ledger = {r["official_code"]: r for r in json.loads(
        (REPO / "graph/reports/C30_MATHS_A_TIER_DEDUPE_LEDGER.json").read_text())["rows"]}
    chunks = yaml.safe_load((REPO / "graph/igcse-maths-a/spec_chunk_mappings.yaml").read_text())["rows"]
    fresh = yaml.safe_load(R4_FRESH.read_text())["verdicts"]
    join = json.loads((REPO / "Official-Specifications/parsed/_derived/notes-join/"
                       "igcse-maths-a-18-higher.json").read_text())
    jrows = {r["note_path"]: r for r in join["joins"]}

    note_headings = {}
    for r in chunks:
        if "note_path" not in r:
            continue
        note_headings.setdefault(r["note_path"], []).append(
            r.get("chunk", {}).get("heading") or r.get("evidence_quote") or "")

    def sec_of(np_):
        return np_.split("/notes/")[1].split("/")[0] if "/notes/" in np_ else None

    # surface 1: the id-level surface, derived from the R4 fresh roots
    anchors, rows_per_anchor = {}, {}
    for x in fresh.values():
        if x["verdict"] == "REJECT" and x.get("root") in ("note-level", "note-level-class"):
            jr = jrows[x["note_path"]]
            anchors.setdefault(jr["anchor_id"], x["note_path"])
            rows_per_anchor[jr["anchor_id"]] = rows_per_anchor.get(jr["anchor_id"], 0) + 1
    surface1 = []
    for aid, np_ in sorted(anchors.items()):
        jr = jrows[np_]
        headings = [h for h in note_headings.get(np_, []) if h]
        name_text = jr["note_title"] + " " + " ".join(headings)
        surface1.append({
            "anchor_id": aid, "note_path": np_, "note_title": jr["note_title"],
            "sme_name": jr["sme_name"], "wrong_code": jr["store_row_code"],
            "wrong_code_wording": jr["official_wording"],
            "r4_reject_rows": rows_per_anchor[aid],
            "note_headings": headings,
            "top_candidates": both_tier_candidates(name_text, sec_of(np_), points, ledger),
        })

    # surface 3: the 4 verdicted section rows + the 2 extension rows
    sl, seen, surface3 = [], set(), []
    for x in sorted(fresh.values(), key=lambda y: (y["note_path"], y["chunk_ordinal"])):
        if x["verdict"] == "REJECT" and x.get("root") == "section-level":
            key = (x["note_path"], x["chunk_ordinal"])
            if key not in seen:
                seen.add(key)
                sl.append({"note_path": x["note_path"], "chunk_ordinal": x["chunk_ordinal"],
                           "heading": x["chunk_heading"], "current_code": x["spec_code"],
                           "fill_note": x.get("note"), "extension": False})
    sl.append({"note_path": "notes/4-geometry-and-trigonometry/area-and-perimeter/area.json",
               "chunk_ordinal": 6, "heading": "How do I find the area of a trapezium?",
               "current_code": "4MA1-4.8E", "fill_note": "EXTENSION row: heading-verbatim 4.9D surface "
               "(trapezia), recorded alongside the R4-verdicted ord-7 parallelogram sibling",
               "extension": True})
    sl.append({"note_path": "notes/1-numbers-and-the-number-system/fractions/basic-fractions.json",
               "chunk_ordinal": 2, "heading": "How do I find a fraction of an amount?",
               "current_code": "4MA1-1.2I", "fill_note": "EXTENSION row: heading-verbatim 1.2D surface "
               "(fraction of a given quantity), recorded under the R6 note-level repair",
               "extension": True})
    for x in sl:
        name_text = x["heading"] + " " + (x["fill_note"] or "")
        surface3.append({**x,
                         "top_candidates": both_tier_candidates(name_text, sec_of(x["note_path"]),
                                                                points, ledger)})

    out = {
        "schema": "syllabai.c42-r6-repair-proposals/1.0",
        "task": "T-C42 / R6 (the second R1-shaped verdict round, over the R4 defect inventory)",
        "directive": "R1-shaped verdict round over this inventory (then R2/R3/R4 re-run) "
                     "(2026-10-02, zai-web)",
        "method": "0.5*difflib(name, wording) + 0.5*token-jaccard + 0.10 section-prior, scored "
                  "against BOTH tier wordings (store operative + C30 ledger foundation.text, "
                  "better-of-two recorded); name_text = note title + the note's own chunk headings "
                  "(surface 1) or chunk heading + evidence note (surface 3); PROPOSAL-ONLY — binds "
                  "nothing; top-1 candidates are deliberately published as noisy; PMT excluded as "
                  "source; the operator verdict round decides",
        "surface1_id_level": surface1,
        "surface3_section_level": surface3,
        "residual": {"anchor_id": "spcpt_QWXhzVp2S3VYZdZc",
                     "disposition": "KEPT UNRESOLVED — continuity from the R1 adjudication; "
                                    "the PDF-verified reason stands; no new scoring"},
    }
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")

    print(f"surface1: {len(surface1)} id-level rows | surface3: {len(surface3)} section rows "
          f"({sum(1 for x in surface3 if x['extension'])} extension)")
    for s in surface1:
        c = s["top_candidates"][0]
        print(f"  {s['note_title'][:30]:30s} wrong={s['wrong_code']:10s} -> {c['code']:10s} "
              f"{c['score']:.3f} | {c['wording_store'][:48]}")
    print("  --- surface 3 ---")
    for s in surface3:
        c = s["top_candidates"][0]
        tag = "EXT" if s["extension"] else "   "
        print(f"  {tag} {s['note_path'].split('/')[-1][:28]:28s} ord {s['chunk_ordinal']} "
              f"cur={s['current_code']:10s} -> {c['code']:10s} {c['score']:.3f}")
    print("proposals ->", OUT.relative_to(REPO))
    return 0


if __name__ == "__main__":
    sys.exit(main())
