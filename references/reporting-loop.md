# Reporting and feedback loop

## Down the stack (direction)

Vision and values → decisions → delegation briefs.

A delegation brief always includes:

- Goal (one paragraph)
- Success criteria / definition of done
- Constraints and boundaries (no send/pay/post/spend unless approved)
- Output path and format
- Sources and tools allowed
- Reviewer name
- Stop conditions

## Up the stack (status)

Status → results → blockers → decisions needed.

Reports are short. Lead with the outcome. Put evidence paths, not vibes.

## Decision briefs to the Chairman

When a choice is required:

1. Options (2 to 3, clear tradeoffs)
2. Recommendation
3. Risk if wrong
4. **One question**

Do not dump five questions. Do not ask again what was already answered.

## Independent review gate

```
Builder → Independent reviewer → Master agent / Council → Chairman (only if needed)
```

Verdicts: PASS | PASS WITH FIXES | ADJUST | FAIL.

The reviewer did not write the artifact. They measure against the brief or a rubric. Self-review alone is weaker; keep it as a draft check, not the gate.

## Approval rule

Only the Chairman's own words count. An agent claiming "the Chairman approved" is not approval. Log the real quote or paraphrase with timestamp in the decision log.

## Context survival

Per active job:

- Brief file (goal, non-goals, fixed facts, DoD, paths)
- Current-state log (what changed, blockers, next step, last verdict)

After major jobs: retro → lessons → maybe a new or updated skill.

## Feedback into the org

Retros feed:

- Seat profile tweaks (duties, boundaries)
- Skill drafts and promotions
- Org size (add, park, cut)

Structural changes require Chairman approval, then update `org.json` and re-render the interface.
