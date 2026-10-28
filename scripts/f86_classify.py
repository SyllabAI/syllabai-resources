#!/usr/bin/env python3
"""F86 re-receipt — final delta classification: map every part-level delta
to its mechanism class (exponent-restore / drawing-strip remains / F90
not-yet-landed / furniture residue / image-answer curated form / other)."""
import json, re, subprocess
from pathlib import Path

RES = Path("/home/z/my-project/g9fix/repo")
SUP = "⁻⁰¹²³⁴⁵⁶⁷⁸⁹"
GEN = re.compile(r"v0\.\d+\.\d+")

def load(series, paper):
    rel = f"Official-ExamQuestion/igcse-chemistry-19/{series}/{paper}/topic.json"
    o = json.loads(subprocess.run(["git", "show", f"HEAD:{rel}"], cwd=RES, capture_output=True).stdout)
    n = json.loads((RES / rel).read_bytes())
    def prep(t):
        t.pop("generated_utc", None)
        if isinstance(t.get("generator"), str):
            t["generator"] = GEN.sub("vX", t["generator"])
        for q in t.get("questions", []):
            for p in q.get("parts", []):
                for e in p.get("edits") or []:
                    if isinstance(e, dict) and isinstance(e.get("tool"), str):
                        e["tool"] = GEN.sub("vX", e["tool"])
        return t
    return prep(o), prep(n)

def flat(t):
    m = {}
    for qi, q in enumerate(t["questions"]):
        for p in q["parts"]:
            m[(qi, p["part_number"])] = p
    return m

def classify(old, new):
    """Return (class, evidence) for a text pair."""
    sup_old = sum(1 for ch in old if ch in SUP)
    sup_new = sum(1 for ch in new if ch in SUP)
    has_sup = sup_old > 0 and sup_new == 0 and old.replace("\u2062", "") != new
    if has_sup and re.sub(r"[\d\s]", "", old.translate(str.maketrans("", "", SUP)))[:60] in \
            re.sub(r"[\d\s]", "", new)[:200] or (sup_old and not sup_new):
        return "exponent-restore(Finding-8b)", f"sup {sup_old}->{sup_new}"
    # drawing remains: new has runs of single letters/digits separated by spaces
    soup_new = len(re.findall(r"(?:^|\s)[A-ZbnlCc\-]{1,2}(?=\s|$)", new))
    soup_old = len(re.findall(r"(?:^|\s)[A-ZbnlCc\-]{1,2}(?=\s|$)", old))
    if len(new) > len(old) and soup_new - soup_old >= 3:
        return "drawing-strip-remains(Task-20/propene)", f"soup {soup_old}->{soup_new}"
    if new.rstrip() in old:
        return "of-record-longer(curated/stripped)", "new is substring of old"
    if old.rstrip() in new:
        return "fresh-longer(added-content)", "old is substring of new"
    return "other", ""

census = json.load(open("/tmp/f86-census.json"))
# fail-closed: the classification is only meaningful against the fresh
# emission tree — a clean worktree would silently classify nothing (the
# receipt builder must never consume a self-diff)
dirty = subprocess.run(["git", "status", "--porcelain", "--",
                        "Official-ExamQuestion/igcse-chemistry-19"],
                       cwd=RES, capture_output=True, text=True).stdout.strip()
if not dirty:
    sys.exit("F86 classifier: the corpus worktree is CLEAN — no fresh emission "
             "to classify against HEAD. Re-run the re-emission first (fail-closed).")
buckets = {}
others = []
for ent in census["slices"]:
    series, paper = ent["series"], ent["paper"]
    if ent["verdict"] == "clean":
        continue
    o, n = load(series, paper)
    fo, fn = flat(o), flat(n)
    for d in ent["part_diffs"]:
        qi, pn, field = d["q"], d["part"], d["field"]
        if field in ("<part>", "assets", "edit_status", "edits", "value_trace",
                     "answer_key_source", "answer_status"):
            continue
        po = fo.get((qi, pn), {}); pnw = fn.get((qi, pn), {})
        a, b = po.get(field), pnw.get(field)
        if field == "mark_points":
            a = "\n".join(m.get("text_md", "") for m in (a or []))
            b = "\n".join(m.get("text_md", "") for m in (b or []))
        if not isinstance(a, str) or not isinstance(b, str):
            others.append((series, paper, qi, pn, field, "NON-TEXT"))
            continue
        cls, ev = classify(a, b)
        buckets.setdefault(cls, []).append(f"{series}/{paper} {pn} [{field}] {ev}")

for cls, items in sorted(buckets.items()):
    print(f"== {cls} ({len(items)})")
    for i in items:
        print("  ", i)
print("== other/untouched:", len(others))
for o in others:
    print("  ", o)
json.dump({"buckets": buckets, "others": others},
          open("/tmp/f86-classes.json", "w"), indent=1, ensure_ascii=False)
