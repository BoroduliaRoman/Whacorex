from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import setup_logging

setup_logging()

app = FastAPI(title=settings.app_name, debug=(settings.app_env == "local"))


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}
