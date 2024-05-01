from flask import Blueprint
from app.controllers import CategoryController
# from flask_login import login_required
from app.auth import login_required
from app.constants import roles
from app.auth import role_required
category_bp = Blueprint("category", __name__)
category_controller = CategoryController()

    
@category_bp.route("/admin/categories/")
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def index():
    return category_controller.get()

@category_bp.route("/admin/categories/data")
def get_category_data():
    return category_controller.get_category_data()


@category_bp.route("/admin/categories/add/", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def add():
    return category_controller.create()


@category_bp.route("/admin/categories/update/<int:id>", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def update(id):
    return category_controller.update(id)


# @category_bp.route("/admin/categories/status/<string:id>", methods=["GET", "PATCH"])
@category_bp.route("/admin/categories/status/<int:id>", methods=["GET", "PATCH"])
@login_required
@role_required([roles.get_key("ADMIN"), roles.get_key("STAFF")])
def status(id):
    return category_controller.status(int(id))