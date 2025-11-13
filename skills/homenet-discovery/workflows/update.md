# Update Network Inventory

Refresh network inventory using existing configuration.

## Execution Requirements

**YOU MUST execute these steps sequentially.**

This workflow loads existing configuration and re-runs discovery to update inventory. Faster than initial discovery - no setup questions.

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
   - **IF other tools missing:**
     - NOTE which methods will be disabled
     - CONTINUE to Step 1

**VERIFICATION:**
Setup script ran successfully.

**STOP before Step 1.**

## Step 1: Load Configuration

**REQUIRED ACTIONS:**

1. READ `~/.config/homenet/config.toml`

2. PARSE TOML configuration

3. EXTRACT enabled methods from `[methods]` section

4. SHOW brief status:
   ```
   Refreshing network inventory...

   Using existing configuration:
   - Network: {network.subnets}
   - Methods: {enabled methods from methods section}
   ```

**VERIFICATION:**
Configuration loaded and methods identified.

**STOP before Step 2.**

## Step 2: Run Discovery

**REQUIRED ACTIONS:**

Execute enabled discovery methods (2a-2d).

### 2a. Parse Manual Drops (if enabled)

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
     cat /tmp/homenet/opnsense-config.xml | python3 parsers/opnsense.py vlans
     ```
   - **IF unifi-devices.json:**
     ```bash
     cat /tmp/homenet/unifi-devices.json | python3 parsers/unifi.py
     ```

3. EXTRACT IPs from parser outputs

4. STORE for use in other discovery methods

### 2b. Nmap Discovery (if enabled)

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

### 2c. SSH Discovery (if enabled)

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

### 2d. DNS Discovery (if enabled)

**IF `methods.dns_enum = true`:**

1. EXTRACT dns.servers and dns.domains from config

2. **IF dns.domains is empty:**
   - INFORM user: "DNS enumeration enabled but no domains configured."
   - SKIP DNS discovery

3. **IF dns.domains not empty:**
   - **FOR each server + domain combination:**
     ```bash
     ./scripts/dns-enum.sh {dns-server} {domain}
     ```
   - COLLECT DNS A records (hostname, IP)

**VERIFICATION:**
All enabled discovery methods completed.

**STOP before Step 3.**

## Step 3: Consolidate Results

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

**STOP before Step 4.**

## Step 4: Generate Outputs

**REQUIRED ACTIONS:**

1. READ `/tmp/homenet/inventory-consolidated.json`

2. PARSE consolidated JSON structure:
   - EXTRACT `hosts` array for host inventory
   - EXTRACT `vlans` array for VLAN data (may be empty)

3. GENERATE AI inventory:
   - READ `templates/inventory-format.md` for structure
   - USE hosts data from consolidated JSON
   - WRITE structured markdown to `~/.local/share/homenet/inventory.md`

4. GENERATE human report:
   - READ `templates/report-format.md` for structure
   - USE hosts data from consolidated JSON
   - WRITE summary tables to `~/.local/share/homenet/report.md`

5. GENERATE Mermaid topology:
   - READ `templates/topology-template.mermaid` for structure
   - INCLUDE all hosts with IPs and services
   - INCLUDE VLANs if vlans array not empty
   - INCLUDE proxy routes if found in host data
   - WRITE diagram to `~/.local/share/homenet/topology.mermaid`

**VERIFICATION:**
All three output files created.

**STOP before Step 5.**

## Step 5: Cache Results

**REQUIRED ACTIONS:**

1. RUN:
   ```bash
   cp ~/.local/share/homenet/inventory.json \
      ~/.local/share/homenet/cache/last-scan-$(date +%Y-%m-%d).json
   ```

2. VERIFY cached copy created

**VERIFICATION:**
Results cached with date stamp.

**STOP before Step 6.**

## Step 6: Report Summary

**REQUIRED ACTIONS:**

1. COUNT discovered hosts from consolidated inventory

2. COUNT subnets scanned

3. LIST enabled methods from config

4. SHOW summary to user:
   ```
   Network inventory updated!

   Discovered: {N} hosts across {M} subnets
   Methods used: {enabled methods}

   Outputs refreshed:
   - ~/.local/share/homenet/inventory.md
   - ~/.local/share/homenet/report.md
   - ~/.local/share/homenet/topology.mermaid

   Previous scan cached in cache/ directory.
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
   To reconfigure discovery: rm ~/.config/homenet/config.toml and re-run
   ```

**Update workflow complete.**

## Key Principles

**Fast refresh:**
- Skips configuration questions
- Uses saved preferences
- Runs same methods as initial discovery

**Incremental updates:**
- Previous scans cached by date
- Easy to compare inventory over time
- Track infrastructure changes

**Consistent results:**
- Same consolidation logic
- Same trust hierarchy
- Same output formats
