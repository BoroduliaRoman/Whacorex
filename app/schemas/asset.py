from pydantic import BaseModel, Field


class AssetBase(BaseModel):
    name: str = Field(..., description="Название Актива")
    price: float = Field(..., gt=0, description="Цена Актива (> 0)")


class AssetCreate(AssetBase):
    # Waiting something from user
    pass


class Asset(AssetBase):
    id: int = Field(..., description="ID Актива")
