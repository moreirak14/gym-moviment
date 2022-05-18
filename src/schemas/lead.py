from pydantic import Field

from src.schemas import CustomBaseModel


class LeadSchema(CustomBaseModel):
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    email: str
    phone: str
