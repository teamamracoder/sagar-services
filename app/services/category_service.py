from db import db
from app.models import CategoryModel

class CategoryService:
    def create(self,**kwargs):
        prev_category=CategoryModel.query.filter_by(category_name=kwargs['category_name']).first()
        if prev_category is None:
            category = CategoryModel(**kwargs)
            db.session.add(category)
            db.session.commit()
            return True
        return False

    def get(self):
        return CategoryModel.query.all()

    def get_category_by_id(self,id):
        return CategoryModel.query.get(id)

    def update(self,id,**kwargs):
        category=self.get_category_by_id(id)
        for key, value in kwargs.items():
            setattr(category, key, value)
        db.session.commit()
        return category

    def status(self,id):
        category=self.get_category_by_id(id)
        if not category.is_active:
            category.is_active=True
        else:
            category.is_active=False
        db.session.commit()
        return category.is_active