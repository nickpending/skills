---
name: skill-foundations
description: Skill architecture reference - structure rules, archetypes, exemplars. USE WHEN creating skills, understanding skill patterns, OR another skill needs structural guidance.
---

# skill-foundations

Reference content for building Claude Code skills.

## content routing

| intent | load |
|--------|------|
| structure, frontmatter, naming, format | `structure.md` |
| archetype, pattern, which type | `archetypes.md` |
| when to use a feature, trade-offs, fork vs inline | `decisions.md` |
| feature combinations, recipes | `decisions.md` |
| forked workflow pattern | `archetypes.md` — Forked Workflow section |
| forked validator pattern | `archetypes.md` — Forked Validator section |
| cli wrapper example | `exemplar-cli-wrapper.md` |
| workflow router example | `exemplar-workflow-router.md` |
| foundations example | `exemplar-foundations.md` |
| knowledge injection example | `exemplar-knowledge-injection.md` |
| full skill context | all files |

## defaults

- archetype: start with `archetypes.md` to pick pattern
- structure: always read `structure.md` for universal rules
- exemplar: read ONE relevant exemplar, not all
