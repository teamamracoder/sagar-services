from db import db
from app.models import MessageModel
from .base_service import BaseService


class MessageService(BaseService):
    def __init__(self) -> None:
        super().__init__(MessageModel)

