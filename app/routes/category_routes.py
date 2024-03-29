from flask import Blueprint
from flask_login import login_required
from app.constants import roles
from app.auth import role_required
from app.controllers import CategoryController

category_bp = Blueprint("category", __name__)
category_controller = CategoryController()


@category_bp.route("/admin/categories/")
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def index():
    return category_controller.get()


@category_bp.route("/admin/categories/add/", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def add():
    return category_controller.create()


@category_bp.route("/admin/categories/update/<int:id>", methods=["GET", "POST"])
def update(id):
    return category_controller.update(id)


@category_bp.route("/admin/categories/status/<int:id>", methods=["GET", "PATCH"])
def status(id):
    return category_controller.status(id)
