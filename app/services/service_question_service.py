from app.models import ServiceQuestionModel
from .base_service import BaseService


class ServiceQuestionService(BaseService):
    def __init__(self) -> None:
        super().__init__(ServiceQuestionModel)