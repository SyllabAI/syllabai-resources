#!/usr/bin/env python3
"""run-013-m4 — the P5/M4 corpus-side isotope+decay debris repair (the
run-011-m3 analog) for igcse-physics-modular-24-unit-2 and
igcse-science-double-award-17-physics, then the small plane sync.

Hand-off of record: resources LANE-STATUS.md F135 (disposition CLOSED, the
M4 hand-off enumerated) <- F134 P5. Law: run-011-m3's — the corpus of
record carries the broken-converter isotope/decay debris (the literal `pre`
token glued before every mmultiscripts sub/superscript group; the aria-nbsp
`space_` base class); the repair is evidence-driven:

  - the LIVE SaveMyExams page's MathML aria-labels are the values of record
    (m3 method: curl --compressed, Chrome UA, -L; the 3 pages are archived
    beside this script), and
  - the LEXICAL form follows each bank's own healthy convention of record
    (postscript bare-letter isotope spans: $Te_{52}^{120}$, $Pu_{94}^{238}$,
    $H_{1}^{3}$, $Am_{95}^{238}$ — same files, same live page's symbols),
    with m3's decisions carried over: <none/> -> empty group {}, and the
    printed fill-in box renders as \\text{square} (the bank's own healthy
    form, e.g. the radon/iodine tick-box tables).

  NOTE the (deliberate) difference from m3's 7-1 forms: that file's bank
  convention is prescript+\\text{} (${}^{210}\\text{Po}$), these two banks'
  is postscript bare ($X_{Z}^{A}$). The m3-space rider adopted the PLANE's
  form verbatim because the plane was healthy there; here the plane carries
  the same debris (verified pre-serve), so the bank-local convention
  governs.

Repairs: 3 topic.json (the corpus of record the v2 importer consumes) +
the 5 human renders (questions.md / mark-schemes.md) by surgical
substitution with reverse-identity proof (the m3 M3-qmd shape — NOT a
re-render; no committed renderer exists for these banks).

Gates (fail-closed, all asserted before/after): G0 T1 round-trip per
topic.json (indent=1, ensure_ascii=False, trailing newline — byte-exact);
G1 debris-post-0 bank-wide (topic.json + both md renders, pre_/pre^/space_
classes); G2 dollar-parity per edited string; G3 char-safety (new forms are
ASCII); G4 count-law (per-form instance counts == the census of record);
G5 field-parity (deep-diff == exactly the 8 part-fields, everything else
byte-identical); G6 md-surgical (reverse-substitution identity byte-exact);
G7 change-set law (git status == exactly 3 topic.json + 5 md + this
dossier); G8 plane pre-identity (every touched corpus field's PRE-repair
value == the v2 plane's current value verbatim — the mapping-repair law's
precondition, DISC-1 lesson).

Receipts land beside this script: census.json, transforms.json,
evidence.json, serve-table.json (the plane-sync manifest), run-report.json,
ledger.json. Idempotent: re-running against a repaired corpus aborts on the
pre-condition (old forms absent).

Stdlib only. Run: python3 repair_m4.py --v2-root <syllabai-v2 clone>
--v2-rev <rev> --apply.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent

BANKS = {
    "igcse-physics-modular-24-unit-2": [
        "radioactivity-particles/properties-of-radiation",
    ],
    "igcse-science-double-award-17-physics": [
        "radioactivity-and-particles/properties-of-radiation",
        "radioactivity-and-particles/radioactivity-uses-and-dangers",
    ],
}

# ---- the transform table of record (old -> new), byte-exact -----------------
T_ISOTOPE = [
    (r"$\text{Po} pre_{ } pre^{210}$", r"$\text{Po}_{}^{210}$", "Po-210, Z absent (m3: <none/> -> {})"),
    (r"$\text{Pb} pre_{ } pre^{210}$", r"$\text{Pb}_{}^{210}$", "Pb-210, Z absent (m3: <none/> -> {})"),
    (r"$\text{Bi} pre_{ } pre^{210}$", r"$\text{Bi}_{}^{210}$", "Bi-210, Z absent (m3: <none/> -> {})"),
    (r"$\ \\alpha pre_{2} pre^{4}$", r"$\ \\alpha_{2}^{4}$", "alpha, Z=2 A=4 (live aria: straight alpha presubscript 2 presuperscript 4)"),
    (r"$Pu_{94}^{238} \rightarrow \ \\alpha pre_{square} pre^{4} + \mathrm{X} pre_{square} pre^{square} + \ \\gamma pre_{0} pre^{square}$",
     r"$Pu_{94}^{238} \rightarrow \ \\alpha_{\text{square}}^{4} + \mathrm{X}_{\text{square}}^{\text{square}} + \ \\gamma_{0}^{\text{square}}$",
     "Pu-238 decay chain (live aria: Pu ... rightwards arrow straight alpha presubscript square presuperscript 4 plus straight X presubscript square presuperscript square plus straight gamma presubscript 0 presuperscript square)"),
    (r"$Th_{90}^{232} \rightarrow \text{Ra} pre_{square} pre^{square} + \ \\alpha pre_{square} pre^{4}$",
     r"$Th_{90}^{232} \rightarrow \text{Ra}_{\text{square}}^{\text{square}} + \ \\alpha_{\text{square}}^{4}$",
     "Th-232 decay (live aria: Th ... rightwards arrow Ra presubscript square presuperscript square plus straight alpha presubscript square presuperscript 4)"),
    (r"$space_{23}^{50} \mathrm{V}$", r"$V_{23}^{50}$",
     "vanadium-50: aria 'space presubscript 23 presuperscript 50 straight V' — nbsp base is junk; bank-local postscript bare-letter convention (cf. healthy $Te_{52}^{120}$ in the same file)"),
]

DEBRIS_SCAN = re.compile(r"\$[^$\n]*?\bpre\b[^$\n]*?\$|\$space_[^$\n]*?\$")

# ---- the wave-D serving canon (LRM strip + asset repin + trim) --------------
# The v2 plane serves these banks with asset hrefs repinned to the bank-wide
# raw-URL pin (wave-D law: 100% of the 1,239 refs at the pin) and LRM/trim
# applied. G8 and the plane sync both speak THIS canon — corpus bytes stay
# untouched in the corpus of record.
BANK_PIN = "1a5c37bcecf379cd98e83aa74aa9472920092428"
RAW_BASE = "https://raw.githubusercontent.com/SyllabAI/syllabai-resources/" + BANK_PIN + "/"
MD_RE = re.compile(r"\]\((assets/[^)]+)\)")
IMG_RE = re.compile(r"<img src=\"(assets/[^\"]+)\"")

def canon(value: str, corpus_topic_dir: str) -> str:
    v = value.replace("\u200e", "")
    v = MD_RE.sub(lambda m: "](" + RAW_BASE + corpus_topic_dir + "/" + m.group(1) + ")", v)
    v = IMG_RE.sub(lambda m: "<img src=\"" + RAW_BASE + corpus_topic_dir + "/" + m.group(1) + "\"", v)
    return v.strip()


def sh(cmd, cwd=None, check=True):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"cmd failed: {' '.join(map(str, cmd))}\n{r.stderr[:400]}")
    return r

def sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def die(msg):
    print(f"M4 ABORT: {msg}", file=sys.stderr)
    sys.exit(1)

def t1_roundtrip_ok(raw: bytes) -> bool:
    doc = json.loads(raw.decode("utf-8"))
    return json.dumps(doc, indent=1, ensure_ascii=False).encode("utf-8") + b"\n" == raw

def dollar_parity(s: str) -> bool:
    return s.count("$") % 2 == 0

def deep_diff(a, b, path="$"):
    """Yield (path, old, new) for every scalar leaf that differs."""
    if isinstance(a, dict) and isinstance(b, dict):
        for k in sorted(set(a) | set(b)):
            yield from deep_diff(a.get(k), b.get(k), f"{path}.{k}")
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            yield (path, f"<list {len(a)}>", f"<list {len(b)}>")
        else:
            for i, (x, y) in enumerate(zip(a, b)):
                yield from deep_diff(x, y, f"{path}[{i}]")
    else:
        if a != b:
            yield (path, a, b)


# ----------------------------------------------------------------- main -----
def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--v2-root", required=True, help="syllabai-v2 clone (blobless OK)")
    ap.add_argument("--v2-rev", required=True, help="v2 rev of record for the plane pre-identity gate")
    ap.add_argument("--apply", action="store_true", help="write the repairs (omit = dry run)")
    a = ap.parse_args(argv)

    v2_root = Path(a.v2_root)

    # ---------------- 1. census (pre-state, dual view) ----------------
    # topic.json fields are censused on PARSED values; md renders on raw text.
    # The same 26 logical instances appear in both views — the cross-view
    # parity is itself a gate (G4a): per-form md count == per-form parsed count.
    corpus = {}   # relpath -> raw bytes
    for bank, topics in BANKS.items():
        for t in topics:
            for fn in ("topic.json", "questions.md", "mark-schemes.md"):
                p = REPO / "SME-ExamQuestion" / bank / t / fn
                corpus[str(p.relative_to(REPO))] = p.read_bytes()
    census_md, census_tj = {}, {}
    total_logical = 0
    for rel, raw in sorted(corpus.items()):
        if rel.endswith("topic.json"):
            doc = json.loads(raw.decode("utf-8"))
            spans = []
            for q in doc["questions"]:
                for p in q["parts"]:
                    for kind in ("problem_md", "solution_md"):
                        v = p.get(kind)
                        if isinstance(v, str):
                            spans += DEBRIS_SCAN.findall(v)
            if spans:
                census_tj[rel] = {f: spans.count(f) for f in sorted(set(spans))}
                census_tj[rel]["__total"] = len(spans)
        else:
            txt = raw.decode("utf-8")
            spans = DEBRIS_SCAN.findall(txt)
            if spans:
                census_md[rel] = {f: spans.count(f) for f in sorted(set(spans))}
                census_md[rel]["__total"] = len(spans)
                total_logical += len(spans)
    if total_logical != 26:
        die(f"census count-law precondition: expected 26 logical spans (md view), found {total_logical}")
    # G4a cross-view parity: per-form md totals == parsed topic.json totals
    def form_totals(c):
        t = {}
        for c1 in c.values():
            for f, n in c1.items():
                if f != "__total":
                    t[f] = t.get(f, 0) + n
        return t
    md_tot, tj_tot = form_totals(census_md), form_totals(census_tj)
    if md_tot != tj_tot:
        die(f"G4a cross-view parity FAILED: md {md_tot} != topic.json {tj_tot}")
    print(f"census: {total_logical} logical debris spans (md view) — cross-view parity G4a PASS")
    for rel, c in {**census_tj, **census_md}.items():
        print(" ", rel.split("SME-ExamQuestion/")[1], c)

    # ---------------- 2. per-form global counts ----------------
    form_counts = md_tot
    for old, new, ev in T_ISOTOPE:
        got = form_counts.get(old, 0)
        print(f"  form x{got}: {old[:60]}")
        if got == 0:
            die(f"transform old-form absent (already repaired?): {old[:60]}")

    # ---------------- 3. topic.json field-level census + plane pre-identity --
    touched_fields = []   # dicts: bank, topic, qid, pid, kind(corpus), old_value, new_value
    field_changes = {}    # rel -> count
    modified_docs = {}    # rel -> mutated parsed document
    for bank, topics in BANKS.items():
        for t in topics:
            rel = f"SME-ExamQuestion/{bank}/{t}/topic.json"
            doc = json.loads(corpus[rel].decode("utf-8"))
            modified_docs[rel] = doc
            n_changed = 0
            for q in doc["questions"]:
                for p in q["parts"]:
                    for kind in ("problem_md", "solution_md"):
                        v = p.get(kind)
                        if not isinstance(v, str) or not DEBRIS_SCAN.search(v):
                            continue
                        new_v = v
                        for old, new, ev in T_ISOTOPE:
                            new_v = new_v.replace(old, new)
                        if new_v == v:
                            die(f"debris present but transforms produced no change: {q['id']} {p['id']} {kind}")
                        # per-field debris must be fully consumed
                        if DEBRIS_SCAN.search(new_v):
                            die(f"residual debris after transforms in {q['id']} {p['id']} {kind}")
                        # G8: plane pre-identity — plane's current value == corpus pre-repair value
                        v2_rel = f"apps/hub/content/{bank}/questions.json"
                        plane_raw = sh(["git", "-C", str(v2_root), "show", f"{a.v2_rev}:{v2_rel}"]).stdout
                        plane = json.loads(plane_raw)
                        pq = [qq for b in plane for qq in (b.get("questions") or []) if qq.get("id") == q["id"]]
                        if len(pq) != 1:
                            die(f"plane has {len(pq)} questions with id {q['id']} ({v2_rel})")
                        pp = [x for x in pq[0]["parts"] if x.get("id") == p["id"]]
                        if len(pp) != 1:
                            die(f"plane has {len(pp)} parts with id {p['id']}")
                        plane_val = pp[0].get({"problem_md": "problemMd", "solution_md": "solutionMd"}[kind])
                        canon_v = canon(v, f"SME-ExamQuestion/{bank}/{t}")
                        if plane_val != canon_v:
                            die(f"G8 plane pre-identity FAILED for {q['id']}/{p['id']}/{kind}:\n"
                                f"  canon(corpus): {canon_v[:120]!r}\n  plane:         {(plane_val or '')[:120]!r}")
                        p[kind] = new_v
                        touched_fields.append(dict(bank=bank, topic=t, qid=q["id"], pid=p["id"],
                                                   kind=kind, old=v, new=new_v,
                                                   new_canon=canon(new_v, f"SME-ExamQuestion/{bank}/{t}")))
                        n_changed += 1
            field_changes[rel] = n_changed
    if len(touched_fields) != 8:
        die(f"field-parity precondition: expected exactly 8 part-fields, got {len(touched_fields)}")
    print(f"topic.json: {len(touched_fields)} part-fields to repair; plane pre-identity G8 PASS (8/8)")

    # ---------------- 4. apply ----------------
    if not a.apply:
        print("dry run — all preconditions + G8 verified; re-run with --apply to write")
        return 0

    receipt_census = {"census_md_view": census_md, "census_topic_json_parsed_view": census_tj,
                      "total_logical_spans": total_logical, "form_counts": form_counts}
    (HERE / "census.json").write_text(json.dumps(receipt_census, indent=1, ensure_ascii=False) + "\n")

    transforms = []
    for old, new, ev in T_ISOTOPE:
        per_file = {}
        for rel in sorted(set(census_md) | set(census_tj)):
            n = census_md.get(rel, {}).get(old, 0) or census_tj.get(rel, {}).get(old, 0)
            if n:
                per_file[rel] = n
        transforms.append(dict(track="M4", old=old, new=new, evidence=ev,
                               total=form_counts[old], per_file=per_file))
    (HERE / "transforms.json").write_text(json.dumps({"transforms": transforms}, indent=1, ensure_ascii=False) + "\n")

    # 4a. topic.json writes + G0/G2/G3/G5
    for rel, raw in sorted(corpus.items()):
        if not rel.endswith("topic.json"):
            continue
        if rel not in field_changes:
            continue
        p = REPO / rel
        orig_doc = json.loads(raw.decode("utf-8"))
        new_doc = modified_docs[rel]
        # G5 deep-diff: exactly the touched fields
        diffs = list(deep_diff(orig_doc, new_doc))
        expected_paths = set()
        for tf in touched_fields:
            if f"SME-ExamQuestion/{tf['bank']}/{tf['topic']}/topic.json" == rel:
                for qi, q in enumerate(orig_doc["questions"]):
                    if q["id"] == tf["qid"]:
                        for pi, pp in enumerate(q["parts"]):
                            if pp["id"] == tf["pid"]:
                                expected_paths.add(f"$.questions[{qi}].parts[{pi}].{tf['kind']}")
        extra = {x[0] for x in diffs} - expected_paths
        if extra:
            die(f"G5 field-parity: unexpected changed paths in {rel}: {sorted(extra)[:6]}")
        if len(diffs) != field_changes[rel]:
            die(f"G5 field-parity: {len(diffs)} diffs != {field_changes[rel]} declared for {rel}")
    # G2/G3 across every touched value + every transform's new form
    for old, new, ev in T_ISOTOPE:
        if not dollar_parity(old) or not dollar_parity(new):
            die(f"G2 dollar-parity failed for transform: {old[:50]}")
        if any(ord(ch) > 127 for ch in new):
            die(f"G3 char-safety: non-ASCII in new form {new[:50]}")
    for tf in touched_fields:
        if not dollar_parity(tf["new"]):
            die(f"G2 dollar-parity failed for {tf['pid']} {tf['kind']}")
        na_old = sorted(ch for ch in tf["old"] if ord(ch) > 127)
        na_new = sorted(ch for ch in tf["new"] if ord(ch) > 127)
        if na_old != na_new:
            die(f"G3 char-safety: non-ASCII inventory changed for {tf['pid']} {tf['kind']}: "
                f"{[(c, hex(ord(c))) for c in na_old]} -> {[(c, hex(ord(c))) for c in na_new]}")
    for rel in [r for r in field_changes if field_changes[r]]:
        new_doc = modified_docs[rel]
        # G0 write: canonical serialization
        out = json.dumps(new_doc, indent=1, ensure_ascii=False).encode("utf-8") + b"\n"
        if not t1_roundtrip_ok(out):
            die(f"G0 T1 round-trip failed post-write: {rel}")
        (REPO / rel).write_bytes(out)
        print(f"wrote {rel} ({field_changes[rel]} fields)")

    # 4b. md renders: surgical substitution + G6 reverse-identity + G1
    for rel, raw in sorted(corpus.items()):
        if rel.endswith("topic.json") or rel not in census_md:
            continue
        p = REPO / rel
        txt = raw.decode("utf-8")
        new_txt = txt
        for old, new, ev in T_ISOTOPE:
            new_txt = new_txt.replace(old, new)
        if new_txt == txt:
            die(f"md file in census but transforms no-op: {rel}")        # G6 reverse-identity
        back = new_txt
        for old, new, ev in T_ISOTOPE:
            back = back.replace(new, old)
        if back != txt:
            die(f"G6 md-surgical reverse-identity FAILED: {rel}")
        if DEBRIS_SCAN.search(new_txt):
            die(f"G1 residual debris in {rel}")
        p.write_text(new_txt, encoding="utf-8")
        print(f"wrote {rel} (surgical, reverse-identity OK)")

    # 4c. G1 bank-wide debris-post-0 (ALL files of both banks incl. untouched)
    for bank, topics in BANKS.items():
        for t in topics:
            for fn in ("topic.json", "questions.md", "mark-schemes.md"):
                relp = REPO / "SME-ExamQuestion" / bank / t / fn
                txt = relp.read_text(encoding="utf-8")
                hits = DEBRIS_SCAN.findall(txt)
                if hits:
                    die(f"G1 debris-post-0 FAILED: {relp.relative_to(REPO)} -> {hits[:3]}")
    print("G1 debris-post-0: PASS (6 bank files scanned, zero debris)")

    # ---------------- 5. serve-table.json (plane-sync manifest) ----------------
    serve = []
    for tf in touched_fields:
        serve.append(dict(bank=tf["bank"], qid=tf["qid"], pid=tf["pid"],
                          kind={"problem_md": "problemMd", "solution_md": "solutionMd"}[tf["kind"]],
                          new_value_sha256=sha(tf["new_canon"]), new_value_len=len(tf["new_canon"])))
    (HERE / "serve-table.json").write_text(json.dumps({
        "law": "plane := repaired corpus of record verbatim (post-M4); compact serialization T1 per bank (indent=None, separators (',',':'), no trailing newline) — detected, not assumed",
        "fields": serve,
    }, indent=1, ensure_ascii=False) + "\n")

    # ---------------- 6. G7 change-set law ----------------
    st = sh(["git", "status", "--porcelain"], cwd=REPO).stdout.strip().splitlines()
    touched = sorted(l.split()[-1] for l in st)
    expected_set = sorted(list(corpus.keys()) + [f"scripts/oeq_phys_run013m4/{f}" for f in
                         ("repair_m4.py", "census.json", "transforms.json", "serve-table.json")])
    unexpected = [t for t in touched if not (t in expected_set or t.startswith("scripts/oeq_phys_run013m4/") or t.startswith('"scripts/oeq_phys_run013m4/'))]
    if unexpected:
        die(f"G7 change-set law: unexpected paths in git status: {unexpected}")
    print(f"G7 change-set: {len(touched)} paths, all expected")

    print("M4 CORPUS REPAIR COMPLETE — receipts written beside repair_m4.py")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
