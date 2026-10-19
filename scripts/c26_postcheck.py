#!/usr/bin/env python3
"""T-C26 Phase-3 verification battery. Exit 0 only if ALL checks pass."""
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import graph_paths as GP  # C28 §3.2 path registry — single source of ratified store paths

ROOT = Path(__file__).resolve().parents[1]
G = GP.qual_dir()  # C28 registry-resolved ratified store dir
P = ROOT / "Official-Specifications/parsed/igcse-chemistry"
FAIL = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (f" | {detail}" if detail else ""))
    if not ok:
        FAIL.append(name)


def norm(s):
    return re.sub(r"\s+", " ", str(s)).strip()


def head(path):
    return subprocess.run(["git", "show", f"HEAD:{path}"], capture_output=True, text=True,
                          cwd=ROOT).stdout


def flat_docs(doc, list_keys=None):
    """code -> record for every list of dicts."""
    out = {}
    for k, v in doc.items():
        if k == "meta" or not isinstance(v, list):
            continue
        for r in v:
            if isinstance(r, dict) and "code" in r:
                out[r["code"]] = r
    return out


# ---- load new + old
names = ["topics", "practicals", "assessment_objectives", "command_words", "relationships"]
new = {n: yaml.safe_load((G / f"{n}.yaml").read_text(encoding="utf-8")) for n in names}
old = {n: yaml.safe_load(head(GP.store_rel(n))) for n in names}
ledger = json.loads((GP.reports_dir() / "C26_WORDING_DIFF_LEDGER.json").read_text(encoding="utf-8"))
can = {n: json.loads((P / f"{n}.json").read_text(encoding="utf-8"))
       for n in ("topics", "practicals", "assessment_objectives", "command_words")}

# ---- Check 1: counts preserved
exp = {"topics": (4, 28), "practicals": (12,), "assessment_objectives": (3, 2),
       "command_words": (25,), "relationships": (210,)}
c_ok = True
for n in names:
    lists = [len(v) for k, v in new[n].items() if isinstance(v, list)]
    if tuple(lists) != exp[n]:
        c_ok = False
        print(f"  {n}: {lists} != {exp[n]}")
check("1 counts preserved", c_ok, str(exp))

# ---- Check 2: semantic diff old->new is intended-only
ledger_paths = set()
for kind in ("wording_changes", "field_adoption", "identity_changes"):
    for e in ledger[kind]:
        ledger_paths.add((e["store"].replace(".yaml", ""), e["code"], e["field"].split(".")[0]))
WHITELIST_FIELDS = {"provenance", "damage_flags", "header_source", "summary", "title",
                    "definition", "command_word", "weighting_overall", "weighting_by_paper"}


def rec_paths(a, b, prefix=""):
    """yield changed leaf paths between two record dicts (shallow-ish)."""
    keys = set(a) | set(b)
    for k in sorted(keys):
        p = f"{prefix}.{k}" if prefix else k
        if k not in a:
            yield p, None, b[k]
        elif k not in b:
            yield p, a[k], None
        elif isinstance(a[k], dict) and isinstance(b[k], dict):
            yield from rec_paths(a[k], b[k], p)
        else:
            if a[k] != b[k]:
                yield p, a[k], b[k]


unexpected = []
for n in names:
    lo, ln = flat_docs(old[n]), flat_docs(new[n])
    assert set(lo) == set(ln), f"{n}: code set changed!"
    for code in lo:
        for p, a, b in rec_paths(lo[code], ln[code]):
            field = p.split(".")[0]
            if field in WHITELIST_FIELDS:
                if field in ("summary", "title", "definition", "command_word",
                             "weighting_overall", "weighting_by_paper"):
                    if (n, code, field) not in ledger_paths:
                        unexpected.append((n, code, p, "not in ledger"))
            else:
                unexpected.append((n, code, p, "non-whitelisted"))
# relationship edges have no codes: compare by index
lo_e, ln_e = old["relationships"]["edges"], new["relationships"]["edges"]
for i, (a, b) in enumerate(zip(lo_e, ln_e)):
    for p, x, y in rec_paths(a, b):
        unexpected.append(("relationships", f"edge[{i}]", p, "edge records must be untouched"))
# meta: only allowed keys may differ
META_ALLOWED = {"statement_text_policy", "generator", "generated", "source_documents",
                "definitive_lineage", "counts"}
for n in names:
    om, nm = old[n]["meta"], new[n]["meta"]
    for k in set(om) | set(nm):
        if om.get(k) != nm.get(k) and k not in META_ALLOWED:
            unexpected.append((n, "meta", k, "meta key changed outside allowlist"))
check("2 semantic diff = intended only", not unexpected, f"{len(unexpected)} unexpected: {unexpected[:5]}")

# ---- Check 2b: refreshed wording really equals canonical
pr_ok = True
cps = {int(x["ordering"]): x for x in can["practicals"]["practicals"]}
for pr in new["practicals"]["practicals"]:
    cv = re.sub(r"^practical:\s*", "", norm(cps[int(pr["ordering"])]["summary"]))
    if pr["code"] == "4CH1-PR-09":
        continue  # PDF-verified override, checked in 2c
    if norm(pr["summary"]) != cv:
        pr_ok = False
        print("  ", pr["code"], "summary != canonical")
