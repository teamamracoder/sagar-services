from flask import Blueprint, request, render_template
from app.controllers import ProductController

product_bp = Blueprint("product", __name__)
product_controller = ProductController()


@product_bp.route("/admin/product/")
def index():
    return product_controller.get()


@product_bp.route("/admin/product/add/", methods=["GET", "POST"])
def add():
    return product_controller.create()


@product_bp.route("/admin/product/edit/<int:id>", methods=["GET", "POST"])
def update(id):
    return product_controller.update(id)


@product_bp.route("/admin/product/status/<int:id>", methods=["GET", "POST"])
def status(id):
    return product_controller.status(id)


