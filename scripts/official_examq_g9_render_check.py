#!/usr/bin/env python3
"""
official_examq_g9_render_check.py — G9 Learner-Surface Quality gate, RENDERED leg.

Drives the REAL syllabai-v2 hub (the production Next.js app — same component tree
as the Vercel deployment of record) through a headless browser (agent-browser CLI)
and validates the learner-facing rendered output per frozen benchmark case:

  A completeness    — question blocks present + ordered, MCQ options served,
                      crop figures inlined and actually LOADED, marks meta line.
  B semantic        — frozen expected fact snippets visible in the rendered text.
  C visual          — zero KaTeX error nodes, zero raw-TeX markers, zero
                      unrendered markdown artifacts in the page text.
  D interaction     — MCQ radiogroup: select correct -> Submit -> deterministic
                      "Correct — well done." feedback; distractor pass -> "Not
                      quite." + destructive styling.
  E solution        — solution reveal carries the frozen solution fact snippet
                      (or, when a case carries no TeX-free solution fact, the
                      reveal/must-expand presence check).
  F labels (F120)   — the printed part label is VISIBLE and rendered INLINE on
                      the same line as the part text: per frozen sample, the
                      chip [data-part-label] carries the exact frozen label,
                      is actually rendered (offsetParent/rects/visibility),
                      sits in a flex items-baseline row geometrically ON the
                      first text line (chip right edge before the text block,
                      chip band overlapping the text block's first line), and
                      the whole-page chip census equals the frozen
                      labelled_parts count with every chip on the attested
                      label grammar. Null (path-less) samples must render NO
                      chip — the fail-closed law, never an index guess. This
                      is the case the gate lacked when the labels shipped
                      (F119 QUEUED follow-up): a data field that exists but is
                      never rendered now FAILS here instead of shipping.

Renderer identity of record is captured per receipt (renderer.class =
"syllabai-v2-local-runtime" | "syllabai-v2-vercel"; the local runtime is the
production app code, NOT a mock or a standalone prototype).

CLI constraint of record: the agent-browser CLI strips double quotes from eval
arguments — every eval snippet below is therefore double-quote-free (single-quote
JS strings via the q() helper, find-by-attribute instead of quoted CSS selectors).

Honesty law: if the hub is unreachable, agent-browser is missing, or a case
cannot be driven, its checks are recorded NOT_RUN — never PASS. Aggregation
follows the G9 law (official_examq_g9_semantics.py, F105): a required check
that did not run can never yield a PASSing case; a case whose required checks
could not be established dispositions NOT_RUN and the leg rises to REVIEW in
the overall gate (official_examq_g9_aggregate.py — all three legs
static-corpus / static-bundles / rendered are mandatory for a PASS).
Evidence-only captures (screenshots) are recorded with requirement=evidence
and are excluded from the required set — they can neither pass nor fail a
case, only decorate it.
Exit codes: 0 all-PASS, 1 any FAIL, 2 blocked/NOT_RUN.

Usage:
  python3 scripts/official_examq_g9_render_check.py \
    --base-url http://localhost:3000 --cases Official-ExamQuestion/benchmark/cases.json \
    --out-dir Official-ExamQuestion/benchmark/receipts/<run-id> \
    [--only case-id1,case-id2] [--label run-label]
"""
import argparse
import datetime
import json
import re
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from official_examq_g9_semantics import (  # noqa: E402
    case_disposition, leg_disposition, REQ_EVIDENCE, OUTCOME_PASS, OUTCOME_NOT_RUN,
    LABEL_GRAMMAR_SRC,
)

VALIDATOR_VERSION = "g9-render-check/0.5"
SCROLL_STEPS = 14

