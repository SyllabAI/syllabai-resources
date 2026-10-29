#!/usr/bin/env python3
"""F117 zero-network unit battery — the exponent-restore gate fix (Finding 8b at source).

Verifies the LAW and its DATA of record without emitting:
  1. The gate law: the converter source of record carries the case-robust
     F117 comparison (the v0.21.1 lowercase `== "4ch1"` regression is gone).
  2. The law is ALIVE in both casings: clean_lines restores flat standard-form
     exponents when ACTIVE_SPEC_CODE is "4CH1" (the run-time value main() sets)
     AND when it is "4ch1"; the physics lane ("4PH1") still refuses (the C74
     pin-of-record tranche stays flat).
  3. The 51 F111 class-2 guard pins recompute live against the corpus of
     record (the guards are not stale).
  4. The 11(d) re-point of record: the corpus solution_md and
     mark_points[0].text_md carry the converter-of-record form (the restored
     superscripts AND the printed notes tail "significant figures from 2")
     and the re-baselined C205/C207 shas recompute.
  5. Zero-mint blast radius: the corpus of record carries ZERO flat
     law-fireable exponent instances across all 54 slices — re-activating the
     law can only reproduce the of-record, never mint a new delta.

Zero network, zero emission; corpus read-only.
"""
import hashlib, json, re, sys
from pathlib import Path

RES = Path(__file__).resolve().parent.parent
CORP = RES / "Official-ExamQuestion" / "igcse-chemistry-19"
sys.path.insert(0, str(RES / "scripts"))
import official_examq_extract as X

fails = []


def check(name, ok, note=""):
    print(("PASS  " if ok else "FAIL  ") + name + (f" — {note}" if note else ""))
    if not ok:
        fails.append(name)


def canon(o):
    return json.dumps(o, sort_keys=True, ensure_ascii=False)


def sha_of(v, field):
    raw = (json.dumps(v, ensure_ascii=False, separators=(",", ":"))
           if field == "mark_points" else (v or "")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


# ---- 1. the gate law in the source of record --------------------------------
src = (RES / "scripts" / "official_examq_extract.py").read_text()
check("F117 gate: case-robust comparison present",
      re.search(r'\(ACTIVE_SPEC_CODE or ""\)\.lower\(\) == "4ch1"', src) is not None)
check("F117 gate: the dead lowercase equality is gone",
      re.search(r'if ACTIVE_SPEC_CODE == "4ch1":', src) is None)
mver = re.search(r'CONVERTER_VERSION = "(\d+)\.(\d+)\.(\d+)"', src)
ver = tuple(int(x) for x in mver.groups()) if mver else (0, 0, 0)
check("F117 version floor 0.32.0 (the gate fix ships at 0.32.0; F118 supersedes at 0.33.0)",
      ver >= (0, 32, 0), f"v{ver[0]}.{ver[1]}.{ver[2]}")

# ---- 2. the law is alive in both casings ------------------------------------
flat_line = "M1 8.46 × 10-3 mol of zinc"
saved = X.ACTIVE_SPEC_CODE
try:
    X.ACTIVE_SPEC_CODE = "4CH1"
    out = X.clean_lines(flat_line)[0]
    check("gate alive at '4CH1' (the run-time value)", "10⁻³" in out, out[:40])
    X.ACTIVE_SPEC_CODE = "4ch1"
    out = X.clean_lines(flat_line)[0]
    check("gate alive at '4ch1'", "10⁻³" in out)
    X.ACTIVE_SPEC_CODE = "4PH1"
    out = X.clean_lines(flat_line)[0]
    check("physics lane still refuses (C74 tranche)", "10-3" in out and "10⁻³" not in out)
finally:
    X.ACTIVE_SPEC_CODE = saved

# ---- 3. the 51 class-2 guard pins recompute ---------------------------------
C = json.loads((RES / "Official-ExamQuestion" / "CANARIES.json").read_text())
pins = [c for c in C["canaries"] if "exponent-guard" in c["id"]]
check("51 exponent pins present", len(pins) == 51, str(len(pins)))
bad = []
for p in pins:
    t = json.loads((CORP / p["series"] / f"4CH1-{p['paper']}" / "topic.json").read_text())
    got = [q for q in t["questions"] for part in q["parts"] if part["part_number"] == p["part"]]
    if not got:
        bad.append(p["id"] + " missing part")
        continue
    part = [pp for q in t["questions"] for pp in q["parts"] if pp["part_number"] == p["part"]][0]
    if sha_of(part.get(p["field"]), p["field"]) != p["sha256"]:
        bad.append(p["id"])
check("all 51 pins recompute live", not bad, ",".join(bad[:4]))

# ---- 4. the 11(d) re-point of record ----------------------------------------
t = json.loads((CORP / "2024-06" / "4CH1-1CR" / "topic.json").read_text())
part = [pp for q in t["questions"] for pp in q["parts"] if pp["part_number"] == "11(d)"][0]
smd, mps = part.get("solution_md") or "", part.get("mark_points") or []
check("11(d) keeps the restored superscripts", "10⁻²¹" in smd and "10²³" in smd)
check("11(d) serves the printed notes tail", "significant figures from\n2" in smd,
      "eyes-on MS p13: 'ALLOW any number of significant figures from 2'")
check("11(d) mark_points mirror solution_md",
      len(mps) == 1 and mps[0].get("text_md") == smd)
c205 = next(c for c in C["canaries"] if c["id"].startswith("C205-"))
c207 = next(c for c in C["canaries"] if c["id"].startswith("C207-"))
check("C205 re-baselined sha recomputes", sha_of(mps, "mark_points") == c205["sha256"])
check("C207 re-baselined sha recomputes", sha_of(smd, "solution_md") == c207["sha256"])

# ---- 5. zero-mint blast radius ----------------------------------------------
SUP_CHARS = "⁰¹²³⁴⁵⁶⁷⁸⁹⁻"
_RE = re.compile(r"×\s?10(-|−)?(\d{1,3})\b")
_SUP = str.maketrans("0123456789-−", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁻")


def restore(s):
    def _r(m):
        sign, d = m.group(1), m.group(2)
        if not (sign or (d[0] != "0" and (len(d) == 1 or 20 <= int(d) <= 29))):
            return m.group(0)
        return "× 10" + (sign or "").translate(_SUP) + d.translate(_SUP)
    return _RE.sub(_r, s)


def iter_strings(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, dict):
        for v in o.values():
            yield from iter_strings(v)
    elif isinstance(o, list):
        for v in o:
            yield from iter_strings(v)


mint = []
slices = sorted(p for p in CORP.iterdir() if p.is_dir() and len(p.name) == 7 and p.name[4] == "-")
n_slices = sum(1 for sl in slices for d in sl.iterdir() if d.is_dir() and d.name.startswith("4CH1-"))
for sl in slices:
    for f in sl.rglob("*"):
        if f.name not in ("topic.json", "questions.md"):
            continue
        strings = (list(iter_strings(json.loads(f.read_text())))
                   if f.suffix == ".json" else f.read_text().splitlines())
        for s in strings:
            if restore(s) != s:
                mint.append(f"{sl.name}/{f.name}")
check("zero flat law-fireable instances corpus-wide (zero-mint law)",
      not mint, "; ".join(mint[:4]))
check("54 slices across the 16 series scanned", len(slices) == 16 and n_slices == 54,
      f"{len(slices)} series / {n_slices} slices")

print()
if fails:
    print(f"F117 UNIT BATTERY: {len(fails)} FAIL")
    sys.exit(1)
print("F117 UNIT BATTERY: all checks PASS")
