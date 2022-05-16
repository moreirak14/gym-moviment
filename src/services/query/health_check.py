import logging
from enum import Enum
from typing import Dict

from src.services.uow import SqlAlchemyUnitOfWork

_logger = logging.getLogger(__name__)


class StatusCheck(Enum):
    UP = "UP"
    DOWN = "DOWN"


class HealthCheckServiceQuery:
    def __init__(self, uow: SqlAlchemyUnitOfWork, logger=_logger):
        self.uow = uow
        self.logger = logger

    def status_check_database(self) -> Dict:
        with self.uow:
            try:
                self.uow.session.execute("SELECT 1")
                self.logger.info(f"Service database is {StatusCheck.UP.value}")
            except Exception as error:
                self.logger.exception(error)
                return {"Service database is": StatusCheck.DOWN.value}
        return {"database": StatusCheck.UP.value}
