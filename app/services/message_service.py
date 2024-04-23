from db import db
from app.models import MessageModel
from .base_service import BaseService


class MessageService(BaseService):
    def __init__(self) -> None:
        super().__init__(MessageModel)

    def get_by_conversation_id(self,conversation_id:int)->dict:
        return self.model.query.filter_by(conversation_id=conversation_id).order_by(self.model.id).all()

    def add_attachement_url_with_this(self,messages:dict)->dict:
        for message in messages:
            message.attachement_url=self.get_by_id(message.id).attachement_url
        return messages
    
    def get_by_conversation_id_json(self, conversation_id, columns):
        query = self.model.query.filter_by(conversation_id=conversation_id, is_active = True).order_by(self.model.id).all()
        data = [{key: getattr(item, key) if key != 'created_at' else getattr(item, key).strftime("%Y-%m-%d %H:%M:%S") for key in columns} for item in query]
        return  data
