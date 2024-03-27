from flask import Blueprint
from app.controllers import ProductController

product_bp = Blueprint("product", __name__)
product_controller = ProductController()

@product_bp.route("/admin/products/")
def index():
    return product_controller.get()

@product_bp.route("/admin/products/add/", methods=["GET", "POST"])
def add():
    return product_controller.create()

@product_bp.route("/admin/products/update/<int:id>", methods=["GET", "POST"])
def update(id):
    return product_controller.update(id)
@product_bp.route("/admin/products/status/<int:id>", methods=["GET", "PATCH"])
def status(id):
    return product_controller.status(id)
