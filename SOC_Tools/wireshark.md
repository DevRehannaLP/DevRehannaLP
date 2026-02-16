# Wireshark  
*A powerful packet analysis tool used for network investigations and threat detection.*

---

## **Overview**
Wireshark is a network protocol analyzer that allows SOC analysts to inspect packet captures (PCAPs) at a granular level.  
It is essential for investigating suspicious traffic, identifying anomalies, and understanding communication patterns.

---

## **Key Features**
- Deep packet inspection  
- Protocol decoding  
- Real‑time capture and offline analysis  
- Filtering and search capabilities  
- Stream reconstruction (TCP/HTTP)  
- Color‑coding for quick visual analysis  

---

## **Common Use Cases in a SOC**
- Investigating suspicious network traffic  
- Analyzing DNS queries  
- Reviewing HTTP requests and responses  
- Detecting brute‑force attempts  
- Identifying command‑and‑control (C2) traffic  
- Inspecting TLS handshakes  
- Extracting files from PCAPs  

---

## **Essential Display Filters**

### **By Protocol**
```
http
dns
ftp
ssh
tls
icmp
```

### **By IP Address**
```
ip.addr == 192.168.1.10
```

### **By Port**
```
tcp.port == 80
udp.port == 53
```

### **By Traffic Direction**
```
ip.src == 10.0.0.5
ip.dst == 8.8.8.8
```

### **Suspicious Indicators**
```
tcp.flags.syn == 1
dns.qry.name contains ".xyz"
http.request.method == "POST"
```

---

## **Useful Analysis Techniques**

### **1. Follow TCP Stream**
Reconstructs conversations between hosts.  
Useful for:
- credential leakage  
- suspicious HTTP requests  
- malware C2 communication  

### **2. Protocol Hierarchy**
Shows which protocols dominate the capture.  
Great for spotting anomalies like:
- unexpected SMB traffic  
- excessive DNS queries  
- unusual encrypted traffic  

### **3. Conversations & Endpoints**
Helps identify:
- top talkers  
- unusual communication pairs  
- unexpected external IPs  

### **4. Export Objects**
Extract files from:
- HTTP  
- SMB  
- FTP  
- TFTP  

Useful for malware investigations.

---

## **Red Flags to Watch For**
- Repeated failed TCP handshakes  
- DNS queries to random or algorithm‑generated domains  
- Large outbound data transfers  
- Unencrypted credentials in HTTP  
- Suspicious user‑agents  
- TLS traffic to unknown IPs  
- Beaconing patterns (regular intervals)  

---

## **Skills Demonstrated**
- Packet analysis  
- Network protocol understanding  
- Threat detection  
- IOC extraction  
- Investigative reasoning  
- SOC‑level traffic triage  
