from flask import Blueprint
from app.controllers import ProductController
from flask_login import login_required
from app.constants import roles
from app.auth import role_required
product_bp = Blueprint("product", __name__)
product_controller = ProductController()

    
@product_bp.route("/admin/products/")
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def index():
    return product_controller.get()

@product_bp.route("/admin/products/data")
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def get_product_data():
    return product_controller.get_product_data()


@product_bp.route("/admin/products/add/", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def add():
    return product_controller.create()


@product_bp.route("/admin/products/update/<int:id>", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def update(id):
    return product_controller.update(id)


@product_bp.route("/admin/products/status/<int:id>", methods=["GET", "PATCH"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def status(id):
    return product_controller.status(id)
