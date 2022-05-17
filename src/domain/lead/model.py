from src.domain import BaseModelCustom


class Lead(BaseModelCustom):
    def __int__(
            self,
            first_name: str,
            last_name: str,
            email: str,
            phone: str,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

    def as_dict(self):
        return dict(
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            phone=self.phone,
        )