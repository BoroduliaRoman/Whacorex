from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "whacorex"
    app_env: str = "dev"
    log_level: str = "INFO"

    jwt_secret: str = "change_me"
    jwt_alg: str = "HS256"
    acces_token_expire_minutes: int = 60

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
