# Intro to SIEM  
*A foundational TryHackMe room introducing Security Information and Event Management concepts.*

---

## **Overview**
This lab introduces the core purpose and functionality of SIEM platforms.  
It covers how SIEMs collect, normalize, correlate, and analyze logs to help SOC analysts detect and investigate security events.

This write‑up documents the key concepts, tasks, and takeaways from the room.

---

## **Objectives**
- Understand what a SIEM is and why SOCs use it  
- Learn how logs are ingested and normalized  
- Explore event correlation and alerting  
- Practice basic searching and filtering  
- Review common SIEM use cases  

---

## **Key Concepts Learned**

### **1. What a SIEM Does**
- Collects logs from multiple sources  
- Normalizes data into a consistent format  
- Correlates events to detect suspicious behavior  
- Generates alerts for analysts  
- Provides dashboards and visualizations  

### **2. Log Sources**
Typical logs ingested into a SIEM include:
- Windows Event Logs  
- Linux system logs  
- Firewall logs  
- DNS logs  
- Authentication logs  
- Application logs  

### **3. Event Correlation**
SIEMs identify patterns such as:
- multiple failed logins  
- lateral movement  
- suspicious DNS queries  
- unusual outbound traffic  

### **4. Alerts & Dashboards**
Analysts use:
- prebuilt dashboards  
- custom queries  
- alert rules  
- visualizations  

---

## **Tools Used**
- SIEM platform provided by TryHackMe  
- Basic search and filtering interface  
- Log viewer  
- Event correlation tools  

---

## **Investigation Steps (Template)**
*(You will fill these in once you complete the room.)*

### **1. Initial Exploration**
- Reviewed available log sources  
- Explored dashboards and event summaries  
- Identified key fields (timestamp, user, IP, event type)  

### **2. Searching Logs**
Examples of searches performed:
- authentication events  
- failed logins  
- DNS queries  
- process execution  

### **3. Identifying Suspicious Activity**
Document any anomalies such as:
- repeated login failures  
- unusual IP addresses  
- odd process names  
- unexpected network connections  

### **4. Reviewing Alerts**
- Checked triggered alerts  
- Analyzed alert details  
- Identified root cause  

---

## **Key Findings (Template)**
*(Fill this in after completing the room.)*

- Summary of suspicious events  
- Notable IPs or users  
- Any detected anomalies  
- What the SIEM revealed  

---

## **Skills Demonstrated**
- SIEM fundamentals  
- Log analysis  
- Event correlation  
- Alert triage  
- Basic threat detection  
- SOC investigation workflow  

---

## **Notes**
This room builds the foundation for more advanced SIEM and SOC labs.  
It prepares you for hands‑on work in Splunk, Elastic, and other SIEM platforms.
