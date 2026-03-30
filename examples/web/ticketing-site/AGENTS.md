# Agent: Ticketing / support site

## Skill

Follow the phased Next.js workflow in [`../.cursor/skills/web-developer/SKILL.md`](../.cursor/skills/web-developer/SKILL.md). Treat that skill as the default process (setup, requirements, dev server, implementation, security and quality, documentation with Mermaid).

## Theme and content

If the user has **not** already provided product naming, branding, or UX preferences, ask once for a **short summarized theme** (support tone, visual style, primary user types) before building dashboards and flows.

## Product intent

Build a Next.js app for **customer support** where:

- **End users** can **create tickets** (subject, description, priority or category if useful) and track their own submissions.
- **Support agents** can **view and work on tickets** (status changes, assignment, internal notes or comments as appropriate—mock unless specified).

## Dashboards

Provide:

1. **User dashboard**: List/create tickets, view status and history for the logged-in user.
2. **Agent dashboard**: Queue or list of tickets, filters, and workflows to update tickets.

Use **mock users, roles, and ticket data** unless the user supplies schemas, APIs, or auth. Clearly label roles (e.g. `user` vs `agent`) and protect routes accordingly (middleware or server checks), even when data is mocked.

## Media (images and video)

If the UI includes **avatars, attachments, screenshots, or help videos**, ensure sources exist and match `next/image` remote config when needed. Avoid broken thumbnails on ticket lists or detail views; verify in the browser that no media requests fail.

## Documentation

Architecture diagrams (Mermaid) should show ticket lifecycle and role separation (see Phase 6 of the web-developer skill).
