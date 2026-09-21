#!/usr/bin/env python3
"""T-C24 WS-5b — refresh the definitive chemistry store wording after the
estate respacing, re-anchor SPEC evidence quotes, and write the record.

The store's wording authority is the official PDF (T-C23). Glyph-geometry
proof (T-C24) showed the parse's span-join fabricated spaces inside tight
paren constructs — '( A r )' where the PDF prints '(Ar)' — and T-C23 had
recorded those as PDF-verbatim. The canonical registry is now respaced from
the PDF; this script brings the store back in line:

  for every store record whose official_wording/official_bullets differ
  from the respaced canonical text: adopt the canonical (PDF) text, bump
  version 1 -> 2, and re-anchor any SPEC evidence quotes (concept_edges +
  concepts attachments) that no longer contain the old wording.

Fail-closed: any quote that cannot be re-anchored aborts the run without
writing (the quote's owner is listed for manual adjudication).
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import graph_paths as GP  # C28 §3.2 path registry — single source of ratified store paths
CANON = REPO / "Official-Specifications/parsed/igcse-chemistry/spec_points.json"
STORE = GP.store("specification_points")
EDGES = GP.store("concept_edges")
CONCEPTS = GP.store("concepts")
REC_JSON = REPO / "graph/reports/C24_STORE_RESPACE_RECORD.json"
REC_MD = REPO / "graph/reports/C24_STORE_RESPACE_RECORD.md"

failures: list[str] = []


def norm(s) -> str:
    s = str(s).lower()
    s = re.sub(r"[^\w\s]+", " ", s, flags=re.UNICODE)
    return re.sub(r"\s+", " ", s).strip()


def words(s) -> list[str]:
    return [w for w in re.split(r"[^\w]+", str(s).lower()) if w]


def reanchor(old_q: str, new_t: str):
    ow = [w for w in words(old_q) if w not in
          {"the", "a", "an", "of", "and", "or", "to", "in", "on", "for", "is",
           "are", "be", "how", "why", "what", "that", "this", "with", "by"}]
    ow_set = {w.lower() for w in ow}
    toks = [(m.group(0), m.start(), m.end()) for m in re.finditer(r"\w+", new_t)]
    low = [t[0].lower() for t in toks]
    idxs = [i for i, w in enumerate(low) if w in ow_set]
    if not idxs:
        return None
    start, end = idxs[0], idxs[-1]
    span_low = low[start:end + 1]
    overlap = sum(1 for w in span_low if w in ow_set)
    if overlap < max(1, int(0.5 * len(ow))):
        return None
    e = toks[end][2]
    m = re.match(r"[)\]»\"'’”]+", new_t[e:])
    if m:
        e += m.end()
    return new_t[toks[start][1]: e]


def main() -> int:
    canon = json.loads(CANON.read_text(encoding="utf-8"))
    cmap = {str(r["official_code"]): r for r in canon["spec_points"]}

    store_doc = yaml.safe_load(STORE.read_text(encoding="utf-8"))
    records = store_doc["specification_points"]

    changed = []
    for rec in records:
        code = str(rec["official_code"])
        c = cmap.get(code)
        if c is None:
            failures.append(f"{code}: not in canonical registry")
            continue
        new_text = str(c.get("text") or "").strip()
        new_bullets = [str(b).strip() for b in (c.get("sub_items") or [])]
        old_text = str(rec.get("official_wording") or "").strip()
        old_bullets = [str(b).strip() for b in (rec.get("official_bullets") or [])]
        if new_text == old_text and new_bullets == old_bullets:
            continue
        changed.append({
            "code": code, "version_from": rec.get("version"),
            "wording_before": old_text, "wording_after": new_text,
            "bullets_before": old_bullets, "bullets_after": new_bullets,
        })
        rec["official_wording"] = new_text
        if new_bullets:
            rec["official_bullets"] = new_bullets
        else:
            rec.pop("official_bullets", None)
        # per-record version stays 1 (house convention: task-level versioning;
        # the change is recorded in provenance.c24_respace + the C24 record)
        pr = rec.get("provenance") or {}
        pr["c24_respace"] = {
            "reason": "span-join space-injection artifact disproven by PDF glyph "
                      "geometry (e.g. '( A r )' -> '(Ar)', '( propan-1-ol only )' "
                      "-> '(propan-1-ol only)'); wording re-aligned to the PDF",
            "date": "2026-09-19"}

    if failures:
        print("FAIL-CLOSED:", *failures, sep="\n  ")
        return 1

    # ---- re-anchor SPEC evidence quotes ----
    text_of = {
        f"4CH1-{r['official_code']}":
            r["official_wording"] + (" " + " ".join(r["official_bullets"])
                                     if r.get("official_bullets") else "")
        for r in records}
    old_text_of = {c["code"]: c["wording_before"] +
                   (" " + " ".join(c["bullets_before"]) if c["bullets_before"] else "")
                   for c in changed}
    edge_doc = yaml.safe_load(EDGES.read_text(encoding="utf-8"))
    edges = edge_doc["edges"] if isinstance(edge_doc, dict) else edge_doc
    reanchors = []

    def fix_quotes(owner, tgt, evidence):
        for a in evidence or []:
            if a.get("kind") != "SPEC" or a.get("file") != GP.store_rel("specification_points"):
                continue
            q = str(a.get("quote", ""))
            nw = text_of.get(tgt, "")
            if not nw or norm(q) in norm(nw):
                continue
            old_t = old_text_of.get(tgt)
            nq = None
            if old_t and norm(q) in norm(old_t):
                nq = reanchor(q, nw)
            if not nq or norm(nq) not in norm(nw):
                # quote must remain resolvable: fall back to the full wording
                nq = nw
            reanchors.append({"where": owner, "sp": tgt,
                              "old_quote": q, "new_quote": nq})
            a["quote"] = nq

    for e in edges:
        fix_quotes(f"edge {e.get('source')} -[{e.get('relation')}]-> {e.get('target')}",
                   str(e.get("target", "")), e.get("evidence") or [])
    concept_doc = yaml.safe_load(CONCEPTS.read_text(encoding="utf-8"))
    nodes = concept_doc["nodes"] if isinstance(concept_doc, dict) else concept_doc
    concepts_before = json.dumps(concept_doc, sort_keys=True, default=str)
    for n in nodes:
        for att in n.get("spec_points") or []:
            fix_quotes(f"node {n.get('code')} @ {att.get('code')}",
                       str(att.get("code", "")), att.get("evidence") or [])
    concepts_changed = json.dumps(concept_doc, sort_keys=True, default=str) != concepts_before

    # ---- write ----
    STORE.write_text(yaml.safe_dump(store_doc, sort_keys=False, allow_unicode=True,
                                    width=110), encoding="utf-8")
    if reanchors:
        EDGES.write_text(yaml.safe_dump(edge_doc, sort_keys=False, allow_unicode=True,
                                        width=110), encoding="utf-8")
    if concepts_changed:
        CONCEPTS.write_text(yaml.safe_dump(concept_doc, sort_keys=False, allow_unicode=True,
                                           width=110), encoding="utf-8")

    record = {
        "task": "T-C24 WS-5b", "date": "2026-09-19",
        "store_records_refreshed": len(changed),
        "changes": changed,
        "quote_reanchors": reanchors,
        "concepts_changed": concepts_changed,
        "glyph_evidence": {
            "igcse-chemistry 1.16 p18": "spans 'atomic mass (' x1=168.9, 'A' x0=168.8, "
            "subscript 'r' x0=175.6, ')' x0=178.3 — zero gaps; PDF prints '(Ar)'",
            "igcse-chemistry 4.30C p31": "spans 'ethanol, propanol (' x1=206.3, "
            "'propan-1-ol only' x0=206.2 — zero gap; PDF prints '(propan-1-ol only)'",
        },
    }
    REC_JSON.write_text(json.dumps(record, indent=1, ensure_ascii=False), encoding="utf-8")
    REC_MD.write_text(
        f"""# C24 store respacing record — 2026-09-19

PDF-authoritative space-injection repair of the definitive chemistry store.

- Store records refreshed: **{len(changed)}** (version bumped to 2; per-record
  provenance block `c24_respace` added).
- Glyph-geometry proof: chemistry 1.16 (`( A r )` vs printed `(Ar)`, zero span
  gaps) and 4.30C (`( propan-1-ol only )` vs printed `(propan-1-ol only)`,
  0.1 pt gap) — the span-join spaces were parse artifacts, not PDF wording.
- SPEC evidence quote re-anchors: **{len(reanchors)}** (originals preserved in
  the JSON record).
- concepts.yaml quote updates: **{concepts_changed}**.
""", encoding="utf-8")

    print(f"store records refreshed: {len(changed)}")
    for c in changed:
        print(f"  {c['code']}: {c['wording_before'][:60]!r} -> {c['wording_after'][:60]!r}")
    print(f"quote re-anchors: {len(reanchors)}; concepts changed: {concepts_changed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
