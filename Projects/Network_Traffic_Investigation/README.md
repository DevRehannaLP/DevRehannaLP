# Network Traffic Investigation  
*A hands‑on analysis of packet captures using Wireshark.*

---

## **Overview**
This project demonstrates the process of analyzing network traffic to identify anomalies, suspicious behavior, and potential security incidents. Using Wireshark, I examined packet captures (PCAP files), filtered traffic, and documented findings that reflect real SOC analyst workflows.

---

## **Objectives**
- Analyze packet captures using Wireshark  
- Identify unusual or malicious traffic patterns  
- Apply filters to isolate relevant packets  
- Investigate protocols, IPs, and communication flows  
- Document findings and recommended actions  

---

## **Tools Used**
- Wireshark  
- Linux CLI  
- WHOIS lookup  
- IP geolocation tools  
- DNS analysis utilities  

---

## **Investigation Steps**
### **1. Initial Review**
- Loaded PCAP file into Wireshark  
- Reviewed high‑level statistics (protocol hierarchy, endpoints, conversations)  
- Identified unusual spikes in traffic  

### **2. Filtering Traffic**
Common filters used:
- `http` — view web traffic  
- `dns` — analyze DNS queries  
- `tcp.flags.syn == 1` — detect connection attempts  
- `ip.addr == x.x.x.x` — isolate specific hosts  
- `tcp.port == 80` — filter by port  

### **3. Identifying Suspicious Behavior**
Looked for:
- repeated failed connections  
- unusual DNS requests  
- communication with known malicious IPs  
- unencrypted credentials  
- large data transfers to unknown hosts  

### **4. Deep Packet Inspection**
Reviewed packet details to identify:
- payload content  
- HTTP headers  
- DNS query patterns  
- TLS handshake anomalies  

### **5. Documentation**
Recorded:
- suspicious IP addresses  
- domains queried  
- timestamps of activity  
- protocol behavior  
- potential indicators of compromise (IOCs)  

---

## **Key Findings**
- Detected repeated DNS queries to suspicious domains  
- Identified outbound traffic to an IP with poor reputation  
- Observed unusual HTTP requests inconsistent with normal user behavior  
- No evidence of successful data exfiltration  

---

## **Recommendations**
- Block identified malicious IPs and domains  
- Monitor for repeated DNS anomalies  
- Enforce TLS for sensitive communications  
- Review firewall rules for unnecessary open ports  
- Conduct user awareness training  

---

## **Skills Demonstrated**
- Packet analysis  
- Wireshark filtering  
- Network protocol understanding  
- IOC identification  
- Threat investigation  
- Documentation and reporting  
