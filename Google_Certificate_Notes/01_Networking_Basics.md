# Networking Basics  
*Google Cybersecurity Certificate — Module Notes*

---

## **1. What Is a Network?**
A **network** is a group of devices connected to share data and resources.  
Key components include:  
- **Devices:** computers, servers, routers, switches  
- **Mediums:** wired (Ethernet), wireless (Wi‑Fi)  
- **Protocols:** rules for communication (TCP/IP)

---

## **2. Types of Networks**
### **LAN (Local Area Network)**
- Small geographic area (home, office)  
- High speed, low latency  

### **WAN (Wide Area Network)**
- Large geographic area  
- The internet is the largest WAN  

### **PAN (Personal Area Network)**
- Very small range (Bluetooth devices)

### **MAN (Metropolitan Area Network)**
- City‑wide networks (ISPs, universities)

---

## **3. OSI Model (7 Layers)**
A conceptual model describing how data moves through a network.

1. **Physical** – cables, signals  
2. **Data Link** – MAC addresses, switches  
3. **Network** – IP addresses, routing  
4. **Transport** – TCP/UDP  
5. **Session** – communication sessions  
6. **Presentation** – encryption, formatting  
7. **Application** – user applications (HTTP, DNS)

---

## **4. TCP vs UDP**
### **TCP (Transmission Control Protocol)**
- Reliable  
- Connection‑oriented  
- Slower  
- Used for: web browsing, email, file transfer  

### **UDP (User Datagram Protocol)**
- Fast  
- No guarantee of delivery  
- Used for: streaming, gaming, VoIP  

---

## **5. IP Addressing**
### **IPv4**
- 32‑bit  
- Example: `192.168.1.1`

### **IPv6**
- 128‑bit  
- Example: `2001:0db8:85a3::8a2e:0370:7334`

### **Public vs Private IP**
- **Public:** reachable from the internet  
- **Private:** internal network only  

---

## **6. Subnetting**
Subnetting divides networks into smaller segments.  
Key terms:  
- **Subnet mask**  
- **CIDR notation** (e.g., `/24`)  
- **Network vs host portions**

---

## **7. Common Network Devices**
- **Router:** connects networks  
- **Switch:** connects devices within a LAN  
- **Firewall:** filters traffic  
- **Access Point:** wireless connectivity  
- **Modem:** connects to ISP  

---

## **8. Common Network Protocols**
- **HTTP/HTTPS** – web traffic  
- **DNS** – domain name resolution  
- **DHCP** – automatic IP assignment  
- **FTP/SFTP** – file transfer  
- **SSH** – secure remote access  
- **SMTP/IMAP/POP3** – email  

---

## **9. Network Security Concepts**
### **Firewalls**
- Block/allow traffic based on rules  

### **IDS/IPS**
- IDS: detects  
- IPS: detects + blocks  

### **VPN**
- Encrypted tunnel for secure remote access  

### **Zero Trust**
- “Never trust, always verify”  

---

## **10. Troubleshooting Basics**
- **Ping:** test connectivity  
- **Traceroute:** identify path issues  
- **ipconfig/ifconfig:** view network settings  
- **nslookup:** test DNS  
- **netstat:** view active connections  

---

## **Summary**
This module covers the foundational concepts of networking — essential knowledge for SOC analysts, incident responders, and anyone working in cybersecurity. Understanding how data moves, how devices communicate, and how networks are secured is critical for detecting and responding to threats.
