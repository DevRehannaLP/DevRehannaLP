# Blue Primer  
*An introductory TryHackMe room focused on Blue Team fundamentals and defensive security concepts.*

---

## **Overview**
Blue Primer introduces the foundational concepts of defensive security, including monitoring, detection, incident response, and the mindset of a SOC analyst.  
This room sets the stage for more advanced blue‑team labs by explaining how defenders identify, analyze, and respond to threats.

This write‑up serves as a structured template for documenting your learning and findings.

---

## **Objectives**
- Understand the role of the Blue Team in cybersecurity  
- Learn core defensive concepts (monitoring, detection, response)  
- Explore common attack techniques from a defender’s perspective  
- Review log sources and defensive tooling  
- Practice identifying suspicious activity  

---

## **Key Concepts Learned**

### **1. Blue Team Responsibilities**
- Monitoring systems and networks  
- Detecting malicious activity  
- Investigating alerts  
- Responding to incidents  
- Hardening systems  
- Maintaining visibility  

### **2. Common Defensive Tools**
- SIEM platforms  
- EDR solutions  
- Network monitoring tools  
- Log analysis utilities  
- Threat intelligence feeds  

### **3. Attack Techniques (Defender View)**
Understanding attacker behavior helps defenders detect:
- brute‑force attempts  
- privilege escalation  
- lateral movement  
- data exfiltration  
- malware execution  

### **4. Logs & Visibility**
Key log types:
- authentication logs  
- process execution logs  
- network traffic logs  
- DNS logs  
- firewall logs  

---

## **Tools Used**
- TryHackMe’s Blue Team learning environment  
- Log viewers  
- Basic SIEM interface (if provided)  
- Threat intelligence references  

---

## **Investigation Steps (Template)**  
*(Fill these in after completing the room.)*

### **1. Reviewing Provided Logs**
- Identified log sources  
- Noted key fields (timestamp, user, IP, event type)  
- Observed normal vs. abnormal patterns  

### **2. Identifying Suspicious Activity**
Examples you may document:
- repeated failed logins  
- unusual process execution  
- odd network connections  
- suspicious DNS queries  

### **3. Mapping Activity to MITRE ATT&CK**
Document which techniques were observed, such as:
- T1110 — Brute Force  
- T1059 — Command Execution  
- T1046 — Network Scanning  

### **4. Defensive Response**
Describe:
- what actions a SOC analyst would take  
- how to escalate or contain the threat  
- what logs or tools would be used next  

---

## **Key Findings (Template)**
*(Fill this in after completing the room.)*

- Summary of suspicious events  
- Notable IPs or users  
- Any attacker behavior identified  
- Defensive insights gained  

---

## **Skills Demonstrated**
- Blue Team fundamentals  
- Log analysis  
- Threat detection  
- MITRE ATT&CK mapping  
- Defensive investigation workflow  
- SOC mindset development  

---

## **Notes**
This room builds the mindset required for SOC analysis and prepares you for hands‑on defensive labs such as:
- SOC Level 1  
- Network Security Monitoring  
- Malware Analysis Basics  
- Windows & Linux investigations  
