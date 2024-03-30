import os
import random
from db import db
from app.models import CategoryModel
from werkzeug.utils import secure_filename

class CategoryService:
    def create(self,**kwargs):
        prev_category=CategoryModel.query.filter_by(category_name=kwargs['category_name']).first()

        if prev_category is None:

            img=kwargs['category_img_url']
            num = str(random.random())
            filename = num+secure_filename(img.filename)

            custom_path = os.path.join(os.getcwd(),'app\\static\\img\\products\\')
            img.save(os.path.join(custom_path, filename))

            kwargs['category_img_url'] = filename

            category = CategoryModel(**kwargs)
            db.session.add(category)
            db.session.commit()
            return True
        return False

    def get(self):
        return CategoryModel.query.order_by(CategoryModel.id.desc()).all()



    def get_category_by_id(self,id):
        return CategoryModel.query.get(id)


    def update(self,id,**kwargs):
        category=self.get_category_by_id(id)

        img = kwargs['category_img_url']
        if img:
            num = str(random.random())
            filename = num + secure_filename(img.filename)
            print(filename)
            custom_path = os.path.join(os.getcwd(), 'app\\static\\img\\products\\')
            img.save(os.path.join(custom_path, filename))
            kwargs['category_img_url'] = filename

        else:
            del kwargs['category_img_url']

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