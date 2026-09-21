# altgrep

CLI-first catalog for unusual listings: rights, dossiers, handles you control, hours.

This is a P0 local scaffold. No network. State lives in `~/.altgrep/state.json` or `$ALTGREP_HOME`.

## Paths

- **Live (this Grok Bot box):** `/workspace/artifacts/altgrep`
- **Named canon (pack prose):** `/home/workdir/artifacts/altgrep`
- Design pack: live `/workspace/artifacts/20260921-altgrep/` (named `/home/workdir/artifacts/20260921-altgrep/`). See `/workspace/artifacts/PATH-NOTE.md`.

## Run

```bash
cd /workspace/artifacts/altgrep
PYTHONPATH=src python3 -m altgrep --help
PYTHONPATH=src python3 -m altgrep demo
```

(Named-canon equivalent: `cd /home/workdir/artifacts/altgrep` with the same commands.)

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
