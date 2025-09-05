from app.repositories.asset_repo import AssetRepository
from app.schemas.asset import Asset, AssetCreate


class AssetService:
    def __init__(self, repo: AssetRepository) -> None:
        self.repo = repo

    def list_assets(self) -> list[Asset]:
        return list(self.repo.list())

    def create_asset(self, payload: AssetCreate) -> Asset:
        ## Can add business rules
        return self.repo.create(payload)
