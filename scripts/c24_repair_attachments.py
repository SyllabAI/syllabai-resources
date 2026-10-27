#!/usr/bin/env python3
"""T-C24 WS-1 — geometric re-attachment repair for parsed specification JSONs.

Root cause (T-C23 Task B, 630 subsection-attachment-impossible findings):
  parse_code_column_bands() finalizes every statement with the PAGE-FINAL
  header context instead of the context at capture; parse_lettered_table()
  (economics) is whole-DOCUMENT-final (94/108 statements claimed the last
  subtopic of the document). maths-a/modular findings are same-line float
  artifacts (hdr <1pt below stmt) -> tolerance, no change.

Repair rule (deterministic, zero-LLM — simulates snapshot-at-capture):
  attach each statement to the LAST topic header and the LAST subsection
  header whose (page, oy) is at-or-above the statement's (page, oy),
  tolerance TOL pt on the same page; a topic header at-or-above that is
  LATER than the subsection header resets the subsection context.

Geometry source: the raw <stem>.parsed.json header tables (the walk's own
snapshots — they carry oy; the canonical topics.json subsection rows have
dropped it). Ref dicts are projected onto the key-shape already used by
each subject's existing statement refs; subjects whose statements carry
no subsection refs (e.g. ial-physics bare_int) are not invented.

Changes ONLY per-record 'topic'/'subsection' refs in <stem>.parsed.json
and canonical spec_points.json. Everything else byte-preserved. Ledger:
kg_audit/c24/repair_ledger.json. Fail-closed per subject.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PARSED = REPO / "Official-Specifications/parsed"
OUTDIR = Path("/home/z/my-project/kg_audit/c24")
TOL = 6.0  # pt; same-line artifact threshold

SUBJECTS = [
    "igcse-chemistry", "igcse-biology", "igcse-physics",
    "igcse-science-double-award", "igcse-chemistry-modular",
    "igcse-biology-modular", "igcse-physics-modular",
    "ial-biology", "ial-chemistry", "ial-maths", "ial-physics",
    "igcse-economics", "igcse-business", "igcse-ict",
    "igcse-geography", "igcse-accounting", "igcse-english-literature",
    "igcse-further-maths", "igcse-maths-a", "igcse-maths-a-modular",
]

# Repair modes:
#   impossible-only — page-final bug families (bands / heading_bullets):
#     a ref is rewritten IFF it is geometrically impossible (header prints
#     below the statement, beyond TOL). Refs are never invented; a None ref
#     stays None unless it is geometrically impossible (never).
#   recompute-all   — whole-document-final bug families (lettered_table,
#     triplet_table): every ref is recomputed from geometry; the bug taints
#     even geometrically-possible attachments (a nearer header may exist).
MODES = {
    "impossible-only": [
        "igcse-chemistry", "igcse-biology", "igcse-physics",
        "igcse-science-double-award", "igcse-chemistry-modular",
        "igcse-biology-modular", "igcse-physics-modular",
        "ial-biology", "ial-chemistry", "ial-maths",
        "igcse-geography", "igcse-accounting",
    ],
    "recompute-all": [
        "igcse-economics", "igcse-business", "igcse-ict",
    ],
    "verify-only": [
        "ial-physics", "igcse-english-literature", "igcse-further-maths",
        "igcse-maths-a", "igcse-maths-a-modular",
    ],
}


def raw_tables(q: str):
    """(topics, subsecs) with page+oy from the raw parse snapshots."""
    topics, subsecs = [], []
    for pj in sorted((PARSED / q).glob("*.parsed.json")):
        d = json.loads(pj.read_text(encoding="utf-8"))
        for t in d.get("topics") or []:
            if t.get("page") is None:
                continue
            topics.append({"number": t.get("number"), "title": t.get("title"),
                           "page": t["page"], "oy": t.get("oy") or 0.0})
        for s in d.get("subsections") or []:
            page = s.get("page")
            if page is None:
                continue
            subsecs.append({"code": s.get("code"), "letter": s.get("letter"),
                            "title": s.get("title"), "page": page,
                            "oy": s.get("oy") or 0.0})
    return topics, subsecs


def at_or_above(headers, page, oy):
    best = None
    for h in headers:  # headers sorted by (page, oy)
        if h["page"] < page or (h["page"] == page and h["oy"] <= oy + TOL):
            best = h
        else:
            break
    return best


def attach(topics, subsecs, page, oy):
    top = at_or_above(topics, page, oy)
    sub = at_or_above(subsecs, page, oy)
    if sub and top and (top["page"], top["oy"]) > (sub["page"], sub["oy"]):
        sub = None  # chapter restart after the last subsection header
    return top, sub


def project(ref_shape, header, none_default=None):
    """Project a table header onto the family's existing ref key-shape."""
    if not ref_shape:            # family carries no refs of this kind
        return none_default
    out = {}
    for k in ref_shape:
        v = header.get(k)
        if v is None:
            v = 0 if k == "oy" else ""
        out[k] = round(v) if k == "oy" and isinstance(v, float) else v
    return out


