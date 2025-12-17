# PII Sanitization Tool

A Python-based utility designed to mask **Personally Identifiable Information (PII)** and sensitive financial data from log files or text documents. This ensures compliance with **Bank Negara Malaysia (BNM)** standards and **PDPA** requirements before sharing data with external LLMs or third-party tools like GitHub Copilot.

## Features

* **Financial Data Masking:** Automatically detects and masks Card Numbers, Account Numbers, and Transaction IDs.
* **Identity Protection:** Redacts NRIC (IC Numbers), Passport Numbers, and Driver Licenses.
* **Security Scrubber:** Removes passwords, API keys, private keys, and hashes.
* **Contact Info:** Masks Malaysian phone numbers, emails, and IP addresses.
* **Flexible Output:** Create a new `_safe` copy by default or overwrite files using the `--in-place` flag.

---

## Installation

To install the tool using the provided wheel file, run one of the following commands in your terminal (ensure you are in the project root directory):

```bash
# Using pip
pip install --force-reinstall dist/pii_sanitization-1.0.0-py3-none-any.whl

# Or using pip3
pip3 install --force-reinstall dist/pii_sanitization-1.0.0-py3-none-any.whl

```

---

## Usage

Once installed, the `pii-sanitization` command will be available in your terminal.

### 1. Basic Sanitization (Creates a Copy)

By default, the tool creates a new file with the suffix `_safe`. The original file remains untouched.

```bash
pii-sanitization <path_to_your_file_to_be_masked>

```

*Example:* `pii-sanitization app_logs.txt` will create `app_logs_safe.txt`.

### 2. Sanitize Multiple Files

You can pass multiple files at once:

```bash
pii-sanitization log1.txt log2.log data.csv

```

### 3. In-Place Overwrite

If you wish to overwrite the original file directly without creating a copy, use the `--in-place` flag:

```bash
pii-sanitization --in-place <path_to_your_file.log>

```

### 4. Help Command

To see all available options, run:

```bash
pii-sanitization --help

```

---

## Masking Logic Overview

The tool uses regex-based rules to identify and replace sensitive patterns:

| Data Type | Masked Format |
| --- | --- |
| **NRIC / MyKad** | `[IC NUMBER]` |
| **Bank Account** | `[ACCOUNT NUMBER]` |
| **Credit Card** | `[CARD NUMBER]` |
| **Passwords/Secrets** | `[PASSWORD]` / `[SECRET]` |
| **Private Keys** | `[PRIVATE KEY]` |
| **MY Phone No.** | `[PHONE NUMBER]` |

---

## Development

If you need to rebuild the distribution file after making changes to `sanitizer.py`:

1. Ensure you have the `build` package: `pip install build`
2. Run the build command: `python -m build`
3. Re-install the new `.whl` file from the `dist/` folder.

**Author:** Elly (ellynoorsyakirahimana.rokmanuddin@maybank.com)

---