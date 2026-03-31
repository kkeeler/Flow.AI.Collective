# Contributing to flow.ai.collective

Thanks for helping the collective stay useful, honest, and easy to follow. This document is the contract for how we add and change content.

---

## GitHub workflow: fork and pull request

We use the **standard GitHub fork workflow**. You do not need direct write access to the upstream repository to contribute.

1. **Fork** the upstream repository on GitHub (your account gets a copy under `github.com/<you>/flow.ai.collective` or similar).
2. **Clone your fork** locally and enter the repo:
   ```bash
   git clone https://github.com/<your-username>/<fork-name>.git
   cd <fork-name>
   ```
3. **Add the upstream remote** (the canonical collective repo) so you can stay in sync:
   ```bash
   git remote add upstream https://github.com/<upstream-org-or-user>/<repo-name>.git
   ```
   Use `git remote -v` to confirm `origin` points at your fork and `upstream` at the main repo.
4. **Sync before you branch** (replace `main` if the default branch has another name):
   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main
   ```
   Alternatively, use **GitHub’s “Sync fork”** on your fork, then `git pull origin main`.
5. **Create a branch** for your change:
   ```bash
   git checkout -b feat/short-description
   ```
6. **Commit** using [Conventional Commits](#commits-conventional-commits) (see below).
7. **Push to your fork**:
   ```bash
   git push -u origin feat/short-description
   ```
8. On GitHub, open a **pull request** from your fork’s branch into the **upstream** default branch. Fill in the PR template and link any related issue.

**Keeping a long-running fork updated:** repeat step 4 (fetch/merge `upstream/main` into your local `main`, or rebase your topic branch onto `upstream/main`) before opening or updating a PR so reviews see a clean diff.

**Maintainers** with write access to the upstream repo may push a branch there and open a PR without a fork; the same commit message and review expectations still apply.

---

## Commits: Conventional Commits

Use [Conventional Commits](https://www.conventionalcommits.org/) so history stays scannable:

- `feat:` — new capability or example  
- `fix:` — bug fix  
- `docs:` — documentation only  
- `chore:` — tooling, config, housekeeping  

Optional scope (recommended for this repo):

- `docs(examples):` — example README / agent docs  
- `feat(presentations):` — presentations example  
- `feat(web):` — web examples  

**Examples:** `docs: add root README`, `feat(web): add ticketing-site scaffold`.

---

## Examples must be self-contained

Each example under `examples/` should include everything a newcomer needs:

- A **README** with purpose, layout, and **install / run** steps  
- An **`AGENTS.md`** (or equivalent) when the workflow is agent-driven  
- A **`.gitignore`** that excludes generated junk (`node_modules/`, `venv/`, build artifacts, local outputs—follow patterns in sibling examples)  
- **Dependencies** listed explicitly (e.g. `package.json`, `requirements.txt`, or documented `pip install` lines)

Do **not** rely on undocumented paths outside the example unless you **document** that dependency in the example README.

---

## Cursor and Claude

Examples today are authored primarily for **Cursor** (`.cursor/skills/`, per-example `AGENTS.md`).

**Contributors must:**

1. **Keep Cursor paths working** — skills and rules should resolve when the example folder is the project root (or as documented).  
2. **Document Claude usage** in the example README when instructions are Cursor-specific: e.g. point Claude users to paste **`AGENTS.md`** into project instructions, or summarize the same workflow in plain steps.  
3. **Add a `CLAUDE.md`** only when it meaningfully improves parity (validated workflow, duplicated critical rules). Don’t add empty stubs.

If you validate an example with Claude, mention that in the PR description.

---

## Update documentation when you change behavior

When you add or change an example:

- Update the example’s **README** and **`AGENTS.md`** / **skills** as needed  
- Update the **root [README.md](README.md)** if the public “examples index” or setup story changes  
- Keep cross-links between docs accurate (relative paths preferred)

---

## Assets

- **Shared** images and media → [`assets/`](assets/)  
- **Example-only** assets stay inside that example (e.g. `public/`) unless you intentionally promote them to `assets/`  
- Reference images in markdown with **repo-relative** paths (e.g. `assets/foo.png`)

---

## Do not commit

- Anything under **`build/`** except **`build/.gitkeep`** — that folder is local scratch (see root [AGENTS.md](AGENTS.md))  
- Generated or vendor dirs already covered by each example’s `.gitignore`

---

## Questions?

Open a discussion or issue on the repo (if enabled), or refer to [AGENTS.md](AGENTS.md) for how agents should navigate the tree.
