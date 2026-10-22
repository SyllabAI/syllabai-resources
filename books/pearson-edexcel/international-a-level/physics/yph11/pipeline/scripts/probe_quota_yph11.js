// One-shot quota probe for the z-ai gateway (PM-3 lean probe).
const ZAI = require('z-ai-web-dev-sdk').default;

async function main() {
  try {
    const zai = await ZAI.create();
    const completion = await Promise.race([
      zai.chat.completions.create({
        messages: [{ role: 'user', content: 'Reply with the single word: ok' }],
        max_tokens: 5,
      }),
      new Promise((_, rej) => setTimeout(() => rej(new Error('timeout 45s')), 45000)),
    ]);
    const txt = (completion.choices[0]?.message?.content || '').trim();
    console.log('PROBE_OK', JSON.stringify(txt.slice(0, 40)));
    process.exit(0);
  } catch (e) {
    const msg = String(e && e.message || e).slice(0, 160);
    if (/429|quota|rate/i.test(msg)) {
      console.log('PROBE_429', msg);
    } else {
      console.log('PROBE_ERR', msg);
    }
    process.exit(2);
  }
}
main();
