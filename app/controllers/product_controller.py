from flask import render_template, redirect, url_for
from app.forms import CreateProductForm,UpdateProductForm
from app.services import ProductService
from datetime import datetime
product_service = ProductService()

class ProductController:

    def get(self):
        products = product_service.get()
        return render_template("admin/product/index.html", products=products)

    def create(self):
        form = CreateProductForm()
        if form.validate_on_submit():
            if product_service.create(
                created_by=1,
                created_at=datetime.now(),
                product_name=form.product_name.data,
                brand=form.brand.data,
                model=form.model.data,
                price=form.price.data,
                discount=form.discount.data,
                stock=form.stock.data,
                product_img_urls=form.product_img_urls.data,
                specifications=form.specifications.data,
                payment_methods=form.payment_methods.data,
                available_area_pincodes=form.available_area_pincodes.data,
                category_id=form.category_id.data,
                return_policy=form.return_policy.data
            ):
                return redirect(url_for("product.index"))
            return render_template("admin/product/add.html", form=form, error="Product already exists")
        return render_template("admin/product/add.html", form=form)

    def update(self, id):
        product = product_service.get_product_by_id(id)
        if not product:
            print("not found")

        form = UpdateProductForm(obj=product)
        if form.validate_on_submit():
            updated_data = {
                'category_id': form.category_id.data,
                'product_name': form.product_name.data,
                'brand': form.brand.data,
                'model': form.model.data,
                'price': form.price.data,
                'discount': form.discount.data,
                'stock': form.stock.data,
                'product_img_urls': form.product_img_urls.data,
                'specifications': form.specifications.data,
                'payment_methods': form.payment_methods.data,
                'available_area_pincodes': form.available_area_pincodes.data,
                'return_policy': form.return_policy.data,
                'updated_at': datetime.now(),
                'updated_by': 1
            }
            product_service.update_product(product, **updated_data)
            return redirect(url_for("product.index"))

        return render_template("admin/product/update.html", form=form, product=product)

    def status(self, id):
        product = product_service.get_product_by_id(id)
        if product is None:
            return render_template("admin/error/something_went_wrong.html")
        product_service.status(id)
        return redirect(url_for("product.index"))