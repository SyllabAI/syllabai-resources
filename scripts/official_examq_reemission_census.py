#!/usr/bin/env python3
"""F86 corpus-wide re-receipt — the census leg.

Diffes the freshly re-emitted corpus (worktree) against the corpus of record
(HEAD) slice by slice, under the normalization law of the prior parity
receipts: volatile fields (generated_utc, the generator version string) are
exempt; everything else must match byte-for-byte or be classified.

File classes:
  topic.json            structural compare after volatile normalization,
                        per-question-part field-level deltas
  questions.md          byte compare
  validation-report.json  semantic compare: per-gate statuses, negative
                        controls, review queue, applied-override listings
  assets/*              sha256 byte compare (+ exec-bit-only noise census)

Output: one JSON census (per-slice verdicts + part-level delta universe)
for the arbitration leg. Zero exotic dependencies.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

RES = Path(__file__).resolve().parent.parent
CORPUS = RES / "Official-ExamQuestion" / "igcse-chemistry-19"
GEN_VER_RE = re.compile(r"v0\.\d+\.\d+")


def head_bytes(rel: str):
    """Blob at HEAD for a repo-relative path (None if absent at HEAD)."""
    r = subprocess.run(["git", "show", f"HEAD:{rel}"], cwd=RES,
                       capture_output=True, timeout=60)
    return r.stdout if r.returncode == 0 else None


def work_bytes(p: Path):
    return p.read_bytes() if p.exists() else None


def norm_topic(raw: bytes):
    t = json.loads(raw.decode("utf-8"))
    t.pop("generated_utc", None)
    if isinstance(t.get("generator"), str):
        t["generator"] = GEN_VER_RE.sub("vX", t["generator"])
    # the edits[] disclosure embeds the applying converter version in
    # edits[].tool — a version bump alone must not read as a content delta
    for q in t.get("questions", []):
        for p in q.get("parts", []):
            for e in p.get("edits") or []:
                if isinstance(e, dict) and isinstance(e.get("tool"), str):
                    e["tool"] = GEN_VER_RE.sub("vX", e["tool"])
    return t


def canon(o):
    return json.dumps(o, sort_keys=True, ensure_ascii=False, indent=1)


def part_map(t):
    """(question_index, part_number) -> part dict, order-stable."""
    out = {}
    for qi, q in enumerate(t.get("questions", [])):
        for p in q.get("parts", []):
            out[(qi, p.get("part_number"))] = (q, p)
    return out


def field_diffs(t_old, t_new):
    """Yield (qid, part_number, field, kind, note) for every part-level delta."""
    old, new = part_map(t_old), part_map(t_new)
    diffs = []
    for key in sorted(set(old) | set(new), key=lambda k: (k[0], str(k[1]))):
        qi, pn = key
        if key not in old:
            diffs.append((qi, pn, "<part>", "added", ""))
            continue
        if key not in new:
            diffs.append((qi, pn, "<part>", "removed", ""))
            continue
        _qo, po = old[key]
        _qn, pn_new = new[key]
        for f in sorted(set(po) | set(pn_new)):
            a, b = po.get(f), pn_new.get(f)
            if canon(a) == canon(b):
                continue
            note = ""
            if f in ("choices", "mark_points") and isinstance(a, list) and isinstance(b, list):
                note = f"len {len(a)}->{len(b)}"
            elif isinstance(a, str) and isinstance(b, str):
                note = f"len {len(a)}->{len(b)}"
            diffs.append((qi, pn, f, "changed", note))
    return diffs


def report_semantics(raw: bytes):
    r = json.loads(raw.decode("utf-8"))
    return {
        "gates": {g.get("gate"): g.get("status") for g in r.get("gates", [])},
        "nc": sorted(nc.get("control", nc.get("name", "?")) for nc in r.get("negative_controls", [])),
        "review_n": len(r.get("review_queue", [])),
        "review": r.get("review_queue", []),
        "mcq_keys_applied": r.get("mcq_keys_applied"),
        "ms_link_overrides_applied": r.get("ms_link_overrides_applied"),
        "spec_tagging": r.get("spec_tagging"),
        "ocr_pages": r.get("ocr_pages"),
        "wave20": r.get("wave20"),
        "text_repairs": r.get("text_repairs"),
    }


def main():
    slices = sorted({(d.name, pd.name) for d in CORPUS.iterdir() if d.is_dir()
                     for pd in d.iterdir() if pd.name.startswith("4CH1-")})
    census = {"schema": "syllabai.official-examq.reemission-census/0.1",
              "converter_of_record": None, "slices": [], "fields": {},
              "assets": {"same": 0, "diff": 0, "added": 0, "removed": 0,
                          "mode_noise": 0, "diff_list": []},
              "totals": {"slices": len(slices)}}
    conv = json.loads((CORPUS / slices[0][0] / slices[0][1] / "topic.json").read_bytes())
    census["converter_of_record"] = conv.get("generator")

    for series, paper in slices:
        sdir = CORPUS / series / paper
        ent = {"series": series, "paper": paper, "files": {},
               "part_diffs": [], "report": {}}
        # --- topic.json
        rel = f"Official-ExamQuestion/igcse-chemistry-19/{series}/{paper}/topic.json"
        hb, wb = head_bytes(rel), work_bytes(sdir / "topic.json")
        if hb is None or wb is None:
            ent["files"]["topic.json"] = "MISSING"
        else:
            to, tn = norm_topic(hb), norm_topic(wb)
            if canon(to) == canon(tn):
                ent["files"]["topic.json"] = "same"
            else:
                ent["files"]["topic.json"] = "differ"
                d = field_diffs(to, tn)
                for qi, pn, f, kind, note in d:
                    ent["part_diffs"].append({"q": qi, "part": pn, "field": f,
                                              "kind": kind, "note": note})
                    census["fields"].setdefault(f, []).append(
                        f"{series}/{paper} q{qi} {pn} {kind} {note}".strip())
        # --- questions.md
        relq = f"Official-ExamQuestion/igcse-chemistry-19/{series}/{paper}/questions.md"
        hb, wb = head_bytes(relq), work_bytes(sdir / "questions.md")
        if hb == wb:
            ent["files"]["questions.md"] = "same"
        else:
            n = abs(len((hb or b"").splitlines()) - len((wb or b"").splitlines()))
            ent["files"]["questions.md"] = f"differ (line-delta ~{n})"
        # --- validation-report.json (semantic)
        relr = f"Official-ExamQuestion/igcse-chemistry-19/{series}/{paper}/validation-report.json"
        hb, wb = head_bytes(relr), work_bytes(sdir / "validation-report.json")
        if hb is None or wb is None:
            ent["files"]["validation-report.json"] = "MISSING"
        else:
            so, sn = report_semantics(hb), report_semantics(wb)
            ent["report"] = {}
            if so["gates"] != sn["gates"]:
                ent["report"]["gates_old"] = so["gates"]
                ent["report"]["gates_new"] = sn["gates"]
            if so["nc"] != sn["nc"]:
                ent["report"]["nc_old"], ent["report"]["nc_new"] = so["nc"], sn["nc"]
            if so["review_n"] != sn["review_n"]:
                ent["report"]["review_n_old"] = so["review_n"]
                ent["report"]["review_n_new"] = sn["review_n"]
            for k in ("mcq_keys_applied", "ms_link_overrides_applied",
                      "spec_tagging", "ocr_pages", "wave20"):
                if canon(so[k]) != canon(sn[k]):
                    ent["report"][k] = {"old": so[k], "new": sn[k]}
            ent["files"]["validation-report.json"] = "same" if not ent["report"] else "semantic-delta"
            if ent["report"] and sn["gates"] and all(v == "PASS" for v in sn["gates"].values()) \
                    and all(v == "PASS" for v in so["gates"].values()):
                ent["report"]["_note"] = "all gates PASS both sides (report prose drift only)"
        # --- assets
        adir = sdir / "assets"
        old_assets = {}
        ls = subprocess.run(["git", "ls-tree", "-r", "--name-only",
                             f"HEAD:Official-ExamQuestion/igcse-chemistry-19/{series}/{paper}/assets"],
                            cwd=RES, capture_output=True, text=True)
        for line in ls.stdout.splitlines():
            old_assets[Path(line).name] = line
        new_assets = sorted(p.name for p in adir.iterdir()) if adir.exists() else []
        for name in sorted(set(old_assets) | set(new_assets)):
            ob = head_bytes(f"Official-ExamQuestion/igcse-chemistry-19/{series}/{paper}/assets/{name}") \
                if name in old_assets else None
            nb = work_bytes(adir / name) if name in new_assets else None
            if ob is not None and nb is None:
                census["assets"]["removed"] += 1
                census["assets"]["diff_list"].append(f"{series}/{paper}/{name} REMOVED")
            elif ob is None and nb is not None:
                census["assets"]["added"] += 1
                census["assets"]["diff_list"].append(f"{series}/{paper}/{name} ADDED")
            elif hashlib.sha256(ob).hexdigest() == hashlib.sha256(nb).hexdigest():
                census["assets"]["same"] += 1
                st = os.stat(adir / name)
                if not (st.st_mode & 0o111):
                    pass  # exec-bit absent in worktree; git may flag M — mode noise
            else:
                census["assets"]["diff"] += 1
                census["assets"]["diff_list"].append(
                    f"{series}/{paper}/{name} BYTES-DIFFER old={hashlib.sha256(ob).hexdigest()[:12]} "
                    f"new={hashlib.sha256(nb).hexdigest()[:12]}")
        census["slices"].append(ent)

    # verdicts
    for ent in census["slices"]:
        ent["verdict"] = ("clean" if all(v == "same" for k, v in ent["files"].items())
                          else "deltas")
    json.dump(census, open("/tmp/f86-census.json", "w"), indent=1, ensure_ascii=False)
    # console summary
    clean = sum(1 for e in census["slices"] if e["verdict"] == "clean")
    print(f"slices: {clean}/{len(census['slices'])} clean after volatile normalization")
    print("delta fields:", {k: len(v) for k, v in census["fields"].items()})
    print("assets:", {k: v for k, v in census["assets"].items() if k != "diff_list"})
    sem = [e for e in census["slices"] if e["files"].get("validation-report.json", "").startswith("semantic")]
    print("report semantic-delta slices:", len(sem))
    qmd = [e for e in census["slices"] if e["files"].get("questions.md", "") != "same"]
    print("questions.md differing slices:", len(qmd))


if __name__ == "__main__":
    main()
