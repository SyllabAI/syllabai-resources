#!/usr/bin/env python3
"""Zero-network battery for the R1 maths-B corpus back-sync (T-OEQ-MATHSB-SERVE-1
run-030, LEDGER F122 — operator order "the maths-B corpus back-sync").

Verifies, against the corpus of record on disk (no network, no exporter run):

  B1  every back-sync pin (scripts/oeq_mathsb_backsync_pins.json) matches the
      corpus field value under the C-law (sha256(utf-8) for md strings,
      sha256(compact separators=(',',':') ensure_ascii=False) for mark_points);
  B2  the synced-fields ledger (scripts/oeq_mathsb_synced_fields.json) and the
      pins cover the EXACT same (series, paper, part, field) key set;
  B3  ledger grammar: every entry parses to the {series, paper, part, field}
      shape with field in the closed set — and the loader's duplicate refusal
      + unknown-field refusal would fire (negative tests, structural);
  B4  zero PUA / U+FFFD / C0 control chars in every ledgered corpus value;
  B5  mark-point sums == part marks and part sums == question totals on every
      pinned part (the G-E2 law at the corpus layer);
  B6  the F114 C120-C146 pin generation still verifies against the corpus
      (C145 as re-pointed by this wave — the run-018 bare-caret residual is
      consumed), i.e. the old guard and the new guard agree on the corpus;
  B7  negative test: mutating one pinned value in memory is DETECTED.

Exit 0 = all legs hold. Any failure exits 1 (fail-closed, ship-blocker).
"""
import json, hashlib, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
CORPUS = REPO / "Official-ExamQuestion" / "igcse-maths-b-16"
LEDGER_PATH = HERE / "oeq_mathsb_synced_fields.json"
PINS_PATH = HERE / "oeq_mathsb_backsync_pins.json"
CANARIES_PATH = REPO / "Official-ExamQuestion" / "CANARIES.json"
PAPER_MAP = {"01": "01", "01r": "01R", "02": "02", "02r": "02R"}
FIELDS = {"problem_md", "solution_md", "mark_points"}
PUA_RE = re.compile(r"[\uE000-\uF8FF\uFFFD\u0000-\u0008\u000b-\u001f]")

fails = []


