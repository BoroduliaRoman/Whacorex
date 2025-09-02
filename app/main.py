from fastapi import FastAPI
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_env: str = "local"
    port: int = 8000

    class Config:
        env_file = ".env"


settings = Settings()

app: FastAPI = FastAPI(title="Whacorex", debug=(settings.app_env == "local"))


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}
