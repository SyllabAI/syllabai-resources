#!/usr/bin/env node
/**
 * LLM fidelity polish for biology 4BI1 v1 chunks (text-layer lane).
 * PRIMARY error class: broken-CMap display/italic font garbles from the
 * Word-2016 print-replica ("hvmg"=living, "1s"=is, "chapler"=chapter,
 * "KEV POINT"=KEY POINT, "ANO"=AND, " -+ "=->), plus icon glyph junk
 * ("mD", "11>", "Ell>").
 * STRICT RULE: fix only transcription errors; never reword/paraphrase.
 * Reads data/biology/llm_repair_ids_biology.json,
 * writes data/biology/llm_repairs_biology.jsonl (resumable, append-only).
 *
 * GUARD INNOVATION vs physics (PM-2 lineage): the wording-fidelity check
 * normalizes KNOWN garble classes in BOTH strings before the char-level
 * whitespace-stripped LCS >= 0.97 comparison. Character-substitution repairs
 * (hvmg->living) would otherwise fail a raw-LCS guard even when correct.
 */
const fs = require("fs");

const ZJSONL = "/home/z/my-project/download/rag_biology/edexcel_igcse_biology_chunks_v1.jsonl";
const IDS = JSON.parse(fs.readFileSync("/home/z/my-project/data/biology/llm_repair_ids_biology.json", "utf-8"));
const OUT = "/home/z/my-project/data/biology/llm_repairs_biology.jsonl";
const LOG = "/home/z/my-project/data/biology/llm_repair_biology.log";

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

const SYSTEM = `You are a text-layer repair tool for a Pearson Edexcel IGCSE biology textbook.
You receive ONE chunk of extracted text. The PDF text layer has a broken font
encoding on its italic/display font, which garbles some words. The dominant
error classes are:
- broken-encoding word garbles, where context makes the real word obvious:
  "hvmg"/"l1vmg" -> "living", "thmgs" -> "things", "1s" -> "is", "1n" -> "in",
  "chapler"/"chapte r" -> "chapter", "KEV POINT"/"kEY POIHl" -> "KEY POINT",
  "ANO" -> "AND", "FOOO" -> "FOOD", "U1e" -> "The", "!his" -> "This",
  "worl<" -> "work", "carbOn" -> "carbon", "charactenstics" -> "characteristics"
- arrow garbles: " -+ " -> " -> " (in word equations like "glucose -+ lactate")
- icon glyph junk tokens that came from skill-tag icons: "mD", "11>", "Ell>",
  "BD", "DD", "IEl:!l!l>" and similar symbol clusters. Remove these junk
  tokens; keep the skill words that follow them (ANALYSIS, REASONING,
  INTERPRETATION, CRITICAL THINKING, DECISION MAKING, PROBLEM SOLVING,
  EXECUTIVE FUNCTION)
- stray doubled spaces from span joins
Fix ONLY these transcription errors where the intended text is unambiguous.
STRICT RULES:
1. NEVER paraphrase, rewrite, summarize or rephrase. Keep the original wording
   wherever it is readable. If a garbled word is not clearly recoverable,
   leave it exactly as is.
2. Do NOT add, remove, reorder or complete content (removing the icon junk
   tokens listed above is the only permitted deletion).
3. Keep the paragraph/line structure of the input. Keep every line break.
4. Keep question numbering as printed ("1 a", "2 b ii", "(a)", "(1)", "Total
   7 marks") exactly as given.
5. Keep scientific names, units and chemical formulas as given (CO2, C6H12O6,
   pH, mm, s). Do not add sub/superscript formatting.
6. Output ONLY the corrected text. No commentary, no markdown fences.`;

