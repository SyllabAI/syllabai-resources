#!/usr/bin/env python3
"""Generate analysis/learner-spec-links-demo.html — a static, self-contained
demo of how the learner UI renders spec links from spec-links/<course>.json.

Embeds real bundle slices (SDA-biology inheritance flashcards, igcse-biology
notes + exam parts) and follows the v72 prototype separation: canonical
truth (spec codes + provenance tiers) rendered plainly; the learner overlay
(mastery etc.) is mocked and visually separate.
"""
from __future__ import annotations
import json
from pathlib import Path

BASE = Path("/home/z/my-project/download/syllabai-resources")
OUT = BASE / "analysis" / "learner-spec-links-demo.html"

sda = json.loads((BASE / "spec-links/igcse-science-double-award-17-biology.json").read_text())
bio = json.loads((BASE / "spec-links/igcse-biology-19.json").read_text())

# flashcards: inheritance deck sample (mix of coded + pending)
fc = [(k, v) for k, v in sda["items"].items()
      if v["kind"] == "flashcard" and v["topic"] == "inheritance"]
fc_coded = [x for x in fc if x[1]["codes"]][:10]
fc_pending = [x for x in fc if not x[1]["codes"]][:2]
# notes: richest leaves
notes = sorted((v for v in bio["items"].values() if v["kind"] == "note" and v["codes"]),
               key=lambda v: -len(v["codes"]))[:3]
# question parts
parts = [(k, v) for k, v in bio["items"].items()
         if v["kind"] == "question_part" and v["codes"]][:6]

def codes_html(v):
    out = []
    for c in v["codes"]:
        t = c["tier"]
        cls = {"T1_verbatim": "t1", "T2_near": "t2",
               "T3_section_anchored": "t3", "T4_fuzzy": "flag",
               "S1_name_match": "s1", "S2_name_ambiguous": "flag"}.get(t, "t2")
        out.append(f'<span class="chip {cls}" title="{c["official_id"]} · {t} · {c.get("method","")}">'
                   f'{c["official_code"]}</span>')
    for p in v.get("pending", []):
        out.append(f'<span class="chip pending" title="{p}">pending</span>')
    return "".join(out)

cards_js = json.dumps([{"front": v["label"], "codes": v["codes"],
                        "pending": v.get("pending", [])} for _, v in fc_coded + fc_pending],
                       ensure_ascii=False)
notes_js = json.dumps([{"title": v["label"].replace(" - IGCSE Biology Revision Notes", ""),
                        "codes": v["codes"]} for v in notes], ensure_ascii=False)
parts_js = json.dumps([{"id": k, "topic": v["topic"], "codes": v["codes"]}
                       for k, v in parts], ensure_ascii=False)

html = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SyllabAI — learner spec links demo</title>
<style>
 :root{--ink:#14212b;--mut:#5b6b76;--line:#dde5ea;--bg:#f6f8f9;--card:#fff;
  --t1:#1c7c54;--t2:#0e7490;--t3:#2563eb;--s1:#b45309;--flag:#b91c1c;--pend:#6b7280;}
 *{box-sizing:border-box}
 body{margin:0;font:15px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:var(--ink);background:var(--bg)}
 header{background:#0f2a3d;color:#e8f1f5;padding:22px 28px}
 header h1{margin:0 0 4px;font-size:20px}
 header p{margin:0;color:#9fb8c4;font-size:13px}
 .wrap{max-width:960px;margin:0 auto;padding:22px 20px 60px}
 .tabs{display:flex;gap:8px;margin:18px 0 14px}
 .tabs button{border:1px solid var(--line);background:#fff;padding:8px 16px;border-radius:9px;
   font-size:14px;cursor:pointer;color:var(--mut)}
 .tabs button.on{background:#0f2a3d;border-color:#0f2a3d;color:#fff}
 .pane{display:none}.pane.on{display:block}
 .card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin-bottom:12px}
 .card h3{margin:0 0 8px;font-size:15px}
 .muted{color:var(--mut);font-size:13px}
 .chip{display:inline-block;margin:2px 6px 2px 0;padding:2px 9px;border-radius:999px;
   font-size:12px;font-weight:600;color:#fff}
 .chip.t1{background:var(--t1)}.chip.t2{background:var(--t2)}.chip.t3{background:var(--t3)}
 .chip.s1{background:var(--s1)}.chip.flag{background:#fff;color:var(--flag);border:1.5px solid var(--flag)}
 .chip.pending{background:#e5e7eb;color:var(--pend);border:1px dashed var(--pend)}
 .flip{margin-top:10px;padding-top:10px;border-top:1px dashed var(--line);font-size:14px}
 .legend{display:flex;flex-wrap:wrap;gap:10px;margin:6px 0 16px;font-size:12.5px;color:var(--mut)}
 .legend b{font-weight:600}
 .overlay{margin-top:26px;border:2px dashed #c4a2c9;border-radius:12px;padding:14px 18px;background:#faf5fb}
 .overlay h4{margin:0 0 6px;font-size:13px;color:#7c3f88;text-transform:uppercase;letter-spacing:.06em}
 .bar{height:8px;border-radius:6px;background:#eadff0;margin:6px 0 10px;overflow:hidden}
 .bar i{display:block;height:100%;background:#a56ab5}
</style></head><body>
<header>
 <h1>Learner spec links — canonical truth layer</h1>
 <p>spec-links/&lt;course&gt;.json · syllabai.learner-spec-links/1.0 · Edexcel official codes with provenance tiers · demo renders real bundle slices</p>
</header>
<div class="wrap">
 <div class="legend">
  <b>Legend:</b>
  <span class="chip t1">T1 verbatim</span><span class="chip t2">T2 near</span>
  <span class="chip t3">T3 section</span><span class="chip s1">S1 name</span>
  <span class="chip flag">review flag</span><span class="chip pending">pending</span>
 </div>
 <div class="tabs">
  <button class="on" onclick="tab(0,this)">Flashcards — SDA Biology · Inheritance</button>
  <button onclick="tab(1,this)">Revision notes — IGCSE Biology</button>
  <button onclick="tab(2,this)">Exam questions — IGCSE Biology</button>
 </div>

 <div class="pane on" id="p0"></div>

 <div class="pane" id="p1"></div>

 <div class="pane" id="p2"></div>

 <div class="overlay">
  <h4>Learner overlay (mock — strictly separate from canonical truth, v72 semantics)</h4>
  <div class="muted">mastery 0.62 · confidence 0.55 · fluency 0.48 · review due in 2 days — overlay is keyed by the same official_code chips above; nothing here edits the spec links.</div>
  <div class="bar"><i style="width:62%"></i></div>
 </div>
</div>
<script>
const CARDS = __CARDS__;
const NOTES = __NOTES__;
const PARTS = __PARTS__;
function chip(c){const cls={T1_verbatim:'t1',T2_near:'t2',T3_section_anchored:'t3',
 T4_fuzzy:'flag',S1_name_match:'s1',S2_name_ambiguous:'flag'}[c.tier]||'t2';
 return `<span class="chip ${cls}" title="${c.tier} · ${c.method||''}">${c.official_code}</span>`;}
function pend(p){return p.map(()=>`<span class="chip pending">pending</span>`).join('');}
document.getElementById('p0').innerHTML = CARDS.map((c,i)=>`
 <div class="card"><h3>Card ${i+1} — ${c.front}</h3>
  <div>${c.codes.map(chip).join('')}${pend(c.pending)}</div>
  <div class="flip muted">flip → back shows the answer with the matched statement's official code displayed as a spec chip.</div>
 </div>`).join('') || '<div class="card muted">no coded cards</div>';
document.getElementById('p1').innerHTML = NOTES.map(n=>`
 <div class="card"><h3>${n.title}</h3>
  <div class="muted">Revision note leaf — every spec point the note covers renders as a chip; the UI deep-links each chip to the official statement and to the learner's mastery on it.</div>
  <div style="margin-top:8px">${n.codes.map(chip).join('')}</div>
 </div>`).join('');
document.getElementById('p2').innerHTML = PARTS.map(p=>`
 <div class="card"><h3>Question part <code>${p.id}</code></h3>
  <div class="muted">topic: ${p.topic}</div>
  <div style="margin-top:8px">${p.codes.map(chip).join('')}${pend(p.pending)}</div>
 </div>`).join('');
function tab(i, btn){
 document.querySelectorAll('.tabs button').forEach(b=>b.classList.remove('on'));
 document.querySelectorAll('.pane').forEach(p=>p.classList.remove('on'));
 btn.classList.add('on'); document.getElementById('p'+i).classList.add('on');
}
</script></body></html>
"""
html = html.replace("__CARDS__", cards_js).replace("__NOTES__", notes_js).replace("__PARTS__", parts_js)
OUT.parent.mkdir(exist_ok=True)
OUT.write_text(html, encoding="utf-8")
print("wrote", OUT, len(html), "bytes")
