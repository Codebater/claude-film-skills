#!/usr/bin/env node
// motion-ui-video recorder
// Deterministic virtual-time frame capture of a React/motion scene + ffmpeg assembly.
//
// usage: node record.mjs <scene.video.json> [--capture-only] [--assemble-only] [--keep-server]
//
// The page clock (rAF, performance.now, Date.now, timers, WAAPI) is patched via
// addInitScript BEFORE any page script runs; each output frame advances the clock
// by exactly 1000/fps ms. Machine load never affects timing.

import { execFileSync, spawn } from 'node:child_process';
import { createRequire } from 'node:module';
import fs from 'node:fs';
import path from 'node:path';
import http from 'node:http';

const args = process.argv.slice(2);
const cfgPath = args.find((a) => !a.startsWith('--'));
if (!cfgPath) {
  console.error('usage: node record.mjs <scene.video.json> [--capture-only|--assemble-only] [--keep-server]');
  process.exit(1);
}
const flags = new Set(args.filter((a) => a.startsWith('--')));
const cfgDir = path.dirname(path.resolve(cfgPath));
const cfg = JSON.parse(fs.readFileSync(cfgPath, 'utf8'));

const fps = cfg.fps ?? 30;
const seconds = cfg.seconds ?? 8;
const totalFrames = Math.round(fps * seconds);
const vw = cfg.viewport?.width ?? 1280;
const vh = cfg.viewport?.height ?? 720;
const dsf = cfg.deviceScaleFactor ?? 2;
const url = cfg.url ?? 'http://localhost:3998';
const name = cfg.name ?? 'scene';
const outDir = path.resolve(cfgDir, cfg.outDir ?? 'out');
const framesDir = path.join(outDir, 'frames');
const dt = 1000 / fps;

// resolve playwright from the scene project (template lists it), falling back
// to anything reachable from this script's location
function loadChromium() {
  for (const base of [path.join(cfgDir, 'package.json'), import.meta.url]) {
    try { return createRequire(base)('playwright').chromium; } catch { /* try next */ }
  }
  throw new Error('playwright not found — run "npm install" in the scene project (template includes it), then "npx playwright install chromium" once.');
}

// ---------- easings ----------
const EASE = {
  linear: (t) => t,
  in: (t) => t * t,
  out: (t) => 1 - (1 - t) * (1 - t),
  inOut: (t) => (t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2),
};

// ---------- dev server management ----------
async function urlUp(u) {
  return new Promise((resolve) => {
    const req = http.get(u, (res) => { res.resume(); resolve(true); });
    req.on('error', () => resolve(false));
    req.setTimeout(2000, () => { req.destroy(); resolve(false); });
  });
}

let serverProc = null;
async function ensureServer() {
  if (await urlUp(url)) return;
  console.log(`[server] ${url} down — starting "npm run dev" in ${cfgDir}`);
  serverProc = spawn('npm', ['run', 'dev'], { cwd: cfgDir, shell: true, stdio: 'ignore', detached: false });
  for (let i = 0; i < 60; i++) {
    await new Promise((r) => setTimeout(r, 1000));
    if (await urlUp(url)) { console.log('[server] up'); return; }
  }
  throw new Error(`dev server did not come up at ${url} within 60s`);
}
function stopServer() {
  if (!serverProc || flags.has('--keep-server')) return;
  try {
    if (process.platform === 'win32') execFileSync('taskkill', ['/pid', String(serverProc.pid), '/T', '/F'], { stdio: 'ignore' });
    else serverProc.kill('SIGTERM');
  } catch { /* already gone */ }
}

