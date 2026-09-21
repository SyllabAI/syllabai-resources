#!/usr/bin/env python3
"""
T-C26 — emit definitive sibling stores (PDF-direct wording + ratified overlay).

Operator directive 2026-09-20: refresh the five OCR-lineage sibling stores
(topics, practicals, assessment_objectives, command_words, relationships) so
that every wording field carries the official-PDF verbatim text (same authority
C23 applied to specification_points.yaml), every ratified enrichment is kept,
and the OCR lineage is retired from their meta blocks.

Zero-LLM. Wording sources, in priority order:
  1. canonical-builder-2.0 parse JSONs (Official-Specifications/parsed/igcse-chemistry/)
  2. adjudicated overrides verified verbatim against the official PDF (embedded
     below with page + proof; see C26 record)
Never silently fixes: every wording change and every damage-flag resolution is
written to graph/reports/C26_WORDING_DIFF_LEDGER.json.

Deterministic: byte-identical re-runs (no clocks beyond GENERATED constant).
"""
import hashlib
import json
import re
from pathlib import Path

import yaml

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import graph_paths as GP  # C28 §3.2 path registry — single source of ratified store paths

ROOT = Path(__file__).resolve().parents[1]
P = ROOT / "Official-Specifications/parsed/igcse-chemistry"
G = GP.qual_dir()  # C28 registry-resolved ratified store dir
REPORTS = GP.reports_dir()  # shared audit trail stays at graph/reports
PDF = ROOT / "Official-Specifications/igcse-chemistry/international-gcse-chemistry-2017-specification.pdf"
PDF_SHA1 = "3ad641b7c60b314fa3b10680feda30bf56280a53"
GENERATOR = "scripts/c26_emit_definitive_sibling_stores.py"
GENERATED = "2026-09-20"

POLICY = ("verbatim from the official PDF (canonical PDF-direct parse, whitespace-normalised only; "
          "PDF glyph-geometry spacing per C24/C26); notation damage preserved and flagged, never fixed")

YAML_KW = dict(sort_keys=False, default_flow_style=False, allow_unicode=True, width=100)


def load_yaml(p):
    return yaml.safe_load(Path(p).read_text(encoding="utf-8"))


def dump_yaml(p, doc):
    Path(p).write_text(yaml.safe_dump(doc, **YAML_KW), encoding="utf-8")


def norm(s):
    return re.sub(r"\s+", " ", str(s)).strip()


def check_pdf():
    got = hashlib.sha1(PDF.read_bytes()).hexdigest()
    assert got == PDF_SHA1, f"official PDF sha1 mismatch: {got}"
    return got


# ---------------------------------------------------------------- adjudications
# Wording verified verbatim from the official PDF where the canonical parse is
# truncated/damaged. Each override carries its proof (recorded in the ledger).
PR09_PDF_P27 = ("investigate temperature changes accompanying some of the following types of change: "
                "\u2022 salts dissolving in water \u2022 neutralisation reactions \u2022 displacement "
                "reactions \u2022 combustion reactions.")
AO2_OVERALL = "38\u201342%"  # PDF p35 Total row renders 38–42% for AO2; 23.2–25.7 + 14.8–16.3 = 38.0–42.0

OVERRIDES = {
    ("practicals.yaml", "4CH1-PR-09", "summary"): (
        PR09_PDF_P27,
        "canonical practicals.json truncated after 'change:' (bullet-colon class); bullets "
        "restored verbatim from official PDF p27 (zero-LLM extraction)"),
    ("assessment_objectives.yaml", "4CH1-AO2", "weighting_overall"): (
        AO2_OVERALL,
        "canonical text-layer cell damaged ('38 42%' + parser annotation, flag ao-dash-lost); "
        "resolved to 38–42% by PDF p35 Total row + column arithmetic "
        "(23.2–25.7 + 14.8–16.3 = 38.0–42.0)"),
}

FLAG_RESOLUTIONS = {
    "title-differs-md-vs-pdf": "record title now equals the PDF-verbatim title (canonical parse); "
                               "historical md-vs-pdf divergence no longer exists in the definitive lineage",
    "subsection-header-missing-in-md": "header sourced from canonical PDF-direct parse (page-anchored); "
                                       "md no longer in any lineage",
    "lost-space": "spacing restored from PDF glyph geometry via canonical parse (C24/C26 space-injection class)",
    "unknown-leading-verb": "PDF prints the 'practical:' statement label; ratified store convention strips "
                            "the label as a leading-verb artifact (C23 rule); canonical confirms",
    "ao-range-dash-missing": "AO2 weighting resolved to 38–42% (PDF p35 Total row + column arithmetic); "
                             "AO1/AO3 dashes were ASCII normalization, restored to PDF en-dash verbatim",
}

