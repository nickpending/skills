#!/usr/bin/env python3
"""
proxmox.py - Parse Proxmox JSON outputs into unified host format
"""

import json
import sys
from typing import List, Dict, Any


def parse_proxmox_nodes(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Parse Proxmox nodes JSON"""
    hosts = []

    for node in data:
        host = {
            "ip": node.get("ip", ""),
            "hostname": node.get("node", ""),
            "mac": "",  # Not in node data
            "os": f"Proxmox VE {node.get('version', 'unknown')}",
            "services": ["proxmox", "kvm"],
            "discovered_by": ["manual-proxmox"],
            "metadata": {
                "type": "hypervisor",
                "status": node.get("status", "unknown"),
                "uptime": node.get("uptime", 0),
                "cpu_count": node.get("maxcpu", 0),
                "mem_total": node.get("maxmem", 0),
            },
        }
        hosts.append(host)

    return hosts


def parse_proxmox_resources(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Parse Proxmox cluster resources JSON"""
    hosts = []

    for resource in data:
        res_type = resource.get("type", "")

        # Only process VMs and containers
        if res_type not in ["qemu", "lxc"]:
            continue

        # Try to get IP from config (may not be available)
        ip = ""
        if "netout" in resource or "netin" in resource:
            # VM is running, might have network info
            ip = resource.get("ip", "")

        host = {
            "ip": ip,
            "hostname": resource.get("name", ""),
            "mac": "",  # Not in resource data
            "os": "VM" if res_type == "qemu" else "LXC",
            "services": [],
            "discovered_by": ["manual-proxmox"],
            "metadata": {
                "type": "vm" if res_type == "qemu" else "container",
                "status": resource.get("status", "unknown"),
                "vmid": resource.get("vmid", ""),
                "node": resource.get("node", ""),
                "cpu_count": resource.get("maxcpu", 0),
                "mem_total": resource.get("maxmem", 0),
            },
        }
        hosts.append(host)

    return hosts


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: proxmox.py <nodes|resources> < input.json", file=sys.stderr)
        sys.exit(1)

    mode = sys.argv[1]

    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON: {e}", file=sys.stderr)
        sys.exit(1)

    if mode == "nodes":
        hosts = parse_proxmox_nodes(
            data if isinstance(data, list) else data.get("data", [])
        )
    elif mode == "resources":
        hosts = parse_proxmox_resources(
            data if isinstance(data, list) else data.get("data", [])
        )
    else:
        print(
            f"ERROR: Unknown mode '{mode}'. Use 'nodes' or 'resources'", file=sys.stderr
        )
        sys.exit(1)

    print(json.dumps(hosts, indent=2))


if __name__ == "__main__":
    main()
