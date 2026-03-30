# Agent: Marketing site

## Skill

Follow the phased Next.js workflow in [`../.cursor/skills/web-developer/SKILL.md`](../.cursor/skills/web-developer/SKILL.md). Treat that skill as the default process (setup, requirements, dev server, implementation, security and quality, documentation with Mermaid).

## Theme and content

If the user has **not** already provided brand, visual, or copy direction, ask once for a **short summarized theme** before building major UI or content. Include at least: audience, tone (e.g. corporate vs playful), color or style hints, and whether the focus is **marketing services** or **a specific product**.

## Product intent

Build a Next.js site centered on **marketing services** or **promoting a product** (landing pages, value props, CTAs, social proof patterns as appropriate).

## Data and assets

Use **mocked** copy, testimonials, metrics, imagery, and logos unless the user supplies real samples or files. Clearly separate placeholder content from user-provided material so it can be swapped later.

## Media (images and video)

Hero images, logos, thumbnails, and any **video** must **load without errors**: real files under `public/` or remote URLs allowed in `next.config` for `next/image`. Verify in the browser that marketing pages do not 404 media or show broken image icons. Follow the **Images and video** section in the web-developer skill.

## Out of scope unless requested

Real CMS integration, live analytics wiring, or production ad pixels—unless the user asks.
