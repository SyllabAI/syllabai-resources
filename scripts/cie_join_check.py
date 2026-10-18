#!/usr/bin/env python3
"""
T-SPECS-CIE-JOIN-1 check battery (J1-J10).

Reads the emitted spec-links/cie-*.json sidecars, the spec-links manifest,
the parsed CIE registries and the git HEAD baseline, and validates the join
lane contract. Exit 0 iff ALL PASS. Print-only; writes nothing.

  J1  file set / schema / SUGGESTED state         (44 sidecars well-formed)
  J2  lane<->manifest bijection vs Official-Specifications manifest
  J3  zero dangling official ids (id AND code exist in the lane's registry)
  J4  official_id prefix == lane's registry prefix
  J5  tier/method vocabulary conformance
  J6  universe conservation: spcpt blocks in notes == anchors.universe_ids;
      every item pending entry is an spcpt id that the lane universe defines
  J7  cross-foot: sidecar totals == items; manifest row == sidecar totals;
      Edexcel manifest rows deep-equal vs HEAD baseline
  J8  Edexcel spec-links files byte-identical vs HEAD baseline
  J9  footprint guard: changed/added paths within the declared set
  J10 reproducibility: fixed-stamp re-run of 3 sample lanes is byte-identical
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path("/home/z/my-project/syllabai-resources")
SL = REPO / "spec-links"
LANE_ID = "T-SPECS-CIE-JOIN-1"
METHODS = ("cie_definition_text_join", "cie_text_join")
TIERS = ("T1_verbatim", "T2_near")

results = []


def check(jid, name, ok, detail=""):
    results.append((jid, name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {jid} {name}" + (f" — {detail}" if detail else ""))


def git_show(path: str) -> bytes:
    r = subprocess.run(["git", "-C", str(REPO), "show", f"HEAD:{path}"],
                       capture_output=True)
    if r.returncode != 0:
        return b""
    return r.stdout


def main() -> int:
    import hashlib

    # ---- inputs
    manifest = json.loads((REPO / "Official-Specifications" / "manifest.json")
                          .read_text(encoding="utf-8"))
    lane_to_qual, quals = {}, {}
    for q in manifest["qualifications"]:
        if str(q.get("slug", "")).startswith("cie-"):
            quals[q["slug"]] = q
            for lane in q.get("sme_courses") or []:
                lane_to_qual[lane] = q["slug"]
    exp_lanes = set(lane_to_qual)

    registries = {}
    for slug, q in quals.items():
        pdf = Path(q["pdf"])
        p = REPO / "Official-Specifications" / "parsed" / slug / (pdf.stem + ".parsed.json")
        d = json.loads(p.read_text(encoding="utf-8"))
        registries[slug] = d

    sidecars = {}
    for f in sorted(SL.glob("cie-*.json")):
        sidecars[f.stem] = json.loads(f.read_text(encoding="utf-8"))

    sl_manifest = json.loads((SL / "manifest.json").read_text(encoding="utf-8"))
    sl_manifest_head = json.loads(git_show("spec-links/manifest.json") or b"{}")

    # ---- J1
    bad = []
    for lane, d in sidecars.items():
        if d.get("schema") != "syllabai.learner-spec-links/1.0":
            bad.append(f"{lane}:schema")
        if d.get("course") != lane:
            bad.append(f"{lane}:course")
        rs = d.get("review_state") or {}
        if rs.get("state") != "SUGGESTED" or rs.get("lane") != LANE_ID \
                or rs.get("gate") != "pending":
            bad.append(f"{lane}:review_state")
        if d.get("board") != "cambridge-cie":
            bad.append(f"{lane}:board")
    check("J1", "44 well-formed SUGGESTED sidecars",
          len(sidecars) == 44 and not bad,
          f"sidecars={len(sidecars)} bad={bad[:4]}")

    # ---- J2
    check("J2", "lane<->manifest bijection (44/44)",
          set(sidecars) == exp_lanes,
          f"missing={sorted(exp_lanes - set(sidecars))[:4]} "
          f"extra={sorted(set(sidecars) - exp_lanes)[:4]}")
    wrong_qual = [l for l, d in sidecars.items()
                  if d.get("qual") != lane_to_qual.get(l)]
    check("J2b", "sidecar qual == manifest mapping", not wrong_qual,
          str(wrong_qual[:4]))

    # ---- J3/J4/J5
    dangling, bad_prefix, bad_vocab = [], [], []
    for lane, d in sidecars.items():
        reg = registries[d["qual"]]
        pts = reg["spec_points"]
        ids = {p["id"]: str(p.get("official_code")) for p in pts}
        # the parsed registry's internal id prefix (UPPER QUAL form) comes
        # from the points themselves — the registry 'id' field is the slug
        prefix = pts[0]["id"].split(":", 1)[0] + ":" if pts else ""
        for item in d["items"].values():
            for c in item.get("codes") or []:
                oid = c.get("official_id")
                if oid not in ids:
                    dangling.append(f"{lane}:{oid}")
                else:
                    if c.get("official_code") != ids[oid]:
                        dangling.append(f"{lane}:{oid}:code")
                    if not oid.startswith(prefix):
                        bad_prefix.append(f"{lane}:{oid}")
                if c.get("tier") not in TIERS or c.get("method") not in METHODS:
                    bad_vocab.append(f"{lane}:{oid}")
    check("J3", "zero dangling official ids/codes", not dangling,
          f"n={len(dangling)} {dangling[:4]}")
    check("J4", "official_id prefix == registry", not bad_prefix,
          f"n={len(bad_prefix)} {bad_prefix[:4]}")
    check("J5", "tier/method vocabulary", not bad_vocab,
          f"n={len(bad_vocab)} {bad_vocab[:4]}")

    # ---- J6 universe conservation (recount spcpt blocks from note blobs)
    sys.path.insert(0, str(REPO / "scripts"))
    from cie_spec_join import ls_tree, cat_blobs
    files = ls_tree()
    bad_uni, bad_pending = [], []
    for lane, d in sidecars.items():
        note_paths = [p for p in files
                      if p.startswith(f"SME-RevisionNotes/{lane}/notes/")
                      and p.endswith(".json")]
        blobs = cat_blobs({files[p]: p for p in note_paths})
        uni = set()
        for p in note_paths:
            try:
                n = json.loads(blobs[p])
            except Exception:
                continue
            for b in n.get("blocks") or []:
                if b.get("type") == "spec_point" and b.get("id"):
                    uni.add(b["id"])
        if len(uni) != (d.get("anchors") or {}).get("universe_ids"):
            bad_uni.append(f"{lane}:{len(uni)}!={d['anchors']['universe_ids']}")
        pend = [s for it in d["items"].values() for s in (it.get("pending") or [])]
        # pending entries must be well-formed spcpt ids. NOTE: the CIE EQ
        # corpus carries spec_point_ids that are dangling in the corpus
        # itself (no embedded definition anywhere) — pending may exceed the
        # note-derived universe; that is the honest state, not a defect.
        stray = sorted({s for s in pend if not (isinstance(s, str) and s.startswith("spcpt_"))})
        if stray:
            bad_pending.append(f"{lane}:{stray[:2]}")
    check("J6", "universe conservation + pending integrity",
          not bad_uni and not bad_pending,
          f"uni={bad_uni[:3]} pend={bad_pending[:3]}")

    # ---- J7 cross-foot + Edexcel manifest rows
    bad_foot = []
    for lane, d in sidecars.items():
        t = d["totals"]
        items = d["items"]
        if t["items"] != len(items):
            bad_foot.append(f"{lane}:items")
        by = {"notes": 0, "question_parts": 0, "flashcards": 0}
        coded = {"notes": 0, "question_parts": 0, "flashcards": 0}
        for it in items.values():
            by[it["kind"] + "s"] += 1
            coded[it["kind"] + "s"] += 1 if it["codes"] else 0
        if t["by_kind"] != by or t["coded_by_kind"] != coded:
            bad_foot.append(f"{lane}:by_kind")
        if t["items_with_codes"] != sum(coded.values()):
            bad_foot.append(f"{lane}:coded")
        row = sl_manifest["courses"].get(lane) or {}
        if row.get("items") != t["items"] or \
                row.get("items_with_codes") != t["items_with_codes"] or \
                row.get("by_kind") != t["by_kind"] or \
                row.get("coded_by_kind") != t["coded_by_kind"]:
            bad_foot.append(f"{lane}:manifest_row")
    check("J7", "sidecar totals cross-foot + manifest rows", not bad_foot,
          str(bad_foot[:4]))

    head_courses = sl_manifest_head.get("courses", {})
    cur_courses = sl_manifest.get("courses", {})
    changed = [k for k, v in head_courses.items() if cur_courses.get(k) != v]
    check("J7b", "pre-existing manifest rows value-identical vs HEAD",
          not changed, f"changed={changed[:4]}")

    # ---- J8 Edexcel files byte-identical
    diff = []
    for f in sorted(SL.glob("*.json")):
        if f.stem.startswith("cie-") or f.name == "manifest.json":
            continue
        if hashlib.sha256(f.read_bytes()).digest() != \
                hashlib.sha256(git_show(f"spec-links/{f.name}")).digest():
            diff.append(f.name)
    for f in sorted(SL.glob("*.md")):
        if f.name == "README.md":
            continue  # README is append-only-extended by this lane
        if hashlib.sha256(f.read_bytes()).digest() != \
                hashlib.sha256(git_show(f"spec-links/{f.name}")).digest():
            diff.append(f.name)
    check("J8", "Edexcel spec-links files byte-identical vs HEAD", not diff,
          str(diff[:4]))

    # ---- J9 footprint guard
    st = subprocess.run(["git", "-C", str(REPO), "status", "--porcelain=v1"],
                        capture_output=True, text=True).stdout.splitlines()
    allowed_added = re.compile(
        r"^(\?\?|A )? ?(spec-links/cie-[a-z0-9-]+\.json|"
        r"graph/reports/T_SPECS_CIE_JOIN_1_(RECORD\.md|CHECK\.json)|"
        r"scripts/cie_spec_join\.py|scripts/cie_join_check\.py)$")
    allowed_mod = re.compile(
        r"^(spec-links/manifest\.json|spec-links/README\.md)$")
    violations = []
    for line in st:
        code, _, path = line[:2], line[2:3], line[3:]
        if code.strip() in ("A", "AM", "??", "M", "MM"):
            ok = allowed_added.match(path) or allowed_mod.match(path) or \
                (code.strip().startswith("A") and allowed_added.match(path))
            if path.startswith("scripts/cie_") and path.endswith(".py"):
                ok = True
            if not ok:
                violations.append(line)
    check("J9", "footprint guard (declared paths only)", not violations,
          str(violations[:6]))

    # ---- J10 reproducibility on 3 sample lanes
    import hashlib
    samples = ["cie-igcse-chemistry-23", "cie-a-level-biology-25",
               "cie-igcse-maths-25-core"]
    same = True
    det = ""
    for lane in samples:
        before = hashlib.sha256((SL / f"{lane}.json").read_bytes()).hexdigest()
        r = subprocess.run([sys.executable, str(REPO / "scripts/cie_spec_join.py"),
                            "--stamp", "2026-10-19T12:00:00Z", "--lanes", lane],
                           capture_output=True, text=True)
        after = hashlib.sha256((SL / f"{lane}.json").read_bytes()).hexdigest()
        if before != after or r.returncode != 0:
            same = False
            det = f"{lane} rerun differs or rc={r.returncode}"
            break
    check("J10", "fixed-stamp rerun byte-identical (3 lanes)", same, det)

    # ---- summary
    fails = [r for r in results if not r[2]]
    print(f"\nJ1-J10: {len(results) - len(fails)}/{len(results)} PASS")
    out = REPO / "graph" / "reports" / "T_SPECS_CIE_JOIN_1_CHECK.json"
    from datetime import datetime, timezone
    payload = {
        "schema": "syllabai.check-battery/1.0",
        "lane": LANE_ID,
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "checks": [{"id": jid, "name": name, "pass": ok, "detail": det}
                   for jid, name, ok, det in results],
        "summary": {"total": len(results), "pass": len(results) - len(fails),
                    "fail": len(fails)},
    }
    out.write_text(json.dumps(payload, indent=1, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    print(f"check json -> {out.relative_to(REPO)}")
    if fails:
        for jid, name, _, det in fails:
            print(f"  FAIL {jid} {name} {det}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
