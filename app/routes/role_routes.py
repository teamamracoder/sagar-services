from flask import Blueprint
from flask_login import login_required
from app.auth import role_required
from app.controllers import RoleController
from app.constants import roles

role_bp = Blueprint("role_bp", __name__)
role_controller = RoleController()


@role_bp.route("/admin/roles/")
@login_required
@role_required([1, 2])
def index():
    return role_controller.get()


@role_bp.route("/admin/roles/data")
def get_role_data():
    return role_controller.get_role_data()


@role_bp.route("/admin/roles/add/", methods=["GET", "POST"])
@login_required
@role_required([1])
def add():
    return role_controller.create()
