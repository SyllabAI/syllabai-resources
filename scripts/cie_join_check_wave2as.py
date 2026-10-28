#!/usr/bin/env python3
"""
T-SPECS-CIE-JOIN-2 check battery (J1-J11).

Validates the wave-2 AS sidecar lane contract. Reads the emitted
spec-links/cie-as-*.json sidecars (the 8 lane set), the spec-links manifest,
the parsed CIE registries and the git HEAD baseline. Exit 0 iff ALL PASS.
Print-only except the check json -> graph/reports/T_SPECS_CIE_JOIN_2_CHECK.json.

  J1   8 well-formed SUGGESTED sidecars (schema/course/board/review_state)
  J2   sidecar qual == Official-Specifications manifest mapping (8/8)
  J3   zero dangling official ids/codes vs the FULL registry
  J4   official_id prefix == registry prefix
  J5   tier/method vocabulary (T1_verbatim/T2_near x cie_*_text_join)
  J6   universe conservation vs note blobs + pending integrity
  J7   cross-foot: sidecar totals == items; manifest rows == totals
  J7b  pre-existing manifest rows value-identical vs HEAD
  J8   every other spec-links file byte-identical vs HEAD
  J9   footprint guard: declared paths only
  J10  fixed-stamp rerun payload-identical modulo review_state (2 samples)
  J11  AS scope law: coded points obey the parse-marker scope rule per lane;
       anchors.scope_law additive block present and consistent
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path("/home/z/my-project/syllabai-resources")
SL = REPO / "spec-links"
LANE_2 = "T-SPECS-CIE-JOIN-2"
METHODS = ("cie_definition_text_join", "cie_text_join")
TIERS = ("T1_verbatim", "T2_near")

LANES_2 = [
    "cie-as-chemistry-25",
    "cie-as-physics-25",
    "cie-as-business-23",
    "cie-as-computer-science-19",
    "cie-as-maths-20-pure-1",
    "cie-as-maths-20-pure-2",
    "cie-as-maths-20-mechanics",
    "cie-as-maths-20-probability-and-statistics-1",
]
SCOPE_AS_ONLY = {"cie-as-chemistry-25", "cie-as-physics-25", "cie-as-business-23"}
SCOPE_DROP_ALEVEL = {"cie-as-computer-science-19"}

results = []


def check(jid, name, ok, detail=""):
    results.append((jid, name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {jid} {name}" + (f" — {detail}" if detail else ""))


def git_show(path: str) -> bytes:
    r = subprocess.run(["git", "-C", str(REPO), "show", f"HEAD:{path}"],
                       capture_output=True)
    return r.stdout if r.returncode == 0 else b""


def payload(text: str) -> str:
    d = json.loads(text)
    d.pop("review_state", None)
    return json.dumps(d, sort_keys=True, ensure_ascii=False)


def main() -> int:
    # ---- inputs
    manifest = json.loads((REPO / "Official-Specifications" / "manifest.json").read_text())
    lane_to_qual, quals = {}, {}
    for q in manifest["qualifications"]:
        for lane in q.get("sme_courses") or []:
            lane_to_qual[lane] = q["slug"]
            quals[q["slug"]] = q

    need_quals = {lane_to_qual[l] for l in LANES_2}
    registries = {}
    for slug, q in quals.items():
        if slug not in need_quals:
            continue  # this battery validates only the 8 banks' quals; some
            # manifest-registered quals (e.g. a-level-geography-2025-2026)
            # predate their parse landing — outside this battery's scope
        pdf = Path(q["pdf"])
        p = REPO / "Official-Specifications" / "parsed" / slug / (pdf.stem + ".parsed.json")
        registries[slug] = json.loads(p.read_text())

    sidecars = {}
    for lane in LANES_2:
        f = SL / f"{lane}.json"
        if not f.exists():
            check("J1", "8 well-formed sidecars", False, f"missing {lane}")
            print("\nJ1-J11: ABORT (missing sidecar)")
            return 1
        sidecars[lane] = json.loads(f.read_text())

    sl_manifest = json.loads((SL / "manifest.json").read_text())
    sl_manifest_head = json.loads(git_show("spec-links/manifest.json") or b"{}")

    # ---- J1
    bad = []
    for lane, d in sidecars.items():
        if d.get("schema") != "syllabai.learner-spec-links/1.0":
            bad.append(f"{lane}:schema")
        if d.get("course") != lane:
            bad.append(f"{lane}:course")
        rs = d.get("review_state") or {}
        if rs.get("state") != "SUGGESTED" or rs.get("lane") != LANE_2 \
                or rs.get("gate") != "pending":
            bad.append(f"{lane}:review_state")
        if d.get("board") != "cambridge-cie":
            bad.append(f"{lane}:board")
    check("J1", "8 well-formed SUGGESTED sidecars (lane T-SPECS-CIE-JOIN-2)",
          not bad, str(bad[:4]))

    # ---- J2
    wrong_qual = [l for l, d in sidecars.items() if d.get("qual") != lane_to_qual.get(l)]
    check("J2", "sidecar qual == manifest mapping (8/8)", not wrong_qual,
          str(wrong_qual[:4]))

    # ---- J3/J4/J5 (vs FULL registry — served subset must exist there)
    dangling, bad_prefix, bad_vocab = [], [], []
    reg_of = {}
    for lane, d in sidecars.items():
        reg = registries[d["qual"]]
        reg_of[lane] = reg
        pts = reg["spec_points"]
        ids = {p["id"]: str(p.get("official_code")) for p in pts}
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
    check("J3", "zero dangling official ids/codes (full registry)", not dangling,
          f"n={len(dangling)} {dangling[:4]}")
    check("J4", "official_id prefix == registry", not bad_prefix, str(bad_prefix[:4]))
    check("J5", "tier/method vocabulary", not bad_vocab, str(bad_vocab[:4]))

    # ---- J6 universe conservation + pending integrity
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
        stray = sorted({s for s in pend
                        if not (isinstance(s, str) and s.startswith("spcpt_"))})
        if stray:
            bad_pending.append(f"{lane}:{stray[:2]}")
    check("J6", "universe conservation + pending integrity",
          not bad_uni and not bad_pending, f"uni={bad_uni[:3]} pend={bad_pending[:3]}")

    # ---- J7 cross-foot
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

    # ---- J7b
    head_courses = sl_manifest_head.get("courses", {})
    cur_courses = sl_manifest.get("courses", {})
    changed = [k for k, v in head_courses.items() if cur_courses.get(k) != v]
    check("J7b", "pre-existing manifest rows value-identical vs HEAD", not changed,
          f"changed={changed[:4]}")
    head_blocks = {k: v for k, v in sl_manifest_head.items()
                   if k not in ("courses", "generated_utc")}
    drifted = [k for k, v in head_blocks.items() if sl_manifest.get(k) != v]
    new_block = sl_manifest.get("cie_join_wave2as", {})
    block_ok = not drifted and new_block.get("lane") == LANE_2 \
        and new_block.get("lanes") == 8 and new_block.get("review_state") == "SUGGESTED"
    check("J7c", "manifest blocks: pre-existing untouched + additive lane block",
          block_ok, f"drifted={drifted[:3]} block={new_block}")

    # ---- J8 every other spec-links file byte-identical vs HEAD
    diff = []
    lane_files = {f"{l}.json" for l in LANES_2}
    for f in sorted(SL.glob("*.json")):
        if f.name == "manifest.json" or f.name in lane_files:
            continue
        if hashlib.sha256(f.read_bytes()).digest() != \
                hashlib.sha256(git_show(f"spec-links/{f.name}")).digest():
            diff.append(f.name)
    for f in sorted(SL.glob("*.md")):
        if f.name == "README.md":
            continue
        if hashlib.sha256(f.read_bytes()).digest() != \
                hashlib.sha256(git_show(f"spec-links/{f.name}")).digest():
            diff.append(f.name)
    check("J8", "all other spec-links files byte-identical vs HEAD", not diff,
          str(diff[:4]))

    # ---- J9 footprint guard
    st = subprocess.run(["git", "-C", str(REPO), "status", "--porcelain=v1"],
                        capture_output=True, text=True).stdout.splitlines()
    allowed = re.compile(
        r"^(?:A |A |\?\? )?"
        r"(spec-links/cie-as-(?:chemistry-25|physics-25|business-23|"
        r"computer-science-19|maths-20-pure-1|maths-20-pure-2|maths-20-mechanics|"
        r"maths-20-probability-and-statistics-1)\.json|"
        r"spec-links/manifest\.json|spec-links/README\.md|"
        r"scripts/cie_spec_join_wave2as\.py|scripts/cie_join_check_wave2as\.py|"
        r"graph/reports/T_SPECS_CIE_JOIN_2_(RECORD\.md|CHECK\.json))$")
    violations = []
    for line in st:
        code, _, path = line[:2], line[2:3], line[3:]
        if code.strip() in ("A", "AM", "??", "M", "MM"):
            if not allowed.match(path):
                violations.append(line)
    check("J9", "footprint guard (declared paths only)", not violations,
          str(violations[:6]))

    # ---- J10 reproducibility (2 samples; fixed stamp from the apply run)
    stamp = ""
    sf = Path("/home/z/my-project/work/join2_stamp.txt")
    if sf.exists():
        m = re.match(r"STAMP=(\S+)", sf.read_text())
        stamp = m.group(1) if m else ""
    if not stamp:
        stamp = "2026-10-28T05:15:32Z"
    same, det = True, ""
    for lane in ("cie-as-chemistry-25", "cie-as-maths-20-pure-1"):
        before = payload((SL / f"{lane}.json").read_text())
        r = subprocess.run(
            [sys.executable, str(REPO / "scripts/cie_spec_join_wave2as.py"),
             "--stamp", stamp, "--lanes", lane],
            capture_output=True, text=True)
        after = payload((SL / f"{lane}.json").read_text())
        if before != after or r.returncode != 0:
            same = False
            det = f"{lane} rerun differs or rc={r.returncode}: {r.stdout[-200:]}"
            break
    check("J10", "fixed-stamp rerun payload-identical modulo review_state (2 lanes)",
          same, det)

    # ---- J11 AS scope law
    bad_scope, bad_block = [], []
    for lane, d in sidecars.items():
        reg = reg_of[lane]
        scope_by_id = {p["id"]: p.get("scope") for p in reg["spec_points"]}
        n_pts = len(scope_by_id)
        if lane in SCOPE_AS_ONLY:
            law_ok = lambda s: s == "AS Level"
        elif lane in SCOPE_DROP_ALEVEL:
            law_ok = lambda s: s != "A Level"
        else:
            law_ok = lambda s: True
        for item in d["items"].values():
            for c in item.get("codes") or []:
                if not law_ok(scope_by_id.get(c["official_id"])):
                    bad_scope.append(f"{lane}:{c['official_id']}:{scope_by_id.get(c['official_id'])}")
        blk = (d.get("anchors") or {}).get("scope_law") or {}
        kept = sum(1 for s in scope_by_id.values()
                   if (s == "AS Level" if lane in SCOPE_AS_ONLY
                       else (s != "A Level" if lane in SCOPE_DROP_ALEVEL else True)))
        if blk.get("registry_points") != n_pts or blk.get("lane_points") != kept:
            bad_block.append(f"{lane}:block")
    check("J11", "AS scope law on every served code + additive scope_law block",
          not bad_scope and not bad_block,
          f"scope={bad_scope[:4]} block={bad_block[:4]}")

    # ---- summary
    fails = [r for r in results if not r[2]]
    print(f"\nJ1-J11: {len(results) - len(fails)}/{len(results)} PASS")
    out = REPO / "graph" / "reports" / "T_SPECS_CIE_JOIN_2_CHECK.json"
    out.write_text(json.dumps({
        "schema": "syllabai.check-battery/1.0",
        "lane": LANE_2,
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "apply_stamp": stamp,
        "checks": [{"id": jid, "name": name, "pass": ok, "detail": det}
                   for jid, name, ok, det in results],
        "summary": {"total": len(results), "pass": len(results) - len(fails),
                    "fail": len(fails)},
    }, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"check json -> {out.relative_to(REPO)}")
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
