# SOC Alert Analysis  
*A hands‑on investigation of simulated security alerts using Splunk.*

---

## **Overview**
This project demonstrates the process of analyzing security alerts in a SIEM environment. Using Splunk, I investigated suspicious login activity, reviewed event logs, and documented findings that reflect real SOC analyst workflows.

---

## **Objectives**
- Analyze authentication logs  
- Identify suspicious login patterns  
- Investigate source IP addresses  
- Correlate events across multiple log sources  
- Document findings and recommended actions  

---

## **Tools Used**
- Splunk  
- Linux CLI  
- WHOIS lookup  
- IP geolocation tools  

---

## **Investigation Steps**
1. Reviewed authentication logs for failed and successful login attempts  
2. Identified unusual login times and geographic anomalies  
3. Investigated source IP addresses for reputation and ownership  
4. Checked for lateral movement or privilege escalation  
5. Documented findings and recommended next steps  

---

## **Key Findings**
- Multiple failed login attempts followed by a successful login  
- Login originated from an unexpected geographic region  
- User behavior inconsistent with normal patterns  
- No evidence of lateral movement detected  

---

## **Recommendations**
- Enforce MFA for all user accounts  
- Review user access permissions  
- Monitor for repeated login anomalies  
- Educate users on account security best practices  

---

## **Skills Demonstrated**
- SIEM log analysis  
- Threat investigation  
- Event correlation  
- Documentation and reporting  
- Analytical thinking  
