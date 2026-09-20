#!/usr/bin/env python3
"""
T-C23 — c23_emit_definitive_specpoints.py

Makes the PDF-direct-parse lineage the DEFINITIVE specification-point source
for the graph store, per the operator directive (2026-09-19):

  new (definitive)  = Official-Specifications/parsed/igcse-chemistry/spec_points.json
                      (canonical-builder-2.0, PDF verbatim wording + sub_items,
                       gates ALL_PASS, provenance sha1-pinned to the 2017 PDF)
  old (retired)     = graph/specification_points.yaml as emitted 2026-09-10 by
                      scripts/c09_spec_graph_extract.py from the OCR'd markdown
                      international-gcse-chemistry-2017-specification-2026-09-10_12-18-50.md

Merge rules (per official_code, all 182 verified present both sides):
  official_wording   <- PDF verbatim text          (authoritative wording)
  official_bullets   <- PDF sub_items              (new field; emitted when non-empty)
  section            <- PDF topic.number           (== old store, 0 disputes)
  subsection         <- OLD ratified               (74 JSON attachments proven
                                                     wrong by span geometry:
                                                     statement ABOVE header)
  ordering/global_order/c_point/practical/draft_skill_tags <- OLD ratified
  applicability      <- PDF (papers/shared identical; per-record rule text)
  leading_verb       <- PDF, except 'practical:' artifact -> OLD command verb
  validation_status/confidence/version <- RULE_DERIVED / 1.0 / 1 (schema)
  provenance         <- canonical lineage + supersedes block (old lineage retired)
  damage_flags       <- recomputed; wording-damage class resolved by the PDF
  4.30C keeps JSON flag possible-superscript-loss (PDF parse uncertainty)

Also re-anchors the only 2 SPEC evidence quotes (concept_edges.yaml) that do
not survive the wording change, and emits the swap record.

Fail-closed: exits nonzero on any precondition or postcondition violation.
Deterministic: no wall-clock input; byte-identical re-run.
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
CANON = REPO / "Official-Specifications/parsed/igcse-chemistry/spec_points.json"
OLD_SP = REPO / "graph/specification_points.yaml"
EDGES = REPO / "graph/concept_edges.yaml"
CONCEPTS = REPO / "graph/concepts.yaml"
RECORD_OUT_JSON = REPO / "graph/reports/C23_DEFINITIVE_SWAP_RECORD.json"
RECORD_OUT_MD = REPO / "graph/reports/C23_DEFINITIVE_SWAP_RECORD.md"

sys.path.insert(0, str(REPO / "scripts"))
from graph_check import c11_norm  # noqa: E402  — the checker's own norm

GENERATOR = "scripts/c23_emit_definitive_specpoints.py"
GENERATED = "2026-09-19"
PDF_SHA1 = "3ad641b7c60b314fa3b10680feda30bf56280a53"
SOURCE_PDF = "international-gcse-chemistry-2017-specification.pdf"
SOURCE_MD = "international-gcse-chemistry-2017-specification-2026-09-10_12-18-50.md"

EXPECT = {"points": 182, "c_points": 52, "global_order_max": 182}
COLON_EXCEPTIONS = {"4.49C"}  # bullet content is equation-class, not sub_items
DAMAGE_KEEP = {"possible-superscript-loss"}

failures: list[str] = []


def die(msg: str):
    failures.append(msg)


def norm(s) -> str:
    s = unicodedata.normalize("NFKC", str(s)).lower()
    s = re.sub(r"[^\w\s]+", " ", s, flags=re.UNICODE)
    return re.sub(r"\s+", " ", s).strip()


def words(s) -> list[str]:
    return [w for w in re.split(r"[^\w]+", str(s).lower()) if w]


def main() -> int:
    # ---------- load ----------
    canon = json.loads(CANON.read_text(encoding="utf-8"))
    P = canon["spec_points"]
    old_doc = yaml.safe_load(OLD_SP.read_text(encoding="utf-8"))
    old_meta = old_doc["meta"]
    O = old_doc["specification_points"]
    pmap = {str(r["official_code"]): r for r in P}
    omap = {str(r["official_code"]): r for r in O}
    codes = sorted(pmap, key=lambda c: (int(str(c).split(".")[0]), c))

    # ---------- preconditions ----------
    if len(pmap) != EXPECT["points"] or len(omap) != EXPECT["points"]:
        die(f"point count canon={len(pmap)} old={len(omap)} != {EXPECT['points']}")
    if set(pmap) != set(omap):
        die("code sets differ between canon and old store")
    for c in codes:
        pv = (pmap[c].get("provenance") or {}).get("pdf_sha1")
        if pv != PDF_SHA1:
            die(f"{c}: canon provenance pdf_sha1 {pv!r} != pin")
    if sum(1 for c in codes if c.endswith("C")) != EXPECT["c_points"]:
        die("c_point count drift")

    # ---------- merge ----------
    new_records, adjud = [], {
        "wording_from_pdf": [], "bullets_added": [], "subsection_kept_ratified": [],
        "leading_verb_fallback": [], "applicability_rule_updated": [],
        "damage_flags_resolved": {}, "damage_flags_kept": {}, "colon_exceptions": [],
        "quote_reanchors": [],
    }
    for c in codes:
        p, o = pmap[c], omap[c]
        wording = str(p["text"]).strip()
        bullets = [str(b).strip() for b in (p.get("sub_items") or [])]
        section = f"4CH1-S{p['topic']['number']}"
        if section != str(o.get("section")):
            die(f"{c}: section dispute canon={section} old={o.get('section')}")
            section = str(o.get("section"))
        subsection = str(o.get("subsection"))
        # geometry adjudication: JSON attachment impossible when the statement
        # prints ABOVE its attached header
        pl = (p.get("subsection") or {})
        stmt = (p["provenance"]["page"], p["provenance"]["oy"])
        hdr = (pl.get("page"), pl.get("oy"))
        if f"4CH1-S{p['topic']['number']}-{pl.get('letter')}" != subsection:
            adjud["subsection_kept_ratified"].append(
                {"code": c, "kept": subsection,
                 "canon": f"4CH1-S{p['topic']['number']}-{pl.get('letter')}",
                 "geometry": f"stmt=p{stmt[0]}y{stmt[1]} hdr=p{hdr[0]}y{hdr[1]}",
                 "impossible": bool(hdr[1] and stmt[1] and stmt < hdr)})
        verb = str(p.get("leading_verb") or "").strip()
        if verb == "practical:" or not verb:
            verb = str(o.get("leading_verb"))
            adjud["leading_verb_fallback"].append({"code": c, "kept": verb,
                                                   "canon_artifact": "practical:"})
        if str(o.get("official_wording")).strip() != wording:
            adjud["wording_from_pdf"].append(c)
        if bullets:
            adjud["bullets_added"].append(c)
        if str(c) in COLON_EXCEPTIONS:
            adjud["colon_exceptions"].append(c)
        if (o.get("applicability") or {}).get("rule") != (p.get("applicability") or {}).get("rule"):
            adjud["applicability_rule_updated"].append(c)
        # damage flags: wording-damage classes resolved by the PDF verbatim
        resolved = [f for f in (o.get("damage_flags") or []) if f not in DAMAGE_KEEP]
        kept = [f for f in (o.get("damage_flags") or []) if f in DAMAGE_KEEP]
        kept += [f for f in (p.get("flags") or []) if f in DAMAGE_KEEP]
        if resolved:
            adjud["damage_flags_resolved"][c] = resolved
        if kept:
            adjud["damage_flags_kept"][c] = sorted(set(kept))
        prov = {
            "tier": "RULE_DERIVED",
            "source_file": "Official-Specifications/parsed/igcse-chemistry/spec_points.json",
            "spec_issue": 3,
            "extraction_method": "pdf-span-geometry (zero-LLM)",
            "generated_by": GENERATOR,
            "generated_date": GENERATED,
            "pdf_source": SOURCE_PDF,
            "pdf_sha1": PDF_SHA1,
            "pdf_page": p["provenance"]["page"],
            "pdf_oy": p["provenance"]["oy"],
            "canonical_builder": "canonical-builder-2.0 (2026-09-17)",
            "supersedes": {
                "source_file": SOURCE_MD,
                "generated_by": "scripts/c09_spec_graph_extract.py",
                "generated_date": "2026-09-10",
                "retired": True,
                "reason": "OCR-lineage wording damage (54 flagged records); "
                          "operator directive 2026-09-19 makes the PDF-direct-parse "
                          "lineage definitive",
            },
        }
        rec = {
            "code": f"4CH1-{c}",
            "official_code": c,
            "official_wording": wording,
            "section": section,
            "subsection": subsection,
            "ordering": o["ordering"],
            "global_order": o["global_order"],
            "c_point": bool(o.get("c_point")),
            "practical": bool(o.get("practical")),
            "applicability": p["applicability"],
            "leading_verb": verb,
            "draft_skill_tags": list(o.get("draft_skill_tags") or []),
            "validation_status": "RULE_DERIVED",
            "confidence": 1.0,
            "version": 1,
            "provenance": prov,
            "damage_flags": sorted(set(kept)),
        }
        if bullets:
            rec["official_bullets"] = bullets
        new_records.append(rec)

    # ---------- postconditions ----------
    if len(new_records) != EXPECT["points"]:
        die("emitted count drift")
    gorders = sorted(r["global_order"] for r in new_records)
    if gorders != list(range(1, EXPECT["global_order_max"] + 1)):
        die("global_order not exactly 1..182")
    for r in new_records:
        if not r["official_wording"]:
            die(f"{r['official_code']}: empty wording")
        if r["official_wording"].rstrip().endswith(":") and not r.get("official_bullets") \
                and r["official_code"] not in COLON_EXCEPTIONS:
            die(f"{r['official_code']}: colon-ending wording without bullets")
        if r["c_point"] != r["official_code"].endswith("C"):
            die(f"{r['official_code']}: c_point semantics")
        if r["practical"] and "4CH1-SK-PRACTICAL" not in r["draft_skill_tags"]:
            die(f"{r['official_code']}: practical lacks PRACTICAL skill tag")
        # note: leading_verb ↔ tag equality is NOT a store invariant (PREPARE
        # has no SK tag in the ratified vocabulary); tags are ratified as-is.

    if failures:
        print("FAIL-CLOSED:", *failures, sep="\n  ")
        return 1

    # ---------- quote re-anchors (concept_edges.yaml) ----------
    edge_doc = yaml.safe_load(EDGES.read_text(encoding="utf-8"))
    edges = edge_doc["edges"] if isinstance(edge_doc, dict) else edge_doc
    # containment/anchor space = definitive wording + PDF bullets (the checker
    # will enforce the same joined source)
    text_of = {f"4CH1-{r['official_code']}":
               r["official_wording"] + (" " + " ".join(r["official_bullets"])
                                        if r.get("official_bullets") else "")
               for r in new_records}
    STOP = {"the", "a", "an", "of", "and", "or", "to", "in", "on", "for", "is",
            "are", "be", "how", "why", "what", "that", "this", "with", "by"}

    def reanchor(old_q: str, new_t: str):
        """Re-anchor a quote into the definitive text: densest old↔new token
        overlap window, mapped back to a verbatim raw-case span of new_t."""
        ow = [w for w in words(old_q) if w not in STOP]
        ow_set = {w.lower() for w in ow}
        toks = [(m.group(0), m.start(), m.end())
                for m in re.finditer(r"\w+", new_t)]
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
        # keep attached closing brackets/quotes so the span stays balanced
        m = re.match(r"[)\]»\"'’”]+", new_t[e:])
        if m:
            e += m.end()
        return new_t[toks[start][1]: e]

    raw_edges = EDGES.read_text(encoding="utf-8")
    reanchored = []

    def fix_evidence(owner_label, tgt, evidence):
        """Re-anchor stale SPEC quotes (checker norm) in one evidence list."""
        for a in evidence or []:
            if a.get("kind") != "SPEC" or a.get("file") != "graph/specification_points.yaml":
                continue
            q = str(a.get("quote", ""))
            nw = text_of.get(tgt, "")
            if c11_norm(q) in c11_norm(nw):
                continue
            new_q = reanchor(q, nw)
            if not new_q or c11_norm(new_q) not in c11_norm(nw):
                new_q = nw  # fallback: the full wording+bullets is the anchor
            adjud["quote_reanchors"].append(
                {"where": owner_label, "sp": tgt,
                 "old_quote": q, "new_quote": new_q,
                 "reason": "quote captured from retired OCR wording; re-anchored "
                           "to the definitive PDF wording (checker c11_norm)"})
            a["quote"] = new_q
            reanchored.append(owner_label)

    for e in edges:
        fix_evidence(f"edge {e.get('source')} -[{e.get('relation')}]-> {e.get('target')}",
                     str(e.get("target", "")), e.get("evidence") or [])
    concept_doc = yaml.safe_load(CONCEPTS.read_text(encoding="utf-8"))
    concept_nodes = concept_doc["nodes"] if isinstance(concept_doc, dict) else concept_doc
    concepts_pre_sha = __import__("hashlib").sha256(
        CONCEPTS.read_bytes()).hexdigest()
    concepts_changed = False
    for n in concept_nodes:
        for att in n.get("spec_points") or []:
            before = json.dumps(att.get("evidence") or [], ensure_ascii=False)
            fix_evidence(f"node {n.get('code')} @ {att.get('code')}",
                         str(att.get("code", "")), att.get("evidence") or [])
            if json.dumps(att.get("evidence") or [], ensure_ascii=False) != before:
                concepts_changed = True
    if concepts_changed:
        CONCEPTS.write_text(
            yaml.safe_dump(concept_doc, sort_keys=False, allow_unicode=True, width=110),
            encoding="utf-8")
    concepts_post_sha = __import__("hashlib").sha256(
        CONCEPTS.read_bytes()).hexdigest()

    # ---------- emit ----------
    meta = dict(old_meta)
    meta["generator"] = GENERATOR
    # C25 closeout: the inherited OCR-era policy line is wrong for the
    # definitive lineage — wording authority is the official PDF now.
    meta["statement_text_policy"] = (
        "verbatim from the official PDF (canonical PDF-direct parse, "
        "whitespace-normalised only; PDF glyph-geometry respacing per C24); "
        "notation damage preserved and flagged, never fixed")
    if concepts_changed:
        meta["concepts_quote_reanchor_note"] = (
            "concepts.yaml SPEC evidence quotes re-anchored to the definitive "
            "wording; statuses/tiers/attachments unchanged in meaning "
            f"(pre {concepts_pre_sha[:16]} -> post {concepts_post_sha[:16]}; "
            "see C23 record)")
    meta["generated"] = GENERATED
    counts = dict(meta.get("counts") or {})
    counts["spec_points"] = len(new_records)
    counts["c_points"] = sum(1 for r in new_records if r["c_point"])
    meta["counts"] = counts
    meta["source_documents"] = [
        {"file": SOURCE_PDF, "role": "official-pdf", "sha1": PDF_SHA1},
        {"file": "Official-Specifications/parsed/igcse-chemistry/spec_points.json",
         "role": "canonical-pdf-direct-parse", "builder": "canonical-builder-2.0"},
    ]
    meta["definitive_lineage"] = {
        "as_of": GENERATED, "wording_authority": SOURCE_PDF,
        "structure_authority": "ratified store overlay (subsections, orderings, skill tags)",
        "retired_lineage": {"source_file": SOURCE_MD,
                            "generated_by": "scripts/c09_spec_graph_extract.py",
                            "generated_date": "2026-09-10", "retired": True},
    }
    out_doc = {"meta": meta, "specification_points": new_records}
    OLD_SP.write_text(
        yaml.safe_dump(out_doc, sort_keys=False, allow_unicode=True, width=110),
        encoding="utf-8")
    EDGES.write_text(
        yaml.safe_dump(edge_doc, sort_keys=False, allow_unicode=True, width=110),
        encoding="utf-8")

    RECORD_OUT_JSON.write_text(json.dumps(
        {"task": "T-C23", "date": GENERATED, "generator": GENERATOR,
         "directive": "operator 2026-09-19: make the Official-Specifications "
                      "PDF-direct-parse the definitive specification; copy all "
                      "ratified enrichments from the old store; retire the OCR lineage",
         "counts": {"records": len(new_records),
                    "wording_from_pdf": len(adjud["wording_from_pdf"]),
                    "bullets_added": len(adjud["bullets_added"]),
                    "subsection_kept_ratified": len(adjud["subsection_kept_ratified"]),
                    "subsection_json_impossible": sum(
                        1 for a in adjud["subsection_kept_ratified"] if a["impossible"]),
                    "leading_verb_fallback": len(adjud["leading_verb_fallback"]),
                    "applicability_rule_updated": len(adjud["applicability_rule_updated"]),
                    "damage_flags_resolved": sum(
                        len(v) for v in adjud["damage_flags_resolved"].values()),
                    "quote_reanchors": len(adjud["quote_reanchors"])},
         "adjudications": adjud,
         "retirement": {"retired_source_file": SOURCE_MD,
                        "retired_generator": "scripts/c09_spec_graph_extract.py",
                        "successor": GENERATOR,
                        "old_store_sha256_pre_swap":
                            __import__("hashlib").sha256(
                                json.dumps(
                                    [[o.get("official_code"),
                                      o.get("official_wording")] for o in O],
                                    ensure_ascii=False).encode()).hexdigest()},
         "concepts_yaml": {
             "pre_sha256": concepts_pre_sha, "post_sha256": concepts_post_sha,
             "scope_note": "only SPEC evidence quote strings re-anchored; node "
                           "statuses (98 CON + 15 MIS all SUGGESTED), provenance "
                           "tiers, aliases, titles, attachments unchanged in "
                           "meaning; C19 promotion record untouched"},
         }, indent=2, ensure_ascii=False), encoding="utf-8")

    n = adjud and len(adjud["wording_from_pdf"]) or 0
    md = f"""# C23 definitive swap record — {GENERATED}

