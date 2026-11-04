# Guardrails

## Permission tiers

| Tier | Meaning | Default |
|---|---|---|
| `read` | Look up, summarize, draft nothing external | Allowed |
| `draft` | Prepare messages, plans, files for review | Allowed |
| `act_with_approval` | Send, post, spend, delete, share outside after yes | Default for irreversible acts |
| `act_freely` | Named narrow actions the Chairman pre-approved | Only where explicitly listed |

Irreversible by default (need approval every time unless the Chairman widened the tier):

- Send email, chat, SMS, or social posts
- Spend money or move money
- Delete or share private data outside the workspace
- Create, rename, merge, or cut org seats
- Publish or schedule content

## Secrets

Never put API keys, tokens, passwords, or private keys in chat, skills, or `org.json`. Use the person's secret store or environment. If a secret appears in a log, rotate it and scrub the log if possible.

## Quiet hours and rest days

Capture in intake and store on the org:

- Quiet hours (no proactive pings)
- Rest days (no outreach, optional deep-work only rules)

The master agent respects these unless the Chairman overrides in the moment.

## Decision log

Append-only. Each entry:

- Timestamp (with timezone label)
- Decision in one line
- Who said it (must be the Chairman for approvals)
- Link to the brief or message
- Downstream effect (what changed in the org or a job)

Never rewrite history. Corrections are new entries.

## Org change rule

Structural changes (seat add/cut/merge/rename, skill create/promote/retire, reporting line or council change) need Chairman approval, then:

1. Update `org.json`
2. Run `scripts/update_org.py`
3. Send a short change report + latest interface snapshot through the person's channel
