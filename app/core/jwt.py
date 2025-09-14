from datetime import UTC, datetime, timedelta

import jwt

from app.core.config import settings


def create_access_token(sub: str | int, expires_minutes: int | None = None) -> str:
    now = datetime.now(UTC)
    exp_minutes = expires_minutes or settings.acces_token_expire_minutes
    payload = {
        "sub": str(sub),
        "iat": int(now.timestamp()),
        "exp": int((now + timedelta(minutes=exp_minutes)).timestamp()),
    }
    return jwt.encode(payload, settings.jwt_secret, algorithm=settings.jwt_alg)


def decode_token(token: str) -> dict:
    return jwt.decode(token, settings.jwt_secret, algorithms=[settings.jwt_alg])
