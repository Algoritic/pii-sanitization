import os

# =========================
# Core service configuration
# =========================

APP_NAME = "copilot-security-gateway"
APP_ENV = os.getenv("APP_ENV", "local")

HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "3333"))

# =========================
# GitHub Copilot settings
# =========================

# Official Copilot API endpoint
GITHUB_COPILOT_BASE_URL = os.getenv(
    "GITHUB_COPILOT_BASE_URL",
    "https://api.githubcopilot.com"
)

# Timeout when calling Copilot
COPILOT_TIMEOUT_SECONDS = int(
    os.getenv("COPILOT_TIMEOUT_SECONDS", "60")
)

# =========================
# Security & compliance
# =========================

# Log only sanitized prompts (never raw)
LOG_SANITIZED_ONLY = os.getenv("LOG_SANITIZED_ONLY", "true").lower() == "true"

# If true, block request if PII is detected (future enhancement)
BLOCK_ON_PII = os.getenv("BLOCK_ON_PII", "false").lower() == "true"

# =========================
# Observability (optional)
# =========================

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")