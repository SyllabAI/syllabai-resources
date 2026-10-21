#!/usr/bin/env python3
"""
T-SPECS-CIE-TRANCHE2-CHEM25-SHEET-1 — the per-bank name-phrase verdict REVIEW
SHEET generator (tranche-2 round-1, head bank cie-a-level-chemistry-25).

The anchor-gap census receipt's tranche-2 program: "the 16,335-part name-phrase
verdict program per bank ... tier laws unchanged (operator_verdict
authoritative; T2_near non-authoritative; never guessed)". This lane's
substrate is NAME-ONLY (255/256 pending spcpt entities carry a name record,
zero carry a definition — the rejoin's identity-grade rules J1-J4 are
exhausted on this pool), so the honest mass instrument is the OPERATOR REVIEW
SHEET (the c11 batch pattern: the lane assembles verbatim evidence + scoped
candidates; the operator rules; a later lane encodes the verdicts as
operator_verdict rows and the chain lands them).

Per pending spcpt entity (the join unit — 1,336 pending question_parts share
256 distinct pending entities in this lane):
  - the verbatim SME name + subtopic scope (the corpus's own placement)
  - the evidence class:
      J4_residue        — the name phrase token-bounded-hits exactly one
                          official point text lane-wide (identity-grade;
                          flagged for the operator's eye — the hit may be a
                          substring of an unrelated statement)
      multi_hit         — the phrase hits several official points (the
                          rejoin's quarantine class); the section-scoped hit
                          set is shown where narrower
      declared_link     — the entity's home note already carries
                          authoritative codes (a candidate inheritance, the
                          weakest of-record class — operator discretion)
      record_less       — no corpus record (upstream coverage gap)
      no_match          — no identity-grade evidence (the operator's
                          semantic ruling is the only honest path)
  - the scoped official candidates: the parsed spec points of the entity's
    own section scope, verbatim statement texts
  - the ruling field (PENDING — operator-owned)

Read-only on the corpora; writes the sheet yaml + the markdown rendering.
"""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
SL = REPO / "spec-links"
REPORTS = REPO / "graph" / "reports"

LANE = "cie-a-level-chemistry-25"
SHEET_YAML = REPO / "scripts" / "cie_tranche2_chem25_review_sheet.yaml"
SHEET_MD = REPORTS / "T_SPECS_CIE_TRANCHE2_CHEM25_SHEET.md"


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


