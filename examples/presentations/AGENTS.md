# Agent instructions: AI-generated PowerPoint presentations

This repository demonstrates using AI to produce polished, animated `.pptx` decks. Agents must follow the **ppt-creator** skill (`.cursor/skills/ppt-creator/SKILL.md`) for the HTML/CSS → Playwright → python-pptx workflow, critical rules, and script templates.

## When the user asks for a presentation

1. **Read the skill first** — Open `.cursor/skills/ppt-creator/SKILL.md` and use its setup, workflow, file structure, and reference paths (`scripts/`, `references/`) under that skill folder.

2. **Theme and visuals — ask explicitly (required)**  
   Before designing slides, ask the user clearly, in your own words:
   - Whether they have **example images** (brand screenshots, mood boards, logos, palette references, or style samples) they want you to use as the **visual theme** for the deck, **or**
   - Whether they prefer you to **propose a theme** (colors, typography, and imagery style) with no reference images.  
   Do not skip this question. If they provide images or links, incorporate that direction into the HTML/CSS. If they decline, choose a coherent theme that fits the topic and audience they described.

3. **Clarify the prompt** — Confirm topic, audience, approximate slide count (or outline), tone, and any must-have sections. If the request is vague, propose a short outline and get agreement before building.

4. **Output location and naming** — All finished `.pptx` files must be written under the repository’s **`presentations/`** directory (create the folder if it does not exist).  
   **Filename:** derive a safe file name from the deck **title** (e.g. `Q1-Product-Roadmap.pptx`). Use letters, numbers, spaces as hyphens, and avoid path characters or reserved names. The stem should match the presentation title the user asked for.

5. **Implementation** — Build `slides.html` (and supporting assets) for the deck, run capture and build steps per the skill (copy or adapt `scripts/capture_slides.py` and `scripts/build_pptx.py` from the skill). Keep intermediate artifacts (e.g. `screenshots/`, HTML) alongside the deck or in a subfolder under `presentations/` named after the same title slug so outputs stay organized.

6. **Verification** — Follow the skill’s verification guidance (e.g. open the `.pptx` in PowerPoint without repair prompts).

## Summary checklist

- [ ] Theme question asked: user images vs. agent-proposed theme  
- [ ] ppt-creator skill followed  
- [ ] Output: `presentations/<Title-Based-Name>.pptx`  
- [ ] Output verified as usable in PowerPoint
