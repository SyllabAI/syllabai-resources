#!/usr/bin/env python3
"""C27 micro-repair: assessment_objectives.yaml shared weighting_by_paper matrix.

Defect (found by the C27 final all-store sweep): the anchored AO x paper matrix
(paper_1: &id001 / paper_2: &id002, aliased into AO2/AO3) carried the AO3 column
values in the ao1/ao2 cells for both papers:
    paper_1: ao1=11.6-12.8%  ao2=11.6-12.8%  ao3=11.6-12.8%   (ao1/ao2 WRONG)
    paper_2: ao1=7.4-8.2%    ao2=7.4-8.2%    ao3=7.4-8.2%     (ao1/ao2 WRONG)
Ground truth (PDF p35, pdftotext-verified; canonical assessment_objectives.json
unit_weightings; C26 field map adopted_fields contract):
    paper_1: ao1=23.2-25.7%  ao2=23.2-25.7%  ao3=11.6-12.8%
    paper_2: ao1=14.8-16.3%  ao2=14.8-16.3%  ao3=7.4-8.2%
Internal-consistency proof: AO1/AO2 23.2-25.7 + 14.8-16.3 = 38.0-42.0 == weighting_overall
38-42%; AO3 11.6-12.8 + 7.4-8.2 = 19.0-21.0 == weighting_overall 19-21%.

Surgical text edit only (anchor/alias structure preserved; no YAML re-serialisation).
"""
import hashlib, json, os, re, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import graph_paths as GP  # C28 §3.2 path registry — single source of ratified store paths

REPO = "/home/z/my-project/gh_repos/syllabai-resources"
STORE = str(GP.store("assessment_objectives"))
CANON = f"{REPO}/Official-Specifications/parsed/igcse-chemistry/assessment_objectives.json"
PDF = f"{REPO}/Official-Specifications/igcse-chemistry/international-gcse-chemistry-2017-specification.pdf"

def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()

# 1. ground truth from canonical
_uw = json.load(open(CANON, encoding="utf-8"))["unit_weightings"]
_uw = [u for u in _uw if not str(u["unit"]).lower().startswith("total")]
assert len(_uw) == 2, _uw
p1, p2 = _uw[0]["weightings"], _uw[1]["weightings"]
assert p1 == ["23.2\u201325.7%", "23.2\u201325.7%", "11.6\u201312.8%"], p1
assert p2 == ["14.8\u201316.3%", "14.8\u201316.3%", "7.4\u20138.2%"], p2

# 2. ground truth from the PDF text layer (page 35)
txt = subprocess.run(["pdftotext", "-f", "35", "-l", "35", "-layout", PDF, "-"],
                     capture_output=True, text=True).stdout
for want in ("Chemistry Paper 1", "23.2–25.7%", "11.6–12.8%", "14.8–16.3%", "7.4–8.2%",
             "38–42%", "19–21%"):
    assert want in txt, f"PDF p35 missing {want!r}"
row1 = re.search(r"Chemistry Paper 1\s+(\S+)\s+(\S+)\s+(\S+)", txt)
row2 = re.search(r"Chemistry Paper 2\s+(\S+)\s+(\S+)\s+(\S+)", txt)
assert row1 and list(row1.groups()) == p1, row1 and row1.groups()
assert row2 and list(row2.groups()) == p2, row2 and row2.groups()
print("[verify] canonical unit_weightings == PDF p35 rows == field-map contract")

# 3. pre-state capture (idempotent: skip write if repair already applied)
#    honest pre-pin always = committed HEAD blob (pre-repair state)
_blob = subprocess.run(["git", "-C", REPO, "show", f"HEAD:{GP.store_rel('assessment_objectives')}"],
                       capture_output=True)
if _blob.returncode == 0:
    pre_sha = hashlib.sha256(_blob.stdout).hexdigest()
else:
    pre_sha = sha256(STORE)
raw = open(STORE, encoding="utf-8").read()
old_block = """    paper_1: &id001
      ao1: 11.6–12.8%
      ao2: 11.6–12.8%
      ao3: 11.6–12.8%
    paper_2: &id002
      ao1: 7.4–8.2%
      ao2: 7.4–8.2%
      ao3: 7.4–8.2%"""
