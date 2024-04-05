from app.models import UserModel
from .base_service import BaseService


class UserService(BaseService):
    def __init__(self) -> None:
        super().__init__(UserModel)

    def get_user_by_email_and_password(self, email, password):
        return UserModel.query.filter_by(email=email, password=password).first()

    def add_user_with_this(self, items: dict) -> dict:
        for item in items["data"]:
            user=self.get_by_id(item["user_id"])
            item["fullname"] = user.first_name+' '+user.last_name
            item["email"] = user.email
        return items


