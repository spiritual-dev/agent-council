# Structure

## Roles

| Role | Who | Job |
|---|---|---|
| Chairman | The person | Vision, values, final yes/no. Never an agent. |
| Master agent | One bot (Jarvis, main bot, Codex, Claude, Cursor agent, etc.) | Only interface to the Chairman. Talks, reports, carries decisions down. |
| Council | Small set of advisor seats | Decision briefs, red team, optional domain counsel. Not a chat room. Summon 1 to 3 per decision. |
| Team lead | One seat per active domain | Owns outcomes for that domain. Single write path for domain artifacts. |
| Specialist | Seat under a lead | Narrow craft. Reports to the lead. |

## Default life domains (adapt)

Use only what is active for this person:

1. Work or company
2. Money
3. Health and body
4. Relationships
5. Learning
6. Home and admin
7. Creative projects

An employee with a side project might start with: Work, Money, Creative. A parent might start with: Home and admin, Relationships, Learning. A founder might start with: Work or company, Money, Creative.

## Council seats (typical)

Keep this small. Examples, not mandates:

- **Decision brief seat:** turns options into a one-question packet for the Chairman
- **Red team:** attacks premises, finds missing risks
- **Optional advisors:** money, health, craft; call only when the decision needs them

Council is on-call, not always online.

## Seat design rules

1. Every seat has a clear purpose and a measurable outcome, or it gets cut.
2. One owner of the write path per artifact.
3. Prefer a skill or a temporary job seat over a permanent new bot for a micro-need.
4. Park idle seats before deleting; revive when load returns.
5. Name seats by role outcome (Editor, Reviewer), not by copying a human's whole personality.

## Org source of truth

The living map of the org is `org.json` (schema in `schemas/org.schema.json`). The visual interface in `interface/` reads that file. Whenever infrastructure changes, update `org.json`, run `scripts/update_org.py`, and send the Chairman a short change report plus the latest interface snapshot. See `references/visual-interface.md`.
