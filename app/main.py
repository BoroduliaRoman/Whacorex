from collections.abc import Awaitable, Callable
from typing import cast

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.responses import Response

from app.api.routers import db_check
from app.api.routers.assets import router as assets_router
from app.api.routers.health import router as health_router
from app.core.config import settings
from app.core.errors import (
    http_exception_holder,
    unhandled_exception_handler,
    validation_exception_handler,
)
from app.core.logging import setup_logging
from app.core.middleware import AccessLogMiddleware, RequestIDMiddleware

setup_logging()

app = FastAPI(title=settings.app_name, debug=(settings.app_env == "local"))

# Reg Errors Exceptions
app.add_exception_handler(
    StarletteHTTPException,
    cast(
        Callable[[Request, Exception], Response | Awaitable[Response]],
        http_exception_holder,
    ),
)
app.add_exception_handler(
    RequestValidationError,
    cast(
        Callable[[Request, Exception], Response | Awaitable[Response]],
        validation_exception_handler,
    ),
)
app.add_exception_handler(
    Exception,
    cast(
        Callable[[Request, Exception], Response | Awaitable[Response]],
        unhandled_exception_handler,
    ),
)

# Reg MiddleWare
app.add_middleware(RequestIDMiddleware)
app.add_middleware(AccessLogMiddleware)

# Подключаем роутер
app.include_router(health_router)
app.include_router(assets_router)
app.include_router(db_check.router)
