from app.models import ProductReviewModel
from .base_service import BaseService


class ProductReviewService(BaseService):
    def __init__(self) -> None:
        super().__init__(ProductReviewModel)

 
    
    def get_reviews_by_product(self, datas) -> dict:
        for data in datas["data"]:
            reviews = self.get_review_by_product_id(data["id"])
            serialized_reviews = [self.serialize_review(review) for review in reviews]
            data["product_review"] = serialized_reviews
        return datas
    
    def get_review_by_product_id(self,product_id):
        return self.model.query.filter_by(product_id=product_id).all()
    
    def serialize_review(self, review):
        return {key: getattr(review, key) for key in review.__dict__ if not key.startswith("_")}