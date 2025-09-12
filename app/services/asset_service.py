from sqlalchemy.orm import Session

from app.repositories.asset import (
    create_asset,
    delete_asset,
    get_asset,
    list_assets,
    update_asset,
)
from app.schemas.asset import AssetCreate, AssetOut, AssetUpdate


class AssetService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def list_assets(self, skip: int = 0, limit: int = 100) -> list[AssetOut]:
        return list_assets(self.db, skip=skip, limit=limit)

    def create_asset(self, payload: AssetCreate) -> AssetOut:
        return create_asset(self.db, payload)

    def get_asset(self, asset_id: int) -> AssetOut | None:
        return get_asset(self.db, asset_id)

    def update_asset(self, asset_id: int, payload: AssetUpdate) -> AssetOut | None:
        return update_asset(self.db, asset_id, payload)

    def delete_asset(self, asset_id: int) -> bool:
        return delete_asset(self.db, asset_id)
