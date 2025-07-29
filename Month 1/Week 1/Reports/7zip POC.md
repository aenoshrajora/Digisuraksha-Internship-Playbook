# Tool Name: 7-Zip 
Tool ID: 157

## History

7-Zip, created by Igor Pavlov in 1999, is a free and open-source file archiver widely used across forensics and system administration for compressing and extracting data securely.

## Description

7-Zip supports a wide range of archive formats and is renowned for its high compression ratio, lightweight design, and AES-256 encryption. It’s commonly used to unpack forensic disk images, isolate malware-laced archives, and maintain data integrity.

## What Is This Tool About?

Primarily a compression utility, 7-Zip serves forensic teams by safely extracting archives, preserving timestamps, and checking file integrity. It also provides command-line options for bulk and automated operations.

## Key Characteristics / Features

- Supports ZIP, RAR, 7z, TAR, GZ, ISO, CAB, and more
- Strong AES-256 encryption
- Open-source license (LGPL)
- Lightweight and portable
- Context-menu integration
- Command-line utility (7z.exe)
- Supports archive splitting
- Compression benchmarking tool
- File integrity check (CRC/SHA)
- Preserves original timestamps
- Password-protected extraction
- Drag-and-drop GUI
- Multi-volume archive extraction
- Batch operations
- Unicode file name support

## Types / Modules Available

- GUI Archive Manager
- CLI (7z.exe / 7za.exe)
- Benchmark Tool
- File Association Manager

## How Will This Tool Help?

- Safe extraction of suspicious file sets
- Password-protected archives used in DFIR workflows
- Automatable unpacking scripts
- Used to verify archive integrity during evidence acquisition

## Proof of Concept (PoC) Images

- Extracting archive from a forensic image
![alt text](./img/Extracting%20archive%20from%20a%20forensic%20image.png)

- CRC check
![alt text](./img/CRC%20check.png)

- CLI unpack script
![alt text](./img/CLI%20unpack%20script.png)

- Archive properties showing metadata
![alt text](./img/Archive%20properties%20showing%20metadata.png)

## 15-Liner Summary

- Free and open-source
- High compression ratio
- AES-256 encryption
- CLI and GUI modes
- Forensic archive extraction
- Portable and lightweight
- Archive format versatility
- Metadata preservation
- Hash-based integrity check
- Supports volume splitting
- Easy password support
- No installation required (portable)
- Scriptable for automation
- Silent mode for clean extraction
- Ideal for secure file storage in chain of custody

## Time to Use / Best Case Scenarios

- During unpacking of case evidence
- Hash validation and safe file access
- Extracting malware from encrypted zips

## When to Use During Investigation

- During evidence acquisition
- When dealing with large datasets
- Post-breach document recovery

## Best Person to Use This Tool & Required Skills

- Forensic Investigator, Malware Analyst, SOC Analyst
- Familiarity with CLI, compression concepts, hash verification

## Flaws / Suggestions to Improve

- Lacks deep archive inspection (no sandbox)
- Limited forensic logging
- No live memory compression option
- Can be abused by threat actors (e.g., zipped ransomware)

## Good About the Tool

- Universal utility in IR
- Robust encryption
- Trusted, well-maintained
- Scriptable and automatable for forensics pipeline