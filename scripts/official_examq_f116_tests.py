#!/usr/bin/env python3
"""F116 zero-network unit battery — the remaining F111 census classes.

Verifies the LAWS and their DATA of record without emitting:
  1. The F47 ledger==corpus law: the 2023-06/2CR/7(c)(i) entry carries
     transcription_of_record byte-equal to the corpus of record's
     solution_md AND mark_points[0].text_md.
  2. The F94 share_with law: every STEM-RESTORE share_with asset dict is
     byte-equal (canon) to the corpus of record's sibling assets entry, and
     its ref_part resolves (owner asset id, or a part number in the same
     question carrying the owner's path).
  3. The 70 F111 guard pins: every part_field_sha pin recomputes to the
     corpus of record value (the guards are live, not stale).
  4. The class-5/6/7 sync of record: the synced corpus fields equal the
     converter-of-record forms (metadata drops, the native 7(c)(i) edits[]
     entry, the curated mention, the 0.305 text_coverage).
  5. The converter source of record carries the three F116 law blocks.
Zero network, zero emission; corpus read-only.
"""
import hashlib, json, re, subprocess, sys
from pathlib import Path

RES = Path(__file__).resolve().parent.parent
CORP = RES / "Official-ExamQuestion" / "igcse-chemistry-19"
GEN = re.compile(r"v0\.\d+\.\d+")
fails = []


def check(name, ok, note=""):
    print(("PASS  " if ok else "FAIL  ") + name + (f" — {note}" if note else ""))
    if not ok:
        fails.append(name)


def canon(o):
    return json.dumps(o, sort_keys=True, ensure_ascii=False)


def sha_of(v, field):
    raw = (json.dumps(v, ensure_ascii=False, separators=(",", ":"))
           if field == "mark_points" else (v or ""))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def head_json(rel):
    r = subprocess.run(["git", "show", f"HEAD:{rel}"], cwd=RES, capture_output=True)
    assert r.returncode == 0, rel
    return json.loads(r.stdout)


def corpus_part(series, paper, pn, from_head=False):
    rel = f"Official-ExamQuestion/igcse-chemistry-19/{series}/4CH1-{paper}/topic.json"
    t = head_json(rel) if from_head else json.loads((CORP / series / f"4CH1-{paper}" / "topic.json").read_bytes())
    for q in t["questions"]:
        for p in q["parts"]:
            if p["part_number"] == pn:
                return p
    raise AssertionError((series, paper, pn))


# ---- 1. the F47 ledger==corpus law ------------------------------------------
mo = json.loads((RES / "Official-ExamQuestion" / "MS-LINK-OVERRIDES.json").read_text())
entry = next(e for e in mo["entries"]
             if (e.get("series"), e.get("paper"), e.get("part")) == ("2023-06", "2CR", "7(c)(i)"))
tor = entry.get("transcription_of_record")
p = corpus_part("2023-06", "2CR", "7(c)(i)")
check("F47 transcription_of_record present", isinstance(tor, str) and len(tor) == 389)
check("F47 tor == corpus solution_md", tor == p["solution_md"])
check("F47 tor == corpus mark_points[0].text_md", tor == p["mark_points"][0]["text_md"])
check("F47 tor == '\\n'.join(ms_lines[0:7]) + prose",
      tor.startswith("\n".join(entry["ms_lines"][:7]) + "\n\n"))
check("F47 evidence carries the F116 law note", "transcription_of_record" in entry["evidence"])

# ---- 2. the F94 share_with law ----------------------------------------------
sr = json.loads((RES / "Official-ExamQuestion" / "STEM-RESTORE.json").read_text())
SHARES = [
    ("2021-11/4CH1-1C:Q1", "asset_1_a_i_particles", "2021-11", "1C",
     [("1(a)(ii)", "asset_1_a_ii_particles"), ("1(a)(iii)", "asset_1_a_iii_particles")]),
    ("2020-11/4CH1-2CR:Q1", "asset_1_stem_apparatus", "2020-11", "2CR",
     [("1(b)", "asset_1_b_apparatus")]),
]
for key, owner_id, series, paper, sibs in SHARES:
    v = sr["verdicts"][key]
    sf = next(s for s in v["stemFigures"] if s["id"] == owner_id)
    sw = sf.get("share_with") or []
    check(f"F94 share_with {key}: {len(sibs)} items", len(sw) == len(sibs))
    for (pn, aid), item in zip(sibs, sw):
        ok_struct = item.get("part") == pn and item.get("asset", {}).get("id") == aid
        check(f"F94 share_with {key} -> {pn} structure", ok_struct)
        cp = corpus_part(series, paper, pn)
        ca = next((a for a in cp.get("assets") or [] if a["id"] == aid), None)
        check(f"F94 share_with {key} -> {pn} == corpus of record",
              ca is not None and canon(ca) == canon(item["asset"]))
        # ref_part resolves: asset id form, or a part number carrying the owner path
        ref = item["asset"].get("ref_part")
        resolved = (ref == owner_id) or any(
            pp["part_number"] == ref
            for qq in (CORP / series / f"4CH1-{paper}" / "topic.json").is_file() and
            [json.loads((CORP / series / f"4CH1-{paper}" / "topic.json").read_bytes())]
            for pp in qq["questions"][0]["parts"]
            for a in (pp.get("assets") or []) if a.get("path") == item["asset"].get("path"))
        check(f"F94 share_with {key} -> {pn} ref_part resolves", bool(resolved))

