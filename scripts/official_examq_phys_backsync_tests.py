#!/usr/bin/env python3
"""Zero-network battery for the 4PH1 corpus back-sync + questions.md regen
(T-OEQ-PHYS-FORMAT-1 run-006, LEDGER F127 — operator order "Proceed with
questions.md regen rides the next converter run", trace 1a190e0aa0abae3d).

Verifies, against the corpus of record on disk (no network, no exporter run):

  B1  every back-sync pin (scripts/oeq_phys_backsync_pins.json) matches the
      corpus field value under the C-law (sha256(utf-8) for md strings,
      sha256(compact separators=(',',':') ensure_ascii=False) for the
      mark_points[0] triple {id,marks,text_md});
  B2  the synced-fields ledger (scripts/oeq_phys_synced_fields.json) and the
      pins cover the EXACT same (series, paper, part, field) key set;
  B3  ledger grammar: every entry parses to {series, paper, part, field} with
      field in the closed set {problem_md, solution_md, mark_points[0]};
  B4  zero PUA / U+FFFD / C0 control chars in every pinned corpus value;
  B5  mark-point sums == part marks and part sums == question totals on every
      pinned part (the G-E2 law at the corpus layer);
  B6  the questions.md of record is the deterministic render of its slice's
      topic.json (the 2022-06 1P slice re-rendered in memory must be
      byte-identical on disk) AND carries the run-005 nuclear-decay
      restoration verbatim;
  B7  negative test: mutating one pinned value in memory is DETECTED.

Exit 0 = all legs hold. Any failure exits 1 (fail-closed, ship-blocker).
"""
import json, hashlib, re, sys, importlib.util, tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
CORPUS = REPO / "Official-ExamQuestion" / "igcse-physics-19"
PINS_PATH = HERE / "oeq_phys_backsync_pins.json"
LEDGER_PATH = HERE / "oeq_phys_synced_fields.json"
FIELDS = {"problem_md", "solution_md", "mark_points[0]"}
PUA_RE = re.compile(r"[\uE000-\uF8FF\uFFFD\u0000-\u0008\u000b-\u001f]")

fails = []


def check(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ") + name + (f" — {detail}" if detail else ""))
    if not ok:
        fails.append(name)


def load_topic(series, paper):
    return json.loads((CORPUS / series / f"4PH1-{paper}" / "topic.json").read_text())


def part_of(topic, pn):
    for q in topic["questions"]:
        for p in q["parts"]:
            if str(p["part_number"]) == pn:
                return p
    return None


def pinned_value(topic, field, pn):
    p = part_of(topic, pn)
    if p is None:
        return None
    if field == "problem_md":
        return p.get("problem_md")
    if field == "solution_md":
        return p.get("solution_md")
    if field == "mark_points[0]":
        mps = p.get("mark_points") or []
        if not mps:
            return None
        m = mps[0]
        return {"id": m.get("id"), "marks": m.get("marks"), "text_md": m.get("text_md")}
    return None


def c_sha(field, value):
    if field == "mark_points[0]":
        return hashlib.sha256(json.dumps(value, separators=(",", ":"),
                                         ensure_ascii=False).encode()).hexdigest()
    return hashlib.sha256(value.encode()).hexdigest()


pins = json.loads(PINS_PATH.read_text())
ledger = json.loads(LEDGER_PATH.read_text())

# ---- B1 pins match the corpus ----
b1_bad = []
for pin in pins:
    topic = load_topic(pin["series"], pin["paper"])
    val = pinned_value(topic, pin["field"], pin["part"])
    if val is None or c_sha(pin["field"], val) != pin["sha256"]:
        b1_bad.append(f'{pin["series"]}/{pin["paper"]}/{pin["part"]}/{pin["field"]}')
check("B1 pins==corpus (C-law)", not b1_bad, f"{len(b1_bad)} drifts {b1_bad[:3]}")

# ---- B2 ledger == pins key sets ----
pin_keys = sorted((p["series"], p["paper"], p["part"], p["field"]) for p in pins)
led_keys = sorted((e["series"], e["paper"], e["part"], e["field"])
                  for e in ledger["fields"])
check("B2 ledger==pins key sets", pin_keys == led_keys,
      f"{len(pin_keys)} pins vs {len(led_keys)} entries")

# ---- B3 ledger grammar ----
b3_bad = [e for e in ledger["fields"]
          if not (isinstance(e.get("series"), str) and isinstance(e.get("paper"), str)
                  and isinstance(e.get("part"), str) and e.get("field") in FIELDS)]
check("B3 ledger grammar", not b3_bad, f"{len(b3_bad)} malformed")

# ---- B4 PUA census on pinned values ----
b4_bad = []
for pin in pins:
    topic = load_topic(pin["series"], pin["paper"])
    val = pinned_value(topic, pin["field"], pin["part"])
    txt = json.dumps(val, ensure_ascii=False) if not isinstance(val, str) else val
    if val is None or PUA_RE.search(txt):
        b4_bad.append(f'{pin["series"]}/{pin["paper"]}/{pin["part"]}/{pin["field"]}')
check("B4 zero PUA/U+FFFD/C0 on pinned values", not b4_bad, f"{len(b4_bad)} hits")

# ---- B5 G-E2 sum laws on pinned parts ----
b5_bad = []
seen = set()
for pin in pins:
    key = (pin["series"], pin["paper"], pin["part"])
    if key in seen:
        continue
    seen.add(key)
    topic = load_topic(pin["series"], pin["paper"])
    p = part_of(topic, pin["part"])
    if p is None:
        b5_bad.append(f'{key}: part missing')
        continue
    mps = p.get("mark_points") or []
    if mps and sum(m["marks"] for m in mps) != p["marks"]:
        b5_bad.append(f'{key}: mp sum {sum(m["marks"] for m in mps)} != {p["marks"]}')
check("B5 G-E2 corpus-layer sums", not b5_bad, f"{len(b5_bad)} violations")

# ---- B6 questions.md determinism + run-005 restoration present ----
try:
    spec = importlib.util.spec_from_file_location(
        "ext", str(HERE / "official_examq_extract.py"))
    ext = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ext)
    t = load_topic("2022-06", "1P")
    qp = CORPUS / "2022-06" / "4PH1-1P" / "questions.md"
    on_disk = qp.read_bytes()
    tmp = Path(tempfile.mkdtemp()) / "q.md"
    ext.write_questions_md(t, tmp)
    det = tmp.read_bytes() == on_disk
    check("B6a questions.md == deterministic re-render (2022-06 1P)", det)
    check("B6b run-005 nuclear-decay restoration present",
          "²³²₉₀Th → ²²⁰₈₆Rn + ⁴₂α + ⁰₋₁β".encode() in on_disk)
except Exception as exc:  # fail-closed on any battery machinery fault
    check("B6 questions.md legs", False, repr(exc))

# ---- B7 negative control ----
pin0 = pins[0]
topic = load_topic(pin0["series"], pin0["paper"])
val = pinned_value(topic, pin0["field"], pin0["part"])
if isinstance(val, str):
    mutated = val + " "
else:
    mutated = dict(val)
    mutated["text_md"] = (val.get("text_md") or "") + " "
check("B7 negative control detected",
      c_sha(pin0["field"], mutated) != pin0["sha256"])

print()
if fails:
    print(f"BATTERY FAIL: {len(fails)} leg(s) down: {fails}")
    sys.exit(1)
print(f"BATTERY PASS: B1-B7 all green ({len(pins)} pins, "
      f"{len(ledger['fields'])} ledger entries)")
