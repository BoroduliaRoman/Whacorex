import logging
import sys

import structlog

from app.core.config import settings

LOG_LEVEL = getattr(logging, settings.log_level.upper(), logging.INFO)


def setup_logging() -> None:
    logging.basicConfig(stream=sys.stdout, level=LOG_LEVEL, format="%(message)s")

    processors = [
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.add_log_level,
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
    ]

    if settings.app_env.lower() in {"dev", "local"}:
        processors.append(structlog.dev.ConsoleRenderer())
    else:
        processors.append(structlog.processors.JSONRenderer())


logger = structlog.getLogger()
