from app import db
from app.models import ProductReviewModel
import os
import random
from werkzeug.utils import secure_filename
from .base_service import BaseService


class ProductReviewService(BaseService):
    def __init__(self) -> None:
        super().__init__(ProductReviewModel)

    # def add_question_with_answers(self, product_answers: dict) -> dict:
    #     for product_answer in product_answers["data"]:
    #         product_answer["question"] = self.get_product_name_by_id(product_answer["question_id"])
    #     return product_answers
    #
    # def get_product_name_by_id(self,question_id):
    #     return ProductReviewModel.query.filter_by(id=question_id).first().question
    #
    # def get_active(self):
    #     return ProductReviewModel.query.filter_by(is_active=True).order_by(ProductReviewModel.question).all()