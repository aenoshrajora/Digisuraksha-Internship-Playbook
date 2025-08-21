# 🛡️ Lightweight Network IDS

This project is a **lightweight Network Intrusion Detection System (IDS)** developed as part of an **internship at DigiSuraksha Parhari Foundation**.  
The IDS analyzes **offline PCAP files** and raises alerts for common suspicious activities such as pings, connection attempts, and basic scan patterns.

---

## ✨ Features
- **ICMP Detection**
  - Echo Request (ping)
  - Echo Reply

- **TCP Detection**
  - SYN packets (connection attempts / half-open connections)
  - NULL scans (no flags)
  - FIN scans

- **Payload Signature Matching**
  - Uses regex-based rules (from a TOML file) to match suspicious keywords in packet payloads.

---

## 📂 Project Structure
├── ids.py # Main IDS script
|-- requirements.txt # Project requirement packages
└── README.md # Documentation

---

## 🚀 Usage

### 1. Install dependencies
```bash
pip install scapy tomlkit intervaltree
```

### 2. Run the IDS
```bash
python3 ids.py rules.toml traffic.pcap
```
- `rules.toml` → Signature file with regex patterns
- `traffic.pcap` → PCAP file to analyze

## Example Alerts
```json
{
  "tv_sec": 1703251247,
  "tv_usec": 421000,
  "source": { "ipv4_address": "127.0.0.1", "tcp_port": 45321 },
  "target": { "ipv4_address": "127.0.0.1", "tcp_port": 22 },
  "attack": "TCP SYN (possible connection attempt/scan)"
}
```

## Demo Rules (rules.toml)

```toml
signatures = [
  "malware",
  "exploit",
  "root"
]
```

## Demo PCAPs
To generate your own test captures:

- Normal traffic (ICMP pings):
```bash
ping -c 4 8.8.8.8
sudo tcpdump -i any -w normal.pcap icmp
```

- Attack traffic (SYN scans with Nmap):
```bash
nmap -sS -p 22,80,443 127.0.0.1
sudo tcpdump -i lo -w attack.pcap tcp
```

# Limitations
- Works only with offline PCAP analysis.
- Does not include live sniffing or interactive TUI options.
- Simple rule-based IDS (not as advanced as Snort/Suricata).
- May raise false positives in noisy datasets.