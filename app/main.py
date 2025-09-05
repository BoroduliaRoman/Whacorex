from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

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
app.add_exception_handler(StarletteHTTPException, http_exception_holder)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)

# Reg MiddleWare
app.add_middleware(RequestIDMiddleware)
app.add_middleware(AccessLogMiddleware)

# Подключаем роутер
app.include_router(health_router)
app.include_router(assets_router)
