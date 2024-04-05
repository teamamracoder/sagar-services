from db import db
from app.models import ServiceAnswerModel
from .base_service import BaseService


class ServiceAnswerService(BaseService):
    def __init__(self) -> None:
        super().__init__(ServiceAnswerModel)

    
