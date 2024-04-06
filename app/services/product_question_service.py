from app.models import ProductQuestionModel
from .base_service import BaseService

class ProductQuestionService(BaseService):
    def __init__(self) -> None:
        super().__init__(ProductQuestionModel)
