from app.models import ServiceReviewModel
from .base_service import BaseService


class ServiceReviewService(BaseService):
    def __init__(self) -> None:
        super().__init__(ServiceReviewModel)

    def get_review_by_service_id(self,service_id):
        reviews= self.model.query.filter_by(service_id=service_id).all()
        
        # for review in reviews
            # user = user_service.get_by_id(review.user_id)
            # review['user']= user
        return reviews

    def get_reviews_by_service_for_home(self, datas) -> dict:
        for data in datas:
            reviews = self.get_review_by_service_id(data["id"])
            serialized_reviews = [self.serialize_review(review) for review in reviews]
            data["service_review"] = serialized_reviews
        return datas

    def serialize_review(self, review):
        return {key: getattr(review, key) for key in review.__dict__ if not key.startswith("_")}

    def get_check_is_review_or_not(self, service_id, user_id):
        reviews = self.model.query.filter_by(service_id=service_id, user_id=user_id).all()

        for review in reviews:
            if review.service_id == service_id and review.user_id == user_id:
                return review
        return None


