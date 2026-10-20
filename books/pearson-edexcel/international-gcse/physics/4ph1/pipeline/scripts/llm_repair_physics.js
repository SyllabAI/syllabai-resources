#!/usr/bin/env node
/**
 * LLM fidelity polish for physics 4PH1 v1 chunks (chemistry-style, physics-adapted).
 * PRIMARY error class on this scan: RapidOCR drops spaces between words.
 * STRICT RULE: fix only OCR/parse transcription errors; never reword/paraphrase.
 * Reads data/llm_repair_ids_physics.json, writes data/llm_repairs_physics.jsonl (resumable).
 */
const fs = require("fs");

const ZJSONL = "/home/z/my-project/download/rag_physics/edexcel_igcse_physics_chunks_v1.jsonl";
const IDS = JSON.parse(fs.readFileSync("/home/z/my-project/data/llm_repair_ids_physics.json", "utf-8"));
const OUT = "/home/z/my-project/data/llm_repairs_physics.jsonl";
const LOG = "/home/z/my-project/data/llm_repair_r2.log";

function log(msg) {
  const line = `[${new Date().toISOString()}] ${msg}`;
  console.log(line);
  try { fs.appendFileSync(LOG, line + "\n"); } catch {}
}

function withTimeout(promise, ms, label) {
  return Promise.race([
    promise,
    new Promise((_, rej) => setTimeout(() => rej(new Error(`TIMEOUT ${label} ${ms / 1000}s`)), ms)),
  ]);
}

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

const LINE_STRICT = `\n\nCRITICAL EXTRA RULE: keep EVERY line break exactly as in the\ninput. Do not merge, split, join or reorder lines. Same number of lines in,\nsame number out. This overrides any urge to reflow paragraphs.`;

const SYSTEM = `You are an OCR/layout-parser repair tool for a scanned IGCSE physics textbook.
You receive ONE chunk of parsed text that still contains transcription errors.
The dominant error on this scan is DROPPED SPACES between words
("therelationshipbetween" -> "the relationship between", "PearsonEdexcel" ->
"Pearson Edexcel", "tcomeswith" -> "It comes with" when the missing letter is
clear from context, "CRITICALTHINKING" -> "CRITICAL THINKING").
Fix ONLY obvious OCR/parser transcription errors, such as:
- missing spaces between words (restore them using context; do not split a
  genuine single word like "electromagnetic" or "without")
- letters dropped at word boundaries ("tcomeswith", "sasked")
- garbled numbers/units in context ("1O m/s" -> "10 m/s" where clear)
- misrecognised characters where context is unambiguous ("rn" vs "m" inside words)
- junk punctuation glued to words (".The" -> ". The", ":Th" -> "Th")
- split or merged words, wrong punctuation that breaks words or numbers
STRICT RULES:
1. NEVER paraphrase, rewrite, summarize or rephrase. Keep the original wording
   wherever it is readable.
2. Do NOT add, remove, reorder or complete content. If something is unreadable
   or unclear, leave it exactly as is.
3. Keep the line/paragraph structure of the input. Keep markdown table pipes "|"
   and row counts EXACTLY as given.
4. Keep Unicode superscripts/subscripts and unit symbols EXACTLY as given
   (m/s², kg·m/s, N/kg, Ω, °C, v², ¹³⁷Cs, ×10⁸, μm). Never convert them to
   ASCII or remove them.
5. Keep question numbering as printed ("1 a", "2 b ii", "(a)") and keep table
   cell values aligned to their pipes.
6. Output ONLY the corrected text. No commentary, no markdown fences, no explanations.`;

const UNICHARS = /[₀-₉⁰¹²³⁴-⁹⁺⁻°×μΩ·]/g;

function lcsRatio(a, b) {
  // token-sequence similarity: allows whitespace reflow, forbids wording changes
  const A = a.split(/\s+/).filter(Boolean), B = b.split(/\s+/).filter(Boolean);
  if (!A.length || !B.length) return 0;
  const prev = new Array(B.length + 1).fill(0);
  let cur = new Array(B.length + 1).fill(0);
  for (let i = 1; i <= A.length; i++) {
    for (let j = 1; j <= B.length; j++) {
      cur[j] = A[i - 1] === B[j - 1] ? prev[j - 1] + 1 : Math.max(prev[j], cur[j - 1]);
    }
    for (let j = 0; j <= B.length; j++) prev[j] = cur[j];
  }
  return (2 * prev[B.length]) / (A.length + B.length);
}

