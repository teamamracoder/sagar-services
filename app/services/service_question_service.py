from db import db
from app.models import ServiceQuestionModel
from .base_service import BaseService


class ServiceQuestionService(BaseService):
    def __init__(self) -> None:
        super().__init__(ServiceQuestionModel)

    def add_answer_with_question(self, datas):
        for data in datas["data"]:
            data["question"] = self.get_question_by_id(data["question_id"])
        return datas

    def get_question_by_id(self, id):
        return ServiceQuestionModel.query.filter_by(id=id).first().question
 
        
    #         # def add_product_with_this(self, items: dict) -> dict:
    #     for item in items["data"]:
    #         item["product_name"] = self.get_product_name_by_id(item["product_id"])
    #     return items
    
    # def get_product_name_by_id(self,product_id):
    #     return ProductModel.query.filter_by(id=product_id).first().product_name
