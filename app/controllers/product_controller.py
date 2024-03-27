from flask import render_template, redirect, url_for,request
from app.forms import CreateProductForm
from app.services import ProductService
from datetime import datetime
product_service = ProductService()



class ProductController:
    # def create(self):
    #     form = CreateProductForm()
    #     if form.validate_on_submit():
    #         product_service.create(
    #             created_by=1,
    #             created_at=datetime.now(),
    #             product_name = form.product_name.data,
    #             brand = form.brand.data,
    #             model = form.model.data,
    #             price = form.price.data,
    #             discount = form.discount.data,
    #             specifications = form.specifications.data,
    #             stock = form.stock.data,
    #             available_area_pincodes = form.available_area_pincodes.data,
    #             payment_methods = form.payment_methods.data,
    #             product_img_urls = form.product_img_urls.data,
    #             category_id = form.category_id.data,
    #             return_policy=form.return_policy.data
    #           )
    #         return redirect(url_for("product.index"))
    #     return render_template("admin/product/add.html", form=form)

    def create(self):
        if request.method == 'POST':
            form = CreateProductForm(request.form)
            if form.validate():
                product_service.create(
                    created_by=1,
                    created_at=datetime.now(),
                    product_name=form.product_name.data,
                    brand=form.brand.data,
                    model=form.model.data,
                    price=form.price.data,
                    discount=form.discount.data,
                    specifications=form.specifications.data,
                    stock=form.stock.data,
                    available_area_pincodes=form.available_area_pincodes.data,
                    payment_methods=form.payment_methods.data,
                    product_img_urls=form.product_img_urls.data,
                    category_id=form.category_id.data,
                    return_policy=form.return_policy.data
                )
                return redirect(url_for('product.index'))  # assuming product.index is your product listing page
        else:
            form = CreateProductForm()
        return render_template('admin/product/add.html', form=form)
    def get(self):
        products = product_service.get()
        return render_template("admin/product/index.html", products=products)

    def update(self, product_id):
        form = CreateProductForm()
        product = product_service.get_by_id(product_id)
        if not product:
            # Handle case where product doesn't exist
            return redirect(url_for("product.index"))
        if form.validate_on_submit():
            product_service.update(
                product_id,
                product_name=form.product_name.data,
                brand=form.brand.data,
                model=form.model.data,
                price=form.price.data,
                discount=form.discount.data,
                specifications=form.specifications.data,
                stock=form.stock.data,
                available_area_pincodes=form.available_area_pincodes.data,
                payment_methods=form.payment_methods.data,
                product_img_urls=form.product_img_urls.data,
                category_id=form.category_id.data,
                return_policy=form.return_policy.data
            )
            return redirect(url_for("product.index"))
        form.product_name.data=product.product_name
        form.brand.data=product.brand
        form.model.data=product.model
        form.price.data=product.price
        form.discount.data=product.discount
        form.specifications.data=product.specifications
        form.stock.data=product.stock
        form.available_area_pincodes.data=product.available_area_pincodes
        form.payment_methods.data=product.payment_methods
        form.product_img_urls.data=product.product_img_urls
        form.category_id.data=product.category_id
        form.return_policy.data=product.return_policy
        return render_template("admin/product/edit.html", form=form, product_id=product_id)
    
    def status(self, id):
        product_service.status(id)
        return redirect(url_for("product.index"))