from app.models import ProductReviewModel
from .base_service import BaseService


class ProductReviewService(BaseService):
    def __init__(self) -> None:
        super().__init__(ProductReviewModel)

    def get_review_by_product_id(self,product_id):
        return self.model.query.filter_by(product_id=product_id).all()