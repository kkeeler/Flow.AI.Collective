# Marketing site example

A **Next.js** starter pattern for **marketing services** or **product marketing**: landing pages, value props, CTAs, and social proof—with **mock** copy and media unless you supply real assets.

## What you get

- Guided build via [`AGENTS.md`](./AGENTS.md) (audience, tone, services vs product focus).
- Implementation follows the shared [**web-developer** skill](../.cursor/skills/web-developer/SKILL.md) (App Router, media that actually loads, security pass, Mermaid architecture notes).
- Out of scope by default: real CMS, live analytics, ad pixels—unless you ask.

## Prerequisites

- **Node.js** (LTS, e.g. 20.x) and **npm**, **pnpm**, or **yarn**
- **Cursor** and/or **Claude** if you want the agent-driven workflow (you can also follow the skill manually)

## Open the right folder

Use **`examples/web/marketing-site/`** as the **workspace root** in your editor so paths like `../.cursor/skills/web-developer/` resolve to the shared skill under `examples/web/`.

## Using an AI agent

1. Open this directory as the project root.
2. **Cursor:** the agent should read [`AGENTS.md`](./AGENTS.md) and the [web-developer skill](../.cursor/skills/web-developer/SKILL.md).
3. **Claude:** add [`AGENTS.md`](./AGENTS.md) to project instructions and include the same skill content (from the path above) so phases match.

The repo may ship this folder **before** a full Next.js app exists; the agent skill’s **Phase 1** covers scaffolding (e.g. `create-next-app`) and install.

## Run the app (after `package.json` exists)

```bash
npm install
npm run dev
```

Use the `dev` / `build` / `lint` scripts defined in **`package.json`** (pnpm or yarn equivalents are fine). Keep secrets in **`.env.local`** only—never commit them.

## Collective docs

- [Repository README](../../../README.md) · [CONTRIBUTING](../../../CONTRIBUTING.md) · [Root AGENTS](../../../AGENTS.md)
