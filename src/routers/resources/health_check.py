from fastapi.routing import APIRouter

from src.schemas.health_check import Message
from src.services.query.health_check import HealthCheckServiceQuery, StatusCheck
from src.services.uow import SqlAlchemyUnitOfWork

health_check_route = APIRouter(prefix="/health-check", tags=["Health Check"])


@health_check_route.get("/health-check")
def health_check():
    status = {"application": StatusCheck.UP.value}
    check_database = HealthCheckServiceQuery(
        uow=SqlAlchemyUnitOfWork()
    ).status_check_database()
    status.update(check_database)

    return Message(**status)
