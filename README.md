# altgrep

CLI-first catalog for unusual listings: rights, dossiers, handles you control, hours.

This is a P0 local scaffold. No network. State lives in `~/.altgrep/state.json` or `$ALTGREP_HOME`.

## Run

```bash
git clone https://github.com/ao3575911/altgrep && cd altgrep
PYTHONPATH=src python3 -m altgrep --help
PYTHONPATH=src python3 -m altgrep demo
```

The design notes are in [`pack/`](pack/).

## Verbs (P0 shipped)

- `signup --handle NAME`
- `whoami`
- `list create --title T --category consulting|dossier|handle`
- `search [q]`
- `show ID`
- `vouch add --to HANDLE --reason worked_with|paid|reviewed_file|knows`
- `categories`
- `demo`

## Not yet in CLI (see pack `05` / `08`)

- `profile @handle`
- `thread open` / `thread reply`
- `vouch revoke`

Seed listing classes only: handle, consulting, dossier. Not production. Not a payments product. No GitHub push unless Adam orders that gate. See `../20260921-altgrep/06-claims-goals.md`.
