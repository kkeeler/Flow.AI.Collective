# Agent: SaaS / commerce starter

## Skill

Follow the phased Next.js workflow in [`../.cursor/skills/web-developer/SKILL.md`](../.cursor/skills/web-developer/SKILL.md). Treat that skill as the default process (setup, requirements, dev server, implementation, security and quality, documentation with Mermaid).

## Theme and content

If the user has **not** already provided brand, product name, or positioning, ask once for a **short summarized theme** (B2B vs B2C, visual style, whether the focus is **subscriptions** for a web product or **one-time product** commerce) before building checkout and marketing surfaces.

## Product intent

Starter Next.js app for someone selling a **web product** (subscriptions) or **commerce** (physical or digital products):

- **Web product path**: Emphasize **subscriptions** (plans, mock billing cycle, mock entitlement if useful).
- **Commerce path**: **Products** are defined by the user in requirements but **implemented with mocked catalog and inventory** unless they supply real data or integrations.

## Required features (implement with mocks unless specified)

- **Sign up**, **log in**, **log out**
- **Cart** (add/update/remove, persisted mock or session)
- **Payments**: UI and flow only with **mock payment success/failure**—no real card processing unless the user provides a provider (e.g. Stripe) and keys via env. Never commit secrets.

All **catalog, pricing, user accounts, orders, and subscription state** should be **mocked** unless the user supplies specifics (schema, APIs, payment provider).

## Media (images and video)

**Product images**, marketing visuals, and any **demo video** on landing or product pages must load reliably: use `public/` assets or allowlisted remotes, and configure `next/image` for external product URLs. Cart and catalog UIs should not show broken images; add fallbacks where image URLs are mock data.

## Clarify early

Ask whether the primary template should optimize for **subscription SaaS** or **product storefront**, and whether payments should stay **fully simulated** or integrate a named provider.

## Documentation

Mermaid diagrams should cover auth, cart, and checkout (mock vs future real payment) boundaries (see Phase 6 of the web-developer skill).
