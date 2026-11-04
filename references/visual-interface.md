# Visual interface rail

The org is not only a doc. It has a living map the Chairman can open in a browser.

## Files

| Path | Role |
|---|---|
| `org.json` | Single source of truth (copy per person; examples ship under `examples/`) |
| `schemas/org.schema.json` | Shape and required fields |
| `interface/index.html` | Self-contained map UI (no build step, no CDN) |
| `scripts/update_org.py` | Validate, embed data, changelog, optional snapshot |
| `interface/changelog.json` | Generated history of org updates |
| `docs/` | Preview PNGs for the skill repo |

## How to open the map

**Option A: local server (preferred)**

```bash
cd /path/to/your-org-folder   # folder that contains org.json + interface/
python3 -m http.server 8765
# open http://127.0.0.1:8765/interface/
```

**Option B: open the file directly**

Open `interface/index.html` in a browser. The page ships with an embedded data block (`window.__ORG__`) so `file://` works even when fetching `../org.json` is blocked. After edits to `org.json`, run the update script so the embed refreshes.

## Update script

```bash
python3 scripts/update_org.py --org examples/solo-founder/org.json --message "Added Learning team"
python3 scripts/update_org.py --org examples/solo-founder/org.json --snapshot
```

What it does:

1. Validates required fields and reporting lines
2. Bumps `meta.version` and `meta.updated`
3. Appends a changelog entry
4. Regenerates the embedded data block inside `interface/index.html` (or a copy next to the org)
5. With `--snapshot` and a headless Chrome/Chromium available, writes `docs/org-snapshot.html` and tries `docs/org-snapshot.png`

No heavy dependencies. Stdlib only for the common path.

## Mandatory rule for the master agent

Whenever infrastructure changes (seat added, cut, merged, renamed; skill created, promoted, or retired; reporting line or council change):

1. Propose the change; wait for the Chairman's own yes
2. Edit `org.json`
3. Run `scripts/update_org.py`
4. Send a short change report plus the latest interface (link or attach the snapshot) on whatever channel this setup uses

Optional: a weekly refresh routine that re-renders and sends a one-screen "what changed this week" even if the org was quiet.

## Taste

Default theme tokens live at the top of `interface/index.html` (`:root`). Swap neutrals easily. No brand lock-in.
