# Security Fundamentals  
*Google Cybersecurity Certificate — Module Notes*

---

## **1. What Is Cybersecurity?**
Cybersecurity is the practice of protecting systems, networks, and data from unauthorized access, attacks, and damage.  
Core goals are defined by the **CIA Triad**:
- **Confidentiality** – prevent unauthorized access  
- **Integrity** – prevent unauthorized modification  
- **Availability** – ensure systems/data are accessible when needed  

---

## **2. Types of Cybersecurity Threats**
### **Malware**
Malicious software designed to harm systems.  
Examples:  
- viruses  
- worms  
- trojans  
- ransomware  
- spyware  

### **Phishing**
Social engineering attack that tricks users into revealing information.

### **DDoS Attacks**
Overwhelm systems with traffic to make them unavailable.

### **Insider Threats**
Employees or contractors who misuse access.

### **Zero‑Day Exploits**
Attacks on vulnerabilities before patches exist.

---

## **3. Security Controls**
Security controls reduce risk and protect assets.

### **Administrative Controls**
Policies, procedures, training  
Examples:  
- security awareness training  
- acceptable use policies  
- incident response plans  

### **Technical Controls**
Technology‑based protections  
Examples:  
- firewalls  
- encryption  
- MFA  
- antivirus  
- SIEM tools  

### **Physical Controls**
Protect physical access  
Examples:  
- locks  
- cameras  
- security guards  
- access badges  

---

## **4. Authentication vs Authorization**
### **Authentication**
Verifies identity  
Examples:  
- passwords  
- biometrics  
- MFA  

### **Authorization**
Determines what a user can access  
Examples:  
- file permissions  
- role‑based access control (RBAC)  

---

## **5. Principle of Least Privilege**
Users should only have the minimum access needed to perform their job.  
Benefits:  
- reduces attack surface  
- limits damage from compromised accounts  

---

## **6. Encryption Basics**
Encryption protects data by converting it into unreadable form.

### **Types of Encryption**
- **Symmetric:** same key for encryption/decryption  
- **Asymmetric:** public/private key pair  

### **Data States**
- **Data at rest** – stored on disk  
- **Data in transit** – moving across networks  
- **Data in use** – actively processed  

---

## **7. Security Frameworks**
Frameworks provide structure for managing security.

### **NIST Cybersecurity Framework (CSF)**
Five core functions:  
1. Identify  
2. Protect  
3. Detect  
4. Respond  
5. Recover  

### **ISO 27001**
International standard for information security management.

---

## **8. Risk Management**
Risk = Threat × Vulnerability × Impact

### **Risk Treatment Options**
- **Mitigate** – reduce risk  
- **Transfer** – insurance, outsourcing  
- **Accept** – acknowledge risk  
- **Avoid** – remove the risk entirely  

---

## **9. Incident Response Basics**
Incident response lifecycle:

1. **Preparation**  
2. **Identification**  
3. **Containment**  
4. **Eradication**  
5. **Recovery**  
6. **Lessons Learned**  

SOC analysts often work in the **Identification** and **Containment** phases.

---

## **10. Logging & Monitoring**
Logs provide visibility into system activity.

Common log types:
- authentication logs  
- network logs  
- system logs  
- application logs  
- firewall logs  

SIEM tools (like Splunk) help analysts:
- detect threats  
- correlate events  
- investigate incidents  

---

## **Summary**
This module introduces the foundational concepts of cybersecurity: threats, controls, frameworks, risk management, and incident response. These fundamentals are essential for SOC analysts and form the basis for more advanced security work.