AUDIT_JS = r"""
(() => {
  const qblocks = [...document.querySelectorAll('[data-question-block]')];
  const imgs = [...document.querySelectorAll('img')];
  const contentImgs = imgs.filter(i => !/(icon|logo|avatar|favicon|emoji)/i.test(i.getAttribute('src') || ''));
  const broken = contentImgs.filter(i => !(i.complete && i.naturalWidth > 0)).map(i => i.getAttribute('src'));
  const katexErr = document.querySelectorAll('.katex-error').length;
  const text = (document.body.innerText || '');
  const rawTex = (text.match(/\$\$|\\frac\{|\\ce\{|\\times\b/g) || []).length;
  const mdArtifacts = (text.match(/\*\*|\|---/g) || []).length;
  const radiogroups = [...document.querySelectorAll('[role=radiogroup],[role=group]')]
    .filter(g => /MCQ/.test(g.getAttribute('aria-label') || ''));
  const options = radiogroups.reduce((a, g) => a + g.querySelectorAll('[role=radio]').length, 0);
  const metaP = [...document.querySelectorAll('p')].find(p => / questions · /.test(p.textContent || ''));
  return JSON.stringify({
    url: location.pathname,
    qblocks: qblocks.length,
    qids: qblocks.map(b => b.getAttribute('data-question-block')),
    contentImgs: contentImgs.length,
    brokenImgs: broken.slice(0, 6),
    brokenCount: broken.length,
    katexErr: katexErr,
    rawTex: rawTex,
    mdArtifacts: mdArtifacts,
    radiogroups: radiogroups.length,
    options: options,
    headerMeta: metaP ? metaP.textContent.trim() : null,
  });
})()
"""


def q(s):
    """Emit a single-quoted JS string literal (agent-browser strips double quotes)."""
    return "'" + str(s).replace("\\", "\\\\").replace("'", "\\'") + "'"


def ab(*args, timeout=90, check_rc=True):
    cmd = ["agent-browser", *args]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    if check_rc and r.returncode != 0:
        raise RuntimeError(f"agent-browser {' '.join(args[:3])} rc={r.returncode}: {r.stderr.strip()[:300]}")
    return r.stdout.strip()


def ab_eval(js, timeout=90):
    """Run agent-browser eval and return the decoded JS result.

    agent-browser prints the JS result JSON-encoded; JSON.stringify results are
    therefore double-encoded. Unwrap until a non-string object or undecodable
    text remains.
    """
    txt = ab("eval", js, timeout=timeout).strip()
    for _ in range(3):
        try:
            v = json.loads(txt)
        except Exception:
            break
        if isinstance(v, str):
            txt = v
            continue
        return v
    return txt


def norm(s):
    return re.sub(r"\s+", " ", (s or "")).strip()


def wait_images(deadline_s=45):
    js = ("JSON.stringify([...document.querySelectorAll('img')]"
          ".filter(i => !(i.complete && i.naturalWidth > 0)).length)")
    t0 = time.time()
    while time.time() - t0 < deadline_s:
        try:
            if int(ab_eval(js)) == 0:
                return True
        except Exception:
            pass
        time.sleep(1.0)
    return False


def qblock_id_for_part(part_id):
    # offp_2023-06_2p_1-a-i -> offq_2023-06_2p_1 (series segment carries a hyphen;
    # split on underscores and keep only the numeric question-number head)
    if not part_id.startswith("offp_"):
        return None
    segs = part_id[len("offp_"):].split("_")
    if not segs:
        return None
    m = re.match(r"^(\d+)", segs[-1])
    if not m:
        return None
    segs[-1] = m.group(1)
    return "offq_" + "_".join(segs)


def find_qblock_js(qb):
    """find-by-attribute (no quoted CSS attribute selectors, no template literals)."""
    return ("(() => { const p = {qb: " + q(qb) + "};"
            " const qs = [...document.querySelectorAll('[data-question-block]')];"
            " const q = qs.find(x => x.getAttribute('data-question-block') === p.qb);"
            " if (!q) return JSON.stringify({err: 'qblock missing', have: qs.slice(0,3).map(x => x.getAttribute('data-question-block'))});"
            " return JSON.stringify({ok: true, q: q.getAttribute('data-question-block')}); })()")


# ── F120 label-visibility probes (the printed label must be VISIBLE + INLINE) ─

