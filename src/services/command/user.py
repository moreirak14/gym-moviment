import logging

from src.schemas.lead import LeadSchema
from src.services.uow import SqlAlchemyUnitOfWork
from src.domain.lead.model import Lead

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
            phone=lead_data.phone)

    def create(self, data: LeadSchema):
        with self.uow:
            if not data:
                return

            self._build_lead(data)
            self.uow.commit()

        return {"message": "Usuario criado com sucesso."}
