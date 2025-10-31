# Network Inventory

## Contents
- [Overview](#overview) - Scan summary and statistics
- [Hosts](#hosts) - Discovered network hosts
- [Services](#services) - Running services by host
- [Proxy Routes](#proxy-routes) - Domain to backend mappings
- [Network Topology](#network-topology) - Subnets and VLANs
- [Access Methods](#access-methods) - SSH access and credentials

Generated: {TIMESTAMP}
Scan methods: {METHODS_LIST}
Total hosts: {HOST_COUNT}

## Overview

Discovered {HOST_COUNT} hosts across {SUBNET_COUNT} subnets using {METHODS}.

## Hosts

List each host with key information for management:

**{IP}** ({hostname})
- MAC: {mac} ({vendor})
- OS: {os}
- Role: {role_description}
- Discovery: {methods}

## Services

Services by host for operational context:

**{IP} ({hostname})**
- {service_name} ({service_detail})
- {service_name}

## Proxy Routes

Domain to service mappings for application access:

**{proxy_type} on {IP}:**
- {domain} → {backend_url}
- {domain} → {backend_url}

## Network Topology

Network structure and subnets:

**Primary Network:** {subnet}
- Gateway: {gateway_ip} ({hostname})

**VLANs:**
- VLAN {id} ({name}): {description}

## Access Methods

How to reach and control systems:

**SSH Access:**
- Most hosts: ssh {user}@<ip>
- Keys deployed: {yes/no}

**Container Management:**
- {IP}: docker commands available
