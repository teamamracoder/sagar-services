from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateProductReviewForm, UpdateProductReviewForm
from app.services import ProductReviewService, ProductService
from datetime import datetime

class ProductReviewController:
    def __init__(self) -> None:
        self.product_review_service = ProductReviewService()
        self.product_service = ProductService()

    def get(self):
        return render_template("admin/product_review/index.html")

    def get_product_review_data(self):
        columns = ["id", "product_id","user_id","review_title","description","rating", "created_by","created_at","updated_by","updated_by","is_active"]
        data = self.product_review_service.get(request, columns)
        combined_data = self.product_service.add_product_with_this(data)
        return jsonify(combined_data)

    def create(self):
        form = CreateProductReviewForm()
        products = self.product_service.get_active()
        form.product_id.choices = [(product.id, product.product_name) for product in products]
        if form.validate_on_submit():
            review=self.product_review_service.create(
                created_by=1,   #logged in user
                created_at=datetime.now(),
                review_title=form.review_title.data,
                description=form.description.data,
                rating=form.rating.data,
                product_id=form.product_id.data,
                user_id=1   #logged in user
            )
            return redirect(url_for("product_review.index"))
            # return render_template("admin/product_review/add.html", form=form, error="product_review already exists")
        return render_template("admin/product_review/add.html", form=form)

    def update(self, id):
        product_review = self.product_review_service.get_by_id(id)
        if product_review is None:
            return render_template("admin/error/something_went_wrong.html")
        form = UpdateProductReviewForm(obj=product_review)
        products = self.product_service.get_active()
        form.product_id.choices = [(product.id, product.product_name) for product in products]
        if form.validate_on_submit():
            updated_data = {
                'updated_at': datetime.now(),
                'updated_by': 1,    #logged in user
                'review_title': form.review_title.data,
                'description': form.description.data,
                'rating': form.rating.data,
                'product_id': form.product_id.data,
                'user_id': 1  # logged in user
            }
            self.product_review_service.update(product_review.id, **updated_data)
            return redirect(url_for("product_review.index"))
        return render_template("admin/product_review/update.html", form=form, product_review=product_review)

    def status(self, id):
        product_review = self.product_review_service.get_by_id(id)
        if product_review is None:
            return render_template("admin/error/something_went_wrong.html")
        self.product_review_service.status(id)
        return redirect(url_for("product_review.index"))