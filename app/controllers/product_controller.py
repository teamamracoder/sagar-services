from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateProductForm,UpdateProductForm
from app.services import ProductService
from app.services import CategoryService
from datetime import datetime
from app.constants import payment_methods

class ProductController:
    def __init__(self) -> None:
        self.product_service = ProductService()
        self.category_service = CategoryService()

    def get(self):
        return render_template("admin/product/index.html")

    def get_product_data(self):
        columns = ["id", "product_name", "brand","model","price","stock","created_by","created_at","updated_by", "updated_at", "is_active", "category_id"]
        data = self.product_service.get(request, columns)
        combined_data = self.category_service.add_category_with_products(data)
        return jsonify(combined_data)
    
    def create(self):
        form = CreateProductForm()
        categories=self.category_service.get_active()
        form.category_id.choices = [(category.id, category.category_name) for category in categories]
        form.payment_methods.choices = payment_methods.get_all_items()

        if form.validate_on_submit():
            pincode_string = form.available_area_pincodes.data
            pincode_list = [pin.strip() for pin in pincode_string.split(',')]
            self.product_service.create(
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
                available_area_pincodes=pincode_list,
                category_id=form.category_id.data,
                return_policy=form.return_policy.data
            )
            return redirect(url_for("product.index"))
            # return render_template("admin/product/add.html", form=form, error="Product already exists")
        return render_template("admin/product/add.html", form=form)

    def update(self, id):
        product = self.product_service.get_by_id(id)
        if product is None:
            return render_template("admin/error/something_went_wrong.html")

        categories=self.category_service.get_active()
        form = UpdateProductForm(obj=product)
        form.category_id.choices = [(category.id, category.category_name) for category in categories]
        form.payment_methods.choices = payment_methods.get_all_items()
        if form.validate_on_submit():
            pincode_string = form.available_area_pincodes.data
            pincode_list = [pin.strip() for pin in pincode_string.split(',')]
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
                'available_area_pincodes': pincode_list,
                'return_policy': form.return_policy.data,
                'updated_at': datetime.now(),
                'updated_by': 1
            }
            self.product_service.update(product.id, **updated_data)
            return redirect(url_for("product.index"))
        
        form.available_area_pincodes.data = ', '.join(product.available_area_pincodes)
        return render_template("admin/product/update.html", form=form, product=product)

    def status(self, id):
        product = self.product_service.get_by_id(id)
        if product is None:
            return render_template("admin/error/something_went_wrong.html")
        self.product_service.status(id)
        return redirect(url_for("product.index"))

    def get_total_price(self):
        price_calculated_data=self.product_service.get_total_price(request)
        return jsonify(price_calculated_data)