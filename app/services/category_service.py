from app.models import CategoryModel
from .base_service import BaseService

class CategoryService(BaseService):
    def __init__(self) -> None:
        super().__init__(CategoryModel)

    # def get_active(self):
    #     return CategoryModel.query.filter_by(is_active=True).order_by(CategoryModel.category_name).all()

    def add_category_with_products(self, products: list) -> list:
        for product in products["data"]:
            product["category_name"] = self.get_category_name_by_id(product["category_id"])
        return products
    
    def get_category_name_by_id(self,category_id):
        return CategoryModel.query.filter_by(id=category_id).first().category_name