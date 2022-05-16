import logging

from fastapi import FastAPI

from config import settings
from src.commons.logger import setup_logger
from src.routers.v1 import router

setup_logger()
logger = logging.getLogger(__name__)


def get_app() -> FastAPI:
    app = FastAPI(
        title=settings.REST_APPLICATION_NAME,
        description=settings.REST_APPLICATION_DESCRIPTION,
        openapi_url="/api/openapi.json",
    )

    app.include_router(router)

    @app.get("/favicon.ico")
    async def root():
        return {"message": "Application Running"}

    return app


if __name__ == "__main__":
    import uvicorn

    logger.info("Starting application...")
    log_dict_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": "%(asctime)s [%(process)d] [%(name)s] [%(levelname)s] %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            }
        },
        "handlers": {
            "default": {
                "level": settings.REST_APPLICATION_LOG_LEVEL.upper(),
                "formatter": "standard",
                "class": "logging.StreamHandler",
            },
        },
        "loggers": {
            "": {
                "handlers": ["default"],
                "level": settings.REST_APPLICATION_LOG_LEVEL.upper(),
                "propagate": False,
            },
        },
    }
    uvicorn.run(
        "main:get_app",
        workers=settings.REST_APPLICATION_WORKERS,
        host=settings.REST_APPLICATION_HOST,
        port=settings.REST_APPLICATION_PORT,
        reload=settings.REST_APPLICATION_RELOAD,
        log_level=settings.REST_APPLICATION_LOG_LEVEL.lower(),
        log_config=log_dict_config,
        factory=True,
    )
