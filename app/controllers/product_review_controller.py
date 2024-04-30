from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateProductReviewForm, UpdateProductReviewForm
from app.services import ProductReviewService, ProductService, OrderService, OrderLogService
from datetime import datetime
from app.auth import get_current_user
from app.utils import FileUtils



class ProductReviewController:
    def __init__(self) -> None:
        self.product_review_service = ProductReviewService()
        self.product_service = ProductService()
        self.order_log_service = OrderLogService()
        self.order_service = OrderService()

    def get(self):
        return render_template("admin/product_review/index.html")

    def get_product_review_data(self):
        columns = ["id", "product_id","user_id","review_title","description","rating", "created_by","created_at","updated_by","updated_by","is_active"]
        data = self.product_review_service.get(request, columns)
        combined_data = self.product_service.add_product_with_this(data)
        return jsonify(combined_data)

    def create(self):
        logged_in_user,roles=get_current_user().values()
        form = CreateProductReviewForm()
        if form.validate_on_submit():
            filepath=FileUtils.save('product_reviews',form.product_review_img_urls.data)
            if isinstance(filepath,str):
                filepath=[filepath]
            self.product_review_service.create(
                created_by=logged_in_user.id,
                created_at=datetime.now(),
                review_title=form.review_title.data,
                description=form.description.data,
                rating=form.rating.data,
                product_id=form.product_id.data,
                user_id=logged_in_user.id,
                product_review_img_urls=filepath
            )
            return redirect(url_for("product_review.index"))
            # return render_template("admin/product_review/add.html", form=form, error="product_review already exists")
        return render_template("admin/product_review/add.html", form=form)

    def update(self, id):
        logged_in_user,roles=get_current_user().values()
        product_review = self.product_review_service.get_by_id(id)
        if product_review is None:
            return render_template("admin/error/something_went_wrong.html")
        form = UpdateProductReviewForm(obj=product_review)

        product = self.product_service.get_by_id(product_review.product_id)
        form.product_id.choices = [(product.id, product.product_name)]

        if form.validate_on_submit():
            updated_data = {
                'updated_at': datetime.now(),
                'updated_by': logged_in_user.id,   
                'review_title': form.review_title.data,
                'description': form.description.data,
                'rating': form.rating.data,
                'product_id': form.product_id.data,
                'user_id': logged_in_user.id
            }
            self.product_review_service.update(id, **updated_data)
            return redirect(url_for("product_review.index"))
        return render_template("admin/product_review/update.html", id=id, form=form)

    def status(self, id):
        product_review = self.product_review_service.get_by_id(id)
        if product_review is None:
            return {"status":"error","message":"Review Not Found"}
        is_active=self.product_review_service.status(id)
        if is_active:
            return {"status":"success","message":"Review Activated","data":is_active}
        return {"status":"success","message":"Review Deactivated","data":is_active}


# ********************************
    def product_review_create(self,product_id):
        logged_in_user,roles=get_current_user().values()
        reviewForm = CreateProductReviewForm()
        products=self.product_service.get_active()
        # form.product_id.choices = [(product.id, product.product_name) for product in products]
       
        if reviewForm.validate_on_submit():
            is_ordered = self.order_service.get_by_user_and_product_id(product_id, logged_in_user.id)
            is_review = self.product_review_service.get_check_is_review_or_not(product_id, logged_in_user.id)
            
            if is_ordered:
                if is_review is None:
           
                    filepath=FileUtils.save('product_reviews',reviewForm.product_review_img_urls.data)
                    if isinstance(filepath,str):
                        filepath=[filepath]
                    self.product_review_service.create(
                        created_by=logged_in_user.id,
                        created_at=datetime.now(),
                        user_id=logged_in_user.id,   
                        review_title=reviewForm.review_title.data,
                        description=reviewForm.description.data,
                        product_review_img_urls=filepath,
                        rating=reviewForm.rating.data,
                        product_id=reviewForm.product_id.data,
                    )
                    product=self.product_service.get_by_id(product_id)
                    return redirect(url_for("product.product_details_page",product_id=product_id,reviewForm=reviewForm))
                
                # If the user has already given feedback, redirect with an error message
                error_message = "Can't give any feedback! Already done..."
                return redirect(url_for("product.product_details_page", product_id=product_id, error=error_message))

            # If the service is not booked by the user, redirect with an error message
            error_message = "Can't give any feedback! Order the product first."
            return redirect(url_for("product.product_details_page", product_id=product_id, error=error_message))

            # return render_template("admin/product_review/add.html", form=form, error="product_review already exists")
        return redirect(url_for("product.product_details_page",product_id=product_id, reviewForm=reviewForm))
