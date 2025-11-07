# Initial Network Discovery

First-time network discovery with configuration setup.

## Execution Requirements

**YOU MUST execute these steps sequentially.**

This workflow configures discovery methods, runs multi-source scanning, and generates network inventory. Each step builds on previous steps. Do not skip ahead.

## Step 0: Validate Environment

**REQUIRED ACTIONS:**

1. RUN setup script:
   ```bash
   bash scripts/setup.sh
   ```

2. PARSE output for status indicators

3. CHECK prerequisites status:
   - IF `PREREQUISITES: ALL_INSTALLED` → Proceed to Step 1
   - IF `PREREQUISITES: MISSING` → CHECK which tools

4. **IF tools missing:**
   - EXTRACT `MISSING_TOOL:` lines
   - EXTRACT `INSTALL_HINT:` lines
   - SHOW hints to user
   - **IF `MISSING_TOOL: python3`:**
     - STOP - python3 required
     - INFORM user: "python3 required. Install hints shown above."
   - **IF other tools missing (nmap, dig, ssh):**
     - NOTE which methods will be disabled
     - CONTINUE to Step 1

**VERIFICATION:**
Setup script ran and directories created.

**STOP before Step 1.**

## Step 1: Ask Discovery Preferences

**REQUIRED ACTIONS:**

1. SHOW brief overview to user:
   ```
   # homenet - First-Time Setup

   Discovery supports multiple methods. All are optional:

   - **Nmap:** Network-wide host scanning (basic discovery)
   - **SSH:** Deep inspection via authorized_keys (no passwords stored)
   - **DNS:** Zone transfers and queries for service discovery
   - **Manual files:** Command outputs you provide (RECOMMENDED - most detail)

   Manual files let you drop Proxmox/OPNsense/UniFi data for richer inventory.
   ```

2. ASK user questions using AskUserQuestion tool:

   **Q1 - DNS Server (header: "DNS Server"):**
   - question: "What's your local DNS server IP?"
   - options:
     - "Auto-detect (use /etc/resolv.conf)"
     - "192.168.1.1"
     - "10.0.0.1"
     - "172.16.0.1"

   **Q2 - Network Range (header: "Network"):**
   - question: "What is your primary home network range?"
   - options:
     - "192.168.1.0/24"
     - "192.168.0.0/24"
     - "10.0.0.0/24"
     - "172.16.0.0/16"

   **Q3 - Methods (header: "Methods", multiSelect: true):**
   - question: "Which discovery methods should be enabled?"
   - options:
     - "Nmap scanning (recommended)"
     - "SSH probing (requires keys)"
     - "DNS enumeration"
     - "Manual file parsing"

   **Q4 - SSH User (header: "SSH User", only if Q3 includes SSH):**
   - question: "What username for SSH connections?"
   - options:
     - "Current user ($USER)"
     - "root"
     - "admin"
     - "ubuntu"

   **Q5 - DNS Domain (header: "Domain", only if Q3 includes DNS):**
   - question: "What is your local DNS domain?"
   - options:
     - "Auto-detect (from hostname)"
     - "home.lab"
     - "local"
     - "lan"

3. WAIT for user responses

4. RECORD all answers for Step 3

**VERIFICATION:**
All questions answered and recorded.

**STOP before Step 2.**

## Step 2: Show Setup Instructions

**REQUIRED ACTIONS:**

1. ANALYZE Q3 answers from Step 1

2. **IF "SSH probing" selected:**
   - READ `references/setup-guides.md` section "SSH Key Setup"
   - SHOW SSH setup instructions to user
   - SUBSTITUTE {username} with Q4 answer

3. **IF "DNS enumeration" selected:**
   - READ `references/setup-guides.md` section "DNS Zone Transfer Setup"
   - SHOW DNS setup instructions to user

4. **IF "Manual file parsing" selected:**
   - READ `references/setup-guides.md` section "Manual Command Outputs"
   - SHOW manual file instructions to user

