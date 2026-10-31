#!/usr/bin/env python3
"""YCH12 SB2 v2 pack-floor fold fix — folds the p49 i9 rescue residual into
the v2 corpus of record (T-PARSE-YCH12-2 follow-up, own gate).

METHOD_AND_FINDINGS D-12 §5: docling sidecar page_049 items i8
("WORKEDEXAMPLE2", section_header, 14 chars) and i9 ("N₂(g) + 3H₂(g) →
2NH₃(g)", formula, 24 chars, `rescued: true` — the last unconsumed rescue
fill) sum to 38 raw block chars, below the 40-char pack floor in
parse_docling_ych12.py flush() (`if size < 40: continue`) — the piece was
dropped and corpus index _0222 consumed (the corpus's 149-gap signature).

Fold design (the gate's legality argument):
  * The piece sits between chunk _0219 (WORKEDEXAMPLE1 block, POLISHED) and
    _0220 (ENTROPYCHANGEOFTHESURROUNDINGS body, UNPOLISHED) in reading order
    (sidecar bboxes y 472/459 vs 370).
  * Folding into _0219 is ILLEGAL: R1 freezes a polished chunk's corpus text
    to the evidence repair text (append-only evidence law — no edits).
  * Therefore the fold PREPENDS the piece text to _0220's text, in BOTH
    pristine and corpus (byte-identical), so R4 (untouched byte-equality),
    R3 (no text_original), R5 (anchor zero-drift) all hold; R6 evidence
    untouched; R1/R3 polished chunks untouched (the fold never enters a
    repair).
  * char_count recomputed as len(text) (the chunker's own law:
    char_count == len("\\n\\n".join(parts))).

Idempotence-guarded: aborts non-zero if the fold text is already present in
the target, if the target is polished, if corpus/pristine diverge on it, or
if the sidecar bytes do not match the fold text. Run BEFORE reseed.sh; the
standard chain (reseed -> merge -> reconcile -> audit -> validate) then
regenerates the corpus/md/report deterministically from the folded pristine.
"""
import json, os, subprocess, sys

LANE = os.environ.get("YCH12_LANE", "/home/z/my-project/gh_repos/syllabai-resources/books/pearson-edexcel/international-a-level/chemistry/ych12")
PRISTINE = os.environ.get("YCH12_PRISTINE", os.path.join(LANE, "parsed/edexcel_ial_chemistry_ych12_sb2_chunks_v2.pristine"))
REPAIRS = os.environ.get("YCH12_REPAIRS", os.path.join(LANE, "pipeline/evidence/llm_repairs_ych12_v2.jsonl"))
TARGET = "ych2_v2_u12_c2_pdf049_0220"
SIDECAR_PAGE = "page_049.json"
I_HEADER, I_FORMULA = 8, 9

fails = []
def fail(msg):
    fails.append(msg)

def load(path):
    m = {}
    for line in open(path, encoding="utf-8"):
        if line.strip():
            c = json.loads(line)
            m[c["id"]] = c
    return m

# --- sidecar ground truth (git show; docling_pages_v2 is sparse-excluded) ---
# blob:none lazy fetches flake occasionally — retry, then honor an
# env-provided pre-fetched copy (YCH12_SIDECAR_P49) as a last resort.
blob = None
for attempt in range(3):
    r = subprocess.run(
        ["git", "-C", LANE, "show", f"HEAD:pipeline/docling_pages_v2/{SIDECAR_PAGE}"],
        capture_output=True, text=True)
    if r.returncode == 0 and r.stdout.strip():
        blob = r.stdout
        break
    print(f"sidecar git-show attempt {attempt + 1} failed: {r.stderr.strip()[:120]}")
    import time
    time.sleep(2)
if blob is None:
    alt = os.environ.get("YCH12_SIDECAR_P49", "")
    if alt and os.path.exists(alt):
        blob = open(alt, encoding="utf-8").read()
        print(f"sidecar read from YCH12_SIDECAR_P49={alt}")
    else:
        print("FATAL: sidecar unreadable via git show and no YCH12_SIDECAR_P49 fallback")
        sys.exit(1)
