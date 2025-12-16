from fastapi import FastAPI, Request
import httpx
import json
from app.sanitizer import sanitize_text
from app.config import (
    APP_NAME,
    GITHUB_COPILOT_BASE_URL,
    COPILOT_TIMEOUT_SECONDS,
)

app = FastAPI(title=APP_NAME)

@app.post("/{path:path}")
async def proxy(path: str, request: Request):
    body = await request.body()
    headers = dict(request.headers)

    try:
        body_json = json.loads(body)
    except Exception:
        body_json = None

    if body_json and "prompt" in body_json:
        body_json["prompt"] = sanitize_text(body_json["prompt"])
        body = json.dumps(body_json).encode()

    async with httpx.AsyncClient(timeout=COPILOT_TIMEOUT_SECONDS) as client:
        response = await client.request(
            method=request.method,
            url=f"{GITHUB_COPILOT_BASE_URL}/{path}",
            headers=headers,
            content=body,
        )

    return response.content, response.status_code, response.headers.items()