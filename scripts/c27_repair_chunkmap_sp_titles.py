#!/usr/bin/env python3
"""C27 micro-repair: refresh spec_chunk_mappings.yaml sp_title labels from the
definitive specification store.

Defect (found by the C27 final all-store sweep): 211 chunk-map rows carry a
`sp_title` display label copied from the spec store at c13 build time
(2026-09-18, pre-C24). 84/211 labels drifted from the definitive
`graph/igcse-chemistry/specification_points` official_wording; 4 of them still carry
retired-lineage notation damage eliminated by C24 (inline-math $R_f$/$A_r$
forms and a CJK ideograph in 1.10) — i.e. graph/ retained exactly one store
deriving wording from the retired OCR lineage, contradicting the C26
"zero stores" unification. The mapping DECISIONS (spec_code, note, anchor,
evidence quotes, HUMAN_VALIDATED promotion) are untouched — only the derived
display label is re-sourced from the definitive wording.

Surgical per-row span edit; idempotent; deep-verified.
"""
import hashlib, json, os, re, subprocess, sys
import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import graph_paths as GP  # C28 §3.2 path registry — single source of ratified store paths

REPO = "/home/z/my-project/gh_repos/syllabai-resources"
CM = str(GP.store("spec_chunk_mappings"))
SP = str(GP.store("specification_points"))

def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()

def norm(s):
    return re.sub(r"\s+", " ", s or "").strip()

# 1. authoritative wording
sp_rows = yaml.safe_load(open(SP, encoding="utf-8"))["specification_points"]
wording = {r["code"]: r["official_wording"] for r in sp_rows}

# 2. current rows
cm = yaml.safe_load(open(CM, encoding="utf-8"))
rows = cm["rows"]
assert len(rows) == 211
byid = {r["mapping_id"]: r for r in rows}
drift = []
for r in rows:
    w = wording.get(r["spec_code"])
    assert w is not None, r["spec_code"]
    if norm(r["sp_title"]) != norm(w):
        drift.append((r["mapping_id"], r["sp_title"], w))
print(f"[scope] drifted sp_title rows: {len(drift)}/211")

# 3. raw-text span replacement (bottom-up)
raw = open(CM, encoding="utf-8").read()
lines = raw.splitlines(keepends=False)
id_at = {}
for i, l in enumerate(lines):
    m = re.match(r"^(\s*)- mapping_id: (\S+)\s*$", l)
    if m:
        id_at[m.group(2)] = i
assert len(id_at) == 211, len(id_at)

def sp_title_span(start, end):
    """Return (i0, i1) covering the sp_title key line + wrapped continuations."""
    i0 = None
    ind = None
    for i in range(start + 1, end):
        m = re.match(r"^(\s*)sp_title:", lines[i])
        if m:
            i0, ind = i, len(m.group(1))
            break
    assert i0 is not None, lines[start]
    i1 = end
    for i in range(i0 + 1, end):
        l = lines[i]
        if not l.strip():
            continue
        li = len(l) - len(l.lstrip())
        if li <= ind:
            i1 = i
            break
        if re.match(r"^\s*-?\s*[\w_]+:", l):
            i1 = i
            break
    return i0, i1, ind

# plan edits
edits = []
for mid, old, new in drift:
    start = id_at[mid]
    end = min((v for v in id_at.values() if v > start), default=len(lines))
    i0, i1, ind = sp_title_span(start, end)
    edits.append((i0, i1, " " * ind + "sp_title: " + json.dumps(new, ensure_ascii=False)))
# bottom-up application keeps indices valid
for i0, i1, newline in sorted(edits, key=lambda e: -e[0]):
    lines[i0:i1] = [newline]
out = "\n".join(lines) + ("\n" if raw.endswith("\n") else "")
assert len(edits) == len(drift)

# 4. meta lineage note (insert before top-level rows: line)
note = [
    f"  sp_title_wording_source: definitive {GP.store_rel('specification_points')} official_wording"
    " (C23 PDF-direct lineage; C24 respacing)",
    "  sp_title_refresh: 'C27 - 84/211 labels re-sourced from the definitive store;"
    " 4 carried retired-lineage notation damage (inline-math + CJK classes, pre-C24 wording)'",
]
mend = next(i for i, l in enumerate(lines) if l.startswith("rows:"))
# idempotency: only insert when note absent
if "sp_title_refresh:" not in raw:
    lines[mend:mend] = note
    out = "\n".join(lines) + ("\n" if raw.endswith("\n") else "")
    print("[meta] lineage note inserted")

pre_sha = hashlib.sha256(subprocess.run(["git", "-C", REPO, "show", f"HEAD:{GP.store_rel('spec_chunk_mappings')}"],
                                        capture_output=True).stdout).hexdigest()
open(CM, "w", encoding="utf-8").write(out)

# 5. deep verify
cm2 = yaml.safe_load(open(CM, encoding="utf-8"))
rows2 = cm2["rows"]
assert len(rows2) == 211
changed = 0
for r in rows2:
    w = wording[r["spec_code"]]
    assert norm(r["sp_title"]) == norm(w), (r["mapping_id"], r["sp_title"])
cm1 = yaml.safe_load(raw)["rows"]
for a, b in zip(cm1, rows2):
    da, db = dict(a), dict(b)
    oa, ob = da.pop("sp_title"), db.pop("sp_title")
    assert da == db, f"non-sp_title field changed in {a['mapping_id']}"
    if norm(oa) != norm(ob):
        changed += 1
assert changed == len(drift), (changed, len(drift))
print(f"[verify] 211 rows re-parsed; sp_title == definitive wording 211/211; "
      f"{changed} rows changed; every other field byte-identical in meaning")
post_sha = sha256(CM)
print(f"[pins] spec_chunk_mappings.yaml  pre={pre_sha[:16]}  post={post_sha[:16]}")
json.dump({"pre": pre_sha, "post": post_sha, "drifted": len(drift),
           "damage_rows": ["3e6b6d8628103928", "cabb0bb60b6450dd", "743c5006b4685a93", "c3d3cb1a632c338b"],
           "changed": [{"mapping_id": m, "from": o, "to": n} for m, o, n in drift]},
          open("/home/z/my-project/scripts/c27_repair_chunkmap_result.json", "w"), indent=1, ensure_ascii=False)
print("OK")
