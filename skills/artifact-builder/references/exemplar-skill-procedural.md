# Exemplar: Procedural Skill

**Pattern:** Procedural/Development
**Source:** Claude Code plugins/plugin-dev/skills/skill-development/SKILL.md
**Lines:** 638
**Use when:** Teaching how to build/create something with clear steps, validation, and best practices

---

## Structure Analysis

- Frontmatter with third-person trigger phrases
- About section (what this is, what it provides)
- Anatomy (directory structure, file purposes)
- Creation Process (numbered steps 1-6)
- Validation Checklist
- Common Mistakes to Avoid
- Best Practices Summary

---

## Key Sections (condensed)

```yaml
---
name: Skill Development
description: This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill", "improve skill description", "organize skill content", or needs guidance on skill structure, progressive disclosure, or skill development best practices for Claude Code plugins.
version: 0.1.0
---
```

### About Skills

Skills are modular, self-contained packages that extend Claude's capabilities by providing specialized knowledge, workflows, and tools.

### What Skills Provide

1. Specialized workflows - Multi-step procedures for specific domains
2. Tool integrations - Instructions for working with specific file formats or APIs
3. Domain expertise - Company-specific knowledge, schemas, business logic
4. Bundled resources - Scripts, references, and assets for complex tasks

### Anatomy of a Skill

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter metadata (required)
│   └── Markdown instructions (required)
└── Bundled Resources (optional)
    ├── scripts/          - Executable code
    ├── references/       - Documentation
    └── assets/           - Templates, files
```

### Progressive Disclosure

1. **Metadata (name + description)** - Always in context (~100 words)
2. **SKILL.md body** - When skill triggers (<5k words)
3. **Bundled resources** - As needed (unlimited)

### Skill Creation Process

**Step 1:** Understanding with Concrete Examples
**Step 2:** Planning Reusable Contents
**Step 3:** Create Skill Structure
**Step 4:** Edit the Skill (imperative form, third-person description)
**Step 5:** Validate and Test
**Step 6:** Iterate

### Validation Checklist

**Structure:**
- [ ] SKILL.md with valid YAML frontmatter
- [ ] Frontmatter has `name` and `description`
- [ ] Referenced files exist

**Description Quality:**
- [ ] Third person ("This skill should be used when...")
- [ ] Specific trigger phrases
- [ ] Concrete scenarios

**Content Quality:**
- [ ] Imperative/infinitive form
- [ ] Lean (1,500-2,000 words)
- [ ] Detailed content in references/

### Common Mistakes to Avoid

1. **Weak Trigger Description** - Vague, no specific phrases
2. **Too Much in SKILL.md** - 8,000 words instead of 1,800
3. **Second Person Writing** - "You should" instead of imperative

### Best Practices Summary

✅ Third-person description, specific triggers, lean SKILL.md, progressive disclosure, imperative form

❌ Second person, vague triggers, everything in one file, unreferenced resources

---

## Key Patterns

1. **Anatomy section:** Directory structure with file purposes
2. **Numbered steps:** Clear creation process (Step 1-6)
3. **Validation checklist:** Checkbox items for verification
4. **Common mistakes:** Bad/Good examples with "Why bad/good"
5. **Best practices:** ✅ DO / ❌ DON'T format
6. **Progressive disclosure:** Three-level loading explanation
7. **Writing style guidance:** Imperative form, third-person description
