# altGrep

Display: **Alt/Grep**. Motto: Grep the listings a shopfront will not hold.

CLI/module: `altgrep`. Pack date: 2026-09-21.

## Layout

| Path | Role |
|---|---|
| `src/altgrep/` | P0 local CLI scaffold |
| `pack/` | Design pack (00–10) + hardening changelog |
| `PATH-NOTE.md` | Named canon vs live box paths |
| `brand/` | Mark assets |

## Run (this box)

```bash
cd ./
PYTHONPATH=src python3 -m altgrep demo
```

## Canon

Highest: `pack/06-claims-goals.md`, then `pack/07-schemas.md` + `pack/08-api.md`.
No GitHub push/release unless Adam explicitly orders that gate.

## P0 status

Shipped: signup, whoami, list create, search, show, vouch add, categories, demo.
Missing: profile @handle, thread open/reply, vouch revoke.
Seed list classes: handle, consulting, dossier.
