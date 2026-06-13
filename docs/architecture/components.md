---
type: architecture
subtype: components
project: "skills"
status: active
created: "2026-03-26"
updated: "2026-06-12"
tags: [architecture, components]
---

# Components

Registry of all system components. Each entry links to a detail doc when the component has enough substance to warrant one.

## artifact-foundations

**Purpose:** Reference content for building Claude Code skills, commands, and prompts — archetypes, structure rules, exemplars.
**Key files:** `plugins/artifact-foundations/skills/skill-foundations/`, `plugins/artifact-foundations/skills/command-foundations/`, `plugins/artifact-foundations/skills/prompt-foundations/`
**Connections:** Consumed by artifact-builder via INVOKE at runtime. No upstream dependencies.
**Detail:** [components/artifact-foundations.md](components/artifact-foundations.md)

## artifact-builder

**Purpose:** Build and improve Claude Code skills and commands through conversational workflows using archetype-based guidance.
**Key files:** `plugins/artifact-builder/skills/skill-builder/`, `plugins/artifact-builder/skills/command-builder/`
**Connections:** Depends on artifact-foundations (skill-foundations, command-foundations, prompt-foundations) via INVOKE. User-facing.
**Detail:** [components/artifact-builder.md](components/artifact-builder.md)

## homenet-tools

**Purpose:** Discover and map home network devices via nmap, SSH, and DNS with automated topology generation.
**Key files:** `plugins/homenet-tools/skills/homenet-discovery/`
**Connections:** Standalone. Uses nmap, SSH, DNS as external tools.
**Detail:** —

## prompt-tools

**Purpose:** Create and improve prompts using prompt engineering best practices.
**Key files:** `plugins/prompt-tools/commands/create-prompt.md`, `plugins/prompt-tools/commands/improve-prompt.md`
**Connections:** Two slash commands (not skills). Both INVOKE prompt-foundations and read `principles.md`.
**Detail:** —
