#!/bin/bash
# ssh-probe.sh - SSH into host and gather system information
# Outputs JSON array with single host object

set -uo pipefail

HOST="${1:-}"

if [ -z "$HOST" ]; then
    echo "Usage: $0 <user@host>" >&2
    echo "Example: $0 root@192.168.1.50" >&2
    exit 1
fi

# Extract IP from user@host format
HOST_IP="${HOST##*@}"

# Test SSH connectivity with short timeout
SSH_TEST_OUTPUT=$(ssh -o ConnectTimeout=2 -o BatchMode=yes -o StrictHostKeyChecking=accept-new "$HOST" echo "ok" 2>&1)
SSH_EXIT_CODE=$?

if [ $SSH_EXIT_CODE -ne 0 ]; then
    # Check if it's auth failure (SSH open but no key) vs connection failure
    if echo "$SSH_TEST_OUTPUT" | grep -q "Permission denied"; then
        # SSH is available but we can't authenticate - output minimal host data
        cat << EOF
[{
  "ip": "$HOST_IP",
  "mac": "",
  "hostname": "",
  "os": "",
  "services": ["ssh"],
  "discovered_by": ["ssh-detected"],
  "metadata": {"ssh_auth_failed": true},
  "proxy_routes": []
}]
EOF
        exit 0
    else
        # Connection refused/timeout - SSH not available
        echo "[]"
        exit 0
    fi
fi

# Gather host information and convert to JSON
ssh -o ConnectTimeout=5 -o BatchMode=yes "$HOST" '
set -e

echo "=== SYSTEM ==="
uname -s -r -m 2>/dev/null || echo "unknown"

echo "=== HOSTNAME ==="
hostname 2>/dev/null || echo "unknown"

echo "=== INTERFACES ==="
if command -v ip >/dev/null 2>&1; then
    ip -br addr show 2>/dev/null | grep -v "^lo " || true
elif command -v ifconfig >/dev/null 2>&1; then
    ifconfig 2>/dev/null | grep -E "^[a-z]|inet " || true
fi

echo "=== DOCKER ==="
if command -v docker >/dev/null 2>&1; then
    docker ps --format "{{.Names}},{{.Image}},{{.Status}}" 2>/dev/null || echo "no-containers"
    echo "=== DOCKER_NETWORKS ==="
    docker network ls --format "{{.Name}},{{.Driver}},{{.ID}}" 2>/dev/null | while IFS=, read -r name driver id; do
        subnet=$(docker network inspect "$id" --format "{{range .IPAM.Config}}{{.Subnet}}{{end}}" 2>/dev/null || echo "")
        echo "$name,$driver,$subnet"
    done
else
    echo "no-docker"
fi

echo "=== SERVICES ==="
if command -v systemctl >/dev/null 2>&1; then
    systemctl list-units --type=service --state=running --no-pager --no-legend 2>/dev/null | \
        awk "{print \$1}" | head -20 || echo "none"
else
    echo "no-systemd"
fi

echo "=== PROXY_CONFIGS ==="

# Detect and read reverse proxy configs

# Check for Caddy (systemd or docker)
if systemctl is-active caddy.service >/dev/null 2>&1 || systemctl is-active caddy >/dev/null 2>&1; then
    echo "--- CADDY (systemd) ---"
    if [ -f /etc/caddy/Caddyfile ]; then
        cat /etc/caddy/Caddyfile 2>/dev/null || echo "ERROR: Cannot read Caddyfile"
    else
        echo "ERROR: Caddyfile not found at /etc/caddy/Caddyfile"
    fi
fi

# Check for nginx (systemd)
if systemctl is-active nginx.service >/dev/null 2>&1 || systemctl is-active nginx >/dev/null 2>&1; then
    echo "--- NGINX (systemd) ---"
    if [ -f /etc/nginx/nginx.conf ]; then
        cat /etc/nginx/nginx.conf 2>/dev/null || echo "ERROR: Cannot read nginx.conf"
    else
        echo "ERROR: nginx.conf not found"
    fi
fi

# Check for Traefik (systemd)
if systemctl is-active traefik.service >/dev/null 2>&1 || systemctl is-active traefik >/dev/null 2>&1; then
    echo "--- TRAEFIK (systemd) ---"
    for conf in /etc/traefik/traefik.yml /etc/traefik/traefik.yaml /etc/traefik/traefik.toml; do
        if [ -f "$conf" ]; then
            cat "$conf" 2>/dev/null || echo "ERROR: Cannot read $conf"
            break
        fi
    done
fi

# Check for HAProxy (systemd)
if systemctl is-active haproxy.service >/dev/null 2>&1 || systemctl is-active haproxy >/dev/null 2>&1; then
    echo "--- HAPROXY (systemd) ---"
    if [ -f /etc/haproxy/haproxy.cfg ]; then
        cat /etc/haproxy/haproxy.cfg 2>/dev/null || echo "ERROR: Cannot read haproxy.cfg"
    else
        echo "ERROR: haproxy.cfg not found"
    fi
