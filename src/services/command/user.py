import logging

import passlib.hash

from src.domain.exceptions import UserAlreadyExists
from src.domain.lead.model import Lead
from src.domain.user.model import User
from src.schemas.lead import LeadSchema
from src.schemas.user import UserSchema
from src.services.uow import SqlAlchemyUnitOfWork

_logger = logging.getLogger(__name__)


class UserServiceCommand:
    def __init__(self, uow: SqlAlchemyUnitOfWork, logger=_logger):
        self.logger = logger
        self.uow = uow

    def _build_lead(self, lead_data: Lead):
        self.logger.debug(f"[Create Lead] - Data inserted: {lead_data.dict()}")
        return Lead(
            first_name=lead_data.first_name,
            last_name=lead_data.last_name,
            email=lead_data.email,
            phone=lead_data.phone,
        )

    def _build_user(self, user_data: UserSchema):
        self.logger.debug(f"[Create User] - Data inserted: {user_data.dict()}")
        return User(
            email=user_data.email,
            hashed_password=passlib.hash.bcrypt.hash(user_data.hashed_password),
        )

    def create_lead(self, data: LeadSchema):
        with self.uow:
            if not data:
                return

            self._build_lead(data)
            self.uow.commit()

        return {"message": "Usuario criado com sucesso."}

    def create_user(self, data: User):
        with self.uow:
            if not data:
                return

            if self.uow.user.get_user_by_email(data.email):
                raise UserAlreadyExists

            self._build_user(data)
            self.uow.commit()

        return {"message": "Usuario criado com sucesso."}
