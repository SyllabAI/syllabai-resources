#!/usr/bin/env node
/** Offline replay of the fixed sanityCheck against saved reject raws. */
const fs = require("fs");

const UNICHARS = /[₀-₉⁰¹²³⁴-⁹⁺⁻°×μΩ·]/g;

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

const chunks = new Map();
for (const line of fs.readFileSync("/home/z/my-project/download/rag_physics/edexcel_igcse_physics_chunks_v1.jsonl", "utf-8").split("\n")) {
  if (line.trim()) { const c = JSON.parse(line); chunks.set(c.id, c); }
}
const rejs = [];
for (const line of fs.readFileSync("/home/z/my-project/data/llm_repairs_physics.jsonl", "utf-8").split("\n")) {
  if (line.trim()) { const r = JSON.parse(line); if (r.status === "rejected") rejs.push(r); }
}
let pass = 0, failLen = 0, failLcs = 0, failOther = 0;
const fails = [];
for (const r of rejs) {
  const c = chunks.get(r.id);
  if (!c) { failOther++; continue; }
  const verdict = sanityCheck(c.text, r.raw || "");
  if (verdict !== null && verdict !== false) { pass++; }
  else {
    const t = (r.raw || "").trim().replace(/^```[a-z]*\n?/, "").replace(/```$/, "").trim();
    if (t.length < c.text.length * 0.6 || t.length > c.text.length * 1.7) failLen++;
    else if (c.text.includes("|")) failOther++;
    else if (lcsRatio(c.text, t) < 0.97) { failLcs++; fails.push([r.id, lcsRatio(c.text, t).toFixed(3)]); }
    else failOther++;
  }
}
console.log(`rejects replayed: ${rejs.length}  | would now PASS: ${pass}  | fail-length: ${failLen}  | fail-lcs: ${failLcs}  | other: ${failOther}`);
for (const [id, ratio] of fails) console.log(`  still-fail-lcs ${id} ratio=${ratio}`);
