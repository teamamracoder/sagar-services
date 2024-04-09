from flask import Blueprint
from flask_login import login_required
from app.auth import role_required
from app.controllers import RoleController
from app.constants import roles

role_bp = Blueprint("role", __name__)
role_controller = RoleController()


@role_bp.route("/admin/roles/add/<int:role_key>/<int:user_id>", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN")])
def add(role_key,user_id):
    return role_controller.create(role_key,user_id)

@role_bp.route("/admin/roles/status/<int:id>", methods=["GET", "POST"])
@login_required
@role_required([roles.get_key("ADMIN")])
def status(id):
    return role_controller.status(id)
