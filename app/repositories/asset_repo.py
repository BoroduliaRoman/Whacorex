from collections.abc import Iterable

from app.schemas.asset import Asset, AssetCreate


class AssetRepository:
    def __init__(self) -> None:
        self._data: dict[int, Asset] = {}
        self._seq: int = 0

    def list(self) -> Iterable[Asset]:
        return self._data.values()

    def create(self, payload: AssetCreate) -> Asset:
        self._seq += 1
        item = Asset(id=self._seq, name=payload.name, price=payload.price)
        self._data[self._seq] = item
        return item
