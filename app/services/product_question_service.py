from app.models import ProductQuestionModel
from .base_service import BaseService

class ProductQuestionService(BaseService):
    def __init__(self) -> None:
        super().__init__(ProductQuestionModel)

    def add_question_with_this(self, datas:dict)->list:
        for data in datas["data"]:
            question=self.get_question_details_by_question_id(data["question_id"])
            data["question"] = question.question
        return datas
    
    def get_question_details_by_question_id(self, question_id):
        return ProductQuestionModel.query.filter_by(id=question_id).first()