#!/bin/bash
# dns-enum.sh - DNS enumeration and zone transfer

set -uo pipefail

DNS_SERVER="${1:-}"
DOMAIN="${2:-}"

if [ -z "$DNS_SERVER" ]; then
    echo "Usage: $0 <dns-server> [domain]" >&2
    echo "Example: $0 192.168.1.1 home.lab" >&2
    exit 1
fi

# If no domain specified, try to detect from system
if [ -z "$DOMAIN" ]; then
    DOMAIN=$(dnsdomainname 2>/dev/null || hostname -d 2>/dev/null || echo "")
fi

if [ -z "$DOMAIN" ]; then
    echo "ERROR: No domain specified or detected"
    exit 1
fi

# Test DNS server connectivity
if ! dig @"$DNS_SERVER" google.com +short +timeout=2 >/dev/null 2>&1; then
    echo "ERROR: Cannot reach DNS server $DNS_SERVER"
    exit 1
fi

# Try zone transfer
RESULT=$(dig @"$DNS_SERVER" "$DOMAIN" AXFR +noall +answer 2>/dev/null | grep -E "^[a-zA-Z0-9].*\sA\s")

if [ -z "$RESULT" ]; then
    echo "ERROR: DNS zone transfer (AXFR) refused for $DOMAIN on $DNS_SERVER"
else
    echo "$RESULT"
fi
