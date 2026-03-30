# Ticketing / support example

A **Next.js** app pattern for **customer support**: end users **create and track tickets**, support **agents** manage a queue (status, assignment, notes)—with **mock** users, roles, and ticket data unless you plug in real auth or APIs.

## What you get

- **User dashboard:** list/create tickets, view status and history for the signed-in user.
- **Agent dashboard:** queue or list, filters, workflows to update tickets.
- Role separation (`user` vs `agent`) with route protection (middleware or server checks) even when persistence is mocked.
- [`AGENTS.md`](./AGENTS.md) + [**web-developer** skill](../.cursor/skills/web-developer/SKILL.md); Phase 6 should add Mermaid for ticket lifecycle and roles.

## Prerequisites

- **Node.js** (LTS, e.g. 20.x) and **npm**, **pnpm**, or **yarn**
- **Cursor** and/or **Claude** for the agent workflow (optional)

## Open the right folder

Use **`examples/web/ticketing-site/`** as the **workspace root** so shared Cursor skills under `examples/web/.cursor/` resolve via `../.cursor/`.

## Using an AI agent

1. Open this directory as the project root.
2. **Cursor:** [`AGENTS.md`](./AGENTS.md) and the [web-developer skill](../.cursor/skills/web-developer/SKILL.md).
3. **Claude:** project instructions from [`AGENTS.md`](./AGENTS.md) plus the same skill file path as above.

If there is no Next.js app yet, the skill’s **Phase 1** describes scaffolding and setup.

## Run the app (after `package.json` exists)

```bash
npm install
npm run dev
```

Use the scripts in **`package.json`**. Avatars, attachments, and help media must not 404—see the **Images and video** section of the web-developer skill.

## Collective docs

- [Repository README](../../../README.md) · [CONTRIBUTING](../../../CONTRIBUTING.md) · [Root AGENTS](../../../AGENTS.md)
