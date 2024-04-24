from db import db
from app.models import ConversationModel
from .base_service import BaseService


class ConversationService(BaseService):
    def __init__(self) -> None:
        super().__init__(ConversationModel)

    def get_by_user_id(self,user_id):
        return self.model.query.filter_by(user_id=user_id).first()
    
    def get_by_user_id_json(self,user_id):
        return self.model.query.filter_by(user_id=user_id).first()

