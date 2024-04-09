from app.models import ProductReviewModel
from .base_service import BaseService


class ProductReviewService(BaseService):
    def __init__(self) -> None:
        super().__init__(ProductReviewModel)