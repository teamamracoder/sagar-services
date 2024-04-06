from app.models import ProductAnswerModel
from .base_service import BaseService

class ProductAnswerService(BaseService):
    def __init__(self) -> None:
        super().__init__(ProductAnswerModel)

    def add_answer_with_this(self, datas:list)->list:
        for data in datas["data"]:
            answer=self.get_answer_details_by_question_id(data["id"])
            data["answer"] = answer.answer if answer else ""
            data["answered_by"] = answer.staff_id if answer else None
        return datas
    
    def get_answer_details_by_question_id(self, question_id):
        return ProductAnswerModel.query.filter_by(question_id=question_id).first()
    