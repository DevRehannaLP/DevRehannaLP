# Threats and Vulnerabilities  
*Google Cybersecurity Certificate — Module Notes*

---

## **1. What Is a Threat?**
A **threat** is any event or actor that can exploit a vulnerability to cause harm.

### **Types of Threat Actors**
- **Cybercriminals** – financially motivated  
- **Hacktivists** – politically or socially motivated  
- **Insider threats** – employees or contractors  
- **Nation‑state actors** – highly skilled, well‑funded  
- **Script kiddies** – inexperienced attackers using pre‑made tools  

---

## **2. What Is a Vulnerability?**
A **vulnerability** is a weakness in a system, application, or process that can be exploited.

### **Common Vulnerability Categories**
- **Software flaws** (bugs, outdated versions)  
- **Misconfigurations** (open ports, weak permissions)  
- **Weak passwords**  
- **Unpatched systems**  
- **Default credentials**  
- **Lack of encryption**  

---

## **3. Common Cybersecurity Threats**
### **Malware**
Malicious software designed to damage or compromise systems.  
Types include:  
- **Viruses**  
- **Worms**  
- **Trojans**  
- **Ransomware**  
- **Spyware**  
- **Adware**  

### **Phishing**
Social engineering attack that tricks users into revealing sensitive information.

### **Man‑in‑the‑Middle (MITM) Attacks**
Attacker intercepts communication between two parties.

### **SQL Injection**
Attacker manipulates database queries through input fields.

### **Cross‑Site Scripting (XSS)**
Injecting malicious scripts into web pages viewed by others.

### **Brute Force Attacks**
Repeated attempts to guess passwords.

### **DDoS Attacks**
Overwhelming a system with traffic to make it unavailable.

---

## **4. Vulnerability Scanning**
Automated tools identify weaknesses in systems.

### **Common Tools**
- Nessus  
- OpenVAS  
- Qualys  

### **What Scanners Look For**
- outdated software  
- missing patches  
- weak configurations  
- open ports  
- known CVEs  

---

## **5. CVE and CVSS**
### **CVE (Common Vulnerabilities and Exposures)**
A catalog of publicly known vulnerabilities.

### **CVSS (Common Vulnerability Scoring System)**
Rates severity from **0.0 to 10.0**.

| Score Range | Severity |
|-------------|----------|
| 0.0–3.9 | Low |
| 4.0–6.9 | Medium |
| 7.0–8.9 | High |
| 9.0–10.0 | Critical |

---

## **6. Exploits**
An **exploit** is code or a technique that takes advantage of a vulnerability.

### **Exploit Types**
- remote code execution  
- privilege escalation  
- buffer overflow  
- directory traversal  

---

## **7. Zero‑Day Vulnerabilities**
A vulnerability that is unknown to the vendor and has no patch available.

Zero‑day exploits are extremely dangerous because:
- no defenses exist yet  
- attackers can strike before detection  

---

## **8. Indicators of Compromise (IOCs)**
Artifacts that suggest a system may be compromised.

Examples:
- unusual outbound traffic  
- unknown processes  
- suspicious file hashes  
- repeated login failures  
- unexpected privilege escalation  

---

## **9. Indicators of Attack (IOAs)**
Patterns that indicate an attack is *in progress*.

Examples:
- lateral movement attempts  
- privilege escalation attempts  
- abnormal command execution  
- suspicious PowerShell or Bash activity  

---

## **10. Mitigation Strategies**
### **Technical Controls**
- firewalls  
- IDS/IPS  
- endpoint protection  
- encryption  
- MFA  

### **Administrative Controls**
- policies  
- training  
- incident response plans  

### **Physical Controls**
- access badges  
- cameras  
- locked server rooms  

---

## **11. Patch and Update Management**
Keeping systems updated reduces vulnerabilities.

Best practices:
- prioritize critical patches  
- test before deployment  
- maintain patch schedules  
- automate updates where possible  

---

## **Summary**
This module covers threats, vulnerabilities, exploits, CVEs, IOCs, IOAs, and mitigation strategies. Understanding how attackers operate — and how vulnerabilities are exploited — is essential for SOC analysts and cybersecurity professionals.
