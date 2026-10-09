/* ghostly landing: flashlight veil, subtle motion, synthesized spooky sounds */

(() => {
  const root = document.documentElement;
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const canHover = window.matchMedia('(hover: hover)').matches;

  /* ---------- 1. Flashlight veil ----------
     A 10% black layer covers the page. Around the cursor a soft circle
     masks it out. The circle eases after the cursor and breathes a little,
     like a torch in a shaky hand. */
  const torch = { x: innerWidth / 2, y: innerHeight * 0.4, tx: innerWidth / 2, ty: innerHeight * 0.4, r: 220, tr: 220 };

  if (canHover) {
    addEventListener('pointermove', (e) => { torch.tx = e.clientX; torch.ty = e.clientY; torch.tr = 220; }, { passive: true });
    document.addEventListener('pointerleave', () => { torch.tr = 0; });
    document.addEventListener('pointerenter', () => { torch.tr = 220; });
    addEventListener('pointerdown', () => { torch.r = 300; }); // brief flare on click
  }

  let t0 = performance.now();
  function frame(now) {
    const t = (now - t0) / 1000;
    const k = reduceMotion ? 1 : 0.14;
    torch.x += (torch.tx - torch.x) * k;
    torch.y += (torch.ty - torch.y) * k;
    torch.r += (torch.tr - torch.r) * 0.08;
    const breathe = reduceMotion ? 0 : Math.sin(t * 2.1) * 6 + Math.sin(t * 7.3) * 2;
    root.style.setProperty('--x', torch.x.toFixed(1) + 'px');
    root.style.setProperty('--y', torch.y.toFixed(1) + 'px');
    root.style.setProperty('--torch', Math.max(0, torch.r + breathe).toFixed(1) + 'px');
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);

  /* ---------- 2. Reveal on scroll ---------- */
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
    });
  }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
  document.querySelectorAll('.reveal').forEach((el) => io.observe(el));

  /* ---------- 3. Hero parallax (prints and phone drift with the mouse) ---------- */
  const hero = document.querySelector('[data-parallax]');
  if (hero && canHover && !reduceMotion) {
    const layers = [...hero.querySelectorAll('[data-depth]')];
    let mx = 0, my = 0, cx = 0, cy = 0;
    addEventListener('pointermove', (e) => {
      mx = (e.clientX / innerWidth - 0.5) * 2;
      my = (e.clientY / innerHeight - 0.5) * 2;
    }, { passive: true });
    (function loop() {
      cx += (mx - cx) * 0.06; cy += (my - cy) * 0.06;
      layers.forEach((l) => {
        const d = parseFloat(l.dataset.depth);
        l.style.setProperty('--px', (cx * d * -10).toFixed(2) + 'px');
        l.style.setProperty('--py', (cy * d * -8).toFixed(2) + 'px');
      });
      requestAnimationFrame(loop);
    })();
  }

  /* ---------- 4. Tilt on feature visuals ---------- */
  if (canHover && !reduceMotion) {
    document.querySelectorAll('.tilt').forEach((el) => {
      el.addEventListener('pointermove', (e) => {
        const r = el.getBoundingClientRect();
        const x = (e.clientX - r.left) / r.width - 0.5;
        const y = (e.clientY - r.top) / r.height - 0.5;
        el.style.transform = `perspective(900px) rotateY(${x * 6}deg) rotateX(${-y * 6}deg)`;
      });
      el.addEventListener('pointerleave', () => { el.style.transform = ''; });
    });
  }

  /* ---------- 5. Sound ----------
     Everything is synthesized with the Web Audio API, no files.
     Browsers only allow audio after a click or key press, so the engine
     wakes up on the first gesture. */
  const toggle = document.querySelector('.sound-toggle');
  const toast = document.querySelector('.toast');
  let soundOn = true;
  try { soundOn = localStorage.getItem('ghostly-sound') !== 'off'; } catch (_) {}

  let ctx = null, master = null, reverb = null, wind = null;

  function makeImpulse(seconds, decay) {
    const len = ctx.sampleRate * seconds;
    const buf = ctx.createBuffer(2, len, ctx.sampleRate);
    for (let c = 0; c < 2; c++) {
      const d = buf.getChannelData(c);
      for (let i = 0; i < len; i++) d[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / len, decay);
    }
    return buf;
  }

  function noiseBuffer(seconds) {
    const len = ctx.sampleRate * seconds;
    const buf = ctx.createBuffer(1, len, ctx.sampleRate);
    const d = buf.getChannelData(0);
    for (let i = 0; i < len; i++) d[i] = Math.random() * 2 - 1;
    return buf;
  }

  function initAudio() {
    if (ctx) return;
    const AC = window.AudioContext || window.webkitAudioContext;
    if (!AC) return;
    ctx = new AC();
    master = ctx.createGain();
    master.gain.value = soundOn ? 0.9 : 0;
    master.connect(ctx.destination);

    reverb = ctx.createConvolver();
    reverb.buffer = makeImpulse(3.2, 2.6);
    const wet = ctx.createGain(); wet.gain.value = 0.55;
    reverb.connect(wet).connect(master);

    startWind();
  }

  // Bus: dry + reverb send
  function out(node, send = 0.6) {
    node.connect(master);
    const s = ctx.createGain(); s.gain.value = send;
    node.connect(s).connect(reverb);
  }

  /* The ghost voice: a buzzy source shaped into an "oo" vowel by two
     formant filters, gliding up then sagging down, with a slow wobble. */
  function boo({ dur = 2.2, base = 150, peak = 210, end = 95, vol = 0.32 } = {}) {
    if (!ctx || !soundOn) return;
    const now = ctx.currentTime;

    const src1 = ctx.createOscillator(); src1.type = 'sawtooth';
    const src2 = ctx.createOscillator(); src2.type = 'triangle'; src2.detune.value = 7;
    [src1, src2].forEach((o) => {
      o.frequency.setValueAtTime(base, now);
      o.frequency.exponentialRampToValueAtTime(peak, now + dur * 0.28);
      o.frequency.exponentialRampToValueAtTime(end, now + dur);
    });

    const vib = ctx.createOscillator(); vib.frequency.value = 5.2;
    const vibAmt = ctx.createGain(); vibAmt.gain.setValueAtTime(0, now); vibAmt.gain.linearRampToValueAtTime(7, now + dur * 0.5);
    vib.connect(vibAmt); vibAmt.connect(src1.frequency); vibAmt.connect(src2.frequency);

    const mix = ctx.createGain(); mix.gain.value = 0.5;
    src1.connect(mix); src2.connect(mix);

    // "oo" formants
    const f1 = ctx.createBiquadFilter(); f1.type = 'bandpass'; f1.frequency.value = 320; f1.Q.value = 6;
    const f2 = ctx.createBiquadFilter(); f2.type = 'bandpass'; f2.frequency.value = 800; f2.Q.value = 9;
    const g1 = ctx.createGain(); g1.gain.value = 1.0;
    const g2 = ctx.createGain(); g2.gain.value = 0.35;
    mix.connect(f1).connect(g1); mix.connect(f2).connect(g2);

    // breath
    const n = ctx.createBufferSource(); n.buffer = noiseBuffer(dur + 0.2);
    const nf = ctx.createBiquadFilter(); nf.type = 'bandpass'; nf.frequency.value = 450; nf.Q.value = 1.2;
    const ng = ctx.createGain(); ng.gain.value = 0.12;
    n.connect(nf).connect(ng);

    const lp = ctx.createBiquadFilter(); lp.type = 'lowpass'; lp.frequency.value = 1400;
    const env = ctx.createGain();
    env.gain.setValueAtTime(0.0001, now);
    env.gain.exponentialRampToValueAtTime(vol, now + 0.35);
    env.gain.setValueAtTime(vol, now + dur * 0.55);
    env.gain.exponentialRampToValueAtTime(0.0001, now + dur);

    g1.connect(lp); g2.connect(lp); ng.connect(lp);
    lp.connect(env);
    out(env, 0.9);

    [src1, src2, vib, n].forEach((o) => { o.start(now); o.stop(now + dur + 0.1); });
  }

  // Old door hinge: a slow train of clicks ringing through a resonant filter
  function creak({ dur = 0.75, vol = 0.22 } = {}) {
    if (!ctx || !soundOn) return;
    const now = ctx.currentTime;
    const pulse = ctx.createOscillator(); pulse.type = 'square';
    pulse.frequency.setValueAtTime(22, now);
    pulse.frequency.linearRampToValueAtTime(48, now + dur * 0.6);
    pulse.frequency.linearRampToValueAtTime(30, now + dur);
    const bp = ctx.createBiquadFilter(); bp.type = 'bandpass'; bp.Q.value = 14;
    bp.frequency.setValueAtTime(900, now);
    bp.frequency.linearRampToValueAtTime(1500, now + dur * 0.5);
    bp.frequency.linearRampToValueAtTime(1100, now + dur);
    const env = ctx.createGain();
    env.gain.setValueAtTime(0.0001, now);
    env.gain.exponentialRampToValueAtTime(vol, now + 0.06);
    env.gain.exponentialRampToValueAtTime(0.0001, now + dur);
    pulse.connect(bp).connect(env);
    out(env, 0.5);
    pulse.start(now); pulse.stop(now + dur + 0.05);
  }

  // Whisper: breathy noise with a moving "sss / hhh" filter
  function whisper({ dur = 0.9, vol = 0.09 } = {}) {
    if (!ctx || !soundOn) return;
    const now = ctx.currentTime;
    const n = ctx.createBufferSource(); n.buffer = noiseBuffer(dur + 0.1);
    const bp = ctx.createBiquadFilter(); bp.type = 'bandpass'; bp.Q.value = 3;
    bp.frequency.setValueAtTime(2600, now);
    bp.frequency.linearRampToValueAtTime(4800, now + dur * 0.3);
    bp.frequency.linearRampToValueAtTime(1800, now + dur);
    const env = ctx.createGain();
    env.gain.setValueAtTime(0.0001, now);
    env.gain.exponentialRampToValueAtTime(vol, now + 0.12);
    env.gain.linearRampToValueAtTime(vol * 0.4, now + dur * 0.5);
    env.gain.exponentialRampToValueAtTime(0.0001, now + dur);
    const pan = ctx.createStereoPanner ? ctx.createStereoPanner() : null;
    n.connect(bp).connect(env);
    if (pan) { pan.pan.setValueAtTime(Math.random() * 1.6 - 0.8, now); env.connect(pan); out(pan, 0.8); } else out(env, 0.8);
    n.start(now); n.stop(now + dur + 0.1);
  }

  // Soft wind that sits under the page while sound is on
  function startWind() {
    const n = ctx.createBufferSource(); n.buffer = noiseBuffer(4); n.loop = true;
    const lp = ctx.createBiquadFilter(); lp.type = 'lowpass'; lp.frequency.value = 380; lp.Q.value = 4;
    const lfo = ctx.createOscillator(); lfo.frequency.value = 0.08;
    const lfoAmt = ctx.createGain(); lfoAmt.gain.value = 180;
    lfo.connect(lfoAmt).connect(lp.frequency);
    wind = ctx.createGain(); wind.gain.value = 0.0001;
    n.connect(lp).connect(wind).connect(master);
    n.start(); lfo.start();
    wind.gain.exponentialRampToValueAtTime(0.035, ctx.currentTime + 3);
  }

  const SOUNDS = {
    'boo': () => boo(),
    'boo-short': () => boo({ dur: 1.0, base: 190, peak: 250, end: 150, vol: 0.26 }),
    'creak': () => creak(),
    'whisper': () => whisper(),
  };

  function setSound(on) {
    soundOn = on;
    try { localStorage.setItem('ghostly-sound', on ? 'on' : 'off'); } catch (_) {}
    toggle.setAttribute('aria-pressed', String(on));
    toggle.setAttribute('aria-label', on ? 'Sound on' : 'Sound off');
    toggle.querySelector('.sound-toggle__label').textContent = on ? 'Sound on' : 'Sound off';
    if (ctx) master.gain.setTargetAtTime(on ? 0.9 : 0, ctx.currentTime, 0.15);
  }
  setSound(soundOn);

  // First gesture wakes the house with a boo
  let woke = false;
  function wake(e) {
    if (woke) return;
    woke = true;
    initAudio();
    if (ctx && ctx.state === 'suspended') ctx.resume();
    toast.classList.remove('is-on');
    const target = e && e.target && e.target.closest('[data-sound], .sound-toggle');
    if (!target) setTimeout(() => boo(), 60);
  }
  addEventListener('pointerdown', wake, { capture: true });
  addEventListener('keydown', wake, { capture: true });

  if (soundOn) setTimeout(() => { if (!woke) toast.classList.add('is-on'); }, 1800);

  toggle.addEventListener('click', () => {
    initAudio();
    setSound(!soundOn);
    if (soundOn) boo({ dur: 1.0, base: 190, peak: 250, end: 150, vol: 0.22 });
  });

  // Clicks on anything with data-sound
  document.addEventListener('click', (e) => {
    const el = e.target.closest('[data-sound]');
    if (!el) return;
    initAudio();
    (SOUNDS[el.dataset.sound] || SOUNDS.boo)();
  });

  // Gentle hover whispers on the photos and products, throttled
  let lastWhisper = 0;
  document.querySelectorAll('[data-sound="whisper"]').forEach((el) => {
    el.addEventListener('pointerenter', () => {
      const now = performance.now();
      if (!ctx || now - lastWhisper < 1800) return;
      lastWhisper = now;
      whisper({ dur: 0.7, vol: 0.06 });
    });
  });

  // FAQ: creak when a question opens
  document.querySelectorAll('.faq__item').forEach((d) => {
    d.addEventListener('toggle', () => { if (d.open && woke) creak({ dur: 0.6, vol: 0.16 }); });
  });


  /* ---------- 6. Blog: reading progress + category filter ---------- */
  const bar = document.querySelector('.progress');
  if (bar) {
    const upd = () => {
      const h = document.documentElement.scrollHeight - innerHeight;
      bar.style.transform = `scaleX(${h > 0 ? Math.min(1, scrollY / h) : 0})`;
    };
    addEventListener('scroll', upd, { passive: true }); upd();
  }
  const chips = document.querySelectorAll('.chip[data-filter]');
  chips.forEach((c) => c.addEventListener('click', () => {
    chips.forEach((x) => x.classList.toggle('is-on', x === c));
    const f = c.dataset.filter;
    document.querySelectorAll('.post-card[data-cat]').forEach((card) => {
      card.classList.toggle('is-hidden', f !== 'All' && card.dataset.cat !== f);
      card.classList.add('is-in');
    });
    if (woke) whisper({ dur: 0.5, vol: 0.05 });
  }));

  // Every now and then, if you sit still, the house answers (sound on only)
  let idleTimer;
  function armIdle() {
    clearTimeout(idleTimer);
    idleTimer = setTimeout(() => {
      if (ctx && soundOn) { Math.random() < 0.5 ? boo({ dur: 2.8, base: 120, peak: 160, end: 80, vol: 0.14 }) : creak({ dur: 1.1, vol: 0.1 }); }
      armIdle();
    }, 35000 + Math.random() * 25000);
  }
  ['pointermove', 'scroll', 'keydown'].forEach((ev) => addEventListener(ev, armIdle, { passive: true }));
  armIdle();
})();
