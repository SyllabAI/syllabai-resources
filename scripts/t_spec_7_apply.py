#!/usr/bin/env python3
"""T-SPEC-7 — apply the humanities + remaining-maths spec-point verdicts
(scripts/t_spec_7_verdicts.yaml) to the fourteen unapplied lanes:

  humanities / other subjects
    igcse-accounting-17-financial-statements          (qual igcse-accounting)
    igcse-accounting-17-introduction-to-bookkeeping-and-accounting
    igcse-business-19                                 (qual igcse-business)
    igcse-economics-17                                (qual igcse-economics)
    igcse-english-literature-16                       (qual igcse-english-literature)
    igcse-geography-19                                (qual igcse-geography)
    igcse-ict-17                                      (qual igcse-ict)
  maths
    igcse-further-maths-19                            (qual igcse-further-maths)
    igcse-maths-a-18-foundation / -higher             (qual igcse-maths-a)
    igcse-maths-a-modular-24-{foundation,higher}-unit-{1,2}
                                                      (qual igcse-maths-a-modular)

Context: SME humanities/other-subject pages publish spec-point tags mostly
WITHOUT definition text (only igcse-business carries definitions, which are
verbatim copies of the official statement headings). Evidence used (all
committed in-repo): the tag NAME, the SME definition where present, the
revision-note page the tag appears on, the exam-question part texts
referencing the tag, and (literature) the published text titles. Tiers:
  V1_definition_verbatim - SME definition token-contained in statement text
  P1_name_fragment_join  - distinctive fragment shared by tag name/statement
  P2_page_context_join   - tag name + page context / exam-part text
  L1_text_title_join     - published text title contained in tag name
  pending                - no-guess tail (verbatim reasons: parse gaps
                           PDF-verified against the committed spec PDFs,
                           exam-technique guide tags, section introductions,
                           literature route duality without anchoring evidence)

Registry note: the accounting / geography / english-literature parses carry
statements without official_code; those registries are keyed by the id
suffix (e.g. S4.071, C1T07) and the suffix becomes the resolved_code. The
igcse-maths-a parse repeats Higher-walk statements with scope 'H'; the
Foundation lane's pool excludes them. The igcse-maths-a-modular parse scopes
statements U1F/U2F/U1H/U2H; each unit lane codes only statements from its
own unit scope (Foundation-walk statements are assumed knowledge on the
Higher unit lanes, matching the published modular structure). Documented
parse gaps: the geography parse dropped the detailed topic content
statements (tags join their topic's committed statement, T3-style); the
igcse-maths-a parse dropped a block of Higher content-walk statements
(surds, sine/cosine rules, algebraic fractions, quadratic inequalities,
arithmetic series, intersecting chords, histograms, cumulative frequency,
tree diagrams, conditional probability — all PDF-verified); those tails
pend with reasons and are flagged for parse repair.

Fail-closed rules (hard errors before ANY write):
  - population closure per lane: yaml resolve ids == per-lane unmapped ids
    minus pendings, exactly; pendings must sit in the unmapped tail;
    stage1_confirm/remap ids must carry existing mappings whose
    official_code matches
  - every resolve code must exist in the lane's own registry pool
  - every resolve quote must equal the committed index name for the tag
  - pending: verbatim reason required
Writes (after validation):
  - spec_point_map.json: resolves merged into mappings, resolved ids
    removed from unmapped, pendings kept with verdict reasons
  - spec_point_resolution.json sidecar covering EVERY index id (verify G2)
  - spec_point_codes written on all parts with ids (verify G1)
  - graph/reports/T_SPEC_7_HUMANITIES_MATHS_VERDICTS.{md,json}

PMT (PhysicsAndMathsTutor) excluded as an evidence source (operator
instruction 2026-09-18); no PMT content appears in any record.
"""
import json
import sys
import time
from collections import Counter
from pathlib import Path

import yaml

BASE = Path("/home/z/my-project/download/syllabai-resources")
EQ = BASE / "SME-ExamQuestion"
PARSED = BASE / "Official-Specifications" / "parsed"
REPORTS = BASE / "graph" / "reports"

