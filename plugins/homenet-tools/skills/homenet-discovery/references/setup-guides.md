# Setup Guides

Setup instructions for optional discovery methods.

## SSH Key Setup

Deploy SSH keys for passwordless access. homenet uses authorized_keys - no passwords stored.

**Deploy your public key to hosts:**

```bash
ssh-copy-id {username}@host1.lab
ssh-copy-id {username}@host2.lab
ssh-copy-id {username}@host3.lab
```

This adds your `~/.ssh/id_rsa.pub` (or similar) to each host's `~/.ssh/authorized_keys` file.

**Test connectivity:**

```bash
ssh {username}@host1.lab hostname
```

Should connect without password prompt.

**Batch deployment:**

If you have many hosts, create a list:

```bash
# hosts.txt
192.168.1.10
192.168.1.20
192.168.1.30
```

Then deploy:

```bash
while read host; do
  ssh-copy-id {username}@$host
done < hosts.txt
```

**Security notes:**
- Uses your existing SSH keys
- No passwords transmitted or stored
- Hosts still require SSH key authentication
- Disable password auth in `/etc/ssh/sshd_config` for security

## DNS Zone Transfer Setup

Enable AXFR (zone transfer) on your DNS server to allow homenet to enumerate all DNS records.

### OPNsense/pfSense

1. Navigate to: **Services → Unbound DNS → Access Lists**
2. Add your IP or network range
3. Check: **Allow DNS Queries** and **Allow AXFR Zone Transfers**
4. Save and apply

### Pi-hole

Pi-hole already allows zone transfers from localhost. If running homenet remotely:

1. SSH to Pi-hole host
2. Edit `/etc/dnsmasq.d/02-pihole-dhcp.conf`
3. Add: `auth-server=pi.hole,192.168.1.0/24`
4. Restart: `sudo systemctl restart pihole-FTL`

### Bind9

Edit `/etc/bind/named.conf.local`:

```
zone "home.lab" {
    type master;
    file "/etc/bind/db.home.lab";
    allow-transfer { 192.168.1.0/24; };
};
```

Reload: `sudo systemctl reload bind9`

### Unbound (generic)

Edit `unbound.conf`:

```
server:
    local-zone: "home.lab." transparent
    access-control: 192.168.1.0/24 allow
```

Restart: `sudo systemctl restart unbound`

### Testing

Verify zone transfer works:

```bash
dig @192.168.1.1 home.lab AXFR
```

Should return all A records in the zone.

## Manual Command Outputs

Drop command outputs in `/tmp/homenet/` for richer discovery. homenet parsers extract detailed infrastructure data.

### Proxmox

Extract node and resource data:

```bash
# Create drop directory
mkdir -p /tmp/homenet

# Export nodes
pvesh get /nodes --output-format json > /tmp/homenet/proxmox-nodes.json

# Export cluster resources (VMs, containers, storage)
pvesh get /cluster/resources --output-format json > /tmp/homenet/proxmox-resources.json
```

**What gets extracted:**
- Node hostnames and IPs
- VM names, IDs, and states
- Container names and configurations
- Storage pools and usage

### OPNsense

Export full configuration via WebUI:

1. Navigate to: **System → Configuration → Backups**
2. Click **Download configuration**
3. Save as: `/tmp/homenet/opnsense-config.xml`

**What gets extracted:**
- Interface configurations and VLANs
- Firewall rules and aliases
- DHCP static mappings
- DNS overrides and host entries
- Gateway and routing information

### pfSense

Similar to OPNsense:

1. Navigate to: **Diagnostics → Backup & Restore**
2. Click **Download configuration as XML**
3. Save as: `/tmp/homenet/opnsense-config.xml` (parser handles both)

### UniFi Controller

Export device data via API:

```bash
# Login to controller and get cookie
curl -k -X POST \
  https://YOUR-CONTROLLER:8443/api/login \
  -H 'Content-Type: application/json' \
  -d '{"username":"admin","password":"yourpassword"}' \
  -c /tmp/unifi-cookie.txt

# Export devices
curl -k -X GET \
  https://YOUR-CONTROLLER:8443/api/s/default/stat/device \
  -b /tmp/unifi-cookie.txt \
  > /tmp/homenet/unifi-devices.json

# Logout
curl -k -X POST \
  https://YOUR-CONTROLLER:8443/api/logout \
  -b /tmp/unifi-cookie.txt

# Clean up
rm /tmp/unifi-cookie.txt
```

**Alternative:** Navigate to `https://YOUR-CONTROLLER:8443/api/s/default/stat/device` in browser (while logged in) and save JSON.

**What gets extracted:**
- Access point names, IPs, and MACs
- Switch names, models, and port counts
- Gateway/router information
- Uplink connections

### TrueNAS/FreeNAS

Export storage and network configuration:

```bash
# Storage pools
midclt call pool.query > /tmp/homenet/truenas-pools.json

# Network interfaces
midclt call interface.query > /tmp/homenet/truenas-interfaces.json
```

### Docker

Export container information from any Docker host:

```bash
docker ps --format '{{json .}}' > /tmp/homenet/docker-containers.json
```

**What gets extracted:**
- Container names and images
- Published ports
- Networks and IPs

## File Naming Conventions

homenet detects parsers by filename pattern:

| Filename | Parser | Platform |
|----------|--------|----------|
| `proxmox-*.json` | `parsers/proxmox.py` | Proxmox VE |
| `opnsense-config.xml` | `parsers/opnsense.py` | OPNsense/pfSense |
| `unifi-*.json` | `parsers/unifi.py` | UniFi Controller |
| `truenas-*.json` | `parsers/truenas.py` | TrueNAS |
| `docker-*.json` | `parsers/docker.py` | Docker |

**Naming tips:**
- Use descriptive prefixes: `proxmox-nodes.json`, `proxmox-resources.json`
- Multiple files per platform supported
- Files processed in alphabetical order

## Combining Methods

**Recommended approach:**

1. **Manual drops first** - Most detailed infrastructure data
2. **nmap** - Fill gaps, find unexpected devices
3. **SSH** - Deep inspect accessible hosts
4. **DNS** - Validate hostnames and find services

**Example workflow:**

```bash
# 1. Export infrastructure data
pvesh get /cluster/resources --output-format json > /tmp/homenet/proxmox-resources.json

# 2. Run homenet discovery
# (Manual parser extracts IPs, nmap validates, SSH inspects)

# 3. Review inventory
cat ~/.local/share/homenet/inventory.md
```

This gives you:
- Official infrastructure data from Proxmox
- Validated with actual network scans
- Deep inspection of running services
- Complete topology with relationships
