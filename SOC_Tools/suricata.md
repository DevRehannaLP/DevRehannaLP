# Suricata  
*An open‑source IDS/IPS and network security engine used for real‑time threat detection.*

---

## **Overview**
Suricata is a high‑performance intrusion detection and prevention system (IDS/IPS) capable of deep packet inspection, signature‑based detection, and protocol analysis.  
It is widely used in SOC environments to detect malicious traffic, enforce rules, and generate actionable alerts.

---

## **Key Features**
- IDS, IPS, and NSM (Network Security Monitoring) capabilities  
- Multi‑threaded performance  
- Deep packet inspection  
- Signature‑based detection (Snort‑compatible rules)  
- File extraction and hashing  
- JSON‑formatted logs  
- Real‑time alerting  

---

## **Core Suricata Logs**

| Log File | Purpose |
|----------|----------|
| `fast.log` | Quick summary of alerts |
| `eve.json` | Detailed JSON events (alerts, DNS, HTTP, TLS, flows) |
| `stats.log` | Performance and engine statistics |
| `http.log` | HTTP metadata |
| `dns.log` | DNS queries and responses |
| `tls.log` | TLS handshake metadata |
| `files.log` | File extraction and hashes |

The **eve.json** log is the most important for SOC analysts.

---

## **Common SOC Use Cases**
- Detecting malware C2 traffic  
- Identifying brute‑force attempts  
- Monitoring DNS anomalies  
- Detecting port scans  
- Reviewing HTTP requests for suspicious patterns  
- Extracting file hashes from network traffic  
- Correlating alerts with SIEM events  

---

## **Example Suricata Rule**
A simple rule detecting outbound traffic to a suspicious IP:

```
alert ip any any -> 203.0.113.10 any (msg:"Suspicious outbound connection"; sid:100001; rev:1;)
```

### Rule Components:
- `alert` — action  
- `ip` — protocol  
- `any any` — source IP and port  
- `->` — direction  
- `203.0.113.10 any` — destination IP and port  
- `msg` — alert message  
- `sid` — signature ID  
- `rev` — revision number  

---

## **Useful Investigation Techniques**

### **1. Reviewing Alerts in eve.json**
Look for:
- repeated alerts from the same IP  
- high‑severity signatures  
- unusual ports or protocols  
- patterns indicating brute‑force or scanning  

### **2. Analyzing DNS Events**
Red flags:
- random‑looking domains  
- excessive DNS queries  
- known malicious domains  

### **3. Inspecting HTTP Events**
Check for:
- suspicious user‑agents  
- encoded payloads  
- POST requests to unknown servers  

### **4. Reviewing TLS Metadata**
Useful for:
- JA3 fingerprinting  
- detecting suspicious encrypted traffic  
- identifying unusual TLS clients  

### **5. Flow Analysis**
Flow records help identify:
- beaconing  
- long‑duration sessions  
- large outbound transfers  

---

## **Common Threat Indicators in Suricata**
- Alerts triggered by known malware signatures  
- DNS queries to algorithm‑generated domains  
- Repeated connection attempts (scanning)  
- Suspicious JA3 fingerprints  
- HTTP requests with encoded or obfuscated payloads  
- Outbound traffic to known malicious IPs  

---

## **Skills Demonstrated**
- IDS/IPS analysis  
- Signature‑based detection  
- Log analysis  
- Threat hunting  
- Network security monitoring  
- Correlating Suricata alerts with SIEM data  