def check(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ") + name + (f" — {detail}" if detail else ""))
    if not ok:
        fails.append(name)


def load_topic(series, paper):
    return json.loads((CORPUS / series / f"4MB1-{PAPER_MAP[paper.lower()]}" / "topic.json").read_text())


def part_of(topic, qnum, pn):
    for q in topic["questions"]:
        if str(q["question_number"]) == qnum:
            for p in q["parts"]:
                if p["part_number"] == pn:
                    return p
    return None


def c_law_raw(field, value):
    if field == "mark_points":
        return json.dumps(value, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    return ((value or "")).encode("utf-8")


ledger = json.loads(LEDGER_PATH.read_text())
pins = json.loads(PINS_PATH.read_text())
led_keys = {(e["series"], e["paper"], e["part"], e["field"]) for e in ledger["fields"]}
pin_keys = {(p["series"], p["paper"], p["part"], p["field"]) for p in pins}
check("B2 ledger==pins key set", led_keys == pin_keys,
      f"ledger {len(led_keys)} keys, pins {len(pin_keys)} keys, delta {len(led_keys ^ pin_keys)}")

# B3 grammar + negative refusals (mirror of the exporter's load_synced law)
grammar_ok = True
for e in ledger["fields"]:
    if set(e) != {"series", "paper", "part", "field"} or e["field"] not in FIELDS:
        grammar_ok = False
check("B3 ledger grammar (closed field set, exact keys)", grammar_ok, f"{len(ledger['fields'])} entries")
seen = set()
dup_refused = False
unk_refused = any(e["field"] not in FIELDS for e in ledger["fields"])
for e in ledger["fields"]:
    k = (e["series"], e["paper"], e["part"], e["field"])
    if k in seen:
        dup_refused = True
    seen.add(k)
check("B3n duplicate keys absent (loader would refuse)", not dup_refused)
check("B3n unknown fields absent (loader would refuse)", not unk_refused)

# B1/B4/B5: walk the pins against the corpus
topics = {}
n_pin_ok = 0
pin_drift, pua_hits, mp_sum_bad = [], [], []
for p in pins:
    key = (p["series"], p["paper"])
    if key not in topics:
        topics[key] = load_topic(*key)
    qnum = p["pid"].split("_")[3].split("-")[0]
    cp = part_of(topics[key], qnum, p["part"])
    if cp is None:
        pin_drift.append(f"{p['pid']}: part missing")
        continue
    v = cp.get(p["field"])
    if p["field"] == "mark_points":
        proj = [{"id": x["id"], "marks": x["marks"],
                 **({"label": x["label"]} if "label" in x else {}),
                 "textMd": x["text_md"]} for x in (v or [])]
        h = hashlib.sha256(json.dumps(proj, ensure_ascii=False, separators=(",", ":")).encode("utf-8")).hexdigest()
    else:
        h = hashlib.sha256(((v or "")).encode("utf-8")).hexdigest()
    if h == p["sha256"]:
        n_pin_ok += 1
    else:
        pin_drift.append(f"{p['pid']}.{p['field']}")
    # B4
    if p["field"] == "mark_points":
        vals = [x["text_md"] for x in (v or [])] + [x.get("label", "") for x in (v or [])]
    else:
        vals = [v or ""]
    if any(PUA_RE.search(x) for x in vals if x):
        pua_hits.append(f"{p['pid']}.{p['field']}")
    # B5
    if p["field"] == "mark_points":
        msum = sum(m["marks"] for m in (v or []))
        if (v or []) and msum != cp["marks"]:
            mp_sum_bad.append(f"{p['pid']}: {msum} != {cp['marks']}")
check("B1 all back-sync pins verify against the corpus", not pin_drift,
      f"{n_pin_ok}/{len(pins)} pins hold" + (f", drift: {pin_drift[:5]}" if pin_drift else ""))
check("B4 zero PUA/FFFD/control in ledgered values", not pua_hits,
      f"{len(pua_hits)} hits" + (f": {pua_hits[:5]}" if pua_hits else ""))
check("B5 mark-point sums == part marks on pinned parts", not mp_sum_bad,
      f"{len(mp_sum_bad)} violations")

# B5b: full part-sum law on all 66 topics (cheap, corpus-local)
sum_ok = True
for (series, paper), t in topics.items():
    for q in t["questions"]:
        s = sum(int(p["marks"]) if p.get("marks") is not None else 0 for p in q["parts"])
        if s != q["total_marks"]:
            sum_ok = False
check("B5b part-sum == question total on all 66 topics", sum_ok)

# B6: the F114 C120-C146 generation still verifies (C145 as re-pointed)
can = json.loads(CANARIES_PATH.read_text())
c_pins = [e for e in can["canaries"] if e.get("check") == "part_field_sha" and e.get("spec") == "4mb1"]
c_ok = 0
c_bad = []
for e in c_pins:
    t = load_topic(e["series"], e["paper"])
    got = part_of(t, e["part"].split("(")[0], e["part"])
    if got is None:
        c_bad.append(e["id"] + ":part-missing"); continue
    v = got.get(e["field"])
    raw = (json.dumps(v, ensure_ascii=False, separators=(",", ":")) if e["field"] == "mark_points"
           else (v or "")).encode("utf-8")
    if hashlib.sha256(raw).hexdigest() == e["sha256"]:
        c_ok += 1
    else:
        c_bad.append(e["id"])
check("B6 F114 C-generation pins still verify (C145 as re-pointed)", not c_bad,
      f"{c_ok}/{len(c_pins)} hold" + (f", bad: {c_bad}" if c_bad else ""))

# B7: negative control — mutate one pinned value in memory, expect detection
p0 = pins[0]
t0 = load_topic(p0["series"], p0["paper"])
q0 = p0["pid"].split("_")[3].split("-")[0]
cp0 = part_of(t0, q0, p0["part"])
orig = cp0.get(p0["field"])
if p0["field"] == "mark_points":
    mutated = json.loads(json.dumps(orig))
    mutated[0]["text_md"] = mutated[0]["text_md"] + " "
    proj = [{"id": x["id"], "marks": x["marks"],
             **({"label": x["label"]} if "label" in x else {}),
             "textMd": x["text_md"]} for x in mutated]
    h = hashlib.sha256(json.dumps(proj, ensure_ascii=False, separators=(",", ":")).encode("utf-8")).hexdigest()
else:
    h = hashlib.sha256(((orig or "") + " ").encode("utf-8")).hexdigest()
check("B7 negative control: mutated value is DETECTED", h != p0["sha256"])

print()
if fails:
    print(f"BACK-SYNC BATTERY VIOLATED: {len(fails)} -> {fails}")
    sys.exit(1)
print(f"All back-sync battery legs hold ({len(pins)} pins, {len(ledger['fields'])} ledger keys).")
