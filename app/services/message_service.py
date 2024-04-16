from db import db
from app.models import MessageModel
from .base_service import BaseService


class MessageService(BaseService):
    def __init__(self) -> None:
        super().__init__(MessageModel)

    def get_by_conversation_id(self,conversation_id:int)->dict:
        return self.model.query.filter_by(conversation_id=conversation_id).all()

    def add_attachement_url_with_this(self,messages:dict)->dict:
        prefix="../"
        for message in messages:
            message.attachement_url=self.get_by_id(message.id).attachement_url
            if message.attachement_url:
                message.attachement_url=f"{prefix}{message.attachement_url}"
        return messages
