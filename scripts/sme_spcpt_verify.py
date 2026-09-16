#!/usr/bin/env python3
"""T-SME-EQ-1 — post-apply verification for the spec-point resolution."""
from __future__ import annotations

import collections
import json
import random
import sys
from pathlib import Path

import yaml

BASE = Path("/home/z/my-project/download/syllabai-resources")
EQ = BASE / "SME-ExamQuestion"

reg_doc = yaml.safe_load((BASE / "graph" / "specification_points.yaml")
                         .read_text(encoding="utf-8"))
registry = {p["code"]: p for p in reg_doc["specification_points"]}

res = json.loads((EQ / "spec_point_resolution.json").read_text(encoding="utf-8"))
idx = json.loads((EQ / "spec_point_index.json").read_text(encoding="utf-8"))

errors: list[str] = []

# G1 every part with spec_point_ids has non-empty spec_point_codes, all in registry
parts = 0
no_ids = 0
code_hist: dict[str, int] = collections.Counter()
subtopic_files = sorted(EQ.glob("*/*/*/topic.json")) + sorted(
    EQ.glob("*/*/topic.json"))
for f in subtopic_files:
    t = json.loads(f.read_text(encoding="utf-8"))
    for q in t.get("questions", []):
        for part in q.get("parts", []):
            parts += 1
            sids = part.get("spec_point_ids") or []
            codes = part.get("spec_point_codes") or []
            if not sids:
                no_ids += 1
                if codes:
                    errors.append(f"{f}: part {part['id']} codes without ids")
                continue
            if not codes:
                errors.append(f"{f}: part {part['id']} ids without codes")
            for c in codes:
                if c not in registry:
                    errors.append(f"{f}: part {part['id']} foreign code {c}")
                code_hist[c] += 1

# G2 resolution table consistency
id2code = {r["id"]: r["resolved_code"] for r in res["resolved"]}
if len(id2code) != len(idx["spec_points"]):
    errors.append("resolution table size != index size")
for sid in idx["spec_points"]:
    if sid not in id2code:
        errors.append(f"unresolved index id {sid}")
for r in res["resolved"]:
    if r["resolved_code"] not in registry:
        errors.append(f"resolution code not in registry: {r['id']}")

# G3 every question-referenced id is covered
qid = idx["coverage"]["question_part_ids_total"]
if idx["coverage"]["covered_by_index"] != qid:
    errors.append("index coverage mismatch")

# G4 cross-check stats + code distribution per section
sec_hist: dict[str, int] = collections.Counter()
for code, n in code_hist.items():
    sec_hist[code.split("-")[1][0]] += n

print(f"parts total: {parts} (without spec_point_ids: {no_ids})")
print(f"distinct codes used by parts: {len(code_hist)}")
print("code references per section:",
      dict(sorted(sec_hist.items())))
print("top 10 codes by part references:")
for code, n in code_hist.most_common(10):
    print(f"  {code} x{n}  {registry[code]['official_wording'][:60]!r}")

c_suffix = [c for c in code_hist if c.endswith("C")]
print(f"C-suffixed (chemistry-only) codes used: {len(c_suffix)}")

# G5 random spot-check sample (deterministic seed)
random.seed(20260917)
sample = []
for f in subtopic_files:
    t = json.loads(f.read_text(encoding="utf-8"))
    for q in t.get("questions", []):
        for part in q.get("parts", []):
            if part.get("spec_point_codes"):
                sample.append((f, t, q, part))
picks = random.sample(sample, 5)
print("\nSPOT-CHECK (5 random parts):")
for f, t, q, part in picks:
    print(f"- {f.relative_to(EQ)} q={q['id']} part={part['id']} "
          f"marks={part.get('marks')}")
    print(f"  codes: {part['spec_point_codes']}")
    print(f"  sme ids: {part.get('spec_point_ids')}")
    print(f"  problem: {(part.get('problem_md') or '')[:90]!r}")
    for c in part["spec_point_codes"]:
        print(f"    {c}: {registry[c]['official_wording'][:90]!r}")

if errors:
    print("\nERRORS:", file=sys.stderr)
    for e in errors:
        print(" ", e, file=sys.stderr)
    sys.exit(1)
print("\nALL GATES PASSED")
