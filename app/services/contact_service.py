from db import db
from app.models import ContactModel
from .base_service import BaseService

class ContactService(BaseService):
    def __init__(self) -> None:
        super().__init__(ContactModel)

    # def get_user_by_email_and_password(self, email, password):
    #     return ContactModel.query.filter_by(email=email, password=password).first()



