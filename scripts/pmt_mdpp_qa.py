#!/usr/bin/env python3
"""QA gate for the Markdown++ pilot batch before commit."""
import json, re, sys
from pathlib import Path
import yaml

ROOT = Path("/home/z/my-project/repos/syllabai-resources/PMT Edexcel IGCSE Chemistry Resources")
GRAPH = yaml.safe_load((Path(__file__).resolve().parents[1] / "graph" / "specification_points.yaml").read_text())

graph_codes = {p["code"] for p in GRAPH["specification_points"]}
split_codes, parents, errors = set(), 0, []

for idx in sorted(ROOT.glob("Unit */Notes (Markdown)/*/*.index.json")):
    d = json.loads(idx.read_text())
    doc_dir = idx.parent
    md = doc_dir / f"{d['docId']}.md"
    if not md.exists():
        errors.append(f"missing md: {md.name}"); continue
    parents += 1
    # front matter must parse as YAML and have required keys
    txt = md.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", txt, re.S)
    if not m:
        errors.append(f"bad front matter: {d['docId']}"); continue
    fm = yaml.safe_load(m.group(1))
    for k in ("docId", "type", "provider", "sourceSha256", "pages", "specRefs", "splits"):
        if k not in fm:
            errors.append(f"missing fm key {k}: {d['docId']}")
    # images referenced must exist
    for img in re.findall(r"!\[[^\]]*\]\((images/[^)]+)\)", txt):
        if not (doc_dir / img).exists():
            errors.append(f"missing image {img}: {d['docId']}")
    # splits: front matter + specRef in graph + parent link
    for sp in sorted((doc_dir / "spec").glob("*.md")):
        st = sp.read_text()
        sm = re.match(r"^---\n(.*?)\n---\n", st, re.S)
        if not sm:
            errors.append(f"bad split fm: {sp}"); continue
        sfm = yaml.safe_load(sm.group(1))
        if sfm.get("specRef") not in graph_codes:
            errors.append(f"foreign specRef: {sfm.get('specRef')}")
        if sfm.get("parent") != d["docId"]:
            errors.append(f"bad parent link: {sp}")
        if sfm.get("specRef") in split_codes:
            errors.append(f"duplicate specRef split: {sfm['specRef']}")
        split_codes.add(sfm.get("specRef"))

missing = graph_codes - split_codes
extra = split_codes - graph_codes
print(f"parents: {parents}/28 | split files: {len(split_codes)}")
print(f"bijection vs graph (182): missing={len(missing)} extra={len(extra)}")
if missing: print("  missing:", sorted(missing)[:10])
if extra: print("  extra:", sorted(extra)[:10])
if errors:
    print(f"ERRORS ({len(errors)}):"); [print(" ", e) for e in errors[:20]]
    sys.exit(1)
if missing or extra:
    sys.exit(2)
print("QA: PASS — parents, front matter, images, parent links, bijection all OK")
