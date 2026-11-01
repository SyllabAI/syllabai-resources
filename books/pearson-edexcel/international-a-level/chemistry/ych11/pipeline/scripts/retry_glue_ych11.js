#!/usr/bin/env node
/**
 * YCH11 polish pass-2 spot retry (T-PARSE-YCH11-1-R5): re-ask the LLM for a
 * fixed id list whose pass-1 "ok" repairs left residual space-glue runs
 * (audit residual class: non-vocabulary 18+ lowercase runs). Evidence law:
 * append-only; a retry record is appended ONLY if it passes the runner's
 * sanity check AND differs from the input — a failed/429 retry appends
 * NOTHING, so the pass-1 ok record stays the of-record (latest-wins merge
 * can never regress the corpus).
 * Paths via env, same surface as llm_repair_ych11.js:
 *   YCH11_CORPUS, YCH11_REPAIRS, YCH11_LOG
 */
const fs = require("fs");

const ZJSONL = process.env.YCH11_CORPUS || "/home/z/my-project/data/ych11_sb1/out/edexcel_ial_chemistry_ych11_sb1_chunks_v1.jsonl";
const OUT = process.env.YCH11_REPAIRS || "/home/z/my-project/data/ych11_sb1/llm_repairs_ych11.jsonl";
const LOG = process.env.YCH11_LOG || "/home/z/my-project/data/ych11_sb1/llm_repair_ych11.log";

// pass-2 targets: audit residuals that are NOT genuine chemistry vocabulary
const RETRY_IDS = [
  "ych1_v1_u6_c21_pdf172_0960",
  "ych1_v1_u10_c0_pdf313_1702",
];

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

const LINE_STRICT = `\n\nCRITICAL EXTRA RULE: keep EVERY line break exactly as in the\ninput. Do not merge, split, join or reorder lines. Same number of lines in,\nsame number out. This overrides any urge to reflow paragraphs.`;

const SYSTEM = `You are an OCR/layout-parser repair tool for a scanned International A-level chemistry textbook.
You receive ONE chunk of parsed text that still contains transcription errors.
The dominant error on this scan is DROPPED SPACES between words
("therelationshipbetween" -> "the relationship between", "PearsonEdexcel" ->
"Pearson Edexcel", "tcomeswith" -> "It comes with" when the missing letter is
clear from context, "CRITICALTHINKING" -> "CRITICAL THINKING",
"2NaClt2H2O" -> "2NaCl + H2O" stays verbatim, "LEARNINGOBJECTIVES" ->
"LEARNING OBJECTIVES").
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
   (g dm⁻³, mol dm⁻³, kJ mol⁻¹, °C, ⇌, →, ΔH, Aᵣ, Mᵣ, H₂O, CO₂, SO₄²⁻,
   Na⁺, CH₃, ×10²³, ½). Never convert them to ASCII or remove them. Keep
   chemical equations (including state symbols like (s)/(l)/(g)/(aq) and the
   reversible arrow ⇌) EXACTLY as given.
5. Keep question numbering as printed ("1 a", "2 b ii", "(a)") and keep table
   cell values aligned to their pipes.
6. Output ONLY the corrected text. No commentary, no markdown fences, no explanations.`;

const UNICHARS = /[₀-₉⁰¹²³⁴-⁹⁺⁻°×μΩ·⇌→Δ½↔]/g;

function lcsRatio(a, b) {
  const A = a.replace(/\s+/g, "");
  const B = b.replace(/\s+/g, "");
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
  if (t.length < original.length * 0.6) return null;
  if (t.length > original.length * 1.7) return null;
  if (/i cannot|unable to|as an ai/i.test(t.slice(0, 80))) return null;
  const oLines = original.split("\n"), rLines = t.split("\n");
  if (original.includes("|")) {
    if (oLines.length !== rLines.length) return null;
    for (let i = 0; i < oLines.length; i++) {
      if ((oLines[i].match(/\|/g) || []).length !== (rLines[i].match(/\|/g) || []).length)
        return null;
    }
  } else {
    if (lcsRatio(original, t) < 0.97) return null;
  }
  const oc = (original.match(UNICHARS) || []).length;
  const rc = (t.match(UNICHARS) || []).length;
  if (rc < oc) return null;
  return t;
}

async function main() {
  const chunks = new Map();
  for (const line of fs.readFileSync(ZJSONL, "utf-8").split("\n")) {
    if (!line.trim()) continue;
    const c = JSON.parse(line);
    chunks.set(c.id, c);
  }
  const zai = await (require("z-ai-web-dev-sdk").default).create();
  for (const id of RETRY_IDS) {
    const chunk = chunks.get(id);
    if (!chunk) { log(`SKIP ${id}: not in corpus`); continue; }
    const body = chunk.text;
    try {
      const completion = await withTimeout(zai.chat.completions.create({
        messages: [
          { role: "assistant", content: SYSTEM + LINE_STRICT },
          { role: "user", content: body },
        ],
        thinking: { type: "disabled" },
      }), 120000, "pass2");
      const raw = completion.choices?.[0]?.message?.content || "";
      const cleaned = sanityCheck(body, raw);
      if (cleaned === null) {
        log(`PASS2 MISS ${id}: sanity check failed -> pass-1 record stands (nothing appended)`);
        continue;
      }
      if (cleaned === body.trim()) {
        log(`PASS2 NOOP ${id}: model returned input unchanged -> nothing appended`);
        continue;
      }
      fs.appendFileSync(OUT, JSON.stringify({ id, status: "ok", text: cleaned, pass2: true }) + "\n");
      log(`PASS2 OK ${id}: appended improved repair record (${body.length} -> ${cleaned.length} chars)`);
    } catch (e) {
      log(`PASS2 ERR ${id}: ${e.message} -> pass-1 record stands (nothing appended)`);
    }
  }
}

main().catch(e => { console.error("FATAL", e.message); log("FATAL " + e.message); process.exit(1); });
