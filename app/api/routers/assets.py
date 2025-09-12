from fastapi import APIRouter, Depends, HTTPException, status

from app.api.deps import get_asset_service
from app.schemas.asset import AssetCreate, AssetOut, AssetUpdate
from app.services.asset_service import AssetService

router = APIRouter(prefix="/assets", tags=["assets"])


@router.get("", response_model=list[AssetOut])
def list_assets(
    skip: int = 0, limit: int = 100, svc: AssetService = Depends(get_asset_service)
):
    return svc.list_assets(skip=skip, limit=limit)


@router.post("", response_model=AssetOut, status_code=status.HTTP_201_CREATED)
def create_asset(payload: AssetCreate, svc: AssetService = Depends(get_asset_service)):
    try:
        return svc.create_asset(payload)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))


@router.get("/{asset_id}", response_model=AssetOut)
def get_asset(asset_id: int, svc: AssetService = Depends(get_asset_service)):
    obj = svc.get_asset(asset_id)
    if not obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Asset not found"
        )
    return obj


@router.patch("/{asset_id}", response_model=AssetOut)
def update_asset(
    asset_id: int, payload: AssetUpdate, svc: AssetService = Depends(get_asset_service)
):
    obj = svc.update_asset(asset_id, payload)
    if not obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Asset not found"
        )
    return obj


@router.delete("/{asset_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_assets(asset_id: int, svc: AssetService = Depends(get_asset_service)):
    ok = svc.delete_asset(asset_id)
    if not ok:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Asset not fount"
        )
    return None
