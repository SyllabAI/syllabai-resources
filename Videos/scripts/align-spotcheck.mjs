#!/usr/bin/env node
/**
 * align-spotcheck.mjs — F189 P2 gate §8.5: live spot-check.
 *
 * Picks N random mapping rows from the draft, fetches the Cognito lesson URL
 * live (identifying UA, polite delay), and asserts:
 *   1. the page still resolves (HTTP 200), and
 *   2. the recorded video id still appears in the page's payload.
 *
 * Usage: node align-spotcheck.mjs [N=5]
 */

import { readFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const VIDEOS = resolve(__dirname, "..");
const COURSE = process.argv[2] && /^\d+$/.test(process.argv[2]) ? "igcse-biology-19" : (process.argv[3] || "igcse-biology-19");
const N = parseInt(process.argv[2] || "5", 10);

const draft = JSON.parse(readFileSync(join(VIDEOS, "drafts", COURSE, "video-map.draft.json"), "utf8"));
const UA = "SyllabAI-VideoMap/1.0 (F189 P2 live spot-check; contact via github.com/SyllabAI)";

const rows = [...draft.mappings];
// deterministic-ish random sample: shuffle with a seed derived from time
for (let i = rows.length - 1; i > 0; i--) {
  const j = Math.floor(Math.random() * (i + 1));
  [rows[i], rows[j]] = [rows[j], rows[i]];
}
const sample = rows.slice(0, N);

let pass = 0;
for (const m of sample) {
  const res = await fetch(m.lessonUrl, { headers: { "user-agent": UA } });
  if (!res.ok) {
    console.log(`FAIL ${m.lessonRef} (${m.video}): HTTP ${res.status}`);
    continue;
  }
  const html = await res.text();
  const ok = html.includes(m.video);
  console.log(`${ok ? "PASS" : "FAIL"} ${m.lessonRef} → ${m.video} (${m.specs.join(",")}) ${m.confidence}`);
  if (ok) pass++;
  else console.log(`      id ${m.video} not found in live payload of ${m.lessonUrl}`);
  await new Promise((r) => setTimeout(r, 400 + Math.floor(Math.random() * 300)));
}

console.log(`\nspot-check: ${pass}/${sample.length} passed`);
process.exit(pass === sample.length ? 0 : 1);