new_block = """    paper_1: &id001
      ao1: 23.2–25.7%
      ao2: 23.2–25.7%
      ao3: 11.6–12.8%
    paper_2: &id002
      ao1: 14.8–16.3%
      ao2: 14.8–16.3%
      ao3: 7.4–8.2%"""
old_note = """    note: AO titles verbatim; weightings PDF en-dash verbatim (AO2 resolved via Total row + arithmetic);
      papers block is ratified overlay (no canonical source)"""
new_note = """    note: AO titles verbatim; weightings PDF en-dash verbatim (AO2 resolved via Total row + arithmetic);
      papers block is ratified overlay (no canonical source); C27 repaired the shared weighting_by_paper
      matrix (ao1/ao2 cells carried the AO3 column values; rebuilt from canonical unit_weightings,
      PDF p35 verified)"""
if old_block in raw:
    assert raw.count(old_block) == 1, f"anchor block count = {raw.count(old_block)}"
    assert raw.count(old_note) == 1, f"meta note count = {raw.count(old_note)}"
    out = raw.replace(old_block, new_block).replace(old_note, new_note)
    open(STORE, "w", encoding="utf-8").write(out)
    print("[repair] applied (4 anchor value lines + meta lineage note)")
elif new_block in raw and "C27 repaired the shared weighting_by_paper" in raw:
    print("[repair] already applied — verify-only pass")
else:
    raise SystemExit("FATAL: neither pre- nor post-repair structure found — aborting")

# 4. arithmetic self-consistency of the new matrix
def ends(s):
    a, b = s.replace("%", "").split("–")
    return float(a), float(b)
lo1 = round(ends(p1[0])[0] + ends(p2[0])[0], 1); hi1 = round(ends(p1[0])[1] + ends(p2[0])[1], 1)
lo3 = round(ends(p1[2])[0] + ends(p2[2])[0], 1); hi3 = round(ends(p1[2])[1] + ends(p2[2])[1], 1)
assert f"{lo1}-{hi1}" == "38.0-42.0" and f"{lo3}-{hi3}" == "19.0-21.0", (lo1, hi1, lo3, hi3)
print(f"[verify] arithmetic: AO1/AO2 {lo1}-{hi1} == 38–42%; AO3 {lo3}-{hi3} == 19–21%")

# 5. post-verify structure
import yaml
d = yaml.safe_load(open(STORE, encoding="utf-8"))
aos = d["assessment_objectives"]
expected = {"paper_1": {"ao1": p1[0], "ao2": p1[1], "ao3": p1[2]},
            "paper_2": {"ao1": p2[0], "ao2": p2[1], "ao3": p2[2]}}
for r in aos:
    assert r["weighting_by_paper"] == expected, (r["code"], r["weighting_by_paper"])
raw2 = open(STORE, encoding="utf-8").read()
assert raw2.count("&id001") == 1 and raw2.count("&id002") == 1, "anchor structure broken"
assert raw2.count("*id001") == 2 and raw2.count("*id002") == 2, "alias structure broken"
assert "C27 repaired the shared weighting_by_paper" in raw2, "meta repair note missing"
assert len(d["papers"]) == 2
print("[verify] all 3 AO records carry the corrected matrix; anchor + 2x alias structure preserved")
post_sha = sha256(STORE)
print(f"[pins] assessment_objectives.yaml  pre={pre_sha[:16]}  post={post_sha[:16]}")
json.dump({"pre": pre_sha, "post": post_sha,
           "changed_lines": {"paper_1.ao1": ["11.6–12.8%", "23.2–25.7%"],
                              "paper_1.ao2": ["11.6–12.8%", "23.2–25.7%"],
                              "paper_2.ao1": ["7.4–8.2%", "14.8–16.3%"],
                              "paper_2.ao2": ["7.4–8.2%", "14.8–16.3%"]},
           "verification": {"pdf_page": 35, "canonical_unit_weightings": [p1, p2],
                             "arithmetic": {"AO1_AO2": "38.0-42.0", "AO3": "19.0-21.0"}}},
          open("/home/z/my-project/scripts/c27_repair_ao_result.json", "w"), indent=1, ensure_ascii=False)
print("OK")
