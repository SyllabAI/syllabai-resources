#!/bin/bash
# wave6 pre-flight: schema + lint per layer
N="$1"
node -e "
const fs = require('fs');
const Ajv = require('/home/z/node_modules/ajv');
const schema = JSON.parse(fs.readFileSync('/home/z/my-project/scripts/guided-lesson.0.1.schema.json', 'utf8'));
const ajv = new Ajv({ allErrors: true, strict: false });
const layer = JSON.parse(fs.readFileSync('/home/z/my-project/.tmp/wave6/layer-' + process.argv[1] + '.json', 'utf8'));
const v = ajv.compile(schema);
const ok = v(layer);
console.log('SCHEMA:', ok ? 'PASS' : 'FAIL ' + JSON.stringify(v.errors, null, 1));
process.exit(ok ? 0 : 1);
" "$N" && node /home/z/my-project/scripts/a1-lint.js /home/z/my-project/.tmp/wave6/layer-"$N".json --note "$N"
