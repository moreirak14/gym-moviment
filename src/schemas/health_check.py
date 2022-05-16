from pydantic import BaseModel


class Message(BaseModel):
    database: str
    application: str
