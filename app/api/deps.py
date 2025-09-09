from collections.abc import Generator
from functools import lru_cache

from app.db.session import SessionLocal
from app.repositories.asset_repo import AssetRepository
from app.services.asset_service import AssetService


@lru_cache
def get_asset_service() -> AssetService:
    # один инстанс на всё приложение (пока in-memory)
    return AssetService(AssetRepository())


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
