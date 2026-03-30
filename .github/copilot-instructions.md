When performing a **pull request code review** for this repository:

## Security and sensitive data (highest priority)

- Flag **secrets and credentials**: API keys, bearer tokens, passwords, private keys (including PEM blocks), OAuth client secrets, signing keys, cloud access keys (AWS/Azure/GCP-style), webhook secrets, and database URLs or connection strings that embed usernames/passwords.
- Flag **`.env` or similar** committed with real-looking values; documented fake placeholders are OK.
- Flag likely **PII** or internal-only identifiers (real employee emails, personal phone numbers, internal hostnames) if they appear unintentional.
- Flag **scratch or generated artifacts** committed under `build/` (only `build/.gitkeep` should be tracked) or other paths that should be gitignored per `CONTRIBUTING.md` / example `.gitignore`.

## Conformance with CONTRIBUTING.md

Use **`CONTRIBUTING.md`** at the repository root as the bar. Mention gaps when the diff touches that area:

- **Conventional Commits** for PR title / commit messages: `feat:`, `fix:`, `docs:`, `chore:`, optional scope (e.g. `docs(examples):`, `feat(web):`).
- **Self-contained examples** under `examples/`: README with purpose and install/run; **`AGENTS.md`** when agent-driven; **`.gitignore`** for generated/vendor output; dependencies explicit (`package.json`, `requirements.txt`, or documented installs). No undocumented reliance on sibling folders.
- **Cursor and Claude**: Cursor paths/skills should remain valid; Cursor-specific flows should document **Claude** usage in the example README (or a purposeful `CLAUDE.md`), not empty stubs.
- **Documentation**: behavior changes should update example README / `AGENTS.md` / skills and **root `README.md`** when the public examples index or setup story changes; keep relative links accurate.
- **Assets**: shared images/media in **`assets/`**; example-only assets stay in the example unless intentionally promoted.

Prioritize **security** and **accidental leakage**. Be specific and actionable in comments.
