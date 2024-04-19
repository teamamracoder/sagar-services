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
    
