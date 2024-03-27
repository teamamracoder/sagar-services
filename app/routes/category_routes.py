from flask import Blueprint
from app.controllers import CategoryController

category_bp = Blueprint("category_bp", __name__)
category_controller = CategoryController()


@category_bp.route("/admin/categories/")
def index():
    return category_controller.get()


@category_bp.route("/admin/categories/add/", methods=["GET", "POST"])
def add():
    return category_controller.create()
