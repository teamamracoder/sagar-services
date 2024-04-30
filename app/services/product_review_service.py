from app.models import ProductReviewModel
from .base_service import BaseService
from datetime import datetime, timedelta
from collections import Counter

class ProductReviewService(BaseService):
    def __init__(self) -> None:
        super().__init__(ProductReviewModel)



    def get_reviews_by_product(self, datas) -> dict:
        for data in datas["data"]:
            reviews = self.get_review_by_product_id(data["id"])
            serialized_reviews = [self.serialize_review(review) for review in reviews]
            data["product_review"] = serialized_reviews
        return datas
    def get_reviews_by_product_for_home(self, datas) -> dict:
        for data in datas:
            reviews = self.get_review_by_product_id(data["id"])
            serialized_reviews = [self.serialize_review(review) for review in reviews]
            data["product_review"] = serialized_reviews
        return datas

    def get_review_by_product_id(self,product_id):
        return self.model.query.filter_by(product_id=product_id).all()

    def serialize_review(self, review):
        return {key: getattr(review, key) for key in review.__dict__ if not key.startswith("_")}


    def get_review_by_product_ids(self,product_ids):
            products = self.model.query.filter(self.model.id.in_(product_ids)).all()

            return products

    def get_product_rating_counts(self,time_range):
        end_date = datetime.now()
        if time_range == 'Weekly':
            start_date = end_date - timedelta(days=end_date.weekday())
        elif time_range == 'Monthly':
            start_date = end_date.replace(day=1)- timedelta(days=1)
        elif time_range == 'Yearly':
            start_date = end_date.replace(month=1, day=1)
        elif time_range == 'Overall':
               start_date = None

        if start_date is not None:
            reviews = ProductReviewModel.query.filter(
                ProductReviewModel.created_at >= start_date,
                ProductReviewModel.created_at <= end_date,
                ProductReviewModel.is_active == True
            ).all()
        else:
            reviews = ProductReviewModel.query.filter(
                ProductReviewModel.is_active == True
            ).all()

        rating_counts = Counter(review.rating for review in reviews)

        ratings = []
        counts = []
        for rating, count in rating_counts.items():
            ratings.append(f'{rating} rating')
            counts.append(count)

        return {
            "rating": ratings,
            "rating_counts": counts
        }


    def get_check_is_review_or_not(self,product_id,user_id):
        reviews = self.model.query.filter_by(product_id=product_id,user_id=user_id).all()

        for review in reviews:
            if review.product_id == product_id and review.user_id == user_id:
                return review
        return None
