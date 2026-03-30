---
name: pptx-animations
description: Create polished, animated PowerPoint presentations using HTML/CSS as the design layer, Playwright for screenshot capture, and python-pptx for assembly. Use when asked to build a presentation, create animated slides, generate a PPTX from HTML, or add click-to-advance animations to PowerPoint.
---

# Animated PPTX from HTML/CSS

Build presentations by designing slides in HTML/CSS, capturing screenshots with Playwright, and assembling into `.pptx` with click-to-advance animations via python-pptx.

## Setup

```bash
python -m venv venv && source venv/bin/activate
pip install playwright python-pptx lxml Pillow
playwright install chromium
```

## Workflow

### 1. Design slides in a single HTML file

Each slide is a `<div>` at 1920×1080. Use `data-step` attributes on elements that should appear on click.

```html
<div class="slide s1">
  <h1>Title</h1>
  <div class="card" data-step="1">Appears on click 1</div>
  <div class="card" data-step="2">Appears on click 2</div>
</div>
```

```css
.slide { width: 1920px; height: 1080px; position: relative; overflow: hidden; }
[data-step] { opacity: 0; transition: all 0.4s ease; }
[data-step].show { opacity: 1; }
```

Add a JS click handler that increments a counter and adds `.show` to elements where `data-step <= counter`.

### 2. Capture screenshots with Playwright

Run `scripts/capture_slides.py` (adapt selectors and step counts to your HTML).

- **Static slides**: Reveal all `data-step` elements, screenshot once.
- **Animated slides**: Click once per step, screenshot after each click. Each screenshot is a full frame of the slide at that animation state.

Key settings: `viewport: 1920×1080`, `device_scale_factor: 2` for retina quality.

### 3. Assemble PPTX with python-pptx

Run `scripts/build_pptx.py` (adapt slide list to your screenshots).

- **Static slides**: One full-bleed image per slide.
- **Animated slides**: Layer all step screenshots on the same slide at position `(0,0)`, full slide size. Then inject animation XML so each click fades in the next layer.

The animation XML template is in `references/animation-xml.md`. Each `<p:par>` block = one click. The `spid` must match each layered image's `shape_id`.

## Critical Rules

1. **Never use `deepcopy` to clone shapes between slides** — it creates broken XML references that corrupt the file. Always use `slide.shapes.add_picture(io.BytesIO(blob), ...)` instead.
2. **When removing slides programmatically**, orphaned `.xml` files remain in the ZIP. Fix by extracting the ZIP, deleting orphaned `slideN.xml` files and their references in `presentation.xml.rels` and `[Content_Types].xml`, then repacking.
3. **Always verify** the output opens in PowerPoint without repair prompts.
4. **EMU conversions**: 914400 EMU = 1 inch. Use `pptx.util.Inches()` or `pptx.util.Emu()`.
5. **Speaker notes for animated slides** should include `[Click N]` markers so the presenter knows what to say at each animation step.
6. **Slide dimensions**: `prs.slide_width = Inches(13.333)`, `prs.slide_height = Inches(7.5)` for standard 16:9 widescreen.

## File Structure

```
project/
├── slides.html           # All slide designs
├── capture_slides.py     # Playwright capture (copy from scripts/)
├── build_pptx.py         # PPTX assembly (copy from scripts/)
├── screenshots/          # Generated PNGs
└── output.pptx           # Final deck
```

## Reference Files

- `references/animation-xml.md` — The PowerPoint XML template for click-to-advance animations
- `scripts/capture_slides.py` — Template Playwright capture script
- `scripts/build_pptx.py` — Template python-pptx assembly script with static + animated slide support
