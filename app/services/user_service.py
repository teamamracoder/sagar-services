from db import db
from app.models import UserModel
from .base_service import BaseService


class UserService(BaseService):
    def __init__(self) -> None:
        super().__init__(UserModel)

    def get_user_by_email_and_password(self, email, password):
        return UserModel.query.filter_by(email=email, password=password).first()