function sanityCheck(original, repaired) {
  if (!repaired) return false;
  let t = repaired.trim();
  t = t.replace(/^```[a-z]*\n?/, "").replace(/```$/, "").trim();
  t = t.replace(/^(here is|here's) the corrected text:?\s*/i, "");
  if (t.length < original.length * 0.6) return null; // too short -> keep original
  if (t.length > original.length * 1.7) return null; // too long -> suspicious
  if (/i cannot|unable to|as an ai/i.test(t.slice(0, 80))) return null;
  const oLines = original.split("\n"), rLines = t.split("\n");
  if (original.includes("|")) {
    // tables: strict structure discipline
    if (oLines.length !== rLines.length) return null;
    for (let i = 0; i < oLines.length; i++) {
      if ((oLines[i].match(/\|/g) || []).length !== (rLines[i].match(/\|/g) || []).length)
        return null;
    }
  } else {
    // prose: wording fidelity via whitespace-normalized token similarity
    if (lcsRatio(original, t) < 0.97) return null;
  }
  // physics guard: Unicode unit/superscript characters must never decrease
  const oc = (original.match(UNICHARS) || []).length;
  const rc = (t.match(UNICHARS) || []).length;
  if (rc < oc) return null;
  return t;
}

async function repairOne(zai, chunk) {
  const body = chunk.text;
  for (let attempt = 1; attempt <= 5; attempt++) {
    try {
      const completion = await withTimeout(zai.chat.completions.create({
        messages: [
          { role: "assistant", content: SYSTEM },
          { role: "user", content: body },
        ],
        thinking: { type: "disabled" },
      }), 120000, "main-call");
      const raw = completion.choices?.[0]?.message?.content || "";
      let cleaned = sanityCheck(body, raw);
      if (cleaned === null) {
        // one line-strict retry before giving up (common failure: reflowed lines)
        try {
          const retry = await withTimeout(zai.chat.completions.create({
            messages: [
              { role: "assistant", content: SYSTEM + LINE_STRICT },
              { role: "user", content: body },
            ],
            thinking: { type: "disabled" },
          }), 120000, "strict-retry");
          const raw2 = retry.choices?.[0]?.message?.content || "";
          cleaned = sanityCheck(body, raw2);
          if (cleaned === null) {
            return { id: chunk.id, status: "rejected", reason: "sanity check failed (incl line-strict retry)", raw: raw2.slice(0, 6000) };
          }
        } catch (e2) {
          const is429b = /429|too many/i.test(e2.message || "");
          if (is429b) throw e2; // quota: bubble up, do not burn the record
          return { id: chunk.id, status: "rejected", reason: "sanity fail + retry errored: " + e2.message, raw: raw.slice(0, 6000) };
        }
      }
      return { id: chunk.id, status: "ok", text: cleaned };
    } catch (e) {
      const is429 = /429|too many/i.test(e.message || "");
      if (attempt === 5) return { id: chunk.id, status: "error", reason: e.message };
      await sleep(is429 ? 20000 * attempt : 1500 * attempt);
    }
  }
}

async function probeQuota(zai) {
  try {
    await withTimeout(zai.chat.completions.create({
      messages: [{ role: "user", content: "Reply with exactly: OK" }],
      thinking: { type: "disabled" },
    }), 30000, "probe");
    return true;
  } catch (e) {
    return !/429|too many/i.test(e.message || ""); // non-429 errors: let the run proceed
  }
}

async function main() {
  const chunks = new Map();
  for (const line of fs.readFileSync(ZJSONL, "utf-8").split("\n")) {
    if (!line.trim()) continue;
    const c = JSON.parse(line);
    chunks.set(c.id, c);
  }
  const done = new Set();
  if (fs.existsSync(OUT)) {
    for (const line of fs.readFileSync(OUT, "utf-8").split("\n")) {
      if (line.trim()) {
        try { const r = JSON.parse(line); if (r.status === "ok" || r.status === "rejected") done.add(r.id); } catch {}
      }
    }
  }
  const todo = IDS.filter(id => chunks.has(id) && !done.has(id));
  log(`todo: ${todo.length}/${IDS.length} (already done: ${done.size})`);
  const zai = await (require("z-ai-web-dev-sdk").default).create();
  // ---- quota probe: do not grind retries while the wall is up ----
  const PROBE_MAX = Number(process.env.PROBE_MAX || 8);
  let cleared = false;
  for (let p = 1; p <= PROBE_MAX; p++) {
    if (await probeQuota(zai)) { log(`quota probe ${p}: clear`); cleared = true; break; }
    const wait = Number(process.env.PROBE_WAIT || 90);
    log(`quota probe ${p}/${PROBE_MAX}: 429 -> wait ${wait}s`);
    await sleep(wait * 1000);
  }
  if (!cleared) { log("quota still down after probes -> clean exit (resume later)"); return; }
  const CONC = Number(process.env.CONC || 1);
  let i = 0, ok = 0, rej = 0, err = 0, consec429 = 0;
  async function worker() {
    while (i < todo.length) {
      const id = todo[i++];
      const res = await repairOne(zai, chunks.get(id));
      fs.appendFileSync(OUT, JSON.stringify(res) + "\n");
      if (res.status === "ok") { ok++; consec429 = 0; log(`OK ${id} (${ok + rej + err}/${todo.length})`); }
      else if (res.status === "rejected") { rej++; log(`REJ ${id} ${res.reason}`); }
      else {
        err++;
        if (/429|too many/i.test(res.reason || "")) consec429++;
        log(`ERR ${id} ${res.reason}`);
      }
      if ((ok + rej + err) % 10 === 0)
        log(`progress: ${ok + rej + err}/${todo.length} (ok=${ok} rej=${rej} err=${err})`);
      if (consec429 >= 2) { log("QUOTA: 2 consecutive 429 chunks -> stopping run (resume later)"); break; }
    }
  }
  await Promise.all(Array.from({ length: CONC }, worker));
  log(`DONE ok=${ok} rejected=${rej} error=${err}`);
}

main().catch(e => { console.error("FATAL", e.message); log("FATAL " + e.message); process.exit(1); });
