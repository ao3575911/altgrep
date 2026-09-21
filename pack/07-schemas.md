---
title: AltGrep schemas
date: 2026-09-21
lane: ops
status: draft
source_skills: files
disclaimer: general-information
---

## Purpose

Canonical field names for profiles, listings, threads, vouches, groups.

## Facts

- JSON objects. IDs are `ag_` + type prefix + hex.
- Times are ISO-8601 UTC.
- Field names here bind CLI `--json`, HTTP, and the local store. Do not invent aliases.
- Seed listing categories in build: `handle`, `consulting`, `dossier`. Broader taxonomy in `04` is not a schema expansion mandate.
- Named canon pack: `/home/workdir/artifacts/20260921-altgrep/`; live: `/workspace/artifacts/20260921-altgrep/`.

## Thesis

Thesis. One schema serves CLI `--json`, HTTP, and the local store.

### Profile

```json
{
  "id": "ag_p_01",
  "handle": "nomen",
  "display": "nomen",
  "bio": "",
  "links": [],
  "created_at": "2026-09-21T00:00:00Z",
  "foreign_handles": [
    {"service": "x", "handle": "example", "control": "pending"}
  ]
}
```

`handle` stores the name without `@`. Display always prints `@handle`. `control` is `pending` | `proven` | `failed` — fail closed; never label as UI “verified.”

### Listing

```json
{
  "id": "ag_l_01",
  "seller": "nomen",
  "title": "Office hours, dossier review",
  "body": "",
  "category": "consulting",
  "tags": ["review"],
  "kind": "service",
  "price": {"amount": 0, "currency": "AUD", "unit": "hour", "note": "enquiry"},
  "foreign_handle": null,
  "status": "draft",
  "created_at": "2026-09-21T00:00:00Z"
}
```

`kind`: `right` | `file` | `service` | `handle` | `seat`. Seed `category` values in P0: `handle` | `consulting` | `dossier`.

### Vouch

```json
{
  "id": "ag_v_01",
  "from": "nomen",
  "to": "other",
  "reason": "reviewed_file",
  "listing_id": null,
  "note": "",
  "created_at": "2026-09-21T00:00:00Z",
  "revoked_at": null
}
```

`revoked_at` non-null means revoked. CLI `vouch revoke` is specified in `08` but not yet shipped in P0.

### Thread

```json
{
  "id": "ag_t_01",
  "listing_id": "ag_l_01",
  "members": ["nomen", "other"],
  "messages": [
    {"from": "other", "body": "still available?", "at": "2026-09-21T00:00:00Z"}
  ]
}
```

Thread verbs are in `08`; P0 CLI does not yet implement `thread open` / `thread reply`.

### Group

```json
{
  "id": "ag_g_01",
  "name": "deal-room-01",
  "members": ["nomen"],
  "listing_id": null,
  "visibility": "invite"
}
```

Groups are P3. Do not claim E2E for group content until crypto exists.

## Actions

1. Code imports these field names. Do not invent aliases.
2. No invented fee, revenue, or user-count fields.

## Open questions

- Attachment objects for dossier files (hash + filename) in P1.

## Sources

- Product design file in this pack; claims in `06-claims-goals.md`.
