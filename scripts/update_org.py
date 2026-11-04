#!/usr/bin/env python3
"""Validate org.json, bump version, embed into interface, append changelog, optional snapshot."""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REQUIRED_TOP = ["meta", "chairman", "vision", "values", "master", "council", "teams", "skills", "decisions", "blockers"]
SKILL_STATUSES = {"noticed", "draft", "reviewed", "active", "retired"}
EMBED_START = "/* __ORG_EMBED_START__ */"
EMBED_END = "/* __ORG_EMBED_END__ */"


def die(msg: str, code: int = 1) -> None:
    print(f"error: {msg}", file=sys.stderr)
    raise SystemExit(code)


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        die(f"cannot read {path}: {e}")


def validate(org: dict) -> list[str]:
    errors = []
    for k in REQUIRED_TOP:
        if k not in org:
            errors.append(f"missing top-level key: {k}")
    if errors:
        return errors
    meta = org["meta"]
    for k in ("id", "version", "updated"):
        if k not in meta:
            errors.append(f"meta.{k} required")
    if "display_name" not in org["chairman"]:
        errors.append("chairman.display_name required")
    for k in ("id", "name", "purpose"):
        if k not in org["master"]:
            errors.append(f"master.{k} required")
    ids = {"master", "chairman"}
    for c in org.get("council", []):
        if "id" not in c:
            errors.append("council seat missing id")
            continue
        if c["id"] in ids:
            errors.append(f"duplicate id: {c['id']}")
        ids.add(c["id"])
    seat_ids = set()
    for t in org.get("teams", []):
        for req in ("id", "name", "domain", "lead", "seats"):
            if req not in t:
                errors.append(f"team missing {req}")
        for s in t.get("seats", []):
            for req in ("id", "name", "purpose", "reports_to"):
                if req not in s:
                    errors.append(f"seat missing {req}")
            sid = s.get("id")
            if sid:
                if sid in seat_ids or sid in ids:
                    errors.append(f"duplicate seat id: {sid}")
                seat_ids.add(sid)
        lead = t.get("lead")
        if lead and lead not in {s.get("id") for s in t.get("seats", [])}:
            errors.append(f"team {t.get('id')} lead {lead} not in seats")
    known = ids | seat_ids
    for t in org.get("teams", []):
        for s in t.get("seats", []):
            rt = s.get("reports_to")
            if rt and rt not in known:
                errors.append(f"seat {s.get('id')} reports_to unknown id {rt}")
    for sk in org.get("skills", []):
        for req in ("id", "name", "owner", "version", "status"):
            if req not in sk:
                errors.append(f"skill missing {req}")
        if sk.get("status") not in SKILL_STATUSES:
            errors.append(f"skill {sk.get('id')} bad status {sk.get('status')}")
        if sk.get("owner") and sk["owner"] not in known:
            errors.append(f"skill {sk.get('id')} owner unknown: {sk.get('owner')}")
    return errors


def bump_patch(version: str) -> str:
    parts = version.split(".")
    if len(parts) >= 3 and parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit():
        return f"{parts[0]}.{parts[1]}.{int(parts[2]) + 1}"
    return version + ".1"


def embed(interface_html: Path, org: dict, changelog: list, out_html: Path | None = None) -> Path:
    text = interface_html.read_text(encoding="utf-8")
    if EMBED_START not in text or EMBED_END not in text:
        die("interface/index.html missing embed markers")
    payload = (
        EMBED_START
        + "\nwindow.__ORG__ = "
        + json.dumps(org, indent=2)
        + ";\nwindow.__CHANGELOG__ = "
        + json.dumps(changelog, indent=2)
        + ";\n"
        + EMBED_END
    )
    new_text = re.sub(
        re.escape(EMBED_START) + r".*?" + re.escape(EMBED_END),
        payload.replace("\\", r"\\"),
        text,
        count=1,
        flags=re.S,
    )
    # re.sub with replace issues for backslashes; do manual slice instead for safety
    start = text.index(EMBED_START)
    end = text.index(EMBED_END) + len(EMBED_END)
    new_text = text[:start] + payload + text[end:]
    target = out_html or interface_html
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(new_text, encoding="utf-8")
    return target


def try_snapshot(html_path: Path, png_path: Path, width: int = 1280, height: int = 1800) -> bool:
    chrome = shutil.which("google-chrome") or shutil.which("chromium") or shutil.which("chromium-browser")
    if not chrome:
        print("note: no headless chrome found; wrote HTML snapshot only")
        return False
    html_path = html_path.resolve()
    png_path = png_path.resolve()
    png_path.parent.mkdir(parents=True, exist_ok=True)
    # Serve via file URL after embed so JSON is inline
    url = html_path.as_uri()
    cmd = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--window-size={width},{height}",
        f"--screenshot={png_path}",
        url,
    ]
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True, timeout=60)
        print(f"wrote {png_path}")
        return True
    except Exception as e:
        print(f"note: screenshot failed ({e}); HTML snapshot kept")
        return False


def main() -> None:
    ap = argparse.ArgumentParser(description="Update agent-council org map")
    ap.add_argument("--org", type=Path, required=True, help="Path to org.json")
    ap.add_argument("--interface", type=Path, help="Path to interface/index.html (default: repo interface)")
    ap.add_argument("--message", default="org update", help="Changelog message")
    ap.add_argument("--no-bump", action="store_true", help="Do not bump meta.version")
    ap.add_argument("--snapshot", action="store_true", help="Write docs snapshot HTML/PNG")
    ap.add_argument("--docs", type=Path, help="Docs output directory for snapshots")
    args = ap.parse_args()

    org_path = args.org.resolve()
    if not org_path.is_file():
        die(f"org not found: {org_path}")

    repo_root = Path(__file__).resolve().parents[1]
    interface = (args.interface or (repo_root / "interface" / "index.html")).resolve()
    if not interface.is_file():
        die(f"interface not found: {interface}")

    org = load_json(org_path)
    errors = validate(org)
    if errors:
        for e in errors:
            print(f"error: {e}", file=sys.stderr)
        raise SystemExit(1)

    now = datetime.now().astimezone().replace(microsecond=0).isoformat()
    if not args.no_bump:
        org["meta"]["version"] = bump_patch(str(org["meta"].get("version", "0.1.0")))
    org["meta"]["updated"] = now

    changelog_path = org_path.parent / "changelog.json"
    shared_changelog = repo_root / "interface" / "changelog.json"
    changelog = load_json(changelog_path) if changelog_path.is_file() else []
    if not isinstance(changelog, list):
        changelog = []
    entry = {"at": now, "version": org["meta"]["version"], "message": args.message, "org_id": org["meta"]["id"]}
    changelog.append(entry)

    org_path.write_text(json.dumps(org, indent=2) + "\n", encoding="utf-8")
    changelog_path.write_text(json.dumps(changelog, indent=2) + "\n", encoding="utf-8")
    # Shared interface embed mirrors the org just written
    shared_changelog.write_text(json.dumps(changelog, indent=2) + "\n", encoding="utf-8")

    embed(interface, org, changelog)
    print(f"validated and embedded {org_path}")
    print(f"version {org['meta']['version']} @ {now}")

    if args.snapshot:
        docs = (args.docs or (repo_root / "docs")).resolve()
        docs.mkdir(parents=True, exist_ok=True)
        slug = org["meta"]["id"]
        snap_html = docs / f"{slug}.html"
        embed(interface, org, changelog, out_html=snap_html)
        snap_png = docs / f"{slug}.png"
        try_snapshot(snap_html, snap_png)
        print(f"snapshot html: {snap_html}")


if __name__ == "__main__":
    main()
