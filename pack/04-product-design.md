---
title: AltGrep product design
date: 2026-09-21
lane: ops
status: draft
source_skills: files, vision-forge
disclaimer: general-information
---

## Purpose

Product design for a three-rail platform: Groups/Chat, Classifieds, Vouch. CLI and web/app are clients of one API.

## Facts

- Onboarding creates a profile with `@name`.
- Marketplace accepts `@handle` listings from other services only after a control proof.
- Raw ideas are generally not a saleable property in Australian explainers; listings must attach a right, a file, or a service. [web:94]
- **MAY LIST (v1 seed only):** handle (after control proof), consulting, dossier. The category taxonomy below is orientation, **not a build queue**. Do not add a class without Adam saying so.
- P0 CLI gap (honest): shipped `signup` / `whoami` / `list create` / `search` / `show` / `vouch add` / `categories` / `demo`. Not yet: `profile @handle`, `thread open` / `thread reply`, `vouch revoke` (see `05`, `08`).

## Thesis

Thesis. One `@name` is the root object. Listings, threads, groups, and vouches hang off it. Trust is a graph of signed vouches, not a composite score that can be gamed in silence.

### Rails

1. Identity — `@name`, bio, links, control proofs for foreign handles.
2. Market — listings in unusual categories (seed: handle, consulting, dossier).
3. Room — listing inquiry threads and invite groups.
4. Vouch — directed statements with a reason code and optional listing reference.

### Surfaces

- CLI: every mutating verb (`signup`, `whoami`, `list`, `search`, `thread`, `vouch`, `group`). Target map; P0 honesty in Facts.
- Web: same verbs, human layout.
- App: later wrapper around the web API.

### Onboarding (CLI or web)

1. Choose `@name` (same grammar freeze as earlier handle work: `a-z0-9`, hyphen not at ends, min 3).
2. 280-character bio.
3. Optional URL list.
4. Accept terms and prohibited-list summary.
5. No KYC. No government document upload. No myID / AGDIS.

### Handle listings

A listing of type `handle` declares a foreign handle (`instagram:coffnup`, `x:AdamOConnorOz`, `github:ao3575911`) and must pass a control challenge (signed bio text, DNS txt, or platform-native proof). Listing someone else’s handle is rejected. Fail closed: unproven is not available. Never shorten “control-proven” to UI “verified.”

### Trust

- Vouch is public, named, revocable.
- Fields: from, to, reason (`worked_with`, `paid`, `reviewed_file`, `knows`), optional listing id, 140-char note.
- Cap: 5 open vouches per giver per 30 days in v1.
- No 0–100 score in v1. Profile shows count + last five.

### Rooms

- Inquiry thread is born from a listing. Visible to seller + inquirer.
- Group is invite-only. Optional listing pin. Server-side encryption at rest in v1. Do not claim E2E until it is true.
- No public global chat.

### Categories (v1 taxonomy — not a build queue)

Orientation only. Build implements seed classes first.

1. **Intellectual property** — trade marks, patents/applications, registered designs, copyright assignments, licence offers (numbers / named work / scope as required).
2. **Dossiers and works** — concept file (copyrighted; no “this will patent”), theory/research brief, world/brand system, dataset with lawful provenance.
3. **Handles and names** — foreign @handles (control-proven), local `@name` transfers, naming packs.
4. **Consulting and time** — office hours, dossier review, advisory retainer (scope, not outcomes).
5. **Advertising and attention** — newsletter slot, group announcement, unusual lawful placement.
6. **Protocols and specs** — open spec with paid support; closed spec under NDA workflow.
7. **Software and systems** — WIP repo, lawful tooling access, automation recipes.
8. **Creative systems** — visual language, editorial voice pack, type/mark files.
9. **Deal rooms** — group seat bundled with a listing; data-room access window.
10. **Education** — workshop seat, recorded brief, reading list + office hour.
11. **Rights in paper** — option to negotiate (not forged title); public-record process introduction.
12. **Collectible abstracts** — numbered essay, editioned diagram, signed notebook dump.
13. **Infrastructure** — moderated group-as-a-service; private index / watchlist feed.
14. **Attestation work** — paid review of someone else’s listing (disclosed).

Each listing must pick one primary category and may add two tags. Seed build: `handle`, `consulting`, `dossier` only.

### Prohibited (non-exhaustive)

Weapons, explosives, illegal drugs, stolen goods, fraud kits, malware, doxxing datasets, CSAM, non-consensual intimate material, listings that instruct crimes, government-ID forgeries, third-party handles without control proof, “guaranteed patent” or “guaranteed returns,” earnings promises on dossiers.

### Core screens / CLI verbs

| Human | CLI | P0 status |
|---|---|---|
| Home search | `altgrep search q` | shipped |
| Listing | `altgrep show <id>` | shipped |
| Compose | `altgrep list create` | shipped (seed categories) |
| Profile | `altgrep whoami` / `altgrep profile @x` | whoami shipped; `profile @x` missing |
| Inbox | `altgrep thread open` / `thread reply` | missing |
| Vouch | `altgrep vouch add @x --reason paid` / `vouch revoke` | add shipped; revoke missing |
| Groups | `altgrep group ls` | later (P3) |

### Product principles

1. Fail closed. Unknown availability or unproven handle is not “green.”
2. The string `@name` does not change. The account can be transferred by a dedicated flow later.
3. Server honesty: if operators can read a room, the UI says so.
4. No feed tab.
5. Unusual inventory only. Ban commodity goods in policy if they drown the catalog.
6. No sibling repo or sibling docs tree. No GitHub push unless Adam orders the gate.

## Actions

1. Implement seed classes only: handle, consulting, dossier.
2. Write listing templates that force a right, a file, or a service. Counsel gate on terms / IP / privacy.
3. Close P0 gaps: `profile @handle`, `thread open` / `reply`, `vouch revoke`.

## Open questions

- Transfer of `@name` in v1 or later.
- Whether advertising listings can target groups without consent (decided: no).

## Sources

- https://sprintlaw.com.au/articles/selling-your-business-idea-in-australia-essential-legal-steps/
- `06-claims-goals.md` (highest canon)
