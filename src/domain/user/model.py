import passlib.hash

from src.domain import BaseModelCustom


class User(BaseModelCustom):
    def __int__(
        self,
        email: str,
        hashed_password: str,
    ):
        self.email = email
        self.hashed_password = hashed_password

    def verify_password(self, password: str):
        return passlib.hash.bcrypt.verify(password, self.hashed_password)

    def as_dict(self):
        return dict(email=self.email, hashed_password=self.hashed_password)