def main() -> int:
    side = json.loads((SL / f"{LANE}.json").read_text())
    idx = json.loads((REPO / "SME-ExamQuestion" / LANE / "spec_point_index.json").read_text())
    sp = idx.get("spec_points") or {}
    items = side["items"]

    # the lane's parsed registry
    man = json.loads((REPO / "Official-Specifications" / "manifest.json").read_text())
    qual = side["registry"]["id"]
    pts = None
    for q in man["qualifications"]:
        if q["slug"] == qual:
            pdf = Path(q["pdf"]).stem
            reg = json.loads((REPO / "Official-Specifications" / "parsed" / qual / f"{pdf}.parsed.json").read_text())
            pts = reg["spec_points"]
    if pts is None:
        raise SystemExit(f"qual {qual} not found")

    uni = [(p, tokens(p.get("text") or "")) for p in pts]

    # pending pool (question_part items with codes == []), post-tranche-2-r1
    pend_parts = []
    sids = defaultdict(lambda: {"parts": [], "sections": set(), "notes": set()})
    for iid, it in items.items():
        if not isinstance(it, dict) or it.get("kind") != "question_part":
            continue
        if it.get("codes"):
            continue
        pend_parts.append(iid)
        for sid in it.get("pending") or []:
            sids[sid]["parts"].append(iid)
            sids[sid]["sections"].add(it.get("section"))
    # note refs per sid (coded or pending notes referencing the entity)
    for iid, it in items.items():
        if not isinstance(it, dict) or it.get("kind") != "note":
            continue
        for sid in it.get("pending") or []:
            if sid in sids:
                sids[sid]["notes"].add((iid, bool(it.get("codes"))))

    # coded home notes (the declared_link candidates)
    coded_notes = {iid: [c.get("official_code") for c in (it.get("codes") or [])]
                   for iid, it in items.items()
                   if isinstance(it, dict) and it.get("kind") == "note" and it.get("codes")}

    rows = []
    cls_census = defaultdict(int)
    for sid in sorted(sids):
        r = sp.get(sid) or {}
        name = (r.get("name") or "").strip()
        subs = r.get("subtopic_slugs") or []
        home_notes = [n for n in (r.get("notes") or [])]
        info = sids[sid]
        sections = sorted(s for s in info["sections"] if s)

        # evidence class
        cls = "no_match"
        hits_wide = phrase_hits(tokens(name), uni) if name else []
        if not name and not (r.get("definition") or "").strip():
            cls = "record_less"
        elif len(hits_wide) == 1:
            cls = "J4_residue"
        elif len(hits_wide) > 1:
            cls = "multi_hit"
        else:
            # declared-link candidate: any home note (or referencing note) coded
            for nid in home_notes:
                if nid in coded_notes:
                    cls = "declared_link"
                    break
            if cls == "no_match":
                for nid, coded in info["notes"]:
                    if coded:
                        cls = "declared_link"
                        break

        # scoped candidates: the official points of the entity's first section topic
        cands = []
        if sections:
            m = re.match(r"(\d+)-", sections[0])
            if m:
                tno = m.group(1)
                cands = [{"code": p.get("official_code"),
                          "id": p.get("id"),
                          "text": (p.get("text") or "").strip()}
                         for p in pts
                         if (p.get("id") or "").split(":")[-1].startswith(tno + ".")]

        rows.append({
            "sid": sid,
            "sme_name": name,
            "sme_definition": (r.get("definition") or "").strip(),
            "subtopic_slugs": subs,
            "sections": sections,
            "pending_parts": len(info["parts"]),
            "part_refs": info["parts"],
            "note_refs": sorted({n for n, _ in info["notes"]}),
            "home_notes": home_notes,
            "cls": cls,
            "wide_phrase_hits": [p.get("official_code") for p in hits_wide],
            "scoped_candidates": cands,
            "declared_note_codes": (coded_notes.get(home_notes[0])
                                    if home_notes and home_notes[0] in coded_notes else None),
            "ruling": "PENDING",
        })
        cls_census[cls] += 1

    sheet = {
        "lane": "T-SPECS-CIE-TRANCHE2-CHEM25-SHEET-1",
        "generated_utc": "2026-10-22T05:40:00Z",
        "bank": LANE,
        "directive": ("operator order 'Tranche-2' (gateway trace 1a15f8160e677949, "
                      "2026-10-22, zai-web) — the name-phrase verdict program, "
                      "head bank of the census receipt's mass order"),
        "law": ("operator_verdict is the only authoritative class for the "
                "no-match pool (ADR-030 + AGENT.md rule 3: no semantic-similarity "
                "manufacturing); the lane assembles verbatim evidence and scoped "
                "candidates; the operator rules per sid; a later lane encodes "
                "the rulings as operator_verdict rows and the chain lands them"),
        "pool": {
            "pending_parts": len(pend_parts),
            "distinct_pending_sids": len(rows),
            "class_census": dict(sorted(cls_census.items())),
            "official_points_in_scope": len(pts),
        },
        "rows": rows,
    }
    SHEET_YAML.write_text(yaml.safe_dump(sheet, sort_keys=False, allow_unicode=True, width=110))

    # markdown rendering (the operator's reading surface)
    lines = [
        f"# T-SPECS-CIE-TRANCHE2-CHEM25-SHEET-1 — {LANE} operator review sheet",
        "",
        f"- Pool: {len(pend_parts)} pending question parts / {len(rows)} distinct pending spcpt entities",
        f"- Class census: {dict(sorted(cls_census.items()))}",
        "- Law: the operator rules per sid (the lane never invents; ADR-030, AGENT.md rule 3). "
        "The scoped candidates are the parsed spec points of the entity's own section; "
        "the ruling names one or more official codes (or QUARANTINE).",
        "",
    ]
    for section in sorted({s for r in rows for s in r["sections"]}):
        block = [r for r in rows if section in r["sections"]]
        lines.append(f"## {section} — {len(block)} entities")
        for r in sorted(block, key=lambda x: -x["pending_parts"]):
            lines.append(f"### {r['sid']} [{r['cls']}] parts={r['pending_parts']}")
            lines.append(f"- SME name: {r['sme_name']!r}")
            if r["wide_phrase_hits"]:
                lines.append(f"- phrase hits: {r['wide_phrase_hits']}")
            if r["declared_note_codes"]:
                lines.append(f"- declared home-note codes: {r['declared_note_codes']}")
            lines.append(f"- ruling: **{r['ruling']}**")
            lines.append("")
    SHEET_MD.write_text("\n".join(lines) + "\n")

    print(f"sheet written: {SHEET_YAML.name} + {SHEET_MD.name}")
    print(f"  pool: {len(pend_parts)} parts / {len(rows)} sids; classes: {dict(sorted(cls_census.items()))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
