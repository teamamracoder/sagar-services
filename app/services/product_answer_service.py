from app import db
from app.models import ProductAnswerModel
import os
import random
from werkzeug.utils import secure_filename
from .base_service import BaseService

class ProductAnswerService(BaseService):
    def __init__(self) -> None:
        super().__init__(ProductAnswerModel)

    def add_product_question_with_answer(self, qnas:list)->list:
        for qna in qnas["data"]:
            qna["answer_id"] = self.get_answer_id_by_question_id(qna["id"])
            qna["answer"] = self.get_answer_by_question_id(qna["id"])
            qna["answered_by"] = self.get_answered_by_by_question_id(qna["id"])
            qna["answered_at"] = self.get_answered_at_by_question_id(qna["id"])
        return qnas
    
    def get_answer_id_by_question_id(self,question_id):
        product_answer=ProductAnswerModel.query.filter_by(question_id=question_id).first()
        if product_answer:
            return product_answer.id
        else:
            return None
        
    def get_answer_by_question_id(self,question_id):
        product_answer=ProductAnswerModel.query.filter_by(question_id=question_id).first()
        if product_answer:
            return product_answer.answer
        else:
            return ""
    
    def get_answered_by_by_question_id(self,question_id):
        product_answer=ProductAnswerModel.query.filter_by(question_id=question_id).first()
        if product_answer:
            return product_answer.staff_id
        else:
            return None
    
    def get_answered_at_by_question_id(self,question_id):
        product_answer=ProductAnswerModel.query.filter_by(question_id=question_id).first()
        if product_answer:
            return product_answer.created_at
        else:
            return None
    
