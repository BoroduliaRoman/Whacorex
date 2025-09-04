from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.core.config import settings
from app.core.errors import (
    http_exception_holder,
    unhandled_exception_handler,
    validation_exception_handler,
)
from app.core.logging import logger, setup_logging

setup_logging()

app = FastAPI(title=settings.app_name, debug=(settings.app_env == "local"))

# Reg Errors Exceptions
app.add_exception_handler(StarletteHTTPException, http_exception_holder)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)


@app.get("/healthz")
def healthz() -> dict[str, str]:
    logger.info("healthz_called")
    return {"status": "ok"}


@app.get("/echo")
def echo(n: int) -> dict[str, int]:
    return {"n": n}
