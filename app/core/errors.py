from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from starlette import status
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.core.logging import logger


# 1) Любые HTTP-ошибки (включая 404)
async def http_exception_holder(request: Request, exc: StarletteHTTPException):
    logger.warning(
        "http_error",
        path=str(request.url),
        method=request.method,
        status_code=exc.status_code,
        detail=exc.detail,
    )
    return JSONResponse(status_code=exc.status_code, content={"error": exc.detail})


# 2) Ошибки валидации входных данных (422)
async def validation_exception_handler(
    request: Request, exc: RequestValidationError | ValidationError
):
    logger.info(
        "validation_error",
        path=str(request.url),
        method=request.method,
        errors=getattr(exc, "errors", lambda: [])(),
    )
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"error": "Validation error", "details": exc.errors()},
    )


# 3) Любая непойманная ошибка (500)
async def unhandled_exception_handler(request: Request, exc: Exception):
    logger.error(
        "unhandled_error",
        path=str(request.url),
        method=request.method,
        exc_info=exc,
    )
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"error": "Internal Server Error"},
    )
