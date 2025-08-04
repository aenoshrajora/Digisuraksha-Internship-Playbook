# MITRE ATT&CK PoC – Network Denial of Service (DoS)
Intern: Aenosh
Organization: DigiSuraksha Parhari Foundation

## Tactic: Impact (TA0040)
Goal: Disrupt availability of services, systems, or networks to degrade performance or cause outages.

## Techniques:
1. **T1498.001 – Network DoS: Direct Network Flood**
    - Flooding network bandwidth using SYN, UDP, or ICMP packets.

2. **T1498.002 – Network DoS: Reflection Amplification**
    - Exploiting open services like DNS/NTP to reflect amplified traffic toward victim.

3. **T1499 – Endpoint DoS**
    - Triggering service or system crashes through malformed packets or resource exhaustion.

## Procedures:
### Technique 1 – Direct Network Flood (SYN Flood)
1. Attacker identifies open ports on target using Nmap.
2. Launches a SYN flood using hping3:

```bash
hping3 -S --flood -V -p 80 VICTIM_IP
```
3. Sends rapid TCP SYN packets without completing handshake → fills up half-open connections.
4. **Result:** Server becomes unresponsive or sluggish.

### Technique 2 – Reflection Amplification (DNS/NTP Abuse)
1. Attacker spoofs victim’s IP as source.
2. Sends small UDP queries to open DNS/NTP servers:

```bash
dig ANY example.com @open_dns_server
```
3. Response (10x–50x larger) is sent to victim’s IP.
4. **Result:** Victim overwhelmed with large amplified traffic.

### Technique 3 – Endpoint DoS (Ping of Death / Fork Bomb)
1. Attacker crafts oversized ICMP packet using ping:

```bash
ping -s 65535 VICTIM_IP
```
2. Or sends a fork bomb payload on exposed shell:

```bash
:(){ :|:& };:
```
3. Causes system instability, crashes or resource exhaustion (RAM/CPU)

# Mitigation Strategies:

| Technique | Detection & Prevention                                                                |
|-----------|---------------------------------------------------------------------------------------|
| T1498.001 | Rate-limit SYN/UDP, use SYN cookies, deploy DDoS protection at firewall/load balancer |
| T1498.002 | Disable open resolvers, restrict NTP/DNS responses, monitor spoofed traffic           |
| T1499     | Patch systems, use WAFs, restrict shell access, monitor for abnormal ICMP traffic     |

# Why This PoC Works
- Attacks use low-cost resources to generate high-impact disruption
- Leverages both direct and indirect (amplified) attack paths
- Common across hacktivism, ransomware extortion, and botnet operations

# References
- [TA0040 – Impact](https://attack.mitre.org/tactics/TA0040/)
- [T1498.001 – Direct Network Flood](https://attack.mitre.org/techniques/T1498/001/)
- [T1498.002 – Reflection Amplification](https://attack.mitre.org/techniques/T1498/002/)
- [T1499 – Endpoint DoS](https://attack.mitre.org/techniques/T1499/)
