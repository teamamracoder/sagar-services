from app.models import ProductQnAModel
from .base_service import BaseService


class ProductQnAService(BaseService):
    def __init__(self) -> None:
        super().__init__(ProductQnAModel)