5. ASK: "Setup instructions shown above. Ready to proceed with discovery?"

6. WAIT for user confirmation

**VERIFICATION:**
User confirmed ready to proceed.

**STOP before Step 3.**

## Step 3: Save Configuration

**REQUIRED ACTIONS:**

1. CREATE config file at `~/.config/homenet/config.toml`

2. WRITE config with user's answers:
   ```toml
   [general]
   first_run_complete = true
   last_scan = "{YYYY-MM-DD}"

   [dns]
   servers = ["{from-Q1}"]
   domains = ["{from-Q5-or-empty}"]

   [network]
   subnets = ["{from-Q2}"]

   [methods]
   nmap = {true/false from Q3}
   ssh = {true/false from Q3}
   dns_enum = {true/false from Q3}
   manual_drops = {true/false from Q3}

   [ssh]
   default_user = "{from-Q4-or-$USER}"
   known_hosts = []

   [output]
   formats = ["json", "markdown", "mermaid"]
   path = "~/.local/share/homenet"
   ```

3. SHOW: "Configuration saved to ~/.config/homenet/config.toml"

**VERIFICATION:**
Config file created and populated.

**STOP before Step 4.**

## Step 4: Run Discovery

**REQUIRED ACTIONS:**

1. READ `~/.config/homenet/config.toml`

2. PARSE TOML to extract enabled methods

3. RUN enabled discovery methods (4a-4d)

### 4a. Parse Manual Drops (if enabled)

**IF `methods.manual_drops = true`:**

1. RUN:
   ```bash
   ls -1 /tmp/homenet/ 2>/dev/null
   ```

2. **FOR each file found:**
   - CHECK filename pattern
   - **IF proxmox-nodes.json:**
     ```bash
     cat /tmp/homenet/proxmox-nodes.json | python3 parsers/proxmox.py nodes
     ```
   - **IF proxmox-resources.json:**
     ```bash
     cat /tmp/homenet/proxmox-resources.json | python3 parsers/proxmox.py resources
     ```
   - **IF opnsense-config.xml:**
     ```bash
     cat /tmp/homenet/opnsense-config.xml | python3 parsers/opnsense.py
     ```
   - **IF unifi-devices.json:**
     ```bash
     cat /tmp/homenet/unifi-devices.json | python3 parsers/unifi.py
     ```

3. EXTRACT IPs from parser outputs

4. STORE for use in other discovery methods

### 4b. Nmap Discovery (if enabled)

**IF `methods.nmap = true`:**

1. EXTRACT subnets from `network.subnets` in config

2. **FOR each subnet:**
   - RUN discovery scan:
     ```bash
     ./scripts/nmap-scan.sh discover {subnet}
     ```
   - COLLECT live host IPs, MACs, vendors

3. COMBINE all discovered IPs

4. RUN service enumeration:
   ```bash
   ./scripts/nmap-scan.sh enumerate {comma-separated-ips}
   ```

5. COLLECT services per host (ports, banners)

### 4c. SSH Discovery (if enabled)

**IF `methods.ssh = true`:**

1. EXTRACT default_user from `ssh.default_user` in config

2. GET all discovered host IPs from previous steps

3. **FOR each host IP:**
   - RUN SSH probe:
     ```bash
     ./scripts/ssh-probe.sh {default_user}@{host-ip}
     ```
   - SILENTLY skip connection failures
   - COLLECT structured output:
     - SYSTEM → OS info
     - HOSTNAME → Hostname
     - INTERFACES → Network interfaces
     - DOCKER → Container names/images
     - SERVICES → systemd services
     - PROXY_CONFIGS → Reverse proxy configs

4. **IF PROXY_CONFIGS found:**
   - EXTRACT domain → backend mappings
   - STORE proxy route information

### 4d. DNS Discovery (if enabled)

**IF `methods.dns_enum = true`:**

