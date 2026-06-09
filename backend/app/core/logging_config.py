"""
Structured Logging Configuration
"""

import logging
import logging.config
from pathlib import Path

from app.core.config import settings


def setup_logging() -> logging.Logger:
    """Configure structured logging for the application."""
    
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "verbose": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            },
            "json": {
                "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
                "format": "%(asctime)s %(name)s %(levelname)s %(message)s",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "json" if settings.LOG_FORMAT == "json" else "verbose",
            },
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "filename": logs_dir / "app.log",
                "maxBytes": 10485760,
                "backupCount": 10,
                "formatter": "json" if settings.LOG_FORMAT == "json" else "verbose",
            },
            "error_file": {
                "class": "logging.handlers.RotatingFileHandler",
                "filename": logs_dir / "error.log",
                "maxBytes": 10485760,
                "backupCount": 10,
                "formatter": "json" if settings.LOG_FORMAT == "json" else "verbose",
                "level": "ERROR",
            },
        },
        "loggers": {
            "": {
                "handlers": ["console", "file", "error_file"],
                "level": settings.LOG_LEVEL,
                "propagate": True,
            },
            "uvicorn": {
                "handlers": ["console", "file"],
                "level": "INFO",
                "propagate": False,
            },
            "sqlalchemy": {
                "handlers": ["file"],
                "level": "WARNING",
                "propagate": False,
            },
        },
    }

    logging.config.dictConfig(logging_config)
    logger = logging.getLogger("app")
    logger.info(f"🔧 Logging configured - Level: {settings.LOG_LEVEL}, Format: {settings.LOG_FORMAT}")
    
    return logger