#!/usr/bin/env node
// wave3-schema-check.js — standalone pre-flight schema validation (ajv draft-07, additionalProperties
// false) for authored layer working copies, run BEFORE the harness export so a schema fail never
// touches the append-only event logs (single-export discipline).
// Usage: node scripts/wave3-schema-check.js <layer1.json> [layer2.json ...]
const fs = require('fs');
const Ajv = require('/home/z/node_modules/ajv');
const schema = JSON.parse(fs.readFileSync('/home/z/my-project/scripts/guided-lesson.0.1.schema.json', 'utf8'));
const ajv = new Ajv({ allErrors: true, strict: false });
const validate = ajv.compile(schema);
let fails = 0;
for (const f of process.argv.slice(2)) {
  const layer = JSON.parse(fs.readFileSync(f, 'utf8'));
  const ok = validate(layer);
  console.log(`SCHEMA ${f}: ${ok ? 'PASS' : 'FAIL'}`);
  if (!ok) {
    fails++;
    console.log(JSON.stringify(validate.errors, null, 1));
  }
}
process.exit(fails ? 1 : 0);
