# skills Architecture Briefing

## Project Purpose
The `skills` project is a Claude Code plugin marketplace that provides production-ready skills, commands, and foundations for artifact authoring, network discovery, and personal data tools. It is distributed as a single marketplace (`voidwire-skills`) containing multiple plugins, each with their own skills.

## Component Map
```markdown
- **artifact-foundations**
  - Purpose: Reference content for building Claude Code skills, commands, and prompts — archetypes, structure rules, exemplars.
  - Key files: `plugins/artifact-foundations/skills/skill-foundations/`, `plugins/artifact-foundations/skills/command-foundations/`, `plugins/artifact-foundations/skills/prompt-foundations/`
  - Connections: Consumed by artifact-builder via INVOKE at runtime. No upstream dependencies.
- **artifact-builder**
  - Purpose: Build and improve Claude Code skills and commands through conversational workflows using archetype-based guidance.
  - Key files: `plugins/artifact-builder/skills/skill-builder/`, `plugins/artifact-builder/skills/command-builder/`
  - Connections: Depends on artifact-foundations (skill-foundations, command-foundations, prompt-foundations) via INVOKE. User-facing.
- **homenet-tools**
  - Purpose: Discover and map home network devices via nmap, SSH, and DNS with automated topology generation.
  - Key files: `plugins/homenet-tools/skills/homenet-discovery/`
  - Connections: Standalone. Uses nmap, SSH, DNS as external tools.
- **prompt-tools**
  - Purpose: Create and improve prompts using prompt engineering best practices.
  - Key files: `plugins/prompt-tools/`
  - Connections: Depends on prompt-foundations via INVOKE.
```

## Key Boundaries
- **Foundations INVOKE Contract**: Between `artifact-builder ↔ artifact-foundations`. Builder SKILL.md declares `INVOKE` for foundations. Claude loads the foundations skill into context at runtime. Builders must not hardcode foundations content or file paths.
- **Marketplace Plugin Contract**: Between `plugins ↔ .claude-plugin/marketplace.json`. Each plugin has a name, description, version, source path, and category. Source path points to a directory containing the plugin's skills/commands. Version bumps are required on changes.
- **Skill Frontmatter Contract**: Between `skills ↔ Claude Code runtime`. SKILL.md frontmatter fields are parsed by Claude Code to control skill discovery, invocation, and execution behavior. Field semantics are defined by the platform.

## Recent Decisions
- **Prefer $0 dispatch over freeform keyword matching for workflow routers**: Switched to `$0` positional dispatch with `argument-hint: create|improve|validate|migrate [path]`. Argument-hint handles discoverability, $0 handles routing cleanly.
- **Builders delegate to foundations via INVOKE, not duplication**: INVOKE foundations at runtime rather than duplicating content in builder workflows. Foundations updates flow through automatically without requiring builder changes.
- **TaskCreate enforcement for multi-step workflows**: Added TaskCreate gate instructions to multi-step workflows to ensure models follow through more reliably.
- **knowledge-tools removed — superseded by Sable built-ins**: Removed `knowledge-tools` from the marketplace as Sable now includes these built-in capabilities.

## Gotchas
- **Avoid hardcoding foundations content**: Builders must not hardcode foundations content or file paths. Foundations must maintain stable content routing tables.
- **Version bumps required**: Plugins must bump their version on changes to ensure compatibility.
- **Understand INVOKE semantics**: INVOKE is used to dynamically load foundations content at runtime. Ensure your builder skills correctly declare their dependencies.
- **Be mindful of argument-hint usage**: Argument-hint is crucial for discoverability. Ensure your workflows use it effectively.
