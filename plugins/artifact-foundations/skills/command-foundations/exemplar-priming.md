# Exemplar: Priming Command

**Pattern:** Priming
**Source:** prime-homenet pattern
**Lines:** 53
**Use when:** Loading dynamic state for orientation, then waiting for direction

---

## Structure Analysis

- Frontmatter with description only (no tool restrictions)
- Instructions section (focus, expectations, constraints)
- Workflow section (numbered steps)
- Report section (what to confirm)

---

## Full Exemplar

```yaml
---
description: Prime network topology and device inventory from latest homenet-discovery scan
---
```

```markdown
# Prime Network Discovery Context

## Instructions

- Focus on device inventory and network topology, not discovery implementation
- Load SSH access patterns for direct host operations
- Index devices by hostname, IP, type, and services
- After priming, compose SSH/network commands naturally without looking up IPs
- Do NOT read homenet-discovery source code - just the output inventory

## Workflow

1. Read latest inventory JSON:
   ```bash
   cat ~/.local/share/homenet/inventory.json
   ```

2. Extract device mappings with jq:
   ```bash
   # All hosts: IP, hostname, OS
   jq -r '.[] | "\(.ip) \(.hostname) \(.os)"' ~/.local/share/homenet/inventory.json

   # Services by host
   jq -r '.[] | "\(.ip) \(.hostname): \(.services | join(", "))"' ~/.local/share/homenet/inventory.json

   # SSH-accessible hosts
   jq -r '.[] | select(.services[] | contains("ssh")) | "\(.hostname) \(.ip)"' ~/.local/share/homenet/inventory.json

   # Docker hosts
   jq -r '.[] | select(.services | any(contains("docker"))) | "\(.hostname) \(.ip)"' ~/.local/share/homenet/inventory.json

   # Proxmox/hypervisor hosts
   jq -r '.[] | select(.services | any(contains("proxmox") or contains("kvm"))) | "\(.hostname) \(.ip)"' ~/.local/share/homenet/inventory.json

   # All hosts with metadata descriptions (roles)
   jq -r '.[] | select(.metadata.description) | "\(.ip) \(.hostname) - \(.metadata.description)"' ~/.local/share/homenet/inventory.json
   ```

3. Read network topology: `@~/.local/share/homenet/topology.mermaid`
4. Read SSH config: `@~/.ssh/config`

## Report

**Ready for network operations!** Confirm you have indexed:
- Total hosts and key infrastructure (gateways, DNS, storage, etc.)
- SSH-accessible hosts with hostnames
- Services available per host (Docker, Proxmox, k3s, etc.)
- Network segments/VLANs
```

---

## Key Patterns

1. **Focus instructions:** What to load, what NOT to load
2. **Workflow with code blocks:** Actual commands, not pseudo-code
3. **@file includes:** `@~/.ssh/config` injects file contents
4. **Report section:** Confirm what was indexed
5. **Wait for direction:** "Ready for X" implies waiting, not acting
6. **Do NOT constraints:** Explicit boundaries on what to avoid

---

## Priming vs Knowledge Injection

| | Priming (Command) | Knowledge Injection (Skill) |
|---|---|---|
| Trigger | Manual (`/prime`) | Auto (description match) |
| Purpose | Load dynamic state | Inject static expertise |
| Content | Files, inventory, current state | Guidelines, principles, patterns |
| After | Wait for direction | Produce artifact |
