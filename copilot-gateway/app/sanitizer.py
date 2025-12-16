import re

def sanitize_text(text: str) -> str:
    rules = [
        (r'name\s*=\s*"[^"]+"', 'name="[FULL NAME]"'),
        (r'\b(?:Mr|Ms|Mrs|Dr)\.?\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+\b', '[FULL NAME]'),

        (r'\b\d{12}\b', '[IC NUMBER]'),
        (r'\b[A-Za-z]\d{7}\b', '[PASSPORT NUMBER]'),
        (r'\bD\d{9,12}\b', '[DRIVER LICENSE]'),

        (r'\b(?:\d{4}[-\s]?){3,4}\b', '[CARD NUMBER]'),
        (r'\b\d{10,20}\b', '[ACCOUNT NUMBER]'),
        (r'\bTX\d+\b', '[TRANSACTION ID]'),

        (r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', '[EMAIL]'),
        (r'\b01\d{8,9}\b', '[PHONE NUMBER]'),
        (r'\b\d{5}\b', '[POSTAL CODE]'),
        (r'\b(?:\d{1,3}\.){3}\d{1,3}\b', '[IP ADDRESS]'),

        (r'\b\d{2}/\d{2}/\d{4}\b', '[DATE]'),
        (r'\b\d{4}-\d{2}-\d{2}\b', '[DATE]'),

        (r'\b(password|passwd|pwd)\s*=\s*"[^"]+"', '[PASSWORD]'),
        (r'\b(api_key|token|secret)\s*=\s*"[^"]+"', '[SECRET]'),

        (r'-----BEGIN (?:PRIVATE|RSA|EC) KEY-----[\s\S]+?-----END (?:PRIVATE|RSA|EC) KEY-----',
         '[PRIVATE KEY]'),

        (r'\b[0-9a-fA-F]{32,64}\b', '[HASH]'),

        (r'otp\s*=\s*"\d{4,6}"', 'otp="[PIN/OTP]"'),
        (r'pin\s*=\s*"\d{4,6}"', 'pin="[PIN/OTP]"'),

        (r'\b\d{3}-\d{2}-\d{4}\b', '[FOREIGN ID]'),
    ]

    masked = text
    for pattern, replacement in rules:
        masked = re.sub(pattern, replacement, masked, flags=re.IGNORECASE)

    return masked