---
name: skill-name
description: Brief description of domain knowledge provided. Use when [specific domain questions or contexts]. Include natural scenarios.
allowed-tools: Read, Grep
---

# Skill Name

## Overview

[2-3 sentence description of what domain knowledge this skill provides, when it's needed during work, and what questions it answers]

<!--
DIRECTORY STRUCTURE:
skill-name/
├── SKILL.md (this file - reference map)
└── references/
    ├── topic-a.md (200-300 lines)
    ├── topic-b.md (200-300 lines)
    ├── topic-c.md (200-300 lines)
    └── schemas.md (database schemas, API specs, etc.)

Replace [placeholders], remove unused sections, keep under 200 lines.
Reference files load on-demand - keep map concise and navigable.
See references/skill-structure.md for structure patterns.
See references/writing-fundamentals.md for writing patterns.
-->

## Available Documentation

### Topic A: [Subject Name]

**File:** `references/topic-a.md`

**Contains:**
- [Key concept 1]
- [Key concept 2]
- [Key concept 3]

**Use when:**
- [Scenario requiring this knowledge]
- [Question type this answers]

### Topic B: [Subject Name]

**File:** `references/topic-b.md`

**Contains:**
- [Key concept 1]
- [Key concept 2]
- [Key concept 3]

**Use when:**
- [Scenario requiring this knowledge]
- [Question type this answers]

### Topic C: [Subject Name]

**File:** `references/topic-c.md`

**Contains:**
- [Key concept 1]
- [Key concept 2]
- [Key concept 3]

**Use when:**
- [Scenario requiring this knowledge]
- [Question type this answers]

### Schemas and Specifications

**File:** `references/schemas.md`

**Contains:**
- [Schema or spec 1]
- [Schema or spec 2]
- [Schema or spec 3]

**Use when:**
- [Need technical specifications]
- [Need data structure definitions]

## How to Use

### Step 1: Identify Information Need

ANALYZE user's question or task to determine what knowledge required.

MATCH need against available documentation above.

### Step 2: Load Reference

READ appropriate `references/[topic].md` file.

**IF specific detail needed and file is large:**
- USE grep patterns below to find exact section
- LOAD only relevant portion

### Step 3: Apply Knowledge

EXTRACT relevant information from loaded reference.

ANSWER user's question with domain knowledge.

CITE reference file and section if applicable.

## Search Patterns

For large reference files (>300 lines), use grep to find specific content:

**Find [specific concept]:**
```bash
grep -n "pattern" references/topic-a.md
```

**Find [database schema]:**
```bash
grep -A 10 "table_name" references/schemas.md
```

**Find [API endpoint]:**
```bash
grep -B 2 -A 5 "endpoint_path" references/api-docs.md
```

**Find [configuration option]:**
```bash
grep "config_key" references/topic-b.md
```

## When to Use

**Use this skill when:**
- [Domain question type 1]
- [Domain question type 2]
- [Task requiring domain knowledge]

**Load references when:**
- Building [related feature]
- Debugging [domain-specific issue]
- Answering [type of question]

**Don't load when:**
- [Unrelated task type]
- [Common knowledge doesn't need reference]

## Reference Organization

**Topic A:** [Brief description of scope]
- Covers [subtopic 1]
- Includes [subtopic 2]
- Documents [subtopic 3]

**Topic B:** [Brief description of scope]
- Covers [subtopic 1]
- Includes [subtopic 2]
- Documents [subtopic 3]

**Topic C:** [Brief description of scope]
- Covers [subtopic 1]
- Includes [subtopic 2]
- Documents [subtopic 3]

## Common Questions

**Q: [Typical question 1]**
A: See `references/topic-a.md` section on [subject]

**Q: [Typical question 2]**
A: See `references/topic-b.md` section on [subject]

**Q: [Typical question 3]**
A: See `references/schemas.md` for [specification]

## Examples

**Example 1: [Common use case]**
```
User: "[Question about domain topic A]"
Assistant: Reads references/topic-a.md
Answers: [Information from reference]
```

**Example 2: [Another use case]**
```
User: "What's the schema for [entity]?"
Assistant: Greps references/schemas.md for [entity]
Answers: [Schema definition]
```

**Example 3: [Complex question]**
```
User: "[Question spanning multiple topics]"
Assistant: Reads references/topic-a.md and references/topic-b.md
Answers: [Synthesized information]
```

## Maintenance

**Adding references:**
1. Create reference file in references/
2. Add to Available Documentation section
3. Document what it contains
4. Add to Search Patterns if large file
5. Update Common Questions

**Keeping references current:**
- Review when domain changes
- Update schemas when APIs change
- Add new patterns as discovered
- Remove outdated information

**File size management:**
- Target 200-300 lines per reference
- Split large topics into multiple files
- Add grep patterns for files >300 lines
- Consider splitting by subtopic
