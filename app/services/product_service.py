from app import db
from app.models import ProductModel
import os
import random
from werkzeug.utils import secure_filename
from .base_service import BaseService

class ProductService(BaseService):
    def __init__(self) -> None:
        super().__init__(ProductModel)

    def add_product_with_questions(self, product_questions: list) -> list:
        for product_question in product_questions["data"]:
            product_question["product_name"] = self.get_product_name_by_id(product_question["product_id"])
        return product_questions
    
    def get_product_name_by_id(self,product_id):
        return ProductModel.query.filter_by(id=product_id).first().product_name
    