def same(a, b):
    return json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True)


def ref_shape(recs, field):
    shapes = set()
    for r in recs:
        v = r.get(field)
        if isinstance(v, dict):
            shapes.add(tuple(sorted(v.keys())))
    if len(shapes) == 1:
        return list(next(iter(shapes)))
    if len(shapes) == 0:
        return None
    raise ValueError(f"mixed ref shapes for {field}: {shapes}")


def impossible(ref, page, oy):
    """True when the attached header prints strictly below the statement."""
    if not isinstance(ref, dict):
        return False
    hp = ref.get("page")
    if hp is None:
        return False
    hy = ref.get("oy") or 0.0
    return (hp, hy) > (page, (oy or 0.0) + TOL)


def repair_subject(q: str, ledger: dict, apply: bool) -> int:
    sp_path = PARSED / q / "spec_points.json"
    if not sp_path.exists():
        return 0
    mode = next((m for m, qs in MODES.items() if q in qs), "verify-only")
    topics, subsecs = raw_tables(q)
    topics.sort(key=lambda h: (h["page"], h["oy"]))
    subsecs.sort(key=lambda h: (h["page"], h["oy"]))
    raw = sp_path.read_text(encoding="utf-8")
    doc = json.loads(raw)
    recs = doc["spec_points"]
    t_shape = ref_shape(recs, "topic")
    s_shape = ref_shape(recs, "subsection")
    changes = []
    for rec in recs:
        pr = rec.get("provenance") or {}
        page, oy = pr.get("page"), pr.get("oy")
        if page is None:
            continue
        old_topic, old_sub = rec.get("topic"), rec.get("subsection")
        if mode == "verify-only":
            continue
        if mode == "impossible-only":
            need_t = impossible(old_topic, page, oy)
            need_s = impossible(old_sub, page, oy)
            if not need_t and not need_s:
                continue
        top, sub = attach(topics, subsecs, page, oy)
        new_topic = project(t_shape, top) if (top and t_shape) else None
        new_sub = project(s_shape, sub) if (sub and s_shape) else None
        if same(old_topic, new_topic) and same(old_sub, new_sub):
            continue
        changes.append({
            "id": rec.get("id"), "official_code": rec.get("official_code"),
            "page": page, "oy": oy,
            "old_topic": old_topic, "new_topic": new_topic,
            "old_subsection": old_sub, "new_subsection": new_sub,
        })
        if apply:
            rec["topic"] = new_topic
            rec["subsection"] = new_sub
    ledger[q] = {
        "mode": mode,
        "spec_points": len(recs),
        "headers": {"topics": len(topics), "subsections": len(subsecs)},
        "ref_shapes": {"topic": t_shape, "subsection": s_shape},
        "changed": len(changes), "changes": changes,
        "status": "REPAIRED" if apply else "DRY",
    }
    if apply and changes:
        txt = json.dumps(doc, indent=1, ensure_ascii=False)
        if raw.endswith("\n") and not txt.endswith("\n"):
            txt += "\n"
        sp_path.write_text(txt, encoding="utf-8")
    return len(changes)


def main() -> int:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    apply = "--apply" in sys.argv
    only = [a for a in sys.argv[1:] if not a.startswith("--")]
    subjects = only or SUBJECTS
    ledger = {}
    total = 0
    for q in subjects:
        try:
            n = repair_subject(q, ledger, apply)
            total += n
            print(f"{q:32s} changed={n:4d}")
        except Exception as e:
            ledger[q] = {"status": "FAILED", "error": f"{type(e).__name__}: {e}"}
            print(f"{q:32s} FAILED {type(e).__name__}: {e}")
    out = OUTDIR / "repair_ledger.json"
    out.write_text(json.dumps(ledger, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"total changed: {total}  (apply={apply})  ledger -> {out}")
    return 0 if all(v.get("status") != "FAILED" for v in ledger.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
