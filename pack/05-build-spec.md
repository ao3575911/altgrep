---
title: AltGrep build plan and spec
date: 2026-09-21
lane: ops
status: draft
source_skills: files
disclaimer: general-information
---

## Purpose

What to build, in what order, against which interfaces.

## Facts

- Named canon code path: `/home/workdir/artifacts/altgrep/`. Live on this box: `/workspace/artifacts/altgrep/` (see `/workspace/artifacts/PATH-NOTE.md`).
- Language for v0: Python 3.11+ stdlib-first CLI, JSON files as the store. Swap the store for Postgres later without changing verbs.
- **P0 shipped today:** `signup`, `whoami`, `list create`, `search`, `show`, `vouch add`, `categories`, `demo`.
- **P0 missing vs this file / `08-api.md`:** `profile @handle`, `thread open`, `thread reply`, `vouch revoke`. Reflect gaps; do not invent features in docs as if they run.
- Seed listing classes only: handle, consulting, dossier. Taxonomy in `04` is not a build queue.
- Code honesty: `store.CATEGORIES` still enumerates the full taxonomy enum; pack canon (seed-only) wins for build priority — do not treat extra enum values as a queue to productise (no code change this hardening pass).

## Thesis

Thesis. Spec the verbs first. Persistence is a plugin.

### Stack v0

- CLI: `python -m altgrep` (on this box: `cd /workspace/artifacts/altgrep && PYTHONPATH=src python3 -m altgrep`)
- Store: `~/.altgrep/state.json` (local) or `$ALTGREP_HOME`
- HTTP later: same JSON schemas, FastAPI or similar
- Web later: read-only catalog over the same store

### Phases

P0 — local CLI, no network
- profile create (`signup`) / whoami — **shipped**
- `profile @handle` — **missing**
- listing create / show / search — **shipped**; categories enum — **shipped**
- vouch add — **shipped**; vouch revoke — **missing**
- thread open / reply (local) — **missing**
- demo — **shipped**

P1 — hosted API
- auth token
- identical verbs over HTTP
- moderation flag
- handle challenge (fail closed)

P2 — web catalog + compose (counsel before paid tier / take-rate)
P3 — groups
P4 — payments decision (no escrow/take-rate before this + counsel)

### Quality gates

- Every CLI command has an `--json` flag.
- Schemas in `07-schemas.md` are the source of field names. Routes/verbs in `08-api.md`.
- No silent default to “available” on a failed handle check. Fail closed.
- No “verified” weasel in UI; say control-proven when true.
- Extend this repo only. No sibling project. No GitHub push unless Adam orders the gate.

### Threat model v0 (honest)

Local store is not multi-user safe. Hosted v1: TLS, hashed credentials, operator-readable rooms unless E2E is actually implemented. Do not market E2E until the crypto is in the repo and the UI tells the truth.

## Actions

1. Run on this box: `cd /workspace/artifacts/altgrep && PYTHONPATH=src python3 -m altgrep demo`.
2. Do not start a chat protocol until listings search works (search already ships; next: thread + profile + vouch revoke).
3. Counsel gate for terms, IP notice mailbox, privacy before public paid offers.

## Open questions

- FastAPI vs raw stdlib http.server for P1.

## Sources

- This pack and the scaffold README. Live pack: `/workspace/artifacts/20260921-altgrep/`.
