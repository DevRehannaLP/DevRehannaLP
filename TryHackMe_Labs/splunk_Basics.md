# Splunk Basics  
*A TryHackMe room introducing Splunk searching, dashboards, and SIEM workflows.*

---

## Overview
This room teaches the fundamentals of using Splunk for log analysis, searching, and alerting — essential skills for SOC analysts.

---

## Objectives
- Learn Splunk search syntax  
- Explore indexes, sourcetypes, and fields  
- Build basic searches  
- Review dashboards  
- Analyze events and identify anomalies  

---

## Key Concepts Learned
- SPL (Search Processing Language)  
- Indexing and data ingestion  
- Field extraction  
- Time-based searching  
- Basic alerting  

---

## Tools Used
- Splunk Web  
- SPL queries  
- Dashboards and visualizations  

---

## Investigation Steps (Template)
### 1. Exploring Data  
- Identifying indexes  
- Reviewing sourcetypes  

### 2. Running Searches  
Examples:
```
index=* error
index=windows EventCode=4625
```

### 3. Filtering & Fields  
- Using `stats`, `table`, `where`  
- Extracting relevant fields  

### 4. Identifying Suspicious Activity  
- Failed logins  
- Odd processes  
- Network anomalies  

---

## Key Findings (Template)

---

## Skills Demonstrated
- SPL querying  
- SIEM analysis  
- Log filtering  
- Event triage  
