# Network Security Monitoring  
*A TryHackMe room focused on analyzing network traffic, identifying threats, and understanding NSM workflows.*

---

## **Overview**
Network Security Monitoring (NSM) teaches how defenders collect, analyze, and interpret network data to detect malicious activity.  
This room introduces the tools, logs, and techniques used to monitor network traffic in real‑world SOC environments.

This write‑up serves as a structured template for documenting your investigation and findings.

---

## **Objectives**
- Understand the purpose of Network Security Monitoring  
- Learn how network data is collected and analyzed  
- Explore tools such as Zeek, Suricata, and Wireshark  
- Identify suspicious network activity  
- Analyze PCAPs and NSM logs  
- Strengthen detection and investigation skills  

---

## **Key Concepts Learned**

### **1. What NSM Is**
Network Security Monitoring focuses on:
- collecting network data  
- analyzing traffic patterns  
- identifying anomalies  
- detecting threats through metadata and packet analysis  

### **2. Types of Network Data**
- **Full packet capture (PCAP)**  
- **Flow data** (NetFlow, Zeek conn logs)  
- **Metadata logs** (DNS, HTTP, TLS)  
- **IDS alerts** (Suricata, Snort)  

### **3. Core NSM Tools**
- **Wireshark** — packet‑level analysis  
- **Zeek** — behavioral and metadata analysis  
- **Suricata** — IDS/IPS alerts and protocol logs  
- **tcpdump** — command‑line packet capture  

### **4. Indicators of Malicious Traffic**
Examples include:
- beaconing patterns  
- suspicious DNS queries  
- encoded HTTP payloads  
- unusual ports or protocols  
- large outbound transfers  
- failed TLS handshakes  

---

## **Tools Used**
- Wireshark  
- Zeek logs  
- Suricata alerts  
- PCAP files  
- TryHackMe NSM environment  

---

## **Investigation Steps (Template)**  
*(Fill these in after completing the room.)*

### **1. Reviewing the PCAP**
Document:
- protocols observed  
- top talkers  
- unusual traffic patterns  
- suspicious IPs or domains  

### **2. Analyzing Zeek Logs**
Examples:
- reviewing `conn.log` for anomalies  
- checking `dns.log` for odd queries  
- inspecting `http.log` for suspicious requests  
- analyzing `ssl.log` for unusual JA3 fingerprints  

### **3. Reviewing Suricata Alerts**
Record:
- triggered signatures  
- severity levels  
- source/destination IPs  
- alert context  

### **4. Correlating Findings**
Examples:
- matching Suricata alerts with Zeek metadata  
- confirming suspicious traffic in Wireshark  
- identifying attacker behavior patterns  

### **5. Determining Threat Type**
Possible categories:
- malware C2  
- brute‑force attempts  
- scanning/reconnaissance  
- data exfiltration  
- suspicious encrypted traffic  

---

## **Key Findings (Template)**
*(Fill this in after completing the room.)*

- Summary of suspicious traffic  
- Notable IPs, domains, or ports  
- Alerts triggered  
- Techniques identified  
- Final assessment of threat  

---

## **Skills Demonstrated**
- Network traffic analysis  
- PCAP investigation  
- Zeek log interpretation  
- Suricata alert triage  
- Threat detection  
- Correlation across multiple data sources  
- SOC‑level NSM workflow  

---

## **Notes**
This room builds the foundation for advanced network‑level detection and prepares you for:
- Malware Analysis  
- Incident Response  
- Threat Hunting  
- SOC Tier 1 & Tier 2 workflows  
