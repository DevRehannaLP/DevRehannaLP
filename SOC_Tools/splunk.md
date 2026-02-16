# Splunk  
*A core SIEM tool used for log analysis, detection, and investigation.*

---

## **Overview**
Splunk is a Security Information and Event Management (SIEM) platform used to collect, index, search, and analyze machine data.  
SOC analysts rely on Splunk to detect threats, investigate incidents, and build dashboards.

---

## **Key Features**
- Log ingestion and indexing  
- Search Processing Language (SPL)  
- Dashboards and visualizations  
- Alerts and correlation rules  
- Real‑time monitoring  

---

## **Common SPL Commands**

### **Basic Searches**
```
index=security
index=windows
index=linux
```

### **Filtering**
```
index=security action=failure
index=windows EventCode=4625
```

### **Time Range**
```
index=security earliest=-24h
```

### **Field Extraction**
```
index=security | fields user, src_ip, dest_ip
```

### **Sorting**
```
index=security | sort - _time
```

### **Counting**
```
index=security | stats count by user
```

---

## **Useful SOC Queries**

### **Failed Logins**
```
index=windows EventCode=4625 | stats count by user, src_ip
```

### **Successful Logins**
```
index=windows EventCode=4624 | stats count by user, src_ip
```

### **Suspicious PowerShell**
```
index=windows process_name="powershell.exe" CommandLine="*encoded*"
```

### **DNS Anomalies**
```
index=dns query="*.xyz" | stats count by query
```

---

## **SOC Use Cases**
- Investigating authentication anomalies  
- Detecting brute‑force attempts  
- Tracking lateral movement  
- Monitoring PowerShell activity  
- Reviewing DNS queries for suspicious domains  

---

## **Skills Demonstrated**
- SPL proficiency  
- Log analysis  
- Event correlation  
- Threat detection  
- Dashboard creation  