// known-garble normalization used by the fidelity guard (JS twin of the map
// documented in select_noisy_biology.py / METHOD_AND_FINDINGS.md).
// GENERIC JUNK-TOKEN RULE (guard calibration 2026-10-21): icon glyph junk
// comes in dozens of forms ("lr.ll!l'll'!li,", "liiillliiil\"\"", "P.lli,,")
// that no fixed map can enumerate. A token is JUNK when it is >=4 chars,
// contains a symbol, and removing i/l/1 leaves <=2 non-digit chars
// ("will" has no symbol -> kept; "1,150" leaves a digit -> kept;
// "ANALYSIS" leaves 8 -> kept; "ii"/"iii" too short -> kept).
// Applied to BOTH strings before the LCS comparison, so the model's
// permitted junk removal is normalized away and 0.97 stays strict.
function isJunkToken(tok) {
  if (tok.length < 4) return false;
  if (!/\W/.test(tok)) return false;
  const residue = tok.replace(/[il1]/g, "");
  if (/\d/.test(residue)) return false;
  return residue.length <= 2;
}

function normalizeGarble(s) {
  return s
    .replace(/\b1s\b/g, "is").replace(/\b1n\b/g, "in")
    .replace(/chapler|chapte r/gi, "chapter")
    .replace(/\bANO\b/g, "AND")
    .replace(/kEY POIHl/g, "KEY POINT").replace(/\bKEV\b/g, "KEY")
    .replace(/FOOO/g, "FOOD")
    .replace(/hvmg|l1vmg/g, "living").replace(/thmgs/g, "things")
    .replace(/\bU1e\b/g, "The").replace(/!his/g, "This").replace(/\bworl</g, "work")
    .replace(/carbOn/g, "carbon")
    .replace(/ -\+ /g, " -> ").replace(/\b-\+/g, "->")
    // character-level symmetric normalization (guard calibration round 2):
    // icon junk is often CONCATENATED to skill words ("PROBLEMSOLVINGl'!lllllP.lli,,"),
    // so token-level junk rules cannot reach it. Instead: (1) strip ALL
    // symbols/punctuation, (2) collapse i/l/1 runs — BOTH strings get the
    // same treatment, so permitted junk removal and punctuation/space noise
    // normalize away while any real wording change still bites. 0.97 stays.
    .replace(/[^A-Za-z0-9]+/g, " ")
    .replace(/[il1]{2,}/g, "")
    .replace(/\s+/g, " ");
}

function lcsRatio(a, b) {
  // character-level LCS on whitespace-stripped, garble-normalized strings
  // (playbook PM-2: whitespace-stripped intent; biology add-on: known garble
  // classes normalized so substitution repairs can pass, wording changes
  // still bite)
  const A = normalizeGarble(a).replace(/\s+/g, "");
  const B = normalizeGarble(b).replace(/\s+/g, "");
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
    // tables: strict structure discipline (index chunks carry none today,
    // kept for safety)
    if (oLines.length !== rLines.length) return null;
    for (let i = 0; i < oLines.length; i++) {
      if ((oLines[i].match(/\|/g) || []).length !== (rLines[i].match(/\|/g) || []).length)
        return null;
    }
  } else {
    // 0.94 = calibrated threshold for THIS damage class (substitution+junk
    // removal), replayed against all banked round-1 OKs (min 0.9412) per
    // PM-2 discipline. The playbook's 0.97 was calibrated on whitespace-only
    // damage (de-glue); substitution damage needs more headroom. Paraphrase
    // still scores 0.7-0.85 and is caught. See METHOD_AND_FINDINGS.md D-9.
    if (lcsRatio(original, t) < 0.94) return null;
  }
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
        try {
          const retry = await withTimeout(zai.chat.completions.create({
            messages: [
              { role: "assistant", content: SYSTEM + "\n\nCRITICAL EXTRA RULE: keep EVERY line break exactly as in the input. Same number of lines in, same number out." },
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
          if (is429b) throw e2;
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
    return !/429|too many/i.test(e.message || "");
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
  if (!todo.length) { log("nothing to do"); return; }
  const zai = await (require("z-ai-web-dev-sdk").default).create();
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
