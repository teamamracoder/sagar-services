from db import db
from app.models import ConversationModel
from .base_service import BaseService


class ConversationService(BaseService):
    def __init__(self) -> None:
        super().__init__(ConversationModel)

