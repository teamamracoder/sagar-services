from app.models import ProductQnAModel
from .base_service import BaseService


class ProductQnAService(BaseService):
    def __init__(self) -> None:
        super().__init__(ProductQnAModel)

    def get_qna_by_product_id(self,product_id):
        return self.model.query.filter_by(product_id=product_id).all()

    def get_check_is_qna_or_not(self,product_id,user_id):
        qnas = self.model.query.filter_by(product_id=product_id,user_id=user_id).all()

        for qna in qnas:
            if qna.product_id == product_id and qna.user_id == user_id:
                return qna
        return None
