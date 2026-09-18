#!/usr/bin/env python3
"""T-SME-EQ-1 / T-SPEC-2 — post-apply verification for spec-point resolution.

Course-aware and registry-per-course:
  - a course carrying spec_point_resolution.json + spec_point_index.json (a
    "sidecar course") is verified: every part with spec_point_ids must have
    spec_point_codes, and every code must belong to the course's OWN official
    universe — igcse-chemistry-19 verifies against graph/specification_points.yaml
    (4CH1, unchanged), sibling courses verify against
    Official-Specifications/parsed/<qual>/spec_points.json
  - parts whose ids are ALL unresolved stay uncoded by design (no-guess
    discipline); they pass only when every id appears in the sidecar's
    resolved table with resolved_code null (the unresolved allowlist) — any
    other uncoded part is a hard error
  - courses without sidecar files have ids awaiting a future apply pass and
    are counted, not enforced

Original single-course paths assumed an EQ-root layout that was never
committed (latent defect fixed 2026-09-18, T-SPEC-1); single-registry
assumption extended to per-course registries (T-SPEC-2, 2026-09-18).
"""
from __future__ import annotations

import collections
import json
import random
import sys
from pathlib import Path

import yaml

BASE = Path("/home/z/my-project/download/syllabai-resources")
EQ = BASE / "SME-ExamQuestion"
PARSED = BASE / "Official-Specifications" / "parsed"

# ---------- per-course registries ----------

def linear_registry() -> dict[str, dict]:
    reg_doc = yaml.safe_load((BASE / "graph" / "specification_points.yaml")
                             .read_text(encoding="utf-8"))
    return {p["code"]: p for p in reg_doc["specification_points"]}


def parsed_registry(qual: str, scope: str | None = None) -> dict[str, dict]:
    pts = json.loads((PARSED / qual / "spec_points.json")
                     .read_text(encoding="utf-8"))["spec_points"]
    if scope:
        scoped = [p for p in pts if p.get("scope") == scope]
        pts = scoped or pts  # single-subject parses carry no scope field
    return {p["official_code"]: p for p in pts}


def course_registry(course: str, qual: str) -> dict[str, dict]:
    if course == "igcse-chemistry-19":
        return linear_registry()
    scope = None
    for s in ("biology", "chemistry", "physics"):
        if course.endswith("-" + s):
            scope = s.capitalize()
            break
    return parsed_registry(qual, scope)


COURSES = sorted(p.name for p in EQ.iterdir()
                 if p.is_dir() and (p / "spec_point_resolution.json").exists()
                 and (p / "spec_point_index.json").exists())
if not COURSES:
    print("no courses carry spec_point_resolution.json + spec_point_index.json",
          file=sys.stderr)
    sys.exit(1)

REG = {}
UNRESOLVED = {}
RES_DOC = {}
for course in COURSES:
    res = json.loads((EQ / course / "spec_point_resolution.json")
                     .read_text(encoding="utf-8"))
    RES_DOC[course] = res
    qual = json.loads((EQ / course / "spec_point_map.json")
                      .read_text(encoding="utf-8"))["qual"]
    REG[course] = course_registry(course, qual)
    UNRESOLVED[course] = {r["id"] for r in res["resolved"]
                          if not r.get("resolved_code")}


def course_of(f: Path) -> str:
    return f.relative_to(EQ).parts[0]


errors: list[str] = []

# G1 every part with spec_point_ids has non-empty spec_point_codes, all in the
# course's own registry. Uncoded parts pass only via the unresolved allowlist.
parts = 0
no_ids = 0
unapplied_no_codes = 0
allowlisted = 0
code_hist: dict[str, int] = collections.Counter()
subtopic_files = sorted(EQ.glob("*/*/*/topic.json")) + sorted(
    EQ.glob("*/*/topic.json"))
