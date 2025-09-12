from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.db.models.asset import Asset
from app.schemas.asset import AssetCreate, AssetUpdate


def create_asset(db: Session, data: AssetCreate) -> Asset:
    obj = Asset(name=data.name, type=data.type)
    db.add(obj)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ValueError("asset with this name already exists")
    db.refresh(obj)
    return obj


def get_asset(db: Session, asset_id: int) -> Asset | None:
    return db.get(Asset, asset_id)


def list_assets(db: Session, skip: int = 0, limit: int = 100) -> Asset | None:
    stmt = select(Asset).offset(skip).limit(limit)
    return db.execute(stmt).scalars().all()


def update_asset(db: Session, asset_id: int, data: AssetUpdate) -> Asset | None:
    obj = db.get(Asset, asset_id)
    if not obj:
        return None
    if data.name is not None:
        obj.name = data.name
    if data.type is not None:
        obj.type = data.type
    db.commit()
    db.refresh(obj)
    return obj


def delete_asset(db: Session, asset_id: int) -> bool:
    obj = db.get(Asset, asset_id)
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True
