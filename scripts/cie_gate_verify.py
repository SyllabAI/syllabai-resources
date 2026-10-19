#!/usr/bin/env python3
"""
T-SPECS-CIE-GATE-1 — independent verification rounds for the review/promotion
gate over the 44 SUGGESTED spec-links/cie-*.json sidecars.

  V2  every T1_verbatim link re-derived from SOURCE blobs: the item's spcpt
      anchors must carry a definition line that normalizes equal to the
      official point text (or >=8-token containment) against EITHER official
      pool (bare text / text+sub_items).  Fresh implementation — shares the
      normalization SPEC, not the join's code (equivalence self-test included).
  V3  every T2_near link passes a LOWER-BOUND audit: some anchor definition
      line with Jaccard >= 0.55 against either pool, OR the spec-point name
      equals the official subsection title.  (Exact-rule replication needs
      candidate reconstruction; the join's determinism is separately pinned
      by J10 fixed-stamp reruns. Documented as a lower bound.)
  V4  stratified SME<->official sample pairs (family x tier) -> printed for
      the gate record (evidence, non-blocking).

Writes graph/reports/T_SPECS_CIE_GATE_1_VERIFY.json. Exit 0 iff V2+V3 have
zero defects.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO = Path("/home/z/my-project/syllabai-resources")
SL = REPO / "spec-links"
GATE = "T-SPECS-CIE-GATE-1"
TRACE = "1a150fee04d54d6d"

# ---- independent normalization (same SPEC as the join, fresh code)
_TRANS = str.maketrans({c: " " for c in
                        "!\"#$%()*,./:;<=>?@[\\]^_`{|}~+-'"})


def norm_v(s: str) -> str:
    if not s:
        return ""
    s = s.replace("&", " and ").replace("\u2019", "'").replace("\u201c", '"')
    s = s.replace("\u201d", '"').replace("\xa0", " ").casefold()
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return " ".join(s.split())


def jac(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def git_show(path: str) -> bytes:
    r = subprocess.run(["git", "-C", str(REPO), "show", f"HEAD:{path}"],
                       capture_output=True)
    return r.stdout if r.returncode == 0 else b""


def ls_tree() -> dict:
    files = {}
    out = subprocess.run(["git", "-C", str(REPO), "ls-tree", "-r", "HEAD"],
                         capture_output=True, check=True).stdout.decode()
    for line in out.splitlines():
        meta, _, path = line.partition("\t")
        parts = meta.split()
        if len(parts) >= 3 and parts[1] == "blob":
            files[path] = parts[2]
    return files


def cat_blobs(sha_to_path: dict, chunk: int = 400) -> dict:
    texts = {}
    shas = list(sha_to_path.keys())
    for i in range(0, len(shas), chunk):
        batch = shas[i:i + chunk]
        r = subprocess.run(
            ["git", "-C", str(REPO), "cat-file", "--batch"],
            input="".join(s + "\n" for s in batch).encode(),
            capture_output=True, check=True)
        buf, pos = r.stdout, 0
        for s in batch:
            nl = buf.index(b"\n", pos)
            size = int(buf[pos:nl].split()[2])
            texts[sha_to_path[s]] = buf[nl + 1:nl + 1 + size].decode("utf-8", "replace")
            pos = nl + 1 + size + 1
    return texts


def main() -> int:
    t0 = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # equivalence self-test of the independent normalizer on corpus samples
    sys.path.insert(0, str(REPO / "scripts"))
    from cie_spec_join import norm as norm_join
    probes = [
        "State the distinguishing properties of solids, liquids & gases",
        "Describe the structures of solids, liquids and gases in terms of particle separation, arrangement and motion",
        "use the Hardy\u2013Weinberg principle to calculate allele and genotype frequencies",
        "Identify and use:", "  ", "", "Explain — in terms of kinetic particle theory…",
    ]
    eq_fail = [p for p in probes if norm_v(p) != norm_join(p)]
    print(f"norm equivalence self-test: {'PASS' if not eq_fail else 'FAIL ' + str(eq_fail)}"
          f" ({len(probes)} probes)")
    if eq_fail:
        return 1

    # inputs
    manifest = json.loads((REPO / "Official-Specifications" / "manifest.json")
                          .read_text(encoding="utf-8"))
    lane_to_qual, quals = {}, {}
    for q in manifest["qualifications"]:
        if str(q.get("slug", "")).startswith("cie-"):
            quals[q["slug"]] = q
            for lane in q.get("sme_courses") or []:
                lane_to_qual[lane] = q["slug"]

    registries = {}
    for slug, q in quals.items():
        pdf = Path(q["pdf"])
        p = REPO / "Official-Specifications" / "parsed" / slug / (pdf.stem + ".parsed.json")
        registries[slug] = json.loads(p.read_text(encoding="utf-8"))

    files = ls_tree()
    sidecars = {f.stem: json.loads(f.read_text(encoding="utf-8"))
                for f in sorted(SL.glob("cie-*.json"))}

    t1_total = t1_ok = t2_total = t2_ok = 0
    defects = []
    samples = []

    for lane, d in sidecars.items():
        reg = registries[d["qual"]]
        pts = {p["id"]: p for p in reg["spec_points"]}

        # official pools per point (both), subsection title sets, per-subsec census
        pools = {}
        for pid, p in pts.items():
            base = set(norm_v(p.get("text") or "").split())
            sub = " ".join(p.get("sub_items") or [])
            withsub = base | set(norm_v((p.get("text") or "") + " " + sub).split())
            pools[pid] = [base, withsub] if base != withsub else [base]

        # lane universe + per-item anchors from source blobs
        note_paths = [p for p in files
                      if p.startswith(f"SME-RevisionNotes/{lane}/notes/")
                      and p.endswith(".json")]
        eq_paths = [p for p in files
                    if p.startswith(f"SME-ExamQuestion/{lane}/")
                    and p.endswith("/topic.json")]
        blobs = cat_blobs({files[p]: p for p in note_paths + eq_paths})

        uni = {}
        anchors = defaultdict(list)  # content_id -> [spcpt ids]
        for p in note_paths:
            try:
                n = json.loads(blobs[p])
            except Exception:
                continue
            for b in n.get("blocks") or []:
                if b.get("type") == "spec_point" and b.get("id"):
                    u = uni.setdefault(b["id"], {"name": b.get("name"),
                                                 "definition": b.get("definition")})
                    if not u.get("definition") and b.get("definition"):
                        u["definition"] = b["definition"]
            for sid in n.get("spec_point_ids") or []:
                anchors[n["note_id"]].append(sid)
        for p in eq_paths:
            try:
                t = json.loads(blobs[p])
            except Exception:
                continue
            for q in t.get("questions") or []:
                for part in q.get("parts") or []:
                    for sid in part.get("spec_point_ids") or []:
                        anchors[part["id"]].append(sid)

        # lines per anchor (normalized token sets)
        anchor_lines = {}
        for sid, u in uni.items():
            lls = []
            for ln in (u.get("definition") or "").split("\n"):
                tk = set(norm_v(ln).split())
                if tk:
                    lls.append(tk)
            anchor_lines[sid] = (set(norm_v(u.get("name") or "").split()), lls)

        fam = d["registry"]["family"]
        for cid, item in d["items"].items():
            anch = [a for a in anchors.get(cid, []) if a in uni]
            for c in item.get("codes") or []:
                pid = c["official_id"]
                if pid not in pts:
                    defects.append(f"{lane}:{cid}:{pid}:not-in-registry")
                    continue
                name_tk, lls_all = [], []
                for a in anch:
                    nt, lls = anchor_lines[a]
                    name_tk = name_tk or nt
                    lls_all.extend(lls)
                if c["tier"] == "T1_verbatim":
                    t1_total += 1
                    hit = False
                    for lt in lls_all:
                        for pool in pools[pid]:
                            if lt == pool or (len(lt & pool) >= 8 and
                                              (lt <= pool or pool <= lt)):
                                hit = True
                                break
                        if hit:
                            break
                    if hit:
                        t1_ok += 1
                    else:
                        defects.append(f"{lane}:{cid}:{pid}:T1-unverified")
                elif c["tier"] == "T2_near":
                    t2_total += 1
                    # per-anchor lower-bound audit: jaccard rule (any line,
                    # either pool), name-weak rule (name == point text tokens
                    # AND some line >= 0.35), or head rule (name == subsection
                    # title). All rules evaluated on ONE anchor at a time —
                    # the join evaluated them per spcpt record.
                    weak = False
                    ssec = pts[pid].get("subsection") or {}
                    title_tk = set(norm_v(ssec.get("title") or "").split())
                    for a in anch:
                        nt, lls = anchor_lines[a]
                        for lt in lls:
                            for pool in pools[pid]:
                                if jac(lt, pool) >= 0.55:
                                    weak = True
                                    break
                            if weak:
                                break
                        if not weak and nt:
                            ptoks = pools[pid][0]
                            if nt == ptoks and any(jac(lt, ptoks) >= 0.35
                                                   for lt in lls):
                                weak = True
                        if not weak and nt and nt == title_tk:
                            weak = True
                        if weak:
                            break
                    if weak:
                        t2_ok += 1
                    else:
                        defects.append(f"{lane}:{cid}:{pid}:T2-unverified")

        # V4 sample: up to 2 links per tier for this lane
        for want_tier in ("T1_verbatim", "T2_near"):
            got = 0
            for cid, item in d["items"].items():
                if got >= 2:
                    break
                for c in item.get("codes") or []:
                    if c["tier"] != want_tier or c["official_id"] not in pts:
                        continue
                    a0 = next((a for a in anchors.get(cid, []) if a in uni), None)
                    if not a0:
                        continue
                    u = uni[a0]
                    samples.append({
                        "lane": lane, "family": fam, "tier": want_tier,
                        "code": str(pts[c["official_id"]].get("official_code")),
                        "sme_name": u.get("name"),
                        "sme_definition": (u.get("definition") or "")[:220],
                        "official_text": (pts[c["official_id"]].get("text") or "")[:220],
                    })
                    got += 1
                    break

    verdict = "PASS" if not defects else "FAIL"
    out = {
        "schema": "syllabai.gate-verification/1.0",
        "gate": GATE,
        "operator_trace": TRACE,
        "generated_utc": t0,
        "norm_selftest": "PASS",
        "v2_t1": {"total": t1_total, "verified": t1_ok,
                  "failed": t1_total - t1_ok},
        "v3_t2": {"total": t2_total, "verified": t2_ok,
                  "failed": t2_total - t2_ok},
        "defects": defects[:50],
        "v4_samples": samples,
        "verdict": verdict,
    }
    outp = REPO / "graph" / "reports" / "T_SPECS_CIE_GATE_1_VERIFY.json"
    outp.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n",
                    encoding="utf-8")
    print(f"V2 T1: {t1_ok}/{t1_total} verified")
    print(f"V3 T2: {t2_ok}/{t2_total} verified (lower-bound audit)")
    print(f"V4 samples: {len(samples)}")
    print(f"defects: {len(defects)} {defects[:5]}")
    print(f"verdict: {verdict} -> {outp.relative_to(REPO)}")
    return 0 if not defects else 1


if __name__ == "__main__":
    raise SystemExit(main())
