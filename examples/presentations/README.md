# Presentations — AI-assisted animated PowerPoint

This repo is an **example workflow** for creating polished, animated PowerPoint decks with AI: slides are designed in **HTML/CSS**, captured with **Playwright**, and assembled into **`.pptx`** with **python-pptx** (including click-to-advance steps). Cursor agents are guided by **`AGENTS.md`** and the **ppt-creator** skill under `.cursor/skills/ppt-creator/`.

## Agents

| File | Role |
|------|------|
| **`AGENTS.md`** | Tells the AI to read the ppt-creator skill, **ask whether you have example images for the theme or it should invent one**, clarify the brief, and save every deck under **`presentations/`** with a **filename derived from the title**. |
| **`.cursor/skills/ppt-creator/SKILL.md`** | Step-by-step pipeline (HTML slides, `data-step` animations, capture script, PPTX build, XML animation rules). |

In Cursor, open the project and describe the presentation you want; the agent should follow `AGENTS.md` automatically.

## How to use

1. Clone or open this repository in Cursor.
2. Ensure **prerequisites** below are installed (Python, packages, Chromium for Playwright).
3. Prompt the agent with your topic, audience, length, and title.  
   The agent should ask: **Do you have example images to use as the visual theme, or should it propose a theme?**
4. The generated **`.pptx`** should appear in **`presentations/`**, named from your title (e.g. `Team-Offsite-2026.pptx`).

You can also follow `.cursor/skills/ppt-creator/SKILL.md` manually if you are not using an agent.

## Prerequisites

- **Python 3.10+** (recommended)
- **pip** packages: `playwright`, `python-pptx`, `lxml`, `Pillow`
- **Playwright Chromium** browser binaries (`playwright install chromium`)

## Installing prerequisites (examples)

### Windows (PowerShell)

```powershell
cd c:\Users\KKeeler\Github\cto-ppt
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install playwright python-pptx lxml Pillow
playwright install chromium
```

### macOS / Linux (bash)

```bash
cd /path/to/cto-ppt
python3 -m venv venv
source venv/bin/activate
pip install playwright python-pptx lxml Pillow
playwright install chromium
```

If `python` is not on your PATH, use `py -3 -m venv venv` on Windows or install Python from [python.org](https://www.python.org/downloads/).

## Project layout (typical)

- **`presentations/`** — Output `.pptx` files (and optionally per-deck HTML/screenshots). The folder is included here so outputs have a fixed place.
- **`.cursor/skills/ppt-creator/`** — Skill definition, `scripts/`, and `references/` for the pipeline.

For full technical detail (slide size, animation XML, pitfalls), see **`.cursor/skills/ppt-creator/SKILL.md`**.
