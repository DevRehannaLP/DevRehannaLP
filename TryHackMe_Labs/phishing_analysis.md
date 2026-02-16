# Phishing Analysis  
*A TryHackMe room focused on identifying, analyzing, and triaging phishing emails and malicious attachments.*

---

## **Overview**
Phishing Analysis teaches the essential skills needed to investigate suspicious emails, extract indicators, analyze attachments, and determine whether an email poses a threat.  
This room mirrors real SOC workflows, where analysts must quickly triage phishing reports and escalate when necessary.

This write‑up serves as a structured template for documenting your findings once you complete the room.

---

## **Objectives**
- Understand common phishing techniques  
- Analyze email headers and metadata  
- Identify malicious links and attachments  
- Extract indicators of compromise (IOCs)  
- Perform static analysis on suspicious files  
- Determine whether an email is malicious, benign, or spam  
- Strengthen SOC‑level phishing triage skills  

---

## **Key Concepts Learned**

### **1. Types of Phishing**
- Credential harvesting  
- Malware delivery  
- Business Email Compromise (BEC)  
- Spear phishing  
- Impersonation attacks  
- Fake invoices / payment fraud  

### **2. Email Header Analysis**
Key fields to review:
- `From:`  
- `Reply-To:`  
- `Return-Path:`  
- `Received:` chain  
- SPF, DKIM, DMARC results  

Red flags:
- mismatched domains  
- suspicious sending servers  
- forged headers  
- unusual reply‑to addresses  

### **3. Link Analysis**
Techniques include:
- hovering to reveal real URLs  
- checking for typosquatting  
- analyzing redirect chains  
- identifying IP‑based URLs  
- spotting URL shorteners  

### **4. Attachment Analysis**
Static analysis may include:
- hashing the file  
- extracting strings  
- identifying macros  
- checking file metadata  
- scanning with sandbox tools (if provided)  

### **5. Indicators of Compromise (IOCs)**
Examples:
- malicious URLs  
- suspicious domains  
- file hashes  
- sender IP addresses  
- embedded payloads  

---

## **Tools Used**
- Email header analyzer  
- Strings utility  
- Hashing tools  
- Sandbox or detonation environment  
- URL analysis tools  
- TryHackMe phishing investigation interface  

---

## **Investigation Steps (Template)**  
*(Fill these in after completing the room.)*

### **1. Reviewing the Email**
Document:
- sender  
- subject  
- timestamp  
- initial red flags  
- user report details  

### **2. Header Analysis**
Examples:
- mismatched sender domain  
- suspicious mail server  
- SPF/DKIM/DMARC failures  
- anomalies in the `Received:` chain  

### **3. Link Inspection**
Record:
- extracted URLs  
- redirect behavior  
- domain reputation  
- any signs of credential harvesting  

### **4. Attachment Analysis**
Document:
- file type  
- hashes  
- suspicious strings  
- embedded URLs  
- macro presence  
- sandbox behavior (if applicable)  

### **5. IOC Extraction**
List:
- domains  
- URLs  
- IPs  
- file hashes  
- email addresses  
- any other artifacts  

### **6. Final Determination**
Possible outcomes:
- malicious  
- suspicious  
- spam  
- benign  

---

## **Key Findings (Template)**
*(Fill this in after completing the room.)*

- Summary of phishing indicators  
- Notable IOCs  
- Techniques used by attacker  
- Potential impact  
- Recommended remediation steps  

---

## **Skills Demonstrated**
- Email header analysis  
- URL and domain investigation  
- Static file analysis  
- IOC extraction  
- Threat classification  
- SOC‑level phishing triage  
- Clear incident documentation  

---

## **Notes**
Phishing is one of the most common attack vectors in real organizations.  
This room prepares you for:
- SOC Tier 1 alert handling  
- Email security investigations  
- Malware triage  
- Incident response workflows  
