#!/usr/bin/env node
/**
 * LLM fidelity repair for OCR-corrupted chunks.
 * STRICT RULE: fix only OCR transcription errors; never reword/paraphrase.
 * Reads data/llm_repair_ids.json, writes data/llm_repairs.jsonl (resumable).
 */
const fs = require("fs");
const path = require("path");

const ZJSONL = "/home/z/my-project/download/rag_chemistry/edexcel_igcse_chemistry_chunks_v2.jsonl";
const IDS = JSON.parse(fs.readFileSync("/home/z/my-project/data/llm_repair_ids.json", "utf-8"));
const OUT = "/home/z/my-project/data/llm_repairs.jsonl";

const SYSTEM = `You are an OCR repair tool for a scanned IGCSE chemistry textbook.
You receive ONE chunk of OCR text that contains transcription errors.
Fix ONLY obvious OCR transcription errors, such as:
- chemical formulas merged with words (e.g. "water,(l)" is H2O(l), "hydrogen,(g)" is H2(g))
- garbled formulas (wrong digits/letters: "H20" -> "H2O", "CH;OH" -> "CH3OH", "CuS04" -> "CuSO4")
- split or merged words, wrong punctuation that breaks words
STRICT RULES:
1. NEVER paraphrase, rewrite, summarize or rephrase. Keep the original wording wherever it is readable.
2. Do NOT add, remove, reorder or complete content. If something is unreadable, leave it unchanged.
3. Keep the line structure of the input.
4. Correct chemistry must be preserved: when a formula is garbled, restore the standard formula only if the intended substance is clear from context; otherwise leave it.
5. Output ONLY the corrected text. No commentary, no markdown fences, no explanations.`;

function stripBreadcrumb(text) {
  const idx = text.indexOf("\n\n");
  if (text.startsWith("[") && idx > 0) return text.slice(idx + 2);
  return text;
}

function sanityCheck(original, repaired) {
  if (!repaired) return false;
  let t = repaired.trim();
  t = t.replace(/^```[a-z]*\n?/, "").replace(/```$/, "").trim();
  t = t.replace(/^(here is|here's) the corrected text:?\s*/i, "");
  if (t.length < original.length * 0.6) return null; // too short -> keep original
  if (t.length > original.length * 1.6) return null; // too long -> suspicious
  if (/i cannot|unable to|as an ai/i.test(t.slice(0, 80))) return null;
  return t;
}

async function repairOne(zai, chunk) {
  const body = stripBreadcrumb(chunk.text);
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
      await new Promise(r => setTimeout(r, is429 ? 8000 * attempt : 1500 * attempt));
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
        try { const r = JSON.parse(line); if (r.status === "ok") done.add(r.id); } catch {}
      }
    }
  }
  const todo = IDS.filter(id => chunks.has(id) && !done.has(id));
  console.log(`todo: ${todo.length}/${IDS.length} (already done: ${done.size})`);
  const zai = await (require("z-ai-web-dev-sdk").default).create();
  const CONC = 2;
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
