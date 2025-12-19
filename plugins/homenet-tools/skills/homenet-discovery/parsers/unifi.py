#!/usr/bin/env python3
"""
unifi.py - Parse UniFi device JSON into host list
"""

import json
import sys
from typing import List, Dict, Any


def parse_unifi_devices(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Parse UniFi devices JSON"""
    hosts = []

    for device in data:
        # UniFi device structure varies, adapt as needed
        ip = device.get("ip", "")
        mac = device.get("mac", "")
        name = device.get("name", "") or device.get("hostname", "")
        device_type = device.get("type", "unknown")
        model = device.get("model", "")
        version = device.get("version", "")

        host = {
            "ip": ip,
            "mac": mac,
            "hostname": name,
            "os": f"UniFi {version}" if version else "UniFi",
            "services": ["unifi", device_type],
            "discovered_by": ["manual-unifi"],
            "metadata": {
                "type": "network-device",
                "model": model,
                "device_type": device_type,
                "state": device.get("state", 0),
                "uptime": device.get("uptime", 0),
            },
        }
        hosts.append(host)

    return hosts


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON: {e}", file=sys.stderr)
        sys.exit(1)

    # Handle both array and object with 'data' field
    if isinstance(data, dict) and "data" in data:
        data = data["data"]

    if not isinstance(data, list):
        print("ERROR: Expected JSON array of devices", file=sys.stderr)
        sys.exit(1)

    hosts = parse_unifi_devices(data)
    print(json.dumps(hosts, indent=2))


if __name__ == "__main__":
    main()