# ---- 3. the 70 guard pins are live ------------------------------------------
cans = json.loads((RES / "Official-ExamQuestion" / "CANARIES.json").read_text())
pins = [c for c in cans["canaries"] if c.get("check") == "part_field_sha"
        and c["id"].startswith(("C147", "C148", "C149")) or
        ("-f111-strip-guard-" in c["id"] or "-f111-exponent-guard-" in c["id"])]
check("70 F111 guard pins present", len(pins) == 70, f"found {len(pins)}")
drift = []
for cpin in pins:
    part = corpus_part(cpin["series"], cpin["paper"], cpin["part"])
    h = sha_of(part.get(cpin["field"]), cpin["field"])
    if h != cpin["sha256"]:
        drift.append(cpin["id"])
check("all 70 pins recompute to the corpus of record", not drift, str(drift[:4]))

# ---- 4. the class-5/6/7 sync of record --------------------------------------
check("sync: 1(a)(i) mention == curated text",
      corpus_part("2021-11", "1C", "1(a)(i)")["assets"][0]["mention"].startswith("F94 option-drawing follow-up"))
check("sync: 6(d)(ii) text_coverage == 0.305",
      corpus_part("2020-01", "2C", "6(d)(ii)")["assets"][0]["text_coverage"] == 0.305)
for series, paper, pn in [("2021-11", "2C", "1(d)"), ("2025-06", "2C", "5(c)(i)"), ("2022-06", "2C", "6(a)")]:
    cp = corpus_part(series, paper, pn)
    check(f"sync: {series} {paper} {pn} stale surgical metadata dropped",
          cp.get("edit_status") == "extracted" and "edits" not in cp)
check("sync: 6(a) value_trace.text dropped",
      "text" not in corpus_part("2022-06", "2C", "6(a)")["value_trace"])
p7 = corpus_part("2023-06", "2CR", "7(c)(i)")
check("sync: 7(c)(i) edits[] == native F47 replay entry",
      len(p7["edits"]) == 1 and GEN.sub("vX", p7["edits"][0]["tool"]) ==
      "official_examq_extract.py vX (F47 ledger application — replay of the F107 adjudication of record)")
check("sync: 7(c)(i) edit_status corrected + value_trace.solution provenance",
      p7["edit_status"] == "corrected" and
      p7["value_trace"]["solution"] == "ms-image-eyeball-transcription (F47 ledger 2023-06/2CR/7(c)(i))")

# ---- 5. the converter source carries the F116 law blocks ---------------------
src = (RES / "scripts" / "official_examq_extract.py").read_text()
check("converter: F47 verbatim law present", "transcription_of_record" in src and "_f47_transcription" in src)
check("converter: F94 share_with replay present", "share_with" in src and "_share_consumed" in src)
check("converter: version 0.31.0", 'CONVERTER_VERSION = "0.31.0"' in src)

# disclosure of record present and census-shaped
disc = json.loads((RES / "scripts" / "exporter-disclosures" /
                   "2026-10-29-f116-f111-remaining-classes.json").read_text())
check("disclosure of record: 1 served delta (the 1(a)(i) caption)",
      disc == {"new": {}, "gone": {},
               "changed": {"official-4ch1-1c-2021-11": ["offp_2021-11_1c_1-a-i"]}})

print()
if fails:
    print(f"F116 UNIT BATTERY VIOLATED: {len(fails)} -> {fails}")
    sys.exit(1)
print("F116 unit battery: all checks hold.")