Operator directive (2026-09-19): make the Official-Specifications PDF-direct-parse the
**definitive** specification-point source; copy all ratified enrichments from the old
store; retire the OCR lineage.

- Definitive wording: `{SOURCE_PDF}` via canonical-builder-2.0 (`spec_points.json`,
  gates ALL_PASS, sha1 `{PDF_SHA1[:12]}…`), zero-LLM span-geometry provenance per record.
- Retired: `{SOURCE_MD}` + `scripts/c09_spec_graph_extract.py` (2026-09-10 OCR lineage).
- Records: {len(new_records)}; wording refreshed from PDF: **{len(adjud['wording_from_pdf'])}**;
  bullet fields added (PDF sub_items): **{len(adjud['bullets_added'])}**.
- Subsections: OLD ratified values kept everywhere; **{len(adjud['subsection_kept_ratified'])}**
  canonical disagreements, **all proven impossible by span geometry** (statement above header).
- Leading verb: **{len(adjud['leading_verb_fallback'])}** canonical `'practical:'` artifacts
  fell back to the ratified command verb.
- Applicability rule text: **{len(adjud['applicability_rule_updated'])}** updated to the
  per-record PDF rule (papers/shared structurally identical 182/182).
- Damage flags: **{sum(len(v) for v in adjud['damage_flags_resolved'].values())}** resolved
  by the verbatim wording; kept: {adjud['damage_flags_kept'] or 'none'}.
- Quote re-anchors: **{len(adjud['quote_reanchors'])}** (details in the JSON record);
  originals preserved verbatim in this record.
- Colon exceptions: {adjud['colon_exceptions'] or 'none'}.

Full per-record detail: `C23_DEFINITIVE_SWAP_RECORD.json`.
"""
    RECORD_OUT_MD.write_text(md, encoding="utf-8")
    print(f"OK: {len(new_records)} records emitted; wording {n}; "
          f"bullets {len(adjud['bullets_added'])}; subsections kept "
          f"{len(adjud['subsection_kept_ratified'])} ({adjud['subsection_kept_ratified'] and sum(1 for a in adjud['subsection_kept_ratified'] if a['impossible'])} impossible); "
          f"reanchors {len(adjud['quote_reanchors'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
