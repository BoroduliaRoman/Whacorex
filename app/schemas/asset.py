from datetime import datetime

from pydantic import BaseModel, Field


class AssetBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=120, description="Название Актива")
    type: str = Field(..., min_length=1, max_length=32, description="Тип актива")


class AssetCreate(AssetBase):
    # Waiting something from user
    pass


class AssetUpdate(BaseModel):
    name: str | None = Field(
        None, min_length=1, max_length=120, description="Название Актива"
    )
    type: str | None = Field(..., min_length=1, max_length=32, description="Тип актива")


class AssetOut(AssetBase):
    id: int = Field(..., description="ID Актива")
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
