# Agent instructions: flow.ai.collective (repository root)

This file is for **any AI agent** (or human) using this monorepo. It defines **where to work** and **repo-wide rules**. It does **not** replace per-example agent docs—those stay next to each workflow.

---

## Scope of this file

| Topic | Where to look |
|--------|----------------|
| Repo layout, scratch folder, choosing an example | **This file** |
| How to build a deck, a Next.js site, etc. | The **example’s** `AGENTS.md` and its `.cursor/skills/` |

---

## Choosing an example (required)

Always treat **one example directory** as your working context so paths and Cursor config resolve:

- **Presentations (PowerPoint pipeline):** `examples/presentations/` — read `AGENTS.md` and `.cursor/skills/ppt-creator/SKILL.md`  
- **Web (Next.js templates):** `examples/web/<site-name>/` — read that folder’s `AGENTS.md` and `examples/web/.cursor/skills/web-developer/SKILL.md`

Open or `cd` into that folder before creating files, running installs, or editing skills.

---

## The `build/` folder (scratch only)

- **Use `build/`** for disposable output: experiments, temporary clones, zip exports, scratch scripts, anything you do not want in version control.  
- **Do not commit** contents of `build/`. The repository root `.gitignore` ignores `build/*` except `build/.gitkeep`.  
- **Do not** put canonical deliverables here. Example outputs belong under the relevant `examples/...` path per that example’s README (e.g. presentation `.pptx` under the presentations example’s documented output folder).

---

## Shared assets

Collective-wide images and media live in **`assets/`**. Keep example-specific media inside the example unless it is intentionally promoted to `assets/`.

---

## Creating a new example (checklist)

1. Add **`examples/<category>/<name>/`** (e.g. `examples/web/my-app/`).  
2. Add a **README** with purpose, prerequisites, install, and run.  
3. Add **`AGENTS.md`** if agents are expected to follow a workflow.  
4. Add **`.gitignore`** for generated files; mirror sibling examples where it makes sense.  
5. Add **Cursor** skills or rules under `.cursor/` as needed; keep paths valid when the example root is the workspace.  
6. **Document Claude** in the README (and add **`CLAUDE.md`** only if it adds real value).  
7. Link the new example from the root **README.md** and follow **[CONTRIBUTING.md](CONTRIBUTING.md)** (conventional commits, doc updates).

---

## Summary

- [ ] Correct example folder is the active workspace  
- [ ] Example `AGENTS.md` + skills read before implementing  
- [ ] `build/` used only for scratch; nothing committed there  
- [ ] Deliverables live under `examples/...` per that example’s docs  
