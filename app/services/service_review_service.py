from app.models import ServiceReviewModel
from .base_service import BaseService


class ServiceReviewService(BaseService):
    def __init__(self) -> None:
        super().__init__(ServiceReviewModel)

    def get_review_by_service_id(self,service_id):
        return self.model.query.filter_by(service_id=service_id).all()


    def service_review_create(self, **kwargs):
        review = self.model(**kwargs)
        db.session.add(review)
        db.session.commit()
        return review