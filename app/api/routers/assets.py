from fastapi import APIRouter

from app.schemas.asset import Asset

router = APIRouter()


@router.post("/assets", response_model=Asset)
def create_asset(asset: Asset) -> Asset:
    # Пока возвращаем то, что пришло
    return asset
