# Exemplar: Foundations Skill

**Pattern:** Foundations
**Source:** visual-foundations pattern
**Lines:** ~30
**Use when:** Providing reference content that other skills or contexts consume

---

## Full Exemplar

```yaml
---
name: visual-foundations
description: Visual design language foundations - palettes, aesthetics, CSS variables, render guides. USE WHEN need color values, design tokens, aesthetic guidelines, OR another skill needs visual context.
---
```

```markdown
# visual-foundations

Reference content for the terminal noir design system.

## content routing

| intent | load |
|--------|------|
| palette, colors, colour values | `palette-tokyo-noir.md` or `palette-tokyo-day.md` |
| aesthetic, style, sketch | `aesthetic-sketch.md` |
| photorealistic, cinematic | `aesthetic-photorealistic.md` |
| css, variables, tokens | `css-variables.md` |
| full visual context | all files |

## defaults

- palette: `tokyo-noir` (dark mode)
- aesthetic: `sketch` for diagrams, `photorealistic` for heroes
```

---

## Directory Structure

```
visual-foundations/
├── SKILL.md
├── palette-tokyo-noir.md
├── palette-tokyo-day.md
├── aesthetic-sketch.md
├── aesthetic-photorealistic.md
├── css-variables.md
└── [other content files]
```

---

## Key Patterns

1. **Content routing table** - Maps intent to specific files
2. **Defaults section** - Common choices to reduce decisions
3. **Flat structure** - Content files as siblings to SKILL.md
4. **USE WHEN includes composition** - "another skill needs visual context"
5. **No workflows** - Pure reference content
