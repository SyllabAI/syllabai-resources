#!/usr/bin/env python3
"""T-SPECS-9696-4HI1 finalize: 3-file split for igcse-history + parse_report +
_summary.json reconstruction (origin 56 rows preserved deep-equal + 2 new)."""
import json, subprocess, datetime, hashlib, sys

REPO = "/home/z/my-project/lane-tspecs-fill"
PDIR = f"{REPO}/Official-Specifications/parsed"

def gshow(rev, path):
    r = subprocess.run(["git", "-C", REPO, "show", f"{rev}:{path}"],
                       capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None

def sha1_of(path):
    h = hashlib.sha1()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()

ORIGIN = "origin/main"
now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")

# ---------- load the two new parses ----------
hi = json.load(open(f"{PDIR}/igcse-history/int-gcse-history-specification.parsed.json"))
geo = json.load(open(f"{PDIR}/cie-a-level-geography-2025-2026/664556-2025-2026-syllabus.parsed.json"))
hi_rep = json.load(open(f"{PDIR}/igcse-history/parse_report.json")) if False else None
geo_rep = json.load(open(f"{PDIR}/cie-a-level-geography-2025-2026/parse_report.json"))

def gates(doc):
    ids = [p["id"] for p in doc["spec_points"]]
    prov_ok = all(p.get("page") is not None and p.get("oy") is not None for p in doc["spec_points"])
    prefix = doc["id"].replace("-", "_").upper() + ":"
    return {
        "G1_schema_present": doc.get("schema") == "syllabai.parsed-specification/1.0",
        "G2_ids_unique": len(ids) == len(set(ids)),
        "G3_provenance_complete": prov_ok,
        "G4_id_prefix_valid": all(i.startswith(prefix) for i in ids),
    }

g_hi, g_geo = gates(hi), gates(geo)
assert all(g_hi.values()), g_hi
assert all(g_geo.values()), g_geo
print("gates igcse-history:", g_hi)
print("gates 9696:", g_geo)

# ---------- 3-file split: igcse-history ----------
pdf_sha = sha1_of(f"{REPO}/Official-Specifications/igcse-history/int-gcse-history-specification.pdf")
pts_rows = []
for p in hi["spec_points"]:
    row = {
        "id": p["id"], "official_code": p["official_code"], "scope": p.get("scope"),
        "text": p["text"],
        "topic": {"number": p["topic"]["number"], "title": p["topic"]["title"],
                  "page": p["topic"]["page"], "oy": p["topic"]["oy"]},
        "subsection": {"code": p["subsection"]["code"], "letter": p["subsection"]["code"],
                       "title": p["subsection"]["title"],
                       "page": p["subsection"]["page"], "oy": p["subsection"]["oy"]},
        "sub_items": p.get("sub_items", []), "practical": False,
        "ordering": p["ordering"],
        "provenance": {"pdf_sha1": pdf_sha, "page": p["page"], "oy": p["oy"]},
        "flags": p.get("flags", []),
    }
    pts_rows.append(row)
spec_points_doc = {
    "schema": "syllabai.parsed-specification/1.0",
    "id": "igcse-history",
    "qualification": "Edexcel International GCSE History",
    "spec_codes": ["4HI1"], "issue": "5",
    "family": hi["family"],
    "source": hi["source"],
    "spec_points": pts_rows,
    "counts": dict(hi["counts"], practicals=0),
}
topics_doc = {
    "schema": "syllabai.parsed-specification/1.0",
    "id": "igcse-history",
    "source": hi["source"],
    "topics": [
        {"code": f"4HI1-T{t['number']}", "number": t["number"], "title": t["title"],
         "ordering": t["ordering"],
         "provenance": {"pdf_sha1": pdf_sha, "page": t["page"], "oy": t["oy"]},
         "scope": t.get("scope")}
        for t in hi["topics"]
    ],
    "subsections": [
        {"code": f"4HI1-SUB{s['code']}", "letter": s["code"], "title": s["title"],
         "page": s["page"],
         "provenance": {"pdf_sha1": pdf_sha, "page": s["page"], "oy": s["oy"]}}
        for s in hi["subsections"]
    ],
    "counts": {"topics": len(hi["topics"]), "subsections": len(hi["subsections"])},
}
with open(f"{PDIR}/igcse-history/spec_points.json", "w") as f:
    json.dump(spec_points_doc, f, indent=1, ensure_ascii=False)
with open(f"{PDIR}/igcse-history/topics.json", "w") as f:
    json.dump(topics_doc, f, indent=1, ensure_ascii=False)

# ---------- parse_report.json for igcse-history (mirror igcse-chemistry shape) ----------
report = {
    "qual": "igcse-history",
    "generated_utc": now,
    "parser": "spec-parser-1.0 (family option_rows, T-SPECS-9696-4HI1)",
    "files": ["int-gcse-history-specification.parsed.json",
              "spec_points.json", "topics.json"],
    "counts": {"int-gcse-history-specification.parsed.json": dict(hi["counts"])},
    "totals": {"spec_points": hi["counts"]["spec_points"],
               "flagged": hi["counts"]["flagged"]},
    "gates": {**g_hi, "ALL_PASS": all(g_hi.values())},
    "duplicate_ids": [],
    "sme_crossref": {
        "status": "not_applicable",
        "note": "no SME bank exists for igcse-history-17 (registered course) — "
                "count-parity triangulation n/a; content spot-verified against "
                "the PDF text layer in-lane (21 options x 5 rows ground truth)",
    },
}
with open(f"{PDIR}/igcse-history/parse_report.json", "w") as f:
    json.dump(report, f, indent=1, ensure_ascii=False)

# ---------- _summary.json reconstruction ----------
origin_rows = json.loads(gshow(ORIGIN, "Official-Specifications/parsed/_summary.json"))
assert isinstance(origin_rows, list) and len(origin_rows) == 56, len(origin_rows)
edexcel = [r for r in origin_rows if not str(r.get("qual", "")).startswith("cie-")]
cie = [r for r in origin_rows if str(r.get("qual", "")).startswith("cie-")]
assert len(edexcel) == 23 and len(cie) == 33, (len(edexcel), len(cie))
new_geo = {"qual": "cie-a-level-geography-2025-2026",
           "pdf": "664556-2025-2026-syllabus",
           "counts": geo["counts"],
           "gates_all_pass": all(g_geo.values())}
new_hi = {"qual": "igcse-history",
          "pdf": "int-gcse-history-specification",
          "counts": hi["counts"],
          "gates_all_pass": all(g_hi.values())}
cie_kept = [r for r in cie if r["qual"] != "cie-a-level-geography-2025-2026"]
edexcel_kept = [r for r in edexcel if r["qual"] != "igcse-history"]
merged = edexcel_kept + cie_kept + [new_geo, new_hi]
assert len(merged) == 58, len(merged)
with open(f"{PDIR}/_summary.json", "w") as f:
    json.dump(merged, f, indent=1)
# deep-equal proof for the preserved rows
final = json.load(open(f"{PDIR}/_summary.json"))
by_q = {r["qual"]: r for r in final}
for r in origin_rows:
    q = r["qual"]
    if q in ("cie-a-level-geography-2025-2026", "igcse-history"):
        continue
    assert by_q[q] == r, f"row drifted: {q}"
print("_summary.json: 58 rows, 56 origin rows deep-equal, +2 new")

# ---------- verify the split feeds the spine builder contract ----------
assert spec_points_doc["spec_points"][0]["topic"]["number"] in ("1",)
assert all(isinstance(r["ordering"], int) for r in pts_rows)
print("OK: split + report + summary written")
