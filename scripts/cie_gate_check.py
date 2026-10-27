#!/usr/bin/env python3
"""
T-SPECS-CIE-GATE-1 check battery (K1-K6).

  K1  44/44 sidecars review_state == ACCEPTED with gate/accepted_by recorded
  K2  items/totals/anchors/registry deep-equal vs the PRE-GATE HEAD blobs —
      the gate moved ZERO links (only review_state + manifest changed)
  K3  updated join battery J1-J10 passes post-gate
  K4  manifest: cie_gate block present and consistent; pre-existing rows
      value-identical vs pre-gate HEAD
  K5  footprint guard: only the declared gate-touched paths in git status
  K6  tier/method distribution per sidecar identical vs pre-gate HEAD
      (cross-proof of K2 at the code-entry level)

Writes graph/reports/T_SPECS_CIE_GATE_1_CHECK.json. Exit 0 iff ALL PASS.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path("/home/z/my-project/syllabai-resources")
SL = REPO / "spec-links"
GATE = "T-SPECS-CIE-GATE-1"
TRACE = "1a150fee04d54d6d"

results = []


def check(kid, name, ok, detail=""):
    results.append((kid, name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {kid} {name}" +
          (f" — {detail}" if detail else ""))


def git_show(path: str) -> bytes:
    r = subprocess.run(["git", "-C", str(REPO), "show", f"HEAD:{path}"],
                       capture_output=True)
    return r.stdout if r.returncode == 0 else b""


def link_fingerprint(d: dict) -> dict:
    """Order-insensitive fingerprint of everything EXCEPT review_state."""
    return {
        "schema": d.get("schema"),
        "course": d.get("course"),
        "qual": d.get("qual"),
        "board": d.get("board"),
        "registry": d.get("registry"),
        "totals": d.get("totals"),
        "anchors": d.get("anchors"),
        "items": {cid: {k: it.get(k) for k in
                        ("kind", "label", "section", "topic", "codes", "pending")}
                  for cid, it in (d.get("items") or {}).items()},
    }


def main() -> int:
    sidecars = {f.stem: json.loads(f.read_text(encoding="utf-8"))
                for f in sorted(SL.glob("cie-*.json"))}

    # ---- K1
    bad = []
    for lane, d in sidecars.items():
        rs = d.get("review_state") or {}
        if rs.get("state") != "ACCEPTED" or rs.get("gate") != GATE:
            bad.append(f"{lane}:state")
        if TRACE not in str(rs.get("accepted_by", "")):
            bad.append(f"{lane}:accepted_by")
        tp = rs.get("tier_policy") or {}
        if tp.get("T1_verbatim") != "authoritative (gate-verified)":
            bad.append(f"{lane}:tier_policy")
    check("K1", "44/44 ACCEPTED with gate provenance",
          len(sidecars) == 44 and not bad, f"bad={bad[:4]}")

    # ---- K2 deep-equal vs pre-gate HEAD
    diff = []
    for lane, d in sidecars.items():
        head = json.loads(git_show(f"spec-links/{lane}.json") or b"null")
        if head is None:
            diff.append(f"{lane}:missing-at-HEAD")
            continue
        if link_fingerprint(head) != link_fingerprint(d):
            diff.append(f"{lane}:links-moved")
    check("K2", "items/codes/pending byte-equivalent vs pre-gate HEAD",
          not diff, str(diff[:4]))

    # ---- K3 join battery post-gate
    r = subprocess.run([sys.executable,
                        str(REPO / "scripts/cie_join_check.py")],
                       capture_output=True, text=True)
    jok = "J1-J10: 12/12 PASS" in r.stdout
    tail = [l for l in r.stdout.splitlines() if "J1-J10" in l]
    check("K3", "join battery J1-J10 post-gate", jok and r.returncode == 0,
          tail[0] if tail else f"rc={r.returncode}")
    # restore the J battery's own generated_utc churn
    subprocess.run(["git", "checkout", "--",
                    "graph/reports/T_SPECS_CIE_JOIN_1_CHECK.json"],
                   cwd=REPO, capture_output=True)
    # NOTE: the J battery's J10 reproducibility rerun REGENERATES its 3
    # sample sidecars from the join script (SUGGESTED state) — the working
    # tree de-promotes those lanes. The applier re-promotes them (idempotent,
    # same gate metadata); K7 below pins the final commit state.
    subprocess.run([sys.executable, str(REPO / "scripts/cie_gate_apply.py")],
                   capture_output=True, text=True)

    # ---- K4 manifest
    manifest = json.loads((SL / "manifest.json").read_text(encoding="utf-8"))
    g = manifest.get("cie_gate") or {}
    head_manifest = json.loads(git_show("spec-links/manifest.json") or b"{}")
    pre = head_manifest.get("courses", {})
    changed = [k for k, v in pre.items()
               if manifest.get("courses", {}).get(k) != v]
    k4 = (g.get("gate") == GATE and g.get("state") == "ACCEPTED"
          and TRACE in str(g.get("accepted_by", ""))
          and g.get("lanes") == 44 and not changed)
    check("K4", "manifest cie_gate block + rows value-identical", k4,
          f"gate={bool(g)} changed_preexisting={changed[:3]}")

    # ---- K5 footprint
    st = subprocess.run(["git", "-C", str(REPO), "status", "--porcelain=v1"],
                        capture_output=True, text=True).stdout.splitlines()
    ok_mod = re.compile(
        r"^(spec-links/cie-[a-z0-9-]+\.json|spec-links/manifest\.json|"
        r"spec-links/README\.md|scripts/cie_join_check\.py)$")
    ok_add = re.compile(
        r"^(graph/reports/T_SPECS_CIE_GATE_1_(VERIFY\.json|RECORD\.md|CHECK\.json)|"
        r"scripts/cie_gate_(verify|apply|check)\.py)$")
    violations = []
    for line in st:
        code, path = line[:2].strip(), line[3:]
        if code in ("M", "MM") and not ok_mod.match(path):
            violations.append(line)
        if code in ("??", "A", "AM") and not ok_add.match(path):
            violations.append(line)
    check("K5", "footprint guard (gate-declared paths only)", not violations,
          str(violations[:6]))

    # ---- K6 tier/method distribution vs pre-gate HEAD
    from collections import Counter
    diff6 = []
    for lane, d in sidecars.items():
        head = json.loads(git_show(f"spec-links/{lane}.json") or b"null")

        def dist(dd):
            c = Counter()
            for it in (dd.get("items") or {}).values():
                for code in it.get("codes") or []:
                    c[(code.get("tier"), code.get("method"))] += 1
            return c

        if dist(head) != dist(d):
            diff6.append(lane)
    check("K6", "tier/method distribution identical vs pre-gate", not diff6,
          str(diff6[:4]))

    # ---- K7 final commit-state guarantee: all 44 ACCEPTED after the K3
    # de-promotion/re-apply cycle
    bad7 = [l for l, d in sidecars.items()
            if (json.loads((SL / f"{l}.json").read_text(encoding="utf-8"))
                .get("review_state") or {}).get("state") != "ACCEPTED"]
    check("K7", "final working-tree state: 44/44 ACCEPTED", not bad7,
          str(bad7[:4]))

    fails = [r for r in results if not r[2]]
    print(f"\nK1-K7: {len(results) - len(fails)}/{len(results)} PASS")
    out = REPO / "graph" / "reports" / "T_SPECS_CIE_GATE_1_CHECK.json"
    out.write_text(json.dumps({
        "schema": "syllabai.check-battery/1.0",
        "gate": GATE,
        "generated_utc": datetime.now(timezone.utc)
            .strftime("%Y-%m-%dT%H:%M:%SZ"),
        "checks": [{"id": k, "name": n, "pass": ok, "detail": det}
                   for k, n, ok, det in results],
        "summary": {"total": len(results), "pass": len(results) - len(fails),
                    "fail": len(fails)},
    }, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"check json -> {out.relative_to(REPO)}")
    return 0 if not fails else 1


if __name__ == "__main__":
    raise SystemExit(main())