fi

# Check Docker containers for reverse proxies
if command -v docker >/dev/null 2>&1; then
    # Get list of running containers with images that look like proxies
    docker ps --format "{{.Names}},{{.Image}}" 2>/dev/null | while IFS=, read -r name image; do
        case "$image" in
            *caddy*)
                echo "--- CADDY (docker: $name) ---"
                # Try common Caddyfile locations inside container
                docker exec "$name" cat /etc/caddy/Caddyfile 2>/dev/null || \
                docker exec "$name" cat /config/Caddyfile 2>/dev/null || \
                docker exec "$name" cat /Caddyfile 2>/dev/null || \
                echo "ERROR: Caddyfile not found in container $name"
                ;;
            *nginx*)
                echo "--- NGINX (docker: $name) ---"
                docker exec "$name" cat /etc/nginx/nginx.conf 2>/dev/null || \
                echo "ERROR: nginx.conf not found in container $name"
                ;;
            *traefik*)
                echo "--- TRAEFIK (docker: $name) ---"
                docker exec "$name" cat /etc/traefik/traefik.yml 2>/dev/null || \
                docker exec "$name" cat /etc/traefik/traefik.yaml 2>/dev/null || \
                docker exec "$name" cat /etc/traefik/traefik.toml 2>/dev/null || \
                echo "ERROR: Traefik config not found in container $name"
                ;;
            *haproxy*)
                echo "--- HAPROXY (docker: $name) ---"
                docker exec "$name" cat /usr/local/etc/haproxy/haproxy.cfg 2>/dev/null || \
                docker exec "$name" cat /etc/haproxy/haproxy.cfg 2>/dev/null || \
                echo "ERROR: haproxy.cfg not found in container $name"
                ;;
        esac
    done
fi
' | python3 -c "
import sys
import re
import json

HOST_IP = '$HOST_IP'

def parse_ssh_output(output):
    sections = {}
    current_section = None
    current_content = []

    for line in output.split('\n'):
        if line.startswith('=== ') and line.endswith(' ==='):
            if current_section:
                sections[current_section] = '\n'.join(current_content).strip()
            current_section = line[4:-4].strip()
            current_content = []
        else:
            current_content.append(line)

    if current_section:
        sections[current_section] = '\n'.join(current_content).strip()

    # Parse sections
    os_info = sections.get('SYSTEM', 'unknown').strip()
    hostname = sections.get('HOSTNAME', '').strip()

    # Parse interfaces
    interfaces = {}
    if 'INTERFACES' in sections:
        for line in sections['INTERFACES'].split('\n'):
            if not line.strip():
                continue
            parts = line.split()
            if len(parts) >= 3 and '/' in parts[2]:
                interfaces[parts[0]] = parts[2].split('/')[0]

    # Parse containers
    containers = []
    if 'DOCKER' in sections:
        docker_content = sections['DOCKER']
        if docker_content not in ['no-docker', 'no-containers']:
            for line in docker_content.split('\n'):
                if line.strip() and line != 'no-containers':
                    parts = line.split(',')
                    if len(parts) >= 2:
                        containers.append({
                            'name': parts[0],
                            'image': parts[1],
                            'status': parts[2] if len(parts) > 2 else 'unknown'
                        })

    # Parse services
    services = []
    if 'SERVICES' in sections:
        service_content = sections['SERVICES']
        if service_content not in ['none', 'no-systemd']:
            for line in service_content.split('\n'):
                if line.strip() and line not in ['none', 'no-systemd']:
                    service_name = line.strip()
                    if service_name.endswith('.service'):
                        service_name = service_name[:-8]
                    services.append(service_name)

    # Check for proxy configs
    if 'PROXY_CONFIGS' in sections:
        proxy_content = sections['PROXY_CONFIGS']
        for line in proxy_content.split('\n'):
            if line.startswith('--- '):
                match = re.match(r'--- (\w+) \(([^)]+)\) ---', line)
                if match:
                    proxy_type = match.group(1).lower()
                    if proxy_type not in [s.lower() for s in services]:
                        services.append(proxy_type)

    # Detect services from containers
    for container in containers:
        image = container['image'].lower()
        for svc in ['postgres', 'mysql', 'mariadb', 'redis', 'nginx', 'caddy', 'traefik']:
            if svc in image and svc not in services:
                services.append('mysql' if svc == 'mariadb' else svc)

    # Build host object
    metadata = {'interfaces': interfaces}
    if containers:
        metadata['containers'] = containers

    host = {
        'ip': HOST_IP,
        'mac': '',
        'hostname': hostname,
        'os': os_info,
        'services': services,
        'discovered_by': ['ssh'],
        'metadata': metadata,
        'proxy_routes': []
    }

    return [host]

output = sys.stdin.read()
hosts = parse_ssh_output(output)
print(json.dumps(hosts, indent=2))
"
