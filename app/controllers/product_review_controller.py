from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateProductReviewForm, UpdateProductReviewForm
from app.services import ProductReviewService, ProductService
from datetime import datetime
from app.auth import get_current_user
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
        if form.validate_on_submit():
            review=self.product_review_service.create(
                created_by=get_current_user().id,
                created_at=datetime.now(),
                review_title=form.review_title.data,
                description=form.description.data,
                rating=form.rating.data,
                product_id=form.product_id.data,
                user_id=form.user_id.data   
            )
            return redirect(url_for("product_review.index"))
            # return render_template("admin/product_review/add.html", form=form, error="product_review already exists")
        return render_template("admin/product_review/add.html", form=form)

    def update(self, id):
        product_review = self.product_review_service.get_by_id(id)
        if product_review is None:
            return render_template("admin/error/something_went_wrong.html")
        form = UpdateProductReviewForm(obj=product_review)
        if form.validate_on_submit():
            updated_data = {
                'updated_at': datetime.now(),
                'updated_by': get_current_user().id,   
                'review_title': form.review_title.data,
                'description': form.description.data,
                'rating': form.rating.data,
                'product_id': form.product_id.data,
                'user_id': form.user_id.data 
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