def labels_census_js():
    """Whole-page chip census over the part rows. The label grammar is the
    SHARED pattern string from official_examq_g9_semantics (single source of
    the F120 law) injected into the JS — the JS regex and the python regex
    cannot drift."""
    return ("(() => { const gram = new RegExp(" + q(LABEL_GRAMMAR_SRC) + ");"
            " const rows = [...document.querySelectorAll('[data-part-row]')];"
            " const chips = [];"
            " for (const r of rows) { const c = r.querySelector('[data-part-label]');"
            "  if (c) chips.push((c.textContent || '').trim()); }"
            " return JSON.stringify({ rows: rows.length, chips: chips.length,"
            "  badGrammar: chips.filter(t => !gram.test(t)).length }); })()")


def label_probe_js(pid, want):
    """Per-sample same-line visibility probe: the chip carries the EXACT frozen
    label, is actually rendered, and sits geometrically ON the first text line
    of its items-baseline row (chip right edge at/behind the text block's left
    edge minus the row gap; chip band overlapping the text block's top line).
    A chip-on-its-own-line layout (the PARTLABEL-1 shape the operator refined
    away) or an aria-only label (the original defect) fails here."""
    return ("(() => { const p = {pid: " + q(pid) + ", want: " + q(want) + "};"
            " const rows = [...document.querySelectorAll('[data-part-row]')];"
            " const row = rows.find(x => x.getAttribute('data-part-row') === p.pid);"
            " if (!row) return JSON.stringify({err: 'part row missing', rows: rows.length});"
            " const chip = row.querySelector('[data-part-label]');"
            " if (!chip) return JSON.stringify({err: 'label chip missing', rowHead: (row.innerText || '').slice(0, 60)});"
            " const got = (chip.textContent || '').trim();"
            " if (got !== p.want) return JSON.stringify({err: 'chip text mismatch', got: got, want: p.want});"
            " const cs = getComputedStyle(row);"
            " const cr = chip.getBoundingClientRect();"
            " const tb = chip.nextElementSibling;"
            " if (!tb) return JSON.stringify({err: 'text block missing'});"
            " const tr = tb.getBoundingClientRect();"
            " const vis = chip.offsetParent !== null && cr.width > 0 && cr.height > 0"
            "  && getComputedStyle(chip).visibility !== 'hidden' && getComputedStyle(chip).display !== 'none';"
            " const sameLine = cs.display === 'flex' && cs.alignItems === 'baseline'"
            "  && cr.bottom >= tr.top + 1 && cr.top <= tr.top + 30 && cr.top >= tr.top - 8"
            "  && cr.right <= tr.left + 2.5;"
            " return JSON.stringify({ ok: vis && sameLine, vis: vis, sameLine: sameLine,"
            "  flex: cs.display, align: cs.alignItems,"
            "  rect: { chipTop: Math.round(cr.top), chipBottom: Math.round(cr.bottom),"
            "          chipRight: Math.round(cr.right), textTop: Math.round(tr.top), textLeft: Math.round(tr.left) } }); })()")


def label_null_probe_js(pid):
    """Fail-closed probe for a path-less (null-label) part: the row must render
    with its text but carry NO chip — never an invented or index-guessed label."""
    return ("(() => { const p = {pid: " + q(pid) + "};"
            " const rows = [...document.querySelectorAll('[data-part-row]')];"
            " const row = rows.find(x => x.getAttribute('data-part-row') === p.pid);"
            " if (!row) return JSON.stringify({err: 'part row missing'});"
            " const chip = row.querySelector('[data-part-label]');"
            " const hasText = (row.innerText || '').trim().length > 0;"
            " return JSON.stringify({ ok: !chip && hasText,"
            "  chip: chip ? (chip.textContent || '').trim() : null, hasText: hasText }); })()")


def wait_ready(base_url):
    import urllib.request
    with urllib.request.urlopen(base_url + "/courses", timeout=20) as r:
        if r.status != 200:
            raise RuntimeError(f"hub /courses HTTP {r.status}")
    ab("--version", timeout=30)


