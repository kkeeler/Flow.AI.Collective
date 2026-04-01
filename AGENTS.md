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

Always treat **one example directory** as your starting template so paths and config resolve:

- **Presentations (PowerPoint pipeline):** `examples/presentations/` — read `AGENTS.md` and `.cursor/skills/ppt-creator/SKILL.md`  
- **Web (Next.js templates):** `examples/web/<site-name>/` — read that folder’s `AGENTS.md` and `examples/web/.cursor/skills/web-developer/SKILL.md`

---

## Starting a new project from an example

When running from the **repository root** and creating something new based on an example:

1. **Copy** the example folder into `build/`:
   ```bash
   cp -r examples/<category>/<example-name> build/<project-name>
   ```
   For example: `cp -r examples/presentations build/my-keynote`

2. **Set `build/<project-name>/` as your working directory** (`cd build/<project-name>/`) before creating files, running installs, or editing anything.

3. **Read the copied example’s `AGENTS.md`** and any skills/config inside the copy — work entirely within the `build/` copy.

4. All generated output stays in the `build/` copy. Do **not** modify the original under `examples/`.

This keeps the `examples/` folder clean as a read-only template library while giving agents a full working copy with all config, skills, and structure intact.

---

## The `build/` folder

- **Use `build/`** as the working directory for new projects created from examples (see above) and for any other disposable output: experiments, scratch scripts, zip exports, etc.  
- **Do not commit** contents of `build/`. The repository root `.gitignore` ignores `build/*` except `build/.gitkeep`.  
- When a project in `build/` is ready to be promoted to a permanent example, follow the "Creating a new example" checklist below to move it into `examples/`.

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

- [ ] Example copied from `examples/` into `build/<project-name>/`  
- [ ] `build/<project-name>/` is the active working directory  
- [ ] Copied example’s `AGENTS.md` + skills read before implementing  
- [ ] Original `examples/` folder left unmodified  
- [ ] Nothing in `build/` committed to version control  
