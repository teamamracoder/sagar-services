from db import db
from app.models import CategoryModel


class CategoryService:
    def create(self,category):
        category = CategoryModel(category_name=category, created_by=1)
        db.session.add(category)
        db.session.commit()
        return category

    def get(self):
        return CategoryModel.query.all()