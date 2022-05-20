class InvalidBase(Exception):
    public_message: str


class UserAlreadyExists(InvalidBase):
    public_message = "Dados bancários já existe na base"