TOPIC_MAP = {"4CH1-S1": "4CH1-T3", "4CH1-S2": "4CH1-T4", "4CH1-S3": "4CH1-T5", "4CH1-S4": "4CH1-T6"}

LEDGER = {"generated": GENERATED, "generator": GENERATOR,
          "wording_changes": [], "field_adoption": [], "flag_resolutions": [], "identity_changes": []}


def ledger_add(kind, **kw):
    LEDGER[kind].append(kw)


def refresh_provenance(rec, page, extra=None):
    prov = rec.get("provenance")
    if not isinstance(prov, dict):
        prov = {}
    prov["wording_source"] = "canonical-pdf-direct-parse (canonical-builder-2.0, zero-LLM)"
    prov["pdf_sha1"] = PDF_SHA1
    if page is not None:
        prov["pdf_page"] = page
    if extra:
        prov.update(extra)
    rec["provenance"] = prov


def resolve_flags(rec, code, store):
    flags = rec.get("damage_flags") or []
    if not flags:
        return
    kept = []
    for f in flags:
        if f in FLAG_RESOLUTIONS:
            ledger_add("flag_resolutions", store=store, code=code, flag=f,
                       evidence=FLAG_RESOLUTIONS[f])
        else:
            kept.append(f)
    rec["damage_flags"] = kept


def set_meta(old_meta, counts, source_docs, extra_note):
    m = dict(old_meta)  # carry ratified keys (see c26_field_map.yaml meta_policy)
    m["statement_text_policy"] = POLICY
    m["generator"] = GENERATOR
    m["generated"] = GENERATED
    m["source_documents"] = source_docs
    m["definitive_lineage"] = {
        "as_of": GENERATED,
        "wording_authority": "international-gcse-chemistry-2017-specification.pdf",
        "structure_authority": "ratified store overlay (codes, orderings, categories, paper block)",
        "retired_lineage": {
            "source_file": "international-gcse-chemistry-2017-specification-2026-09-10_12-18-50.md",
            "generated_by": "scripts/c09_spec_graph_extract.py",
            "retired": True,
            "reason": "OCR-lineage wording damage; C23 made the PDF-direct-parse lineage definitive "
                      "and T-C26 extends it to the sibling stores",
        },
        "note": extra_note,
    }
    m["counts"] = counts
    return m


def head_yaml(rel):
    """Load the pre-C26 baseline from git HEAD (emitter must be idempotent: the
    ledger always diffs against the original store, never the working tree)."""
    import subprocess
    txt = subprocess.run(["git", "show", f"HEAD:{rel}"], capture_output=True, text=True,
                         cwd=ROOT).stdout
    return yaml.safe_load(txt)


def canonical_docs():
    docs = {}
    for n in ("topics", "practicals", "assessment_objectives", "command_words"):
        docs[n] = json.loads((P / f"{n}.json").read_text(encoding="utf-8"))
    return docs


# ---------------------------------------------------------------- emitters
def emit_topics(doc, can):
    ct = {t["code"]: norm(t["title"]) for t in can["topics"]}
    csub = can["subsections"]
    assert len(csub) == 28
    for t in doc["topics"]:
        cv = ct[TOPIC_MAP[t["code"]]]
        if norm(t["title"]) != cv:
            ledger_add("wording_changes", store="topics.yaml", code=t["code"], field="title",
                       old=t["title"], new=cv)
            t["title"] = cv
        refresh_provenance(t, None)
        resolve_flags(t, t["code"], "topics.yaml")
    for cs_, st_ in zip(csub, doc["subtopics"]):
        assert cs_["letter"] == st_["letter"], (cs_["code"], st_["code"])
        if norm(st_["title"]) != norm(cs_["title"]):
            ledger_add("wording_changes", store="topics.yaml", code=st_["code"], field="title",
                       old=st_["title"], new=cs_["title"], page=cs_["page"])
            st_["title"] = cs_["title"]
        st_["header_source"] = "canonical-pdf-direct-parse"
        refresh_provenance(st_, cs_["page"])
        resolve_flags(st_, st_["code"], "topics.yaml")
    meta = set_meta(doc["meta"], doc["meta"]["counts"],
                    [{"file": "international-gcse-chemistry-2017-specification.pdf",
                      "role": "official-pdf", "sha1": PDF_SHA1},
                     {"file": "Official-Specifications/parsed/igcse-chemistry/topics.json",
                      "role": "canonical-pdf-direct-parse", "builder": "canonical-builder-2.0"}],
                    "titles + subsection headers from the canonical PDF-direct parse; title_md and "
                    "structure are ratified overlay")
    doc["meta"] = meta
    return doc


