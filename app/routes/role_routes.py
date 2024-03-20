from flask import Blueprint

from app.controllers import RoleController

role_bp = Blueprint("role_bp", __name__)
role_controller = RoleController()


@role_bp.route("/admin/roles/")
def index():
    return role_controller.get()


@role_bp.route("/admin/roles/add/", methods=["GET", "POST"])
def add():
    return role_controller.create()
