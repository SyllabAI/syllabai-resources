#!/usr/bin/env python3
"""T-SPECS-CIE-1 — verification battery (C1-C7) + record emission.

C1  per-PDF integrity: sha1(spec.json) == sha1(pdf on disk), %PDF magic,
    bytes match, pypdf pages == spec.json pages
C2  manifest <-> spec.json two-way consistency over the 33 CIE entries
C3  lane coverage: the 44 cie-* lanes from the SME-ExamQuestion registry
    appear in EXACTLY ONE CIE entry's sme_courses
C4  Edexcel byte-stability: 23 pre-change entries match the sha256 snapshot
C5  cover_code sanity: every CIE entry has a 4-digit cover_code != "?" and a
    parseable edition_window
C6  totals: qualifications == 56 (23 Edexcel + 33 CIE), sme_courses_covered
    == 93, missing_courses == []
C7  footprint guard: git status touches ONLY the declared lane footprint

Output: graph/reports/T_SPECS_CIE_1_CHECK.json — exit 0 iff ALL PASS.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import pypdf

REPO = Path("/home/z/my-project/syllabai-resources")
OUT = REPO / "Official-Specifications"
SNAP = REPO / "scripts" / "cie_spec_edexcel_snapshot.json"
REPORT = REPO / "graph" / "reports"

FOOTPRINT_PREFIXES = (
    "Official-Specifications/", "scripts/cie_spec_",
    "graph/reports/T_SPECS_CIE_1_", "LICENSE-DATA.md",
)


def git(*args: str) -> str:
    return subprocess.run(["git", "-C", str(REPO), *args],
                          capture_output=True, text=True, check=True).stdout


def sha1_file(p: Path) -> str:
    return hashlib.sha1(p.read_bytes()).hexdigest()


def main() -> int:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    manifest = json.loads((OUT / "manifest.json").read_text())
    quals = manifest["qualifications"]
    cie = [e for e in quals if e.get("board") == "cambridge-cie"]
    edx = [e for e in quals if not e.get("board") == "cambridge-cie"]
    checks: dict[str, dict] = {}

    # C1 + C5 per PDF
    c1_fails, c5_fails = [], []
    for e in cie:
        qdir = OUT / e["slug"]
        pdf = qdir / e["pdf"]
        try:
            if sha1_file(pdf) != e["sha1"]:
                c1_fails.append(f"{e['slug']}: sha1 mismatch")
            if not pdf.read_bytes()[:5].startswith(b"%PDF-"):
                c1_fails.append(f"{e['slug']}: not a PDF")
            if pdf.stat().st_size != e["bytes"]:
                c1_fails.append(f"{e['slug']}: bytes mismatch")
            pages = len(pypdf.PdfReader(str(pdf)).pages)
            if pages != e["pages"]:
                c1_fails.append(f"{e['slug']}: pages {pages} != {e['pages']}")
        except Exception as exc:  # noqa: BLE001
            c1_fails.append(f"{e['slug']}: {exc!r}")
        if not (isinstance(e.get("cover_code"), str)
                and e["cover_code"].isdigit() and len(e["cover_code"]) == 4):
            c5_fails.append(f"{e['slug']}: cover_code={e.get('cover_code')}")
        if not (isinstance(e.get("edition_window"), str)
                and e["edition_window"] != "unknown"):
            c5_fails.append(f"{e['slug']}: edition_window={e.get('edition_window')}")
    checks["C1_pdf_integrity"] = {"pass": not c1_fails, "fails": c1_fails, "n": len(cie)}
    checks["C5_cover_and_window"] = {"pass": not c5_fails, "fails": c5_fails, "n": len(cie)}

    # C2 manifest <-> spec.json two-way
    c2_fails = []
    spec_by_slug = {}
    for spec_path in OUT.glob("cie-*/spec.json"):
        rec = json.loads(spec_path.read_text())
        spec_by_slug[rec["slug"]] = rec
    man_by_slug = {e["slug"]: e for e in cie}
    for slug, rec in spec_by_slug.items():
        m = man_by_slug.get(slug)
        if not m:
            c2_fails.append(f"{slug}: spec.json not in manifest")
        elif m["sha1"] != rec["sha1"]:
            c2_fails.append(f"{slug}: manifest/spec sha1 divergence")
    for slug in man_by_slug:
        if slug not in spec_by_slug:
            c2_fails.append(f"{slug}: manifest entry has no spec.json")
    if len(spec_by_slug) != 33 or len(man_by_slug) != 33:
        c2_fails.append(f"counts: spec.json={len(spec_by_slug)} manifest={len(man_by_slug)} (want 33/33)")
    checks["C2_manifest_two_way"] = {"pass": not c2_fails, "fails": c2_fails}

    # C3 lane coverage
    registry = json.loads(git("show", "HEAD:SME-ExamQuestion/manifest.json"))
    cie_lanes = sorted(c["slug"] for c in registry["courses"] if c["slug"].startswith("cie-"))
    covered: dict[str, str] = {}
    dupes = []
    for e in cie:
        for s in e["sme_courses"]:
            if s in covered:
                dupes.append(f"{s} in {covered[s]} and {e['slug']}")
            covered[s] = e["slug"]
    missing = [s for s in cie_lanes if s not in covered]
    extra = [s for s in covered if s not in cie_lanes]
    checks["C3_lane_coverage"] = {
        "pass": not (dupes or missing or extra) and len(cie_lanes) == 44,
        "fails": dupes + [f"missing {s}" for s in missing] + [f"extra {s}" for s in extra],
        "lanes": len(cie_lanes), "covered": len(covered),
    }

    # C4 Edexcel byte-stability vs snapshot
    snap = json.loads(SNAP.read_text())
    c4_fails = []
    for e in edx:
        h = hashlib.sha256(json.dumps(e, sort_keys=True).encode()).hexdigest()
        if snap.get(e["slug"]) != h:
            c4_fails.append(e["slug"])
    checks["C4_edexcel_byte_stable"] = {
        "pass": not c4_fails and len(edx) == len(snap) == 23,
        "fails": c4_fails, "edexcel_entries": len(edx),
    }

    # C6 totals
    t = manifest["totals"]
    c6_fails = []
    if t["qualifications"] != 56:
        c6_fails.append(f"qualifications={t['qualifications']} want 56")
    if t["sme_courses_covered"] != 93:
        c6_fails.append(f"covered={t['sme_courses_covered']} want 93")
    if t["sme_courses_total"] != 93 or t["missing_courses"] != []:
        c6_fails.append(f"total/missing: {t['sme_courses_total']}/{t['missing_courses']}")
    checks["C6_totals"] = {"pass": not c6_fails, "fails": c6_fails}

    # C7 footprint guard
    status = git("status", "--porcelain").splitlines()
    out_of_footprint = [l for l in status if not any(
        l[3:].startswith(p) for p in FOOTPRINT_PREFIXES)]
    checks["C7_footprint"] = {
        "pass": not out_of_footprint, "fails": out_of_footprint,
        "changed_paths": len(status),
    }

    all_pass = all(c["pass"] for c in checks.values())
    result = {
        "schema": "syllabai.specs-cie-check/1.0",
        "generated_utc": now,
        "tip": git("rev-parse", "HEAD").strip(),
        "all_pass": all_pass,
        "checks": checks,
        "summary": {
            "cie_qualifications": len(cie),
            "edexcel_qualifications": len(edx),
            "cie_lanes_covered": len(covered),
            "cie_lanes_total": len(cie_lanes),
        },
    }
    REPORT.mkdir(parents=True, exist_ok=True)
    (REPORT / "T_SPECS_CIE_1_CHECK.json").write_text(json.dumps(result, indent=1) + "\n")
    print(json.dumps({k: v["pass"] for k, v in checks.items()}, indent=1))
    print("ALL PASS" if all_pass else "FAILURES PRESENT")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