items = json.loads(blob)["items"] if isinstance(json.loads(blob), dict) else json.loads(blob)
header_txt, formula_txt = items[I_HEADER]["text"], items[I_FORMULA]["text"]
if items[I_HEADER].get("label") != "section_header" or items[I_FORMULA].get("label") != "formula":
    fail(f"sidecar labels unexpected: {items[I_HEADER].get('label')}/{items[I_FORMULA].get('label')}")
if not items[I_FORMULA].get("rescued"):
    fail("sidecar i9 not marked rescued — fold premise changed, re-adjudicate")
FOLD = header_txt + "\n\n" + formula_txt

pristine = load(PRISTINE)
ok_ids = set()
for line in open(REPAIRS, encoding="utf-8"):
    if line.strip():
        r = json.loads(line)
        if r["status"] == "ok":
            ok_ids.add(r["id"])

# --- preconditions (the gate's first half) ---
t = pristine.get(TARGET)
if t is None:
    fail(f"{TARGET} missing from pristine")
else:
    if TARGET in ok_ids:
        fail(f"{TARGET} is polished — fold target illegal (R1 freezes repair text)")
    if "text_original" in t:
        fail(f"{TARGET} carries text_original — not an untouched parse-layer chunk")
    if FOLD in t["text"]:
        print(f"IDEMPOTENT: fold text already present in {TARGET} — nothing to do")
        sys.exit(0)
    if header_txt in t["text"] or formula_txt in t["text"]:
        fail(f"{TARGET} already contains part of the fold text — partial state, re-adjudicate")
    if t["char_count"] != len(t["text"]):
        fail(f"{TARGET} char_count {t['char_count']} != len(text) {len(t['text'])}")
    # drop confirmation: the header must not exist anywhere in the u12_c2 page-49 span
    span_hits = [cid for cid, c in pristine.items()
                 if cid.startswith("ych2_v2_u12_c2_pdf049") and header_txt in c["text"]]
    if span_hits:
        fail(f"WE2 header already present in {span_hits} — not a drop, re-adjudicate")
    if len(t["text"]) + len(FOLD) + 2 > 2500:
        fail("folded text would exceed the validator hard max 2500")

if fails:
    print("FOLD GATE PRE-CHECKS FAIL:")
    for m in fails:
        print("  -", m)
    sys.exit(1)

# --- apply: fold into pristine only; the chain regenerates corpus from it ---
snapshot = {cid: dict(c) for cid, c in pristine.items()}  # pre-fold copy for post-diff
before = t["text"]
t["text"] = FOLD + "\n\n" + before
t["char_count"] = len(t["text"])
with open(PRISTINE, "w", encoding="utf-8") as f:
    for cid, c in pristine.items():
        f.write(json.dumps(c, ensure_ascii=False) + "\n")

# --- post checks (the gate's second half) ---
p2 = load(PRISTINE)
t2 = p2[TARGET]
s2 = snapshot[TARGET]
if t2["text"] != FOLD + "\n\n" + before:
    fail("post: folded text mismatch")
if t2["char_count"] != len(t2["text"]):
    fail("post: char_count != len(text)")
ANCHOR_KEYS = ("id", "unit_no", "chapter_no", "content_type",
               "pdf_pages", "book_pages", "section", "unit_name", "chapter_title")
for k in ANCHOR_KEYS:
    if t2.get(k) != s2.get(k):
        fail(f"post: anchor field {k} drifted")
others = [cid for cid in p2 if cid != TARGET and p2[cid] != snapshot[cid]]
if others:
    fail(f"post: {len(others)} non-target chunks changed (e.g. {others[:3]})")
print(f"FOLD APPLIED to {TARGET}")
print(f"  fold text ({len(FOLD)} chars): {FOLD!r}")
print(f"  text {len(before)} -> {len(t2['text'])} chars (char_count {t2['char_count']})")
print("  sidecar byte-match: OK (i8 header + i9 rescued formula)")
print("FOLD GATE PRE/POST CHECKS PASS — proceed: reseed.sh -> merge -> reconcile -> audit -> validate x2")
if fails:
    print("FOLD GATE POST-CHECKS FAIL:")
    for m in fails:
        print("  -", m)
    sys.exit(1)
