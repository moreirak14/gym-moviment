import logging
from typing import Type, TypeVar
from sqlalchemy.orm import Session
from src.adapters.repositories import CRUDSqlAlchemyRepository
from src.domain.user.model import User

T = TypeVar("T")
_logger = logging.getLogger(__name__)


class UserRepository(CRUDSqlAlchemyRepository):
    def __init__(self, session: Session, obj_type: Type[T], logger=_logger):
        super().__init__(session=session, obj_type=obj_type)
        self.logger = logger
        self.session = session

    def get_user_by_email(self, email: str) -> User:
        return (
            self.session.query(User)
            .filter(User.email == email)
            .first()
        )
