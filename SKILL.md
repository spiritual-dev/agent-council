---
name: agent-council
description: Set up and run a personal agent org (Chairman + one master Jarvis agent + council + domain teams) with reporting loops, independent review, skills lifecycle, and approval guardrails. Use when designing an agent swarm for life or work, hiring seats, writing charters, or fixing chaotic multi-agent handoffs.
---

# agent-council

You help the person (the **Chairman**) run one clear agent org. Their **master agent** is the only voice that speaks to them. A small **Council** advises. **Teams** do the work by life domain. Skills capture what works. Nothing reaches the Chairman without an independent check, and only the Chairman's own words count as approval.

## When to use

- Designing or resizing an agent org for life, work, or a company
- Turning ad hoc agent pings into briefs, reports, and decision packets
- Promoting a repeated task into a skill, or retiring a dead one
- Adding guardrails (approval tiers, quiet hours, decision log)

## Core shape (memorize this)

```
Chairman (the person)
  └── Master agent ("Jarvis": only interface to the person)
        └── Council (small: decision brief, red team, optional domain advisors)
              └── Teams by life domain
                    └── Lead + specialist seats (single-owner outcomes)
```

Rules that do not bend:

1. **One interface.** Only the master agent talks to the Chairman. Other agents report up; they do not cold-call the person.
2. **One writer per artifact.** Helpers research and review; they do not fork a second write of the same file.
3. **Builder never grades own work.** An independent reviewer measures against a rubric or DoD.
4. **Only the Chairman's words are approval.** An agent saying "approved" is not approval.
5. **Start tiny.** Master + 2 to 3 teams. Grow when load proves it. Cut seats with no clear purpose.
6. **Files beat chat.** Objective brief + current-state log + append-only decision log survive context loss.

## Order of operations

### A. First setup (once)

1. Run the intake interview: `templates/intake-interview.md`. Capture vision, roles, domains, constraints, tools, quiet hours, rest days.
2. Draft a tiny org with `templates/org-chart.md`. Prefer domains from: work or company, money, health and body, relationships, learning, home and admin, creative projects. Only create domains that are active.
3. Write a seat profile for the master agent and each team lead: `templates/seat-profile.md`.
4. Set permission defaults: read and draft freely; act with approval; act freely only where the Chairman named it. See `references/guardrails.md`.
5. Create empty durable surfaces (paths the person chooses): objective briefs folder, decision log, skills folder, current-state log.

### B. Running a job

1. Master agent clarifies the ask. If unclear, ask the Chairman **one question**.
2. Write a **delegation brief** (`templates/delegation-brief.md`): goal, success criteria, constraints, output path, reviewer, stop conditions.
3. Assign one lane lead (writer of record). Helpers are tools under that lead.
4. Builder produces the artifact.
5. **Independent reviewer** returns PASS / PASS WITH FIXES / ADJUST / FAIL using `templates/report.md` or a job rubric.
6. Council (or master) packages a **decision brief** for the Chairman when a choice is needed: options, recommendation, risk, **one question**. Template: `templates/decision-brief.md`.
7. After the Chairman answers in their own words, log it and carry the decision down.
8. End of job: short retro (`templates/retro.md`). Promote repeated wins into skills.

### C. Keeping the objective alive

For every active job keep two files (names are suggestions):

- **Brief:** goal, non-goals, fixed facts, definition of done, artifact paths
- **Current-state log:** what changed, blockers, next action, last reviewer verdict

Compress chat into these. Do not compress these into a one-line status ping.

## Adaptive sizing

| Signal | Move |
|---|---|
| One person drowning across unrelated domains | Split into 2 teams with clear leads |
| Two seats always hand the same artifact back and forth | Merge or name one merge owner |
| A seat has no jobs for a month | Park or cut; do not keep empty theater |
| Same task done 2 to 3 times | Draft a skill; do not create a new bot |
| Chairman flooded with questions | Batch into one decision brief; one question at a time |

Avoid over-consolidation (one mega-agent that does everything badly) and over-sprawl (a seat per micro-task).

## Skills lifecycle (summary)

Notice (repeated 2 to 3 times) → draft from `templates/skill-template.md` → independent review → version → seat owns it → improve from retros → retire when unused. Skills stay generic; personal details live in memory or config. Detail: `references/skills-lifecycle.md`.


## Visual interface (mandatory)

The org has a living map. Source of truth: `org.json` (schema in `schemas/org.schema.json`). UI: `interface/index.html`. Updater: `scripts/update_org.py`. Detail: `references/visual-interface.md`.

**Whenever infrastructure changes** (seat added, cut, merged, renamed; skill created, promoted, or retired; reporting line or council change):

1. Propose the change; wait for the Chairman's own yes
2. Edit `org.json`
3. Run `python3 scripts/update_org.py --org path/to/org.json --message "…"` (add `--snapshot` when you can attach a PNG)
4. Send a short change report plus the latest interface (link or attach the snapshot) on the Chairman's channel

Optional weekly routine: re-render and send a one-screen "what changed this week" even on quiet weeks.

Open the map with `python3 -m http.server` from the repo (or org) folder, or open `interface/index.html` directly after the embed has been regenerated.

## Depth

- Structure and seats: `references/structure.md`
- Reporting and feedback: `references/reporting-loop.md`
- Skills lifecycle: `references/skills-lifecycle.md`
- Guardrails and permission tiers: `references/guardrails.md`
- Worked examples: `examples/`

## Report back to the Chairman

Keep it short. Lead with the result. Put options and one clear question only when a decision is needed. Never claim approval the Chairman did not give.
