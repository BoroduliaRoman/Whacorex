from pydantic import BaseModel, Field


class Asset(BaseModel):
    id: int = Field(..., description="ID Актива")
    name: str = Field(..., description="Название Актива")
    price: float = Field(..., gt=0, description="Цена Актива (> 0)")