def drive_case(base_url, case, outdir, shots=True):
    checks = []
    url = base_url + case["url_path"]

    def ck(area, name, ok, detail="", requirement="required"):
        checks.append({"id": f"{area}:{name}", "area": area,
                       "outcome": ("PASS" if ok else "FAIL"), "requirement": requirement,
                       "detail": str(detail)[:300]})

    def open_page():
        try:
            ab("open", url, timeout=120)
        except RuntimeError:
            time.sleep(4)  # dev-server first-compile / browser-relaunch race
            ab("open", url, timeout=120)
        ab("wait", "--load", "networkidle", timeout=90, check_rc=False)
        for _ in range(SCROLL_STEPS):
            ab("scroll", "down", "900", timeout=30, check_rc=False)
            time.sleep(0.2)
        ab("scroll", "up", "400", timeout=30, check_rc=False)
        wait_images()
        time.sleep(0.4)

    open_page()
    audit = ab_eval(AUDIT_JS)
    if audit["brokenCount"] > 0:
        # one retry round: re-scroll (some lazy loads need a second pass) and re-wait
        for _ in range(SCROLL_STEPS):
            ab("scroll", "down", "900", timeout=30, check_rc=False)
            time.sleep(0.15)
        ab("scroll", "up", "400", timeout=30, check_rc=False)
        wait_images(30)
        time.sleep(0.5)
        audit = ab_eval(AUDIT_JS)
    (outdir / f"dom-audit-{case['id']}.json").write_text(json.dumps(audit, indent=1))
    e = case["expected"]

    # ── A completeness ──────────────────────────────────────────────────────
    ck("completeness", "question-blocks", audit["qblocks"] == e["questions"],
       f"{audit['qblocks']} blocks vs {e['questions']} expected; head={audit['qids'][:2]}")
    hm = audit.get("headerMeta") or ""
    ck("completeness", "marks-meta",
       f"{e['marks_total']} marks" in hm and f"{e['questions']} questions" in hm, hm)
    ck("completeness", "images-loaded", audit["brokenCount"] == 0,
       f"{audit['contentImgs']} content imgs, broken={audit['brokenImgs']}")
    ck("completeness", "mcq-options-served",
       (audit["options"] == 0 and e["mcq_parts"] == 0) or audit["options"] > 0,
       f"radiogroups={audit['radiogroups']} options={audit['options']} (expected mcq_parts={e['mcq_parts']})")

    # ── B semantic fidelity ─────────────────────────────────────────────────
    page_text = norm(ab_eval("JSON.stringify((document.body.innerText||''))"))
    for fact in case["fact_parts"]:
        want = norm(fact["snippet"])
        ck("semantic", f"fact:{fact['part_id']}", want in page_text,
           "snippet visible in rendered text" if want in page_text else "MISSING from rendered text")

    # ── C visual integrity ──────────────────────────────────────────────────
    ck("visual", "no-katex-errors", audit["katexErr"] == 0, f"{audit['katexErr']} .katex-error nodes")
    ck("visual", "no-raw-tex", audit["rawTex"] == 0, f"{audit['rawTex']} raw-TeX markers in page text")
    ck("visual", "no-md-artifacts", audit["mdArtifacts"] == 0, f"{audit['mdArtifacts']} markdown artifacts")

    # ── D interaction — MCQ deterministic marking (correct + distractor) ────
    ix = case.get("mcq_interaction")
    if ix:
        qb = qblock_id_for_part(ix["part_id"])
        found = ab_eval(find_qblock_js(qb))
        if not found.get("ok"):
            ck("interaction", "qblock-resolves", False, f"{qb}: {found}")
        else:
            ck("interaction", "qblock-resolves", True, qb)
            for attempt, want_correct, label in (("correct", True, ix["correct_label"]),
                                                 ("distractor", False, ix["distractor_label"])):
                if not want_correct:
                    open_page()  # fresh player state for the second pass
                click_js = ("(() => { const p = {qb: " + q(qb) + ", label: " + q(label) + "};"
                            " const qs = [...document.querySelectorAll('[data-question-block]')];"
                            " const q = qs.find(x => x.getAttribute('data-question-block') === p.qb);"
                            " if (!q) return JSON.stringify({err: 'qblock missing'});"
                            " const radios = [...q.querySelectorAll('[role=radio]')];"
                            " const target = radios.find(r => ((r.querySelector('span') || {}).textContent || '').trim() === p.label);"
                            " if (!target) return JSON.stringify({err: 'radio not found', labels: radios.map(r => ((r.querySelector('span') || {}).textContent || '').trim().slice(0,2))});"
                            " target.click(); return JSON.stringify({ok: true}); })()")
                res = ab_eval(click_js)
                if res.get("err"):
                    ck("interaction", f"select-{attempt}", False, f"{ix['part_id']}: {res}")
                    break
                submit_js = ("(() => { const p = {qb: " + q(qb) + "};"
                             " const qs = [...document.querySelectorAll('[data-question-block]')];"
                             " const q = qs.find(x => x.getAttribute('data-question-block') === p.qb);"
                             " const btn = [...q.querySelectorAll('button')].find(b => /Submit answer/.test(b.textContent));"
                             " if (!btn) return JSON.stringify({err: 'submit button missing'}); btn.click();"
                             " return JSON.stringify({ok: true}); })()")
                res2 = ab_eval(submit_js)
                time.sleep(0.5)
                if res2.get("err"):
                    ck("interaction", f"submit-{attempt}", False, f"{ix['part_id']}: {res2}")
                    break
                state_js = ("(() => { const p = {qb: " + q(qb) + ", correct: " + q(ix["correct_label"]) + ", chosen: " + q(label) + "};"
                            " const qs = [...document.querySelectorAll('[data-question-block]')];"
                            " const q = qs.find(x => x.getAttribute('data-question-block') === p.qb);"
                            " const radios = [...q.querySelectorAll('[role=radio]')];"
                            " const row = (lab) => { const r = radios.find(r => ((r.querySelector('span') || {}).textContent || '').trim() === lab);"
                            "   if (!r) return null; return {success: r.className.includes('border-success'), destructive: r.className.includes('border-destructive')}; };"
                            " const fb = [...q.querySelectorAll('p')].map(x => x.textContent.trim()).filter(t => /Correct|Not quite/.test(t));"
                            " return JSON.stringify({rowCorrect: row(p.correct), rowChosen: row(p.chosen), feedback: fb.slice(0, 1)}); })()")
                st = ab_eval(state_js)
                if want_correct:
                    rowc = st.get("rowCorrect") or {}
                    okc = bool(rowc.get("success")) and any("Correct — well done" in t for t in st.get("feedback", []))
                    ck("interaction", "submit-correct", okc, f"{ix['part_id']}: {st}")
                else:
                    rowc = st.get("rowCorrect") or {}
                    rowch = st.get("rowChosen") or {}
                    okw = bool(rowc.get("success")) and bool(rowch.get("destructive")) and any("Not quite" in t for t in st.get("feedback", []))
                    ck("interaction", "submit-distractor", okw, f"{ix['part_id']}: {st}")

    # ── E solution ──────────────────────────────────────────────────────────
    if case["solution_facts"]:
        fact = case["solution_facts"][0]
        want = norm(fact["snippet"])
        epart = fact["part_id"]
        qbs = qblock_id_for_part(epart)
        reveal_js = ("(() => { const p = {qb: " + q(qbs) + "};"
                     " const qs = [...document.querySelectorAll('[data-question-block]')];"
                     " const q = qs.find(x => x.getAttribute('data-question-block') === p.qb);"
                     " if (!q) return JSON.stringify({err: 'qblock missing'});"
                     " const btn = [...q.querySelectorAll('button')].find(b => /Why this is the answer|Answer and mark scheme/.test(b.textContent));"
                     " if (!btn) return JSON.stringify({err: 'reveal button missing'});"
                     " if (btn.getAttribute('aria-expanded') !== 'true') btn.click();"
                     " return JSON.stringify({ok: true}); })()")
        rv = ab_eval(reveal_js)
        if not rv.get("ok") and want:
            # non-MCQ case: solutions open through the per-question "View answer" modal
            open_js = ("(() => { const p = {qb: " + q(qbs) + "};"
                       " const qs = [...document.querySelectorAll('[data-question-block]')];"
                       " const q = qs.find(x => x.getAttribute('data-question-block') === p.qb);"
                       " const btns = [...(q || document).querySelectorAll('button')].filter(b => b.textContent.trim() === 'View answer');"
                       " if (!btns.length) return JSON.stringify({err: 'no View answer button'});"
                       " btns[0].click(); return JSON.stringify({ok: true}); })()")
            ov = ab_eval(open_js)
            time.sleep(0.6)
            dtxt = norm(ab_eval("JSON.stringify((document.body.innerText||'').slice(0, 20000))"))
            ck("solution", f"solution-modal:{epart}", ov.get("ok") and want in dtxt,
               "solution fact visible in the View answer modal" if want in dtxt else f"MISSING from modal; open={ov}")
            close_js = ("(() => { const b = [...document.querySelectorAll('button')]"
                        "                        .find(b => (b.getAttribute('aria-label') || '') === 'Close mark scheme');"
                        " if (b) b.click(); return JSON.stringify({ok: true}); })()")
            ab_eval(close_js)
        else:
            time.sleep(0.4)
            txt_js = ("(() => { const p = {qb: " + q(qbs) + "};"
                      " const qs = [...document.querySelectorAll('[data-question-block]')];"
                      " const q = qs.find(x => x.getAttribute('data-question-block') === p.qb);"
                      " return JSON.stringify(q.innerText.slice(0, 4000)); })()")
            qtxt = norm(ab_eval(txt_js))
            ck("solution", f"solution-renders:{epart}", rv.get("ok") and want in qtxt,
               "solution fact visible after reveal" if want in qtxt else f"MISSING; reveal={rv}")
    elif e.get("solutions", 0) > 0:
        pick_js = ("(() => { const qs = [...document.querySelectorAll('[data-question-block]')];"
                   " for (const q of qs) { const btn = [...q.querySelectorAll('button')].find(b => /Why this is the answer|Answer and mark scheme/.test(b.textContent));"
                   " if (btn) return JSON.stringify({qb: q.getAttribute('data-question-block')}); }"
                   " return JSON.stringify({err: 'no reveal button on page'}); })()")
        picked = ab_eval(pick_js)
        if picked.get("qb"):
            rv = ab_eval("(() => { const p = {qb: " + q(picked["qb"]) + "};"
                         " const qs = [...document.querySelectorAll('[data-question-block]')];"
                         " const q = qs.find(x => x.getAttribute('data-question-block') === p.qb);"
                         " const btn = [...q.querySelectorAll('button')].find(b => /Why this is the answer|Answer and mark scheme/.test(b.textContent));"
                         " if (btn && btn.getAttribute('aria-expanded') !== 'true') btn.click();"
                         " return JSON.stringify({ok: true}); })()")
            time.sleep(0.4)
            txt_js = ("(() => { const p = {qb: " + q(picked["qb"]) + "};"
                      " const qs = [...document.querySelectorAll('[data-question-block]')];"
                      " const q = qs.find(x => x.getAttribute('data-question-block') === p.qb);"
                      " return JSON.stringify(q.innerText.slice(0, 4000)); })()")
            qtxt = norm(ab_eval(txt_js))
            ck("solution", f"reveal-presence:{picked['qb']}",
               rv.get("ok") and len(qtxt) > 0,
               "solution reveal expands with non-empty content" if rv.get("ok") else f"reveal failed: {rv}")
        else:
            ck("solution", "reveal-presence", False, str(picked))

    # ── F labels — the printed label is visible, inline, exact (F120) ────────
    if "labelled_parts" in e or case.get("part_labels"):
        ls = ab_eval(labels_census_js())
        ck("labels", "labels-rows-served",
           ls.get("rows") == e["parts"],
           f"rows={ls.get('rows')} vs parts={e['parts']}")
        ck("labels", "labels-chip-census",
           ls.get("chips") == e.get("labelled_parts") and ls.get("badGrammar") == 0,
           f"chips={ls.get('chips')} vs labelled={e.get('labelled_parts')} "
           f"badGrammar={ls.get('badGrammar')}")
        for smp in case.get("part_labels") or []:
            if smp.get("kind") == "null" or not smp.get("label"):
                r = ab_eval(label_null_probe_js(smp["part_id"]))
                ck("labels", f"label-null:{smp['part_id']}", bool(r.get("ok")), str(r)[:220])
            else:
                r = ab_eval(label_probe_js(smp["part_id"], smp["label"]))
                ck("labels", f"label:{smp['part_id']}", bool(r.get("ok")), str(r)[:220])

    # ── evidence ────────────────────────────────────────────────────────────
    if shots:
        try:
            ab("screenshot", str(outdir / f"case-{case['id']}-post-interaction.png"), timeout=60)
        except Exception as exc:
            checks.append({"id": "evidence:screenshot", "area": "visual",
                           "outcome": "NOT_RUN", "requirement": REQ_EVIDENCE,
                           "detail": f"screenshot failed (evidence-only, non-blocking): {exc}"})

    return case_disposition(checks), checks, audit


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-url", default="http://localhost:3000")
    ap.add_argument("--cases", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--only", default=None)
    ap.add_argument("--label", default="run")
    args = ap.parse_args()

    bench = json.loads(Path(args.cases).read_text())
    cases = bench["cases"]
    if args.only:
        keep = set(args.only.split(","))
        cases = [c for c in cases if c["id"] in keep]

    outdir = Path(args.out_dir)
    outdir.mkdir(parents=True, exist_ok=True)

    receipt = {
        "receipt_schema": "syllabai.g9-render-receipt/0.1",
        "validator_version": VALIDATOR_VERSION,
        "benchmark_version": bench.get("benchmark_version"),
        "label": args.label,
        "base_url": args.base_url,
        "started_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "cases": [],
    }
    try:
        wait_ready(args.base_url)
        renderer_class = "syllabai-v2-vercel" if "vercel.app" in args.base_url else "syllabai-v2-local-runtime"
    except Exception as exc:
        for c in cases:
            receipt["cases"].append({
                "case_id": c["id"], "disposition": OUTCOME_NOT_RUN, "checks": [
                    {"id": "renderer-available", "area": "completeness",
                     "outcome": OUTCOME_NOT_RUN, "requirement": "required",
                     "detail": f"hub/browser unavailable: {exc}"}]})
        receipt["overall"] = OUTCOME_NOT_RUN
        receipt["renderer"] = {"class": None, "note": "BLOCKED — renderer not reachable; NOT_RUN is not PASS"}
        (outdir / "g9-render-receipt.json").write_text(json.dumps(receipt, indent=1))
        print(f"G9 render check: BLOCKED ({exc}) — all cases NOT_RUN -> {outdir/'g9-render-receipt.json'}")
        sys.exit(2)

    receipt["renderer"] = {"class": renderer_class, "base_url": args.base_url,
                           "note": "production syllabai-v2 app (apps/hub) driven through a real browser; "
                                   "not a mock or standalone prototype"}
    for case in cases:
        try:
            disp, checks, audit = drive_case(args.base_url, case, outdir, shots=True)
        except Exception as exc:
            disp, checks = OUTCOME_NOT_RUN, [{"id": "case-driver", "area": "completeness",
                                              "outcome": OUTCOME_NOT_RUN, "requirement": "required",
                                              "detail": f"driver error: {exc}"}]
        receipt["cases"].append({"case_id": case["id"], "disposition": disp, "checks": checks})
        print(f"  {case['id']}: {disp}")
    receipt["finished_utc"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    receipt["overall"] = leg_disposition(receipt["cases"])
    (outdir / "g9-render-receipt.json").write_text(json.dumps(receipt, indent=1))
    print(f"G9 render check: overall={receipt['overall']} -> {outdir/'g9-render-receipt.json'}")
    sys.exit(0 if receipt["overall"] == "PASS" else (2 if receipt["overall"] == "NOT_RUN" else 1))


if __name__ == "__main__":
    main()
