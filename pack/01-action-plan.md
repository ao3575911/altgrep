---
title: AltGrep master action plan
date: 2026-09-21
lane: ops
status: draft
source_skills: files
disclaimer: general-information
---

## Purpose

Ordered work from zero to a testable three-rail loop.

## Facts

- Three rails: Chat/Groups, Classifieds/Marketplace, Vouch/Reputation.
- Surfaces: CLI, web, later mobile. CLI is first-class, not a toy port.
- First market: unusual listings that Craigslist/eBay/Gumtree treat as junk or scam-adjacent, handled here with honest category rules.
- Name locked: **altGrep** (see `09-brand-kit.md`).
- P0 CLI **shipped today**: `signup`, `whoami`, `list create`, `search`, `show`, `vouch add`, `categories`, `demo`.
- P0 CLI **missing vs** `05-build-spec.md` / `08-api.md`: `profile @handle`, `thread open` / `thread reply`, `vouch revoke`. Do not claim they ship until implemented.
- MAY LIST seed only: handle (after control proof), consulting, dossier. Taxonomy in `04` is not a build queue.

## Thesis

Thesis. Do not build chat, market, and trust as three apps. Build one identity (`@name`) and one object model (Profile, Listing, Thread, Vouch) that all clients share.

## Actions

1. Keep non-goals frozen in `06-claims-goals.md`. Especially: no raw-idea “guaranteed unique invention” sales; no third-party handle listings without a control proof; no UI weasel “verified” for control-proven.
2. Publish prohibited list before the first public listing form. Seed classes only: Handles (proof-of-control), Consulting hours, Dossier (copyrighted file, not a patent promise).
3. Profile onboarding: `@name` + 280-char bio + optional links. CLI and web same schema. Add `profile @handle` to close the P0 gap.
4. Threading: listing-attached inquiry thread (`thread open` / `thread reply`). No global public square.
5. Vouch: directed, revocable (`vouch revoke`), capped. Visible on profile. No numeric “trust score out of 100” in v1.
6. Groups: invite-only rooms with listing optional. Encryption threat model written before any “E2E” marketing.
7. Counsel gate: ACL listing copy, IP assignment templates, privacy policy, prohibited goods, terms. Do not draft as counsel.
8. Closed beta: 20 operators who already trade odd inventory (names, briefs, advisory time).
9. Public scout page: search listings, no wallet required.
10. Payments: v1 introductions + marked “deal off-platform” or a later escrow. No escrow/take-rate before P2 + counsel. Do not pretend escrow exists.
11. No GitHub push, release, domain buy, mark filing, or paid tier unless Adam explicitly orders that gate. No sibling docs tree or sibling repo.

## 30 / 90 / 180

- 30 days. Schema, close P0 CLI gaps (profile / thread / vouch revoke), web read-only catalog, prohibited list.
- 90 days. Inquiries live, vouches + revoke, invite groups, handle-control challenge.
- 180 days. First-party web compose, moderation queue, IP notice channel, one paid listing tier if counsel clears it.

## Open questions

- Escrow in year 1 or never (blocked on P2 + counsel either way).
- Whether groups can exist with zero marketplace use.

## Sources

- Pack files in this directory. Live paths: `pack/` (named: `pack/`).
