from flask import Blueprint
from app.controllers import ProductReviewController
from flask_login import login_required
from app.constants import roles
from app.auth import role_required
product_review_bp = Blueprint("product_review", __name__)
product_review_controller = ProductReviewController()

    
@product_review_bp.route("/admin/product_reviews/")
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def index():
    return product_review_controller.get()

@product_review_bp.route("/admin/product_reviews/data")
def get_product_review_data():
    return product_review_controller.get_product_review_data()


@product_review_bp.route("/admin/product_reviews/add/", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def add():
    return product_review_controller.create()


# @product_review_bp.route("/admin/product_reviews/update/<int:id>", methods=["GET", "POST"])
# @login_required
# @role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
# def update(id):
#     return product_review_controller.update(id)


@product_review_bp.route("/admin/product_reviews/status/<int:id>", methods=["GET", "PATCH"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def status(id):
    return product_review_controller.status(id)



# **************
@product_review_bp.route("/product_reviews/<int:product_id>", methods=["GET", "POST"])
def product_review_create(product_id):
    return product_review_controller.product_review_create(product_id)