1. EXTRACT dns.servers and dns.domains from config

2. **IF dns.domains is empty:**
   - INFORM user: "DNS enumeration enabled but no domains configured. Edit config or skip."
   - SKIP DNS discovery

3. **IF dns.domains not empty:**
   - **FOR each server + domain combination:**
     ```bash
     ./scripts/dns-enum.sh {dns-server} {domain}
     ```
   - COLLECT DNS A records (hostname, IP)

**VERIFICATION:**
All enabled discovery methods completed.

**STOP before Step 5.**

## Step 5: Consolidate Results

**REQUIRED ACTIONS:**

1. RUN consolidation script:
   ```bash
   python3 scripts/consolidate.py \
     /tmp/homenet/discovery-*.json \
     > /tmp/homenet/inventory-consolidated.json
   ```

2. VERIFY output file created

3. CHECK consolidation used trust hierarchy:
   - SSH > nmap > DNS > manual

4. VERIFY deduplication by MAC or IP

**VERIFICATION:**
Consolidated inventory JSON created.

**STOP before Step 6.**

## Step 6: Generate Outputs

**REQUIRED ACTIONS:**

1. READ `/tmp/homenet/inventory-consolidated.json`

2. GENERATE AI inventory:
   - READ `templates/inventory-format.md` for structure
   - WRITE structured markdown to `~/.local/share/homenet/inventory.md`

3. GENERATE human report:
   - READ `templates/report-format.md` for structure
   - WRITE summary tables to `~/.local/share/homenet/report.md`

4. GENERATE Mermaid topology:
   - READ `templates/topology-template.mermaid` for structure
   - INCLUDE hosts with IPs and services
   - INCLUDE VLANs if detected
   - INCLUDE proxy routes if found
   - WRITE diagram to `~/.local/share/homenet/topology.mermaid`

**VERIFICATION:**
All three output files created.

**STOP before Step 7.**

## Step 7: Cache Results

**REQUIRED ACTIONS:**

1. RUN:
   ```bash
   cp ~/.local/share/homenet/inventory.json \
      ~/.local/share/homenet/cache/last-scan-$(date +%Y-%m-%d).json
   ```

2. VERIFY cached copy created

**VERIFICATION:**
Results cached with date stamp.

**STOP before Step 8.**

## Step 8: Report Summary

**REQUIRED ACTIONS:**

1. COUNT discovered hosts from consolidated inventory

2. COUNT subnets scanned

3. LIST enabled methods from config

4. SHOW summary to user:
   ```
   Network discovery complete!

   Discovered: {N} hosts across {M} subnets
   Methods used: {enabled methods}

   Outputs saved:
   - ~/.local/share/homenet/inventory.md
   - ~/.local/share/homenet/report.md
   - ~/.local/share/homenet/topology.mermaid

   Other skills can now query your network inventory.
   ```

5. CHECK if specific platforms detected in inventory:
   - **IF Proxmox detected:**
     - READ `templates/proxmox-commands.txt`
     - SHOW relevant commands to user
   - **IF OPNsense/pfSense detected:**
     - READ `templates/opnsense-commands.txt`
     - SHOW relevant instructions to user
   - **IF UniFi detected:**
     - READ `templates/unifi-commands.txt`
     - SHOW relevant commands to user

6. SHOW reconfiguration hint:
   ```
   To reconfigure: rm ~/.config/homenet/config.toml and re-run
   To refresh inventory: re-run this skill anytime
   ```

**Discovery workflow complete.**

## Key Principles

**Multi-source consolidation:**
- Each method provides different detail levels
- SSH gives deepest inspection
- Manual drops provide infrastructure APIs
- Consolidation merges all sources intelligently

**Persistent configuration:**
- Config saved for future updates
- No re-prompting on subsequent runs
- Easy reconfiguration by deleting config

**Non-destructive:**
- All discovery is read-only
- No changes to network devices
- Safe to run repeatedly
