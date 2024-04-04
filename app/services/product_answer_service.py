from app.models import ProductAnswerModel
from .base_service import BaseService

class ProductAnswerService(BaseService):
    def __init__(self) -> None:
        super().__init__(ProductAnswerModel)

    def add_product_question_with_answer(self, qnas:list)->list:
        for qna in qnas["data"]:
            answer=self.get_answer_details_by_question_id(qna["id"])
            qna["answer"] = answer.answer
            qna["answered_by"] = answer.created_by
            qna["answered_at"] = answer.created_at
        return qnas
    
    def get_answer_details_by_question_id(self, question_id):
        return ProductAnswerModel.query.filter_by(question_id=question_id).first()
    