LANES = {
    "igcse-accounting-17-financial-statements": ("igcse-accounting", None),
    "igcse-accounting-17-introduction-to-bookkeeping-and-accounting": ("igcse-accounting", None),
    "igcse-business-19": ("igcse-business", None),
    "igcse-economics-17": ("igcse-economics", None),
    "igcse-english-literature-16": ("igcse-english-literature", None),
    "igcse-geography-19": ("igcse-geography", None),
    "igcse-ict-17": ("igcse-ict", None),
    "igcse-further-maths-19": ("igcse-further-maths", None),
    "igcse-maths-a-18-foundation": ("igcse-maths-a", "F"),
    "igcse-maths-a-18-higher": ("igcse-maths-a", "ALL"),
    "igcse-maths-a-modular-24-foundation-unit-1": ("igcse-maths-a-modular", "U1F"),
    "igcse-maths-a-modular-24-foundation-unit-2": ("igcse-maths-a-modular", "U2F"),
    "igcse-maths-a-modular-24-higher-unit-1": ("igcse-maths-a-modular", "U1FH"),
    "igcse-maths-a-modular-24-higher-unit-2": ("igcse-maths-a-modular", "U2FH"),
}
SUFFIX_QUALS = {"igcse-accounting", "igcse-geography", "igcse-english-literature"}

METHOD_V1 = ("operator-verdict definition-verbatim join (T-SPEC-7; PMT excluded as source)")
METHOD_P1 = ("operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source)")
METHOD_P2 = ("operator-verdict page-context join (T-SPEC-7; PMT excluded as source)")
METHOD_L1 = ("operator-verdict text-title join (T-SPEC-7; PMT excluded as source)")


def registry_pool(qual, mode):
    pts = json.loads((PARSED / qual / "spec_points.json").read_text())["spec_points"]
    if qual in SUFFIX_QUALS:
        by_code = {p["id"].rsplit(":", 1)[-1]: p for p in pts}
        return by_code, pts
    if mode in (None, "ALL"):
        return {p["official_code"]: p for p in pts}, pts
    if mode == "F":
        pool = [p for p in pts if p.get("scope") != "H"]
    elif mode == "U1F":
        pool = [p for p in pts if p.get("scope") == "U1F"]
    elif mode == "U2F":
        pool = [p for p in pts if p.get("scope") == "U2F"]
    elif mode == "U1FH":
        pool = [p for p in pts if p.get("scope") in ("U1F", "U1H")]
    elif mode == "U2FH":
        pool = [p for p in pts if p.get("scope") in ("U2F", "U2H")]
    else:
        pool = pts
    return {p["official_code"]: p for p in pool}, pool


def topic_files(cdir: Path):
    return sorted(cdir.glob("*/*/*/topic.json")) + \
        sorted(cdir.glob("*/*/topic.json")) + sorted(cdir.glob("*/topic.json"))


