#!/usr/bin/env node
/**
 * LLM fidelity polish for residual noisy v3 (Docling) chunks.
 * STRICT RULE: fix only OCR/parse transcription errors; never reword/paraphrase.
 * Reads data/llm_repair_ids_v3.json, writes data/llm_repairs_v3.jsonl (resumable).
 */
const fs = require("fs");

const ZJSONL = "/home/z/my-project/download/rag_chemistry/edexcel_igcse_chemistry_chunks_v3.jsonl";
const IDS = JSON.parse(fs.readFileSync("/home/z/my-project/data/llm_repair_ids_v3.json", "utf-8"));
const OUT = "/home/z/my-project/data/llm_repairs_v3.jsonl";

const SYSTEM = `You are an OCR/layout-parser repair tool for a scanned IGCSE chemistry textbook.
You receive ONE chunk of parsed text that still contains transcription errors.
Fix ONLY obvious OCR/parser transcription errors, such as:
- garbled chemical formulas (wrong digits/letters: "CH8" -> "C3H8" where context is clear,
  "CH10" -> "C4H10", "H20" -> "H2O", "CuS04" -> "CuSO4", "C_H10" -> "C4H10")
- junk punctuation glued to words or cell values (".Ce" -> "Ce", ":Th" -> "Th", "• dThe" -> "The")
- split or merged words, wrong punctuation that breaks words or numbers
- misrecognised characters in context (tick marks shown as J or x in a checklist only if clear,
  "CI-CI" -> "Cl-Cl", "J-r" -> "I-I" when it is in a halogens bond-energy table)
STRICT RULES:
1. NEVER paraphrase, rewrite, summarize or rephrase. Keep the original wording wherever it is readable.
2. Do NOT add, remove, reorder or complete content. If something is unreadable or unclear, leave it exactly as is.
3. Keep the line/paragraph structure of the input. Keep markdown table pipes "|" and row counts EXACTLY as given.
4. Keep Unicode subscripts/superscripts (H₂O, CO₂, Cu²⁺) intact. In table cells you may restore
   correct subscripts to formulas (CH4 -> CH₄) when the substance is unambiguous.
5. Correct chemistry must be preserved: when a formula is garbled, restore the standard formula
   only if the intended substance is clear from context; otherwise leave it unchanged.
6. Output ONLY the corrected text. No commentary, no markdown fences, no explanations.`;

function sanityCheck(original, repaired) {
  if (!repaired) return false;
  let t = repaired.trim();
  t = t.replace(/^```[a-z]*\n?/, "").replace(/```$/, "").trim();
  t = t.replace(/^(here is|here's) the corrected text:?\s*/i, "");
  if (t.length < original.length * 0.6) return null; // too short -> keep original
  if (t.length > original.length * 1.6) return null; // too long -> suspicious
  if (/i cannot|unable to|as an ai/i.test(t.slice(0, 80))) return null;
  // table row-count guard: pipes per line must match
  const oLines = original.split("\n"), rLines = t.split("\n");
  if (oLines.length !== rLines.length) return null;
  for (let i = 0; i < oLines.length; i++) {
    if ((oLines[i].match(/\|/g) || []).length !== (rLines[i].match(/\|/g) || []).length)
      return null;
  }
  return t;
}

async function repairOne(zai, chunk) {
  const body = chunk.text;
  for (let attempt = 1; attempt <= 5; attempt++) {
    try {
      const completion = await zai.chat.completions.create({
        messages: [
          { role: "assistant", content: SYSTEM },
          { role: "user", content: body },
        ],
        thinking: { type: "disabled" },
      });
      const raw = completion.choices?.[0]?.message?.content || "";
      const cleaned = sanityCheck(body, raw);
      if (cleaned === null) {
        return { id: chunk.id, status: "rejected", reason: "sanity check failed" };
      }
      return { id: chunk.id, status: "ok", text: cleaned };
    } catch (e) {
      const is429 = /429|too many/i.test(e.message || "");
      if (attempt === 5) return { id: chunk.id, status: "error", reason: e.message };
      await new Promise(r => setTimeout(r, is429 ? 20000 * attempt : 1500 * attempt));
    }
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
  console.log(`todo: ${todo.length}/${IDS.length} (already done: ${done.size})`);
  const zai = await (require("z-ai-web-dev-sdk").default).create();
  const CONC = 1;
  let i = 0, ok = 0, rej = 0, err = 0;
  async function worker() {
    while (i < todo.length) {
      const id = todo[i++];
      const res = await repairOne(zai, chunks.get(id));
      fs.appendFileSync(OUT, JSON.stringify(res) + "\n");
      if (res.status === "ok") ok++;
      else if (res.status === "rejected") rej++;
      else { err++; console.log("ERR", id, res.reason); }
      if ((ok + rej + err) % 10 === 0)
        console.log(`progress: ${ok + rej + err}/${todo.length} (ok=${ok} rej=${rej} err=${err})`);
    }
  }
  await Promise.all(Array.from({ length: CONC }, worker));
  console.log(`DONE ok=${ok} rejected=${rej} error=${err}`);
}

main().catch(e => { console.error("FATAL", e.message); process.exit(1); });
