#!/bin/bash
# nmap-scan.sh - Network host discovery and enumeration wrapper
# Outputs JSON array of discovered hosts
#
# Usage:
#   nmap-scan.sh discover <subnet>     # Lightweight: find hosts (ping sweep)
#   nmap-scan.sh enumerate <target>    # Deep: port scan + services on known host(s)
#
# Examples:
#   nmap-scan.sh discover 192.168.1.0/24
#   nmap-scan.sh enumerate 192.168.1.50
#   nmap-scan.sh enumerate 192.168.1.50,192.168.1.51,192.168.1.52

set -uo pipefail

MODE="${1:-}"
TARGET="${2:-}"

if [ -z "$MODE" ] || [ -z "$TARGET" ]; then
    echo "ERROR: Missing arguments"
    echo "Usage: $0 <discover|enumerate> <subnet|host>"
    echo "Examples:"
    echo "  $0 discover 192.168.1.0/24"
    echo "  $0 enumerate 192.168.1.50"
    exit 1
fi

if [ "$MODE" != "discover" ] && [ "$MODE" != "enumerate" ]; then
    echo "ERROR: Invalid mode '$MODE' (must be 'discover' or 'enumerate')"
    exit 1
fi

# Check if nmap is available
if ! command -v nmap &> /dev/null; then
    echo "ERROR: nmap not installed (required for network scanning)"
    exit 1
fi

if [ "$MODE" = "discover" ]; then
    # Discovery mode: lightweight ping sweep to find live hosts
    # -sn: Ping scan only (no port scan)
    # -T4: Aggressive timing
    # -n: No DNS resolution (faster)
    # --host-timeout: Don't hang on slow hosts
    # -oX -: XML output to stdout
    nmap -sn -T4 -n --host-timeout 30s "$TARGET" -oX - 2>/dev/null | python3 -c "
import sys
import xml.etree.ElementTree as ET
import json

tree = ET.parse(sys.stdin)
root = tree.getroot()

hosts = []
for host in root.findall('host'):
    if host.find('status').get('state') != 'up':
        continue

    ip = host.find('address[@addrtype=\"ipv4\"]').get('addr')
    mac_elem = host.find('address[@addrtype=\"mac\"]')

    host_data = {'ip': ip}

    if mac_elem is not None:
        host_data['mac'] = mac_elem.get('addr')
        host_data['vendor'] = mac_elem.get('vendor', '')
    else:
        host_data['mac'] = ''
        host_data['vendor'] = ''

    hosts.append(host_data)

print(json.dumps(hosts, indent=2))
"
elif [ "$MODE" = "enumerate" ]; then
    # Enumeration mode: deep port scan + service detection on known hosts
    # -Pn: Skip ping, treat all hosts as online (hosts we already know exist)
    # -T4: Aggressive timing
    # -n: No DNS resolution (faster)
    # -sV: Service/version detection (banners)
    # --top-ports 1000: Scan most common 1000 ports
    # --host-timeout: Don't hang on slow hosts
    # -oX -: XML output to stdout

    # Convert comma-separated IPs to space-separated for nmap
    TARGETS_SPACE="${TARGET//,/ }"

    nmap -Pn -T4 -n -sV --top-ports 1000 --host-timeout 3m $TARGETS_SPACE -oX - 2>/dev/null | python3 -c "
import sys
import xml.etree.ElementTree as ET
import json

tree = ET.parse(sys.stdin)
root = tree.getroot()

hosts = []
for host in root.findall('host'):
    if host.find('status').get('state') != 'up':
        continue

    ip = host.find('address[@addrtype=\"ipv4\"]').get('addr')
    mac_elem = host.find('address[@addrtype=\"mac\"]')

    host_data = {'ip': ip, 'services': []}

    if mac_elem is not None:
        host_data['mac'] = mac_elem.get('addr')
        host_data['vendor'] = mac_elem.get('vendor', '')
    else:
        host_data['mac'] = ''
        host_data['vendor'] = ''

    # Extract service info from open ports
    ports = host.find('ports')
    if ports is not None:
        for port in ports.findall('port'):
            state = port.find('state')
            if state is not None and state.get('state') == 'open':
                service = port.find('service')
                if service is not None:
                    svc_name = service.get('name', 'unknown')
                    svc_product = service.get('product', '')
                    svc_version = service.get('version', '')
                    port_num = port.get('portid')

                    svc_str = f\"{svc_name}/{port_num}\"
                    if svc_product:
                        svc_str += f\" ({svc_product}\"
                        if svc_version:
                            svc_str += f\" {svc_version}\"
                        svc_str += \")\"

                    host_data['services'].append(svc_str)

    hosts.append(host_data)

print(json.dumps(hosts, indent=2))
"
fi
