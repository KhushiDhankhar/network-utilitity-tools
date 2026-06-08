# Network Utility & Cybersecurity Tools

A collection of cybersecurity and networking tools developed as part of my Cybersecurity Project Trainee program. These projects were built to strengthen my understanding of networking fundamentals, security concepts, Python programming, and system-level operations.

## Overview

This repository contains three security-focused tools:

1. **Port Scanner**
2. **Password Hashing & Verification Tool**
3. **Signature-Based Antivirus Scanner**

Each project demonstrates practical applications of cybersecurity principles such as network reconnaissance, cryptographic hashing, malware detection, and security auditing.

---

## Features

* Multi-threaded TCP Port Scanner
* Password Hashing and Verification
* Signature-Based Malware Detection
* Audit Logging for Security Monitoring
* Hostname and DNS Resolution
* Network Service Identification
* Thread-Safe Port Discovery Tracking
* Detailed Scan Reports

---

## Project 1: Port Scanner

### Description

A multi-threaded TCP port scanner that identifies open ports on a target host and attempts to determine the associated service running on each port.

### Key Features

* Scans user-specified port ranges
* Supports IP addresses and hostnames
* Multi-threaded scanning for improved performance
* Service detection using known port mappings
* Hostname resolution
* Audit logging with timestamps
* Session-based scan tracking

### Concepts Used

* TCP/IP Networking
* DNS Resolution
* Socket Programming
* Multi-threading
* Logging and Auditing

---

## Project 2: Password Hashing & Lookup Tool

### Description

A Python-based utility that generates hash digests for user passwords and stores password–hash mappings. The tool allows users to retrieve the original password corresponding to a stored hash by searching the maintained mapping database.

### Key Features

* Generate hash digests from user passwords8*
* Store password and hash mappings
* Search for passwords using stored hash values
* Demonstrate how hashing functions work
* Simple credential management system

### Concepts Used

* Cryptographic Hash Functions
* Data Storage and Retrieval
* Dictionary-Based Lookup
* Password Management Fundamentals
* Python File Handling

---

## Project 3: Signature-Based Antivirus Scanner

### Description

A simple antivirus scanner that detects known malicious files by comparing file contents against predefined malware signatures.

### Key Features

* Signature-based malware detection
* File scanning
* Known threat identification
* Detection reporting
* Security auditing

### Concepts Used

* Malware Detection
* Signature Matching
* Threat Analysis
* File Processing

---

## Audit Logging

The Port Scanner includes an audit logging system that records:

* Scan initiation
* Target resolution
* Open port discoveries
* Hostname resolution
* Scan completion summaries
* Session identifiers

Logs provide traceability and assist in troubleshooting and monitoring scan activity.

---

## Technologies Used

* Python
* Socket Programming
* Threading
* Logging Framework
* Networking Protocols
* DNS Resolution

---

## Networking Concepts Learned

During development of these projects, the following concepts were explored:

* OSI Model
* TCP/IP Model
* DNS (Domain Name System)
* DHCP (Dynamic Host Configuration Protocol)
* HTTP/HTTPS
* TCP and UDP Communication
* Port Scanning Techniques
* ICMP and Ping Operations
* Network Troubleshooting

---

## Educational Purpose

These tools were developed for educational and learning purposes to gain practical experience in cybersecurity, networking, and Python development.

Use these tools responsibly and only on systems that you own or have explicit permission to test.

---

## Future Improvements

* GUI Interface
* Advanced Service Detection
* Improved Malware Signature Database
* Real-Time Threat Monitoring
* Exportable Scan Reports
* Enhanced Logging and Analytics

---

## Author

khushi

Cybersecurity Project Trainee | Python Developer | Networking Enthusiast
