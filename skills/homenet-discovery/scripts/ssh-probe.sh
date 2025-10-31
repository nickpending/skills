#!/bin/bash
# ssh-probe.sh - SSH into host and gather system information

set -uo pipefail

HOST="${1:-}"

if [ -z "$HOST" ]; then
    echo "Usage: $0 <host>" >&2
    echo "Example: $0 192.168.1.50" >&2
    exit 1
fi

# Test SSH connectivity with short timeout
if ! ssh -o ConnectTimeout=2 -o BatchMode=yes -o StrictHostKeyChecking=accept-new "$HOST" echo "ok" >/dev/null 2>&1; then
    echo "ERROR: SSH connection to $HOST failed (no key access or host unreachable)"
    exit 1
fi

# Gather host information
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
'
