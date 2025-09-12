from collections.abc import Generator

from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.services.asset_service import AssetService


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_asset_service(db: Session = Depends(get_db())) -> AssetService:
    # сервис использует БД-CRUD (app/repositories/asset.py)
    return AssetService(db)
