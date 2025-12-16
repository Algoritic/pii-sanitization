# Copilot Security Gateway

**Sanitize and proxy GitHub Copilot prompts for enterprise compliance**

---

## Overview

`copilot-gateway` is a **local proxy server** designed to **sanitize PII (Personally Identifiable Information) and sensitive data** from user prompts before sending them to **GitHub Copilot**.  

This ensures:

- Compliance with **PDPA** and **Bank Negara Malaysia** data privacy guidelines.  
- No raw PII leaves the corporate network.  
- Centralized control and logging of Copilot prompt traffic.

---

## Features

- Masks sensitive information such as:
  - Names, emails, phone numbers, IC/Passport/Driver license numbers
  - Bank account numbers, credit card numbers, transaction IDs
  - API keys, passwords, secrets, private keys
  - IP addresses, postal codes, dates, OTP/PIN, hashes
- Can be integrated with **VS Code Copilot** or **Copilot CLI**.
- Easy to run via **Uvicorn** or **Docker Compose**.
- Fully configurable via environment variables.

---

## Directory Structure
copilot-gateway/
├── app/
│   ├── init.py
│   ├── main.py          # FastAPI proxy app
│   ├── sanitizer.py     # PII masking logic
│   └── config.py        # Configurable settings
├── .venv/               # Python virtual environment
├── requirements.txt     # Python dependencies
├── Dockerfile
├── docker-compose.yml
└── README.md

---

## Installation

### 1. Clone repository

```bash
git clone <your-repo-url>
cd copilot-gateway
```

## Set up Python virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running Locally
```bash
uvicorn app.main:app --host 0.0.0.0 --port 3333 --reload
```

## VS Code Integration
1.	Open User Settings (JSON) in VS Code:
```bash
Cmd + Shift + P → Preferences: Open User Settings (JSON)
```
2. Add:
```json
"github.copilot.advanced": {
    "proxy": "http://localhost:3333"
}
```

3.	Restart VS Code.
4.	All Copilot requests will now go through the gateway.

## How It Works
	1.	User types a prompt in VS Code / Copilot CLI.
	2.	Prompt is sent to the gateway.
	3.	The gateway sanitizes all PII and sensitive info using sanitizer.py.
	4.	Sanitized prompt is forwarded to GitHub Copilot.
	5.	Copilot’s response is returned to the user.

