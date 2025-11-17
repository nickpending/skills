---
name: homenet-discovery
description: Discovers home network devices via nmap, SSH, and DNS. Creates machine-readable inventory with topology diagrams. Use when mapping networks, discovering devices, creating network inventory, updating inventory, refreshing network data, tracking infrastructure changes, or documenting infrastructure.
model: sonnet
---

# Homenet Discovery

Automatically discover and document home network infrastructure through multi-method discovery and consolidation.

## Overview

Combines nmap scanning, SSH probing, DNS enumeration, and manual data drops to create comprehensive network inventory with topology diagrams. Persists configuration for easy updates.

**Discovery Methods:**
- **nmap** - Network-wide host discovery
- **SSH** - Deep inspection of accessible hosts
- **DNS** - Enumeration and zone transfers
- **Manual drops** - User-provided command outputs

**Outputs:**
- `~/.local/share/homenet/inventory.md` - AI-queryable device inventory
- `~/.local/share/homenet/report.md` - Human-readable summary
- `~/.local/share/homenet/topology.mermaid` - Network topology diagram

## Workflow

Copy to track progress:
```
Homenet Discovery:
- [ ] Step 1: Determine scenario
- [ ] Step 2: Load appropriate workflow
- [ ] Step 3: Execute workflow steps
```

## Execute ALL steps in sequence

### Step 1: Determine Scenario

CHECK for existing configuration at `~/.config/homenet/config.toml`

**IF config exists** (subsequent run):
- Scenario: **Update inventory**
- User wants: Refresh discovery with existing settings
- Workflow: `workflows/update.md`

**IF config missing** (first run):
- Scenario: **Initial discovery**
- User wants: Set up discovery and run first scan
- Workflow: `workflows/discover.md`

### Step 2: Load Workflow

READ the workflow file for the matching scenario:

- **First-time discovery** → READ `workflows/discover.md`
- **Update inventory** → READ `workflows/update.md`

### Step 3: Execute Workflow

Follow workflow instructions exactly as written.

Each workflow contains complete step-by-step discovery procedures.

## Available Scripts

**Discovery:**
- `scripts/setup.sh` - Validate environment and create directories
- `scripts/nmap-scan.sh` - Network scanning (discover|enumerate)
- `scripts/ssh-probe.sh` - SSH-based host inspection
- `scripts/dns-enum.sh` - DNS enumeration and zone transfers

**Processing:**
- `scripts/consolidate.py` - Merge multi-source discovery data
- `parsers/proxmox.py` - Parse Proxmox API outputs
- `parsers/opnsense.py` - Parse OPNsense config XML
- `parsers/unifi.py` - Parse UniFi controller JSON

**Output:**
- `templates/inventory-format.md` - AI inventory template
- `templates/report-format.md` - Human report template
- `templates/topology-template.mermaid` - Diagram template

## Supporting References

- `references/setup-guides.md` - SSH keys, DNS zones, manual drops
- `templates/proxmox-commands.txt` - Proxmox data extraction
- `templates/opnsense-commands.txt` - OPNsense config export
- `templates/unifi-commands.txt` - UniFi API access

## When to Use

**Triggers:**
- "What's on my network?"
- "Map my homelab"
- "Discover network devices"
- "Create network inventory"
- "Generate network topology"
- "Scan home network"

**Use cases:**
- Initial network documentation
- Regular inventory updates
- Infrastructure change tracking
- Service discovery across hosts
- Reverse proxy mapping

## Data Locations

**Configuration:**
- `~/.config/homenet/config.toml` - Discovery settings
- `~/.config/homenet/templates/` - Custom templates

**Inventory:**
- `~/.local/share/homenet/inventory.md` - Current inventory
- `~/.local/share/homenet/report.md` - Human summary
- `~/.local/share/homenet/topology.mermaid` - Network diagram
- `~/.local/share/homenet/cache/` - Historical scans

**Manual inputs:**
- `/tmp/homenet/` - Drop command outputs here

## Reconfiguration

To change discovery settings:
```bash
rm ~/.config/homenet/config.toml
```

Next run will prompt for new configuration.
