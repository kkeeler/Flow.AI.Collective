# Photography site example

A **Next.js** site for **photography services**: public **portfolio / galleries** with real working images, plus two mocked roles:

- **Client:** log in and **view** photos shared with them (galleries or albums).
- **Photographer:** log in and **upload** photos for a client (mock storage unless you specify otherwise).

## What you get

- Heavy emphasis on **media that loads**: galleries, client views, and any video need valid paths (`public/` or allowlisted remotes in `next.config`); use fallbacks where mock URLs might fail.
- **Mock auth** and **mock persistence** (in-memory, JSON, or a simple dev store) unless you provide real providers—see [`AGENTS.md`](./AGENTS.md) and [**web-developer** skill](../.cursor/skills/web-developer/SKILL.md) Phase 6 for documented roles and sessions.
- Secure patterns for forms and sessions even with mocks, so swapping in a real backend is easier later.

## Prerequisites

- **Node.js** (LTS, e.g. 20.x) and **npm**, **pnpm**, or **yarn**
- **Cursor** and/or **Claude** for the agent workflow (optional)

## Open the right folder

Use **`examples/web/photography-site/`** as the **workspace root** so `../.cursor/skills/web-developer/` resolves correctly.

## Using an AI agent

1. Open this directory as the project root.
2. **Cursor:** [`AGENTS.md`](./AGENTS.md) and the [web-developer skill](../.cursor/skills/web-developer/SKILL.md).
3. **Claude:** add [`AGENTS.md`](./AGENTS.md) to project instructions and include the web-developer skill from `examples/web/.cursor/skills/web-developer/SKILL.md`.

Scaffolding, sample assets under `public/`, and smoke-testing client vs photographer views are part of the guided workflow.

## Run the app (after `package.json` exists)

```bash
npm install
npm run dev
```

Align with your chosen package manager. Do not commit storage credentials or API keys—use **`.env.local`** only.

## Collective docs

- [Repository README](../../../README.md) · [CONTRIBUTING](../../../CONTRIBUTING.md) · [Root AGENTS](../../../AGENTS.md)
