#!/usr/bin/env python3
"""
consolidate.py - Merge discovery data into unified inventory
"""

import json
import sys
from collections import defaultdict
from typing import Dict, List, Any
from pathlib import Path


# Trust hierarchy for conflicting data
TRUST_ORDER = {
    "ssh": 4,
    "nmap": 3,
    "dns": 2,
    "manual-opnsense": 1,
    "manual-proxmox": 1,
    "manual-unifi": 1,
}


def trust_level(discovered_by: List[str]) -> int:
    """Calculate trust level based on discovery methods"""
    return max((TRUST_ORDER.get(method, 0) for method in discovered_by), default=0)


def merge_host_data(existing: Dict[str, Any], new: Dict[str, Any]) -> Dict[str, Any]:
    """Merge two host records, preferring higher-trust data"""

    existing_trust = trust_level(existing.get("discovered_by", []))
    new_trust = trust_level(new.get("discovered_by", []))

    # Merge discovered_by lists
    discovered_by = list(
        set(existing.get("discovered_by", []) + new.get("discovered_by", []))
    )

    # Choose data source based on trust
    if new_trust > existing_trust:
        primary = new
        secondary = existing
    else:
        primary = existing
        secondary = new

    merged = {
        "ip": primary.get("ip") or secondary.get("ip", ""),
        "mac": primary.get("mac") or secondary.get("mac", ""),
        "hostname": primary.get("hostname") or secondary.get("hostname", ""),
        "os": primary.get("os") or secondary.get("os", ""),
        "services": list(
            set(primary.get("services", []) + secondary.get("services", []))
        ),
        "discovered_by": discovered_by,
        "metadata": {**secondary.get("metadata", {}), **primary.get("metadata", {})},
        "proxy_routes": primary.get("proxy_routes", [])
        or secondary.get("proxy_routes", []),
    }

    return merged


def normalize_host(host: Dict[str, Any], source_file: str) -> Dict[str, Any]:
    """Normalize host data to unified format based on source"""

    # Detect source type from filename or data structure
    if "discovery-nmap" in source_file:
        # nmap format: {ip, services, mac, vendor}
        return {
            "ip": host.get("ip", ""),
            "mac": host.get("mac", ""),
            "hostname": "",
            "os": "",
            "services": host.get("services", []),
            "discovered_by": ["nmap"],
            "metadata": {"vendor": host.get("vendor", "")}
            if host.get("vendor")
            else {},
            "proxy_routes": [],
        }
    elif "discovery-ssh" in source_file:
        # ssh format: {ip, hostname, os, services, interfaces, containers}
        return {
            "ip": host.get("ip", ""),
            "mac": "",
            "hostname": host.get("hostname", ""),
            "os": host.get("os", ""),
            "services": host.get("services", []),
            "discovered_by": ["ssh"],
            "metadata": {
                "interfaces": host.get("interfaces", {}),
                "containers": host.get("containers", []),
            },
            "proxy_routes": host.get("proxy_routes", []),
        }
    elif "discovery-dns" in source_file:
        # dns format: {hostname, ip}
        return {
            "ip": host.get("ip", ""),
            "mac": "",
            "hostname": host.get("hostname", ""),
            "os": "",
            "services": [],
            "discovered_by": ["dns"],
            "metadata": {},
            "proxy_routes": [],
        }
    elif "discovery-manual" in source_file:
        # Already in unified format from parsers
        if "discovered_by" not in host:
            host["discovered_by"] = ["manual"]
        return host
    else:
        # Assume unified format if all required fields present
        if "discovered_by" in host:
            return host
        # Otherwise, best-effort normalization
        return {
            "ip": host.get("ip", ""),
            "mac": host.get("mac", ""),
            "hostname": host.get("hostname", ""),
            "os": host.get("os", ""),
            "services": host.get("services", []),
            "discovered_by": host.get("discovered_by", ["unknown"]),
            "metadata": host.get("metadata", {}),
            "proxy_routes": host.get("proxy_routes", []),
        }


def consolidate(discovery_files: List[Path]) -> Dict[str, Any]:
    """Consolidate multiple discovery files into unified inventory"""

    # Track by MAC (preferred) and IP (fallback)
    by_mac: Dict[str, Dict[str, Any]] = {}
    by_ip: Dict[str, Dict[str, Any]] = {}
    vlans: Dict[int, Dict[str, Any]] = {}

    for filepath in discovery_files:
        if not filepath.exists():
            continue

        try:
            with open(filepath) as f:
                data = json.load(f)
        except json.JSONDecodeError:
            continue

        # Check if this is VLAN data
        if isinstance(data, list) and data and "vlan_id" in data[0]:
            # VLAN data - deduplicate by VLAN ID
            for vlan in data:
                vlan_id = vlan.get("vlan_id")
                if vlan_id:
                    vlans[vlan_id] = vlan
            continue

        # Handle both list and dict responses for host data
        if isinstance(data, dict):
            hosts = data.get("hosts", [])
        else:
            hosts = data

        for raw_host in hosts:
            # Normalize to unified format
            host = normalize_host(raw_host, str(filepath))
            mac = host.get("mac", "")
            ip = host.get("ip", "")

            if not ip:
                continue

            # Prefer MAC-based deduplication
            if mac:
                if mac in by_mac:
                    by_mac[mac] = merge_host_data(by_mac[mac], host)
                else:
                    by_mac[mac] = host

                # Also track by IP for cross-referencing
                by_ip[ip] = by_mac[mac]
            else:
                # No MAC, fallback to IP-based deduplication
                if ip in by_ip:
                    by_ip[ip] = merge_host_data(by_ip[ip], host)
                else:
                    by_ip[ip] = host

    # Combine MAC-based and IP-only hosts
    seen_ips = set()
    inventory = []

    # Add all MAC-based hosts first
    for host in by_mac.values():
        inventory.append(host)
        seen_ips.add(host["ip"])

    # Add IP-only hosts that weren't in by_mac
    for ip, host in by_ip.items():
        if ip not in seen_ips:
            inventory.append(host)

    # Sort by IP address
    def ip_sort_key(host: Dict[str, Any]) -> tuple:
        try:
            return tuple(map(int, host["ip"].split(".")))
        except (ValueError, AttributeError):
            return (999, 999, 999, 999)

    inventory.sort(key=ip_sort_key)

    # Sort VLANs by VLAN ID
    def vlan_sort_key(vlan: Dict[str, Any]) -> int:
        return vlan.get("vlan_id", 9999)

    vlan_list = sorted(vlans.values(), key=vlan_sort_key)

    return {"hosts": inventory, "vlans": vlan_list}


def main() -> None:
    if len(sys.argv) < 2:
        print("ERROR: Missing arguments")
        print("Usage: consolidate.py <discovery-file1.json> [discovery-file2.json ...]")
        sys.exit(1)

    discovery_files = [Path(arg) for arg in sys.argv[1:]]

    result = consolidate(discovery_files)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
