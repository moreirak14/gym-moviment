from pydantic import Field

from src.schemas import CustomBaseModel


class Lead(CustomBaseModel):
    owner_id: int = Field(alias="ownerId")
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    email: str
    phone: str