def emit_practicals(doc, can):
    cps = sorted(can["practicals"], key=lambda x: int(x["ordering"]))
    assert len(cps) == len(doc["practicals"]) == 12
    for pr, cp in zip(doc["practicals"], cps):
        cv = re.sub(r"^practical:\s*", "", norm(cp["summary"]))
        ov = OVERRIDES.get(("practicals.yaml", pr["code"], "summary"))
        if ov:
            cv, proof = ov
            ledger_add("wording_changes", store="practicals.yaml", code=pr["code"], field="summary",
                       old=pr["summary"], new=cv, page=cp.get("page"), evidence=proof)
        elif norm(pr["summary"]) != cv:
            ledger_add("wording_changes", store="practicals.yaml", code=pr["code"], field="summary",
                       old=pr["summary"], new=cv, page=cp.get("page"))
        pr["summary"] = cv
        refresh_provenance(pr, cp.get("page"))
        resolve_flags(pr, pr["code"], "practicals.yaml")
    meta = set_meta(doc["meta"], doc["meta"]["counts"],
                    [{"file": "international-gcse-chemistry-2017-specification.pdf",
                      "role": "official-pdf", "sha1": PDF_SHA1},
                     {"file": "Official-Specifications/parsed/igcse-chemistry/practicals.json",
                      "role": "canonical-pdf-direct-parse", "builder": "canonical-builder-2.0"}],
                    "summaries verbatim from the canonical PDF-direct parse ('practical:' label "
                    "stripped per C23 leading-verb rule); PR-09 bullets PDF-verified p27")
    doc["meta"] = meta
    return doc


def emit_ao(doc, can):
    units = {u["unit"]: u["weightings"] for u in can["unit_weightings"]}
    w1, w2 = units["Chemistry Paper 1"], units["Chemistry Paper 2"]
    cds = {a["ao"]: a for a in can["statements"]}
    for a in doc["assessment_objectives"]:
        n = a["code"].split("-AO")[1]
        c = cds[f"AO{n}"]
        if norm(a["title"]) != norm(c["description"]):
            ledger_add("wording_changes", store="assessment_objectives.yaml", code=a["code"],
                       field="title", old=a["title"], new=c["description"], page=c.get("page"))
            a["title"] = c["description"]
        ov = OVERRIDES.get(("assessment_objectives.yaml", a["code"], "weighting_overall"))
        old_w = a.get("weighting_overall")
        new_w = ov[0] if ov else c["weighting_overall"]
        if old_w != new_w:
            entry = dict(store="assessment_objectives.yaml", code=a["code"],
                         field="weighting_overall", old=old_w, new=new_w, page=c.get("page"))
            if ov:
                entry["evidence"] = ov[1]
            ledger_add("field_adoption", **entry)
            a["weighting_overall"] = new_w
        bp = a.setdefault("weighting_by_paper", {})
        for key, vals in (("paper_1", w1), ("paper_2", w2)):
            tgt = bp.setdefault(key, {})
            for i in range(3):
                k = f"ao{n.lower()}"
                old_v = tgt.get(k)
                new_v = vals[i]
                if old_v != new_v:
                    ledger_add("field_adoption", store="assessment_objectives.yaml", code=a["code"],
                               field=f"weighting_by_paper.{key}.{k}", old=old_v, new=new_v)
                    tgt[k] = new_v
        refresh_provenance(a, c.get("page"))
        resolve_flags(a, a["code"], "assessment_objectives.yaml")
    for p in doc["papers"]:
        prov = p.setdefault("provenance", {})
        prov["source"] = "ratified-overlay (no canonical JSON source; marks/duration/weighting kept)"
    meta = set_meta(doc["meta"], doc["meta"]["counts"],
                    [{"file": "international-gcse-chemistry-2017-specification.pdf",
                      "role": "official-pdf", "sha1": PDF_SHA1},
                     {"file": "Official-Specifications/parsed/igcse-chemistry/assessment_objectives.json",
                      "role": "canonical-pdf-direct-parse", "builder": "canonical-builder-2.0"}],
                    "AO titles verbatim; weightings PDF en-dash verbatim (AO2 resolved via Total row "
                    "+ arithmetic); papers block is ratified overlay (no canonical source)")
    doc["meta"] = meta
    return doc


