
# Eternal Veridian Hydra

*A Historical Analysis Tool for Demonstrating Early 21st Century Authentication Protocol Vulnerabilities*

---

## 📖 Overview

**Eternal Veridian Hydra** is a Python-based command-line tool designed for cybersecurity researchers and historians studying the fragility of early 21st-century authentication systems. This tool simulates concurrent verification requests across multiple (40+) legacy service provider APIs, demonstrating how phone number-based verification systems could be overwhelmed by coordinated, simulated sign-up attempts.

> **Disclaimer:** This tool is intended for **educational and research purposes only** in controlled environments. Use on any system or phone number without explicit permission is strictly prohibited.

---

## 🚀 Quick Start

### Step 1: Install Prerequisites

**Windows:**
```cmd
python --version
pip install requests
```

macOS:

```bash
python3 --version
pip3 install requests
```

Linux (Ubuntu/Debian):

```bash
sudo apt update
sudo apt install python3 python3-pip git
pip3 install requests
```

Termux (Android):

```bash
pkg update && pkg upgrade
pkg install python git
pip install requests
```

Step 2: Download the Tool

Method A - Git Clone:

```bash
git clone https://github.com/696XXX/Hydra-spammer.git
cd Hydra-spammer
```

Method B - Direct Download:

```bash
mkdir Hydra-spammer && cd Hydra-spammer
curl -o hydra_pulse.py "https://raw.githubusercontent.com/696XXX/Hydra-spammer/refs/heads/main/hydra_pulse.py"
```

Method C - Manual Download:

1. Visit: https://github.com/696XXX/Hydra-spammer
2. Click hydra_pulse.py
3. Copy raw content and save as hydra_pulse.py

Step 3: Run the Tool

Basic Usage:

```bash
python3 hydra_pulse.py +1234567890
```

With Custom Delay:

```bash
python3 hydra_pulse.py +1234567890 --delay 1.5
```

Stop the Tool:

```bash
Press CTRL + C
```

---

⚙️ Features

· Dynamic Target Specification: Target phone number as command-line argument
· 40+ Service Simulation: Multiple legacy service endpoints
· Concurrent Requests: Multi-threaded architecture
· Configurable Timing: Adjustable delay between cycles (0.1-10 seconds)
· Persistent Operation: Runs until manually stopped
· Cross-Platform: Works on Windows, macOS, Linux, Android (Termux)

---

🛠️ Complete Installation Guide

Python Verification & Installation

Check if Python is installed:

```bash
python3 --version  # macOS/Linux
python --version   # Windows
```

If not installed:

Windows:

1. Download from https://python.org/downloads/
2. Run installer → Check "Add Python to PATH" → Install

macOS:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python
```

Linux:

```bash
sudo apt install python3 python3-pip
```

Termux:

```bash
pkg install python
```

Install Required Library

```bash
pip install requests
```

If pip fails:

```bash
python3 -m pip install requests
pip3 install requests
py -m pip install requests  # Windows alternative
```

Get the Script

Option 1 - Git (Recommended):

```bash
git clone https://github.com/your-username/eternal-veridian-hydra.git
cd eternal-veridian-hydra
```

Option 2 - Direct Download:

```bash
# macOS/Linux/Termux
curl -o hydra_pulse.py "https://raw.githubusercontent.com/696XXX/Hydra-spammer/refs/heads/main/hydra_pulse.py"

# Windows PowerShell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/696XXX/Hydra-spammer/refs/heads/main/hydra_pulse.py" -OutFile "hydra_pulse.py"
```

Option 3 - Manual Creation:
Create filehydra_pulse.py and paste the code from GitHub.

---

🎯 Usage Examples

Basic Test Run

```bash
python3 hydra_pulse.py +1000000000
```

Different Number Formats

```bash
# US Number
python3 hydra_pulse.py +1234567890

# UK Number
python3 hydra_pulse.py +441234567890

# Indonesian Number
python3 hydra_pulse.py +628123456789
```

Custom Configuration

```bash
# Aggressive (fast cycles)
python3 hydra_pulse.py +1234567890 --delay 0.3

# Conservative (slow cycles)
python3 hydra_pulse.py +1234567890 --delay 5.0

# Save output to file
python3 hydra_pulse.py +1234567890 > results.log 2>&1
```

Platform-Specific Commands

Windows:

```cmd
python hydra_pulse.py +1234567890
py hydra_pulse.py +1234567890
```

macOS/Linux:

```bash
python3 hydra_pulse.py +1234567890
```

Termux:

```bash
python hydra_pulse.py +1234567890
```

---

🛑 Troubleshooting

Common Issues & Solutions

"python3: command not found"

· Use python instead of python3 on Windows
· Install Python3 using platform-specific instructions above

"ModuleNotFoundError: No module named 'requests'"

```bash
pip install requests
python3 -m pip install requests
```

"git: command not found"

· Use Direct Download method instead of git clone
· Install git: sudo apt install git (Linux) or download from git-scm.com (Windows)

Permission Errors (macOS/Linux)

```bash
chmod +x hydra_pulse.py
pip3 install requests --user
```

SSL Certificate Errors

```bash
python3 -c "import ssl; ssl._create_default_https_context = ssl._create_unverified_context"
```

Verification Steps

1. Check Python: python3 --version (should show 3.6+)
2. Check requests: python3 -c "import requests; print('OK')"
3. Check file: ls hydra_pulse.py (should exist)
4. Run test: python3 hydra_pulse.py +1000000000

Expected Output

```
============================================================
    ETERNAL VERIDIAN HYDRA - ACTIVATED
============================================================
[+] Target: +1234567890
[+] Cycle Delay: 2.0 seconds
[+] Service Endpoints: 40
[!] Press CTRL + C to terminate the eternal storm.
============================================================

[--- Beginning Hydra Cycle #1 ---]
[+] Pulse to https://api.service-alpha.com/v1/verify - Status: 200
[!] Pulse to https://gateway.bravo-app.net/request_otp failed: ...
```

---

⚠️ Important Notes

· Many endpoints are historical and may not respond - this is normal
· The tool demonstrates attack patterns, not necessarily working services
· Use E.164 phone number format: +[country code][number]
· Default delay is 2.0 seconds between cycles
· Stop with CTRL + C
· Test with dummy numbers first: +1000000000, +15555555555

---

🔧 Advanced Configuration

Modify Service Endpoints

Edit the SERVICE_ENDPOINTS list in hydra_pulse.py to add/remove services.

Add Custom Headers

Modify the USER_AGENTS list to rotate different user agents.

Adjust Timeouts

Change timeout=15 in the requests.post() calls for different network conditions.

---

🆘 Emergency Stop

Normal Stop:

```bash
Press CTRL + C
```

Force Stop:

```bash
# Windows
taskkill /f /im python.exe

# macOS/Linux
pkill -f python3

# Termux
pkill -f python
```

---

📞 Support

If issues persist:

1. Verify all prerequisites are installed
2. Check internet connection
3. Try Direct Download method if Git fails
4. Test with different phone number formats
5. Ensure you're in the correct directory containing hydra_pulse.py

Remember: This is an educational tool for understanding historical vulnerabilities in authentication systems.

```
