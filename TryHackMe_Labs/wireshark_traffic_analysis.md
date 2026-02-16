# Wireshark Traffic Analysis  
*A TryHackMe room focused on analyzing PCAPs and identifying suspicious network activity.*

---

## Overview
This room teaches packet-level investigation using Wireshark, including filtering, protocol analysis, and threat detection.

---

## Objectives
- Analyze PCAP files  
- Use display filters  
- Identify suspicious traffic  
- Reconstruct sessions  
- Extract IOCs  

---

## Key Concepts Learned
- TCP/UDP basics  
- HTTP request analysis  
- DNS query inspection  
- TLS handshake review  
- Beaconing patterns  

---

## Tools Used
- Wireshark  
- PCAP files  
- Protocol analyzers  

---

## Investigation Steps (Template)
### 1. Initial PCAP Review  
- Protocol hierarchy  
- Conversations  
- Endpoints  

### 2. Filtering Suspicious Traffic  
Examples:
```
http
dns
tcp.flags.syn == 1
```

### 3. Session Reconstruction  
- Follow TCP stream  
- Identify payloads  

### 4. IOC Extraction  
- IPs  
- Domains  
- User-agents  

---

## Key Findings (Template)

---

## Skills Demonstrated
- Packet analysis  
- Threat detection  
- Network investigation  
- IOC extraction  