for f in subtopic_files:
    course = course_of(f)
    applied = course in COURSES
    registry = REG.get(course, {})
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
                if applied:
                    if all(s in UNRESOLVED[course] for s in sids):
                        allowlisted += 1
                    else:
                        errors.append(f"{f}: part {part['id']} ids without codes")
                else:
                    unapplied_no_codes += 1
                continue
            for c in codes:
                if c not in registry:
                    errors.append(f"{f}: part {part['id']} foreign code {c}")
                code_hist[(course, c)] += 1

# G2 resolution table consistency per course
for course in COURSES:
    cdir = EQ / course
    res = RES_DOC[course]
    idx = json.loads((cdir / "spec_point_index.json").read_text(encoding="utf-8"))
    id2code = {r["id"]: r.get("resolved_code") for r in res["resolved"]}
    if len(id2code) != len(idx["spec_points"]):
        errors.append(f"{course}: resolution table size != index size")
    for sid in idx["spec_points"]:
        if sid not in id2code:
            errors.append(f"{course}: unresolved index id {sid}")
    for r in res["resolved"]:
        code = r.get("resolved_code")
        if code and code not in REG[course]:
            errors.append(f"{course}: resolution code not in registry: {r['id']}")
        if not code and not r.get("reason"):
            errors.append(f"{course}: unresolved id without reason: {r['id']}")

    # G3 every question-referenced id is covered
    qid = idx["coverage"]["question_part_ids_total"]
    if idx["coverage"]["covered_by_index"] != qid:
        errors.append(f"{course}: index coverage mismatch")

# G4 cross-check stats + code distribution per section
sec_hist: dict[str, int] = collections.Counter()
for (course, code), n in code_hist.items():
    entry = REG[course].get(code) or {}
    sec = None
    if course == "igcse-chemistry-19" and "-" in code:
        sec = code.split("-")[1][0]
    else:
        tp = (entry.get("topic") or {}).get("number")
        sec = str(tp)[:1] if tp is not None else None
    if sec:
        sec_hist[sec] += n

print(f"courses verified: {', '.join(COURSES)}")
print(f"parts total: {parts} (without spec_point_ids: {no_ids}; "
      f"ids awaiting apply pass (non-sidecar courses): {unapplied_no_codes}; "
      f"allowlisted unresolved (no-guess tail): {allowlisted})")
print(f"distinct codes used by parts: "
      f"{len({c for (_, c) in code_hist})}")
print("code references per section:",
      dict(sorted(sec_hist.items())))
print("top 10 codes by part references:")
reg_first = {}
for (course, code), n in code_hist.most_common(10):
    wording = (REG[course].get(code) or {}).get("official_wording") \
        or (REG[course].get(code) or {}).get("text") or ""
    print(f"  {code} x{n}  {wording[:60]!r}")

c_suffix = [c for (_, c) in code_hist if c.endswith("C")]
print(f"C-suffixed (chemistry-only) codes used: {len(c_suffix)}")

# G5 random spot-check sample (deterministic seed)
random.seed(20260917)
sample = []
for f in subtopic_files:
    if course_of(f) not in COURSES:
        continue
    t = json.loads(f.read_text(encoding="utf-8"))
    for q in t.get("questions", []):
        for part in q.get("parts", []):
            if part.get("spec_point_codes"):
                sample.append((f, t, q, part))
picks = random.sample(sample, 5)
print("\nSPOT-CHECK (5 random parts):")
for f, t, q, part in picks:
    course = course_of(f)
    print(f"- {f.relative_to(EQ)} q={q['id']} part={part['id']} "
          f"marks={part.get('marks')}")
    print(f"  codes: {part['spec_point_codes']}")
    print(f"  sme ids: {part.get('spec_point_ids')}")
    print(f"  problem: {(part.get('problem_md') or '')[:90]!r}")
    for c in part["spec_point_codes"]:
        entry = REG[course].get(c) or {}
        w = entry.get("official_wording") or entry.get("text") or ""
        print(f"    {c}: {w[:90]!r}")

if errors:
    print("\nERRORS:", file=sys.stderr)
    for e in errors:
        print(" ", e, file=sys.stderr)
    sys.exit(1)
print("\nALL GATES PASSED")
