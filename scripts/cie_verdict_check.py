#!/usr/bin/env python3
"""
T-SPECS-CIE-VERDICT-1 check battery (V1-V10).

Reads the 25 filled spec-links/cie-*.json sidecars, the verdict sheet, the
manifest, the parsed CIE registries, the SME note blobs and the git HEAD
baseline (fea58c8a, pre-lane), and validates the verdict-fill lane contract.
Exit 0 iff ALL PASS. Print-only by default; --json PATH also writes the
machine check record (generated_utc pinned to the lane stamp).

  V1  25 verdict lanes well-formed (review_state ACCEPTED + gate intact +
      additive verdict block; anchors.verdict present)
  V2  verdict bijection: sheet (lane,id) == per-lane by_tier sums ==
      independently recomputed resolved set (pre-pending minus post-pending)
  V3  zero dangling verdict targets (official_id AND official_code exist in
      the lane's parsed registry)
  V4  vocabulary: verdict entries tier in V1..V5 + method operator_verdict;
      pre-existing entries keep the join vocabulary unchanged
  V5  INDEPENDENT re-derivation: every resolve re-derived from source blobs
      with a fresh implementation (shares the normalization SPEC, not the
      engine's code); the applied code must be the unique rule-conforming
      target for that id, at the recorded tier
  V6  cascade integrity: verdict codes only on items that anchored the id
      pre-lane; resolved ids leave pending; totals cross-foot;
      pending_refs/universe_resolved recomputed from a fresh blob recount
  V7  manifest consistency: 25 verdict rows == sidecars; pre-existing rows
      value-identical vs HEAD; manifest.cie_verdict totals == sums
  V8  footprint: 19 non-verdict CIE lanes + 49 Edexcel spec-links files
      byte-identical vs HEAD; the 25 lanes' pre-existing code entries
      preserved verbatim (order included); non-cascade item fields intact
  V9  footprint guard: git status changes within the declared set
  V10 reproducibility: fresh in-process re-evaluation of 2 sample lanes
      matches the sheet exactly (fixed stamp; no wall-clock dependence)
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

REPO = Path("/home/z/my-project/syllabai-resources")
SL = REPO / "spec-links"
LANE_ID = "T-SPECS-CIE-VERDICT-1"
BASE = "fea58c8a"
STAMP = "2026-10-18T22:46:00Z"
METHOD = "operator_verdict"
TIERS = ("V1_name_text_identity", "V2_name_phrase_identity",
         "V3_subsection_head_identity", "V4_settext_title_identity",
         "V5_topic_scoped_phrase_identity")
JOIN_TIERS = ("T1_verbatim", "T2_near")
JOIN_METHODS = ("cie_definition_text_join", "cie_text_join")

VERDICT_LANES = [
    "cie-a-level-business-23", "cie-a-level-computer-science-19",
    "cie-a-level-economics-23", "cie-a-level-maths-20-mechanics",
    "cie-a-level-maths-20-probability-and-statistics-1",
    "cie-a-level-maths-20-probability-and-statistics-2",
    "cie-a-level-maths-20-pure-1", "cie-a-level-maths-20-pure-3",
    "cie-as-english-general-paper-21", "cie-igcse-accounting-21",
    "cie-igcse-accounting-25", "cie-igcse-economics-25",
    "cie-igcse-english-language-20", "cie-igcse-english-language-25",
    "cie-igcse-english-literature-21", "cie-igcse-environmental-management-25",
    "cie-igcse-further-maths-additional-maths-25", "cie-igcse-history-18",
    "cie-igcse-ict-21", "cie-igcse-maths-25-core", "cie-igcse-maths-25-extended",
    "cie-igcse-maths-international-maths-23-core",
    "cie-igcse-maths-international-maths-23-extended",
    "cie-igcse-religious-studies-23",
    "cie-igcse-science-co-ordinated-sciences-double-award-23-biology",
]

results = []


def check(jid, name, ok, detail=""):
    results.append((jid, name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {jid} {name}" + (f" — {detail}" if detail else ""))


def git_show(path: str) -> bytes:
    r = subprocess.run(["git", "-C", str(REPO), "show", f"{BASE}:{path}"],
                       capture_output=True)
    return r.stdout if r.returncode == 0 else b""


def git_ls() -> set:
    r = subprocess.run(["git", "-C", str(REPO), "ls-tree", "-r", "--name-only", BASE],
                       capture_output=True, text=True)
    return set(r.stdout.splitlines())


# ---- normalization SPEC (same semantics as the join/gate/verdict lineage:
# NFKC, lower, & -> and, ALL punctuation stripped to spaces). Independence
# lives in the RULE CODE below, not in a divergent SPEC; the self-test pins
# norm2 == engine.norm on unicode-punctuation probes (the gate's pattern).
def norm2(s: str) -> str:
    s = unicodedata.normalize("NFKC", s or "").lower().replace("&", " and ")
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def phrase2(needle: str, hay: str) -> bool:
    return bool(needle) and f" {needle} " in f" {hay} "


def artifact_strip2(s: str) -> str:
    return re.sub(r"\b(notes?|examples?)\b", " ", s or "")


def main() -> int:
    import yaml

    json_out = None
    if "--json" in sys.argv:
        json_out = sys.argv[sys.argv.index("--json") + 1]

    sheet = yaml.safe_load((REPO / "scripts" / "cie_verdict_fill_verdicts.yaml").read_text())
    sheet_v = {}
    for e in sheet["verdicts"]:
        sheet_v.setdefault(e["lane"], {})[e["id"]] = e
    sheet_a = {}
    for e in sheet["ambiguous"]:
        sheet_a.setdefault(e["lane"], {})[e["id"]] = e

    all_git = git_ls()
    sidecars = {lane: json.loads((SL / f"{lane}.json").read_text()) for lane in VERDICT_LANES}
    head_sidecars = {lane: json.loads(git_show(f"spec-links/{lane}.json") or b"null")
                     for lane in VERDICT_LANES}

    # registries
    man = json.loads((REPO / "Official-Specifications" / "manifest.json").read_text())
    qual_of = {q["slug"]: q for q in man["qualifications"]}
    regs = {}
    for lane in VERDICT_LANES:
        qual = sidecars[lane]["qual"]
        q = qual_of[qual]
        regs[lane] = json.loads((REPO / "Official-Specifications" / "parsed" / qual /
                                 (Path(q["pdf"]).stem + ".parsed.json")).read_text())

    # ---- pools (mirror the lane scoping contract; independent implementation)
    SCIENCES = {"biology": "Biology", "chemistry": "Chemistry", "physics": "Physics"}

    def lane_scope2(lane):
        for suf, sc in SCIENCES.items():
            if lane.endswith("-" + suf):
                return sc
        return ""

    def lane_tier2(lane):
        if re.search(r"-(core)(-\d+)?$", lane):
            return "Core"
        if re.search(r"-(extended)(-\d+)?$", lane):
            return "Extended"
        return ""

    COMPONENTS = {
        "cie-a-level-maths-20-mechanics": ["mechanics"],
        "cie-a-level-maths-20-probability-and-statistics-1": ["probability and statistics 1"],
        "cie-a-level-maths-20-probability-and-statistics-2": ["probability and statistics 2"],
        "cie-a-level-maths-20-pure-1": ["pure mathematics 1", "pure mathematics 2"],
        "cie-a-level-maths-20-pure-3": ["pure mathematics 3"],
    }

    def pool2(lane):
        pts = regs[lane]["spec_points"]
        sc = lane_scope2(lane)
        if sc:
            pts = [p for p in pts if (p.get("scope") or "") == sc]
        t = lane_tier2(lane)
        if t:
            tf = [p for p in pts if p.get("tier") == t]
            pts = tf or pts
        comps = COMPONENTS.get(lane)
        if comps:
            def tt(p):
                x = p.get("topic") or {}
                return norm2(x.get("title") if isinstance(x, dict) else "")
            sel = [p for p in pts if tt(p) in comps]
            pts = sel or pts
        return pts

    # ---- blobs (fresh reader: one ls-tree per lane, chunked --batch, cached)
    _blob_cache = {}

    def lane_blobs(lane):
        if lane in _blob_cache:
            return _blob_cache[lane]
        note_paths = sorted(p for p in all_git
                            if p.startswith(f"SME-RevisionNotes/{lane}/notes/")
                            and p.endswith(".json"))
        shas = {}
        if note_paths:
            r = subprocess.run(["git", "-C", str(REPO), "ls-tree", "-r", BASE, "--",
                                f"SME-RevisionNotes/{lane}/notes/"],
                               capture_output=True, text=True)
            for line in r.stdout.splitlines():
                meta, _, path = line.partition("\t")
                parts = meta.split()
                if len(parts) >= 3 and parts[1] == "blob" and path in set(note_paths):
                    shas[parts[2]] = path
        out = {}
        items = list(shas.items())
        CH = 300
        for i in range(0, len(items), CH):
            batch = items[i:i + CH]
            proc = subprocess.run(["git", "-C", str(REPO), "cat-file", "--batch"],
                                  input="".join(s + "\n" for s, _ in batch).encode(),
                                  capture_output=True)
            buf = proc.stdout
            pos = 0
            for sha, p in batch:
                hdr_end = buf.index(b"\n", pos)
                hdr = buf[pos:hdr_end].decode()
                parts = hdr.split()
                if len(parts) < 3 or parts[1] != "blob":
                    continue
                ln = int(parts[2])
                data = buf[hdr_end + 1:hdr_end + 1 + ln]
                out[p] = data.decode("utf-8", "replace")
                pos = hdr_end + 1 + ln + 1
        _blob_cache[lane] = out
        return out

    # ---- V1
    bad = []
    for lane in VERDICT_LANES:
        d = sidecars[lane]
        rs = d.get("review_state") or {}
        if rs.get("state") != "ACCEPTED" or rs.get("gate") != "T-SPECS-CIE-GATE-1":
            bad.append(f"{lane}:state")
        v = rs.get("verdict") or {}
        if v.get("lane") != LANE_ID or v.get("applied_utc") != STAMP or \
                not v.get("directive") or not v.get("tiers"):
            bad.append(f"{lane}:review_state.verdict")
        av = (d.get("anchors") or {}).get("verdict") or {}
        if av.get("lane") != LANE_ID or "resolved_ids" not in av or \
                "pending_reasons" not in av:
            bad.append(f"{lane}:anchors.verdict")
        if d.get("schema") != "syllabai.learner-spec-links/1.0" or \
                d.get("board") != "cambridge-cie":
            bad.append(f"{lane}:schema")
    check("V1", "25 verdict lanes well-formed (ACCEPTED + additive verdict blocks)",
          not bad, str(bad[:4]))

    # ---- V2 bijection
    bad2, ok2 = [], True
    for lane in VERDICT_LANES:
        d = sidecars[lane]
        pre, post = head_sidecars[lane], d
        pre_pend = {s for it in pre["items"].values() for s in (it.get("pending") or [])}
        post_pend = {s for it in post["items"].values() for s in (it.get("pending") or [])}
        resolved = pre_pend - post_pend
        sheet_ids = set(sheet_v.get(lane, {}))
        av = d["anchors"]["verdict"]
        by_tier = av.get("by_tier") or {}
        if resolved != sheet_ids:
            bad2.append(f"{lane}:resolved!=sheet diff={sorted(resolved ^ sheet_ids)[:3]}")
        if av.get("resolved_ids") != len(resolved):
            bad2.append(f"{lane}:resolved_count")
        if sum(by_tier.values()) != len(resolved):
            bad2.append(f"{lane}:by_tier_sum")
        # per-tier counts match the sheet
        from collections import Counter
        st = Counter(e["tier"] for e in sheet_v.get(lane, {}).values())
        if dict(st) != {k: v for k, v in by_tier.items() if v}:
            bad2.append(f"{lane}:tier_dist {dict(st)} vs {by_tier}")
    check("V2", "verdict bijection (resolved == sheet == by_tier, per lane)",
          not bad2, str(bad2[:4]))

    # ---- V3/V4
    dang, bad_vocab = [], []
    for lane in VERDICT_LANES:
        ids = {p["id"]: str(p.get("official_code")) for p in regs[lane]["spec_points"]}
        for it in sidecars[lane]["items"].values():
            for c in it.get("codes") or []:
                if c.get("method") == METHOD:
                    if c.get("official_id") not in ids:
                        dang.append(f"{lane}:{c.get('official_id')}")
                    elif ids[c["official_id"]] != c.get("official_code"):
                        dang.append(f"{lane}:{c.get('official_id')}:code")
                    if c.get("tier") not in TIERS:
                        bad_vocab.append(f"{lane}:{c.get('tier')}")
                else:
                    if c.get("tier") not in JOIN_TIERS or c.get("method") not in JOIN_METHODS:
                        bad_vocab.append(f"{lane}:join:{c.get('tier')}/{c.get('method')}")
    check("V3", "zero dangling verdict targets (id + code in registry)",
          not dang, str(dang[:4]))
    check("V4", "verdict + join vocabularies both conform", not bad_vocab,
          str(bad_vocab[:4]))

    # ---- V5 independent re-derivation (fresh logic)
    # SPEC-equivalence self-test first (probes: typographic quotes, ayin,
    # apostrophes, ampersands, dashes) — norm2 must equal the engine's norm.
    import cie_verdict_fill as _eng
    _probes = [
        "Roosevelt\u2019s inauguration and the \u2018Hundred Days\u2019",
        "Shi\u2019ah beliefs \u02bf about the Twelve Imams",
        "Mi'ad (Day of Resurrection)",
        "Dot & Cross Diagrams — \u2014 test",
        "\u201cQuoted Title\u201d 'single'",
    ]
    _st_fail = [p for p in _probes if _eng.norm(p) != norm2(p)]
    check("V5a", "normalization SPEC equivalence self-test (5 probes)",
          not _st_fail, str(_st_fail[:2]))

    def rederive(lane, sid, blobs):
        """Fresh evaluator: returns (tier, official_id) the id must resolve to."""
        pts = pool2(lane)
        rec = None
        topic_title = ""
        for p, blob in blobs.items():
            try:
                n = json.loads(blob)
            except Exception:
                continue
            tt = (n.get("titles") or {}).get("topic") or ""
            for b in n.get("blocks") or []:
                if b.get("type") == "spec_point" and b.get("id") == sid:
                    rec = b
                    topic_title = tt
                    break
            if rec:
                break
        if not rec:
            return None
        name = rec.get("name") or ""
        nn = norm2(name)
        texts = [(p, norm2(p.get("text"))) for p in pts]
        eq = [p for p, t in texts if t and t == nn]
        if len(eq) == 1:
            return ("V1_name_text_identity", eq[0]["id"])
        if len(eq) > 1:
            return "AMBIG"
        ph = [p for p, t in texts if len(nn) >= 3 and phrase2(nn, t)]
        if len(ph) == 1:
            return ("V2_name_phrase_identity", ph[0]["id"])
        if len(ph) > 1:
            # V5 scoped disambiguation (battery accepts a topic-title-scoped
            # unique hit as confirming evidence for the engine's section-first
            # version; both share the same SPEC)
            topi = {}
            for p, t in texts:
                x = p.get("topic") or {}
                topi.setdefault(norm2(x.get("title") if isinstance(x, dict) else ""),
                                []).append(p)
            if topic_title and norm2(topic_title) in topi:
                scoped = [p for p in topi[norm2(topic_title)]
                          if phrase2(nn, norm2(p.get("text")))]
                if len(scoped) == 1:
                    return ("V5_topic_scoped_phrase_identity", scoped[0]["id"])
            return "AMBIG"
        subs = {}
        for p in pts:
            x = p.get("subsection") or {}
            subs.setdefault(norm2(artifact_strip2(x.get("title") or "")), []).append(p)
        for cand in (name, topic_title):
            nc = norm2(artifact_strip2(cand))
            if nc and nc in subs:
                if len(subs[nc]) == 1:
                    return ("V3_subsection_head_identity", subs[nc][0]["id"])
                return "AMBIG"
        if "literature" in regs[lane]["id"]:
            seg = norm2(name.split(":")[0]) if name else ""
            if seg:
                def qt(x):
                    m = re.search(r"[\u2018'\"“]([^'\u2019\"”]+)[\u2019'\"”]", x or "")
                    return norm2(m.group(1)) if m else ""
                qh = [p for p, t in texts if qt(p.get("text")) and qt(p.get("text")) == seg]
                if len(qh) == 1:
                    return ("V4_settext_title_identity", qh[0]["id"])
                if len(qh) > 1:
                    return "AMBIG"
        return None

    v5_fail, v5_n = [], 0
    for lane in VERDICT_LANES:
        for sid, e in sheet_v.get(lane, {}).items():
            r = rederive(lane, sid, lane_blobs(lane))
            v5_n += 1
            if r == "AMBIG" or r is None:
                v5_fail.append(f"{lane}:{sid}:rederive={r}")
            elif r[0] != e["tier"] or r[1] != e["official_id"]:
                v5_fail.append(f"{lane}:{sid}:{r}!={e['tier']}/{e['official_id']}")
    check("V5", f"independent re-derivation of every resolve ({v5_n})",
          not v5_fail, str(v5_fail[:4]))
    # ---- V6 cascade integrity + fresh universe recount
    cas, uni_bad = [], []
    for lane in VERDICT_LANES:
        d = sidecars[lane]
        pre = head_sidecars[lane]
        vmap = {}
        for sid, e in sheet_v.get(lane, {}).items():
            vmap[sid] = e["official_id"]
        pre_pend = {k: set(it.get("pending") or []) for k, it in pre["items"].items()}
        blobs = lane_blobs(lane)
        universe = set()
        for blob in blobs.values():
            try:
                n = json.loads(blob)
            except Exception:
                continue
            for b in n.get("blocks") or []:
                if b.get("type") == "spec_point" and b.get("id"):
                    universe.add(b["id"])
        a = d["anchors"]
        if len(universe) != a.get("universe_ids"):
            uni_bad.append(f"{lane}:universe {len(universe)}!={a.get('universe_ids')}")
        pend_all = set()
        refs = 0
        for it in d["items"].values():
            refs += len(it.get("pending") or [])
            for s in it.get("pending") or []:
                pend_all.add(s)
        if refs != a.get("pending_refs"):
            cas.append(f"{lane}:pending_refs {refs}!={a.get('pending_refs')}")
        if a["verdict"].get("pending_ids") != len(pend_all & universe):
            cas.append(f"{lane}:pending_ids")
        if a.get("universe_resolved") != len(universe) - len(pend_all & universe):
            cas.append(f"{lane}:universe_resolved")
        t = d["totals"]
        by = {"notes": 0, "question_parts": 0, "flashcards": 0}
        coded = {"notes": 0, "question_parts": 0, "flashcards": 0}
        for it in d["items"].values():
            by[it["kind"] + "s"] += 1
            coded[it["kind"] + "s"] += 1 if it["codes"] else 0
        if t["by_kind"] != by or t["coded_by_kind"] != coded or \
                t["items_with_codes"] != sum(coded.values()):
            cas.append(f"{lane}:totals")
        # per-item: verdict codes only on pre-anchoring items; resolved out of pending
        for k, it in d["items"].items():
            pp = pre_pend.get(k, set())
            v_codes = [c for c in (it.get("codes") or []) if c.get("method") == METHOD]
            v_oids = {c["official_id"] for c in v_codes}
            want = {vmap[s] for s in pp if s in vmap}
            # an item keeps only verdict codes it is entitled to; an oid may
            # also have arrived via the pre-lane join — subtract those
            pre_oids = {c["official_id"] for c in (pre["items"][k].get("codes") or [])} \
                if k in pre["items"] else set()
            if v_oids - want - pre_oids:
                cas.append(f"{lane}:{k}:extra_verdict_codes")
            for s in (pp & set(vmap)):
                if s in (it.get("pending") or []):
                    cas.append(f"{lane}:{k}:resolved_still_pending")
    check("V6", "cascade integrity + fresh universe recount (25 lanes)",
          not cas and not uni_bad, str((cas + uni_bad)[:4]))

    # ---- V7 manifest
    slm = json.loads((SL / "manifest.json").read_text())
    slm_head = json.loads(git_show("spec-links/manifest.json") or b"null")
    bad7 = []
    for lane in VERDICT_LANES:
        d = sidecars[lane]
        row = slm["courses"].get(lane) or {}
        t, a = d["totals"], d["anchors"]
        if row.get("items") != t["items"] or \
                row.get("items_with_codes") != t["items_with_codes"] or \
                row.get("by_kind") != t["by_kind"] or \
                row.get("coded_by_kind") != t["coded_by_kind"] or \
                row.get("pending_refs") != a["pending_refs"]:
            bad7.append(f"{lane}:row")
        rv = row.get("verdict") or {}
        if rv.get("resolved_ids") != a["verdict"]["resolved_ids"] or \
                rv.get("by_tier") != a["verdict"]["by_tier"]:
            bad7.append(f"{lane}:row.verdict")
        # pre-existing rows untouched
        if lane not in VERDICT_LANES:
            continue
    for lane, row in slm_head.get("courses", {}).items():
        if lane in VERDICT_LANES:
            continue
        if slm["courses"].get(lane) != row:
            bad7.append(f"pre-existing:{lane}")
    cv = slm.get("cie_verdict") or {}
    tot_res = sum(sidecars[l]["anchors"]["verdict"]["resolved_ids"] for l in VERDICT_LANES)
    tot_codes = sum(1 for l in VERDICT_LANES for it in sidecars[l]["items"].values()
                    for c in it.get("codes") or [] if c.get("method") == METHOD)
    if cv.get("resolved_ids_total") != tot_res or \
            cv.get("code_entries_added_total") != tot_codes or \
            cv.get("applied_utc") != STAMP or cv.get("lanes") != 25:
        bad7.append("cie_verdict_block")
    check("V7", "manifest verdict rows + pre-existing rows + cie_verdict block",
          not bad7, str(bad7[:4]))

    # ---- V8 footprint vs HEAD
    bad8 = []
    for f in sorted(all_git):
        if f.startswith("spec-links/") and f.endswith(".json"):
            lane = Path(f).stem
            if lane in VERDICT_LANES or lane in ("manifest",):
                continue
            cur = (REPO / f).read_bytes()
            if cur != git_show(f):
                bad8.append(f)
    check("V8a", "non-verdict CIE lanes + Edexcel spec-links byte-identical vs HEAD",
          not bad8, str(bad8[:4]))
    bad8b = []
    for lane in VERDICT_LANES:
        pre = head_sidecars[lane]
        for k, pit in pre["items"].items():
            nit = sidecars[lane]["items"].get(k)
            if nit is None:
                bad8b.append(f"{lane}:{k}:missing")
                continue
            for fld in ("kind", "label", "section", "topic"):
                if pit.get(fld) != nit.get(fld):
                    bad8b.append(f"{lane}:{k}:{fld}")
            pre_codes = [c for c in (pit.get("codes") or [])]
            post_join_codes = [c for c in (nit.get("codes") or [])
                               if c.get("method") != METHOD]
            if pre_codes != post_join_codes:
                bad8b.append(f"{lane}:{k}:join_codes_altered")
            pre_pend = list(pit.get("pending") or [])
            post_pend = list(nit.get("pending") or [])
            vmap = {sid: True for sid in sheet_v.get(lane, {})}
            expected_pend = [s for s in pre_pend if s not in vmap]
            if post_pend != expected_pend:
                bad8b.append(f"{lane}:{k}:pending_delta")
    check("V8b", "join payload preserved verbatim; pending delta == verdict removals",
          not bad8b, str(bad8b[:4]))

    # ---- V9 footprint guard (working tree)
    r = subprocess.run(["git", "-C", str(REPO), "status", "--porcelain"],
                       capture_output=True, text=True)
    declared_prefixes = ("spec-links/", "scripts/cie_verdict_fill", "graph/reports/T_SPECS_CIE_VERDICT_1",
                         "scripts/cie_verdict_check")
    stray = []
    for line in r.stdout.splitlines():
        p = line[3:].strip().strip('"')
        if p.startswith("scripts/cie_verdict_fill_verdicts.yaml"):
            continue
        if not p.startswith(declared_prefixes):
            stray.append(p)
    check("V9", "footprint guard (git status within declared set)", not stray,
          str(stray[:6]))

    # ---- V10 reproducibility (evaluation-level, 2 sample lanes)
    sys.path.insert(0, str(REPO / "scripts"))
    import importlib
    import cie_verdict_fill as eng
    importlib.reload(eng)
    bad10 = []
    eng_files = eng.ls_tree()
    for lane in ("cie-igcse-ict-21", "cie-igcse-religious-studies-23"):
        r10 = eng.evaluate_lane(lane, regs[lane], eng_files, {})
        sheet_ids = {sid: (e["tier"], e["official_id"])
                     for sid, e in sheet_v.get(lane, {}).items()}
        got = {sid: (v["tier"], v["official_id"])
               for sid, v in r10["verdicts"].items()}
        if got != sheet_ids:
            bad10.append(f"{lane}:reval mismatch {len(got)} vs {len(sheet_ids)}")
    check("V10", "fixed-stamp re-evaluation of 2 sample lanes == sheet",
          not bad10, str(bad10[:2]))

    # ---- verdict
    npass = sum(1 for _, _, ok, _ in results if ok)
    print(f"\n{'='*66}\nVERDICT-FILL BATTERY: {npass}/{len(results)} "
          f"{'ALL PASS' if npass == len(results) else 'FAILURES PRESENT'}")
    if json_out:
        doc = {
            "lane": LANE_ID,
            "generated_utc": STAMP,
            "base_commit": BASE,
            "checks": [
                {"id": jid, "name": name, "ok": bool(ok), "detail": detail}
                for jid, name, ok, detail in results
            ],
            "summary": {
                "total": len(results), "passed": npass,
                "all_pass": npass == len(results),
                "resolved_ids_total": sum(
                    sidecars[l]["anchors"]["verdict"]["resolved_ids"]
                    for l in VERDICT_LANES),
            },
        }
        Path(json_out).write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
        print(f"check record -> {json_out}")
    return 0 if npass == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
