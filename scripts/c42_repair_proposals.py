#!/usr/bin/env python3
"""c42_repair_proposals.py — T-C42 R1 deterministic PROPOSAL-ONLY scorer.

Generates, for the three R1 verdict surfaces, transparent candidate lists that
bind nothing (the C32 residual-scorer convention, generalized):

  surface 1 — the 45 id-level defective joins: candidates for the corrected
              code of each note's anchor, scored from the id's sme_name AND
              the note's own taught-content signal (its section headings in
              the chunk store) against the ratified 188 store wordings;
  surface 2 — the C32 residual anchor spcpt_QWXhzVp2S3VYZdZc: the notes-join
              artifact's recorded proposals, carried verbatim;
  surface 3 — the 16 section-level rows: candidates for the section chunk's
              true code, scored from the chunk's heading + evidence quote.

Scoring: 0.5*difflib(name, wording) + 0.5*token-jaccard(name, wording)
+ 0.10 section-prior when the note's corpus tree section matches the code's
spec section (the chemistry matcher's subsection boost). PMT is not a source;
nothing here resolves anything — the operator verdict round decides.

Writes graph/reports/C42_R1_REPAIR_PROPOSALS.json; prints a compact table.
"""
import difflib
import json
import re
import sys
import unicodedata
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "graph/reports/C42_R1_REPAIR_PROPOSALS.json"

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
    return {"score": round(0.5 * d + 0.5 * j + boost, 4),
            "difflib_ratio": round(d, 4), "token_overlap": round(j, 4),
            "section_prior_boost": boost}


def main() -> int:
    store = yaml.safe_load((REPO / "graph/igcse-maths-a/specification_points.yaml").read_text())
    points = store["specification_points"]
    chunks = yaml.safe_load((REPO / "graph/igcse-maths-a/spec_chunk_mappings.yaml").read_text())["rows"]
    verdicts = yaml.safe_load((REPO / "scripts/c40_maths_a_substrate_review_verdicts.yaml").read_text())["verdicts"]
    join = json.loads((REPO / "Official-Specifications/parsed/_derived/notes-join/"
                       "igcse-maths-a-18-higher.json").read_text())
    jrows = {r["note_path"]: r for r in join["joins"]}

    # per-note content signal: headings of ALL its chunks (anchored + worklist;
    # the 77 unmapped-SP worklist rows are SP-shaped and carry no note_path)
    note_headings = {}
    for r in chunks:
        if "note_path" not in r:
            continue
        note_headings.setdefault(r["note_path"], []).append(
            r.get("chunk", {}).get("heading") or r.get("evidence_quote") or "")

    def top_candidates(name_text: str, note_section: str | None, k: int = 3) -> list:
        scored = []
        for p in points:
            s = score(name_text, p["official_wording"], note_section, p["code"])
            scored.append({"code": p["code"], "wording": p["official_wording"],
                           "tier": (p.get("applicability") or {}).get("tier")
                           if isinstance(p.get("applicability"), dict) else None, **s})
        scored.sort(key=lambda x: -x["score"])
        return scored[:k]

    nl = [x for x in verdicts.values()
          if x["verdict"] == "REJECT" and x.get("root") == "note-level"]
    pairs = sorted(set((x["note_path"], x["spec_code"]) for x in nl))

    surface1 = []
    for np_, wrong in pairs:
        jr = jrows[np_]
        sec = np_.split("/notes/")[1].split("/")[0] if "/notes/" in np_ else None
        headings = [h for h in note_headings.get(np_, []) if h]
        name_text = jr["note_title"] + " " + " ".join(headings)
        surface1.append({
            "anchor_id": jr["anchor_id"], "note_path": np_, "note_title": jr["note_title"],
            "sme_name": jr["sme_name"], "wrong_code": wrong,
            "wrong_code_wording": next((p["official_wording"] for p in points if p["code"] == wrong), None),
            "note_headings": headings,
            "top_candidates": top_candidates(name_text, sec),
        })

    residual = {"anchor_id": "spcpt_QWXhzVp2S3VYZdZc",
                "recorded_proposals": join["unresolved"][0]["disposition_proposals"][0]["top_candidates"],
                "note_headings": note_headings.get(join["unresolved"][0]["note_path"], [])}

    sl = [x for x in verdicts.values()
          if x["verdict"] == "REJECT" and x.get("root") == "section-level"]
    seen, surface3 = set(), []
    for x in sorted(sl, key=lambda y: (y["note_path"], y["chunk_ordinal"])):
        key = (x["note_path"], x["chunk_ordinal"])
        if key in seen:
            continue
        seen.add(key)
        sec = x["note_path"].split("/notes/")[1].split("/")[0] if "/notes/" in x["note_path"] else None
        surface3.append({
            "note_path": x["note_path"], "chunk_ordinal": x["chunk_ordinal"],
            "heading": x["heading"], "current_code": x["spec_code"],
            "fill_note": x.get("note"),
            "top_candidates": top_candidates(x["heading"] + " " + (x.get("note") or ""), sec),
        })

    out = {
        "schema": "syllabai.c42-r1-repair-proposals/1.0",
        "task": "T-C42 / R1",
        "method": "0.5*difflib(name, wording) + 0.5*token-jaccard + 0.10 section-prior; "
                  "name_text = note title + the note's own chunk headings (surface 1) "
                  "or chunk heading + evidence note (surface 3); PROPOSAL-ONLY — binds nothing; "
                  "PMT excluded as source; the operator verdict round decides",
        "surface1_id_level": surface1,
        "surface2_residual": residual,
        "surface3_section_level": surface3,
    }
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")

    print(f"surface1: {len(surface1)} id-level rows | surface3: {len(surface3)} section rows")
    for s in surface1:
        c = s["top_candidates"][0]
        print(f"  {s['note_title'][:34]:34s} wrong={s['wrong_code']:10s} -> {c['code']:10s} "
              f"{c['score']:.3f} | {c['wording'][:52]}")
    print("  --- residual ---")
    for c in residual["recorded_proposals"][:3]:
        print(f"  residual -> {c['store_row_code']:10s} {c['score']:.3f} | {c['official_wording'][:52]}")
    print("proposals ->", OUT.relative_to(REPO))
    return 0


if __name__ == "__main__":
    sys.exit(main())
