import re

def sanitize_text(text: str) -> str:
    """
    Mask PII, confidential, and secret data in text
    in line with Bank Negara Malaysia & PDPA expectations.
    """

    rules = [

        # =========================
        # 1. Explicit name fields
        # =========================
        (r'name\s*=\s*"[^"]+"', 'name="[FULL NAME]"'),
        (r'\b(?:Mr|Ms|Mrs|Dr)\.?\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+\b', '[FULL NAME]'),

        # =========================
        # 2. Government identifiers
        # =========================
        (r'\b\d{12}\b', '[IC NUMBER]'),                      # NRIC / MyKad
        (r'\b[A-Za-z]\d{7}\b', '[PASSPORT NUMBER]'),         # Passport
        (r'\bD\d{9,12}\b', '[DRIVER LICENSE]'),              # Driving license

        # =========================
        # 3. Financial information
        # =========================
        (r'\b(?:\d{4}[-\s]?){3,4}\b', '[CARD NUMBER]'),      # Card numbers
        (r'\b\d{10,20}\b', '[ACCOUNT NUMBER]'),              # Account numbers
        (r'\bTX\d+\b', '[TRANSACTION ID]'),                  # Transaction IDs
        (r'\bfrom_account="[^"]+"', 'from_account="[ACCOUNT NUMBER]"'),
        (r'\bto_account="[^"]+"', 'to_account="[ACCOUNT NUMBER]"'),

        # =========================
        # 4. Contact & location
        # =========================
        (r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', '[EMAIL]'),
        (r'\b01\d{8,9}\b', '[PHONE NUMBER]'),                # MY phone numbers
        (r'\b\d{5}\b', '[POSTAL CODE]'),
        (r'\b(?:\d{1,3}\.){3}\d{1,3}\b', '[IP ADDRESS]'),

        # =========================
        # 5. Dates (personal data)
        # =========================
        (r'\b\d{2}/\d{2}/\d{4}\b', '[DATE]'),
        (r'\b\d{4}-\d{2}-\d{2}\b', '[DATE]'),
        (r'dob\s*=\s*"[^"]+"', 'dob="[DATE]"'),

        # =========================
        # 6. Authentication & secrets
        # =========================
        (r'\b(password|passwd|pwd)\s*=\s*"[^"]+"', '[PASSWORD]'),
        (r'\b(api_key|token|secret)\s*=\s*"[^"]+"', '[SECRET]'),
        (r'-----BEGIN (?:PRIVATE|RSA|EC) KEY-----[\s\S]+?-----END (?:PRIVATE|RSA|EC) KEY-----',
         '[PRIVATE KEY]'),

        # =========================
        # 7. Security artefacts
        # =========================
        (r'\b[0-9a-fA-F]{32,64}\b', '[HASH]'),

        # =========================
        # 8. OTP / PIN
        # =========================
        (r'otp\s*=\s*"\d{4,6}"', 'otp="[PIN/OTP]"'),
        (r'pin\s*=\s*"\d{4,6}"', 'pin="[PIN/OTP]"'),

        # =========================
        # 9. SSN / foreign IDs (logs may contain them)
        # =========================
        (r'\b\d{3}-\d{2}-\d{4}\b', '[FOREIGN ID]'),
    ]

    masked = text
    for pattern, replacement in rules:
        masked = re.sub(pattern, replacement, masked, flags=re.IGNORECASE)

    return masked