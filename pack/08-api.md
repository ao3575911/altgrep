---
title: AltGrep API sketch
date: 2026-09-21
lane: ops
status: draft
source_skills: files
disclaimer: general-information
---

## Purpose

HTTP and CLI verb map. P0 implements CLI only against a local store.

## Facts

- Auth later: `Authorization: Bearer <token>`.
- All responses wrap `{ "ok": true, "data": ... }` or `{ "ok": false, "error": "..." }`.
- **P0 CLI shipped:** `signup`, `whoami`, `list create`, `search`, `show`, `vouch add`, `categories`, `demo`.
- **P0 CLI missing (table below still binds the target):** `profile @handle`, `thread open`, `thread reply`, `vouch revoke`. Also later: `handle prove`, `group create`, `report`.
- Fail closed: `unproven_handle` is not success. No UI “verified” weasel.
- Named canon code: the repo root; live: the repo root.

## Thesis

Thesis. CLI flags are query parameters. No special CLI-only fields.

### Routes

| Method | Path | CLI | P0 CLI |
|---|---|---|---|
| POST | `/v1/profiles` | `altgrep signup --handle x` | shipped |
| GET | `/v1/profiles/@{handle}` | `altgrep profile @x` | **missing** |
| GET | `/v1/me` | `altgrep whoami` | shipped |
| POST | `/v1/listings` | `altgrep list create` | shipped |
| GET | `/v1/listings` | `altgrep search --q --category` | shipped |
| GET | `/v1/listings/{id}` | `altgrep show {id}` | shipped |
| POST | `/v1/listings/{id}/challenge` | `altgrep handle prove` | later (P1) |
| POST | `/v1/vouches` | `altgrep vouch add` | shipped |
| POST | `/v1/vouches/{id}/revoke` | `altgrep vouch revoke` | **missing** |
| POST | `/v1/threads` | `altgrep thread open` | **missing** |
| POST | `/v1/threads/{id}/messages` | `altgrep thread reply` | **missing** |
| POST | `/v1/groups` | `altgrep group create` | later (P3) |
| POST | `/v1/reports` | `altgrep report` | later |

`--json` on every CLI verb. Seed listing categories only: handle, consulting, dossier.

### Errors

`invalid_handle`, `taken`, `unproven_handle`, `forbidden_category`, `not_found`, `rate_limited`.

### Output contract

- Success and error shapes as above. No silent success on unproven handles.
- Estimates prefixed Estimate. Unverified facts prefixed Unverified. No invented revenue, user counts, or fee tables in API docs.

## Actions

1. Keep this table and the CLI `--help` text aligned. When shipping a missing verb, update this column in the same change.
2. No GitHub push unless Adam orders the gate. No sibling API docs tree.

## Open questions

- Pagination cursor format.

## Sources

- `07-schemas.md`, `06-claims-goals.md`, `05-build-spec.md`
