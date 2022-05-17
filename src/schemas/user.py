from pydantic import Field

from src.schemas import CustomBaseModel


class User(CustomBaseModel):
    email: str
    hashed_password: str = Field(alias="hashedPassword")
