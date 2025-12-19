#!/usr/bin/env python3
"""
opnsense.py - Parse OPNsense config XML into host list
"""

import sys
import xml.etree.ElementTree as ET
from typing import List, Dict, Any
import json


def parse_opnsense_vlans(xml_data: str) -> List[Dict[str, Any]]:
    """Parse OPNsense VLAN configuration"""
    vlans = []

    try:
        root = ET.fromstring(xml_data)
    except ET.ParseError as e:
        print(f"ERROR: Invalid XML: {e}", file=sys.stderr)
        sys.exit(1)

    vlans_container = root.find(".//vlans")
    if vlans_container is not None:
        for vlan in vlans_container.findall("vlan"):
            tag = vlan.find("tag")
            descr = vlan.find("descr")
            if_elem = vlan.find("if")
            vlanif = vlan.find("vlanif")

            if tag is not None:
                vlan_info = {
                    "vlan_id": int(tag.text) if tag.text else 0,
                    "name": descr.text if descr is not None and descr.text else "",
                    "interface": if_elem.text
                    if if_elem is not None and if_elem.text
                    else "",
                    "vlanif": vlanif.text if vlanif is not None and vlanif.text else "",
                }
                vlans.append(vlan_info)

    return vlans


def parse_opnsense_config(xml_data: str) -> List[Dict[str, Any]]:
    """Parse OPNsense XML config for network hosts"""
    hosts = []

    try:
        root = ET.fromstring(xml_data)
    except ET.ParseError as e:
        print(f"ERROR: Invalid XML: {e}", file=sys.stderr)
        sys.exit(1)

    # Parse DHCP static mappings
    dhcpd = root.find(".//dhcpd")
    if dhcpd is not None:
        for interface in dhcpd:
            static_maps = interface.findall("staticmap")
            for mapping in static_maps:
                mac = mapping.find("mac")
                ip = mapping.find("ipaddr")
                hostname = mapping.find("hostname")
                descr = mapping.find("descr")

                if mac is not None and ip is not None:
                    host = {
                        "ip": ip.text,
                        "mac": mac.text,
                        "hostname": hostname.text if hostname is not None else "",
                        "os": "",
                        "services": [],
                        "discovered_by": ["manual-opnsense"],
                        "metadata": {
                            "type": "dhcp-static",
                            "description": descr.text if descr is not None else "",
                        },
                    }
                    hosts.append(host)

    # Parse DNS host overrides (OPNsense uses <hosts> container)
    hosts_container = root.find(".//hosts")
    if hosts_container is not None:
        hosts_overrides = hosts_container.findall("host")
        for host_entry in hosts_overrides:
            hostname_elem = host_entry.find("hostname")
            domain_elem = host_entry.find("domain")
            ip_elem = host_entry.find("server")  # OPNsense uses <server> not <ip>
            descr_elem = host_entry.find("description")

            if hostname_elem is not None and ip_elem is not None:
                fqdn = hostname_elem.text
                if domain_elem is not None and domain_elem.text:
                    fqdn = f"{hostname_elem.text}.{domain_elem.text}"

                host = {
                    "ip": ip_elem.text,
                    "mac": "",
                    "hostname": fqdn,
                    "os": "",
                    "services": [],
                    "discovered_by": ["manual-opnsense"],
                    "metadata": {
                        "type": "dns-override",
                        "description": descr_elem.text
                        if descr_elem is not None
                        else "",
                    },
                }
                hosts.append(host)

    return hosts


def main() -> None:
    mode = sys.argv[1] if len(sys.argv) > 1 else "hosts"
    xml_data = sys.stdin.read()

    if mode == "vlans":
        result = parse_opnsense_vlans(xml_data)
    elif mode == "hosts":
        result = parse_opnsense_config(xml_data)
    else:
        print(f"ERROR: Unknown mode '{mode}'. Use 'hosts' or 'vlans'", file=sys.stderr)
        sys.exit(1)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
