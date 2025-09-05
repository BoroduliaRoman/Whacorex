from fastapi import APIRouter

from app.core.logging import logger

router = APIRouter(tags=["healthz"])


@router.get("/healthz")
def healthz() -> dict[str, str]:
    logger.info("healthz_called")
    return {"status": "ok"}
