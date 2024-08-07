from flask import Blueprint
from app.controllers import ProductQnAController
from flask_login import login_required
from app.constants import roles
from app.auth import role_required
product_qna_bp = Blueprint("product_qna", __name__)
product_qna_controller = ProductQnAController()

    
@product_qna_bp.route("/admin/product_qnas/")
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def index():
    return product_qna_controller.get()

@product_qna_bp.route("/admin/product_qnas/data")
def get_product_qna_data():
    return product_qna_controller.get_product_qna_data()


@product_qna_bp.route("/admin/product_qnas/add/", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def add():
    return product_qna_controller.create()


@product_qna_bp.route("/admin/product_qnas/update/<int:id>", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def update(id):
    return product_qna_controller.update(id)


@product_qna_bp.route("/admin/product_qnas/status/<int:id>", methods=["GET", "PATCH"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def status(id):
    return product_qna_controller.status(id)


# customer
@product_qna_bp.route("/product_qnas/<int:product_id>", methods=["GET","POST"])
def product_qna_create(product_id):
    return product_qna_controller.product_qna_create(product_id)
