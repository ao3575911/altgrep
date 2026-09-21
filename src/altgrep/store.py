from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

HANDLE_RE = re.compile(r"^[a-z0-9](?:[a-z0-9-]{1,30}[a-z0-9])$")
CATEGORIES = (
    "ip",
    "dossier",
    "handle",
    "consulting",
    "advertising",
    "protocol",
    "software",
    "creative",
    "dealroom",
    "education",
    "paper-rights",
    "collectible",
    "infrastructure",
    "attestation",
)


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def home() -> Path:
    raw = os.environ.get("ALTGREP_HOME")
    return Path(raw) if raw else Path.home() / ".altgrep"


def state_path() -> Path:
    return home() / "state.json"


def empty_state() -> dict:
    return {"profile": None, "listings": [], "vouches": [], "threads": [], "groups": []}


def load() -> dict:
    path = state_path()
    if not path.exists():
        return empty_state()
    return json.loads(path.read_text(encoding="utf-8"))


def save(state: dict) -> None:
    path = state_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")


def valid_handle(name: str) -> bool:
    return bool(HANDLE_RE.match(name.lower()))
