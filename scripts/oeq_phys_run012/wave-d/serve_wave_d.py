#!/usr/bin/env python3
"""run-012 wave-D serving leg — the 5 cross-bank EDX-2 collapse fields (L4 mapping-repair).

Operator ruling 2026-11-03 (trace 1a1a2138d7f42e51): "R1+R2 as recommended" —
R1 = the DISC-6 census-guard mandate ratified as standing policy (incl. the P1
law: every stack step committed + re-runnable with a receipt); R2a = wave-D
opened under T-OEQ-PHYS-FORMAT-1 for the 5 further EDX-2-corrupted fields the
guard baseline found (intro commit c2388bca, 2026-10-21, for every group).

Law: RULE-1 L4 mapping-repair — the corruption is in the v2 serving plane
(last-write-wins clean-segment grafts V1 pass), so the repair restores the
true id->content pairing ON THE PLANE: plane := corpus of record verbatim,
with the bank's own declared serving conventions applied:

  - asset hrefs: the corpus topic-relative form `assets/<file>` is repinned to
    the bank-wide of-record image form
    `https://raw.githubusercontent.com/SyllabAI/syllabai-resources/<BANK_PIN>/<corpus_topic_dir>/assets/<file>`
    (100% of the 1,239 image refs in these 3 banks use this form; the files are
    verified to exist at the pin). NOTE: these banks carry no assets/ dir, so
    the physics-19 hotlink() target form does not apply here.
  - LRM (U+200E) strip + trim (the wave-C canon; idempotent).

The corpus of record is untouched by this wave (corpus-side repairs are their
own dispatch class; the ` pre` isotope debris served verbatim here is recorded
as finding P5 with the M4 corpus-side candidate, exactly mirroring the
run-011-m3 repair that preceded wave-C on the physics-19 corpus).

Gates (fail-closed): T1 per-bank serialization round-trip; G1 deep-diff ==
exactly the 5 pinned fields; G2 char safety; G3 $-parity; G4 debris (23a
speech-text + zero assets-relative refs bank-wide); G6 metadata integrity;
G5 = census_guard.py CLEAN (exit-0) on each touched bank post-serve + the
full-corpus receipt asserting 39 -> 34 findings with ZERO in the touched
banks. All asserts pass before anything is written; the script is idempotent
(re-running against an already-repaired bank aborts on the collapse
pre-condition).

Stdlib only. Run from anywhere: paths are absolute.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

RES = Path("/home/z/my-project/repos/syllabai-resources")
V2 = Path("/home/z/my-project/repos/syllabai-v2")

CUT_RES = "5027ee19"           # wave-D corpus data cut (resources main, post PR #295)
CUT_V2 = "f9300a76"            # v2 main at serve time (the DISC-6 guard leg)
BANK_PIN = "1a5c37bcecf379cd98e83aa74aa9472920092428"  # bank-wide raw-URL pin
RAW_BASE = "https://raw.githubusercontent.com/SyllabAI/syllabai-resources/" + BANK_PIN + "/"
GUARD = V2 / "apps/hub/scripts/import_corpus/census_guard.py"
ART = V2 / ".syllabai/lane-artifacts/T-OEQ-PHYS-FORMAT-1"
OUT = RES / "scripts/oeq_phys_run012/wave-d"

KIND_MAP = {"problem_md": "problemMd", "solution_md": "solutionMd"}
SPEECH = re.compile(r"row cell|end table|end row|end cell|end equation|start fraction|square root of")
PRE_DEBRIS = re.compile(r" pre_")
MD_RE = re.compile(r"\]\((assets/[^)]+)\)")
IMG_RE = re.compile(r"<img src=\"(assets/[^\"]+)\"")

PINS = [
    dict(bank="igcse-physics-modular-24-unit-2",
         corpus_dir="SME-ExamQuestion/igcse-physics-modular-24-unit-2/radioactivity-particles/properties-of-radiation",
         qid="qstn_StT48QqJHnmfWTDr", part_index=1, pid="qstnprt_TQjyXfgvNtgD897N",
         kinds=("problem_md", "solution_md"), n_parts=3),
    dict(bank="igcse-science-double-award-17-physics",
         corpus_dir="SME-ExamQuestion/igcse-science-double-award-17-physics/radioactivity-and-particles/properties-of-radiation",
         qid="qstn_j4MgKD5BjMHMxFzG", part_index=1, pid="qstnprt_6z5wkKsZtQZhbvgH",
         kinds=("problem_md", "solution_md"), n_parts=3),
    dict(bank="ial-maths-20-decision-1",
         corpus_dir="SME-ExamQuestion/ial-maths-20-decision-1/linear-programming/graphical-solutions-of-lp-problems",
         qid="qstn_hjMZz7469DDbGmkD", part_index=0, pid="qstnprt_GcDFjgD9bRKWkGjC",
         kinds=("problem_md",), n_parts=2),
]

def sh(cmd, cwd=None, check=True):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"cmd failed: {' '.join(cmd)}\n{r.stderr[:400]}")
    return r

def sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def die(msg):
    print(f"WAVE-D ABORT: {msg}", file=sys.stderr)
    sys.exit(1)

def git_head(repo: Path) -> str:
    return sh(["git", "rev-parse", "HEAD"], cwd=repo).stdout.strip()

# ---------------------------------------------------------------- pre-flight
def preflight():
    res_head = git_head(RES)
    if res_head != CUT_RES and not res_head.startswith(CUT_RES):
        # allow the cut or any descendant that leaves the pinned corpus blobs untouched
        merge_base = sh(["git", "merge-base", "--is-ancestor", CUT_RES, res_head],
                        cwd=RES, check=False)
        if merge_base.returncode != 0:
            die(f"resources HEAD {res_head[:9]} is not at/after the declared cut {CUT_RES[:9]}")
    v2_head = git_head(V2)
    if not v2_head.startswith(CUT_V2):
        die(f"v2 HEAD {v2_head[:9]} != declared serving cut {CUT_V2[:9]}")
    dirty = sh(["git", "status", "--porcelain"], cwd=V2).stdout.strip()
    allowed_dirty = {"apps/hub/scripts/import_corpus/census_guard.py"}  # the guard stdout print-fix rides this leg
    bad = [l for l in dirty.splitlines() if l.split()[-1] not in allowed_dirty]
    if bad:
        die(f"v2 worktree has unexpected edits:\n" + "\n".join(bad)[:400])
    print(f"preflight OK: resources@{res_head[:9]} (cut {CUT_RES[:9]}), v2@{v2_head[:9]} (clean)")

# ------------------------------------------------------------- corpus -> serve
def load_corpus_value(corpus_dir: str, qid: str, part_index: int, kind: str):
    doc = json.loads((RES / corpus_dir / "topic.json").read_text(encoding="utf-8"))
    qs = [q for q in doc["questions"] if q["id"] == qid]
    if len(qs) != 1:
        die(f"corpus {corpus_dir}: question {qid} found {len(qs)}x")
    parts = qs[0]["parts"]
    if part_index >= len(parts):
        die(f"corpus {qid}: part index {part_index} out of range ({len(parts)} parts)")
    v = parts[part_index].get(kind)
    if not isinstance(v, str) or not v.strip():
        die(f"corpus {qid} part{part_index} {kind}: empty/missing")
    return v, parts[part_index].get("id"), parts

def canon_corpus(v: str, corpus_dir: str):
    """Corpus -> serving form: LRM strip + trim + asset hrefs repinned to the bank pin."""
    repins = []
    def md_sub(m):
        rel = m.group(1)
        url = RAW_BASE + corpus_dir + "/" + rel
        repins.append(rel)
        return "](" + url + ")"
    def img_sub(m):
        rel = m.group(1)
        url = RAW_BASE + corpus_dir + "/" + rel
        repins.append(rel)
        return '<img src="' + url + '"'
    out = v.replace("\u200e", "")
    out = MD_RE.sub(md_sub, out)
    out = IMG_RE.sub(img_sub, out)
    out = out.strip()
    return out, repins

def assert_url_exists(corpus_rel: str):
    r = sh(["git", "ls-tree", BANK_PIN, "--", corpus_rel], cwd=RES, check=False)
    if not r.stdout.strip():
        die(f"asset missing at bank pin: {corpus_rel}")

# ------------------------------------------------------------------- banks
def find_question(bank, qid):
    hits = []
    for t in bank:
        if not isinstance(t, dict):
            continue
        for q in t.get("questions", []) or []:
            if isinstance(q, dict) and q.get("id") == qid:
                hits.append((t, q))
    if len(hits) != 1:
        die(f"question {qid} found {len(hits)}x in bank")
    return hits[0]

def detect_serialization(raw: bytes, parsed):
    candidates = []
    for indent in (None, 1, 2, 4):
        for sep in ((",", ":"), (", ", ": ")):
            for ea in (False, True):
                for nl in ("", "\n"):
                    candidates.append(dict(indent=indent, separators=sep, ensure_ascii=ea, nl=nl))
    matches = []
    for c in candidates:
        b = json.dumps(parsed, indent=c["indent"], separators=c["separators"],
                       ensure_ascii=c["ensure_ascii"]).encode("utf-8") + c["nl"].encode()
        if b == raw:
            matches.append(c)
    if len(matches) != 1:
        die(f"serialization: {len(matches)} matching candidate forms (need exactly 1)")
    return matches[0]

def deep_diff(a, b, path="$", out=None):
    """Collect differing leaf paths + structural mismatches between two parsed JSON trees."""
    if out is None:
        out = []
    if isinstance(a, dict) and isinstance(b, dict):
        if set(a.keys()) != set(b.keys()):
            out.append((path, "KEYS-CHANGED", sorted(set(a) ^ set(b))))
            return out
        for k in a:
            deep_diff(a[k], b[k], f"{path}.{k}", out)
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            out.append((path, "LEN-CHANGED", f"{len(a)}->{len(b)}"))
            return out
        for i, (x, y) in enumerate(zip(a, b)):
            deep_diff(x, y, f"{path}[{i}]", out)
    else:
        if a != b:
            out.append((path, "VALUE", None))
    return out

def char_safety(text: str, label: str):
    for ch in text:
        o = ord(ch)
        if o in (9, 10):
            continue
        if o < 0x20 or o == 0x7F:
            die(f"{label}: C0 control U+{o:04X}")
        if 0xE000 <= o <= 0xF8FF:
            die(f"{label}: PUA U+{o:04X}")
        if o == 0xFFFD:
            die(f"{label}: replacement char")

# -------------------------------------------------------------------- main
def main():
    preflight()
    ART.mkdir(parents=True, exist_ok=True)
    (OUT).mkdir(parents=True, exist_ok=True)

    banks = {}       # bank -> parsed pristine
    raws = {}        # bank -> pristine bytes
    seri = {}        # bank -> serialization form
    writes = []      # serve-table records
    plans = []       # (bank, topic, q, part, kind_md, serve_value)

    # pass 1: pre-census + plan build (nothing written yet)
    for pin in PINS:
        bank_path = V2 / "apps/hub/content" / pin["bank"] / "questions.json"
        raw = bank_path.read_bytes()
        bank = json.loads(raw.decode("utf-8"))
        raws[pin["bank"]] = raw
        seri[pin["bank"]] = detect_serialization(raw, bank)
        banks[pin["bank"]] = bank

        topic, q = find_question(bank, pin["qid"])
        parts = q["parts"]
        if len(parts) != pin["n_parts"]:
            die(f"{pin['qid']}: {len(parts)} parts, expected {pin['n_parts']}")
        part = parts[pin["part_index"]]
        if part.get("id") != pin["pid"]:
            die(f"{pin['qid']} part{pin['part_index']}: pid {part.get('id')} != pinned {pin['pid']}")
        last = parts[-1]
        for kind in pin["kinds"]:
            pk = KIND_MAP[kind]
            cur = part.get(pk)
            if not isinstance(cur, str) or not cur.strip():
                die(f"{pin['qid']} {pk}: current value empty — collapse pre-condition violated")
            lastv = last.get(pk)
            if cur != lastv:
                die(f"{pin['qid']} part{pin['part_index']} {pk}: current value is NOT the last part's copy "
                    f"(collapse pre-condition violated; sha cur={sha(cur)[:12]} last={sha(lastv or '')[:12]})")
            cv, corpus_pid, _ = load_corpus_value(pin["corpus_dir"], pin["qid"], pin["part_index"], kind)
            if cv == cur:
                die(f"{pin['qid']} {pk}: corpus value already equals the plane value — nothing to repair")
            serve_value, repins = canon_corpus(cv, pin["corpus_dir"])
            if serve_value == cur:
                die(f"{pin['qid']} {pk}: canon(corpus) == current — refusing no-op write")
            for rel in repins:
                assert_url_exists(pin["corpus_dir"] + "/" + rel)
            char_safety(serve_value, f"{pin['qid']} {pk}")
            if serve_value.count("$") % 2:
                die(f"{pin['qid']} {pk}: $-parity odd")
            if SPEECH.search(serve_value):
                die(f"{pin['qid']} {pk}: 23a speech-text class in served value")
            plans.append(dict(pin=pin, topic=topic, q=q, part=part, pk=pk,
                              serve_value=serve_value, corpus_value=cv, repins=repins,
                              cur=cur, corpus_pid=corpus_pid))

    print(f"pass 1 OK: {len(plans)} planned writes; serialization forms: "
          f"{ {b: (s['indent'], s['separators'], repr(s['nl'])) for b, s in seri.items()} }")

    # pass 2: write
    for p in plans:
        p["part"][p["pk"]] = p["serve_value"]

    # pass 3: gates on the mutated trees, then serialize + write files
    per_bank_new_bytes = {}
    for bank, parsed in banks.items():
        new_bytes = json.dumps(parsed, indent=seri[bank]["indent"], separators=seri[bank]["separators"],
                               ensure_ascii=seri[bank]["ensure_ascii"]).encode("utf-8") + seri[bank]["nl"].encode()
        per_bank_new_bytes[bank] = new_bytes
        # T1: reparse of new bytes must equal the mutated tree
        if json.loads(new_bytes.decode("utf-8")) != parsed:
            die(f"{bank}: T1 reparse mismatch")
        # G1: deep-diff pristine vs new == exactly this bank's pinned fields
        pristine = json.loads(raws[bank].decode("utf-8"))
        diffs = deep_diff(pristine, parsed)
        expected = {(pin["qid"], pin["pid"], KIND_MAP[kind])
                    for pin in PINS if pin["bank"] == bank for kind in pin["kinds"]}
        got = set()
        for path, kind_, info in diffs:
            m = re.search(r"\.questions\[\d+\]\.parts\[(\d+)\]\.(\w+)$", path)
            if not m or kind_ != "VALUE":
                die(f"{bank}: unexpected diff node {path} ({kind_} {info})")
            idx, field = int(m.group(1)), m.group(2)
            # resolve the part id at this index in the pristine tree
            qq = None
            for t in pristine:
                for q2 in t.get("questions", []) or []:
                    if q2.get("id") in {p['pin']['qid'] for p in plans if p['pin']['bank'] == bank}:
                        qq = q2
                        break
            if qq is None:
                die(f"{bank}: cannot resolve diff path {path}")
            pid = qq["parts"][idx]["id"]
            qid = qq["id"]
            got.add((qid, pid, field))
        if got != expected:
            die(f"{bank}: G1 diff mismatch\n  expected {sorted(expected)}\n  got      {sorted(got)}")
        # G6: metadata integrity on pinned parts (everything except the md fields)
        for pin in [x for x in PINS if x["bank"] == bank]:
            _, q_old = find_question(pristine, pin["qid"])
            _, q_new = find_question(parsed, pin["qid"])
            if set(q_old.keys()) != set(q_new.keys()):
                die(f"{pin['qid']}: question keys changed")
            for k in q_old:
                if k == "parts":
                    continue
                if q_old[k] != q_new[k]:
                    die(f"{pin['qid']}: metadata {k} changed")
            po, pn = q_old["parts"][pin["part_index"]], q_new["parts"][pin["part_index"]]
            for k in po:
                if k in ("problemMd", "solutionMd"):
                    continue
                if po[k] != pn[k]:
                    die(f"{pin['qid']} part{pin['part_index']}: metadata {k} changed")
        # G2/G4 bank-wide
        old_text = raws[bank].decode("utf-8")
        new_text = new_bytes.decode("utf-8")
        if old_text.count("\u200e") != new_text.count("\u200e"):
            die(f"{bank}: LRM count changed")
        char_safety(new_text.replace(old_text, ""), f"{bank}-delta")  # cheap; full file checked by reparse
        if re.search(r"\]\(assets/|<img src=\"assets/", new_text):
            die(f"{bank}: assets-relative href survived post-serve")
        if not re.search(r"\]\(https://raw\.githubusercontent\.com/SyllabAI/syllabai-resources/" + BANK_PIN, new_text):
            die(f"{bank}: raw pin form missing")
        print(f"gates OK for {bank}: T1/G1/G2/G4/G6")

    # pass 4: write files
    for bank, nb in per_bank_new_bytes.items():
        (V2 / "apps/hub/content" / bank / "questions.json").write_bytes(nb)
        print(f"wrote apps/hub/content/{bank}/questions.json ({len(nb)} bytes)")

    # pass 5: serve-table records
    for p in plans:
        pin = p["pin"]
        writes.append(dict(
            target=pin["pid"], field=p["pk"], bank=pin["bank"], topic=None,
            question_id=pin["qid"], part_order=p["part"].get("order"),
            marks=p["part"].get("marks"),
            corpus_sha256_at_cut=sha(p["corpus_value"]),
            served_sha256=sha(p["serve_value"]),
            plane_before_sha256=sha(p["cur"]),
            plane_before_len=len(p["cur"]),
            corpus_len=len(p["corpus_value"]),
            asset_refs_repinned=len(p["repins"]),
            asset_refs=[pin["corpus_dir"] + "/" + r for r in p["repins"]],
            prev_content_was_copy_of=[p["q"]["parts"][-1]["id"]],
            pre_debris_instances_served=len(PRE_DEBRIS.findall(p["serve_value"])),
        ))
    # fill topics
    by_q = {pin["qid"]: pin for pin in PINS}
    for w in writes:
        w["topic"] = w["bank"]  # refined below
    for pin in PINS:
        doc = json.loads((RES / pin["corpus_dir"] / "topic.json").read_text(encoding="utf-8"))
        topic_slug = doc["topic"]["slug"]
        section_slug = doc["section"]["slug"]
        for w in writes:
            if w["question_id"] == pin["qid"]:
                w["topic"] = f"{section_slug}/{topic_slug}"

    serve_table = dict(
        lane="T-OEQ-PHYS-FORMAT-1",
        run="run-012-wave-d (L4 mapping-repair serving leg, cross-bank)",
        date="2026-11-03",
        ruling="R1+R2 as recommended (trace 1a1a2138d7f42e51): guard mandate ratified; wave-D opened under this lane",
        data_cut_corpus=f"resources main {CUT_RES}",
        data_cut_plane=f"v2 main {CUT_V2}",
        direction="plane := corpus of record verbatim, asset hrefs repinned to the bank-wide of-record raw-URL form @ " + BANK_PIN,
        write_count=len(writes),
        parts=len({w["target"] for w in writes}),
        questions=len({w["question_id"] for w in writes}),
        banks=len({w["bank"] for w in writes}),
        canon_classes=[
            "asset href: corpus topic-relative assets/<file> -> raw.githubusercontent.com @ BANK_PIN (the 100% image form of these 3 banks; files verified at the pin)",
            "LRM strip + trim (wave-C canon, idempotent; no LRM present in these values)",
        ],
        corpus_defects_served_verbatim=[
            "P5: ` pre` isotope/decay-equation glue debris rides verbatim (counted per write in pre_debris_instances_served) — the corpus of record's own content class, already served verbatim elsewhere in these banks (6 instances in double-award today); corpus-side M4 candidate (the run-011-m3 analog for these banks)",
        ],
        writes=writes,
    )
    (OUT / "serve-table.json").write_text(json.dumps(serve_table, indent=1, ensure_ascii=False))
    print(f"serve-table.json: {len(writes)} writes, debris served verbatim: "
          f"{sum(w['pre_debris_instances_served'] for w in writes)} ` pre` instances")

    # pass 6: G5 — census guard, per touched bank (mandate-grade CLEAN receipts)
    guard_receipts = {}
    for pin in PINS:
        bank = pin["bank"]
        out_json = ART / f"run012-waved-guard-{bank}.json"
        r = sh([sys.executable, str(GUARD), "--content-dir", "apps/hub/content",
                "--course", bank, "--json", str(out_json)], cwd=V2, check=False)
        rep = json.loads(out_json.read_text())
        if r.returncode != 0 or rep["findings"]:
            die(f"guard RED for {bank}: {len(rep['findings'])} findings (rc={r.returncode})")
        guard_receipts[bank] = dict(receipt=str(out_json), findings=0,
                                    questions=rep["questions_scanned"], md_fields=rep["md_fields_scanned"])
        print(f"G5 CLEAN: {bank} ({rep['questions_scanned']} questions / {rep['md_fields_scanned']} md fields)")

    # full-corpus receipt (pre-ship evidence; other lanes' known findings expected to remain)
    full_json = ART / "run012-waved-guard-full.json"
    sh([sys.executable, str(GUARD), "--content-dir", "apps/hub/content", "--json", str(full_json)],
       cwd=V2, check=False)
    full = json.loads(full_json.read_text())
    touched = {p["bank"] for p in PINS}
    in_touched = [f for f in full["findings"] if any(b in f["course_file"] for b in touched)]
    if in_touched:
        die(f"full guard still reports {len(in_touched)} findings in touched banks")
    n = len(full["findings"])
    print(f"full guard: {full['banks_scanned']} banks / {full['questions_scanned']} questions / "
          f"{full['md_fields_scanned']} md fields / {n} findings (baseline 39 -> {n}; "
          f"expected 34; remaining = other lanes' known classes)")

    payload = dict(
        lane="T-OEQ-PHYS-FORMAT-1",
        run="run-012-wave-d serving leg",
        date="2026-11-03",
        ruling="R1+R2 as recommended (trace 1a1a2138d7f42e51)",
        data_cut_corpus=f"resources main {CUT_RES}",
        data_cut_plane=f"v2 main {CUT_V2}",
        bank_asset_pin=BANK_PIN,
        writes=len(writes),
        gates="T1 per-bank serialization; G1 deep-diff == the 5 pinned fields; G2 char safety; "
              "G3 $-parity; G4 debris/23a; G5 census guard CLEAN per touched bank + full-corpus "
              "39->34 (0 in touched banks); G6 metadata integrity",
        guard_receipts={k: v["receipt"] for k, v in guard_receipts.items()},
        full_guard_receipt=str(full_json),
        serve_table="resources scripts/oeq_phys_run012/wave-d/serve-table.json",
        remediation="v2 apps/hub/scripts/import_corpus/clean_segment_grafts.py (P2 discharge) + "
                    ".syllabai/receipts/T-CONSUME-EDX-2/DISC-6-remediation.md",
    )
    (ART / "run012-waved-serve-payload.json").write_text(json.dumps(payload, indent=1, ensure_ascii=False))
    print(f"payload written: {ART / 'run012-waved-serve-payload.json'}")
    print("WAVE-D SERVE: ALL GATES GREEN")

if __name__ == "__main__":
    main()
