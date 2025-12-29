# Exemplar: Knowledge Injection Skill

**Pattern:** Knowledge Injection
**Source:** Claude Code plugins/frontend-design/skills/frontend-design/SKILL.md
**Lines:** 42
**Use when:** Injecting domain expertise without complex workflows - pure thinking guidance

---

## Structure Analysis

- Frontmatter with description (no USE WHEN - older style)
- Brief intro paragraph
- Design Thinking section (questions to ask)
- Guidelines section (domain expertise)
- CRITICAL/IMPORTANT warnings inline
- NEVER anti-patterns

---

## Full Exemplar

```yaml
---
name: frontend-design
description: Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, or applications. Generates creative, polished code that avoids generic AI aesthetics.
license: Complete terms in LICENSE.txt
---
```

```markdown
This skill guides creation of distinctive, production-grade frontend interfaces that avoid generic "AI slop" aesthetics. Implement real working code with exceptional attention to aesthetic details and creative choices.

The user provides frontend requirements: a component, page, application, or interface to build. They may include context about the purpose, audience, or technical constraints.

## Design Thinking

Before coding, understand the context and commit to a BOLD aesthetic direction:
- **Purpose**: What problem does this interface solve? Who uses it?
- **Tone**: Pick an extreme: brutally minimal, maximalist chaos, retro-futuristic, organic/natural, luxury/refined, playful/toy-like, editorial/magazine, brutalist/raw, art deco/geometric, soft/pastel, industrial/utilitarian, etc.
- **Constraints**: Technical requirements (framework, performance, accessibility).
- **Differentiation**: What makes this UNFORGETTABLE? What's the one thing someone will remember?

**CRITICAL**: Choose a clear conceptual direction and execute it with precision. Bold maximalism and refined minimalism both work - the key is intentionality, not intensity.

Then implement working code (HTML/CSS/JS, React, Vue, etc.) that is:
- Production-grade and functional
- Visually striking and memorable
- Cohesive with a clear aesthetic point-of-view
- Meticulously refined in every detail

## Frontend Aesthetics Guidelines

Focus on:
- **Typography**: Choose fonts that are beautiful, unique, and interesting. Avoid generic fonts like Arial and Inter; opt instead for distinctive choices.
- **Color & Theme**: Commit to a cohesive aesthetic. Use CSS variables for consistency. Dominant colors with sharp accents outperform timid palettes.
- **Motion**: Use animations for effects and micro-interactions. Focus on high-impact moments: one well-orchestrated page load with staggered reveals creates more delight than scattered micro-interactions.
- **Spatial Composition**: Unexpected layouts. Asymmetry. Overlap. Diagonal flow. Grid-breaking elements. Generous negative space OR controlled density.
- **Backgrounds & Visual Details**: Create atmosphere and depth rather than defaulting to solid colors.

NEVER use generic AI-generated aesthetics like overused font families (Inter, Roboto, Arial), cliched color schemes (purple gradients on white), predictable layouts.

**IMPORTANT**: Match implementation complexity to the aesthetic vision. Maximalist designs need elaborate code. Minimalist designs need restraint and precision.
```

---

## Key Patterns

1. **No workflows:** Pure expertise injection - no numbered steps
2. **Design Thinking section:** Questions to ask before acting
3. **Guidelines section:** Domain expertise organized by aspect (Typography, Color, Motion, etc.)
4. **CRITICAL/IMPORTANT inline:** Emphasized guidance within flow
5. **NEVER anti-patterns:** What to avoid, explicitly stated
6. **Compact:** ~42 lines - no bloat, pure knowledge
7. **Output expectations:** What the result should be (production-grade, memorable, cohesive)

---

## Knowledge Injection vs Priming

| | Knowledge Injection | Priming |
|---|---|---|
| Type | Skill (auto-triggered) | Command (manual) |
| Purpose | Inject expertise for creation | Load state for orientation |
| After | Produce artifact | Wait for direction |
| Content | Static expertise | Dynamic state |
