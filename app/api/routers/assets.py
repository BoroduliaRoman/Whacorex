from fastapi import APIRouter, Depends

from app.api.deps import get_asset_service
from app.schemas.asset import Asset, AssetCreate
from app.services.asset_service import AssetService

router = APIRouter(prefix="/assets", tags=["assets"])


@router.get("/", response_model=list[Asset])
def list_assets(svc: AssetService = Depends(get_asset_service)) -> list[Asset]:
    return svc.list_assets()


@router.post("/", response_model=Asset, status_code=201)
def create_asset(
    asset: AssetCreate, svc: AssetService = Depends(get_asset_service)
) -> Asset:
    # Пока возвращаем то, что пришло
    return svc.create_asset(asset)