cw_ok = True
cwk = {re.sub(r"[^a-z0-9]", "", norm(x["command_word"]).lower()): x for x in can["command_words"]["command_words"]}
for w in new["command_words"]["command_words"]:
    c = cwk[re.sub(r"[^a-z0-9]", "", norm(w["command_word"]).lower())]
    if norm(w["command_word"]) != norm(c["command_word"]) or norm(w["definition"]) != norm(c["definition"]):
        cw_ok = False
check("2b store wording == canonical (practicals, command_words)", pr_ok and cw_ok)

# ---- Check 2c: PDF-verified overrides present verbatim
a2 = [a for a in new["assessment_objectives"]["assessment_objectives"] if a["code"] == "4CH1-AO2"][0]
p9 = [p for p in new["practicals"]["practicals"] if p["code"] == "4CH1-PR-09"][0]
check("2c overrides verbatim",
      a2["weighting_overall"] == "38\u201342%"
      and p9["summary"].endswith("\u2022 combustion reactions.")
      and "bullet-colon" in json.dumps(ledger))

# ---- Check 3: damage-class sweep (stores + canonical + untouched-ness of derived)
pats = {"CJK": r"[\u4e00-\u9fff\u3400-\u4dbf]", "LaTeX": r"\$[^$\n]{1,60}\$",
        "fullwidth": r"[\u3000-\u303f\uff01-\uff5e\u3000]", "U+FFFD": r"\ufffd",
        "double-enc": r"[ÃÂ][\u0080-\u00ff]?", "esc": r"\\u[0-9a-fA-F]{4}"}
hits = []
texts = {GP.store_rel(n): (G / f"{n}.yaml").read_text(encoding="utf-8") for n in names}
texts[GP.store_rel("specification_points")] = (G / "specification_points.yaml").read_text(encoding="utf-8")
for f, t in texts.items():
    for pn, pp in pats.items():
        for m in re.finditer(pp, t):
            hits.append((f, pn))
for n in ("topics", "practicals", "assessment_objectives", "command_words"):
    t = (P / f"{n}.json").read_text(encoding="utf-8")
    for pn, pp in pats.items():
        if re.search(pp, t):
            hits.append((f"{n}.json(canonical)", pn))
check("3 damage-class sweep", not hits, str(hits[:4]))

# ---- Check 4: referential integrity
sp = yaml.safe_load((G / "specification_points.yaml").read_text(encoding="utf-8"))
codes = {x["code"] for x in sp["specification_points"]}
for n in ("topics", "practicals", "assessment_objectives"):
    for k, v in new[n].items():
        if isinstance(v, list):
            codes |= {r["code"] for r in v if isinstance(r, dict) and "code" in r}
eps = {e[k] for e in new["relationships"]["edges"] for k in ("from", "to")}
check("4a relationship endpoints resolve", eps <= codes, f"{len(eps)} endpoints")
sub_ok = all(set(st_.get("spec_points") or []) <= codes for st_ in new["topics"]["subtopics"])
check("4b subtopic spec_points refs resolve", sub_ok)

# ---- Check 5: meta audit
md_ocr = [n for n in names if "md OCR" in (G / f"{n}.yaml").read_text(encoding="utf-8")]
gens = {n: new[n]["meta"].get("generator", "") for n in names}
gen_ok = all(v == "scripts/c26_emit_definitive_sibling_stores.py" for v in gens.values())
sp_txt = (G / "specification_points.yaml").read_text(encoding="utf-8")
c09_misuse = []
for n in names:
    t = (G / f"{n}.yaml").read_text(encoding="utf-8")
    for line in t.splitlines():
        if "c09_spec_graph_extract" in line and "generated_by" not in line and "retired" not in line.lower() \
           and "reason" not in line and "extends" not in line:
            c09_misuse.append((n, line.strip()[:60]))
check("5 meta audit (no md OCR, live generators, c09 only as retired)",
      not md_ocr and gen_ok and not c09_misuse, f"md_ocr={md_ocr} c09_misuse={c09_misuse}")

# ---- Check 6: untouched files stay untouched
diff = subprocess.run(["git", "diff", "--name-only", "HEAD"], capture_output=True, text=True,
                      cwd=ROOT).stdout.split()
allowed = {f"graph/{n}.yaml" for n in names} | {"graph/reports/C26_WORDING_DIFF_LEDGER.json",
                                                "scripts/c26_emit_definitive_sibling_stores.py",
                                                "scripts/c26_field_map.yaml"}
stray = [f for f in diff if f not in allowed]
check("6 working-tree changes are intended only", not stray, str(stray))

print("=" * 50)
print("RESULT:", "ALL PASS" if not FAIL else f"FAILURES: {FAIL}")
sys.exit(1 if FAIL else 0)
