# SaaS / commerce example

A **Next.js** starter for either **subscription SaaS** (plans, mock billing) or **product commerce** (mock catalog and cart)—with **sign up / log in / log out**, **cart**, and **mock payments** (no real card processing unless you wire a provider and env vars yourself).

## What you get

- Product direction clarified in [`AGENTS.md`](./AGENTS.md): B2B vs B2C, subscriptions vs storefront, simulated vs named payment provider.
- **Mock** catalog, users, orders, and subscriptions unless you specify real APIs or data.
- Build process: [**web-developer** skill](../.cursor/skills/web-developer/SKILL.md) (Phases 1–6). Phase 6 should include Mermaid for auth, cart, and checkout boundaries (mock vs future real payments).

## Prerequisites

- **Node.js** (LTS, e.g. 20.x) and **npm**, **pnpm**, or **yarn**
- **Cursor** and/or **Claude** for the agent workflow (optional if you implement manually)

## Open the right folder

Use **`examples/web/saas-site/`** as the **workspace root** so `../.cursor/skills/web-developer/` points at the shared skill under `examples/web/`.

## Using an AI agent

1. Open this directory as the project root.
2. **Cursor:** follow [`AGENTS.md`](./AGENTS.md) and the [web-developer skill](../.cursor/skills/web-developer/SKILL.md).
3. **Claude:** paste [`AGENTS.md`](./AGENTS.md) into project instructions and attach the web-developer skill from `examples/web/.cursor/skills/web-developer/SKILL.md`.

Scaffolding and dependency install are covered in the skill’s **Phase 1** if the app is not present yet.

## Run the app (after `package.json` exists)

```bash
npm install
npm run dev
```

Match commands to your lockfile (**pnpm**/**yarn** if used). **Never commit** API keys or payment provider secrets—use **`.env.local`** and document required vars in the project docs.

## Collective docs

- [Repository README](../../../README.md) · [CONTRIBUTING](../../../CONTRIBUTING.md) · [Root AGENTS](../../../AGENTS.md)
