# SOC Level 1  
*A hands‑on TryHackMe room simulating real SOC analyst tasks, including log analysis, alert triage, and threat investigation.*

---

## **Overview**
SOC Level 1 introduces practical, job‑aligned workflows used by Security Operations Center analysts.  
This room focuses on analyzing logs, identifying suspicious activity, and understanding how alerts are generated and escalated.

This write‑up serves as a structured template for documenting your investigation and findings.

---

## **Objectives**
- Understand the responsibilities of a SOC Level 1 analyst  
- Analyze logs from multiple sources (Windows, Linux, network, SIEM)  
- Identify suspicious events and potential indicators of compromise  
- Practice alert triage and prioritization  
- Map attacker behavior to MITRE ATT&CK  
- Document findings in a professional SOC format  

---

## **Key Concepts Learned**

### **1. SOC Analyst Responsibilities**
- Monitoring SIEM alerts  
- Investigating suspicious activity  
- Escalating incidents when necessary  
- Documenting findings clearly  
- Maintaining situational awareness  

### **2. Alert Triage Workflow**
Typical steps:
1. Review alert details  
2. Identify affected hosts/users  
3. Check related logs  
4. Determine severity  
5. Escalate or close the alert  

### **3. Common Log Sources**
- Windows Event Logs  
- Linux system logs  
- Firewall logs  
- DNS logs  
- Web server logs  
- SIEM correlation alerts  

### **4. MITRE ATT&CK Mapping**
Examples of techniques often seen:
- T1110 — Brute Force  
- T1059 — Command Execution  
- T1047 — WMI Execution  
- T1021 — Remote Services  
- T1041 — Exfiltration Over C2 Channel  

---

## **Tools Used**
- SIEM platform (TryHackMe environment)  
- Log viewers  
- Windows Event Viewer  
- Linux CLI tools  
- Threat intelligence lookups  

---

## **Investigation Steps (Template)**  
*(Fill these in after completing the room.)*

### **1. Reviewing the Alert**
Document:
- alert name  
- severity  
- affected host  
- timestamp  
- triggering event  

### **2. Gathering Context**
Examples:
- checking related logs  
- identifying user activity  
- reviewing network connections  
- correlating multiple events  

### **3. Identifying Suspicious Indicators**
Possible findings:
- repeated failed logins  
- unusual PowerShell commands  
- unexpected outbound traffic  
- suspicious process execution  
- odd DNS queries  

### **4. MITRE ATT&CK Mapping**
Record:
- techniques observed  
- tactics involved (Initial Access, Execution, Persistence, etc.)  

### **5. Determining Severity**
Consider:
- impact  
- scope  
- likelihood  
- whether escalation is required  

### **6. Recommended Actions**
Examples:
- isolate host  
- reset credentials  
- block IP  
- escalate to Tier 2  
- collect additional logs  

---

## **Key Findings (Template)**
*(Fill this in after completing the room.)*

- Summary of suspicious activity  
- Notable IPs, users, or processes  
- Techniques identified  
- Root cause (if determined)  
- Recommended remediation steps  

---

## **Skills Demonstrated**
- SOC alert triage  
- Log analysis  
- Threat detection  
- MITRE ATT&CK mapping  
- Investigative reasoning  
- Incident documentation  
- Blue‑team analytical workflow  

---

## **Notes**
This room is one of the most important for SOC career preparation.  
It builds the foundation for:
- Network Security Monitoring  
- Malware Analysis  
- Incident Response  
- SIEM‑based investigations  
- Real‑world SOC workflows  