// ---------- virtual time init script (runs in page before any page JS) ----------
function vtimeScript(cursorEnabled) {
  return `(() => {
  if (window.__vt) return;
  let now = 0;
  const rafQ = new Map(); let rafId = 1;
  const timers = new Map(); let timerId = 1e6; // high ids: never collide with real ones from before patch
  const waapiOffsets = new WeakMap();

  performance.now = () => now;
  Date.now = () => now;
  window.requestAnimationFrame = (cb) => { const id = rafId++; rafQ.set(id, cb); return id; };
  window.cancelAnimationFrame = (id) => { rafQ.delete(id); };
  window.setTimeout = (cb, delay = 0, ...a) => {
    if (typeof cb !== 'function') return timerId++;
    const id = timerId++; timers.set(id, { at: now + Math.max(0, +delay || 0), cb: () => cb(...a), every: null });
    return id;
  };
  window.setInterval = (cb, every = 0, ...a) => {
    if (typeof cb !== 'function') return timerId++;
    const id = timerId++; const e = Math.max(1, +every || 1);
    timers.set(id, { at: now + e, cb: () => cb(...a), every: e });
    return id;
  };
  window.clearTimeout = (id) => { timers.delete(id); };
  window.clearInterval = (id) => { timers.delete(id); };

  window.__vt = {
    now: () => now,
    step(ms) {
      const target = now + ms;
      // fire due timers in chronological order (may schedule more)
      for (let guard = 0; guard < 10000; guard++) {
        let bestId = null, bestAt = Infinity;
        for (const [id, t] of timers) if (t.at <= target && t.at < bestAt) { bestAt = t.at; bestId = id; }
        if (bestId === null) break;
        const t = timers.get(bestId);
        now = Math.max(now, t.at);
        if (t.every) t.at = t.at + t.every; else timers.delete(bestId);
        try { t.cb(); } catch (e) { console.error('[vt timer]', e); }
      }
      now = target;
      // flush rAF callbacks queued as of this frame
      const cbs = [...rafQ.values()]; rafQ.clear();
      for (const cb of cbs) { try { cb(now); } catch (e) { console.error('[vt raf]', e); } }
      // seek WAAPI/CSS animations against the virtual clock
      try {
        for (const a of document.getAnimations()) {
          if (!waapiOffsets.has(a)) waapiOffsets.set(a, now);
          try { a.pause(); a.currentTime = Math.max(0, now - waapiOffsets.get(a)); } catch {}
        }
      } catch {}
    },
  };

  ${cursorEnabled ? `
  // visible cursor dot driven by real mouse events
  addEventListener('DOMContentLoaded', () => {
    const dot = document.createElement('div');
    dot.id = '__cursor';
    dot.style.cssText = 'position:fixed;left:0;top:0;width:22px;height:22px;border-radius:50%;' +
      'background:rgba(255,255,255,.95);box-shadow:0 0 0 1.5px rgba(0,0,0,.55),0 4px 14px rgba(0,0,0,.45);' +
      'pointer-events:none;z-index:2147483647;transform:translate(-50%,-50%) scale(1);will-change:transform;' +
      'opacity:0;';
    document.body.appendChild(dot);
    let scale = 1;
    const place = (e) => { dot.style.opacity = '1'; dot.style.transform = 'translate(' + (e.clientX) + 'px,' + (e.clientY) + 'px) translate(-50%,-50%) scale(' + scale + ')'; dot.__x = e.clientX; dot.__y = e.clientY; };
    addEventListener('mousemove', place, true);
    addEventListener('mousedown', (e) => { scale = 0.72; place(e); }, true);
    addEventListener('mouseup', (e) => { scale = 1; place(e); }, true);
  });` : ''}
})();`;
}

// ---------- beat plan: expand config beats into per-frame actions ----------
// beat: { at, action: move|hover|click|dblclick|type|press|scroll|wait,
//         selector?, to?: [x,y], over?, text?, key?, by? }
function buildPlan() {
  const perFrame = new Map(); // frame -> [async fn(page, state)]
  const add = (f, fn) => {
    const k = Math.max(0, Math.min(totalFrames - 1, Math.round(f)));
    if (!perFrame.has(k)) perFrame.set(k, []);
    perFrame.get(k).push(fn);
  };

  const resolvePoint = async (page, beat) => {
    if (beat.to) return { x: beat.to[0], y: beat.to[1] };
    const el = page.locator(beat.selector).first();
    const box = await el.boundingBox();
    if (!box) throw new Error(`beat selector not found/visible: ${beat.selector}`);
    return { x: box.x + box.width / 2, y: box.y + box.height / 2 };
  };

  for (const beat of cfg.beats ?? []) {
    const startF = beat.at * fps;
    const action = beat.action ?? 'move';

    if (action === 'move' || action === 'hover' || action === 'click' || action === 'dblclick') {
      // cursor flight: eased, slightly arced path spread across frames
      const over = beat.over ?? 0.6;
      const nSteps = Math.max(1, Math.round(over * fps));
      add(startF, async (page, state) => {
        const to = await resolvePoint(page, beat);
        const from = state.pos ?? { x: vw / 2, y: vh + 30 };
        state.flight = { from, to, start: state.frame, n: nSteps };
      });
      for (let i = 1; i <= nSteps; i++) {
        add(startF + i, async (page, state) => {
          if (!state.flight) return;
          const { from, to, n } = state.flight;
          const t = EASE[beat.ease ?? 'inOut'](Math.min(1, i / n));
          // quadratic arc: bow perpendicular to the path
          const mx = (from.x + to.x) / 2 + (to.y - from.y) * 0.12;
          const my = (from.y + to.y) / 2 - (to.x - from.x) * 0.12;
          const x = (1 - t) * (1 - t) * from.x + 2 * (1 - t) * t * mx + t * t * to.x;
          const y = (1 - t) * (1 - t) * from.y + 2 * (1 - t) * t * my + t * t * to.y;
          await page.mouse.move(x, y);
          state.pos = { x, y };
          if (i === n) state.flight = null;
        });
      }
      if (action === 'click' || action === 'dblclick') {
        const downF = startF + nSteps + Math.round(0.08 * fps);
        add(downF, async (page) => { await page.mouse.down(); });
        add(downF + Math.round(0.12 * fps), async (page) => { await page.mouse.up(); });
        if (action === 'dblclick') {
          add(downF + Math.round(0.2 * fps), async (page) => { await page.mouse.down(); });
          add(downF + Math.round(0.3 * fps), async (page) => { await page.mouse.up(); });
        }
      }
    } else if (action === 'type') {
      // spread keystrokes across `over` seconds so typing is visible
      const text = beat.text ?? '';
      const over = beat.over ?? Math.min(2, text.length * 0.06);
      add(startF, async (page) => { if (beat.selector) await page.locator(beat.selector).first().focus(); });
      const step = (over * fps) / Math.max(1, text.length);
      [...text].forEach((ch, i) => {
        add(startF + 1 + i * step, async (page) => { await page.keyboard.type(ch); });
      });
    } else if (action === 'press') {
      add(startF, async (page) => { await page.keyboard.press(beat.key ?? 'Enter'); });
    } else if (action === 'scroll') {
      const over = beat.over ?? 0.8;
      const n = Math.max(1, Math.round(over * fps));
      let last = 0;
      for (let i = 1; i <= n; i++) {
        const eased = EASE[beat.ease ?? 'inOut'](i / n) * (beat.by ?? 300);
        const delta = eased - last; last = eased;
        add(startF + i, async (page) => { await page.mouse.wheel(0, delta); });
      }
    } else if (action === 'eval') {
      add(startF, async (page) => { await page.evaluate(beat.js ?? ''); });
    }
  }
  return perFrame;
}

