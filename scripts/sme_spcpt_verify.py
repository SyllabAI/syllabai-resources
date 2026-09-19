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
    if qual in ("igcse-accounting", "igcse-geography", "igcse-english-literature",
                "igcse-english-language-a"):
        # T-SPEC-7: these parses carry statements without official_code;
        # registries key by the id suffix (e.g. S4.071, C1T07) and that
        # suffix is the resolved_code written on parts
        pts = json.loads((PARSED / qual / "spec_points.json")
                         .read_text(encoding="utf-8"))["spec_points"]
        if scope:
            scoped = [p for p in pts if p.get("scope") == scope]
            pts = scoped or pts
        return {p["id"].rsplit(":", 1)[-1]: p for p in pts}
    return parsed_registry(qual, scope)


COURSES = sorted(p.name for p in EQ.iterdir()
                 if p.is_dir() and (p / "spec_point_resolution.json").exists()
                 and (p / "spec_point_index.json").exists())
if not COURSES:
    print("no courses carry spec_point_resolution.json + spec_point_index.json",
          file=sys.stderr)
    sys.exit(1)

# Unit-scoped regime (T-SPEC-6 IAL maths): the course map carries unit_scope;
# the qualification parse carries unit-prefixed ids (IAL_MATHS:P1-1.1 ...).
# For these courses G1 checks part codes by exact derivation from the part's
# own tag ids via the resolution sidecar, and G2 additionally checks the
# (official_id, official_code) pair against the full qualification registry.
UNIT_SCOPED: dict[str, str] = {}
REG_BY_ID: dict[str, dict] = {}
REG = {}
UNRESOLVED = {}
RES_DOC = {}
for course in COURSES:
    res = json.loads((EQ / course / "spec_point_resolution.json")
                     .read_text(encoding="utf-8"))
    RES_DOC[course] = res
    mp = json.loads((EQ / course / "spec_point_map.json")
                    .read_text(encoding="utf-8"))
    qual = mp["qual"]
    unit_scope = mp.get("unit_scope")
    REG[course] = course_registry(course, qual)
    if unit_scope and qual in ("ial-maths", "igcse-maths-a-modular"):
        # T-SPEC-6 IAL maths + T-SPEC-7 modular maths-a: unit-scoped lanes
        # verify against the full qualification registry by code, with the
        # (official_id, official_code) pair check in G2
        UNIT_SCOPED[course] = unit_scope
        pts = json.loads((PARSED / qual / "spec_points.json")
                         .read_text(encoding="utf-8"))["spec_points"]
        REG[course] = {p["official_code"]: p for p in pts}
        REG_BY_ID[course] = {p["id"]: p for p in pts}
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
            if course in UNIT_SCOPED:
                # exact derivation: part codes must equal the codes derived
                # from the part's own tag ids via the resolution sidecar
                id2code = {r["id"]: r.get("resolved_code")
                           for r in RES_DOC[course]["resolved"]}
                derived = {id2code[s] for s in sids if id2code.get(s)}
                if not derived:
                    if all(s in UNRESOLVED[course] for s in sids):
                        allowlisted += 1
                    else:
                        errors.append(f"{f}: part {part['id']} ids without codes")
                    continue
                if set(codes) != derived:
                    errors.append(f"{f}: part {part['id']} codes {sorted(codes)} "
                                  f"!= id-derived {sorted(derived)}")
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
        if course == "igcse-maths-a-18-foundation" and code:
            # T-SPEC-7: the Foundation lane's pool excludes Higher-only
            # statements (scope 'H' in the igcse-maths-a parse)
            oid = r.get("official_id") or ""
            pts_by_id = {p["id"]: p for p in json.loads(
                (PARSED / "igcse-maths-a" / "spec_points.json")
                .read_text(encoding="utf-8"))["spec_points"]}
            p = pts_by_id.get(oid)
            if p and p.get("scope") == "H":
                errors.append(f"{course}: Higher-only statement {code} "
                              f"resolved on the Foundation lane: {r['id']}")
        if not code and not r.get("reason"):
            errors.append(f"{course}: unresolved id without reason: {r['id']}")
        if course in UNIT_SCOPED:
            oid = r.get("official_id")
            if code and oid:
                p = REG_BY_ID[course].get(oid)
                if not p or p["official_code"] != code:
                    errors.append(f"{course}: resolution {r['id']} "
                                  f"(official_id, code) pair mismatch")

    # G3 every question-referenced id is covered; lanes whose harvest index
    # carries an explicit missing_from_index tail (enumerated, T-SPEC-7
    # index repair documentation) pass on the arithmetic
    qid = idx["coverage"]["question_part_ids_total"]
    nmiss = len(idx["coverage"].get("missing_from_index") or [])
    if idx["coverage"]["covered_by_index"] + nmiss != qid:
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
