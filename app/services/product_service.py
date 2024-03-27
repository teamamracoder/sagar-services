from db import db
from app.models import ProductModel


class ProductService:
    def create(self, **kwargs):
        product = ProductModel(**kwargs)
        db.session.add(product)
        db.session.commit()
        print("in db")
        return product


    def get(self):
        return ProductModel.query.all()

    def get_by_id(self, product_id):
        return ProductModel.query.get(product_id)

    def update(self, product_id, **kwargs):
        product = self.get_by_id(product_id)
        if product:
            for key, value in kwargs.items():
                setattr(product, key, value)
            db.session.commit()
            return product
        return None

    def status(self,id):
        product = ProductModel.query.get(id)
        if not product.is_active:
            product.is_active = True
        else:
            product.is_active = False
        db.session.commit()
        return product.is_active