# Eternal Veridian Hydra

*A Historical Analysis Tool for Demonstrating Early 21st Century Authentication Protocol Vulnerabilities*

---

## 📖 Overview

**Eternal Veridian Hydra** is a Python-based command-line tool designed for cybersecurity researchers and historians studying the fragility of early 21st-century authentication systems. This tool simulates concurrent verification requests across multiple (40+) legacy service provider APIs, demonstrating how phone number-based verification systems could be overwhelmed by coordinated, simulated sign-up attempts.

This project serves as an educational artifact, illustrating the importance of rate limiting, CAPTCHA mechanisms, and robust identity verification in modern system design.

> **Disclaimer:** This tool is intended for **educational and research purposes only** in controlled environments. Use on any system or phone number without explicit permission is strictly prohibited.

---

## 🚀 Features

- **Dynamic Target Specification:** Target phone number provided as a command-line argument
- **Comprehensive Service Simulation:** 40+ configurable service endpoints simulating real-world verification flows
- **Concurrent Request Engine:** Multi-threaded architecture for simultaneous request execution
- **Configurable Timing:** Adjustable delay between attack cycles
- **Persistent Operation:** Continuous execution until manual termination
- **Request Logging:** Real-time status monitoring for each service endpoint

---

## ⚙️ Prerequisites

- Python 3.6 or higher
- `requests` library
- Git (for repository cloning)

### Installing Dependencies

```bash
pip install requests
