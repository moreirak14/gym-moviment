import logging

from fastapi import APIRouter, HTTPException, status
from starlette.responses import JSONResponse

from src.domain.exceptions import InvalidBase
from src.schemas.user import UserSchema
from src.services.command.user import UserServiceCommand
from src.services.uow import SqlAlchemyUnitOfWork

user_route = APIRouter(prefix="/users", tags=["Create Users"])
logger = logging.getLogger(__name__)


@user_route.post("/create/", status_code=status.HTTP_201_CREATED)
def post_users(data: UserSchema):
    logger.info("Creating user!")

    try:
        user_service = UserServiceCommand(SqlAlchemyUnitOfWork())
        user_details = user_service.create_user(data)
        return JSONResponse(content=dict(detail=user_details))
    except InvalidBase as error:
        raise HTTPException(
            status_code=400, detail=dict(message=str(error.public_message))
        ) from error

    except Exception as error:
        logger.exception(f"Error: {error}")
        return HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=dict(message="Ocorreu um erro ao criar usuario"),
        )
