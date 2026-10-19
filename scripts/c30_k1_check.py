#!/usr/bin/env python3
"""T-C30 — c30_k1_check.py: the K1 gate battery for igcse-maths-a.

K1 gate (C28 spec §6): canonical equality 1:1; damage-class scan 0; counts ==
parse_report; graph-check coverage extended to the new paths; single commit +
record. This checker is the maths-qual analogue of the chemistry-only
graph_check.py schema/referential/consistency lanes, plus the K1-specific
gates; the chemistry graph_check itself must stay green (G9) and the S0
no-hardcode/registry gate must stay green (G10).

Gates:
  G1  canonical equality 1:1 — specification_points vs the chosen canonical
      rows (wording whitespace-normalised, everything else verbatim)
  G2  topics/subtopics — counts, Higher-walk titles, membership closure,
      ordering contiguity, parent resolution
  G3  counts == parse_report + meta agreement across the 5 stores
  G4  schema/provenance/namespace — RULE_DERIVED discipline, provenance
      completeness, 4MA1-* namespace, foreign-code scan
  G5  tier-dedupe integrity — ledger == observed dedupe; higher-preferred
      choices verified; reworded rows carry the note
  G6  damage-class scan 0 + no md-OCR residue (the C27 S1 scanner, reused)
  G7  empty-by-parse stores — practicals/command_words notes verbatim
  G8  assessment_objectives — statements + unit weightings verbatim
  G9  chemistry graph_check exit 0 (default qual untouched)
  G10 check_no_hardcode exit 0 (multi-qual registry consistency)

Read-only toward the stores and the canonical plane; writes only its own
report (graph/reports/C30_K1_CHECK.json). Exit 0 iff all gates PASS.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
sys.path.insert(0, str(HERE))
import graph_paths as GP  # noqa: E402

QUAL = "igcse-maths-a"
CODE = "4MA1"
PDF_SHA1 = "b71a6432b8e34c155efb510d79a7b6e97611ba01"
CANON = REPO / "Official-Specifications/parsed/igcse-maths-a"
LEDGER_REL = "graph/reports/C30_MATHS_A_TIER_DEDUPE_LEDGER.json"
REPORT = REPO / "graph/reports/C30_K1_CHECK.json"
EMITTER = "scripts/c30_emit_maths_a_spec_stores.py"
GENERATED = "2026-10-01"
STORES = ["specification_points", "topics", "practicals",
          "assessment_objectives", "command_words"]
PROV_KEYS = {"tier", "source_file", "extraction_method", "generated_by",
             "generated_date", "pdf_source", "pdf_sha1", "canonical_builder"}
FOREIGN_RE = re.compile(r"\b(4CH1|4SD0|WMA[0-9]|WPH[0-9]|IAL)\b")
SUB_RE = re.compile(r"^(\d+)\.(\d+)([A-Z]?)$")


def norm(s) -> str:
    return re.sub(r"\s+", " ", str(s)).strip()


def sub_num(c: str) -> tuple:
    a, b = c.split(".")
    return (int(a), int(b))


def point_key(oc: str) -> tuple:
    m = SUB_RE.match(oc)
    return (int(m.group(1)), int(m.group(2)), m.group(3))


def main() -> int:
    gates: dict[str, dict] = {}

    def gate(name: str, ok: bool, detail) -> None:
        gates[name] = {"status": "PASS" if ok else "FAIL", "detail": detail}

    stores = {n: yaml.safe_load(GP.store(n, QUAL).read_text(encoding="utf-8"))
              for n in STORES}
    spec = json.loads((CANON / "spec_points.json").read_text(encoding="utf-8"))
    rows = spec["spec_points"]
    parse_report = json.loads((CANON / "parse_report.json").read_text(encoding="utf-8"))
    ao_c = json.loads((CANON / "assessment_objectives.json").read_text(encoding="utf-8"))
    cw_c = json.loads((CANON / "command_words.json").read_text(encoding="utf-8"))
    pr_c = json.loads((CANON / "practicals.json").read_text(encoding="utf-8"))
    topics_c = json.loads((CANON / "topics.json").read_text(encoding="utf-8"))

    # ---- rebuild the sanctioned dedupe choice independently -------------------
    by_code = {}
    for r in rows:
        by_code.setdefault(r["official_code"], []).append(r)
    chosen = {}
    for oc, g in by_code.items():
        hi = [x for x in g if x["applicability"]["tier"] == "Higher"]
        chosen[oc] = hi[0] if hi else g[0]

    # ---- G1 canonical equality 1:1 -------------------------------------------
    d = {}
    sp = stores["specification_points"]["specification_points"]
    codes = [r["official_code"] for r in sp]
    d["rows"] = len(sp)
    d["unique_store_codes"] = len(set(codes))
    d["canonical_unique"] = len(by_code)
    bad_wording, bad_verbatim, missing = [], [], []
    for r in sp:
        c = chosen.get(r["official_code"])
        if c is None:
            missing.append(r["official_code"])
            continue
        if norm(r["official_wording"]) != norm(c["text"]):
            bad_wording.append(r["official_code"])
        for field, cfield in (("leading_verb", "leading_verb"),
                              ("ordering", "ordering"), ("scope", "scope")):
            if r.get(field) != c.get(cfield):
                bad_verbatim.append(f"{r['official_code']}:{field}")
        if r["applicability"]["tier"] != c["applicability"]["tier"] or \
           r["applicability"]["papers"] != c["applicability"]["papers"] or \
           norm(r["applicability"]["rule"]) != norm(c["applicability"]["rule"]):
            bad_verbatim.append(f"{r['official_code']}:applicability")
        if (r.get("damage_flags") or []) != (c.get("flags") or []):
            bad_verbatim.append(f"{r['official_code']}:flags")
        if r.get("practical") != bool(c.get("practical")) or r.get("c_point") is not False:
            bad_verbatim.append(f"{r['official_code']}:practical/c_point")
    d["bad_wording"] = bad_wording[:8]
    d["bad_verbatim"] = bad_verbatim[:8]
    d["missing"] = missing[:8]
    go = [r["global_order"] for r in sp]
    d["global_order_contiguous"] = go == list(range(1, len(sp) + 1))
    ok = (len(sp) == len(by_code) == len(set(codes)) and not bad_wording
          and not bad_verbatim and not missing and d["global_order_contiguous"])
    gate("G1_canonical_equality_1to1", ok, d)

    # ---- G2 topics/subtopics ---------------------------------------------------
    d = {}
    tp = stores["topics"]
    topics, subs = tp["topics"], tp["subtopics"]
    d["topics"] = len(topics)
    d["subtopics"] = len(subs)
    hi_titles, fo_titles = {}, {}
    for r in rows:
        n = int(r["topic"]["number"])
        (hi_titles if r["applicability"]["tier"] == "Higher" else fo_titles
         ).setdefault(n, r["topic"]["title"])
    bad_title = [t["code"] for t in topics
                 if norm(t["title"]) != norm(hi_titles.get(
                     int(t["code"].split("S")[1]), ""))]
    # canonical topics.json numbered rows must carry the same titles (some walk)
    tj_bad = []
    for t in topics_c.get("topics", []):
        num = str(t.get("number"))
        if num.isdigit():
            n = int(num)
            if norm(t["title"]) not in {norm(hi_titles.get(n, "")),
                                        norm(fo_titles.get(n, ""))}:
                tj_bad.append(t["code"])
    declared = [p for s in subs for p in s["spec_points"]]
    sp_codes = sorted(r["code"] for r in sp)
    d["membership_closure"] = sorted(declared) == sp_codes
    d["parent_resolved"] = all(
        any(t["code"] == s["parent"] for t in topics) for s in subs)
    d["bad_titles"] = bad_title
    d["topics_json_disagreements"] = tj_bad
    d["subtopic_ordering_contiguous"] = [s["ordering"] for s in subs] == \
        list(range(1, len(subs) + 1))
    d["topic_ordering_contiguous"] = [t["ordering"] for t in topics] == \
        list(range(1, len(topics) + 1))
    d["letter_is_subsection_code"] = all(
        s["letter"] == s["code"].split("-", 2)[2].replace(
            f"S{s['code'].split('-')[1][1:]}", "", 1) if False else
        s["code"] == f"{s['parent']}-{s['letter']}" for s in subs)
    sec_of_sub_ok = all(
        s["parent"] == f"{CODE}-S{int(s['letter'].split('.')[0])}" for s in subs)
    d["sub_parent_section_agrees"] = sec_of_sub_ok
    ok = (len(topics) == 6 and len(subs) == 39 and not bad_title and not tj_bad
          and d["membership_closure"] and d["parent_resolved"]
          and d["subtopic_ordering_contiguous"] and d["topic_ordering_contiguous"]
          and d["letter_is_subsection_code"] and sec_of_sub_ok)
    gate("G2_topics_subtopics_closure", ok, d)

    # ---- G3 counts == parse_report + meta agreement ----------------------------
    d = {}
    pr_counts = parse_report["counts"]["international-gcse-in-mathematics-spec-a.parsed.json"]
    metas = {n: stores[n]["meta"] for n in STORES}
    all_counts = {n: m["counts"] for n, m in metas.items()}
    consistent = all(
        c["spec_points"] == 188 and c["topics"] == 6 and c["subtopics"] == 39
        and c["practicals"] == 0 and c["command_words"] == 0
        for c in all_counts.values())
    d["parse_report"] = {k: pr_counts[k] for k in
                         ("spec_points", "topics", "subsections", "flagged")}
    d["dedupe_note"] = "242 rows -> 188 unique official_codes (both tiers)"
    d["meta_counts_consistent"] = consistent
    d["flagged"] = all_counts["specification_points"]["flagged_spec_points"]
    ok = (consistent and pr_counts["spec_points"] == 242
          and d["flagged"] == pr_counts["flagged"] == 8)
    gate("G3_counts_match_parse_report", ok, d)

    # ---- G4 schema/provenance/namespace ----------------------------------------
    d = {}
    bad_schema, bad_prov, foreign = [], [], []
    for r in sp:
        ctx = r.get("code")
        if not re.match(rf"^{CODE}-", str(r.get("code"))):
            bad_schema.append(f"{ctx}:code")
        if r.get("validation_status") != "RULE_DERIVED" or \
           r.get("confidence") != 1.0 or r.get("version") != 1 or \
           not isinstance(r.get("damage_flags"), list):
            bad_schema.append(f"{ctx}:discipline")
        if not re.match(rf"^{CODE}-S\d+$", str(r.get("section"))):
            bad_schema.append(f"{ctx}:section")
        if not re.match(rf"^{CODE}-S\d+-\d+\.\d+$", str(r.get("subsection"))):
            bad_schema.append(f"{ctx}:subsection")
        p = r.get("provenance") or {}
        missing_keys = PROV_KEYS - set(p)
        if missing_keys or p.get("tier") != "RULE_DERIVED" or \
           p.get("pdf_sha1") != PDF_SHA1 or \
           p.get("generated_by") != EMITTER or \
           p.get("generated_date") != GENERATED or \
           not isinstance(p.get("pdf_page"), int) or p.get("pdf_page") < 1 or \
           not isinstance(p.get("pdf_oy"), (int, float)) or \
           isinstance(p.get("pdf_oy"), bool):
            bad_prov.append(ctx)
        for f in (r.get("applicability", {}).get("rule") or ""):
            pass
        for s in (r.get("applicability", {}).get("rule"),
                  r.get("official_wording")):
            if isinstance(s, str) and FOREIGN_RE.search(s):
                foreign.append(f"{ctx}:{s[:40]}")
    for coll, kind in ((tp["topics"], "topic"), (tp["subtopics"], "sub")):
        for r in coll:
            if r.get("validation_status") != "RULE_DERIVED" or \
               r.get("confidence") != 1.0 or r.get("version") != 1 or \
               not isinstance(r.get("damage_flags"), list) or \
               (r.get("provenance") or {}).get("tier") != "RULE_DERIVED":
                bad_schema.append(f"{r.get('code')}:{kind}")
    for coll in (stores["assessment_objectives"]["assessment_objectives"],
                 stores["assessment_objectives"]["unit_weightings"]):
        for r in coll:
            if r.get("validation_status") != "RULE_DERIVED" or \
               r.get("confidence") != 1.0 or r.get("version") != 1:
                bad_schema.append(f"{r.get('code') or r.get('unit')}:ao")
    d["bad_schema"] = bad_schema[:8]
    d["bad_provenance"] = bad_prov[:8]
    d["foreign_code_hits"] = foreign[:8]
    d["flag_vocab"] = all_counts["specification_points"]["damage_flag_vocabulary"]
    ok = not bad_schema and not bad_prov and not foreign
    gate("G4_schema_provenance_namespace", ok, d)

    # ---- G5 tier-dedupe integrity -----------------------------------------------
    d = {}
    ledger = json.loads((REPO / LEDGER_REL).read_text(encoding="utf-8"))
    lrows = ledger["rows"]
    obs_dups = sorted(oc for oc, g in by_code.items() if len(g) > 1)
    d["ledger_rows"] = len(lrows)
    d["observed_dups"] = len(obs_dups)
    d["census"] = ledger["census"]
    store_by_code = {r["official_code"]: r for r in sp}
    bad_choice, bad_note = [], []
    for lr in lrows:
        oc = lr["official_code"]
        sr = store_by_code.get(oc)
        if sr is None:
            bad_choice.append(f"{oc}:missing")
            continue
        if norm(sr["official_wording"]) != norm(lr["higher"]["text"]):
            bad_choice.append(oc)
        if sr["provenance"].get("tier_walk") != "Higher":
            bad_choice.append(f"{oc}:tier_walk")
        if not lr["same_text_normalized"] and "tier_dedupe_note" not in sr:
            bad_note.append(oc)
    reworded = sum(1 for lr in lrows if not lr["same_text_normalized"])
    fo_count = sum(1 for oc, g in by_code.items()
                   if len(g) == 1 and g[0]["applicability"]["tier"] == "Foundation")
    ho_count = sum(1 for oc, g in by_code.items()
                   if len(g) == 1 and g[0]["applicability"]["tier"] == "Higher")
    d["reworded"] = reworded
    d["foundation_only"] = fo_count
    d["higher_only"] = ho_count
    title_var = ledger.get("title_variants", [])
    d["title_variants"] = title_var
    ok = (len(lrows) == len(obs_dups) == 54 and reworded == 53
          and fo_count == 108 and ho_count == 26
          and not bad_choice and not bad_note
          and any(v["section"] == 4 and v["higher"] == "Geometry and trigonometry"
                  for v in title_var))
    gate("G5_tier_dedupe_integrity", ok, d)

    # ---- G6 damage-class scan (C27 S1 scanner) + md-OCR residue ------------------
    d = {}
    try:
        from c27_final_all_store_sweep import damage_scan_strings
        hits = {}
        for n in STORES:
            hs = list(damage_scan_strings(stores[n]))
            if hs:
                hits[n] = hs[:3]
        d["damage_hits"] = hits
        residue = {n: "md ocr" in GP.store(n, QUAL).read_text(encoding="utf-8").lower()
                   for n in STORES}
        d["md_ocr_residue"] = {k: v for k, v in residue.items() if v}
        ok = not hits and not any(residue.values())
    except Exception as e:  # noqa: BLE001
        ok, d["error"] = False, repr(e)
    gate("G6_damage_scan_zero", ok, d)

    # ---- G7 empty-by-parse stores -----------------------------------------------
    d = {}
    d["practicals_note_verbatim"] = stores["practicals"].get("note") == pr_c.get("note")
    d["command_words_note_verbatim"] = stores["command_words"].get("note") == cw_c.get("note")
    d["practicals_empty"] = stores["practicals"]["practicals"] == []
    d["command_words_empty"] = stores["command_words"]["command_words"] == []
    ok = all([d["practicals_note_verbatim"], d["command_words_note_verbatim"],
              d["practicals_empty"], d["command_words_empty"]])
    gate("G7_empty_by_parse_stores", ok, d)

    # ---- G8 assessment_objectives verbatim ----------------------------------------
    d = {}
    ao = stores["assessment_objectives"]
    d["statements"] = len(ao["assessment_objectives"])
    d["unit_weightings"] = len(ao["unit_weightings"])
    bad = []
    for s, c in zip(ao["assessment_objectives"], ao_c["statements"]):
        if s["code"] != c["ao"] or norm(s["description"]) != norm(c["description"]) \
           or s["weighting_overall"] != c["weighting_overall"] or \
           s["provenance"]["pdf_page"] != c["page"]:
            bad.append(s["code"])
    for u, c in zip(ao["unit_weightings"], ao_c["unit_weightings"]):
        if u["unit"] != c["unit"] or u["weightings"] != c["weightings"] or \
           norm(u["table_title"]) != norm(c["table_title"]):
            bad.append(u["unit"])
    d["bad"] = bad
    ok = (d["statements"] == 3 and d["unit_weightings"] == 3 and not bad)
    gate("G8_assessment_objectives_verbatim", ok, d)

    # ---- G9 chemistry graph_check still green --------------------------------------
    r = subprocess.run([sys.executable, str(HERE / "graph_check.py")],
                       capture_output=True, text=True)
    d = {"exit": r.returncode,
         "tail": (r.stdout or r.stderr).strip().splitlines()[-3:]}
    gate("G9_chemistry_graph_check_green", r.returncode == 0, d)

    # ---- G10 no-hardcode + multi-qual registry --------------------------------------
    r = subprocess.run([sys.executable, str(HERE / "check_no_hardcode.py")],
                       capture_output=True, text=True)
    d = {"exit": r.returncode,
         "registry_line": next((ln for ln in r.stdout.splitlines()
                                if ln.startswith("registry consistency")), "")}
    gate("G10_no_hardcode_registry_green", r.returncode == 0, d)

    result = {
        "schema": "syllabai.c30-k1-check/1.0",
        "task": "T-C30 K1 spec store build — igcse-maths-a (4MA1 Higher)",
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "head": subprocess.run(["git", "-C", str(REPO), "rev-parse", "HEAD"],
                               capture_output=True, text=True).stdout.strip(),
        "stores": {n: GP.store_rel(n, QUAL) for n in STORES},
        "gates": gates,
        "all_pass": all(g["status"] == "PASS" for g in gates.values()),
    }
    REPORT.write_text(json.dumps(result, indent=1) + "\n", encoding="utf-8")
    for name, g in gates.items():
        print(f"{g['status']:4}  {name}")
    print(f"ALL_PASS = {result['all_pass']}  ->  {REPORT}")
    return 0 if result["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
