from app import db
from app.models import ProductModel

class ProductService:
    def get(self):
        return ProductModel.query.all()
    def create(self, **kwargs):
        prev_product = ProductModel.query.filter_by(product_name=kwargs['product_name']).first()
        if prev_product is None:
            product = ProductModel(**kwargs)
            db.session.add(product)
            db.session.commit()
            return True
        return False

    def get_product_by_id(self, product_id):
        return ProductModel.query.get(product_id)

    def update_product(self, product, **kwargs):
        for key, value in kwargs.items():
            setattr(product, key, value)
        db.session.commit()

    def status(self,id):
        product=self.get_product_by_id(id)
        if not product.is_active:
            product.is_active=True
        else:
            product.is_active=False
        db.session.commit()
        return product.is_active
