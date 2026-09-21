from __future__ import annotations

import argparse
import json
import sys
from uuid import uuid4

from altgrep.store import CATEGORIES, load, now, save, valid_handle


def out(data, as_json: bool) -> None:
    if as_json:
        print(json.dumps({"ok": True, "data": data}, indent=2))
    else:
        if isinstance(data, dict):
            for k, v in data.items():
                print(f"{k}: {v}")
        elif isinstance(data, list):
            for row in data:
                print(row if isinstance(row, str) else json.dumps(row))
        else:
            print(data)


def err(msg: str, as_json: bool) -> int:
    if as_json:
        print(json.dumps({"ok": False, "error": msg}))
    else:
        print(f"error: {msg}", file=sys.stderr)
    return 1


def nid(prefix: str) -> str:
    return f"ag_{prefix}_{uuid4().hex[:8]}"


def cmd_signup(args) -> int:
    handle = args.handle.lstrip("@").lower()
    if not valid_handle(handle):
        return err("invalid_handle", args.json)
    state = load()
    state["profile"] = {
        "id": nid("p"),
        "handle": handle,
        "display": handle,
        "bio": args.bio or "",
        "links": [],
        "created_at": now(),
        "foreign_handles": [],
    }
    save(state)
    out({"handle": f"@{handle}"}, args.json)
    return 0


def cmd_whoami(args) -> int:
    state = load()
    if not state.get("profile"):
        return err("not_found", args.json)
    p = state["profile"]
    out({"handle": f"@{p['handle']}", "bio": p.get("bio", "")}, args.json)
    return 0


def cmd_list_create(args) -> int:
    state = load()
    if not state.get("profile"):
        return err("not_found", args.json)
    if args.category not in CATEGORIES:
        return err("forbidden_category", args.json)
    if args.category == "handle" and not args.foreign:
        return err("unproven_handle", args.json)
    item = {
        "id": nid("l"),
        "seller": state["profile"]["handle"],
        "title": args.title,
        "body": args.body or "",
        "category": args.category,
        "tags": [],
        "kind": "handle" if args.category == "handle" else "service" if args.category == "consulting" else "file",
        "price": {"amount": args.price, "currency": "AUD", "unit": args.unit, "note": "enquiry"},
        "foreign_handle": args.foreign,
        "status": "draft",
        "created_at": now(),
    }
    state["listings"].append(item)
    save(state)
    out(item, args.json)
    return 0


def cmd_search(args) -> int:
    state = load()
    q = (args.q or "").lower()
    rows = []
    for item in state["listings"]:
        if args.category and item["category"] != args.category:
            continue
        blob = f"{item['title']} {item['body']} {item['category']}".lower()
        if q and q not in blob:
            continue
        rows.append(f"{item['id']}\t@{item['seller']}\t{item['category']}\t{item['title']}")
    out(rows, args.json)
    return 0


def cmd_show(args) -> int:
    state = load()
    for item in state["listings"]:
        if item["id"] == args.id:
            out(item, args.json)
            return 0
    return err("not_found", args.json)


def cmd_vouch(args) -> int:
    state = load()
    if not state.get("profile"):
        return err("not_found", args.json)
    v = {
        "id": nid("v"),
        "from": state["profile"]["handle"],
        "to": args.to.lstrip("@").lower(),
        "reason": args.reason,
        "listing_id": args.listing,
        "note": args.note or "",
        "created_at": now(),
        "revoked_at": None,
    }
    state["vouches"].append(v)
    save(state)
    out(v, args.json)
    return 0


def cmd_categories(args) -> int:
    out(list(CATEGORIES), args.json)
    return 0


def cmd_demo(args) -> int:
    class N:
        json = args.json
        handle = "nomen"
        bio = "lists rights, files, hours"
        title = "Dossier review, two hours"
        category = "consulting"
        body = "Read a concept file. No outcome promise."
        foreign = None
        price = 0
        unit = "hour"
        q = "dossier"
        to = "other"
        reason = "reviewed_file"
        listing = None
        note = "local demo"

    cmd_signup(N)
    cmd_list_create(N)
    print("--- search ---")
    cmd_search(N)
    cmd_vouch(N)
    return 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="altgrep", description="Unusual listings, named vouches.")
    p.add_argument("--json", action="store_true")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("signup")
    s.add_argument("--handle", required=True)
    s.add_argument("--bio", default="")
    s.set_defaults(func=cmd_signup)

    sub.add_parser("whoami").set_defaults(func=cmd_whoami)

    c = sub.add_parser("list")
    cs = c.add_subparsers(dest="listcmd", required=True)
    cc = cs.add_parser("create")
    cc.add_argument("--title", required=True)
    cc.add_argument("--category", required=True)
    cc.add_argument("--body", default="")
    cc.add_argument("--foreign", default=None)
    cc.add_argument("--price", type=int, default=0)
    cc.add_argument("--unit", default="enquiry")
    cc.set_defaults(func=cmd_list_create)

    se = sub.add_parser("search")
    se.add_argument("q", nargs="?", default="")
    se.add_argument("--category")
    se.set_defaults(func=cmd_search)

    sh = sub.add_parser("show")
    sh.add_argument("id")
    sh.set_defaults(func=cmd_show)

    v = sub.add_parser("vouch")
    vs = v.add_subparsers(dest="vcmd", required=True)
    va = vs.add_parser("add")
    va.add_argument("--to", required=True)
    va.add_argument("--reason", required=True)
    va.add_argument("--listing", default=None)
    va.add_argument("--note", default="")
    va.set_defaults(func=cmd_vouch)

    sub.add_parser("categories").set_defaults(func=cmd_categories)
    sub.add_parser("demo").set_defaults(func=cmd_demo)

    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
