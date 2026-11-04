# agent-council

A portable skill for running your life (or company) with one master agent and a small council of teams underneath it.

You are the **Chairman**. One master agent (call it Jarvis, your main bot, or whatever you like) is the **only** interface that talks to you. It reports up, carries your decisions down, and keeps a council of advisors plus domain teams in sync.

Works for a solo founder, an employee with a side project, a student, a parent, or anyone who wants agent help without a chaotic swarm.

## Who it is for

- People using **Codex**, **Claude Code**, **Cursor**, or any agent that loads `SKILL.md` files
- Anyone who wants hierarchy, reporting, review, and a skills lifecycle without vendor lock-in
- Teams that need guardrails: draft by default, act only with approval
- Visual thinkers who want a living org map they can open locally

## Install

### Codex

```bash
mkdir -p ~/.codex/skills
git clone <this-repo-url> ~/.codex/skills/agent-council
```

Or reference it from `AGENTS.md` in a project:

```markdown
Skills: ~/.codex/skills/agent-council
```

### Claude Code

```bash
mkdir -p ~/.claude/skills
git clone <this-repo-url> ~/.claude/skills/agent-council
```

### Cursor or any agent

Copy or clone this repo into your skills / rules path, or drop `SKILL.md` where your agent looks for skills. Point the agent at `SKILL.md` and the `references/` folder.

## Quick start

1. Open `SKILL.md` with your master agent.
2. Run the **intake interview** (questions in `templates/intake-interview.md`).
3. Copy an example org, or fill `templates/org-chart.md`, then write your `org.json`.
4. Open the visual map (see below). Start with master + 2 or 3 teams.
5. For the first real job, use `templates/delegation-brief.md` and require an independent review before anything reaches you.
6. Log decisions in an append-only decision log. Promote repeated work into skills.

Start tiny. Grow only when workload proves you need another seat.

## Visual map (local HTML)

Source of truth: `org.json`. UI: `interface/index.html` (no CDN, no build step).

```bash
# from this repo (or your org folder that contains interface/ + org.json)
python3 -m http.server 8765
# open http://127.0.0.1:8765/interface/
```

Or open `interface/index.html` directly. The page embeds the latest org so `file://` works. After you edit `org.json`:

```bash
python3 scripts/update_org.py --org path/to/org.json --message "Added Learning team"
python3 scripts/update_org.py --org path/to/org.json --snapshot   # optional PNG in docs/
```

**Mandatory:** whenever seats, skills, council, or reporting lines change, the master agent must (1) get the Chairman's own yes, (2) update `org.json`, (3) run the updater, (4) send a short change report **plus** the latest interface (link or snapshot) back to the Chairman. Details: `references/visual-interface.md`.

Preview stills for the two shipped examples live in `docs/`.

## What is in here

| Path | Purpose |
|---|---|
| `SKILL.md` | The skill the agent loads |
| `org.json` | Default demo org (solo founder); your copy becomes the live source of truth |
| `interface/` | Self-contained org map HTML + changelog |
| `scripts/update_org.py` | Validate, embed, version, changelog, optional snapshot |
| `schemas/org.schema.json` | Shape of `org.json` |
| `references/` | Structure, reporting loop, skills lifecycle, guardrails, visual interface |
| `templates/` | Org chart, seat profile, briefs, retro, skill template, intake |
| `examples/` | Solo founder and full-time nurse + side project (each with its own `org.json`) |
| `docs/` | HTML/PNG snapshots of the example maps |

## Naming note

Folder and skill name: **agent-council**. Alternate name you might prefer: **life-council** (same idea, leans personal rather than company). Pick one and stay consistent.

## License

MIT. See `LICENSE`.
