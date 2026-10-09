# unghosted website

Landing page for unghosted, the care app for people who live with a ghost.
Built from the Figma frame "Landing / Desktop v2 (styled)".

Plain HTML, CSS and JS. No build step.

```
python3 -m http.server 8765
```
Open http://localhost:8765 and click once to wake the sound.

## Experience
- Flashlight veil: 10% black overlay (`--veil` in styles.css) with a soft circle around the cursor (`--torch`) that masks it out.
- Subtle motion: scroll reveals, flickering headlines, floating and parallax ghost prints, tilt on feature phones, film grain.
- Sound, synthesized with the Web Audio API: "boooo" on buttons, door creaks on links and FAQ, whispers on photo hover, soft wind, an occasional answer when idle. Toggle in the nav.
