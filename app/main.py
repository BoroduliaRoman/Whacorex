from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(title=settings.app_name, debug=(settings.app_env == "local"))


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}
