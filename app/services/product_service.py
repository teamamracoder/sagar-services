from app import db
from app.models import ProductModel
import os
import random
from werkzeug.utils import secure_filename
class ProductService:
    def get(self):
        return ProductModel.query.all()
    def create(self, **kwargs):
        prev_product = ProductModel.query.filter_by(product_name=kwargs['product_name']).first()
        if prev_product is None:
            img_urls=kwargs['product_img_urls']
            new_img_urls = []
            for img_url in img_urls:
                if img_url:
                    print(type(img_url))
                    num = str(random.random())
                    filename = num + secure_filename(img_url.filename)

                    custom_path = os.path.join(os.getcwd(), 'app\\static\\img\\products\\')
                    img_url.save(os.path.join(custom_path, filename))

                    new_img_urls.append(filename)

            kwargs['product_img_urls'] = new_img_urls

            product = ProductModel(**kwargs)
            db.session.add(product)
            db.session.commit()
            return True
        return False

    def get_product_by_id(self, product_id):
        return ProductModel.query.get(product_id)

    def update_product(self, product, **kwargs):
        existing_img_urls = product.product_img_urls
        img_urls = kwargs['product_img_urls']
        new_img_urls = []
        for img_url in img_urls:
            print(img_url)
            print(type(img_url))
            if img_url:
                num = str(random.random())
                filename = num + secure_filename(img_url.filename)

                custom_path = os.path.join(os.getcwd(), 'app\\static\\img\\products\\')
                img_url.save(os.path.join(custom_path, filename))

                new_img_urls.append(filename)

        existing_img_urls.extend(new_img_urls)
        kwargs['product_img_urls']=existing_img_urls

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
