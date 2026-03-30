# Agent: Photography site

## Skill

Follow the phased Next.js workflow in [`../.cursor/skills/web-developer/SKILL.md`](../.cursor/skills/web-developer/SKILL.md). Treat that skill as the default process (setup, requirements, dev server, implementation, security and quality, documentation with Mermaid).

## Theme and content

If the user has **not** already provided brand or visual direction, ask once for a **short summarized theme** before building major UI (e.g. portfolio aesthetic, light vs dark, mood, target clientele).

## Product intent

Build a Next.js site that **showcases photography services** and includes **sample photography** on the public-facing pages (galleries, categories, or featured work as appropriate).

## Media (images and video)

Photography is media-heavy: **every gallery, portfolio, and client-view image** must resolve (no 404s, no `next/image` host errors). Prefer committed samples under `public/` or a small set of allowlisted remote hosts in `next.config`. If mock uploads produce URLs, those URLs must work in dev or use a visible placeholder on `onError`. Any **video** (e.g. behind-the-scenes) must use valid `src`/`poster` paths. Smoke-test client and photographer views after changes.

## Roles and flows

Implement distinct experiences (routes or sections as needed):

1. **Client**: Can **log in** and **view** photos shared with them (galleries, albums, or assignments—use clear mocked data unless the user specifies structure).
2. **Photographer**: Can **log in** and **upload** photos for a client (mock storage and metadata unless real storage or APIs are specified).

Use **mock authentication** and **mock persistence** (in-memory, JSON files, or a simple dev store) unless the user provides auth providers, database, or file-storage requirements. Document assumed roles and session behavior in Phase 6 of the web-developer skill.

## Security note

Even with mocks, follow secure patterns for forms and session handling so replacing mocks with a real backend does not require a full rewrite.