def emit_cw(doc, can):
    key = lambda s: re.sub(r"[^a-z0-9]", "", norm(s).lower())  # punctuation/space-insensitive identity
    cds = {key(k["command_word"]): k for k in can["command_words"]}
    for w in doc["command_words"]:
        c = cds[key(w["command_word"])]
        if norm(w["command_word"]) != norm(c["command_word"]):
            ledger_add("identity_changes", store="command_words.yaml", code=w["code"],
                       field="command_word", old=w["command_word"], new=c["command_word"],
                       page=c.get("page"))
            w["command_word"] = c["command_word"]
        if norm(w["definition"]) != norm(c["definition"]):
            ledger_add("wording_changes", store="command_words.yaml", code=w["code"],
                       field="definition", old=w["definition"], new=c["definition"], page=c.get("page"))
            w["definition"] = c["definition"]
        refresh_provenance(w, c.get("page"))
        resolve_flags(w, w["code"], "command_words.yaml")
    meta = set_meta(doc["meta"], doc["meta"]["counts"],
                    [{"file": "international-gcse-chemistry-2017-specification.pdf",
                      "role": "official-pdf", "sha1": PDF_SHA1},
                     {"file": "Official-Specifications/parsed/igcse-chemistry/command_words.json",
                      "role": "canonical-pdf-direct-parse", "builder": "canonical-builder-2.0"}],
                    "command words + definitions verbatim from the canonical PDF-direct parse "
                    "(appendix pages 51-52); category is ratified overlay")
    doc["meta"] = meta
    return doc


def emit_relationships(doc):
    sp = load_yaml(G / "specification_points.yaml")
    codes = {p["code"] for p in sp["specification_points"]}
    for n in ("topics", "practicals", "assessment_objectives"):
        d = load_yaml(G / f"{n}.yaml")
        for k, v in d.items():
            if isinstance(v, list):
                codes |= {r["code"] for r in v if isinstance(r, dict) and "code" in r}
    bad = []
    for e in doc["edges"]:
        for ep in (e["from"], e["to"]):
            if ep not in codes:
                bad.append((e.get("from"), e.get("to"), ep))
    assert not bad, f"unresolved relationship endpoints: {bad}"
    meta = set_meta(doc["meta"], doc["meta"]["counts"],
                    [{"file": "international-gcse-chemistry-2017-specification.pdf",
                      "role": "official-pdf", "sha1": PDF_SHA1}],
                    "no wording fields exist in this store (pure structure); meta brought to the "
                    "definitive standard and all 210-edge endpoints integrity-checked")
    doc["meta"] = meta
    return doc


def main():
    check_pdf()
    can = canonical_docs()
    out = {}
    for name, fn in (("topics", emit_topics), ("practicals", emit_practicals),
                     ("assessment_objectives", emit_ao), ("command_words", emit_cw)):
        doc = head_yaml(GP.store_rel(name))  # baseline: ledger + output independent of working tree
        out[name] = fn(doc, can[name])
    rel = head_yaml(GP.store_rel("relationships"))
    out["relationships"] = emit_relationships(rel)
    for name, doc in out.items():
        dump_yaml(G / f"{name}.yaml", doc)
    REPORTS.mkdir(exist_ok=True)
    (REPORTS / "C26_WORDING_DIFF_LEDGER.json").write_text(
        json.dumps(LEDGER, indent=1, ensure_ascii=False), encoding="utf-8")
    print("ledger:", {k: len(v) for k, v in LEDGER.items()})
    print("emitted:", ", ".join(sorted(out)) + " + C26_WORDING_DIFF_LEDGER.json")


if __name__ == "__main__":
    main()
