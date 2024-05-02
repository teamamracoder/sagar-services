from app.models import ServiceQnAModel
from .base_service import BaseService


class ServiceQnAService(BaseService):
    def __init__(self) -> None:
        super().__init__(ServiceQnAModel)

    def get_qna_by_service_id(self,service_id):
        qnas= self.model.query.filter_by(service_id=service_id).all()
        # for review in reviews
            # user = user_service.get_by_id(review.user_id)
            # review['user']= user
        return qnas

    def get_check_is_qna_or_not(self, service_id, user_id):
        qnas = self.model.query.filter_by(service_id=service_id, user_id=user_id).all()

        for qna in qnas:
            if qna.service_id == service_id and qna.user_id == user_id:
                return qna
        return None
