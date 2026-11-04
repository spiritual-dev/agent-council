# Skills lifecycle

Skills are reusable procedures. They are not bots. Personal details live in memory or config, not inside the shared skill text.

## Stages

| Status | Meaning |
|---|---|
| `noticed` | Same task done ~2 to 3 times |
| `draft` | Written from the skill template; not trusted yet |
| `reviewed` | Independent reviewer passed it |
| `active` | In use; has an owning seat and a version |
| `retired` | Unused or replaced; kept for history |

## Loop

1. **Notice.** A seat or the master agent flags a repeated task.
2. **Draft.** Use `templates/skill-template.md`. Keep steps generic. Put names, channels, and paths in config/memory.
3. **Review.** Someone who did not draft it checks clarity, safety, and "when to use".
4. **Version.** Start at `0.1.0` for drafts, `1.0.0` when active. Bump minor for improvements, major for breaking changes.
5. **Own.** Every active skill has one owning seat. That seat keeps it honest.
6. **Improve.** Retros and failed jobs feed edits.
7. **Retire.** If unused for a long stretch or replaced, mark `retired` in `org.json`. Do not delete history blindly.

## What belongs in a skill vs memory

| In the skill | In memory / config |
|---|---|
| When to use | The person's name, brands, private URLs |
| Ordered steps | Channel IDs, emails, phone numbers |
| Definition of done | API keys, tokens |
| Guardrails | Preferred vendors that change often |
| Templates and checklists | One-off project paths |

## Tie-in to the visual map

`org.json` lists skills with `id`, `name`, `owner`, `version`, `status`. The interface skills panel shows draft → reviewed → active → retired. Updating a skill status is an infrastructure change: run `scripts/update_org.py` and notify the Chairman.
