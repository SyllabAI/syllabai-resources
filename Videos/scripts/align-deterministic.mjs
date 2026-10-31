#!/usr/bin/env node
/**
 * align-deterministic.mjs — F189 P2 (T-VIDEOMAP-P2): deterministic pre-pass.
 *
 * Scores every (lesson, spine SPEC_POINT) pair by lexical evidence and emits
 * the top candidates per lesson. This is EVIDENCE for the curation pass, not
 * the mapping itself: on this shelf Cognito's chapter numbering is its own
 * (chapters 1–11), so lesson refs must NOT be trusted against spec codes
 * (P1 tracker gap 4). The scorer therefore never looks at refs — only at
 * title / description / keyPoints token overlap against the spine statements.
 *
 * Usage: node align-deterministic.mjs [course=igcse-biology-19]
 * Output: Videos/drafts/<course>/deterministic-candidates.json
 */

import { readFileSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const VIDEOS = resolve(__dirname, "..");
const COURSE = process.argv[2] || "igcse-biology-19";

// spine of record is fetched to the drafts dir by the P2 runbook
const SPINE_PATH = join(VIDEOS, "drafts", COURSE, "spine.json");
const ENRICH_PATH = join(VIDEOS, "drafts", COURSE, "lesson-enrichment.json");

// ---------------------------------------------------------------- tokenizer
const STOP = new Set(
  ("a an the and or of to in on for with by from as is are be that this these those it its their his her " +
    "how what which when where why including include includes know understand describe explain use used using " +
    "can may might must should will would not no into onto out up down over under between among during through " +
    "such other more most some any each every than then so if because about against also only own same too very " +
    "practical investigate term terms meaning meanings role roles function functions structure structures " +
    "process processes type types level levels name names effect effects affect affects")
    .split(/\s+/)
);

function tokens(text) {
  return (text || "")
    .toLowerCase()
    .replace(/[^a-z0-9\s-]/g, " ")
    .split(/[\s-]+/)
    .map((t) => t.replace(/ies$/, "y").replace(/(ses|xes|zes|ches|shes)$/, "s").replace(/s$/, ""))
    .filter((t) => t.length > 2 && !STOP.has(t) && !/^\d+$/.test(t));
}

const bonusr = new Set(tokens("practical core investigate investigate investigation")); // practicals rarely align lexically

// ---------------------------------------------------------------- main
const spine = JSON.parse(readFileSync(SPINE_PATH, "utf8"));
const specs = spine.curriculum.nodes
  .filter((n) => n.family === "SPEC_POINT")
  .map((n) => ({ code: n.code, title: n.title, tok: new Set(tokens(n.title)) }));

const enrich = JSON.parse(readFileSync(ENRICH_PATH, "utf8"));

const lessons = enrich.lessons.map((l) => {
  const titleTok = tokens(l.h1);
  const descTok = tokens(l.description);
  const kpTok = tokens((l.keyPoints || []).join(" "));
  const lessonText = {
    title: new Set(titleTok),
    desc: new Set(descTok),
    kp: new Set(kpTok),
  };
  const scored = specs.map((sp) => {
    let s = 0;
    let hitsTitle = [];
    let hitsBody = [];
    for (const t of sp.tok) {
      if (lessonText.title.has(t)) {
        s += 3;
        hitsTitle.push(t);
      } else if (lessonText.desc.has(t)) {
        s += 2;
        hitsBody.push(t);
      } else if (lessonText.kp.has(t)) {
        s += 1;
        hitsBody.push(t);
      }
    }
    return { code: sp.code, score: s, hitsTitle, hitsBody };
  });
  scored.sort((a, b) => b.score - a.score);
  const top = scored.filter((x) => x.score > 0).slice(0, 8);
  return {
    key: l.key,
    lessonRef: l.lessonRef,
    h1: l.h1,
    primaryVideoId: l.primaryVideoId,
    candidates: top,
  };
});

const out = {
  schema: "syllabai.video-align-candidates/1",
  task: "T-VIDEOMAP-P2",
  course: COURSE,
  generatedUtc: new Date().toISOString(),
  note: "Deterministic lexical evidence only (title/description/keyPoints token overlap). Refs deliberately ignored — Cognito chapter numbering is not the spec numbering on this shelf (P1 gap 4). Feeds the curation pass; is not the mapping.",
  lessons,
};
const outPath = join(VIDEOS, "drafts", COURSE, "deterministic-candidates.json");
writeFileSync(outPath, JSON.stringify(out, null, 2) + "\n");
console.log(`wrote ${outPath}`);
const withTop = lessons.filter((l) => l.candidates.length > 0).length;
console.log(`lessons with ≥1 candidate: ${withTop}/${lessons.length}`);
