# Windows Fundamentals  
*A foundational TryHackMe room introducing Windows architecture, navigation, system tools, and event logs.*

---

## **Overview**
Windows Fundamentals covers the essential skills needed to navigate and understand the Windows operating system — a critical requirement for SOC analysts, incident responders, and blue‑team defenders.

This write‑up serves as a structured template for documenting your learning and findings as you progress through the room.

---

## **Objectives**
- Understand Windows file system structure  
- Learn key system directories and their purposes  
- Explore user accounts, permissions, and groups  
- Practice using built‑in Windows tools  
- Review Windows Event Logs and common log sources  
- Strengthen OS‑level investigation skills  

---

## **Key Concepts Learned**

### **1. Windows File System Structure**
Important directories:
- `C:\Users\` — user profiles  
- `C:\Windows\System32\` — core system files  
- `C:\Program Files\` — installed applications  
- `C:\ProgramData\` — shared application data  
- `C:\Windows\Temp\` — temporary files  

### **2. User Accounts & Groups**
Understanding:
- local users  
- administrators  
- standard users  
- built‑in groups (Administrators, Users, Guests)  

### **3. Essential Windows Tools**
Command Line:
```
dir
cd
type
tasklist
ipconfig
```

PowerShell:
```
Get-Process
Get-Service
Get-EventLog
Get-LocalUser
```

GUI Tools:
- Task Manager  
- Event Viewer  
- Services.msc  
- File Explorer  

### **4. Windows Event Logs**
Key logs for SOC work:
- **Security** — authentication, access, privilege use  
- **System** — driver and service events  
- **Application** — software‑related events  
- **PowerShell** — script execution  
- **Sysmon** (if installed) — detailed process/network activity  

---

## **Tools Used**
- Windows Command Prompt  
- PowerShell  
- Event Viewer  
- Task Manager  
- TryHackMe’s Windows learning environment  

---

## **Investigation Steps (Template)**  
*(Fill these in after completing the room.)*

### **1. Exploring the File System**
Document:
- directories reviewed  
- hidden/system files discovered  
- interesting paths  

### **2. Reviewing User Accounts**
Examples:
- listing users  
- identifying admin accounts  
- checking group memberships  

### **3. Process & Service Analysis**
Record:
- suspicious processes  
- unusual services  
- resource usage observations  

### **4. Event Log Review**
Document:
- authentication events  
- warnings/errors  
- PowerShell activity  
- any anomalies found  

### **5. Network Information**
Examples:
- IP configuration  
- active connections  
- hostname and system details  

---

## **Key Findings (Template)**
*(Fill this in after completing the room.)*

- Notable events in logs  
- Suspicious processes or services  
- Interesting system behavior  
- Any security‑relevant observations  

---

## **Skills Demonstrated**
- Windows OS navigation  
- User and group enumeration  
- Process and service analysis  
- Event log review  
- PowerShell fundamentals  
- SOC‑level Windows investigation skills  

---

## **Notes**
Windows is a core operating system in enterprise environments.  
This room builds the foundation for:
- SOC Level 1  
- Windows Event Log analysis  
- Malware investigations  
- Incident response  
- Blue Team operations  