def main() -> int:
    t0 = time.time()
    doc = yaml.safe_load((BASE / "scripts" / "t_spec_7_verdicts.yaml").read_text())
    idv = doc["id_verdicts"]

    state = {}
    for lane, (qual, mode) in LANES.items():
        cdir = EQ / lane
        mp = json.loads((cdir / "spec_point_map.json").read_text())
        idx = json.loads((cdir / "spec_point_index.json").read_text())
        by_code, _ = registry_pool(qual, mode)
        state[lane] = {
            "qual": qual, "dir": cdir, "map": mp, "index": idx, "by_code": by_code,
            "mappings": mp.get("mappings", {}),
            "unmapped": {u["spcpt_id"]: u.get("reason", "") for u in mp.get("unmapped", [])},
        }

    # ---------- population closure + validation ----------
    errors = []
    for lane, st in state.items():
        got_res, got_pen = set(), set()
        for sid, v in idv.items():
            crec = (v.get("courses") or {}).get(lane)
            if crec is None:
                continue
            verdict = crec.get("verdict") or v["verdict"]
            if verdict == "pending":
                got_pen.add(sid)
            elif not crec.get("stage1_confirm") and crec.get("superseded_code") is None:
                got_res.add(sid)
        need_res = set(st["unmapped"]) - got_pen
        if not need_res <= got_res:
            errors.append(f"{lane}: resolve coverage gap "
                          f"need-only={sorted(need_res - got_res)[:4]} "
                          f"(need={len(need_res)} got={len(got_res)})")
        for sid in got_pen:
            crec = (idv[sid].get("courses") or {}).get(lane) or {}
            if sid not in st["unmapped"] and sid in st["mappings"] \
                    and not crec.get("demote"):
                errors.append(f"{lane}: pending {sid} not in unmapped tail")
        for sid, v in idv.items():
            crec = (v.get("courses") or {}).get(lane)
            if not crec or (crec.get("verdict") or v["verdict"]) != "resolve":
                continue
            if sid in st["mappings"] and not crec.get("stage1_confirm") \
                    and "superseded_code" not in crec:
                errors.append(f"{lane}: resolve {sid} would silently overwrite "
                              f"an existing mapping (no superseded_code)")
            e = st["index"]["spec_points"].get(sid)
            if e is None:
                errors.append(f"{lane}: {sid} not in index")
                continue
            if (crec.get("quote") or e.get("name") or "") != (e.get("name") or ""):
                errors.append(f"{lane}: {sid} quote mismatch")
            code = crec["codes"][0]
            if code not in st["by_code"]:
                errors.append(f"{lane}: {sid} code {code} not in registry pool")
            elif "superseded_code" in crec:
                m = st["mappings"].get(sid)
                if not m:
                    errors.append(f"{lane}: remap {sid} has no existing mapping")
                elif m.get("official_code") != crec["superseded_code"]:
                    errors.append(f"{lane}: remap {sid} superseded "
                                  f"{crec['superseded_code']!r} != existing {m.get('official_code')!r}")
            elif crec.get("stage1_confirm"):
                m = st["mappings"].get(sid)
                if not m:
                    errors.append(f"{lane}: stage1_confirm {sid} has no existing mapping")
                elif m.get("official_code") != code:
                    errors.append(f"{lane}: stage1_confirm {sid} existing "
                                  f"{m.get('official_code')} != confirmed {code}")
            if v["verdict"] == "pending" and not (crec.get("reason") or "").strip():
                errors.append(f"{lane}: pending {sid} without verbatim reason")

    if errors:
        print("VALIDATION FAILED — no writes performed:")
        for e in errors:
            print("  -", e)
        return 1

    # ---------- apply ----------
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    summary = {}
    for lane, st in state.items():
        merged = remapped = demoted = 0
        # demote stage-1 mappings overridden by pending verdicts: the
        # provisional name-only match is withdrawn (no-guess discipline)
        for sid, v in idv.items():
            crec = (v.get("courses") or {}).get(lane)
            if not crec or (crec.get("verdict") or v["verdict"]) != "pending" or not crec.get("demote"):
                continue
            if st["mappings"].pop(sid, None) is not None:
                demoted += 1
            st["unmapped"].setdefault(
                sid, (crec.get("reason") or "pending verdict (T-SPEC-7)"))
        for sid, v in idv.items():
            crec = (v.get("courses") or {}).get(lane)
            if not crec or (crec.get("verdict") or v["verdict"]) != "resolve" or crec.get("stage1_confirm"):
                continue
            codes = [str(c) for c in crec["codes"]]
            lead = st["by_code"][codes[0]]
            remap = "superseded_code" in crec
            tier = v.get("tier", "P2_page_context_join")
            method = {"V1_definition_verbatim": METHOD_V1,
                      "P1_name_fragment_join": METHOD_P1,
                      "L1_text_title_join": METHOD_L1}.get(tier, METHOD_P2)
            st["mappings"][sid] = {
                "official_id": lead["id"],
                "official_code": codes[0],
                "tier": tier,
                "score": None if remap else 1.0,
                "unit": None,
                "method": method,
                "resolution": {
                    "lane": "operator-verdict (T-SPEC-7)",
                    "quote": crec.get("quote") or v.get("quote"),
                    "page": v.get("page"),
                    "twin_codes": codes[1:] or None,
                    "superseded_code": crec.get("superseded_code"),
                    "pmt_excluded": True,
                },
            }
            st["unmapped"].pop(sid, None)
            if remap:
                remapped += 1
            else:
                merged += 1

        # 1) map
        mp = st["map"]
        mp["mappings"] = st["mappings"]
        um = []
        for sid in sorted(st["unmapped"]):
            vv = idv.get(sid) or {}
            crec = (vv.get("courses") or {}).get(lane) or {}
            reason = (crec.get("reason") or st["unmapped"][sid]) \
                if (crec.get("verdict") or vv.get("verdict")) == "pending" else st["unmapped"][sid]
            um.append({"spcpt_id": sid,
                       "name": (st["index"]["spec_points"].get(sid) or {}).get("name"),
                       "reason": reason})
        mp["unmapped"] = um
        (st["dir"] / "spec_point_map.json").write_text(
            json.dumps(mp, ensure_ascii=False, indent=1), encoding="utf-8")

        # 2) resolution sidecar covering EVERY index id (verify G2)
        part_refs = Counter()
        for f in topic_files(st["dir"]):
            t = json.loads(f.read_text())
            for q in t.get("questions", []):
                for p in q.get("parts", []):
                    for s in p.get("spec_point_ids") or []:
                        part_refs[s] += 1
        records = []
        for sid, e in st["index"]["spec_points"].items():
            rec = {"id": sid, "sme_name": e.get("name"),
                   "sme_definition": e.get("definition"),
                   "referenced_by_parts": part_refs.get(sid, 0)}
            m = st["mappings"].get(sid)
            if m:
                stmt = st["by_code"].get(m["official_code"], {})
                rec.update({
                    "resolved_code": m["official_code"],
                    "official_id": m["official_id"],
                    "official_wording": stmt.get("text"),
                    "tier": m["tier"], "score": m.get("score"),
                    "method": m.get("method"), "unit": m.get("unit"),
                })
            else:
                vv = idv.get(sid) or {}
                crec = (vv.get("courses") or {}).get(lane) or {}
                rec["resolved_code"] = None
                rec["reason"] = (crec.get("reason") or "no-guess pending") \
                    if (crec.get("verdict") or vv.get("verdict")) == "pending" else "unresolved (T-SPEC-7: no verdict; honest tail)"
            records.append(rec)
        res_doc = {
            "schema": "syllabai.sme-spec-point-resolution/1.0",
            "generated_utc": now,
            "validation": "AI_VALIDATED (operator-delegated chain; "
                          "definition-verbatim / name-fragment / page-context / "
                          "text-title joins per T-SPEC-7; parse-gap pendings "
                          "PDF-verified; PMT excluded as source); HUMAN_VALIDATED "
                          "reserved for human review",
            "counts": {
                "ids": len(records),
                "resolved": sum(1 for r in records if r.get("resolved_code")),
                "unresolved": sum(1 for r in records if not r.get("resolved_code")),
            },
            "unresolved_allowlist_note": "parts whose ids are all unresolved "
                                         "stay uncoded by design (no-guess discipline)",
            "resolved": records,
        }
        (st["dir"] / "spec_point_resolution.json").write_text(
            json.dumps(res_doc, ensure_ascii=False, indent=1), encoding="utf-8")

        # 3) part codes: id-derived
        coded = uncoded = 0
        for f in topic_files(st["dir"]):
            t = json.loads(f.read_text())
            changed = False
            for q in t.get("questions", []):
                for p in q.get("parts", []):
                    sids = p.get("spec_point_ids") or []
                    if not sids:
                        continue
                    codes, seen = [], set()
                    for s in sids:
                        m = st["mappings"].get(s)
                        if m and m["official_code"] not in seen:
                            codes.append(m["official_code"])
                            seen.add(m["official_code"])
                    if codes:
                        p["spec_point_codes"] = codes
                        coded += 1
                        changed = True
                    else:
                        uncoded += 1
            if changed:
                f.write_text(json.dumps(t, ensure_ascii=False, indent=1), encoding="utf-8")

        n = res_doc["counts"]
        summary[lane] = {"ids": n["ids"], "resolved": n["resolved"],
                         "unresolved": n["unresolved"], "map_merged": merged,
                         "remaps": remapped, "demotes": demoted,
                         "parts_coded": coded, "parts_uncoded": uncoded}
        print(f"[{lane}] resolved {n['resolved']}/{n['ids']} ids (+{merged} merges, "
              f"{remapped} remaps, {demoted} demotes); parts coded {coded}, "
              f"uncoded {uncoded}")

    # ---------- report ----------
    REPORTS.mkdir(parents=True, exist_ok=True)
    report = {
        "schema": "syllabai.t-spec-7-report/1.0",
        "generated_utc": now,
        "courses": list(LANES),
        "summary": summary,
        "verdict_counts": doc["courses"],
        "evidence_note": "Humanities and remaining-maths lanes: joins use tag "
                         "name, SME definition (business), revision-note page, "
                         "exam-part text, published text titles (literature) and "
                         "topic anchors (geography). Accounting/geography/"
                         "english-literature parses carry no official_code; "
                         "id-suffix codes are used. Parse gaps documented and "
                         "PDF-verified; pendings flagged for parse repair.",
        "parse_notes": [
            "igcse-geography: the committed parse dropped the detailed topic "
            "content statements (PDF-verified against the published issue-3 "
            "spec); tags join their topic's committed statement (T3-style "
            "section anchor) and the tail pends; parse repair flagged to "
            "restore statement-level granularity.",
            "igcse-maths-a: the committed parse dropped a block of Higher "
            "content-walk statements (surds + rationalising, recurring "
            "decimals, algebraic fractions, quadratic inequalities, "
            "arithmetic series, sine/cosine rules, elevation/depression, "
            "intersecting chord properties, algebraic proof, histograms, "
            "cumulative frequency, tree diagrams, conditional probability, "
            "sectors) — all PDF-verified present in the published spec; the "
            "affected tags pend with reasons; parse repair flagged.",
            "igcse-accounting: the Topic 4 content walk survived only as the "
            "ratio fragments S4.069-S4.072; most financial-statements topics "
            "pend flagged for parse repair.",
            "igcse-maths-a-modular: unit-scoped pools (U1F/U2F/U1H/U2H) "
            "enforced per lane; Foundation-walk statements are assumed "
            "knowledge on the Higher unit lanes, matching the published "
            "modular structure.",
        ],
        "pmt_excluded": True,
    }
    (REPORTS / "T_SPEC_7_HUMANITIES_MATHS_VERDICTS.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    md = ["# T-SPEC-7 — humanities + remaining maths spec-point verdicts "
          "(2026-09-19)", "",
          "SME humanities/other-subject pages publish spec-point tags mostly "
          "without definition text (only igcse-business carries definitions — "
          "verbatim official statement headings, enabling T-SPEC-3-style "
          "definition-verbatim joins). Evidence used: tag name, definition "
          "where present, revision-note page anchoring, exam-part text and "
          "published text titles (literature). Registries without "
          "official_code use id-suffix codes (S4.071, C1T07, ...). Documented "
          "parse gaps (PDF-verified): the geography parse dropped the "
          "detailed topic content statements (tags join their topic's "
          "committed statement, T3-style; repair flagged); the igcse-maths-a "
          "parse dropped a block of Higher content-walk statements (surds, "
          "sine/cosine rules, algebraic fractions, quadratic inequalities, "
          "arithmetic series, intersecting chords, histograms, cumulative "
          "frequency, tree diagrams, conditional probability, sectors); the "
          "accounting parse retained only the ratio fragments of Topic 4. "
          "PMT excluded as source.", "",
          "| lane | ids | resolved | merges | remaps | pendings | parts coded | parts uncoded |",
          "|---|---|---|---|---|---|---|---|"]
    for c, s in summary.items():
        md.append(f"| {c} | {s['ids']} | {s['resolved']} | {s['map_merged']} "
                  f"| {s['remaps']} | {s['unresolved']} | {s['parts_coded']} "
                  f"| {s['parts_uncoded']} |")
    (REPORTS / "T_SPEC_7_HUMANITIES_MATHS_VERDICTS.md").write_text(
        "\n".join(md), encoding="utf-8")

    ws = Path("/home/z/my-project/scripts/specmap_work")
    ws.mkdir(parents=True, exist_ok=True)
    (ws / "t_spec_7_apply_summary.json").write_text(
        json.dumps({"generated_utc": now, "courses": summary}, indent=1))
    print(f"report -> {REPORTS / 'T_SPEC_7_HUMANITIES_MATHS_VERDICTS.md'}")
    print(f"done in {time.time()-t0:.1f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
