# Linux Basics  
*Google Cybersecurity Certificate — Module Notes*

---

## **1. What Is Linux?**
Linux is an open‑source operating system widely used in servers, cybersecurity, cloud environments, and embedded systems.  
Key advantages:  
- stability  
- security  
- flexibility  
- command‑line power  

Cybersecurity analysts rely heavily on Linux for investigations, scripting, and system analysis.

---

## **2. Linux File System Structure**
Linux uses a hierarchical directory structure starting at the **root** `/`.

Common directories:

| Directory | Purpose |
|----------|----------|
| `/` | Root of the file system |
| `/home` | User home directories |
| `/etc` | Configuration files |
| `/var` | Logs and variable data |
| `/bin` | Essential binaries |
| `/usr` | User programs and utilities |
| `/tmp` | Temporary files |
| `/opt` | Optional software |

---

## **3. Basic Linux Commands**
### **Navigation**
- `pwd` — print working directory  
- `ls` — list files  
- `cd` — change directory  

### **File & Directory Management**
- `touch file.txt` — create file  
- `mkdir folder` — create directory  
- `cp source dest` — copy  
- `mv source dest` — move/rename  
- `rm file` — remove file  
- `rm -r folder` — remove directory  

### **Viewing Files**
- `cat file` — display file contents  
- `less file` — view file page by page  
- `head file` — first lines  
- `tail file` — last lines  

---

## **4. Permissions**
Linux uses a permission model for security.

Example output of `ls -l`:

```
-rwxr-xr--
```

Breakdown:

| Symbol | Meaning |
|--------|---------|
| `r` | read |
| `w` | write |
| `x` | execute |
| `-` | no permission |

Three groups:
1. **Owner**
2. **Group**
3. **Others**

### Changing permissions
- `chmod 755 file`  
- `chown user:group file`  

---

## **5. Package Management**
Depends on the distribution:

### **Debian/Ubuntu**
- `apt update`  
- `apt install package`  

### **Red Hat/CentOS**
- `yum install package`  
- `dnf install package`  

---

## **6. Processes & System Monitoring**
### **Common commands**
- `ps` — list processes  
- `top` — real‑time system monitor  
- `htop` — enhanced monitor (if installed)  
- `kill PID` — terminate process  

---

## **7. Networking Commands**
- `ifconfig` or `ip a` — view interfaces  
- `ping host` — test connectivity  
- `netstat -tulnp` — view ports  
- `ss -tulnp` — modern replacement for netstat  
- `nslookup domain` — DNS lookup  
- `traceroute host` — trace network path  

---

## **8. Logs & Monitoring**
Logs are stored in:

```
/var/log
```

Common logs:
- `auth.log` — authentication events  
- `syslog` — system events  
- `kern.log` — kernel messages  

View logs with:
- `cat`  
- `less`  
- `tail -f` (live updates)

---

## **9. Shell Scripting Basics**
Shell scripts automate tasks.

Example script:

```bash
#!/bin/bash
echo "Hello, world!"
```

Make executable:

```
chmod +x script.sh
```

Run:

```
./script.sh
```

---

## **10. Why Linux Matters in Cybersecurity**
SOC analysts use Linux for:
- log analysis  
- scripting  
- malware investigation  
- network monitoring  
- running security tools (Zeek, Suricata, Wireshark)  
- accessing servers via SSH  

Linux is foundational for blue‑team work.

---

## **Summary**
This module covers essential Linux concepts: navigation, permissions, processes, networking, logs, and scripting. Mastering Linux is critical for cybersecurity roles, especially SOC analysts who rely on command‑line tools for investigations and automation.