// ---------- capture ----------
async function capture() {
  fs.rmSync(framesDir, { recursive: true, force: true });
  fs.mkdirSync(framesDir, { recursive: true });

  const cursorEnabled = cfg.cursor ?? (cfg.beats?.length > 0);
  const chromium = loadChromium();
  const browser = await chromium.launch({
    headless: true,
    args: [
      '--disable-features=CalculateNativeWinOcclusion', // Windows: occlusion detection freezes rAF
      '--disable-backgrounding-occluded-windows',
      '--disable-renderer-backgrounding',
      '--disable-background-timer-throttling',
    ],
  });
  const context = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dsf,
    reducedMotion: 'no-preference',
    colorScheme: cfg.colorScheme ?? 'dark',
  });
  await context.addInitScript(vtimeScript(cursorEnabled));
  const page = await context.newPage();
  page.on('console', (m) => { if (m.type() === 'error') console.log('[page error]', m.text()); });
  page.on('pageerror', (e) => console.log('[page crash]', e.message));

  await page.goto(url, { waitUntil: 'networkidle' });
  await page.waitForFunction(() => window.__SCENE_READY === true || document.fonts.status === 'loaded', { timeout: 15000 }).catch(() => {
    console.log('[warn] __SCENE_READY never set — capturing anyway');
  });

  const plan = buildPlan();
  const state = { pos: null, flight: null, frame: 0 };
  const t0 = performance.now();

  for (let f = 0; f < totalFrames; f++) {
    state.frame = f;
    for (const fn of plan.get(f) ?? []) await fn(page, state);
    await page.evaluate((ms) => window.__vt.step(ms), dt);
    await page.screenshot({ path: path.join(framesDir, `f_${String(f).padStart(6, '0')}.png`), animations: 'allow' });
    if (f % fps === 0) process.stdout.write(`\r[capture] ${f}/${totalFrames} frames (${((performance.now() - t0) / 1000).toFixed(0)}s)`);
  }
  console.log(`\r[capture] ${totalFrames}/${totalFrames} frames done`);

  await browser.close();
  fs.writeFileSync(path.join(outDir, 'manifest.json'), JSON.stringify({ name, fps, seconds, totalFrames, vw, vh, dsf }, null, 2));
}

// ---------- assemble ----------
function assemble() {
  const outMp4 = path.join(outDir, `${name}.mp4`);
  const ffArgs = [
    '-y',
    '-framerate', String(fps),
    '-i', path.join(framesDir, 'f_%06d.png'),
    '-vf', `scale=${vw}:${vh}:flags=lanczos`,
    '-c:v', 'libx264', '-crf', '18', '-preset', 'medium',
    '-pix_fmt', 'yuv420p', '-movflags', '+faststart',
    outMp4,
  ];
  console.log('[ffmpeg]', ffArgs.join(' '));
  execFileSync('ffmpeg', ffArgs, { stdio: ['ignore', 'ignore', 'inherit'] });
  console.log(`[done] ${outMp4}`);

  if (cfg.formats?.includes('webm')) {
    const outWebm = path.join(outDir, `${name}.webm`);
    execFileSync('ffmpeg', [
      '-y', '-framerate', String(fps), '-i', path.join(framesDir, 'f_%06d.png'),
      '-vf', `scale=${vw}:${vh}:flags=lanczos`,
      '-c:v', 'libvpx-vp9', '-crf', '32', '-b:v', '0', '-pix_fmt', 'yuv420p',
      outWebm,
    ], { stdio: ['ignore', 'ignore', 'inherit'] });
    console.log(`[done] ${outWebm}`);
  }
}

// ---------- main ----------
try {
  if (!flags.has('--assemble-only')) {
    await ensureServer();
    await capture();
  }
  if (!flags.has('--capture-only')) assemble();
} finally {
  stopServer();
}
