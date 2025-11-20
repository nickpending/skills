---
name: skill-name
description: Brief description of documentation provided. USE WHEN user says "[trigger1]", "[trigger2]", "[trigger3]", or [semantic category].
---

# Skill Name

## Overview

[2-3 sentence description of what documentation this skill contains, what it covers, and when to reference it]

<!--
DIRECTORY STRUCTURE:
skill-name/
├── SKILL.md (this file - documentation map)
└── references/
    ├── getting-started.md
    ├── core-concepts.md
    ├── api-reference.md
    ├── examples.md
    └── troubleshooting.md

Replace [placeholders], remove unused sections, keep under 200 lines.
Pure reference skill - no workflows, tools, or procedural execution.
See references/skill-structure.md for structure patterns.
See references/writing-fundamentals.md for writing patterns.
-->

## Documentation Map

### Getting Started

**File:** `references/getting-started.md`

**Contains:**
- [Fundamental concept 1]
- [Fundamental concept 2]
- [Basic usage patterns]

**Read when:**
- New to [subject]
- Need overview of [system/concept]
- Understanding basics

### Core Concepts

**File:** `references/core-concepts.md`

**Contains:**
- [Core concept 1 detailed explanation]
- [Core concept 2 detailed explanation]
- [How concepts interact]

**Read when:**
- Building understanding of [domain]
- Need deep dive on [concept]
- Designing [related feature]

### API Reference

**File:** `references/api-reference.md`

**Contains:**
- [API/interface documentation]
- [Method signatures and parameters]
- [Return types and behaviors]

**Read when:**
- Integrating with [system]
- Need exact specifications
- Implementing [interface]

### Examples

**File:** `references/examples.md`

**Contains:**
- [Common use case examples]
- [Code samples and snippets]
- [Implementation patterns]

**Read when:**
- Need working examples
- Want to see [concept] in practice
- Looking for patterns to follow

### Troubleshooting

**File:** `references/troubleshooting.md`

**Contains:**
- [Common issues and solutions]
- [Error messages and fixes]
- [Debugging approaches]

**Read when:**
- Encountering errors
- Debugging [specific issue]
- Need solutions to common problems

## Navigation Guide

**For quick lookups:**
All reference files use clear section headers. Scan headers first, read relevant sections.

**For comprehensive understanding:**
Read in order: Getting Started → Core Concepts → API Reference → Examples

**For problem solving:**
Start with Troubleshooting, fall back to relevant concept docs if needed.

**For implementation:**
Read Core Concepts + API Reference + Examples together.

## When to Use

**Use this skill when:**
- [Information need 1]
- [Information need 2]
- [Question type this answers]

**Reference Getting Started when:**
- [Specific scenario 1]
- [Specific scenario 2]

**Reference Core Concepts when:**
- [Specific scenario 1]
- [Specific scenario 2]

**Reference API Reference when:**
- [Specific scenario 1]
- [Specific scenario 2]

**Reference Examples when:**
- [Specific scenario 1]
- [Specific scenario 2]

**Reference Troubleshooting when:**
- [Specific scenario 1]
- [Specific scenario 2]

## Common Queries

**Q: [Typical question 1]**
A: See `references/getting-started.md` section on [topic]

**Q: [Typical question 2]**
A: See `references/core-concepts.md` section on [topic]

**Q: [Typical question 3]**
A: See `references/api-reference.md` for [specification]

**Q: [Typical question 4]**
A: See `references/examples.md` example [N]

**Q: [Typical question 5]**
A: See `references/troubleshooting.md` issue [description]

## Examples

**Example 1: [Information lookup]**
```
User: "[Question about basic concept]"
Assistant: Reads references/getting-started.md
Answers: [Information from reference]
```

**Example 2: [Technical specification]**
```
User: "What's the signature of [function/method]?"
Assistant: Reads references/api-reference.md
Answers: [Specification with parameters and return type]
```

**Example 3: [Implementation guidance]**
```
User: "How do I [implement feature]?"
Assistant: Reads references/examples.md
Shows: [Relevant example and pattern]
```

**Example 4: [Problem resolution]**
```
User: "[Error message or issue description]"
Assistant: Reads references/troubleshooting.md
Provides: [Solution or debugging steps]
```

## Reference Organization

**Getting Started** (~200-300 lines)
- High-level overview
- Basic terminology
- Simple usage
- Links to deeper topics

**Core Concepts** (~200-300 lines per major concept)
- Detailed explanations
- How components work
- Relationships and dependencies
- Design rationale

**API Reference** (~200-300 lines per major interface)
- Specifications
- Parameters and types
- Return values and errors
- Usage notes

**Examples** (~200-300 lines)
- Working code samples
- Common patterns
- Best practices
- Anti-patterns to avoid

**Troubleshooting** (~200-300 lines)
- Common errors
- Solutions and workarounds
- Debugging techniques
- Prevention strategies

## Maintenance

**Keeping references current:**
- Update when [system] changes
- Add new examples as patterns emerge
- Document new troubleshooting cases
- Review quarterly for accuracy

**Adding documentation:**
1. Determine which category
2. Create or update reference file
3. Add to Documentation Map
4. Update Common Queries
5. Add navigation guidance

**File size management:**
- Target 200-300 lines per reference
- Split large topics into separate files
- Use clear section headers for scanning
- Cross-reference related topics

## Notes

- Pure reference skill - no execution logic
- Load references on-demand as needed
- Keep documentation map concise
- Use clear navigation guidance
- Cross-reference between files when helpful
- Update regularly as information changes
